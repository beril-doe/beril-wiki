---
type: "Summary"
description: "Summary of the project Metal-Specific vs General Stress Genes."
doc_type: "short"
full_text: "sources/metal_specificity__REPORT.md"
---
# Metal-Specific vs General Stress Genes

This page summarizes the project Metal-Specific vs General Stress Genes. It asks which metal-important genes are specific to metal stress and which are general stress genes. In 24 organisms, 4,177 of 7,609 metal-important gene records (54.9%) are metal-specific. [src: metal_specificity] Metal-specific genes are slightly less core-genome-enriched than general sick genes (Cochran-Mantel-Haenszel p=0.011). [src: metal_specificity] The module-level analysis found 0 metal-specific ICA modules. [src: metal_specificity] Seven of 31 metal-tested organisms could not be processed. [src: metal_specificity] The report concludes that the Metal Atlas's 87.4% core finding is not an artifact of general stress genes, and that its two-tier model is only partially supported. [src: metal_specificity] See [[concepts/metal-specific-versus-pleiotropic-stress-gene-classification]].

## Key Findings

### Classification of metal-important genes

Most metal-important gene records are metal-specific, and the result holds across sick-rate thresholds. Of 7,609 records in 24 organisms (of 12,838 atlas total, 59.3%), 4,177 (54.9%) are metal-specific. [src: metal_specificity] They show significant fitness defects under metal stress but a <5% sick rate across 5,945 non-metal experiments. [src: metal_specificity] The rest are general sick (2,888, 38.0%) and metal+stress (544, 7.2%). [src: metal_specificity] At a 2% sick rate ~41% are metal-specific, and at 10% ~67% are. [src: metal_specificity] The report calls the 5% threshold arbitrary and says results are qualitatively stable across 1-20% while exact fractions vary. [src: metal_specificity] The dataset classified 6,504 experiments in total. Of these, 559 (8.6%) were metal experiments and 5,945 (91.4%) were non-metal. [src: metal_specificity]

Specificity varies by metal. With DvH included, essential metals show substantial specificity: Manganese 60.6%, Molybdenum 60.5%, Tungsten 56.5% and Selenium 46.4%. [src: metal_specificity] Toxic metals range from 42-56% metal-specific. [src: metal_specificity] Mercury, also categorized as toxic, is lower at 32.7% (35/107). [src: metal_specificity] Iron is lowest at 21.9%, which the report suggests likely reflects its central role in core metabolism. [src: metal_specificity]

| Metal | Category | Metal-specific / metal-important records | Percent |
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

The report interprets genes important only for metals, and not for antibiotics, osmotic stress, carbon sources or other conditions, as the bona fide metal resistance repertoire. It says this validates the cross-species approach. [src: metal_specificity]

### Core-genome conservation

All three specificity categories are significantly core-enriched above baseline. Metal-specific genes are the least enriched, consistent with a modest tendency for specialized metal-resistance mechanisms to sit in the accessory genome. [src: metal_specificity] Figures cover the 22 organisms with pangenome links. They are given as pooled core fractions (total core / total genes) and organism-mean core fractions. [src: metal_specificity]

| Category | Pooled core fraction | Organism mean | Mean delta vs baseline | Positive/total | Significant/total |
|---|---|---|---|---|---|
| Metal-specific | 84.8% (2,969/3,500) | 88.0% | +6.9% | 19/22 | 12/22 [src: metal_specificity] |
| Metal+stress | 94.3% (467/495) | 93.6% | +10.9% | 13/13 | 1/13 [src: metal_specificity] |
| General sick | 90.2% (2,183/2,420) | 90.2% | +9.0% | 21/21 | 8/21 [src: metal_specificity] |
| Baseline | 79.8% (73,957/92,650) | 81.1% | — | — | — [src: metal_specificity] |

The pooled metal-specific fraction is lower than the organism mean. The report says this reflects organisms with large gene sets and lower core fractions. [src: metal_specificity] A Cochran-Mantel-Haenszel test finds metal-specific genes less core-enriched than general sick genes across organisms (p=0.011). [src: metal_specificity] The report states metal-specific genes are core-enriched (88.0% vs 81.1% baseline) but less so than general sick genes (90.2%). [src: metal_specificity] It calls the difference modest [src: metal_specificity], and concludes that specialized metal resistance genes are slightly more likely to reside in the accessory genome than general stress genes. [src: metal_specificity]

The report argues the Metal Atlas's 87.4% core finding was not inflated by general stress genes, because removing all pleiotropic genes leaves a metal-specific set that is 88% core. [src: metal_specificity] It reads the 2% gap between metal-specific (88%) and general sick genes (90.2%) as a detectable accessory-genome contribution. [src: metal_specificity] It judges the Metal Atlas two-tier model partially supported: general stress is more core than specific resistance, but both tiers are strongly core-enriched and the accessory contribution is small. [src: metal_specificity]

