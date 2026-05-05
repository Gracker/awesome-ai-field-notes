#!/usr/bin/env python3
"""Compatibility wrapper for legacy build commands.

Cloudflare Pages and older OpenClaw tasks may still invoke
`python3 scripts/generate-site.py`. This wrapper lands on the modern static
site generator through `openclaw/scripts/generate-site.py`.
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
