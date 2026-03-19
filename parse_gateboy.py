#!/usr/bin/env python3
"""
GateBoy PPU Combinatorial Path Analysis — Parser & Graph Builder

Extracts a signal dependency graph from the GateBoy gate-level simulator source.
Identifies registered (clocked) vs combinatorial nodes and builds a directed graph
suitable for critical path analysis.

Key design decisions:
- Wire/triwire local variables are scoped by source file ("file_stem:WIRE_NAME")
  because 726+ wire names appear in multiple files. Without scoping, the last
  definition wins and cross-file edges silently connect to the wrong node.
- Nodes from reg_new paths (DFF updates, gate assigns, bus writes, sig_in/sig_out)
  are global since their names come from unique state struct field names.
- Computed methods (GateBoyState.cpp, GateBoyCpuBus.cpp, GateBoyPins.cpp) are
  parsed as gate chains with the method name as a global combinatorial node.
"""

import re
import json
import sys
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional

# ============================================================================
# Configuration
# ============================================================================

GATEBOY_SRC = Path("metroboy/src/GateBoyLib")

# Files to parse — all gate logic files (PPU + system integration)
GATE_FILES = [
    "GateBoy.cpp",           # Main tock_gates() — bulk of the logic
    "GateBoyLCD.cpp",        # LY, LYC match, LCD timing
    "GateBoyPixPipe.cpp",    # Pixel pipelines, window logic
    "GateBoyTileFetcher.cpp",
    "GateBoySpriteFetcher.cpp",
    "GateBoySpriteScanner.cpp",
    "GateBoySpriteStore.cpp",
    "GateBoyRegisters.cpp",  # LCDC, STAT, palette regs
    "GateBoyClocks.cpp",     # Clock generation
    "GateBoyDMA.cpp",        # DMA (shares OAM bus)
    "GateBoyInterrupts.cpp", # STAT/VBlank interrupts
    "GateBoyCpuBus.cpp",     # CPU bus, bootrom
    "GateBoyVramBus.cpp",    # VRAM bus
    "GateBoyOamBus.cpp",     # OAM bus
    "GateBoyTimer.cpp",      # DIV, TIMA
    "GateBoyReset.cpp",      # Reset logic
    "GateBoyJoypad.cpp",     # Joypad (minimal PPU relevance)
    "GateBoySerial.cpp",     # Serial (minimal PPU relevance)
    "GateBoyExtBus.cpp",     # External bus
    "GateBoyPins.cpp",       # Pin logic
]

# Additional files with computed methods (parsed separately)
COMPUTED_METHOD_FILES = [
    "GateBoyState.cpp",
    "GateBoyCpuBus.cpp",
    "GateBoyPins.cpp",
]

# Gate functions — these are combinatorial
GATE_FUNCTIONS = {
    "not1", "and2", "and3", "and4", "and5", "and6", "and7",
    "or2", "or3", "or4", "or5", "or6",
    "nor2", "nor3", "nor4", "nor5", "nor6", "nor8",
    "nand2", "nand3", "nand4", "nand5", "nand6", "nand7",
    "xor2", "xnor2",
    "mux2p", "mux2n",
    "amux2", "amux3", "amux4", "amux6",
    "and_or3", "or_and3", "not_or_and3",
    "add3",
    "tri6_nn", "tri6_pn", "tri10_np", "tri_pp",
}

# DFF/latch methods — these indicate registered (clocked) elements
REGISTERED_METHODS = {
    "dff", "dff8", "dff9", "dff11", "dff13",
    "dff17", "dff17_any", "dff17_clk", "dff17_rst",
    "dff20", "dff20_any", "dff20_clk", "dff20_async",
    "dff22", "dff22_any", "dff22_sync", "dff22_async",
    "dff_r", "dff_pp",
    "nor_latch", "nand_latch",
    "tp_latchn", "tp_latchp",
}

# Bus methods
BUS_METHODS = {"tri_bus"}

# Signal output accessors — map back to registered source
OUTPUT_ACCESSORS = {
    "qp_old", "qn_old", "qp_new", "qn_new",
    "qp_mid", "qn_mid", "qp_any", "qn_any",
    "out_old", "out_new", "out_any", "out_mid",
    "qp_int_old", "qp_int_new", "qp_int_any",
    "qp_ext_old", "qp_ext_new", "qn_ext_new",
}

# Methods to skip when matching computed method calls
SKIP_METHODS = (
    REGISTERED_METHODS | BUS_METHODS |
    {'hold', 'sig_in', 'sig_out', 'set_data', 'set_addr', 'pin_in',
     'pin_out', 'pin_io', 'pin_io_any', 'pin_clk', 'rst', 'set',
     'clkgood_new', 'clkgood_old', 'clk_new', 'clk_old',
     'reset', 'poweron', 'check_old', 'check_new'}
)


# ============================================================================
# Data structures
# ============================================================================

@dataclass
class Node:
    name: str                          # Signal name (e.g., PALY_LY_MATCHa_old)
    node_type: str                     # "combinatorial", "registered", "bus", "boundary", "gate_output"
    reg_type: str = ""                 # DFF type if registered (dff9, dff17, etc.)
    source_file: str = ""
    source_line: int = 0
    gate_func: str = ""                # Gate function if combinatorial (not1, and2, etc.)
    state_path: str = ""               # Full path in GateBoyState if applicable
    comment: str = ""                  # Die page reference comment
    display_name: str = ""             # Short name for display (without file scope prefix)


@dataclass
class Edge:
    src: str    # source signal name
    dst: str    # destination signal name
    edge_type: str = "data"  # "data", "clock", "reset", "set"


@dataclass
class ParseResult:
    nodes: dict = field(default_factory=dict)   # name -> Node
    edges: list = field(default_factory=list)    # list of Edge
    # Maps bare wire name -> set of scoped names (file_stem:WIRE_NAME)
    wire_scopes: dict = field(default_factory=lambda: {})
    # Set of global node names (registered, gate_output, bus, boundary, computed methods)
    global_names: set = field(default_factory=set)
    # Set of known computed method names (from GateBoyState, GateBoyCpuABus, PinsSys)
    computed_methods: set = field(default_factory=set)


# ============================================================================
# Scoping helpers
# ============================================================================