Putatively essential genes are ~14% of protein-coding genes (~82% core) and are absent from fitness data. This biases all categories toward core enrichment, so the true baseline is likely below 81% and the deltas are conservative. [src: metal_specificity]

### Functional keywords

Metal-specific genes are 1.64x more likely than general sick genes to match metal-resistance keywords such as efflux, transporter, metal, CDF and siderophore (12.2% vs 7.8%, Fisher exact OR=1.64, p=2.4e-8). [src: metal_specificity] The keyword rates are based on 3,344 annotated metal-specific genes (12.2% metal-resistance, 13.7% general-stress), 495 annotated metal+stress genes (8.9% and 6.5%) and 2,573 annotated general sick genes (7.8% and 11.5%). [src: metal_specificity] General sick genes are slightly more enriched for general-stress keywords such as DNA repair, cell wall and chaperone (11.5% vs 13.7%, metal-specific vs general sick). [src: metal_specificity] The report concludes that the classification captures biologically meaningful categories. [src: metal_specificity] It reads the enrichment as confirming that metal-specific genes are genuine metal tolerance determinants rather than general stress genes that also affect metal survival. [src: metal_specificity]

### Novel metal candidates

Novel candidates are less metal-specific than annotated families. Across all 149 novel candidate families, 45.6% have metal-specific as their dominant specificity, versus 58.2% for annotated families (Fisher exact OR=0.60, p=0.003). [src: metal_specificity] The report attributes this to many novel candidates coming from deeply profiled organisms (DvH, Btheta, psRCH2). There the high experiment count gives more chances to detect pleiotropic effects, which pushes genes toward general sick. [src: metal_specificity]

| Candidate | Orgs, metals | Metal-specific/total | Fraction | Mean sick rate |
|---|---|---|---|---|
| UCP030820 (OG01015) | 3, 7 | 2/3 | 67% | 0.021 [src: metal_specificity] |
| YebC (OG01383) | 11, 6 | 7/12 | 58% | 0.056 [src: metal_specificity] |
| DUF1043/YhcB (OG03264) | 6, 5 | 3/6 | 50% | 0.054 [src: metal_specificity] |
| UPF0042/RapZ (OG02094) | 8, 7 | 2/8 | 25% | 0.130 [src: metal_specificity] |
| MlaD (OG04003) | 4, 4 | 1/4 | 25% | 0.113 [src: metal_specificity] |
| YfdZ (OG00391) | 7, 9 | 2/13 | 15% | 0.268 [src: metal_specificity] |
| YrbC (OG02233) | 8, 4 | 1/9 | 11% | 0.234 [src: metal_specificity] |
| DUF39 (OG08209) | 2, 8 | 0/2 | 0% | 0.637 [src: metal_specificity] |
| YrbE (OG03534) | 6, 5 | 0/6 | 0% | 0.190 [src: metal_specificity] |

The report prioritizes UCP030820, YebC and DUF1043 as the strongest novel candidates, citing metal-specificity of 50-67%, low pleiotropic effects, and validation across multiple species. [src: metal_specificity] UCP030820 is an oxidoreductase involved in sulfite reduction and important for 7 metals including Cd and Cr. [src: metal_specificity] [[entities/yebc|YebC]] is a transcriptional regulator/translation factor. [src: metal_specificity] DUF1043/YhcB is a cell division/envelope coordination protein. [src: metal_specificity]

The report offers a hypothesis for YebC. Ignatov et al. (2025) showed YebC is a translation factor for proline-rich proteins that resolves ribosome stalling at polyproline motifs. [src: metal_specificity] Many metal homeostasis proteins contain proline-rich cytoplasmic-loop regions. Examples are the P-type ATPases CopA and ZntA, the CDF transporter CzcD, and metal-binding chaperones. [src: metal_specificity] The hypothesis is that metal-induced demand for these transporters creates a translation bottleneck that YebC resolves. [src: metal_specificity] Under non-metal conditions the transporters are not highly expressed, so YebC would be dispensable. [src: metal_specificity]

YfdZ and the Mla/Yrb system (YrbC/D/E) are more pleiotropic and sick under many non-metal conditions. [src: metal_specificity] The report deprioritizes YfdZ and Mla/Yrb because high pleiotropic effects suggest general fitness factors with incidental metal phenotypes. [src: metal_specificity] It attributes YfdZ's high sick rate (0.268) to its known role in alanine biosynthesis. [src: metal_specificity] It says the Mla system's defects fit its established role in maintaining outer membrane integrity under diverse stresses. [src: metal_specificity] Despite spanning 8 metals, DUF39 appears to be a general fitness factor (sick rate 0.637) rather than a specific metal-tolerance determinant. [src: metal_specificity]

