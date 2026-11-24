---
type: "Concept"
description: "How metal-important genes are split into metal-specific, metal+stress and general sick classes by their sick rate across non-metal experiments, per-metal differences, threshold robustness and validation; stops at conservation and candidate-level results."
sources: ["summaries/counter_ion_effects__REPORT.md", "summaries/discoveries.md", "summaries/metal_cross_resistance__REPORT.md", "summaries/metal_fitness_atlas__REPORT.md", "summaries/metal_specificity__REPORT.md"]
---
# Metal-specific versus pleiotropic stress gene classification

Metal-important genes can be split by how often they are also sick in non-metal experiments. Several projects report a majority of metal-specific genes, but the exact fraction depends on the threshold and on how the classes are defined. The evidence is descriptive classification, not formal enrichment testing. [src: counter_ion_effects] The metal_specificity report reads genes important only for metals as the bona fide metal resistance repertoire. [src: metal_specificity]

## Three-class scheme by sick rate

The metal_specificity report calls a gene metal-specific if it shows significant fitness defects under metal stress but has a <5% sick rate across 5,945 non-metal experiments. This gave 4,177 (54.9%) of 7,609 metal-important gene records in 24 organisms. [src: metal_specificity] The discoveries digest reports the same figures (55%). [src: discoveries] The remaining genes are general sick (2,888, 38.0%) and metal+stress (544, 7.2%). [src: metal_specificity] General sick means important across many conditions; metal+stress means shared with other stresses. [src: discoveries]

The metal_specificity dataset classified 6,504 experiments: 559 metal (8.6%) and 5,945 non-metal (91.4%). [src: metal_specificity] The 7,609 records are 59.3% of the 12,838 in the atlas. [src: metal_specificity] The discoveries digest concludes that the majority of the metal-important gene set of the [[entities/metal-fitness-atlas|Metal Fitness Atlas]] are genuine metal tolerance determinants, not general stress genes. [src: discoveries] The metal_specificity report says this validates the cross-species approach. [src: metal_specificity]

Other projects use different definitions and get different numbers:

- The counter_ion_effects project defines metal-specific as important for metals but not NaCl (sodium chloride). It found 6,517 of 10,821 records (60.2%) metal-specific. [src: counter_ion_effects] Its framework gives 40% shared-stress and 60% metal-specific. [src: counter_ion_effects]
- The metal_cross_resistance project defines three tiers by breadth. General-stress genes are pleiotropic, metal-shared genes matter for ≥2 metals, and metal-specific genes matter for exactly 1 metal. [src: metal_cross_resistance] Of 8,162 genes in 28 organisms, 1,484 (18.2%) are general stress, 2,306 (28.3%) metal-shared and 4,372 (53.6%) metal-specific. [src: metal_cross_resistance]

These schemes use different definitions, so each percentage stands on its own.

The metal_fitness_atlas report takes a contrasting view. It calls its metal-important definition broad (fit < -1 OR n_sick ≥ 1, ~3.3% of genes). It says most of those genes are general stress genes rather than metal-specific. [src: metal_fitness_atlas] This is in tension with the majority-specific result of the sick-rate analyses. [src: metal_specificity, discoveries] The atlas report proposes a two-tier model. The core tier is general stress genes, conserved for functions beyond metal tolerance. The accessory tier is a smaller set giving specific resistance, visible only after controlling for general stress. [src: metal_fitness_atlas] It proposes repeating the conservation analysis with condition-specific genes only. [src: metal_fitness_atlas] See [[concepts/core-genome-enrichment-of-metal-stress-fitness-genes]] and [[concepts/metal-tolerance-determinants-and-shared-stress-confounding]].

## Conservation by tier

In metal_cross_resistance, conservation falls from general stress to metal-shared to metal-specific. Mean core percentage is 92.0%, 91.0% and 89.8%. Fully core (≥95%) percentage is 57.2%, 50.4% and 45.7%. [src: metal_cross_resistance] The report says the predicted gradient holds. [src: metal_cross_resistance]

## Per-metal differences

Specificity varies by metal. Iron is lowest at 21.9% (144/659 records), which the report suggests reflects its central role in core metabolism. [src: metal_specificity] Toxic metals range from 42-56% metal-specific. [src: metal_specificity] Essential metals show 47-61% once DvH is included. [src: discoveries] With DvH included, manganese is 60.6%, molybdenum 60.5%, tungsten 56.5% and selenium 46.4%. [src: metal_specificity]

Among toxic metals, nickel has 993/2,271 records metal-specific (43.7%) [src: metal_specificity], aluminum 752/1,772 (42.4%) [src: metal_specificity] and mercury 35/107 (32.7%). [src: metal_specificity]