def file_stem(fname: str) -> str:
    """Get file stem for scoping: 'GateBoy.cpp' -> 'GateBoy'."""
    return Path(fname).stem


def scoped_name(fname: str, wire_name: str) -> str:
    """Create a file-scoped wire name: 'GateBoy:AVOR_SYS_RSTp'."""
    return f"{file_stem(fname)}:{wire_name}"


def display_name_from_scoped(name: str) -> str:
    """Strip file scope prefix for display: 'GateBoy:AVOR_SYS_RSTp' -> 'AVOR_SYS_RSTp'."""
    if ':' in name:
        return name.split(':', 1)[1]
    return name


def register_scoped_wire(result: ParseResult, fname: str, wire_name: str):
    """Register a wire name in the scope tracking structures."""
    sname = scoped_name(fname, wire_name)
    if wire_name not in result.wire_scopes:
        result.wire_scopes[wire_name] = set()
    result.wire_scopes[wire_name].add(sname)


# ============================================================================
# Parsing
# ============================================================================

def extract_comment(line: str) -> str:
    """Extract the die-page comment like /*#p21.MUWY*/ from a line."""
    m = re.match(r'\s*/\*[#_]?(p\d+\.\w+)\*/', line)
    return m.group(1) if m else ""


def extract_state_path(expr: str) -> str:
    """Extract a state path like 'reg_ly.MUWY_LY0p_odd' from reg_old/reg_new references."""
    # Match reg_old.xxx.yyy.accessor() or reg_new.xxx.yyy.accessor()
    m = re.search(r'reg_(?:old|new)\.(.+?)\.(?:' + '|'.join(OUTPUT_ACCESSORS) + r')\(\)', expr)
    if m:
        return m.group(1)
    # Match reg_new.xxx.yyy.method(...)  (for DFF calls)
    m = re.search(r'reg_new\.(.+?)\.(?:' + '|'.join(REGISTERED_METHODS | BUS_METHODS) + r')\(', expr)
    if m:
        return m.group(1)
    # Match reg_new.xxx.yyy <<= ...
    m = re.search(r'reg_new\.(.+?)\s*<<=', expr)
    if m:
        return m.group(1)
    return ""


def extract_signal_refs(expr: str, result: ParseResult = None) -> list:
    """Extract all signal references from an expression.

    Returns list of (signal_name, is_registered_read, temporal_phase) tuples.

    When is_registered_read=True and temporal_phase="old", this represents a read
    from the previous tick -- a clock boundary. The edge should come from a
    special "@old" boundary node, not the current-tick computation.
    """
    refs = []

    # Track which parts of the expression are already matched by reg_old/reg_new
    # patterns so we don't double-count them in the local wire pattern
    matched_spans = []

    # Pattern 1: reg_old.path.accessor() -- reading a registered output from previous phase
    for m in re.finditer(
        r'reg_old\.(.+?)\.(' + '|'.join(OUTPUT_ACCESSORS) + r')\(\)',
        expr
    ):
        path = m.group(1)
        parts = path.split('.')
        sig_name = parts[-1]
        refs.append((sig_name, True, "old"))
        matched_spans.append(m.span())

    # Pattern 2: reg_new.path.accessor() -- reading a registered/gate output from current phase
    for m in re.finditer(
        r'reg_new\.(.+?)\.(' + '|'.join(OUTPUT_ACCESSORS) + r')\(\)',
        expr
    ):
        path = m.group(1)
        parts = path.split('.')
        sig_name = parts[-1]
        refs.append((sig_name, True, "new"))
        matched_spans.append(m.span())

    # Pattern 2b: reg_new.path.method_name() -- calling a computed method
    # e.g. reg_new.XAPO_VID_RSTn_new(), reg_new.cpu_abus.SYRO_FE00_FFFF_new()
    for m in re.finditer(
        r'reg_new\.(.+?)\b(\w+)\(\)',
        expr
    ):
        full_path = m.group(1) + m.group(2)
        method_name = m.group(2)
        # Skip if this is an accessor we already matched
        if method_name in OUTPUT_ACCESSORS:
            continue
        # Skip DFF/latch methods and other non-signal methods
        if method_name in SKIP_METHODS:
            continue
        # This is a computed method call -- reference the global method node
        refs.append((method_name, True, "new"))
        matched_spans.append(m.span())

    # Pattern 2c: pins.sys.method_name() -- calling PinsSys computed methods
    # e.g. pins.sys.UCOB_CLKBADp_new(), pins.sys.UPOJ_MODE_PRODn_new()
    for m in re.finditer(
        r'pins\.sys\.(\w+)\(\)',
        expr
    ):
        method_name = m.group(1)
        if method_name in OUTPUT_ACCESSORS | SKIP_METHODS:
            continue
        refs.append((method_name, True, "new"))
        matched_spans.append(m.span())

    # Pattern 2d: pins.sys.FIELD.accessor() -- reading a pin register
    # e.g. pins.sys.PIN_71_RST.qp_int_new(), pins.sys.PIN_74_CLK.clkgood_new()
    for m in re.finditer(
        r'pins\.sys\.(\w+)\.(' + '|'.join(OUTPUT_ACCESSORS) + r'|clkgood_new|clkgood_old|clk_new|clk_old)\(\)',
        expr
    ):
        sig_name = m.group(1)
        accessor = m.group(2)
        phase = "old" if accessor.endswith("_old") else "new"
        refs.append((sig_name, True, phase))
        matched_spans.append(m.span())

    # Pattern 2e: Direct or nested member access FIELD.accessor() -- used inside computed
    # methods where `this->` members are accessed without reg_new prefix.
    # Handles both one-level (BUS_CPU_A15p.out_new()) and two-level
    # (sys_rst.AFER_SYS_RSTp.qp_new(), reg_lcdc.XONA_LCDC_LCDENp.qp_new())
    accessor_pat = '|'.join(OUTPUT_ACCESSORS) + r'|clkgood_new|clkgood_old|clk_new|clk_old'
    # Two-level: struct.FIELD.accessor()
    for m in re.finditer(
        r'\b(\w+)\.(\w+)\.(' + accessor_pat + r')\(\)',
        expr
    ):
        struct_name = m.group(1)
        field_name = m.group(2)
        accessor = m.group(3)
        # Skip if already matched
        in_matched = False
        for start, end in matched_spans:
            if start <= m.start() < end:
                in_matched = True
                break
        if in_matched:
            continue
        if struct_name in ('reg_old', 'reg_new', 'pins'):
            continue
        phase = "old" if accessor.endswith("_old") else "new"
        refs.append((field_name, True, phase))
        matched_spans.append(m.span())

    # One-level: FIELD.accessor() -- only at word boundary, not after a dot
    for m in re.finditer(
        r'(?<!\.)(\b\w+)\.(' + accessor_pat + r')\(\)',
        expr
    ):
        field_name = m.group(1)
        accessor = m.group(2)
        # Skip if already matched by any previous pattern
        in_matched = False
        for start, end in matched_spans:
            if start <= m.start() < end:
                in_matched = True
                break
        if in_matched:
            continue
        # Skip struct names
        if field_name in ('reg_old', 'reg_new', 'pins', 'sys'):
            continue
        phase = "old" if accessor.endswith("_old") else "new"
        refs.append((field_name, True, phase))
        matched_spans.append(m.span())

    # Pattern 3: Local wire references -- just variable names that match known signal patterns
    for m in re.finditer(r'\b([A-Z][A-Z0-9]{3,}_\w+)\b', expr):
        candidate = m.group(1)
        pos = m.start()

        # Skip if this position was already matched by a reg_old/reg_new pattern
        in_matched = False
        for start, end in matched_spans:
            if start <= pos < end:
                in_matched = True
                break
        if in_matched:
            continue

        # Skip things that are clearly not signals
        if candidate.startswith(('BIT_', 'TRI_', 'DELTA_', 'SIM_', 'CHECK_', 'LOG_')):
            continue
        if candidate in ('BIT_DATA', 'BIT_CLOCK', 'BIT_DRIVEN', 'BIT_PULLED',
                         'BIT_OLD', 'BIT_NEW', 'TRI_DRIVEN', 'TRI_NEW'):
            continue
        refs.append((candidate, False, None))

    return refs


