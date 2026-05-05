#!/usr/bin/env python3
"""Compatibility entrypoint for all OpenClaw site rebuild tasks.

The production site is now the modern static God of GPT portal generated into
dist/. Older Cloudflare settings, task docs, or cron jobs may still call
`python3 scripts/generate-site.py` or `python3 openclaw/scripts/generate-site.py`;
both paths intentionally land here and run the modern generator.
"""

from pathlib import Path
import runpy
import sys


TARGET = Path(__file__).resolve().with_name("generate-modern-site.py")

if not TARGET.exists():
    print(f"Missing modern site generator: {TARGET}", file=sys.stderr)
    sys.exit(1)

runpy.run_path(str(TARGET), run_name="__main__")
