---
type: "Summary"
description: "Summary of the metal_specificity project, which classifies metal-important fitness genes from 24 organisms as metal-specific, metal+stress, or general sick, and tests their conservation, functional enrichment, candidate families, and module behavior."
doc_type: "short"
full_text: "sources/metal_specificity__REPORT.md"
---
# Metal-Specific vs General Stress Genes

## Overview

This project classified metal-important genes by comparing fitness defects under metal experiments with sick rates across non-metal experiments, then tested their conservation, functional enrichment, candidate specificity, and module-level behavior. The analysis included 6,504 experiments, 559 metal experiments (8.6%), 5,945 non-metal experiments (91.4%), and 7,609 metal-important gene records from 24 organisms. [src: metal_specificity]

## Key Findings

### Metal specificity is common

Of 7,609 metal-important gene records with fitness-matrix data, 4,177 (54.9%) were metal-specific: they showed significant fitness defects under metal stress but a <5% sick rate across 5,945 non-metal experiments. A further 2,888 (38.0%) were general sick and 544 (7.2%) were metal+stress. At a 2% sick-rate threshold, approximately 41% were metal-specific; at 10%, approximately 67% were metal-specific. [src: metal_specificity]

Seven of 31 metal-tested organisms (ANA3, Dino, Keio, MR1, Miya, PV4, and SB2B) could not be processed because their metal-important gene locusIds did not match the fitness-matrix index format. The 24 included organisms accounted for 7,609 of 12,838 metal-important gene records (59.3%); 5,229 gene records were excluded. [src: metal_specificity]

Specificity varied by metal. Metal-specific fractions were 60.6% for manganese (20/33), 60.5% for molybdenum (185/306), 56.5% for tungsten (173/306), 46.4% for selenium (64/138), 55.9% for cadmium (52/93), 51.9% for copper (1,346/2,594), 50.2% for cobalt (1,167/2,324), 49.3% for chromium (132/268), 48.6% for uranium (88/181), 47.2% for zinc (843/1,786), 43.7% for nickel (993/2,271), 42.4% for aluminum (752/1,772), 32.7% for mercury (35/107), and 21.9% for iron (144/659). The report's table labels manganese, molybdenum, tungsten, selenium, and iron as essential metals and the rest as toxic. Its prose states that, with DvH now included, essential metals show substantial specificity: Manganese (60.6%), Molybdenum (60.5%), Tungsten (56.5%), Selenium (46.4%). The prose also states that toxic metals range from 42-56% metal-specific and that iron is lowest at 21.9%. It attributes the iron value to iron's central role in core metabolism, which is an interpretation, not a tested result. The stated toxic-metal range conflicts with the report's own table, which lists mercury, a toxic metal, at 35/107 (32.7%). The source does not reconcile this internal inconsistency. [src: metal_specificity]

### Metal-specific genes are core-enriched but less so than general sick genes

Core fractions across the 22 organisms with pangenome links were reported both as pooled values (total core / total genes) and as organism means (mean of per-organism core fractions). Across these 22 organisms, metal-specific genes had a pooled core fraction of 84.8% (2,969/3,500) and an organism-mean core fraction of 88.0%, with a mean delta versus baseline of +6.9%; 19/22 organisms had positive deltas and 12/22 showed significant enrichment. Metal+stress genes had pooled and organism-mean core fractions of 94.3% (467/495) and 93.6%, respectively, with a mean delta of +10.9%; 13/13 organisms had positive deltas and 1/13 showed significant enrichment. General sick genes had pooled and organism-mean core fractions of 90.2% (2,183/2,420), with a mean delta of +9.0%; 21/21 organisms had positive deltas and 8/21 showed significant enrichment. The baseline was 79.8% (73,957/92,650) pooled and 81.1% organism-mean. The pooled metal-specific core fraction (84.8%) is lower than the organism mean (88.0%). The report attributes this gap to the influence of organisms with large gene sets and lower core fractions. [src: metal_specificity]

All three categories were significantly core-enriched above baseline. Metal-specific genes were less core-enriched than general sick genes, and the Cochran-Mantel-Haenszel test comparing them across organisms was significant (p=0.011). This supports a modest two-tier model in which general stress functions are more core-enriched than specialized metal resistance functions, while both remain strongly core-associated. [src: metal_specificity]

Approximately 14% of protein-coding genes, estimated at approximately 82% core, were putatively essential and absent from fitness data; this biases all categories toward core enrichment. The report states that the true baseline core fraction is therefore likely lower than 81%, which would make the reported deltas conservative. [src: metal_specificity]

### Metal-specific genes are enriched for metal-resistance functions

Metal-specific genes matched metal-resistance keywords (efflux, transporter, metal, CDF, siderophore, etc.) at 12.2% versus 7.8% for general sick genes, based on annotated gene sets of 3,344 metal-specific and 2,573 general sick genes. The report gives this as Fisher exact OR=1.64 and p=2.4e-8. Among 495 annotated metal+stress genes, 8.9% matched metal-resistance keywords. General-stress keyword matches were 13.7% for metal-specific genes, 6.5% for metal+stress genes, and 11.5% for general sick genes. The report's prose says general sick genes show slightly higher enrichment for general-stress keywords (DNA repair, cell wall, chaperone, etc.). However, the values it cites (11.5% vs 13.7%) and its table point the other way: the table assigns 13.7% to metal-specific genes and 11.5% to general sick genes. The source does not resolve this internal inconsistency. These results support the biological distinction between metal-specific determinants and broadly pleiotropic stress genes. [src: metal_specificity]

