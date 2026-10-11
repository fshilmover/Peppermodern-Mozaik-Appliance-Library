# Changelog

## v1.4.3 — 2026-10-11

The Fulgor rangetop and range now use Mozaik's range appliance type instead of its cooktop type.

- **Products:** Fulgor F6IRT485GS1 Rangetop 48 and Fulgor F6PGR304S2 Range 30. Sizes, models,
  elevations and descriptions are unchanged.
- **Why:** as in v1.4.2, Mozaik draws a cooktop-type appliance in its 3D views 58.5 mm further
  from the wall than the floor plan shows. A pro rangetop sits on its cabinet like Mozaik's own
  Pro Rangetops, which use the range type; the cooktop type is for drop-ins.
- **Countertops:** no appliance type cuts the countertop in Mozaik; only sinks get an automatic
  cutout. Notch the countertop around a rangetop by editing the top's shape, the same way as
  for an apron sink.
- **Already placed:** a placed appliance keeps the type it was placed with. Delete and re-place
  it to pick up the change, then set its Elevation and Outset again.

## v1.4.2 — 2026-10-11

The seven ovens now use Mozaik's range appliance type instead of its cooktop type.

- **Why:** Mozaik draws a cooktop-type appliance in its 3D views with the back 58.5 mm in
  front of the wall, whatever the appliance's depth, even when the floor plan shows it against
  the wall. Mozaik's own cooktop does the same. Range-type appliances (and Mozaik's own ranges)
  sit against the wall in both views. The ovens had inherited the cooktop type from a template.
- **Products:** Wolf CSO3050PE Steam Oven, Wolf SO3050PE Wall Oven, GE Monogram ZTDX1FPSNSS
  Double Oven, Wolf CSO24TE Steam Oven, Miele H 7580 BP Wall Oven 30, Miele H 7640 BM Speed
  Oven 24, Thermador PO302W Double Oven 30. Sizes, models and descriptions are unchanged.
- **Ovens already placed in a job keep the cooktop type.** A placed appliance stores its own type,
  and re-opening the job does not update it. Delete and re-place an oven to pick up the change.

## v1.4.0 — 2026-10-11

One new product and a new brand, Thermador.

- **Thermador PO302W Double Oven 30** (Ovens): the 30" Professional double wall oven, with
  bottom-hinge doors and Professional handles. Thermador's CAD download holds a 2D drawing and
  a Revit family that SketchUp cannot open, so the model is built in SketchUp from Thermador's
  printed dimensions. The doors, handles,
  glass, display and knob positions are scaled from Thermador's current product photo. The
  knob profile comes from its 2D CAD views.
  - Size: 755.65 × 1322.39 × 688.98, which is the printed 29 3/4" × 52 1/16". The depth is
    the printed 24 1/2" to the door face plus the 2 5/8" (67 mm) handle; Thermador's guide
    prints the total as 27 1/8" (689 mm).
  - Thermador's millimetre figures round the inches differently from page to page (756 or
    755 wide, 1324 or 1323 tall). The model follows the inches.
  - The oven rests on the floor of its cut-out: set Elevation to that floor. Size the cut-out
    from the spec sheet. The product's Description field says the same.
- The install guide no longer states a product count; README and MANIFEST carry it.

## v1.3.3 — 2026-10-10

- **Fulgor F6IRT485GS1 Rangetop 48:** the model now stands on the cabinet below it.
  Its origin was at the counter line, 7" (179 mm) above the bottom of the unit. Setting
  Elevation to the cabinet top therefore sank the body into the cabinet, leaving the
  glass level with the cabinet top. Fulgor's side view shows this rangetop resting on
  the cabinet or an open frame, so the origin is now the bottom of the unit. Set
  Elevation to the top of the cabinet it sits on.
