# Changelog

## v1.4.13 — 2026-10-29

- **Bosch HUI36253UC Hood Insert 36** (Hoods): the triangle mesh lines on the insert's steel shell are hidden.
  Bosch's model is built from large triangles, and every triangle edge used to draw as a line across faces that
  are flat on the real unit. Edges where two faces meet at 20 degrees or less are now softened, as SketchUp's
  own Soften Edges command does. Softening only changes how edges draw: no point moved and no face was removed,
  so the size (841.95 × 329.66 × 269.93 mm), the origin and the Elevation rule are unchanged. The model was
  checked against the unit drawings on page 8 of Bosch's installation guide; the grey box is the insert's own
  shell (part D there), not part of the wood hood around it.

## v1.4.12 — 2026-10-28

Six new products: five Bosch appliances and an Electrolux wine cooler, the library's first Electrolux. Each one's
Description field (at the top of the Product Editor) says how to set its Elevation. Electrolux is the 18th brand.

- **Bosch NITP660UC Induction Cooktop 36** (Cooktops + Rangetops). This is a 36 in frameless black-glass induction
  cooktop. Bosch's CAD file for it shows a sibling with a stainless frame, so this model is built from Bosch's spec
  sheet instead.
  - **Size:** 940 × 86.94 × 540 mm. The glass is 940 × 540 mm and stands 5/16 in (7.94 mm) above the counter.
  - **Anchor:** the model's origin is the countertop top. Its Elevation is preset to 908.05 mm, which assumes a
    34-1/2 in box and a 1-1/4 in counter build-up, and it snaps to the countertop top when placed.
  - **The body is not drawn.** Bosch does not print the size or position of the body under the glass. A
    see-through box, centred under the glass, marks the zone to keep clear instead. It is the size of Bosch's
    smallest allowed cut-out (883 × 505 mm) and 79 mm deep. Bosch prints the depth below the counter as 69 mm in
    this model's installation guide and 79 mm on its family drawings; the deeper value is used. Size the cut-out
    from the spec sheet.
- **Bosch B30IB100SP Refrigerator 30** (Refrigeration). This is Bosch's Benchmark 30 in built-in, panel-ready
  bottom-freezer refrigerator. The model is Bosch's own 3D file (an OBJ export; Bosch publishes no SketchUp
  file for it), turned to Mozaik's axes and not scaled.
  - **Size:** 756 × 2126.66 × 615.38 mm. It matches Bosch's printed width exactly, and the door's front-to-back
    depth and the height to the bracket tops within 1 mm.
  - **Panels and handles:** none are drawn. The panels and handles are the customer's own, and Bosch's drawings
    show no handles, so the two handles in Bosch's file were left out. The doors sit one panel thickness (19 or
    38 mm, per Bosch's installation guide) behind the cabinet face.
  - **Hinges:** on the right, as shipped. In Bosch's file the hinges stand 7.76 mm and 3.19 mm proud of the door.
- **Electrolux EI24WC15VS Wine Cooler 24** (Refrigeration). This is a 24 in under-counter wine cooler with a
  stainless-framed glass door. Electrolux publishes no 3D model of it, so it is built from the spec sheet.
  - **Size:** 604.84 × 865.19 × 654.05 mm, which is the printed 23-13/16 × 34-1/16 × 25-3/4 in, the depth
    including the handle. The handle stands 2-1/8 in proud of the door.
  - **Height:** drawn at the spec sheet's 34-1/16 in. The legs adjust; size the niche from the spec sheet.
  - **Hinges:** on the right, as shipped. The door is reversible.
