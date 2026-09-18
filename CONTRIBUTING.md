# Contributing

Additions welcome. A product contribution is a pair of files plus one index line:

## What a product needs

1. **`.moz` + `.skp` pair** in `Product Libraries/PM Fixtures and Appliances/Products/`,
   named identically (`Brand Model Description.moz` / `.skp`). The `.moz`'s `ProdName`
   must equal the filename base, `SourceLib` must be `PM Fixtures and Appliances`,
   `UseSUModel="1"`, and `WStretch`/`HStretch`/`DStretch` all `False`.
2. **Dimensions from the spec sheet.** `Width`/`Height`/`Depth` in the `.moz` are the
   manufacturer's published overall dimensions in millimeters — never estimated. For a
   manufacturer's own 3D model they are the wrapped model's measured envelope, which must
   agree with the published numbers (Mozaik scales the model to the `.moz` values, so a
   mismatch renders stretched); state any delta in the PR. Say which spec sheet (link it).
3. **A `<Node>` line** in the library's `Library.ndx` under the right category folder, with
   `Name` exactly equal to the product name and an unused `ID`. Preserve the file's format:
   first line `4`, CRLF line endings, no BOM.
4. **A row in `MANIFEST.md`** — category, dimensions, and model source ("authored from spec"
   or "manufacturer model", with the manufacturer's download page if it's theirs).

## Model rules

- SketchUp axes map as Mozaik expects: X = width, Y = depth (front at low Y), Z = height,
  all geometry positive, bounding box = the product's W/H/D.
- The model is a placement graphic. Anything a cabinet is built around — cutout sizes,
  clearances — belongs in the spec sheet, not inferred from the model.

## Manufacturer models: ship as-is, slim, or build our own

Measured across this library (SketchUp census, 2026-09-17): the script-built massing
models run 6–150 faces and 12–55 KB; manufacturer models run 447–24,750 faces and
126 KB–4.7 MB; every one loads in under a second. The heaviest shipped products (Wolf
CSO3050PE at 24,750 faces / 4.7 MB, Fulgor rangetop at 19,713 / 3.8 MB) render fine in
real jobs, so that is the proven ceiling — not a target. File size and detail are separate
problems: the Brizo faucets are ~3 MB with only ~1,300 faces (embedded textures, not
geometry).

| Tier | Faces | `.skp` size | What to do |
|---|---|---|---|
| Ship as-is | ≤ 5,000 | ≤ 1 MB | Wrap the manufacturer's geometry unmodified (BIM exports usually land here — the Miele IFC files are 571 and 656 faces). |
| Slim first | 5,000–25,000, or 1–5 MB | | Strip textures/materials and remove what cannot be seen from outside (internals, fasteners, threads, lettering). Never re-model a visible surface; prove the result with before/after snapshots and the face count. |
| Build our own | > 25,000 faces or > 5 MB after slimming; or the file is 2D-only, the wrong variant, the wrong state (e.g. a downdraft raised), or won't import | | Model the massing from the spec sheet, borrowing the manufacturer's silhouettes for proportions only. Dimensions still come from the spec. |

Prefer the lightest manufacturer format that carries 3D: IFC and 3D DWG BIM exports are
normally placement-grade; FBX/OBJ mesh exports and native SketchUp marketing models are
where polygon counts explode.

## Checks

`python tools/validate.py` must pass; it runs automatically on every pull request. It checks
the name bindings, stretch flags, node/file pairing, and file-format details that Mozaik is
strict about.
A configuration variant of an existing product is named `<base product> (<variant>)` — for
example `Miele DA 6891 Downdraft 36 (blower at back)` — and shares the base product's spec
sheet; the validator accepts that.

If git isn't your thing, email the files through
[peppermodern.com/resources](https://peppermodern.com/resources) and we'll add them with credit.
