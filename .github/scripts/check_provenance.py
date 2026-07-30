#!/usr/bin/env python3
"""Provenance checks, per docs/pattern-template.md.

Fails if:
- a pattern doc (any .md in the content dirs, excluding README.md charters/indexes)
  lacks a Provenance section carrying a tag or an explicit [TODO ...] placeholder;
- any citation key used in content resolves to nothing in REFERENCES.md.

Placeholders pass: stubs are expected to carry [TODO: pending prior-art review]
until their prior-art row exists. A finished tag with no docs/prior-art.md row is
not yet machine-checked; the review process owns that until titles stabilize.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
CONTENT_DIRS = ["docs/modules", "reference-architectures", "implementation-guides"]
TAG_RE = re.compile(r"\b(Established|Adapted|Original)\b|\[TODO[^\]]*\]")
KEY_RE = re.compile(r"\[([A-Z][A-Z0-9]*-\d{4}[a-z]?)\]")

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
        provenance = next((s for s in sections if s.startswith("Provenance")), None)
        if provenance is None or not TAG_RE.search(provenance):
            errors.append(f"{rel}: missing Provenance section or tag")

        for key in KEY_RE.findall(text):
            if key not in known_keys:
                errors.append(f"{rel}: citation key [{key}] not found in REFERENCES.md")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print("provenance: ok")
