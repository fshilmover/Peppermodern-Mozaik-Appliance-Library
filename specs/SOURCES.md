# Spec sheet sources

One row per PDF in this folder. Every file passed the verification gauntlet on
2026-08-27: real `%PDF` header and the exact model string found in the extracted
text — except the two Lynx CAD drawings (no text layer), which were verified
visually and are byte-identical to the copies the shop already build-validated.
"Shop archive" files were collected from Peppermodern's own job records, where
each was used to build and verify the matching 3D model; their upstream origin
is noted. Manufacturer documents remain their manufacturers' property and are
removed on request ([open an issue](../../../issues)).

| File | Status | Source | Note |
|---|---|---|---|
| AmeriSink AS1126.pdf | verified (model-exact) | shop archive; amerisink.com per-model spec PDF | matched 'AS1126' in extracted text |
| AmeriSink AS1136.pdf | verified (model-exact) | shop archive; amerisink.com per-model spec PDF | matched 'AS1136' in extracted text |
| AmeriSink AS240A.pdf | verified (model-exact) | shop archive; amerisink.com per-model spec PDF | matched 'AS240A' in extracted text |
| Best HBC163ESS Ceiling Hood 63.pdf | verified (model-exact) | shop archive; Best official spec sheet (EN/FR) | matched 'HBC163ESS' in extracted text |
| Brizo 61363LF Beverage Faucet.pdf | verified (model-exact) | media.brizo.com spec submittal | model string verified in file |
| Brizo 64063LF Kitchen Faucet.pdf | verified (model-exact) | media.brizo.com spec submittal | model string verified in file |
| Brizo 81392 Raincan 12.pdf | verified (model-exact) | media.brizo.com/SpecSheet/BSP-B-81392 Rev B.pdf | model string verified in file |
| Brizo 87292 Shower Head 5.pdf | verified (model-exact) | media.brizo.com spec submittal | model string verified in file |
| Brizo 88775 Hand Shower Slide Bar.pdf | verified (model-exact) | media.brizo.com spec submittal | model string verified in file |
| Brizo 88875 Hand Shower Wall.pdf | verified (model-exact) | media.brizo.com spec submittal | model string verified in file |
| Brizo 8GE-TSG15 Steam Generator.pdf | verified (model-exact) | media.brizo.com spec submittal | model string verified in file |
| Brizo BSS-Odin Diverter Trim.pdf | verified (model-exact) | media.brizo.com spec submittal | sheet covers T60875 (Odin 3-function diverter trim — the model this product's geometry carries) |
| Brizo T65875LF Lav Faucet.pdf | verified (model-exact) | Brizo-authored spec submittal (distributor asset host) | model string verified in file |
| Fulgor F6IRT485GS1 Rangetop 48.pdf | verified (model-exact) | shop archive; Fulgor Milano official data sheet | matched 'F6IRT485GS1' in extracted text |
| GE Monogram ZTDX1FPSNSS Double Oven.pdf | verified (model-exact) | shop archive; GE-authored spec PDF (retailer-hosted; GE/Monogram sites block direct fetch) | matched 'ZTDX1FPSNSS' in extracted text |
| Kohler K-26071-LA Tub 60.pdf | verified (model-exact) | techcomm.kohler.com/techcomm/pdf/K-26071-LA_spec_US-CA_Kohler_en.pdf | matched 'K-26071-LA' in extracted text |
| Kohler K-2882 Undermount Lav.pdf | verified (model-exact) | techcomm.kohler.com/techcomm/pdf/K-2882_spec_US-CA_Kohler_en.pdf | matched 'K-2882' in extracted text |
| Lynx L30AGSS Asado Cooktop.pdf | verified (visual + MD5 vs shop copy) | lynxgrills.com CDN (du2gj1v5rko5e.cloudfront.net/file/56) | official dimensions drawing (Lynx canonical file LYNX_L30AG_ASADO_BUILT-IN.pdf); no per-model spec-sheet PDF exists; model binds via Lynx's own filename/page label; vector CAD, verified visually + byte-identical (MD5) to the shop's build-validated copy |
| Lynx L36TR Grill 36.pdf | verified (model-exact) | lynxgrills.com CDN (du2gj1v5rko5e.cloudfront.net/file/13246) | official product spec sheet, prints (L36TR); covers L36TR-LP/NG |
| Lynx LPB Power Burner.pdf | verified (visual + MD5 vs shop copy) | lynxgrills.com CDN (du2gj1v5rko5e.cloudfront.net/file/653) | official dimensions drawing, prints LYNX POWER BURNER LPB; vector CAD (no text layer), verified visually + byte-identical (MD5) to the shop's build-validated copy |
| Pfister GT529-BIB Brislin.pdf | verified (model-exact) | shop archive; Pfister spec submittal (pfisterstorage blob) | matched 'GT529-BIB' in extracted text |
| Pfister GT72-TNTBG Tenet.pdf | verified (model-exact) | shop archive; Pfister spec submittal (pfisterstorage blob), finishes incl. TNTBG | matched 'GT72-TNT' in extracted text |
| Pfister LG42-PFM0BG Pfirst Modern.pdf | verified (model-exact) | shop archive; Pfister spec submittal (pfisterstorage blob) | matched 'LG42-PFM0' in extracted text |
| Ruvati RVH8310 Pantry Sink.pdf | verified (model-exact) | ruvati.com/wp-content/uploads/RVH8310.pdf | matched 'RVH8310' in extracted text |
| Ruvati RVH8542ST Bar Sink.pdf | verified (model-exact) | shop archive; ruvati.com per-model spec sheet | matched 'RVH8542' in extracted text |
| Ruvati RVH8555 Workstation Sink.pdf | verified (model-exact) | shop archive; ruvati.com per-model spec sheet | matched 'RVH8555' in extracted text |
| Ruvati RVQ6290 Outdoor Sink.pdf | verified (model-exact) | ruvati.com/wp-content/uploads/RVQ6290.pdf | matched 'RVQ6290' in extracted text |
| Samsung DW80CG4021SR Dishwasher.pdf | verified (model-exact) | shop archive; Samsung-authored sheet (EQ-2 Samsung DW80CG4021SR.pdf) | matched 'DW80CG4021SR' in extracted text |
| Samsung RF70F27SER Refrigerator.pdf | verified (model-exact) | shop archive; Samsung-authored sheet via pdf.lowes.com (doc 75953811) | matched 'RF70F27SER' in extracted text |
| Samsung RF70H30GER Refrigerator.pdf | verified (model-exact) | shop archive; Samsung-authored sheet (retailer-hosted) | matched 'RF70H30GER' in extracted text |
| SubZero DEC1850FIL Freezer 18.pdf | verified (model-exact) | shop archive; subzero-wolf.com quick reference (sheet headed DEC1850FI) | matched 'DEC1850FI' in extracted text |
| SubZero DEC3650RIDL Fridge 36.pdf | verified (model-exact) | shop archive; same DEC3650RID sheet — covers L/R hinge variants | one Sub-Zero DEC3650RID sheet covers the L/R hinge variants; matched 'DEC3650RID' in extracted text |
| SubZero DEC3650RIDR Fridge 36.pdf | verified (model-exact) | shop archive; subzero-wolf.com quick reference — one DEC3650RID sheet covers L/R hinge variants | one Sub-Zero DEC3650RID sheet covers the L/R hinge variants; matched 'DEC3650RID' in extracted text |
| Wolf CSO24TE Steam Oven.pdf | verified (model-exact) | shop archive; subzero-wolf.com quick reference (standard install), model CSO24TE/S/TH | matched 'CSO24TE' in extracted text |
| Wolf CSO24TE Steam Oven (flush inset).pdf | verified (model-exact) | shop archive; subzero-wolf.com quick reference (flush inset) | matched 'CSO24TE' in extracted text |
| Wolf CSO3050PE Steam Oven.pdf | verified (model-exact) | shop archive; subzero-wolf.com quick reference (standard install) | matched 'CSO3050' in extracted text |
| Wolf CSO3050PE Steam Oven (flush inset).pdf | verified (model-exact) | shop archive; subzero-wolf.com quick reference (flush inset) | matched 'CSO3050' in extracted text |
| Wolf SO3050PE Wall Oven.pdf | verified (model-exact) | shop archive; subzero-wolf.com quick reference (standard install) | matched 'SO3050' in extracted text |
| Wolf SO3050PE Wall Oven (flush inset).pdf | verified (model-exact) | shop archive; subzero-wolf.com quick reference (flush inset) | matched 'SO3050' in extracted text |
