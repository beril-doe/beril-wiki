---
type: "Summary"
description: "Classifies metal-important genes as metal-specific or general stress determinants."
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

Specificity varied by metal. Metal-specific fractions were 60.6% for manganese (20/33), 60.5% for molybdenum (185/306), 56.5% for tungsten (173/306), 46.4% for selenium (64/138), 55.9% for cadmium (52/93), 51.9% for copper (1,346/2,594), 50.2% for cobalt (1,167/2,324), 49.3% for chromium (132/268), 48.6% for uranium (88/181), 47.2% for zinc (843/1,786), 43.7% for nickel (993/2,271), 42.4% for aluminum (752/1,772), 32.7% for mercury (35/107), and 21.9% for iron (144/659). [src: metal_specificity]

### Metal-specific genes are core-enriched but less so than general sick genes

Across 22 organisms with pangenome links, metal-specific genes had a pooled core fraction of 84.8% (2,969/3,500) and an organism-mean core fraction of 88.0%, with a mean delta versus baseline of +6.9%; 19/22 organisms had positive deltas and 12/22 showed significant enrichment. Metal+stress genes had pooled and organism-mean core fractions of 94.3% (467/495) and 93.6%, respectively, with a mean delta of +10.9%; 13/13 organisms had positive deltas and 1/13 showed significant enrichment. General sick genes had pooled and organism-mean core fractions of 90.2% (2,183/2,420), with a mean delta of +9.0%; 21/21 organisms had positive deltas and 8/21 showed significant enrichment. The baseline was 79.8% (73,957/92,650) pooled and 81.1% organism-mean. [src: metal_specificity]

All three categories were significantly core-enriched above baseline. Metal-specific genes were less core-enriched than general sick genes, and the Cochran-Mantel-Haenszel test comparing them across organisms was significant (p=0.011). This supports a modest two-tier model in which general stress functions are more core-enriched than specialized metal resistance functions, while both remain strongly core-associated. [src: metal_specificity]

Approximately 14% of protein-coding genes, estimated at approximately 82% core, were putatively essential and absent from fitness data; this biases all categories toward core enrichment and makes the reported deltas conservative. [src: metal_specificity]

### Metal-specific genes are enriched for metal-resistance functions

Metal-specific genes matched metal-resistance keywords at 12.2% versus 7.8% for general sick genes, corresponding to Fisher exact OR=1.64 and p=2.4e-8. General-stress keyword matches were 13.7% for metal-specific genes, 6.5% for metal+stress genes, and 11.5% for general sick genes. These results support the biological distinction between metal-specific determinants and broadly pleiotropic stress genes. [src: metal_specificity]

### Candidate specificity prioritizes three novel families

UCP030820 (OG01015) was metal-specific in 2/3 organisms across 7 metals (67%) with a mean sick rate of 0.021; YebC (OG01383) was metal-specific in 7/12 organisms across 6 metals (58%) with a mean sick rate of 0.056; and DUF1043/YhcB (OG03264) was metal-specific in 3/6 organisms across 5 metals (50%) with a mean sick rate of 0.054. [src: metal_specificity]

UPF0042/RapZ (OG02094) was metal-specific in 2/8 organisms across 7 metals (25%) with a mean sick rate of 0.130; MlaD (OG04003) in 1/4 organisms across 4 metals (25%) with a mean sick rate of 0.113; YfdZ (OG00391) in 2/13 organisms across 9 metals (15%) with a mean sick rate of 0.268; YrbC (OG02233) in 1/9 organisms across 4 metals (11%) with a mean sick rate of 0.234; DUF39 (OG08209) in 0/2 organisms across 8 metals (0%) with a mean sick rate of 0.637; and YrbE (OG03534) in 0/6 organisms across 5 metals (0%) with a mean sick rate of 0.190. [src: metal_specificity]

The report prioritizes UCP030820, YebC, and DUF1043/YhcB as the strongest candidates because they combine 50–67% metal-specificity with lower pleiotropic effects across multiple species. It deprioritizes YfdZ and the Mla/Yrb system because their fitness defects are more pleiotropic, and interprets DUF39 as a general fitness factor rather than a specific metal-tolerance determinant. [src: metal_specificity]

YebC's proposed mechanism is explicitly a hypothesis: because YebC functions as a translation factor for proline-rich proteins, and several metal-homeostasis proteins contain proline-rich regions, metal-induced demand for these transporters could create a translation bottleneck that YebC resolves. [src: metal_specificity]

### Novel candidates are less metal-specific than annotated families

Among 149 novel metal-candidate families, 45.6% had a dominant specificity of metal-specific, compared with 58.2% of annotated families; Fisher exact testing gave OR=0.60 and p=0.003. The report attributes this difference to the composition of the novel set, including deeply profiled organisms in which more experiments provide more opportunities to detect pleiotropic effects. [src: metal_specificity]

### Module analysis was inconclusive

The independent component analysis (ICA), a method for decomposing activity profiles into modules, identified 0 metal-specific modules. Per-module z-normalization produced maximum absolute z values <2.0 for most metal experiments because metal experiments were a small fraction of each organism's experiments. The report notes that raw module-condition scores used here were on a different scale from the precomputed z-scored profiles that identified 600 metal-responsive module records in the Metal Atlas analysis. [src: metal_specificity]

### Counter-ion comparison supports directional agreement

The counter-ion analysis reported 39.8% overlap between metal-important and NaCl-stress genes, whereas this analysis found 14.7% of metal-important genes sick under osmotic stress, a 2.7x discrepancy. The report attributes most of the difference to the stricter threshold used here (fit < -1 and |t| > 4 rather than fit < -1 alone) and partially different organism sets; the direction of the overlap supports both analyses. [src: metal_specificity]

## Caveats and Open Work

The analysis had 40.7% gene attrition because locusId format mismatches excluded ANA3, Dino, Keio, MR1, Miya, PV4, and SB2B, including important model organisms such as Keio (*E. coli*), MR1 (*Shewanella*), and ANA3. The report cautions that excluded genes may have different specificity profiles and that the absent organisms are taxonomically diverse. [src: metal_specificity]

The 5% sick-rate threshold is arbitrary: results were qualitatively stable across 1–20%, but exact fractions varied. The planned validation against the Fitness Browser's built-in `specificphenotype` annotations was not performed. [src: metal_specificity]

The ICA module analysis failed to identify metal-specific modules; the proposed correction is to use precomputed z-scored module activities from Metal Atlas NB05. Further work should also resolve the locusId mismatches, replicate the counter-ion analysis using fit < -1 without the |t| > 4 requirement, and use AlphaFold predictions to examine metal-binding sites in UCP030820, YebC, and DUF1043. [src: metal_specificity]

## Slots Into

- [[concepts/metal-cross-resistance]] — distinguishes metal-specific fitness determinants from genes that respond to metals and other stresses, and compares metal–osmotic overlap.
- [[concepts/condition-specific-fitness]] — provides a cross-condition classification of 7,609 metal-important gene records using metal and non-metal sick rates.
- [[concepts/gene-essentiality]] — shows that putatively essential genes are absent from fitness data and bias conservation estimates toward the core genome.
- [[concepts/environmental-resistome]] — prioritizes metal-resistance candidates and quantifies the contribution of core and accessory genes to metal tolerance.