### Candidate specificity prioritizes three novel families

Candidate-family specificity is reported as the number of metal-specific records out of all records for the family. UCP030820 (OG01015; 3 organisms, 7 metals) was metal-specific in 2/3 records (67%) with a mean sick rate of 0.021. YebC (OG01383; 11 organisms, 6 metals) was metal-specific in 7/12 records (58%) with a mean sick rate of 0.056. DUF1043/YhcB (OG03264; 6 organisms, 5 metals) was metal-specific in 3/6 records (50%) with a mean sick rate of 0.054. [src: metal_specificity]

UPF0042/RapZ (OG02094; 8 organisms, 7 metals) was metal-specific in 2/8 records (25%) with a mean sick rate of 0.130. MlaD (OG04003; 4 organisms, 4 metals) was metal-specific in 1/4 records (25%) with a mean sick rate of 0.113. YfdZ (OG00391; 7 organisms, 9 metals) was metal-specific in 2/13 records (15%) with a mean sick rate of 0.268. YrbC (OG02233; 8 organisms, 4 metals) was metal-specific in 1/9 records (11%) with a mean sick rate of 0.234. Two families had no metal-specific records: DUF39 (OG08209; 2 organisms, 8 metals) at 0/2 (0%) with a mean sick rate of 0.637, and YrbE (OG03534; 6 organisms, 5 metals) at 0/6 (0%) with a mean sick rate of 0.190. [src: metal_specificity]

The report prioritizes UCP030820, YebC, and DUF1043/YhcB as the strongest candidates because they combine 50–67% metal-specificity with lower pleiotropic effects across multiple species. It describes UCP030820 (67%) as an oxidoreductase involved in sulfite reduction that is important for 7 metals, including Cd and Cr. It describes DUF1043/YhcB (50%) as a cell division/envelope coordination protein. The report deprioritizes YfdZ and the Mla/Yrb system (YrbC/D/E) because they are more pleiotropic: they are sick under many non-metal conditions. It attributes YfdZ's high sick rate (0.268) to its known role in alanine biosynthesis. It interprets the Mla system's pleiotropic defects as consistent with its established function in maintaining outer membrane integrity under diverse stresses. DUF39 showed 0% metal-specificity (sick rate 0.637). Because it is important for many conditions, not just metals, the report treats it as a general fitness factor rather than a specific metal-tolerance determinant. [src: metal_specificity]

The report cites Ignatov et al. (2025) as showing that YebC functions as a translation factor for proline-rich proteins, resolving ribosome stalling at polyproline motifs. YebC's proposed metal-stress mechanism is explicitly a hypothesis that this analysis did not test: because YebC functions as a translation factor for proline-rich proteins, and several metal-homeostasis proteins contain proline-rich regions, metal-induced demand for these transporters could create a translation bottleneck that YebC resolves. [src: metal_specificity]

### Novel candidates are less metal-specific than annotated families

Among 149 novel metal-candidate families, 45.6% had a dominant specificity of metal-specific, compared with 58.2% of annotated families; Fisher exact testing gave OR=0.60 and p=0.003. The report attributes this difference to the composition of the novel set. Many novel candidates were identified in deeply profiled organisms (DvH, Btheta, psRCH2). In those organisms, the high experiment count provides more opportunities to detect pleiotropic effects and pushes genes toward "general sick." The comparison is therefore qualified by this sampling difference. [src: metal_specificity]

### Module analysis was inconclusive

The independent component analysis (ICA), a method for decomposing activity profiles into modules, identified 0 metal-specific modules. Per-module z-normalization produced maximum absolute z values <2.0 for most metal experiments because metal experiments were a small fraction of each organism's experiments. The report notes that raw module-condition scores used here were on a different scale from the precomputed z-scored profiles that identified 600 metal-responsive module records in the Metal Atlas analysis. [src: metal_specificity]

### Counter-ion comparison supports directional agreement

The counter-ion analysis reported 39.8% overlap between metal-important and NaCl-stress genes, whereas this analysis found 14.7% of metal-important genes sick under osmotic stress, a 2.7x discrepancy. The report attributes most of the difference to the stricter threshold used here (fit < -1 and |t| > 4 rather than fit < -1 alone) and partially different organism sets; the direction of the overlap supports both analyses. [src: metal_specificity]

## Caveats and Open Work

The analysis had 40.7% gene attrition: 7 organisms and 5,229 gene records were excluded because of locusId format mismatches between the metal atlas and fitness matrices. The excluded organisms were ANA3, Dino, Keio, MR1, Miya, PV4, and SB2B, including important model organisms such as Keio (*E. coli*), MR1 (*Shewanella*), and ANA3. The report cautions that excluded genes may have different specificity profiles. Elsewhere it states that the excluded organisms are taxonomically diverse and that their absence is not expected to introduce systematic bias. The report asserts this expectation but does not test it empirically. [src: metal_specificity]