def add_edge_for_ref(ref_name: str, is_reg: bool, phase: str, dst_name: str,
                     result: ParseResult, file: str, lineno: int):
    """Add an edge from a signal reference to a destination node.

    For reg_old reads (phase="old"), creates a boundary node representing
    the clock-edge output. This prevents false combinatorial cycles across
    temporal boundaries.
    """
    if ref_name == dst_name:
        return  # no self-loops

    if is_reg and phase == "old":
        # This is a read from the previous tick. Create a boundary node
        # named "SIGNAL@old" that represents the registered output.
        # The combinatorial path terminates here.
        boundary_name = f"{ref_name}@old"
        if boundary_name not in result.nodes:
            result.nodes[boundary_name] = Node(
                name=boundary_name,
                display_name=f"{ref_name}@old",
                node_type="registered",  # acts as path terminator
                reg_type="clock_boundary",
                source_file=file,
                source_line=lineno,
                state_path=f"reg_old.{ref_name}",
                comment=f"Clock boundary read of {ref_name}",
            )
            result.global_names.add(boundary_name)
        result.edges.append(Edge(src=boundary_name, dst=dst_name))
    else:
        result.edges.append(Edge(src=ref_name, dst=dst_name))


def parse_wire_assignment(line: str, file: str, lineno: int, result: ParseResult):
    """Parse: wire NAME = gate_func(args...) or wire NAME = expr

    Wire/triwire local variables are scoped by file to avoid collisions
    when the same wire name appears in multiple files.
    """
    # Match wire declarations with gate function calls
    m = re.match(
        r'\s*(?:/\*[^*]*\*/\s*)?(?:wire|triwire)\s+(\w+)\s*=\s*(.+?)\s*;',
        line
    )
    if not m:
        return False

    bare_name = m.group(1)
    expr = m.group(2)
    comment = extract_comment(line)

    # Scope the wire name by file
    name = scoped_name(file, bare_name)
    register_scoped_wire(result, file, bare_name)

    # Determine the gate function
    gate_func = ""
    for gf in GATE_FUNCTIONS:
        if re.search(rf'\b{gf}\s*\(', expr):
            gate_func = gf
            break

    # Also check for Adder (add3 returns struct)
    if 'add3(' in expr:
        gate_func = "add3"

    node = Node(
        name=name,
        display_name=bare_name,
        node_type="combinatorial",
        source_file=file,
        source_line=lineno,
        gate_func=gate_func,
        comment=comment,
    )
    result.nodes[name] = node

    # Extract dependencies from the expression
    refs = extract_signal_refs(expr, result)
    for ref_name, is_reg, phase in refs:
        add_edge_for_ref(ref_name, is_reg, phase, name, result, file, lineno)

    return True


def parse_reg_update(line: str, file: str, lineno: int, result: ParseResult):
    """Parse: reg_new.path.dffXX(args...) -- registered element update."""
    m = re.match(
        r'\s*(?:/\*[^*]*\*/\s*)?reg_new\.(.+?)\.(' + '|'.join(REGISTERED_METHODS) + r')\s*\((.+?)\)\s*;',
        line
    )
    if not m:
        return False

    path = m.group(1)
    method = m.group(2)
    args_str = m.group(3)
    comment = extract_comment(line)

    parts = path.split('.')
    sig_name = parts[-1]

    node = Node(
        name=sig_name,
        display_name=sig_name,
        node_type="registered",
        reg_type=method,
        state_path=path,
        source_file=file,
        source_line=lineno,
        comment=comment,
    )
    result.nodes[sig_name] = node
    result.global_names.add(sig_name)

    # Parse arguments -- typically (CLK, RST, D) or (CLK, D) or (SET, RST) etc.
    # All arguments are dependencies
    refs = extract_signal_refs(args_str, result)
    for ref_name, is_reg, phase in refs:
        add_edge_for_ref(ref_name, is_reg, phase, sig_name, result, file, lineno)

    return True