- **Bosch HBLP651UC Double Oven 30** (Ovens). This is Bosch's Benchmark 30 in double wall oven. The model is
  Bosch's own SketchUp file, moved only, not scaled.
  - **Size:** 755 × 1323 × 676 mm, Bosch's printed 29-3/4 × 52-1/16 × 26-5/8 in (the depth includes the handles)
    within 1 mm.
  - **Anchor:** the model's origin is the bottom of the oven body, which rests on the floor of the cut-out. Set
    Elevation to that floor. A 5 mm trim strip at the front hangs below it, over the cabinet face; for a flush
    install, add 5 mm. With the body on the floor, the control panel overlaps the cabinet above the opening by
    an amount inside Bosch's allowed 10 to 51 mm.
  - **Recorded difference:** the model's body is 4 mm shorter than the current sheet's 49-3/4 in and matches
    Bosch's 2016 sheet.
  - It uses the range appliance type, like the library's other wall ovens, so it sits against the wall in 3D.
- **Bosch HUI36253UC Hood Insert 36** (Hoods). This is a 36 in ventilation insert for a custom hood. The model is
  Bosch's own SketchUp file, moved only, not scaled.
  - **Size:** 841.95 × 329.66 × 269.93 mm. The side spring clips set the width.
  - **Anchor:** the model's origin is the top of the trim flange. The flange is larger than the cut-out, so it
    sits against the underside of the hood's bottom panel. Set Elevation to that underside.
  - **Cut-out:** 812 × 260 mm, centred. The 6 in duct's centre is 83 mm in front of the cut-out's back edge. The
    spec sheet prints a 6 in duct opening and the installation guide a 6-1/2 in hole; follow the installation
    guide.
  - **Recorded difference:** the model is 327 mm tall where the spec sheet prints 324 mm. Bosch's own parts add up
    to 327 mm.
- **Bosch SHV9PCM3N Dishwasher 24** (Dishwashers). This is Bosch's 24 in custom-panel dishwasher. Bosch's CAD
  file is a coarse mesh that carries a sample panel and handle, so this model is built clean to Bosch's printed
  sizes. The details Bosch does not print, such as the toe recess and the door gap, are measured on Bosch's file.
  - **Size:** 598 × 860 × 585 mm. It is drawn at the lowest height, 860 mm; the feet raise it to 890 mm.
  - **No panel or handle is drawn.** Add the custom panel, 19 to 22 mm thick, in front of the door.
  - **Left out:** Bosch's file shows a raised cap on the top that no Bosch document shows. It is left out so that
    the model fits Bosch's printed minimum opening of 860 mm.

## v1.4.11 — 2026-10-28

One new product, a 1-1/2 in P-trap for laundry and utility sinks with a 1-1/2 in drain. The library's other trap,
the K-8998, is 1-1/4 in and fits lavatory sinks only.

- **Kohler K-9000 P-Trap** (Sinks). This is Kohler's 1-1/2 in adjustable cast-brass P-trap with a tubing outlet and a
  slip-joint inlet, the 1-1/2 in sibling of the K-8998. It wraps Kohler's own SketchUp model from Kohler's technical
  site. Kohler drew it with the wall flange facing Mozaik's back already, so the model is only shifted, not turned.
  - **Size:** 76.2 × 170.61 × 273.05 mm, measured on the model.
  - **Checked against the spec sheet:** the flange diameter (3 in), the outlet tube (1-1/2 in OD), the distance
    between the two slip nuts (3 in) and the inlet top to the trap bottom (4-7/8 in) each land within 0.01 in
    (0.3 mm) of Kohler's printed values.
  - **Anchor:** the model's origin is the arm's centre line at the wall flange, as on the K-8998. Set Elevation to
    the drain stub's centre height. The inlet's axis sits 1.500 in from the trap's left end and 1.000 in from its
    front. The inlet's top is 0.335 in below the arm's centre line.
  - **The arm is shorter than Kohler's sheet.** Kohler's sheets print 11-3/4 in from the flange to the inlet centre.
    Kohler's model, in both its SketchUp and 3DS files, measures 9-3/4 in. The model is shipped as Kohler drew it,
    with no vendor geometry edited. A real arm is cut to length on site, so place the trap by its inlet, under the
    sink's drain, and let the flange land where it lands.
  - **Drawn as Kohler drew it:** the arm is straight and level. A real arm swivels at the J-bend and falls toward the
    wall.

## v1.4.10 — 2026-10-28