The 5% sick-rate threshold is arbitrary: results were qualitatively stable across 1–20%, but exact fractions varied. The planned validation against the Fitness Browser's built-in `specificphenotype` annotations was not performed. [src: metal_specificity]

The ICA module analysis failed to identify metal-specific modules; the proposed correction is to use precomputed z-scored module activities from Metal Atlas NB05. Further work should also resolve the integer-versus-string locusId mismatch for ANA3, Dino, Keio, MR1, Miya, PV4, and SB2B; the report says this would recover the remaining 40% of gene records. It should also use the Fitness Browser's built-in `specificphenotype` condition-specificity annotations as an independent validation. The counter_ion_effects methodology should be replicated exactly (fit < -1 without |t| > 4) to validate the osmotic overlap. Finally, AlphaFold predictions should be used to identify metal-binding sites in the top metal-specific candidates (UCP030820, YebC, DUF1043). This structural analysis is proposed work; the report gives no structural result. [src: metal_specificity]

## Cited Literature and Related Reports

The report cites three papers:
- Price MN et al. (2018), "Mutant phenotypes for thousands of bacterial genes of unknown function" (*Nature* 557:503-509; PMID: 29769716).
- Wu et al. (2019), which reports that the RuvRCAB operon contributes to resistance against Cr(VI), As(III), Sb(III), and Cd(II) (*Appl Microbiol Biotechnol* 103:2489-2500; PMID: 30729256). This is cited literature, not a result of this analysis.
- Ignatov et al. (2025), which identifies YebC as a ribosome-associated translation factor for proline-rich proteins (*Nature Communications*; PMID: 40624002). [src: metal_specificity]

It also references two related observatory reports: the Metal Fitness Atlas ([[summaries/metal_fitness_atlas__REPORT]]) and Counter Ion Effects ([[summaries/counter_ion_effects__REPORT]]). [src: metal_specificity]

## Figures

- `experiment_classification.png`: experiment category distribution and per-organism breakdown.
- `specificity_breakdown.png`: stacked bar of metal-specific versus general sick by organism.
- `threshold_sensitivity.png`: classification stability across 1-20% sick-rate thresholds.
- `conservation_by_specificity.png`: core-fraction boxplots by specificity category.
- `functional_comparison.png`: keyword enrichment and module specificity. [src: metal_specificity]

## Slots Into

- [[concepts/metal-cross-resistance]] — distinguishes metal-specific fitness determinants from genes that respond to metals and other stresses, and compares metal–osmotic overlap.
- [[concepts/condition-specific-fitness]] — provides a cross-condition classification of 7,609 metal-important gene records using metal and non-metal sick rates. [src: metal_specificity]
- [[concepts/gene-essentiality]] — shows that putatively essential genes are absent from fitness data and bias conservation estimates toward the core genome.
- [[concepts/environmental-resistome]] — prioritizes metal-resistance candidates and quantifies the contribution of core and accessory genes to metal tolerance.
- [[concepts/shared-stress-versus-stressor-specific-fitness]] — 54.9% metal-specific versus 38.0% general sick classification, threshold sensitivity, keyword enrichment (including the source's internal inconsistency on general-stress keywords), and per-family pleiotropy. [src: metal_specificity]
- [[concepts/pangenome-conservation-fitness-decoupling]] — all specificity classes are core-enriched, but metal-specific genes are less so than general sick genes (CMH p=0.011); also covers the pooled versus organism-mean and essential-gene biases. [src: metal_specificity]
- [[concepts/transposon-callability-bias]] — putatively essential genes absent from fitness data bias core-fraction baselines.
- [[concepts/genetic-perturbation-coverage-bias]] — locusId format mismatches excluded 7 of 31 organisms, including Keio and MR1. [src: metal_specificity]
- [[concepts/pangenome-integration]] — identifier-format mismatches between metal-important gene lists and fitness-matrix indices block cross-dataset joins.
- [[concepts/experimental-prioritization-of-functional-dark-matter]] — UCP030820, YebC, and DUF1043/YhcB are prioritized as candidates; novel families are less often metal-specific than annotated families.
- [[concepts/fitness-condition-coverage-prioritization-bias]] — metal experiments are a small share of all experiments, and deeply profiled organisms push novel candidates toward "general sick."
- [[concepts/fitness-module-detection-sensitivity]] — 0 metal-specific modules under per-module z-normalization, versus 600 metal-responsive module records on the Metal Atlas scale. [src: metal_specificity]
- [[concepts/ontology-and-category-schema-sensitivity]] — threshold definitions drive the 39.8% versus 14.7% metal–osmotic overlap discrepancy. [src: metal_specificity]
- [[concepts/condition-dependent-gene-tradeoffs]] — YfdZ and the Mla/Yrb system are sick across many non-metal conditions.
- [[concepts/outer-membrane-lipid-homeostasis]] — the Mla system's pleiotropic metal and non-metal defects are interpreted through outer-membrane maintenance.