| Metal | Class | Metal-specific records | % |
|---|---|---|---|
| Manganese | essential | 20/33 | 60.6% [src: metal_specificity] |
| Molybdenum | essential | 185/306 | 60.5% [src: metal_specificity] |
| Tungsten | essential | 173/306 | 56.5% [src: metal_specificity] |
| Cadmium | toxic | 52/93 | 55.9% [src: metal_specificity] |
| Copper | toxic | 1,346/2,594 | 51.9% [src: metal_specificity] |
| Cobalt | toxic | 1,167/2,324 | 50.2% [src: metal_specificity] |
| Chromium | toxic | 132/268 | 49.3% [src: metal_specificity] |
| Uranium | toxic | 88/181 | 48.6% [src: metal_specificity] |
| Zinc | toxic | 843/1,786 | 47.2% [src: metal_specificity] |
| Selenium | essential | 64/138 | 46.4% [src: metal_specificity] |
| Nickel | toxic | 993/2,271 | 43.7% [src: metal_specificity] |
| Aluminum | toxic | 752/1,772 | 42.4% [src: metal_specificity] |
| Mercury | toxic | 35/107 | 32.7% [src: metal_specificity] |
| Iron | essential | 144/659 | 21.9% [src: metal_specificity] |

An early analysis showed 0% specificity for Mo, W, Se and Mn. A locusId type mismatch had silently excluded DvH, which has 608 non-metal experiments. After the fix, the discoveries digest gives Mn 61%, Mo 61%, W 57% and Se 46%. [src: discoveries] The digest also says the experiment-count bias is real but less severe than first thought. [src: discoveries]

## Desulfovibrio vulgaris Hildenborough example

In [[entities/desulfovibrio-vulgaris-hildenborough|DvH]], counter_ion_effects found 495 unique metal-important genes. Of these, 73 (14.7%) were shared-stress and 422 (85.3%) metal-specific. [src: counter_ion_effects] Shared-stress genes were important for a mean 4.1 metals per gene versus 2.5 for metal-specific genes, consistent with broad cellular vulnerability. [src: counter_ion_effects] SEED annotations covered 90.5% of metal-specific genes and 78.1% of shared-stress genes. [src: counter_ion_effects] The report suggests, as interpretation, that metal-specific genes include Ni/Fe-hydrogenase, nitrogenase regulators and metal transporters. It suggests shared-stress genes include more uncharacterized general-stress proteins. [src: counter_ion_effects]

## Threshold robustness and validation

The 5% sick-rate threshold is arbitrary. Results are qualitatively stable across 1-20%, but exact fractions vary. [src: metal_specificity] About 41% are metal-specific at a 2% sick rate and ~67% at 10%. [src: metal_specificity]

Cross-validation against counter_ion_effects gives a gap. That project found 39.8% overlap between metal-important and NaCl-stress genes. [src: metal_specificity] metal_specificity finds 14.7% of metal-important genes sick under osmotic stress, a 2.7x discrepancy. [src: metal_specificity] The report attributes this to its stricter threshold (fit < -1 AND |t| > 4) versus fit < -1 only, and to partly different organism sets. [src: metal_specificity] It reads the directional agreement as supporting both analyses. [src: metal_specificity] It proposes matching the counter_ion_effects threshold (fit < -1 without |t| > 4) to validate the osmotic overlap. [src: metal_specificity] See [[concepts/shared-metal-and-osmotic-stress-fitness-determinants]].

## Caveats

- The shared-stress versus metal-specific split was not formally tested for functional enrichment, and the SEED comparison is descriptive. [src: counter_ion_effects]
- The counter_ion_effects report proposes testing, with COG (clusters of orthologous groups), KEGG and PFAM annotations, whether shared-stress genes are enriched for envelope/transport functions and metal-specific genes for metal-binding/efflux. [src: counter_ion_effects]
- Validation against the [[entities/fitness-browser|Fitness Browser]] specificphenotype table was planned but not completed. [src: metal_specificity]
- Matching the counter_ion_effects methodology exactly would strengthen cross-validation. [src: metal_specificity]

## Open Directions

- Run the COG, KEGG and PFAM enrichment test described above. It closes the gap that only descriptive SEED comparisons exist.
- Rerun the specificity classification with fit < -1 without |t| > 4, to see whether the osmotic overlap gap closes.
- Validate the classes against the Fitness Browser specificphenotype annotations.
- Repeat the conservation analysis on condition-specific genes only, to separate the core stress signal from metal-resistance evolution.