### Module-level analysis (null result)

The module-level analysis using z-scored activity profiles found 0 metal-specific ICA (independent component analysis) modules. [src: metal_specificity] Per-module z-normalization gives max |z| < 2.0 for most metal experiments, because metal experiments are a small fraction of each organism's experiments. [src: metal_specificity] Raw activity scores are on a different scale from the z-scored profiles used in Metal Atlas NB05, which identified 600 metal-responsive module records. [src: metal_specificity] The report recommends using the atlas's pre-computed z-scores directly in a revision. [src: metal_specificity]

### Cross-validation with counter_ion_effects

The counter_ion_effects project found 39.8% overlap between metal-important and NaCl-stress genes. [src: metal_specificity] This analysis finds 14.7% of metal-important genes sick under osmotic stress, a 2.7x discrepancy. [src: metal_specificity] The report attributes the gap to its stricter threshold (fit < -1 AND |t| > 4, versus fit < -1 only) and to partly different organism sets. [src: metal_specificity] It says threshold stringency explains most of the gap, and that matching the counter_ion_effects methodology exactly would strengthen the validation. [src: metal_specificity] It reads the directional agreement as supporting the validity of both analyses. [src: metal_specificity]

## Data and Methods

The analysis uses fitness matrices from 24 organisms, fully analyzed out of 31 with metal data. [src: metal_specificity] Gene specificity is analysed in notebook 02_gene_specificity.ipynb. [src: metal_specificity] Conservation is analysed in 03_conservation_analysis.ipynb. [src: metal_specificity] Functional enrichment and the novel-candidate analyses are in 04_functional_enrichment.ipynb. [src: metal_specificity]

## Caveats and Open Work

- Seven of 31 metal-tested organisms (ANA3, Dino, Keio, MR1, Miya, PV4, SB2B) could not be processed. Their metal-important gene locusIds did not match the fitness matrix index format. [src: metal_specificity]
- The report notes 40.7% gene attrition: 5,229 gene records were excluded for locusId mismatches. The excluded organisms include the important model organisms Keio (Escherichia coli), MR1 (Shewanella) and ANA3, and the excluded genes may have different specificity profiles. [src: metal_specificity]
- The 24 included organisms account for 7,609 of 12,838 metal-important gene records (59.3%). [src: metal_specificity]
- The report considers the excluded organisms taxonomically diverse and does not expect systematic bias from their absence. [src: metal_specificity]
- Planned validation against the Fitness Browser specificphenotype table's built-in condition-specificity annotations was not completed. [src: metal_specificity]
- Genes absent from fitness data (~14%, ~82% core) bias all conservation estimates toward core enrichment. [src: metal_specificity]
- The 5% sick-rate threshold is arbitrary; exact fractions vary across 1-20%. [src: metal_specificity]
- The osmotic-overlap comparison with counter_ion_effects differs in threshold stringency. [src: metal_specificity]
- Proposed next steps: fix the integer-vs-string locusId format for the excluded organisms to recover the remaining 40% of gene records. [src: metal_specificity] Validate specificity against the specificphenotype table. [src: metal_specificity] Rerun the ICA module analysis with the atlas's pre-computed z-scores. [src: metal_specificity] Replicate the counter_ion_effects threshold (fit < -1 without |t| > 4) to validate the osmotic overlap. [src: metal_specificity] Use AlphaFold predictions to find metal-binding sites in UCP030820, YebC and DUF1043. [src: metal_specificity]

## Slots Into

- [[concepts/metal-specific-versus-pleiotropic-stress-gene-classification]]: 54.9% of metal-important records are metal-specific, and the result is threshold-robust. [src: metal_specificity]
- [[concepts/core-genome-enrichment-of-metal-stress-fitness-genes]]: metal-specific genes are the least core-enriched category (CMH p=0.011). [src: metal_specificity]
- [[concepts/conserved-metal-phenotype-gene-families-and-novel-metal-tolerance-candidates]]: novel candidates are less metal-specific than annotated families (45.6% vs 58.2%). [src: metal_specificity]
- [[concepts/shared-metal-and-osmotic-stress-fitness-determinants]]: 14.7% of metal-important genes are sick under osmotic stress, versus 39.8% overlap in counter_ion_effects. [src: metal_specificity]
- [[concepts/metal-responsive-ica-fitness-modules]]: the z-scored module analysis found 0 metal-specific modules. [src: metal_specificity]
- [[concepts/organism-coverage-and-attrition-in-cross-organism-fitness-conservation-analyses]]: 7 of 31 organisms were lost to locusId mismatch. [src: metal_specificity]
- [[concepts/essential-genes-as-a-blind-spot-of-transposon-fitness-screens]]: putatively essential genes are absent from the fitness data and bias results toward core enrichment. [src: metal_specificity]