One new product, a P-trap, and the Brizo wall faucet turned to hang on the wall. Both were first used on a
bathroom vanity, and both match the library files in use at the shop since 2026-10-21.

- **Kohler K-8998 P-Trap** (Sinks). This is Kohler's 1-1/4 in adjustable cast-brass P-trap with a tubing outlet. It
  wraps Kohler's own SketchUp model from Kohler's technical site, turned half a turn so the wall flange faces
  Mozaik's back and the inlet faces the front.
  - **Size:** 76.78 × 152.6 × 323.47 mm, measured on the model.
  - **Checked against the spec sheet:** the flange diameter (3 in), the flange face to the inlet centre (11-3/4 in)
    and the inlet top to the trap bottom (4-3/8 in) each land within 0.05 in (1.3 mm) of Kohler's printed values.
  - **Anchor:** the model's origin is the arm's centre line at the wall flange. Set Elevation to the drain stub's
    centre height. The inlet's axis sits 1.511 in from the trap's left end and 0.970 in from its front.
  - **Drawn as Kohler drew it:** the arm is straight and level. A real arm is cut to length, swivels at the J-bend
    and falls toward the wall.
- **Brizo T65875LF Lav Faucet** (Faucets). The faucet was drawn lying on its back, with the spout pointing up, and
  the Odin cross handles drew over the lever handles. It is now turned to hang on the wall, and only the lever
  handles (HL5875) are kept. No vendor geometry was edited; the cross-handle groups were left out whole.
  - **Size:** 327.02 × 68.15 × 226.52 mm (was 327.02 × 226.51 × 77.68).
  - **Anchor:** the model's origin is the valve centre line on the finished wall face. Set Elevation to the valve
    centre height. The product type changes from a sink-class appliance to the faucet class (SubType 10 to 13),
    its Elevation default from 908.05 to 0, and its Snap To setting from 3 to 0.
  - **Faucets already placed in a job keep their old product type and Elevation.** Place the faucet again from
    the library to get the wall-hung anchor.

## v1.4.9 — 2026-10-27

Two new products, both first used on a laundry room: a utility sink and a pull-down faucet.

- **Sterling S995-0 Utility Sink** (Sinks). This is Sterling's Latitude 995, a 25" single-bowl
  utility sink in white Vikrell. It wraps Sterling's own SketchUp model from Kohler's technical
  site. Two changes were made to that model. It is turned a quarter turn, so the front faces
  Mozaik's front and the faucet ledge sits at the back. The optional drain strainer is removed,
  because Sterling does not ship one with this sink; that takes the model from 27,998 faces to
  22,252, and the file is 3.8 MB.
  - **Size:** 634.89 × 332.9 × 559.05 mm, measured on the model. Sterling prints 25" × 13" × 22".
    The height is 2.7 mm over 13" because the drain boss under the bowl hangs below the foot ring
    the sink stands on.
  - **Checked against the spec sheet:** the faucet hole's position and diameter, the drain's
    position and the rim-to-foot height each land within 1 mm of Sterling's printed values.
  - **Anchor:** the model's origin is the top of the rim, for undermounting, as with the Kohler
    K-2882. Set Elevation to the countertop underside. The sink can also be top-mounted; this
    product is not anchored for that.
  - **Not drawn:** the mounting clips, the countertop anchors and the two extra faucet-hole
    locations, which are only marked on the sink. Size the countertop cut-out from Sterling's
    installation guide, not from the model.
