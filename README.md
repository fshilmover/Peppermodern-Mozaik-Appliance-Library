# Peppermodern Mozaik Appliance Library

A free library of real appliances and plumbing fixtures for [Mozaik](https://www.mozaiksoftware.com/) —
36 products across 10 categories, built to the manufacturers' spec sheets, locked to their true
dimensions, and ready to place. Maintained by [Peppermodern](https://peppermodern.com/resources),
a millwork + casework shop in Mooresville, NC.

**Categories:** Ovens · Refrigeration · Dishwashers · Hoods · Cooktops + Rangetops ·
Outdoor Cooking · Sinks · Faucets · Showers · Tubs

**Brands:** AmeriSink, Best, Brizo, Fulgor, GE Monogram, Kohler, Lynx, Pfister, Ruvati,
Samsung, Sub-Zero, Wolf

Every product carries the width, height, and depth printed on the manufacturer's spec sheet
and cannot be stretched — place a 30" wall oven and it stays a 30" wall oven. Each shows as a
3D model in plans, elevations, and renders. The full product list with dimensions is in
[MANIFEST.md](MANIFEST.md).

> **Never used GitHub?** You don't need an account. Click the green **Code** button above →
> **Download ZIP**, or follow the [install guide](https://fshilmover.github.io/Peppermodern-Mozaik-Appliance-Library/install-guide.html) —
> it walks through everything, and includes a prompt you can paste into [Claude](https://claude.ai)
> to be talked through the install step by step.

## Install the whole library (recommended)

1. Download this repository (green **Code** button → **Download ZIP**) and unzip it,
   or grab the library-only zip from [Releases](../../releases).
2. Close Mozaik.
3. Copy the folder `Product Libraries/PM Fixtures and Appliances` into your Mozaik
   `Product Libraries` folder — `C:\Mozaik\Product Libraries` on a default install. If you're
   not sure where yours is, it's the folder that already contains libraries like
   `Appliances V12`.
4. Open Mozaik. The library appears in **Libraries → Products** as
   **PM Fixtures and Appliances**, with its category tree intact.
5. Verify: place **Wolf CSO24TE Steam Oven** in a scratch job. It should face the room,
   render as a steam oven (control band on top, tubular handle), and hold 597 × 454 × 582 mm —
   the dimensions are locked and won't stretch.

Installing the whole library is collision-proof: it never touches your existing libraries.

## Add single products to a library you already have

1. Copy the product's `.moz` **and** its matching `.skp` from
   `Product Libraries/PM Fixtures and Appliances/Products/` into your own library's
   `Products` folder.
2. In Mozaik: **Libraries → Products** → open your library.
3. Right-click the category you want it in → **Add** → type **exactly the same name as the
   .moz file** (without the extension). Mozaik connects the name to the file and its
   SketchUp model.

This is Mozaik's own documented mechanism —
[Copying Products to Different Library](https://mozaik.support.cyncly.com/hc/en-us/articles/40831678424465-Copying-Products-to-Different-Library).
The name must match the filename exactly; a mismatched name creates a blank product instead.
No dimensions or settings to enter — everything rides in the `.moz`.

## Updating

Download the newest release and replace the `PM Fixtures and Appliances` folder. If you've
added your own products *into this library's folder*, they'd be lost in the replace — keep
your own products in your own libraries and cherry-pick ours instead, or merge by hand.

## Request a model

Use the request form at [peppermodern.com/resources](https://peppermodern.com/resources), or
[open an issue](../../issues) with the make, model, and a link to the spec sheet.

## Contribute

Pull requests welcome — see [CONTRIBUTING.md](CONTRIBUTING.md). If you'd rather not deal with
git, email the files through the [resources page](https://peppermodern.com/resources) and
we'll add them with credit.

## How these are made

Each model starts from the manufacturer's printed spec sheet. We use Claude to write a
SketchUp build script to those dimensions, check the result against the drawing, and place it
in Mozaik to verify it renders correctly before it ships. Where a manufacturer publishes
their own 3D model, we use it unmodified. One rule throughout: **cabinet cutout dimensions
come from the spec sheet, never from measuring the model.**

## License

Everything authored for this repository is [MIT-licensed](LICENSE). Models published by the
manufacturers remain their property, included here so their products can be specified
accurately; a manufacturer who wants a file removed can say so in an
[issue](../../issues) or through [peppermodern.com](https://peppermodern.com/contact) and
it comes out. Per-product provenance is tracked in [MANIFEST.md](MANIFEST.md).
