---
type: "Concept"
description: "How sampling depth and coverage distort pangenome core boundaries"
sources: ["summaries/conservation_vs_fitness__REPORT.md"]
---
# Pangenome Core Boundaries and Clade-Size Bias

Pangenome core-versus-auxiliary classifications depend not only on gene presence, but also on which genomes are sampled, how many genomes represent a clade, and how completely genes can be linked across datasets. The [[summaries/conservation_vs_fitness__REPORT]] shows that these design choices can make the core boundary more or less discriminative when Fitness Browser fitness data are integrated with KBase pangenome clusters. [src: conservation_vs_fitness]

## Sampling depth changes the meaning of “core”

In the integrated analysis, 44 of 48 Fitness Browser organisms were mapped to pangenome species clades, yielding 177,863 gene-to-cluster links with 100.0% median protein identity and 94.2% median gene coverage. [src: conservation_vs_fitness] Thirty-four organisms had at least 90% coverage, while 33 organisms were retained for downstream analysis after Dyella79 was excluded because of a locus-tag mismatch. [src: conservation_vs_fitness]

The classification assigned 145,821 linked genes, or 82.0%, to core clusters and 32,042, or 18.0%, to auxiliary clusters; the 7,574 singleton genes were a subset of the auxiliary category. [src: conservation_vs_fitness] These proportions describe conservation within the sampled clades, not an unconditional boundary between biologically “core” and “accessory” functions. [src: conservation_vs_fitness]

## Small clades can inflate core fractions

Clades containing only 2 genomes can have trivially high core fractions because a gene present in both genomes equals 100% core, reducing the discriminative power of the core-versus-auxiliary classification. [src: conservation_vs_fitness] Thus, a high core fraction in a small clade may reflect limited sampling rather than broad conservation across the species. [src: conservation_vs_fitness]

This sampling effect is important when interpreting associations between conservation and phenotype. Essential genes were 86.1% core compared with 81.2% for non-essential genes, with a median odds ratio of 1.56, and 18 of 33 organisms showed statistically significant enrichment by Fisher’s exact test after Benjamini-Hochberg false discovery rate correction at BH-FDR q < 0.05. [src: conservation_vs_fitness] The enrichment supports a relationship between essentiality and within-clade conservation, but the clade-size limitation means that the magnitude and discriminative value of the core category can vary with genome sampling. [src: conservation_vs_fitness]

## Coverage failure creates a second boundary problem

Coverage determines whether a gene can be assigned to a pangenome cluster at all, so incomplete joins can move genes out of the core-versus-auxiliary comparison or make apparent absence ambiguous. [src: conservation_vs_fitness] Ten organisms were excluded from Phase 2 because they had less than 90% DIAMOND coverage, reducing taxonomic breadth. [src: conservation_vs_fitness]

Four organisms—Cola, Kang, Magneto, and SB2B—were unmatched because their species had too few genomes in GTDB for pangenome construction. [src: conservation_vs_fitness] The main Escherichia coli clade was absent because it contained too many genomes, while Keio, an Escherichia coli BW25113 strain, mapped to the small s__Escherichia_coli_E clade at only 26.1% coverage. [src: conservation_vs_fitness] These exclusions and uneven mappings make the observed core fraction partly a property of which clade was available and successfully joined, not solely a property of gene biology. [src: conservation_vs_fitness]

Dyella79 illustrates a distinct failure mode: it was excluded from Phase 2 because the Fitness Browser gene table used the locus-tag format N515DRAFT_* whereas the protein sequences used ABZR86_RS*, producing a 0% join rate. [src: conservation_vs_fitness] This case shows that identifier incompatibility can alter the analyzed population before biological conservation is assessed. [src: conservation_vs_fitness]

## Implications for integrated fitness analyses

The conservation-versus-fitness result should therefore be interpreted as a clade- and coverage-conditioned association. [src: conservation_vs_fitness] Essential genes were generally more likely to be classified as core, but the analysis also found that most genes in well-characterized bacteria were core regardless of essentiality, making the enrichment modest. [src: conservation_vs_fitness]

The report’s stratification by clade size and lifestyle indicated that essential-core enrichment was robust across the genomic contexts examined, but the report also cautioned that small clades reduce the discriminative power of core-versus-auxiliary status. [src: conservation_vs_fitness] This combination supports using core status as evidence of conservation while treating it as a sampling-dependent measurement rather than a fixed universal label. [src: conservation_vs_fitness]

This concept refines [[concepts/pangenome-integration]] by identifying clade composition and join coverage as interpretive constraints on cross-dataset integration. [src: conservation_vs_fitness] It also qualifies the essentiality relationship discussed in [[concepts/gene-essentiality]], because the observed 1.56 median odds ratio depends on the sampled clades and the resulting conservation categories. [src: conservation_vs_fitness] The proposed extension to condition-specific fitness connects this issue to [[concepts/condition-specific-fitness]], since stress-dependent fitness effects may be compared against conservation only after sampling and coverage are controlled. [src: conservation_vs_fitness]

## Tensions

The analysis supports essential genes being more conserved within sampled clades, with 86.1% of essential genes classified as core versus 81.2% of non-essential genes and a median odds ratio of 1.56. [src: conservation_vs_fitness] At the same time, clades containing only 2 genomes can produce trivially high core fractions, and the main Escherichia coli clade was unavailable because it contained too many genomes. [src: conservation_vs_fitness] The tension is therefore between interpreting core status as biological conservation and recognizing that the estimate is shaped by both undersampling and exclusion of overlarge or poorly joinable clades. [src: conservation_vs_fitness]

## Open Directions

- Recompute core fractions across controlled subsamples of each clade, using repeated genome down-sampling to ask how the essential-versus-non-essential odds ratio changes with clade size. [src: conservation_vs_fitness]
- Reanalyze the 10 organisms excluded for less than 90% DIAMOND coverage with identifier harmonization and orthology-based recovery, asking whether their exclusion changes the 82.0% core and 18.0% auxiliary proportions. [src: conservation_vs_fitness]
- Compare clades with different genome counts using confidence intervals or hierarchical models, asking whether essential-core enrichment remains after explicitly modeling clade size and coverage. [src: conservation_vs_fitness]
- Extend the comparison from binary essentiality to condition-specific fitness, especially genes with fitness < -2 under stress conditions, asking whether conditionally important genes show the same sampling-sensitive conservation pattern. [src: conservation_vs_fitness]
