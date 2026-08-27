"""Library integrity gate. Run from the repo root: python tools/validate.py

Checks the format details Mozaik is strict about:
- Library.ndx: no BOM, first line "4", CRLF endings, unique node IDs, folder parents exist
- name triple-binding: ndx Node Name == .moz ProdName == filename base
- every product node has a .moz and every .moz has a node
- each .moz: Mozaik header, SourceLib == library folder name, UseSUModel's .skp exists,
  stretch flags False, positive W/H/D, unique UniqueID
- no .LCK files committed
Exits 1 on any failure.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors = []


def err(msg):
    errors.append(msg)


libs = [p for p in (ROOT / "Product Libraries").iterdir() if p.is_dir()]
if len(libs) != 1:
    sys.exit(f"FAIL: expected exactly one library under 'Product Libraries', found {len(libs)}")
LIB = libs[0]
LIBNAME = LIB.name

for lck in ROOT.rglob("*.LCK"):
    err(f"lock file committed: {lck.relative_to(ROOT)}")

# --- Library.ndx ---
raw = (LIB / "Library.ndx").read_bytes()
if raw[:3] == b"\xef\xbb\xbf":
    err("Library.ndx has a BOM (Mozaik requires none)")
if not raw.startswith(b"4\r\n"):
    err("Library.ndx must start with the line '4' followed by CRLF")
if b"\r\n" not in raw:
    err("Library.ndx has no CRLF line endings")

node_re = re.compile(
    rb'<Node Name="([^"]*)" ID="(\d+)" ParentID="(\d+)" IsFolder="(True|False)"')
folders, prod_nodes, seen_ids = {}, {}, set()
for m in node_re.finditer(raw):
    name, nid, pid = m.group(1).decode("utf-8"), int(m.group(2)), int(m.group(3))
    if nid in seen_ids:
        err(f"duplicate node ID {nid}")
    seen_ids.add(nid)
    if m.group(4) == b"True":
        folders[nid] = name
    else:
        if name in prod_nodes:
            err(f"duplicate product node name: {name}")
        prod_nodes[name] = pid
for name, pid in prod_nodes.items():
    if pid not in folders and pid != 0:
        err(f"node '{name}' points at missing folder ID {pid}")

# --- .moz files ---
moz_files = sorted((LIB / "Products").glob("*.moz"))
uids = {}
for moz in moz_files:
    base = moz.stem
    text = moz.read_text(encoding="utf-8")
    lines = text.splitlines()
    if len(lines) < 4 or lines[0].strip() != "2" or lines[2].strip() != "Mozaik Product Properties File":
        err(f"{moz.name}: unexpected Mozaik header lines")
        continue
    try:
        attrs = dict(re.findall(r'(\w+)="([^"]*)"', text.split("<Product ", 1)[1].split(">", 1)[0]))
    except IndexError:
        err(f"{moz.name}: no <Product> element")
        continue
    if attrs.get("ProdName") != base:
        err(f"{moz.name}: ProdName '{attrs.get('ProdName')}' != filename base '{base}'")
    if attrs.get("SourceLib") != LIBNAME:
        err(f"{moz.name}: SourceLib '{attrs.get('SourceLib')}' != library folder '{LIBNAME}'")
    if attrs.get("UseSUModel") == "1":
        skp = attrs.get("SketchUpFile", "")
        if not skp or not (LIB / "Products" / skp).is_file():
            err(f"{moz.name}: SketchUpFile '{skp}' not found beside the .moz")
    for flag in ("WStretch", "HStretch", "DStretch"):
        if attrs.get(flag) != "False":
            err(f"{moz.name}: {flag} is '{attrs.get(flag)}', must be 'False' (fixed-size product)")
    for dim in ("Width", "Height", "Depth"):
        try:
            if float(attrs.get(dim, "0")) <= 0:
                err(f"{moz.name}: {dim} not positive")
        except ValueError:
            err(f"{moz.name}: {dim} not a number")
    uid = attrs.get("UniqueID", "")
    if uid in uids:
        err(f"{moz.name}: UniqueID {uid} duplicates {uids[uid]}")
    uids[uid] = moz.name
    if base not in prod_nodes:
        err(f"{moz.name}: no <Node> in Library.ndx — product would be INVISIBLE in Mozaik")

for name in prod_nodes:
    if not (LIB / "Products" / f"{name}.moz").is_file():
        err(f"ndx node '{name}' has no matching .moz file")

# --- spec sheets: every product ships one, named to match ---
SPECS = ROOT / "specs"
spec_count = 0
for moz in moz_files:
    pdf = SPECS / f"{moz.stem}.pdf"
    if not pdf.is_file():
        err(f"specs/{moz.stem}.pdf missing — every product ships a verified spec sheet")
        continue
    spec_count += 1
    if not pdf.read_bytes()[:4] == b"%PDF":
        err(f"specs/{moz.stem}.pdf is not a PDF")

if errors:
    print(f"FAIL — {len(errors)} problem(s):")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
print(f"PASS — {len(moz_files)} products, {len(folders)} categories, "
      f"{spec_count} spec sheets, all name bindings, models, and flags "
      f"verified in '{LIBNAME}'")
