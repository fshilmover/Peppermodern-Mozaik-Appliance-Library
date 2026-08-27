# Changelog

## v1.1.0 — 2026-08-27

Spec sheets for submittals, plus a face for the repo.

- `specs/` — the manufacturer's spec sheet for every product, named to match it
  (plus flush-inset variant sheets for the three Wolf ovens). Per-file source and
  verification status in `specs/SOURCES.md`; every file passed the gauntlet
  (real PDF + exact model coverage; the two Lynx CAD drawings verified visually
  and byte-identical to the shop's build-validated copies).
- Validator now requires a spec PDF per product.
- README: 3D collage of ten models sampled across the categories.
- Release zips are now built by CI from the tag (v1.0.0's was packaged by hand).

## v1.0.0 — 2026-08-27

Initial public release.

- 36 products across 10 categories (12 brands): ovens, refrigeration, dishwashers, hoods,
  cooktops + rangetops, outdoor cooking, sinks, faucets, showers, tubs.
- Library ships install-ready: `Library.ndx` category tree, `parameters.dat`, and 36
  `.moz`/`.skp` pairs with spec-sheet dimensions and stretch locked off.
- Install guide (`docs/install-guide.html`), product manifest, validator (`tools/validate.py`).
