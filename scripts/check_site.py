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
for needle in ['rel="canonical"', 'property="og:title"', 'name="description"', 'id="join-roles"', 'role consumer', 'role producer', 'role prosumer']:
    if needle not in html:
        errors.append(f"index.html: missing {needle}")

import hashlib
if 'class="skip-link"' not in html: errors.append("index.html: missing skip link")
if 'aria-level="1"' not in html: errors.append("index.html: missing level-1 heading")
for tag in re.findall(r"<(?:canvas|svg)\b[^>]*>", html):
    if "aria-label" not in tag and "aria-hidden" not in tag:
        errors.append("index.html: canvas/svg without aria-label or aria-hidden: " + tag[:70])
for tag in re.findall(r"<img\b[^>]*>", html):
    if "alt=" not in tag: errors.append("index.html: img without alt")
state = json.loads((root / "hivemind_at_home_state.json").read_text(encoding="utf-8"))
m = re.search(r"var STATE = (\{.*?\});\n", html, re.S)
if not m or json.loads(m.group(1)) != state:
    errors.append("index.html embedded STATE differs from hivemind_at_home_state.json")
body = {k: v for k, v in state.items() if k != "dashboard_state_sha256"}
if hashlib.sha256(json.dumps(body, sort_keys=True).encode()).hexdigest() != state.get("dashboard_state_sha256"):
    errors.append("dashboard_state_sha256 does not match state contents")
langs = state["i18n_dictionary"]
base = set(langs["en"])
for code, d in langs.items():
    if set(d) != base:
        errors.append(f"i18n[{code}] keys differ from en: {sorted(set(d) ^ base)}")

print("\n".join(errors) or "all site checks passed")
sys.exit(1 if errors else 0)
