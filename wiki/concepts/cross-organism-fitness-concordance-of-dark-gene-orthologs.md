---
type: "Concept"
description: "Whether orthologs of unannotated genes show fitness effects under the same condition class in several bacteria, and whether this differs from annotated genes."
sources: ["summaries/discoveries.md", "summaries/functional_dark_matter__REPORT.md", "summaries/truly_dark_genes__REPORT.md"]
---
# Cross-organism fitness concordance of dark gene orthologs

Cross-organism fitness concordance asks whether orthologs of the same dark gene show fitness effects under the same conditions in several organisms. [src: functional_dark_matter] In the functional dark matter analysis, 65 dark ortholog groups present in 3+ Fitness Browser organisms were testable, and they showed concordance. [src: functional_dark_matter, discoveries] Dark-gene concordance was statistically indistinguishable from that of annotated genes, so the evidence supports dark genes behaving like functional genes, not that they differ from annotated genes. [src: discoveries, functional_dark_matter] See [[entities/fitness-browser]] and [[summaries/functional_dark_matter__REPORT]].

## Main result: concordance exists

The report concludes that concordance shows dark-gene phenotypes are reproducible across organisms, not single-species artifacts. [src: functional_dark_matter] It says these 65 groups have conserved phenotypes that could not be found from any single organism. [src: functional_dark_matter] It marks H1c (cross-organism concordance) as supported for the 65 testable groups. [src: functional_dark_matter] Separately, 101 ortholog groups in the top 500 dark-gene candidates span 2+ organisms. [src: functional_dark_matter]

## Dark versus annotated genes

A matched comparison (NB06; Mann-Whitney, 65 dark vs. 490 annotated groups) found no difference, p=0.17. [src: functional_dark_matter] The same comparison gave KS p=1.0, with dark median=1.0, annotated median=1.0, dark mean=0.976 and annotated mean=0.985. [src: functional_dark_matter] The report reads this null as support for H1, that dark genes behave like real functional genes, not noise. [src: functional_dark_matter] The null limits any claim that dark genes are more or less concordant than annotated ones.

## Which conditions and groups

Carbon-source genes (spanning 3–8 organisms) and motility genes (3 organisms each) show the strongest concordance. The report suggests these are conserved but unannotated carbohydrate-metabolism and chemotaxis components. [src: functional_dark_matter] Motility-related dark genes are strongest overall, consistent with conserved but incompletely annotated chemotaxis machinery. [src: functional_dark_matter, discoveries] This is an interpretation, not a tested mechanism.

The groups below each have concordance of 1.00. [src: functional_dark_matter]

| Group | Condition | Organisms | Notes |
|---|---|---|---|
| OG11386 | carbon source | 8 | DUF5064; P. putida, P. syringae, P. stutzeri RCH2 [src: functional_dark_matter] |
| OG15006 | carbon source | 7 | Ralstonia spp. [src: functional_dark_matter] |
| OG14628 | carbon source | 5 | Ralstonia spp. [src: functional_dark_matter] |
| OG12530 | carbon source | 4 | DUF2844; B. thailandensis, Burkholderia sp. 376 [src: functional_dark_matter] |
| OG05812 | stress | 8 | Peptidase_M50; MR-1, SB2B; module-predicted TIGR01730 [src: functional_dark_matter] |
| OG05815 | stress | 8 | ParE_toxin; S. meliloti [src: functional_dark_matter] |
| OG03384 | stress | 6 | Metallophos; module-predicted glutathione S-transferase [src: functional_dark_matter] |
| OG10428 | motility | 3 | ThiS; S. meliloti; max abs fit 2.2 [src: functional_dark_matter] |
| OG10455 | motility | 3 | MS_channel; S. meliloti [src: functional_dark_matter] |

The report says the Peptidase_M50 site-2 protease-family domain in OG05812 hints at a conserved regulatory protease under stress. [src: functional_dark_matter]

### Widely shared groups among top candidates

| Group | Condition | Organisms spanned |
|---|---|---|
| OG03827 | carbon source | 6: MR-1, Marinobacter, ANA3, PV4, P. fluorescens N1B4, P. simiae N2E2 [src: functional_dark_matter] |
| OG02907 | nitrogen source | 6: MR-1, E. coli Keio, K. oxytoca, P. putida, P. fluorescens N1B4, P. simiae N2E3 [src: functional_dark_matter] |
| OG01383 | pH | 5: MR-1, S. meliloti, C. metallidurans, P. fluorescens GW456-L13, P. putida N2C3 [src: functional_dark_matter] |
| OG03534 | stress | 5: MR-1, ANA3, Dinoroseobacter, PV4, Synechococcus [src: functional_dark_matter] |
| OG01997 | stress | 4: MR-1, ANA3, S. meliloti, P. putida N2C3 [src: functional_dark_matter] |

The report proposes that stress experiments in MR-1 and P. putida N2C3 would give concordance data for OG01997, and that adding nitrogen experiments would test OG02907 and OG01383 across several genetic backgrounds. [src: functional_dark_matter]

## Truly dark genes are mostly invisible to this test

Truly dark genes are 4.2× less likely to have cross-organism orthologs (OR = 0.236, odds ratio), and their orthologs span a median of 1 organism versus 4 for annotation-lag genes. [src: truly_dark_genes] Only 3 of the 65 dark ortholog groups with concordance data contain truly dark genes. [src: truly_dark_genes] See [[concepts/reannotation-lag-versus-genuinely-unannotatable-dark-genes]]. Ortholog data cover 3,449 pairs for 1,885 truly dark genes (29.3% of them) across 48 Fitness Browser organisms. [src: truly_dark_genes] Bidirectional best hit orthologs cover only 32 of 48 organisms, so truly dark genes from the other 16 lack concordance and breadth data. [src: truly_dark_genes]

## Open Directions

- Run the proposed stress experiments in MR-1 and P. putida N2C3, plus nitrogen experiments, to test OG01997, OG02907 and OG01383 across genetic backgrounds.
- Extend ortholog calls to the 16 organisms without bidirectional best hit coverage. This would test whether truly dark genes are non-concordant or just unmeasured.
- Use a test sensitive to ceiling effects, since both medians are 1.0. This would check whether the dark-versus-annotated null hides differences.
- Test motility-concordant groups such as OG10428 and OG10455 for chemotaxis roles by targeted assays.
