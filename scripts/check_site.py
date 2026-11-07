#!/usr/bin/env python3
"""Sanity checks for the static site: control chars, JSON/XML validity, duplicate drift, required meta."""
import json, re, sys, pathlib
import xml.dom.minidom as minidom

root = pathlib.Path(__file__).resolve().parent.parent
errors = []

for name in ["README.md", "index.html", "404.html", "hivemind_at_home_dashboard.html"]:
    text = (root / name).read_text(encoding="utf-8")
    for m in re.finditer(r"[\x00-\x08\x0b-\x1f]", text):
        line = text.count("\n", 0, m.start()) + 1
        errors.append(f"{name}:{line}: control character {m.group()!r} (unescaped LaTeX backslash?)")
    if name == "README.md" and "\t" in text:
        errors.append("README.md: tab character found")

for f in root.glob("*.json"):
    try:
        json.loads(f.read_text(encoding="utf-8"))
    except ValueError as e:
        errors.append(f"{f.name}: invalid JSON: {e}")

try:
    minidom.parse(str(root / "sitemap.xml"))
except Exception as e:
    errors.append(f"sitemap.xml: {e}")

if (root / "index.html").read_bytes() != (root / "hivemind_at_home_dashboard.html").read_bytes():
    errors.append("index.html and hivemind_at_home_dashboard.html have drifted apart")

html = (root / "index.html").read_text(encoding="utf-8")
for needle in ['rel="canonical"', 'property="og:title"', 'name="description"']:
    if needle not in html:
        errors.append(f"index.html: missing {needle}")

print("\n".join(errors) or "all site checks passed")
sys.exit(1 if errors else 0)
