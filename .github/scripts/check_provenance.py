#!/usr/bin/env python3
"""Sources & Stories checks, per docs/pattern-template.md.

Fails if:
- a pattern doc (any .md in the content dirs, excluding README.md charters/indexes)
  lacks a non-empty "Sources & Stories" section;
- any citation key used in content resolves to nothing in REFERENCES.md.

No formal provenance tag is required. Sources are natural-language references
so readers can trace back to the original stories or research; stubs may carry
a [TODO ...] placeholder until their sources are written up.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
CONTENT_DIRS = ["docs/modules", "docs/metrics", "reference-architectures", "implementation-guides"]
# Citation keys are SURNAME-YEAR, with two extensions in use: multi-name keys
# joined by hyphens (JIN-CHEN-2018) and a letter suffix that separates two works
# by the same author in the same year (RIES-2009A).
KEY_RE = re.compile(r"\[([A-Z][A-Z0-9]*(?:-[A-Z][A-Z0-9]*)*-\d{4}[A-Za-z]?)\]")

errors = []

references = (ROOT / "REFERENCES.md").read_text(encoding="utf-8")
known_keys = set(KEY_RE.findall(references))

for content_dir in CONTENT_DIRS:
    for path in sorted((ROOT / content_dir).rglob("*.md")):
        if path.name == "README.md":
            continue
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT)

        sections = re.split(r"^##\s+", text, flags=re.M)
        sources = next((s for s in sections if s.startswith("Sources & Stories")), None)
        if sources is None or not sources.splitlines()[1:] or not "".join(sources.splitlines()[1:]).strip():
            errors.append(f"{rel}: missing or empty Sources & Stories section")

        for key in KEY_RE.findall(text):
            if key not in known_keys:
                errors.append(f"{rel}: citation key [{key}] not found in REFERENCES.md")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print("sources & stories: ok")
