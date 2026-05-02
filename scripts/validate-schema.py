#!/usr/bin/env python3
"""Compatibility wrapper for legacy validation commands."""

from pathlib import Path
import runpy
import sys

ROOT = Path(__file__).resolve().parent.parent
TARGET = ROOT / "openclaw" / "scripts" / "validate-schema.py"

if not TARGET.exists():
    print(f"Missing target script: {TARGET}", file=sys.stderr)
    sys.exit(1)

runpy.run_path(str(TARGET), run_name="__main__")
