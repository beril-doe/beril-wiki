---
type: "Concept"
description: "Ortholog families with metal fitness phenotypes across organisms, whether specificity classes match metal-resistance annotations, and how unannotated candidate families differ in specificity, pleiotropy and pangenome conservation; stops at predictions awaiting validation."
sources: ["summaries/discoveries.md", "summaries/metal_fitness_atlas__REPORT.md", "summaries/metal_specificity__REPORT.md"]
---
# Conserved metal-phenotype gene families and novel metal-tolerance candidates

Ortholog families with metal fitness phenotypes across organisms, whether specificity classes match metal-resistance annotations, and how unannotated candidate families differ in specificity, pleiotropy and pangenome conservation; stops at predictions awaiting validation.

## Conserved metal-phenotype families

Of 2,891 ortholog groups with metal phenotypes, 1,182 are conserved across ≥2 organisms and 601 across ≥3 organisms. [src: metal_fitness_atlas] The report calls these 1,182 families cross-species functional markers for metal biology. It describes them as extending Price et al. (2018) and as the first cross-species metal fitness atlas. [src: metal_fitness_atlas] The most broadly conserved family, OG00128, spans 17 organisms and 9 metals. [src: metal_fitness_atlas] Families with metal phenotypes in more organisms tend to have higher pangenome conservation (% core), which fits fundamental cellular processes. [src: metal_fitness_atlas]

## Do specificity classes match resistance annotations?

Metal-specific genes match metal-resistance keywords more often than general sick genes do. The keywords include efflux, transporter, metal, CDF and siderophore. The rates are 12.2% vs 7.8%, a 1.64x difference (Fisher exact OR=1.64, p=2.4e-8). [src: metal_specificity] The OR is the odds ratio. The groups hold 3,344 metal-specific and 2,573 general sick annotated genes. [src: metal_specificity] The 495 metal+stress genes sit between them, at 8.9%. [src: metal_specificity]

General sick genes show slightly higher general-stress keyword rates (DNA repair, cell wall, chaperone). The figures are 13.7% for metal-specific genes and 11.5% for general sick genes, a gap the report labels "11.5% vs 13.7%". [src: metal_specificity] The report concludes that the specificity classes capture biologically meaningful categories. It reads the enrichment as showing genuine metal tolerance determinants rather than general stress genes. [src: metal_specificity] See [[concepts/metal-tolerance-determinants-and-shared-stress-confounding]].

## Novel candidate families

The atlas identifies 149 novel candidates. These have conserved metal fitness phenotypes across ≥2 organisms but lack full annotation. [src: metal_fitness_atlas] They split into 89 truly unknown families, 43 with DUF/UPF domains and 17 with partial hints such as "transporter" or "hydrolase". [src: metal_fitness_atlas] DUF/UPF domains are known structural domains with an unknown metal role. [src: metal_fitness_atlas]

Novel candidates are less metal-specific than annotated families. 45.6% have a dominant specificity of metal-specific, against 58.2% for annotated families (Fisher exact OR=0.60, p=0.003). [src: metal_specificity] The report attributes this partly to composition. Many novel candidates came from deeply profiled organisms (DvH, Btheta, psRCH2). There, more experiments give more chances to detect pleiotropic effects and push genes toward "general sick". [src: metal_specificity]

### Specificity, pleiotropy and examples

Three candidates stand out as metal-specific rather than pleiotropic [src: discoveries, metal_specificity]:

| Candidate | Family | Organisms / metals | Metal-specific / total | Fraction | Mean sick rate |
|---|---|---|---|---|---|
| UCP030820 | OG01015 | 3 / 7 | 2/3 | 67% | 0.021 [src: metal_specificity] |
| YebC | OG01383 | 11 / 6 | 7/12 | 58% | 0.056 [src: metal_specificity] |
| DUF1043/YhcB | OG03264 | 6 / 5 | 3/6 | 50% | 0.054 [src: metal_specificity] |

