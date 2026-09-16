#!/usr/bin/env python3
"""Entry-file checks for llms.txt, the file an AI assistant reads first.

Fails if:
- a link in llms.txt points at a path that does not exist in the repository;
- a finished page or template has no row in llms.txt.

A finished page is any .md under the content directories that is not a README
and not a stub. Stubs carry a "**Status:** stub" line until their content lands.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
ENTRY = ROOT / "llms.txt"
RAW = "https://raw.githubusercontent.com/h3qing/open-analytics-framework/main/"
CONTENT_DIRS = ["docs/modules", "docs/metrics", "reference-architectures", "implementation-guides", "skill", "templates"]

errors = []

text = ENTRY.read_text(encoding="utf-8")
linked = set(re.findall(r"\]\(" + re.escape(RAW) + r"([^)\s]+)\)", text))

for rel in sorted(linked):
    if not (ROOT / rel).is_file():
        errors.append(f"llms.txt: {rel} does not exist")

for content_dir in CONTENT_DIRS:
    for path in sorted((ROOT / content_dir).rglob("*.md")):
        if path.name == "README.md":
            continue
        if "**Status:** stub" in path.read_text(encoding="utf-8"):
            continue
        rel = str(path.relative_to(ROOT))
        if rel not in linked:
            errors.append(f"{rel}: no row in llms.txt")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print("entry file: ok")