def parse_gate_assign(line: str, file: str, lineno: int, result: ParseResult):
    """Parse: reg_new.path <<= expr -- Gate type assignment (combinatorial stored in state)."""
    m = re.match(
        r'\s*(?:/\*[^*]*\*/\s*)?reg_new\.(.+?)\s*<<=\s*(.+?)\s*;',
        line
    )
    if not m:
        return False

    path = m.group(1)
    expr = m.group(2)
    comment = extract_comment(line)

    parts = path.split('.')
    sig_name = parts[-1]

    gate_func = ""
    for gf in GATE_FUNCTIONS:
        if re.search(rf'\b{gf}\s*\(', expr):
            gate_func = gf
            break

    node = Node(
        name=sig_name,
        display_name=sig_name,
        node_type="gate_output",  # combinatorial but stored in state
        state_path=path,
        source_file=file,
        source_line=lineno,
        gate_func=gate_func,
        comment=comment,
    )
    result.nodes[sig_name] = node
    result.global_names.add(sig_name)

    refs = extract_signal_refs(expr, result)
    for ref_name, is_reg, phase in refs:
        add_edge_for_ref(ref_name, is_reg, phase, sig_name, result, file, lineno)

    return True


def parse_bus_write(line: str, file: str, lineno: int, result: ParseResult):
    """Parse: reg_new.path.tri_bus(triwire_name) -- bus write."""
    m = re.match(
        r'\s*(?:/\*[^*]*\*/\s*)?reg_new\.(.+?)\.tri_bus\s*\((.+?)\)\s*;',
        line
    )
    if not m:
        return False

    path = m.group(1)
    args_str = m.group(2)
    comment = extract_comment(line)

    parts = path.split('.')
    sig_name = parts[-1]

    # Only create the node if not already defined
    if sig_name not in result.nodes:
        node = Node(
            name=sig_name,
            display_name=sig_name,
            node_type="bus",
            state_path=path,
            source_file=file,
            source_line=lineno,
            comment=comment,
        )
        result.nodes[sig_name] = node
        result.global_names.add(sig_name)

    refs = extract_signal_refs(args_str, result)
    for ref_name, is_reg, phase in refs:
        add_edge_for_ref(ref_name, is_reg, phase, sig_name, result, file, lineno)

    return True


def parse_sig_assign(line: str, file: str, lineno: int, result: ParseResult):
    """Parse: reg_new.path.sig_in(expr) or sig_out(expr) -- boundary signals."""
    m = re.match(
        r'\s*(?:/\*[^*]*\*/\s*)?reg_new\.(.+?)\.(sig_in|sig_out)\s*\((.+?)\)\s*;',
        line
    )
    if not m:
        return False

    path = m.group(1)
    method = m.group(2)
    args_str = m.group(3)
    comment = extract_comment(line)

    parts = path.split('.')
    sig_name = parts[-1]

    node = Node(
        name=sig_name,
        display_name=sig_name,
        node_type="boundary",
        state_path=path,
        source_file=file,
        source_line=lineno,
        comment=comment,
    )
    result.nodes[sig_name] = node
    result.global_names.add(sig_name)

    refs = extract_signal_refs(args_str, result)
    for ref_name, is_reg, phase in refs:
        add_edge_for_ref(ref_name, is_reg, phase, sig_name, result, file, lineno)

    return True


def parse_hold(line: str, file: str, lineno: int, result: ParseResult):
    """Parse: reg_new.path.hold() -- hold current value."""
    m = re.match(
        r'\s*(?:/\*[^*]*\*/\s*)?reg_new\.(.+?)\.hold\s*\(\)\s*;',
        line
    )
    if not m:
        return False
    # Just note the node exists -- hold doesn't create new dependencies
    return True


def parse_file(filepath: Path, result: ParseResult):
    """Parse a single GateBoy source file."""
    if not filepath.exists():
        print(f"  [SKIP] {filepath.name} -- not found")
        return

    text = filepath.read_text()
    lines = text.split('\n')
    fname = filepath.name

    parsed = 0

    # Join continuation lines (lines ending with a comma or opening paren
    # followed by more args on the next line)
    joined_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        orig_lineno = i + 1

        # Detect multi-line statements: line has unbalanced parens
        open_count = line.count('(') - line.count(')')
        while open_count > 0 and i + 1 < len(lines):
            i += 1
            line += ' ' + lines[i].strip()
            open_count = line.count('(') - line.count(')')

        joined_lines.append((line, orig_lineno))
        i += 1

    for line, lineno in joined_lines:
        # Skip comments, preprocessor, blank lines
        stripped = line.strip()
        if not stripped or stripped.startswith('//') or stripped.startswith('#'):
            continue
        # Skip lines that are inside comments
        if stripped.startswith('/*') and '*/' not in stripped:
            continue

        if parse_wire_assignment(line, fname, lineno, result):
            parsed += 1
        elif parse_reg_update(line, fname, lineno, result):
            parsed += 1
        elif parse_gate_assign(line, fname, lineno, result):
            parsed += 1
        elif parse_bus_write(line, fname, lineno, result):
            parsed += 1
        elif parse_sig_assign(line, fname, lineno, result):
            parsed += 1
        elif parse_hold(line, fname, lineno, result):
            parsed += 1

    print(f"  {fname}: {parsed} statements parsed")


# ============================================================================
# Computed method parsing
# ============================================================================