- **Signature SHXCRA102ZSS Faucet** (Faucets). This is Signature Hardware's Ravenel single-hole
  pull-down kitchen faucet in stainless (SKU 949685, code SHXCRA102). Signature Hardware
  publishes no 3D model, so the faucet is built from its spec sheet.
  - **Size:** 106.36 × 400.04 × 242.76 mm, from the printed 4-3/16" side to side, 15-3/4" tall
    and 9-9/16" front to back.
  - **Checked against the spec sheet:** the spout height, the spout reach, the base plate, the
    tube diameter, the handle height and length and the 8° spray-head tilt match the printed
    values. The valve body and the handle hub carry no printed sizes; they are measured off the
    sheet's drawing and are good to about 3 mm.
  - **Two printed sizes on the sheet disagree with the rest of it.** The 3-1/2" beside the spray
    head does not fit the printed spout chain; the model follows the chain. The 3-15/16" to the
    lever would push the lever past the printed overall width; the model follows the drawing.
  - **Anchor:** the model's origin is the deck. Set Elevation to the countertop top surface. The
    faucet's centre line is 25.4 mm from the model's left and back edges. The handle is on the
    right as you face the faucet.
  - **Clearance:** the lever swings 20° back. Signature asks for at least 1-15/16" (49 mm) from
    the faucet's centre line to the backsplash; the model's back edge is only 25.4 mm behind it.
- **Library index:** the two products take node IDs 146 and 147. ID 145 is left unused here; it
  is taken in the maintainer's own copy of the library.

## v1.4.8 — 2026-10-24

The Kohler K-2882 Undermount Lav is drawn white. The K-2882 is vitreous china, and the model came in a metal finish.
Every face now carries the material "Kohler White -0" (K-2882-0, White). Geometry, size and origin are unchanged.

## v1.4.7 — 2026-10-13

The Best HBC163ESS Ceiling Hood 63 is rebuilt as the recessed ceiling hood it is. It is also
now Mozaik's hood type.

- **What the old model got wrong:** it was two stacked boxes hanging 12-3/16" below the
  ceiling. It read Best's 1-3/16" as the face's height; it is the face plate's lip past the
  band, measured sideways. It also read 8-3/8" as part of a stack of heights; it is measured
  from the face plate, and Best's drawing does not say what it reaches (most likely the duct
  outlets' centre line, not the top of the housing).
- **Face:** the stainless face plate is sheet metal and sits on the finished ceiling, so it is
  drawn flat, at the ceiling line. It is 63-1/2" × 27-9/16". On it are the outer frame ring,
  the dark perimeter-aspiration gap, the flat centre panel and the three LED light slots. Best
  prints no sizes for these, so they are measured from Best's straight-on product photo,
  within 1/4".
- **Above the ceiling:**
  - the band, 61-1/4" × 25-3/16" and 2-5/8" tall, which passes through the 61-3/4" × 25-3/4"
    framed opening;
  - the two adjustable support brackets, drawn at their 14" minimum (they adjust to 23-3/4").
    Each is drawn only as a flat plane on its screw line, 35-9/16" apart, with its five screws
    at 5-1/2", because Best prints no bracket member sizes;
  - a see-through blue box between the brackets, from the band to the top of the brackets. It
    is the space the framing must leave clear for the housing and the blower. **It is not
    Best's housing size:** Best prints the housing's width (23-11/16") but not its height or
    depth. Size framing and ducts from Best's spec sheet and installation guide.
  - the two cable inputs. Best prints their heights and their distances from the housing's
    centre line: 120 V 4-5/8" up and 8-3/16" off, the external-blower cable 8-1/16" up and
    4-1/8" off. Best does not name the face; its side view puts them on one end of the
    housing, drawn here on the left end, behind the centre line, with that end placed by the
    printed 23-11/16" housing width. The hood can be installed turned end for end, which moves
    them to the other end.
- **Not drawn:** the 10" duct damper (its height is not printed) and the housing itself.
- **Size:** Mozaik's height for the product becomes 355.6 mm (the 14" bracket minimum), from
  309.56 mm. Width and depth are unchanged (1612.9 × 700.09 mm).
- **Anchor:** the model's origin is the finished ceiling (or soffit) bottom face. Set
  Elevation to that height. Nothing hangs below it except the sheet-metal face.
- **Type:** the hood now uses Mozaik's hood type (SubType 25, like Mozaik's own metal hoods)
  instead of the cooktop type, which Mozaik drew 58.5 mm further from the wall in 3D than the
  floor plan showed.
- **Already placed:** a placed appliance keeps the type and the size it was placed with.
  Delete the hood and place it again, then set its Elevation to the finished ceiling.
- Its Description field gives the anchor and says what the blue box is.

