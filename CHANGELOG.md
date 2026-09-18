# Changelog

## v1.2.1 — 2026-09-18

- **Miele DA 6891 Downdraft 36 (blower at back)** (Hoods) — the same downdraft with the
  DAG 600 blower in Miele's rear-mount position (installation manual p. 25: the blower
  "can also be installed in the same position at the back of the appliance"). Requested by
  Alpenglow Woodworks after the first release; Mozaik cannot rotate part of a SketchUp
  product, so it is a second product. Built from Miele's printed dimensions (915 × 120 × 6
  trim, 802 × 108 × 646 housing, 332 × 332 × 250 blower lifted 17, collar 150 at 463 below
  the counter); the trim opening, canopy top and collar length are measured on Miele's own
  model. Omits the wordmark emboss, touch pad and the small stub under the housing, so its
  height reads 652 (Miele's unextended height) where the front-blower product reads 683.9.
  Collar on the left, as on the front-blower product; the motor is rotatable, so treat the
  collar side as a configuration.
- Validator: a product named `<base> (<variant>)` shares the base product's spec sheet.

## v1.2.0 — 2026-09-17

First products built by request through the resources-page form.

- **Miele H 7580 BP Wall Oven 30** (Ovens) and **Miele DA 6891 Downdraft 36** (Hoods),
  requested by Alpenglow Woodworks. Both are Miele's own BIM geometry (the IFC in the
  "CAD data / BIM data" download on each mieleusa.com product page), wrapped unmodified
  into the Mozaik frame; the downdraft ships retracted, with the blower box where Miele
  modeled it (its real position is configurable — see the spec). Dimensions in the
  `.moz` are the measured model envelopes; cutouts come from the spec sheets, which ship
  in `specs/` (proud and flush-mount sheets for the downdraft). Envelope deltas against
  the sheets, both inside Miele's own geometry: oven depth 688 mm measured where a chain
  built from Miele's printed pieces gives 690 (Miele prints no overall depth with the
  handle); downdraft width 914 mm measured against 915 on Miele's drawing and 916 in
  its product-sheet table. The `.moz` keeps
  the measured values so Mozaik does not stretch the models.
- CONTRIBUTING: a measured size/detail threshold for manufacturer models — ship as-is,
  slim first, or build our own — from a census of every model in the library.

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
