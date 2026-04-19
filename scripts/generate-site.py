#!/usr/bin/env python3
"""Compatibility wrapper for legacy build commands.

Cloudflare Pages and older docs may still invoke `python3 scripts/generate-site.py`.
The real generator now lives at `openclaw/scripts/generate-site.py`.
"""

from pathlib import Path
import runpy
import sys

ROOT = Path(__file__).resolve().parent.parent
TARGET = ROOT / "openclaw" / "scripts" / "generate-site.py"

if not TARGET.exists():
    print(f"Missing target script: {TARGET}", file=sys.stderr)
    sys.exit(1)

runpy.run_path(str(TARGET), run_name="__main__")