def parse_computed_methods(filepath: Path, result: ParseResult):
    """Parse computed methods from GateBoyState.cpp, GateBoyCpuBus.cpp, GateBoyPins.cpp.

    These files define methods like:
        wire GateBoyState::XAPO_VID_RSTn_new() const { ... }
        wire GateBoyCpuABus::TUNA_0000_FDFF_new() const { ... }
        wire PinsSys::UCOB_CLKBADp_new() const { ... }

    The method name becomes a global combinatorial node. Internal wires are
    scoped to the source file. References to other computed methods create
    edges to those global nodes.
    """
    if not filepath.exists():
        print(f"  [SKIP] {filepath.name} -- not found")
        return

    text = filepath.read_text()
    fname = filepath.name
    parsed = 0

    # Pattern for method declarations (both _new and _old variants)
    # Matches: wire ClassName::MethodName() const { ... }
    # Handle both single-line and multi-line method bodies
    method_pattern = re.compile(
        r'(?:/\*[^*]*\*/\s*)?wire\s+\w+::(\w+)\s*\(\)\s*const\s*\{',
    )

    pos = 0
    while pos < len(text):
        m = method_pattern.search(text, pos)
        if not m:
            break

        method_name = m.group(1)
        body_start = m.end()

        # Find the matching closing brace
        brace_depth = 1
        i = body_start
        while i < len(text) and brace_depth > 0:
            if text[i] == '{':
                brace_depth += 1
            elif text[i] == '}':
                brace_depth -= 1
            i += 1

        body = text[body_start:i - 1]  # exclude the closing brace
        lineno = text[:m.start()].count('\n') + 1

        pos = i  # advance past this method

        # Skip _old and _any variants -- we only care about _new for current-tick analysis
        # But also parse _old methods from PinsSys since they are called from other files
        # Actually, we should parse all of them since they may be referenced
        # Skip non-signal methods
        if method_name in ('reset', 'poweron', 'check_old', 'check_new'):
            continue

        # Determine the gate function from the return expression or last wire assignment
        gate_func = ""
        for gf in GATE_FUNCTIONS:
            if re.search(rf'\b{gf}\s*\(', body):
                gate_func = gf
                break

        # Create the global method node
        node = Node(
            name=method_name,
            display_name=method_name,
            node_type="combinatorial",
            source_file=fname,
            source_line=lineno,
            gate_func=gate_func,
            comment="",
        )
        result.nodes[method_name] = node
        result.global_names.add(method_name)
        result.computed_methods.add(method_name)

        # Parse internal wire declarations within the method body
        # These are scoped to the file
        internal_wires = []
        for wm in re.finditer(
            r'(?:/\*[^*]*\*/\s*)?(?:wire|triwire)\s+(\w+)\s*=\s*(.+?)\s*;',
            body
        ):
            wire_name = wm.group(1)
            wire_expr = wm.group(2)

            sname = scoped_name(fname, wire_name)
            register_scoped_wire(result, fname, wire_name)

            wire_gate_func = ""
            for gf in GATE_FUNCTIONS:
                if re.search(rf'\b{gf}\s*\(', wire_expr):
                    wire_gate_func = gf
                    break

            wire_node = Node(
                name=sname,
                display_name=wire_name,
                node_type="combinatorial",
                source_file=fname,
                source_line=lineno,
                gate_func=wire_gate_func,
                comment=extract_comment(wm.group(0)),
            )
            result.nodes[sname] = wire_node
            internal_wires.append((sname, wire_name, wire_expr))

            # Parse dependencies of this internal wire
            refs = extract_signal_refs(wire_expr, result)
            for ref_name, is_reg, phase in refs:
                add_edge_for_ref(ref_name, is_reg, phase, sname, result, fname, lineno)

        # Parse the return statement to connect internal wires to the method node.
        # If the return variable has the same name as the method, merge them:
        # replace the method node with the scoped wire (avoids double-counting).
        ret_match = re.search(r'return\s+(\w+)\s*;', body)
        if ret_match:
            ret_var = ret_match.group(1)
            ret_scoped = scoped_name(fname, ret_var)
            if ret_var == method_name and ret_scoped in result.nodes:
                # The internal wire IS the method output. Promote the scoped wire
                # to be the global method node instead of having two separate nodes.
                scoped_node = result.nodes[ret_scoped]
                # Remove the scoped wire node
                del result.nodes[ret_scoped]
                # Update the method node with the scoped wire's attributes
                result.nodes[method_name].gate_func = scoped_node.gate_func
                result.nodes[method_name].comment = scoped_node.comment
                # Redirect all edges that pointed to/from the scoped wire
                for edge in result.edges:
                    if edge.src == ret_scoped:
                        edge.src = method_name
                    if edge.dst == ret_scoped:
                        edge.dst = method_name
                # Remove from wire_scopes
                if ret_var in result.wire_scopes:
                    result.wire_scopes[ret_var].discard(ret_scoped)
            elif ret_scoped in result.nodes:
                result.edges.append(Edge(src=ret_scoped, dst=method_name))
            elif ret_var in result.nodes:
                result.edges.append(Edge(src=ret_var, dst=method_name))

        # If there are no internal wires (simple return of a function call),
        # parse dependencies directly on the method body
        if not internal_wires:
            refs = extract_signal_refs(body, result)
            for ref_name, is_reg, phase in refs:
                add_edge_for_ref(ref_name, is_reg, phase, method_name, result, fname, lineno)

        # Also handle calls to other computed methods within the body
        # e.g. XAPO_VID_RSTn_new() called as a bare function (within same class)
        for cm in re.finditer(r'\b(\w+_(?:new|old))\(\)', body):
            callee = cm.group(1)
            if callee == method_name:
                continue  # skip self
            if callee in OUTPUT_ACCESSORS | SKIP_METHODS:
                continue
            # Check if this is inside a wire assignment expression we already parsed
            # If so, the dependency is already captured via the wire's refs
            already_handled = False
            for sname, wire_name, wire_expr in internal_wires:
                if callee + '()' in wire_expr:
                    already_handled = True
                    break
            if not already_handled:
                # Direct method call not in a wire assignment -- connect to method node
                result.edges.append(Edge(src=callee, dst=method_name))

        # Handle member references like sys_rst.AFER_SYS_RSTp.qp_new() within method bodies
        # These resolve to registered elements. Already handled by extract_signal_refs
        # via the pattern matching on field.accessor() -- but we need to handle
        # the case where these are on `this` members (no reg_new prefix).
        for rm in re.finditer(
            r'(\w+)\.(\w+)\.(' + '|'.join(OUTPUT_ACCESSORS) + r'|clkgood_new|clkgood_old|clk_new|clk_old)\(\)',
            body
        ):
            struct_name = rm.group(1)
            field_name = rm.group(2)
            accessor = rm.group(3)
            # Skip if this was already matched inside a wire expression
            if struct_name in ('reg_old', 'reg_new', 'pins'):
                continue
            phase = "old" if accessor.endswith("_old") else "new"
            # field_name is the registered element
            # Find which internal wire (or method) this belongs to
            rm_start = rm.start()
            target = method_name  # default: edge to the method node
            for sname, wire_name, wire_expr in internal_wires:
                if field_name in wire_expr:
                    target = sname
                    break
            add_edge_for_ref(field_name, True, phase, target, result, fname, lineno)

        parsed += 1

    if parsed > 0:
        print(f"  {fname}: {parsed} computed methods parsed")


# ============================================================================
# Edge resolution with file scoping
# ============================================================================