Other candidates have lower specificity fractions and, in most rows, higher mean sick rates. The report itself calls only YfdZ and the Mla/Yrb system pleiotropic [src: discoveries, metal_specificity]:

| Candidate | Family | Organisms / metals | Metal-specific / total | Fraction | Mean sick rate |
|---|---|---|---|---|---|
| UPF0042/RapZ | OG02094 | 8 / 7 | 2/8 | 25% | 0.130 [src: metal_specificity] |
| MlaD | OG04003 | 4 / 4 | 1/4 | 25% | 0.113 [src: metal_specificity] |
| YfdZ | OG00391 | 7 / 9 | 2/13 | 15% | 0.268 [src: metal_specificity] |
| YrbC | OG02233 | 8 / 4 | 1/9 | 11% | 0.234 [src: metal_specificity] |
| DUF39 | OG08209 | 2 / 8 | 0/2 | 0% | 0.637 [src: metal_specificity] |
| YrbE | OG03534 | 6 / 5 | 0/6 | 0% | 0.190 [src: metal_specificity] |

The report prioritizes UCP030820, YebC and DUF1043 for their specificity (50-67%), low pleiotropy and validation across multiple species. [src: metal_specificity] It deprioritizes YfdZ and Mla/Yrb as general fitness factors with incidental metal phenotypes. [src: metal_specificity, discoveries] It ties YfdZ's sick rate to alanine biosynthesis and the Mla system's defects to outer membrane integrity. [src: metal_specificity] DUF39 spans 8 metals but has a sick rate of 0.64 (0.637 in the specificity report). The report therefore calls it a general fitness factor, not a metal-tolerance determinant. [src: discoveries, metal_specificity]

### YebC hypothesis

Ignatov et al. (2025), as cited by the report, showed that YebC is a translation factor for proline-rich proteins and resolves ribosome stalling at polyproline motifs. [src: metal_specificity] Many metal homeostasis proteins have proline-rich cytoplasmic loops. Examples are CopA, ZntA, CzcD and metal-binding chaperones. [src: metal_specificity] The report hypothesizes that metal-induced demand for these transporters creates a translation bottleneck that YebC resolves. [src: metal_specificity, discoveries] Under non-metal conditions the transporters are weakly expressed and YebC is dispensable. This would explain its metal-specific profile. [src: metal_specificity, discoveries]

## Proposed validation

The reports propose PaperBLAST, InterPro and AlphaFold structural prediction to characterize the 89 truly unknown and 43 DUF-domain families. [src: metal_fitness_atlas] They also propose AlphaFold to find metal-binding sites in UCP030820, YebC and DUF1043. [src: metal_specificity] Two organisms each have 54 novel candidate genes but have only been tested against iron. A standard metal panel would validate or refute those predictions. [src: metal_fitness_atlas] The report states that the 149 candidates could be validated directly in organisms where they are predicted to matter. [src: metal_fitness_atlas] See [[concepts/metal-coverage-gaps-and-proposed-validation-experiments]].

## Tensions

- Specificity comes in two layers. The keyword enrichment supports the specificity classes. [src: metal_specificity] Novel candidates are nonetheless less metal-specific than annotated ones, and the report ties this to the organisms in which they were found. [src: metal_specificity]
- Breadth across metals does not imply specificity. DUF39 spans 8 metals but is classified as general. [src: discoveries, metal_specificity]

## Open Directions

- Characterize the 89 truly unknown and 43 DUF-domain families with PaperBLAST, InterPro and AlphaFold. This would fill the annotation gap. See also [[concepts/function-prediction-for-uncharacterized-genes-by-guilt-by-association-and-ortholog-transfer]].
- Use AlphaFold to look for metal-binding sites in UCP030820, YebC and DUF1043.
- Test the two organisms with 54 novel candidate genes each against the standard metal panel, since they have so far been tested only against iron.
- Re-estimate novel versus annotated specificity with experiment count controlled. This would test the report's explanation for the lower specificity of novel candidates.
- Test the YebC translation-bottleneck hypothesis. One option is to measure expression of proline-rich metal transporters under metal and non-metal conditions.
