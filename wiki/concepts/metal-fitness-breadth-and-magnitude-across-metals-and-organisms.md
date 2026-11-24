---
type: "Concept"
description: "How many experiments, organisms and genes show metal fitness effects in the Fitness Browser, and differences between essential and toxic metals and between organisms."
sources: ["summaries/metal_cross_resistance__REPORT.md", "summaries/metal_fitness_atlas__REPORT.md"]
---
# Metal-fitness breadth and magnitude across metals and organisms

Metal fitness effects in the Fitness Browser (FB) are broad but unevenly sampled. Cobalt and nickel are tested in 27 and 26 organisms [src: metal_fitness_atlas], while six metals on the USGS (United States Geological Survey) critical minerals list are tested in only 1-2 organisms. [src: metal_fitness_atlas] Essential-metal limitation affects a larger share of genes than toxic-metal stress. [src: metal_fitness_atlas] The evidence comes from two reports, [[summaries/metal_fitness_atlas__REPORT]] and [[summaries/metal_cross_resistance__REPORT]].

## How much metal data exists

The FB contains 559 metal-related experiments, 8.2% of 6,804 total experiments, covering 16 metals. [src: metal_fitness_atlas] The [[entities/metal-fitness-atlas]] holds 383,349 gene × metal fitness records across 24 organisms and 14 metals, and the report calls it the first cross-species genome-wide fitness atlas for metal tolerance. [src: metal_fitness_atlas] Metal data exist for 31 organisms, of which 24 have fitness matrices. [src: metal_fitness_atlas]

The cross-resistance report used a different selection. It classified 452 metal experiments across 37 organisms and 14 metals (Al, Cd, Co, Cr, Cu, Fe, Hg, Mn, Mo, Ni, Se, U, W, Zn). [src: metal_cross_resistance] It extracted metal fitness data for 119,561 genes in 28 organisms with ≥3 metals. Thirty organisms were extracted, and 2 were excluded for having <3 metals. [src: metal_cross_resistance] It analyzed 317 organism-pair observations across 85 unique metal pairs. [src: metal_cross_resistance]

## Breadth across metals

Coverage differs strongly between metals. Six metals have cross-species coverage (≥3 organisms), listed here with organism counts: [[entities/cobalt]] 27 [src: metal_fitness_atlas], [[entities/nickel]] 26 [src: metal_fitness_atlas], [[entities/copper]] 23 [src: metal_fitness_atlas], [[entities/aluminum]] 22 [src: metal_fitness_atlas], zinc 17 [src: metal_fitness_atlas] and [[entities/iron]] 3. [src: metal_fitness_atlas]

Aluminum, cobalt and nickel are the three USGS critical minerals with broad FB coverage. [src: metal_fitness_atlas] Six metals on the USGS critical minerals list are tested in only 1-2 organisms. [src: metal_fitness_atlas] The atlas report caveats that uranium, chromium, mercury, cadmium, selenium and manganese are each in only 1-2 organisms. Cross-species patterns for these rare metals therefore reflect DvH and psRCH2 biology. [src: metal_fitness_atlas] See [[concepts/metal-coverage-gaps-and-proposed-validation-experiments]] for the proposed fixes.

## Breadth across organisms

DvH ([[entities/desulfovibrio-vulgaris-hildenborough]]) is the most metal-profiled organism, with 149 experiments across 13 metals. [src: metal_fitness_atlas] *Pseudomonas putida* KT2440 (pseudomonas putida) has FB fitness matrices but zero metal experiments. It is the only FB organism with no metal data. [src: metal_fitness_atlas]

## Magnitude of effects

Across the atlas, 3.3% of gene × metal records (12,838 / 383,349) show significant fitness defects (fit < -1, |t| > 4). [src: metal_fitness_atlas] Iron and essential-metal limitation give the highest fractions of important genes: 12.3% for Fe and 11.2% for Mo/W. [src: metal_fitness_atlas] Toxic metals cluster around 2.7-4.4%. [src: metal_fitness_atlas] The strict category contains 5,667 metal-important genes (1.5%). [src: metal_fitness_atlas]

Organisms differ widely. DvH has 1,366 metal-important genes, 49.8% of its genome across 13 metals. [src: metal_fitness_atlas] The cyanobacterium *Synechococcus elongatus* ([[entities/synechococcus-elongatus]]) is notably metal-sensitive, with 33.6% of genes important across just 2 metals. [src: metal_fitness_atlas]

## Open Directions

- Test the rare metals (U, Cr, Hg, Cd, Se, Mn) in at least 5 organisms each. This would separate general conservation from DvH- and psRCH2-specific patterns.
- Run metal experiments in *P. putida* KT2440, the only FB organism without them, to fill the largest organism gap.
- Compare important-gene fractions at matched numbers of metals per organism. This would show whether DvH's 49.8% and SynE's 33.6% reflect biology or sampling depth.
- Apply the atlas thresholds to the 37-organism cross-resistance set. This would show how organism selection changes the breadth counts.
- See [[concepts/organism-coverage-and-attrition-in-cross-organism-fitness-conservation-analyses]] for how attrition affects such comparisons.