def resolve_scoped_edges(result: ParseResult):
    """Resolve edges considering file-scoped wire names.

    For each edge, if the source is a bare wire name (not already scoped):
    1. If it exists as a global node, use it directly
    2. If it exists as a scoped wire in the same file as the destination, use that
    3. If it exists as a scoped wire in exactly one file, use that
    4. Otherwise, mark as unresolved

    For destination nodes, they are already resolved (scoped during parse).
    """
    known = set(result.nodes.keys())
    unknown_refs = set()

    resolved_edges = []
    seen = set()

    for edge in result.edges:
        src = edge.src
        dst = edge.dst

        # Resolve source if it's a bare name
        resolved_src = _resolve_ref(src, dst, result, known)

        if resolved_src is None:
            unknown_refs.add(src)
            continue

        key = (resolved_src, dst)
        if key in seen:
            continue
        seen.add(key)

        if resolved_src == dst:
            continue  # no self-loops

        resolved_edges.append(Edge(src=resolved_src, dst=dst, edge_type=edge.edge_type))

    result.edges = resolved_edges
    return unknown_refs


def _resolve_ref(src: str, dst: str, result: ParseResult, known: set) -> Optional[str]:
    """Resolve a signal reference to a known node name.

    Returns the resolved node name, or None if unresolvable.
    """
    # Already a known node (global or scoped)
    if src in known:
        return src

    # Check if src is a bare wire name that needs scoping
    if src in result.wire_scopes:
        scoped_candidates = result.wire_scopes[src]

        # Try same-file scope first: if dst is scoped, use the same file
        if ':' in dst:
            dst_stem = dst.split(':')[0]
            same_file = f"{dst_stem}:{src}"
            if same_file in scoped_candidates and same_file in known:
                return same_file
        else:
            # dst is a global name -- check its source file
            dst_node = result.nodes.get(dst)
            if dst_node and dst_node.source_file:
                dst_stem = file_stem(dst_node.source_file)
                same_file = f"{dst_stem}:{src}"
                if same_file in scoped_candidates and same_file in known:
                    return same_file

        # If only one scope exists, use it
        valid = [s for s in scoped_candidates if s in known]
        if len(valid) == 1:
            return valid[0]

        # If multiple scopes exist, we cannot disambiguate -- use any
        # This is a best-effort fallback; ideally all should be resolved above
        if valid:
            return valid[0]

    # Check if it's a computed method name
    if src in result.computed_methods and src in known:
        return src

    return None


def classify_gate_outputs(result: ParseResult):
    """Gate outputs (type 'gate_output') are combinatorial -- they just happen to be
    stored in state for cross-function visibility. For path analysis they should be
    treated as combinatorial (path continues through them)."""
    for node in result.nodes.values():
        if node.node_type == "gate_output":
            node.node_type = "combinatorial"


# ============================================================================
# Graph construction
# ============================================================================

def build_graph(result: ParseResult):
    """Build a networkx DiGraph from parsed results."""
    import networkx as nx

    G = nx.DiGraph()

    for name, node in result.nodes.items():
        G.add_node(name,
            node_type=node.node_type,
            reg_type=node.reg_type,
            source_file=node.source_file,
            source_line=node.source_line,
            gate_func=node.gate_func,
            state_path=node.state_path,
            comment=node.comment,
            display_name=node.display_name or display_name_from_scoped(name),
        )

    for edge in result.edges:
        if edge.src in G and edge.dst in G:
            G.add_edge(edge.src, edge.dst, edge_type=edge.edge_type)

    return G


def is_path_terminator(G, node):
    """Check if a node is a path terminator (registered, bus, or boundary)."""
    return G.nodes[node].get('node_type') in ('registered', 'bus', 'boundary')


def find_all_cycles(G):
    """Find all simple cycles, grouped by whether they pass through registered nodes."""
    import networkx as nx

    cycles = []
    try:
        # Find up to 100 cycles
        count = 0
        for cycle in nx.simple_cycles(G):
            cycles.append(cycle)
            count += 1
            if count >= 100:
                break
    except Exception:
        pass

    # Classify cycles
    feedback_cycles = []  # cycles through async set/reset of DFFs
    pure_comb_cycles = []  # cycles entirely in combinatorial logic (problematic)

    for cycle in cycles:
        has_reg = any(is_path_terminator(G, n) for n in cycle)
        if has_reg:
            feedback_cycles.append(cycle)
        else:
            pure_comb_cycles.append(cycle)

    return feedback_cycles, pure_comb_cycles


def build_dag_for_analysis(G):
    """Build a DAG suitable for critical path analysis.

    Removes edges that enter registered/bus/boundary nodes from combinatorial nodes
    when those registered nodes also have outgoing edges to combinatorial nodes.
    This breaks feedback cycles while preserving the combinatorial path structure.

    Returns a new graph where edges OUT of registered nodes are kept (they're sources)
    and edges INTO registered nodes are kept (they're sinks), but the registered nodes
    themselves act as path terminators.
    """
    import networkx as nx

    DAG = G.copy()

    # Find and break all cycles by removing back-edges found during DFS
    # We iteratively remove edges until the graph is acyclic
    removed_edges = []
    while True:
        try:
            cycle_edges = nx.find_cycle(DAG)
            # Remove the last edge in the cycle (arbitrary but consistent)
            edge = cycle_edges[-1]
            DAG.remove_edge(edge[0], edge[1])
            removed_edges.append((edge[0], edge[1]))
        except nx.NetworkXNoCycle:
            break

    return DAG, removed_edges


def graph_stats(G) -> dict:
    """Compute basic graph statistics."""
    import networkx as nx

    node_types = {}
    for _, data in G.nodes(data=True):
        t = data.get('node_type', 'unknown')
        node_types[t] = node_types.get(t, 0) + 1

    # Check for cycles
    has_cycles = False
    cycle_sample = []
    try:
        cycle = nx.find_cycle(G)
        has_cycles = True
        cycle_sample = [(str(e[0]), str(e[1])) for e in cycle[:10]]
    except nx.NetworkXNoCycle:
        pass

    n_components = nx.number_weakly_connected_components(G)

    reg_nodes = [n for n, d in G.nodes(data=True)
                 if d.get('node_type') in ('registered', 'bus', 'boundary')]
    comb_nodes = [n for n, d in G.nodes(data=True)
                  if d.get('node_type') == 'combinatorial']

    return {
        "total_nodes": G.number_of_nodes(),
        "total_edges": G.number_of_edges(),
        "node_types": node_types,
        "registered_nodes": len(reg_nodes),
        "combinatorial_nodes": len(comb_nodes),
        "weakly_connected_components": n_components,
        "has_cycles": has_cycles,
        "cycle_sample": cycle_sample,
    }