## v1.4.6 — 2026-10-12

One new sink configuration.

- **Ruvati RVH8555 Workstation Sink (drain left)** (Sinks): the RVH8555 turned end for end, so its
  drain is at the left end when you face the sink. Ruvati draws the sink with its drain at the right
  end. The sink is the same along the front and the back, so turning it gives the left-hand drain
  with the same ledges, slope and size. The model is the v1.4.5 model rotated half a turn about its
  centre, not mirrored. It shares the RVH8555 spec sheet.
  - Mozaik cannot mirror or turn a sink once it is placed, so a left-hand drain needs its own product.
    Place this one instead of the RVH8555 when the drain must be at the left.
  - Ask Ruvati whether your installation may be turned this way; its spec sheet does not say.
  - Its Description field says the same and gives the anchor: set Elevation to the countertop
    underside.

## v1.4.5 — 2026-10-11

The Ruvati RVH8555 Workstation Sink model is rebuilt to match Ruvati's dimension drawing.

- **Ledges:** the two accessory ledges along the front and the back now each step in 11/16".
  The rim opening is 17-3/8" front to back, the upper ledge's inside edge is 16", and the bowl
  below the lower ledge is 14-5/8", as Ruvati's product page gives it. Ruvati's drawing labels
  each ledge 3/4"; only 11/16" fits those three printed sizes. Ruvati's spec sheet calls the
  16" size the interior bowl, but its drawing shows the lower ledge inside that line. The old
  model had a 16" bowl.
- **Ledge heights:** the upper ledge sits 1" and the lower ledge 2" below the top of the rim.
  Ruvati's drawing shows both but prints no height, so both are scaled from the drawing, whose
  printed sizes check to within 0.1". The old model had them 3/4" and 1-1/2" down, estimated
  from photos.
- **Body:** below the rim, the sink is now a formed stainless shell that steps in at each
  ledge and is 55-1/2" long, as Ruvati's elevation draws it. The old model was a solid block the
  full 57" × 19" size of the rim, so it showed the body 3/4" too long at each end and up to
  2-1/8" too deep at the front and the back.
- **Rim:** the rim's four corners are clipped, as Ruvati draws them. Each clip runs from the
  rim opening to the outside edge, so its legs are the 13/16" width of the rim.
- **Unchanged:** the size Mozaik uses (1447.8 × 252.41 × 482.6 mm), the origin at the top of
  the rim (Elevation = the countertop underside), the drain 6-1/4" from the right inside wall,
  the floor sloping 9" to 9-7/8" toward the drain, and the `.moz` file.
- **Already placed:** a sink already placed in a job shows the new model the next time the job
  opens; it does not need to be placed again.

## v1.4.4 — 2026-10-11

- **Bosch B36CL80ENS Refrigerator 36** gets a brushed-stainless image texture. Until now
  it rendered white: Bosch's model has one plain-white material on every face. Only that
  material changed; the geometry is identical to v1.3.2. The texture is our own, a
  procedurally generated 512 px seamless tile mapped at 300 mm, so it is covered by this
  library's licence. Bosch's own product photo shows horizontal grain, and the texture
  runs the same way. Because the model uses one material, its sides, top and back also
  show stainless.
  Mozaik shows the texture in the product preview, in its 3D product viewer and in its
  SketchUp 3D export of a room.
  This is the first of a planned roll-out to the library's other stainless products.

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

## v1.4.1 — 2026-10-11

- **Samsung RF70H30GER Refrigerator:** the product's Notes field is now empty. It held an
  old note from one shop job telling that job not to use this fridge. The note was about the
  job, not the product. Mozaik prints Notes on cabinet labels and assembly sheets, so every
  shop that placed this fridge would have printed it. The model, its size and its spec sheet
  are unchanged.
- The validator now fails any product whose Notes field is filled. Notes is the cabinet Notes
  tab: an appliance's Product Editor does not show it, and it prints on labels and assembly
  sheets. Text about a product belongs in its Description field (`ProductDesc`), at the top
  of the Product Editor.

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
