---
type: "Concept"
description: "How strongly AMR repertoires, niche breadth, metal resistance and metabolic traits track phylogeny (Mantel tests, Pagel's lambda), and what this implies for vertical inheritance versus horizontal transfer; stops at effect sizes."
sources: ["summaries/amr_strain_variation__REPORT.md", "summaries/comprehensive_metal_ecology__REPORT.md", "summaries/discoveries.md", "summaries/microbeatlas_metal_ecology__REPORT.md"]
---
# Phylogenetic signal of gene content and traits

This page collects effect sizes for how strongly antimicrobial resistance (AMR) repertoires, niche breadth, metal AMR and nitrification track phylogeny. It uses Mantel tests and Pagel's λ. Within species, 55.6% (701 of 1,261) show significant AMR phylogenetic signal. [src: amr_strain_variation] Across genera, bacterial niche breadth has λ of 0.787 and metal AMR traits have λ of about 0.26–0.44. [src: microbeatlas_metal_ecology] Within bacterial metal AMR, the ordering of signal is core fraction above type diversity above cluster count. [src: microbeatlas_metal_ecology] Several interpretations are proposals, not tests.

## Literature Context

Several candidate papers bear on how strongly gene content and traits follow phylogeny. The clearest support for strong vertical structure comes from a study of metabolic traits. It cultured 96 bacterial isolates and assayed growth on 10 compounds as sole carbon sources. Classifiers trained on gene content predicted carbon utilization accurately by encoding phylogenetic information, and they outperformed automatically built constraint-based metabolic models [PMID 38113208](https://pubmed.ncbi.nlm.nih.gov/38113208/). The same work found that phylogeny-based prediction fails for taxa phylogenetically distant from the training set [PMID 38113208](https://pubmed.ncbi.nlm.nih.gov/38113208/). A study of 440 public Sphingomonas genomes (252 high quality) found that strains from the same habitat clustered within clades. Strains within a clade also shared similar clusters of accessory genes, so gene content reflected habitat preference [PMID 37138640](https://pubmed.ncbi.nlm.nih.gov/37138640/).

Other papers show that gene content does not always follow phylogeny. In the Mycobacterium tuberculosis complex, fewer gene families were shared as phylogenetic distance increased, but only in between-species comparisons and not within species. This suggests that ecological characteristics are associated with gene content. Gene loss drove the variation, and the gene repertoire of M. africanum L6 deviated from the expected phylogenetic niche conservatism [PMID 38230932](https://pubmed.ncbi.nlm.nih.gov/38230932/). For Escherichia coli, reviews describe an open accessory genome with frequent horizontal transfer. They report that this transfer creates hybrid pathogenic strains and spreads antibiotic resistance and virulence traits [PMID 35749579](https://pubmed.ncbi.nlm.nih.gov/35749579/) [PMID 23340801](https://pubmed.ncbi.nlm.nih.gov/23340801/). A phylogenetic comparative analysis of bacterial GC content found gradual evolution plus evolutionary "jumps" in both directions [PMID 35579351](https://pubmed.ncbi.nlm.nih.gov/35579351/). That points to trait evolution that is not purely gradual Brownian drift.

The corpus's metabolic and niche results are consistent with this literature. Nitrification has λ of 0.939 in bacteria and 1.000 in archaea. Bacterial niche breadth has λ of 0.787. Both fit the strong link between phylogeny and metabolic traits seen in [PMID 38113208](https://pubmed.ncbi.nlm.nih.gov/38113208/). They also fit habitat-clade structure in [PMID 37138640](https://pubmed.ncbi.nlm.nih.gov/37138640/). The intermediate metal AMR λ of about 0.26–0.44 sits with the evidence of frequent horizontal transfer of resistance and virulence genes in E. coli [PMID 35749579](https://pubmed.ncbi.nlm.nih.gov/35749579/). That E. coli evidence is review-level, not a direct λ estimate.

The within-species Mantel result is harder to place. Of 1,261 species, 701 (55.6%) showed significant AMR signal. Non-core AMR genes had stronger signal than core genes, with median r of 0.222 against 0.117. The corpus reads this as clonal inheritance of acquired genes. None of the candidates tests this directly. The M. tuberculosis complex study is the closest. It is clonal, and its within-species gene content showed no distance effect, so it does not clearly support or contradict the Mantel pattern [PMID 38230932](https://pubmed.ncbi.nlm.nih.gov/38230932/). The E. coli reviews, which stress horizontal acquisition, are in some tension with the clonal reading. The corpus excluded E. coli from its ANI analysis, so that tension remains untested. The acquired-over-core finding is therefore best treated as novel and unreplicated in these candidates. It is also partly a statistical artifact of near-zero Jaccard variance in core genes. The remaining candidates (eukaryote, plant and chloroplast studies) concern other systems and do not bear on these findings.

## AMR repertoires within species (Mantel tests)

Within species, AMR gene content tracks strain relatedness. A [[entities/mantel-test]] compared average nucleotide identity (ANI) distance with AMR Jaccard distance across 1,261 species. Of these, 55.6% (701 species) showed significant signal (false discovery rate, FDR, < 0.05). [src: amr_strain_variation] The median Mantel r was 0.247. [src: amr_strain_variation] In 87.8% of species the correlation was positive. [src: amr_strain_variation] The report concludes that closely related strains tend to share more AMR genes. [src: amr_strain_variation]

Non-core (putatively acquired) AMR genes showed stronger signal than core (intrinsic) genes. Median r was 0.222 against 0.117 (paired t-test: t = -8.35, p = 7.0e-16, n = 489). [src: amr_strain_variation, discoveries] The report calls this its most surprising finding. [src: amr_strain_variation] See also [[concepts/intrinsic-versus-acquired-resistance-gene-conservation]].

The report reads this as clonal inheritance. Acquired genes, it suggests, are more often inherited within lineages than acquired at random by horizontal gene transfer (HGT). [src: amr_strain_variation] It proposes that a lineage keeps a resistance element once it has acquired it, likely through mobile genetic elements (MGE), and so creates lineage-specific AMR signatures. [src: amr_strain_variation] The discoveries digest states this as contradicting the standard model of phylogenetically random acquisition. [src: discoveries] The report cites Maier et al. (2025), who found that AMR transfer is largely confined to closely related lineages. [src: amr_strain_variation] It also suggests that tracking clonal lineages may be more informative for surveillance than tracking single genes. [src: amr_strain_variation]

Two caveats limit this result:
- Core genes are near-universal (>=95% prevalence by definition). Their Jaccard distances are near zero with little variance. This suppresses Mantel r, a statistical artifact that partly explains their lower signal independent of biology. [src: amr_strain_variation, discoveries]
- ANI extraction was limited to species with <=500 genomes. This excluded [[entities/escherichia-coli]] (15,388 genomes) and [[entities/klebsiella-pneumoniae]] (14,240 genomes). [src: amr_strain_variation] The report proposes subsampling strategies for ANI-based Mantel tests in species with >500 genomes. [src: amr_strain_variation]

## Niche breadth and metal AMR across genera (Pagel's λ)

Across genera, niche breadth is much more phylogenetically conserved than metal AMR. In bacteria, λ for niche traits was about 0.79–0.91, against about 0.26–0.44 for AMR traits. [src: microbeatlas_metal_ecology] The report reads this as ecological range being canalized by lineage, while metal AMR is more labile, likely because AMR genes sit on MGE and are exchanged among distant taxa. [src: microbeatlas_metal_ecology] It also frames λ partitioning as a way to separate vertically inherited repertoires from HGT-driven accessory acquisition. [src: microbeatlas_metal_ecology] See [[concepts/horizontal-transfer-signatures-of-metal-resistance-genes]].

The report interprets the ordering of bacterial metal-AMR signal (core fraction λ above type diversity λ above cluster count λ) as consistent with mainly vertical inheritance of constitutive (core) resistance. On this reading, horizontal transfer and local metal exposure shape accessory accumulation and type expansion. [src: microbeatlas_metal_ecology]

Pagel's λ values by trait, tested with a likelihood ratio test (LRT):

| Domain | Trait | Genera | λ | p |
|---|---|---|---|---|
| Bacteria | Levins' B_std | 1,264 | 0.787 | 7.9×10⁻¹⁰² [src: microbeatlas_metal_ecology] |
| Archaea | Levins' B_std | 132 | 0.197 | 1.1×10⁻⁵ [src: microbeatlas_metal_ecology] |
| Bacteria | Number of environments | 1,264 | 0.909 | 1.4×10⁻¹⁵⁷ [src: microbeatlas_metal_ecology] |
| Archaea | Number of environments | 132 | 0.898 | 4.6×10⁻¹⁴ [src: microbeatlas_metal_ecology] |
| Bacteria | Nitrification | 2,286 | 0.939 | 2.5×10⁻¹⁰² [src: microbeatlas_metal_ecology] |
| Archaea | Nitrification | 132 | 1.000 | 2.5×10⁻⁵¹ [src: microbeatlas_metal_ecology] |
| Bacteria | AMR clusters | 606 | 0.260 | 6.1×10⁻²⁸ [src: microbeatlas_metal_ecology] |
| Bacteria | Core AMR fraction | 606 | 0.441 | 1.8×10⁻⁸ [src: microbeatlas_metal_ecology] |
| Bacteria | Metal types | 606 | 0.335 | 1.1×10⁻²³ [src: microbeatlas_metal_ecology] |
| Archaea | AMR clusters | 48 | ≈0 | 1.0 [src: microbeatlas_metal_ecology] |

See [[entities/levins-niche-breadth]] for the B_std measure.

The report treats nitrification as a metabolic positive control. Its λ of 0.94–1.00 in both domains contrasts with the intermediate metal AMR signal. [src: microbeatlas_metal_ecology] It describes ammonia- and nitrite-oxidation genes as deep, vertically inherited innovations that define major lineages such as Nitrospirota and Thaumarchaeota. [src: microbeatlas_metal_ecology] It reads the near-maximal nitrification λ as ancient, vertically inherited metabolic entrenchment. [src: microbeatlas_metal_ecology]

The report treats the bacterial results as consistent with the literature:
- Bacterial niche breadth λ = 0.787 is consistent with Malfertheiner et al. (2026). [src: microbeatlas_metal_ecology]
- Conserved soil prokaryote niche breadth is consistent with Hernandez et al. (2023). [src: microbeatlas_metal_ecology]
- Intermediate metal AMR λ is consistent with Hemme et al. (2016) on lateral-gene-transfer hotspots for metal resistance. [src: microbeatlas_metal_ecology]
- Core fraction λ exceeding total cluster count λ is consistent with Gillieatt & Coleman (2024), who reviewed MGE-mediated AMR transfer under metal co-selection. [src: microbeatlas_metal_ecology]

### Archaea

Archaeal niche breadth shows significant signal, with B_std λ = 0.197 and number of environments λ = 0.898. [src: microbeatlas_metal_ecology] Archaeal B_std λ is notably lower than the bacterial value (0.787). [src: microbeatlas_metal_ecology] The report considers this consistent with sparse phylogenetic sampling and ecological distinctness in short-read amplicon surveys. [src: microbeatlas_metal_ecology] It cites Jiao et al. (2021), who found niche conservatism in soil archaea, as support that the signal is real. [src: microbeatlas_metal_ecology] Archaeal AMR cluster count has λ ≈ 0, but only 48 genera were tested. [src: microbeatlas_metal_ecology] See [[concepts/statistical-power-and-database-coverage-gap-for-archaeal-trait-analyses]].

## Signal after controlling for a predictor

Including a predictor in phylogenetic generalized least squares (PGLS; [[entities/phylogenetic-generalized-least-squares]]) lowers λ modestly. The report defines standalone λ as the share of total B_std variance explained by Brownian-motion phylogenetic covariance. PGLS λ is the residual signal after removing variance explained by metal type diversity. [src: microbeatlas_metal_ecology] Bacterial B_std λ is 0.787 standalone (NB04) and 0.708 in PGLS (NB05), a difference of Δλ = 0.079. [src: microbeatlas_metal_ecology] The report explains the drop by the predictor's own signal (λ_metal_types = 0.335). [src: microbeatlas_metal_ecology] It reads the drop as metal type diversity accounting for approximately 10% of B_std's phylogenetic covariance. [src: microbeatlas_metal_ecology] It concludes that metal resistance breadth is one of several phylogenetically structured predictors, not the sole driver. [src: microbeatlas_metal_ecology] It finds strong residual signal (λ = 0.708, p ≪ 0.001) and no evidence of model misspecification. [src: microbeatlas_metal_ecology]

A separate report found a lower λ in its P5 model than in P1 (0.734 vs 0.757). It reads this as slightly less residual structure after controlling for the predictor. [src: comprehensive_metal_ecology] It reads λ = 0.757 as meaning shared ancestry partly, but not entirely, explains the metal-gene density–niche breadth relationship. [src: comprehensive_metal_ecology] See [[concepts/metal-gene-density-and-ecological-niche-breadth]]. Specific pH niches had much lower λ (0.11–0.20), which the report takes to mean environmental-axis niches are mostly shaped by ecology. [src: comprehensive_metal_ecology] Near-zero λ for Earth Microbiome Project (EMP) data suggests limited signal in EMPO-2 niche breadth at coarse habitat resolution. [src: comprehensive_metal_ecology]

## Tensions

- Across genera, metal AMR λ is intermediate (about 0.26–0.44) and the report reads it as lability through MGE exchange among distant taxa. [src: microbeatlas_metal_ecology] The same report also reads the core-over-accessory ordering as mainly vertical inheritance of core resistance. [src: microbeatlas_metal_ecology]
- The core-versus-acquired Mantel difference is partly a statistical artifact of near-zero Jaccard variance in core genes. [src: amr_strain_variation]

## Open Directions

- Run ANI-based Mantel tests on species with >500 genomes, such as E. coli and K. pneumoniae, using subsampling. This would test whether the acquired-over-core pattern holds in the largest species.
- Repeat the core-versus-acquired comparison with a metric that is not suppressed by near-zero variance, such as a permutation-calibrated or prevalence-matched test. This would separate the artifact from the biology.
- Measure Pagel's λ for core versus accessory AMR fractions within the same genera, and compare it with the within-species Mantel r. This would reconcile the scale difference.
- Expand archaeal genus coverage beyond 132 genera, and beyond short-read amplicon surveys. This would check whether the low archaeal B_std λ is a sampling effect.