# ============================================================================
# Critical Path Analysis
# ============================================================================

def find_critical_paths(DAG, G_original):
    """Find the longest combinatorial paths between registered nodes.

    For each node, computes the longest path from any registered source
    through combinatorial logic to any registered sink.

    Returns sorted list of (depth, path) tuples.
    """
    import networkx as nx

    # Topological sort the DAG
    try:
        topo_order = list(nx.topological_sort(DAG))
    except nx.NetworkXUnfeasible:
        print("ERROR: DAG still has cycles after cycle-breaking!")
        return []

    # For each node, compute the longest path TO it from any registered source,
    # counting only combinatorial gates in the depth.
    # dist[n] = (depth, path) where depth is number of combinatorial gates
    dist = {}
    for n in topo_order:
        nt = DAG.nodes[n].get('node_type', '')

        if is_path_terminator(DAG, n):
            # Registered node -- path starts here with depth 0
            dist[n] = (0, [n])
        else:
            # Combinatorial node -- find longest incoming path + 1
            best_depth = -1
            best_path = []
            for pred in DAG.predecessors(n):
                if pred in dist:
                    d, p = dist[pred]
                    if d > best_depth:
                        best_depth = d
                        best_path = p
            if best_depth >= 0:
                dist[n] = (best_depth + 1, best_path + [n])
            else:
                # No predecessors with known distance -- this is a root
                dist[n] = (1, [n])

    # Now find paths that terminate at registered nodes.
    # For each registered sink, look at its predecessors' distances.
    critical_paths = []

    for n in topo_order:
        if not is_path_terminator(DAG, n):
            continue
        # This registered node is a sink. Check all predecessors.
        for pred in DAG.predecessors(n):
            if pred in dist:
                depth, path = dist[pred]
                if depth >= 1:  # at least one combinatorial gate
                    full_path = path + [n]
                    critical_paths.append((depth, full_path))

    # Sort by depth, descending
    critical_paths.sort(key=lambda x: -x[0])

    # Deduplicate paths that share the same start and end
    seen = set()
    unique_paths = []
    for depth, path in critical_paths:
        key = (path[0], path[-1], depth)
        if key not in seen:
            seen.add(key)
            unique_paths.append((depth, path))

    return unique_paths


def _display(G, node_name):
    """Get display name for a node, stripping file scope prefix."""
    return G.nodes[node_name].get('display_name', '') or display_name_from_scoped(node_name)


def format_path_report(paths, G, max_paths=30):
    """Format critical paths into a human-readable report."""
    lines = []
    lines.append("# GateBoy PPU Critical Combinatorial Paths\n")
    lines.append("Ranked by combinatorial gate depth between registered elements.\n")
    lines.append(f"Showing top {min(len(paths), max_paths)} of {len(paths)} paths with depth >= 1.\n")
    lines.append("## Timing Reference\n")
    lines.append("- Game Boy master clock: 4.194304 MHz")
    lines.append("- T-cycle period: ~238.4 ns")
    lines.append("- Half T-cycle: ~119.2 ns")
    lines.append("- Estimated gate delay (Sharp CMOS): 5-15 ns per gate")
    lines.append("- Paths exceeding ~8-24 gates may cause signals to arrive late\n")

    # Count paths by depth for summary
    depth_counts = {}
    for depth, _ in paths:
        depth_counts[depth] = depth_counts.get(depth, 0) + 1

    lines.append("## Depth Distribution\n")
    lines.append("| Depth | Count | Est. Delay (min) | Est. Delay (max) | % of Half T-cycle |")
    lines.append("|-------|-------|-------------------|-------------------|--------------------|")
    for d in sorted(depth_counts.keys(), reverse=True):
        min_delay = d * 5
        max_delay = d * 15
        pct = max_delay / 119.2 * 100
        flag = " **CRITICAL**" if pct > 50 else ""
        lines.append(f"| {d} | {depth_counts[d]} | {min_delay} ns | {max_delay} ns | {pct:.0f}%{flag} |")

    lines.append(f"\n## Top {min(len(paths), max_paths)} Deepest Paths\n")

    for i, (depth, path) in enumerate(paths[:max_paths]):
        min_delay = depth * 5
        max_delay = depth * 15
        pct = max_delay / 119.2 * 100

        src_node = G.nodes.get(path[0], {})
        dst_node = G.nodes.get(path[-1], {})

        lines.append(f"### Path {i+1}: Depth {depth} ({min_delay}-{max_delay} ns, {pct:.0f}% of half T-cycle)")
        lines.append(f"**Source:** `{_display(G, path[0])}` ({src_node.get('node_type', '?')}, {src_node.get('reg_type', '')})")
        lines.append(f"**Sink:** `{_display(G, path[-1])}` ({dst_node.get('node_type', '?')}, {dst_node.get('reg_type', '')})")
        lines.append(f"**Source file:** `{src_node.get('source_file', '?')}:{src_node.get('source_line', '?')}`")
        lines.append("")
        lines.append("```")
        for j, node_name in enumerate(path):
            nd = G.nodes.get(node_name, {})
            nt = nd.get('node_type', '?')
            gf = nd.get('gate_func', '')
            sf = nd.get('source_file', '')
            sl = nd.get('source_line', '')
            dn = _display(G, node_name)

            if nt in ('registered', 'bus', 'boundary'):
                marker = f"[{nt.upper()}]"
            else:
                marker = f"[{gf}]" if gf else "[comb]"

            loc = f"{sf}:{sl}" if sf else ""
            lines.append(f"  {'  ' * j}{marker} {dn}  ({loc})")
        lines.append("```\n")

    return "\n".join(lines)


# ============================================================================
# Serialization
# ============================================================================