- The new default Elevation is 729.05 mm (28 11/16"). That puts the counter line at a
  standard 35 3/4" (908.05 mm) counter top, 7" above the cabinet, which is Fulgor's
  cutout height. The glass stands 3/8" (8 mm) above the counter.
- The size (1216 × 187 × 743.8) and the model's appearance are unchanged. Fulgor's
  component is the same; only its position inside the file moved up 179 mm.
- The product's Description says where to set Elevation.

## v1.3.2 — 2026-09-29

A user measured the Miele dishwasher's face at 30 9/16"; Miele prints 30 3/16" (767 mm).
v1.3.0 had stretched each of this release's four manufacturer models to match its sheet's
printed overall size. On the dishwasher, the 10 mm difference really sat in the legs, and
the stretch moved it into the face. All four models now ship as the manufacturers drew
them. Their doors and faces keep their true sizes, and openings come from the spec sheets.

- **Miele G 5006 U Dishwasher 24:** 598 × 845 × 573. The face is Miele's 767 mm (30 3/16")
  again. Miele's model stands 845 mm, which is what Miele's European sheets print; that is
  10 mm under the 855–920 mm installed range on its North American sheet. Size the niche
  from the spec sheet.
- **Bosch B36CL80ENS Refrigerator 36:** 910.35 × 1821.65 × 704.61. Bosch prints
  905 × 1830 × 706. Bosch's model has its case sides 2 mm outboard of the doors on each
  side, and its top sits 8 mm lower. The doors match the sheet. Size the opening from the
  spec sheet.
- **Miele H 7640 BM Speed Oven 24:** 595 × 455 × 620.3. The door and control band are
  exact; the 0.5 mm difference sits in the gap between them.
- **Fulgor F6PGR304S2 Range 30:** 758 × 923.89 × 753.68. That depth is 0.3–2.3 mm short
  of Fulgor's own printed 754 / 756.
- The dishwasher and fridge Descriptions state what to size from the spec sheet.
- MANIFEST and CONTRIBUTING: a manufacturer's model is scaled only to correct a uniform
  units or export error.

## v1.3.1 — 2026-09-29

- **Fulgor F6PGR304S2 Range 30:** the note about what the model shows (1" island trim,
  no backguards, other configurations on request) moves to the product's **Description**
  field, shown at the top of Mozaik's Product Editor. v1.3.0 put it in the Notes field.
  Mozaik doesn't show that field for appliances, and prints it on cabinet labels and
  assembly sheets.

## v1.3.0 — 2026-09-28

Four new products and a new **Ranges** category. All four are the manufacturers' own 3D
models, wrapped unmodified.

- **Bosch B36CL80ENS Refrigerator 36** (Refrigeration). Bosch's trade-CAD SketchUp model
  from the product page's "CAD File" download.
- **Fulgor F6PGR304S2 Range 30** (Ranges). Fulgor's own SketchUp model. It is shown with the
  1" cast-iron island trim, which Fulgor draws as standard and also sells as accessory
  F6BG30BCI / F6BG30ISL; backguards are not shown. The legs are at their lowest setting. Ask
  through the form for another configuration.
- **Miele H 7640 BM Speed Oven 24** (Ovens). Miele's IFC from the mieleusa.com CAD/BIM
  download.
- **Miele G 5006 U Dishwasher 24** (Dishwashers), the Canadian model. Miele's IFC from the
  miele.ca CAD/BIM download. Its spec sheet ships alongside Miele's product sheet.
- **(Reverted in v1.3.2.)** Where a manufacturer's model and its spec sheet disagree, the
  spec sheet now wins. We
  first check the gap isn't a part the printed figure leaves out. None was, in any of these
  four. We then scale the model on that axis, and never edit its geometry. Factors:
  - Bosch, width ×0.99412, height ×1.00459 and depth ×1.00197, giving 905 × 1830 × 706.
  - Fulgor, depth ×1.00308, giving 756.
  - The speed oven, height ×1.00110, giving 455.5.
  - The dishwasher, height ×1.01183, giving 855. Miele's model has the legs fully retracted,
    at the 845 its European sheets print. It now meets the North American sheet's 855
    minimum; the door renders 9 mm taller than printed as a result.

  MANIFEST and CONTRIBUTING now describe this rule.

## v1.2.1 — 2026-09-18

- **Miele DA 6891 Downdraft 36 (blower at back)** (Hoods) — the same downdraft with the
  DAG 600 blower in Miele's rear-mount position (installation manual p. 25: the blower
  "can also be installed in the same position at the back of the appliance"). Mozaik cannot
  rotate part of a SketchUp product, so it is a second product. Built from Miele's printed dimensions (915 × 120 × 6
  trim, 802 × 108 × 646 housing, 332 × 332 × 250 blower lifted 17, collar 150 at 463 below
  the counter); the trim opening, canopy top and collar length are measured on Miele's own
  model. Omits the wordmark emboss, touch pad and the small stub under the housing, so its
  height reads 652 (Miele's unextended height) where the front-blower product reads 683.9.
  Collar on the left, as on the front-blower product; the motor is rotatable, so treat the
  collar side as a configuration.
- Validator: a product named `<base> (<variant>)` shares the base product's spec sheet.

## v1.2.0 — 2026-09-17

First products built by request through the resources-page form.

- **Miele H 7580 BP Wall Oven 30** (Ovens) and **Miele DA 6891 Downdraft 36** (Hoods).
  Both are Miele's own BIM geometry (the IFC in the
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
