# Contributing

Additions welcome. A product contribution is a pair of files plus one index line:

## What a product needs

1. **`.moz` + `.skp` pair** in `Product Libraries/PM Fixtures and Appliances/Products/`,
   named identically (`Brand Model Description.moz` / `.skp`). The `.moz`'s `ProdName`
   must equal the filename base, `SourceLib` must be `PM Fixtures and Appliances`,
   `UseSUModel="1"`, and `WStretch`/`HStretch`/`DStretch` all `False`.
2. **Dimensions from the spec sheet.** `Width`/`Height`/`Depth` in the `.moz` are the
   manufacturer's published overall dimensions in millimeters — never measured off the model,
   never estimated. Say in the PR which spec sheet (link it).
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

## Checks

`python tools/validate.py` must pass; it runs automatically on every pull request. It checks
the name bindings, stretch flags, node/file pairing, and file-format details that Mozaik is
strict about.

If git isn't your thing, email the files through
[peppermodern.com/resources](https://peppermodern.com/resources) and we'll add them with credit.