def export_graph_json(G, filepath: Path):
    """Export graph to JSON format."""
    data = {
        "nodes": [],
        "edges": [],
    }

    for name, attrs in G.nodes(data=True):
        data["nodes"].append({
            "name": name,
            "display_name": attrs.get('display_name', display_name_from_scoped(name)),
            **{k: v for k, v in attrs.items() if v and k != 'display_name'},
        })

    for src, dst, attrs in G.edges(data=True):
        data["edges"].append({
            "src": src,
            "dst": dst,
            **{k: v for k, v in attrs.items() if v},
        })

    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"\nGraph exported to {filepath}")
    print(f"  {len(data['nodes'])} nodes, {len(data['edges'])} edges")


def export_paths_json(paths, G, filepath: Path):
    """Export critical paths to JSON."""
    data = []
    for depth, path in paths:
        path_data = {
            "depth": depth,
            "min_delay_ns": depth * 5,
            "max_delay_ns": depth * 15,
            "pct_half_tcycle": round(depth * 15 / 119.2 * 100, 1),
            "source": path[0],
            "sink": path[-1],
            "nodes": [],
        }
        for node_name in path:
            nd = G.nodes.get(node_name, {})
            path_data["nodes"].append({
                "name": node_name,
                "display_name": _display(G, node_name),
                "node_type": nd.get('node_type', ''),
                "gate_func": nd.get('gate_func', ''),
                "source_file": nd.get('source_file', ''),
                "source_line": nd.get('source_line', 0),
            })
        data.append(path_data)

    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"Critical paths exported to {filepath}")


# ============================================================================
# Main
# ============================================================================

def main():
    print("GateBoy PPU Signal Dependency Parser")
    print("=" * 50)

    result = ParseResult()

    # Phase 1: Parse computed methods first so their global nodes exist
    # when we parse the gate files
    print("\nParsing computed methods...")
    for fname in COMPUTED_METHOD_FILES:
        filepath = GATEBOY_SRC / fname
        parse_computed_methods(filepath, result)

    print(f"  Computed method nodes: {len(result.computed_methods)}")

    # Phase 2: Parse all gate logic files
    print("\nParsing source files...")
    for fname in GATE_FILES:
        filepath = GATEBOY_SRC / fname
        parse_file(filepath, result)

    print(f"\nRaw parse: {len(result.nodes)} nodes, {len(result.edges)} edges")
    scoped_wire_count = sum(len(v) for v in result.wire_scopes.values())
    dup_wire_names = sum(1 for v in result.wire_scopes.values() if len(v) > 1)
    print(f"  Scoped wires: {scoped_wire_count} ({dup_wire_names} wire names appear in multiple files)")

    # Classify gate_output nodes as combinatorial
    classify_gate_outputs(result)

    # Resolve edges with file-scoped lookup
    unknown = resolve_scoped_edges(result)
    print(f"Resolved edges: {len(result.edges)} (removed refs to {len(unknown)} unknown signals)")

    if unknown:
        sample = sorted(unknown)[:20]
        print(f"  Sample unknown refs: {', '.join(sample)}")

    # Build networkx graph
    print("\nBuilding graph...")
    G = build_graph(result)

    stats = graph_stats(G)
    print(f"\nGraph Statistics:")
    print(f"  Total nodes: {stats['total_nodes']}")
    print(f"  Total edges: {stats['total_edges']}")
    print(f"  Node types: {stats['node_types']}")
    print(f"  Registered: {stats['registered_nodes']}, Combinatorial: {stats['combinatorial_nodes']}")
    print(f"  Connected components: {stats['weakly_connected_components']}")
    print(f"  Has cycles: {stats['has_cycles']}")
    if stats['has_cycles']:
        print(f"  Cycle sample: {stats['cycle_sample']}")

    # Build DAG for analysis (break cycles)
    print("\nBuilding DAG (breaking cycles)...")
    DAG, removed_edges = build_dag_for_analysis(G)
    print(f"  Removed {len(removed_edges)} edges to break cycles")
    for src, dst in removed_edges[:10]:
        print(f"    {_display(G, src)} -> {_display(G, dst)}")

    # Critical path analysis
    print("\nFinding critical paths...")
    paths = find_critical_paths(DAG, G)
    print(f"  Found {len(paths)} paths")
    if paths:
        print(f"  Deepest: {paths[0][0]} gates")
        print(f"  Top 10 depths: {[p[0] for p in paths[:10]]}")

    # Export everything
    out_dir = Path("output")
    export_graph_json(G, out_dir / "ppu_graph.json")
    export_paths_json(paths, G, out_dir / "critical_paths.json")

    # Write human-readable report
    report = format_path_report(paths, G)
    report_path = out_dir / "critical_paths_report.md"
    with open(report_path, 'w') as f:
        f.write(report)
    print(f"Report written to {report_path}")

    # Write stats
    stats_path = Path("docs/graph-stats.md")
    with open(stats_path, 'w') as f:
        f.write("# GateBoy PPU Dependency Graph -- Statistics\n\n")
        f.write(f"| Metric | Value |\n")
        f.write(f"|--------|-------|\n")
        f.write(f"| Total nodes | {stats['total_nodes']} |\n")
        f.write(f"| Total edges | {stats['total_edges']} |\n")
        f.write(f"| Registered nodes | {stats['registered_nodes']} |\n")
        f.write(f"| Combinatorial nodes | {stats['combinatorial_nodes']} |\n")
        f.write(f"| Connected components | {stats['weakly_connected_components']} |\n")
        f.write(f"| Has cycles | {stats['has_cycles']} |\n")
        f.write(f"| Cycle-breaking edges removed | {len(removed_edges)} |\n\n")
        f.write("## Node Type Breakdown\n\n")
        f.write("| Type | Count |\n")
        f.write("|------|-------|\n")
        for t, c in sorted(stats['node_types'].items()):
            f.write(f"| {t} | {c} |\n")
        if removed_edges:
            f.write(f"\n## Cycle-Breaking Edges\n\n")
            f.write("These edges were removed to create a DAG for path analysis.\n")
            f.write("They represent feedback loops (typically through async set/reset of DFFs).\n\n")
            for src, dst in removed_edges:
                f.write(f"- `{_display(G, src)}` -> `{_display(G, dst)}`\n")

    print(f"Stats written to {stats_path}")

    return G, DAG, paths


if __name__ == "__main__":
    G, DAG, paths = main()
