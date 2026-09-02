---
type: "Concept"
description: "Gene co-occurrence identifies ecological guilds but does not prove physical linkage."
sources: ["summaries/pgp_pangenome_ecology__REPORT.md"]
---
# Gene co-occurrence can reveal ecological guilds without proving physical linkage

Gene co-occurrence is useful for identifying ecological guilds: recurring combinations of genes can indicate shared environmental selection or complementary ecological roles. However, co-occurrence across genomes does not establish that genes are physically linked in the same operon, genomic island, or locus. [src: pgp_pangenome_ecology]

## Evidence from plant-growth-promoting genes

The [[summaries/pgp_pangenome_ecology__REPORT]] analyzed 13 plant-growth-promoting gene markers across 27,702 species, including 32,736 PGP gene clusters. [src: pgp_pangenome_ecology] Eight of 10 focal-gene pairs were significantly associated after Benjamini–Hochberg false-discovery-rate (BH-FDR) correction, with five positive and three negative associations. [src: pgp_pangenome_ecology]

The strongest positive association was between [[entities/pqqc]] and [[entities/acds]], with odds ratio (OR) = 7.24, n = 286 co-occurring species, and q = 1.2e-83. [src: pgp_pangenome_ecology] [[entities/pqqc]] also co-occurred significantly with [[entities/hcnc]] (OR = 1.91) and [[entities/ipdc]] (OR = 1.55), forming a putative non-diazotrophic rhizosphere-effectiveness module. [src: pgp_pangenome_ecology]

This pattern supports the use of co-occurrence to identify an ecological guild, because the genes recur together more often than expected under the tested association model. [src: pgp_pangenome_ecology] It does not prove that [[entities/pqqc]], [[entities/acds]], [[entities/hcnc]], and [[entities/ipdc]] occupy the same genomic neighborhood or are transferred as one unit. [src: pgp_pangenome_ecology]

The negative associations involving [[entities/nifh]] further refine the guild interpretation. nifH was negatively associated with hcnC (OR = 0.23, q = 5.8e-29) and pqqC (OR = 0.57, q = 2.9e-19), while its association with ipdC was not significant (OR = 1.13, q = 0.54). [src: pgp_pangenome_ecology] These results support ecological separation between diazotrophs and pqqC/acdS-bearing rhizobacteria in this dataset, rather than proving mutually exclusive genomic architectures. [src: pgp_pangenome_ecology]

Only 157 species (1.4%) carried at least three focal traits, indicating that broad multi-trait combinations were uncommon in the analyzed species set. [src: pgp_pangenome_ecology] The most common reported multi-trait genotype was pqqC + acdS (n = 153), while nifH + pqqC was reported at n = 225 despite the negative genome-wide association between those genes. [src: pgp_pangenome_ecology] This illustrates why pairwise association statistics and genotype counts should be interpreted together rather than treated as interchangeable evidence of a single guild. [src: pgp_pangenome_ecology]

## Environmental support for guild interpretation

The co-occurrence pattern was accompanied by environmental differentiation. Among 1,039 soil/rhizosphere species and 10,233 species from other environments, acdS prevalence was 15.8% versus 2.6% (OR = 7.02, q = 5.1e-62), pqqC prevalence was 43.8% versus 21.2% (OR = 2.90, q = 2.8e-53), and hcnC prevalence was 11.3% versus 6.4% (OR = 1.85, q = 6.1e-08). [src: pgp_pangenome_ecology] nifH was depleted in soil-classified species, with prevalence of 12.9% versus 19.7% (OR = 0.60, q = 5.5e-08). [src: pgp_pangenome_ecology]

The acdS enrichment remained strong after phylum-level fixed effects in logistic regression (OR = 6.98, p = 4.8e-61) and in a strict rhizosphere-only sensitivity analysis using genomes whose isolation source contained “rhizosphere” or “root nodule” (OR = 10.6, q = 7.6e-38). [src: pgp_pangenome_ecology] The agreement between gene co-occurrence and environment-stratified prevalence supports an ecological-guild interpretation more strongly than co-occurrence alone. [src: pgp_pangenome_ecology]

This evidence connects to [[concepts/ecotype-environment-gene-content]], because the gene combinations and their negative or positive associations corresponded to different environmental distributions. [src: pgp_pangenome_ecology] It also complements [[concepts/module-level-coinheritance]], while leaving open whether the observed module is physically coinherited or instead assembled repeatedly by ecological selection. [src: pgp_pangenome_ecology]

## Co-occurrence is not physical linkage

The report explicitly notes that co-occurrence does not establish physical linkage. [src: pgp_pangenome_ecology] The pqqC–acdS association could reflect a shared habitat, complementary functions, correlated lineage structure, repeated independent acquisition, or physical linkage, and the reported analysis does not distinguish among these mechanisms. [src: pgp_pangenome_ecology]

The core/accessory results also caution against assuming that a co-occurring pair is a horizontally transferred cassette. [src: pgp_pangenome_ecology] All 13 PGP genes had higher core fractions than the 46.8% genome-wide baseline, and pqqC was 81.5% core, 7.8% auxiliary, and 10.7% singleton, whereas acdS was 70.4% core, 13.4% auxiliary, and 16.2% singleton. [src: pgp_pangenome_ecology] Thus, the pqqC–acdS guild signal is compatible with predominantly conserved gene distributions rather than requiring a single mobile element. [src: pgp_pangenome_ecology]

The analysis also identified pqqD as an exception, with 55.5% core and 27.5% singleton status, suggesting that pqqD can sometimes spread as a standalone gene. [src: pgp_pangenome_ecology] This distinction between statistical co-occurrence, shared ecological function, and physical coinheritance is central to interpreting [[concepts/gene-cooccurrence-ecological-guilds]]. [src: pgp_pangenome_ecology]

## Interpretation limits

The environmental classification was conservative and noisy: 1,637 species (5.9% of species with an environment label) were classified as soil/rhizosphere dominant, while 291,279 genomes had isolation-source metadata and 93.5% were classifiable. [src: pgp_pangenome_ecology] NCBI sampling is biased toward clinical and host-associated genomes, so the observed acdS and pqqC enrichment may underestimate true rhizosphere enrichment. [src: pgp_pangenome_ecology]

PGP detection relied on Bakta annotations matching exact gene names such as nifH, acdS, and pqqC, so product-only annotations and variant gene names could have been missed. [src: pgp_pangenome_ecology] Gene clusters were not functionally validated for truncations, frameshifts, or pseudogenization, meaning that an annotated co-occurring cluster was not necessarily functional. [src: pgp_pangenome_ecology]

Phylogenetic structure and uneven sampling can also contribute to apparent co-occurrence, so the guild interpretation should be tested with lineage-aware models and genome-context analyses. [src: pgp_pangenome_ecology] These limitations connect the concept to [[concepts/phylogenetic-confounding-of-pangenome-associations]], [[concepts/annotation-dependent-resistome-inference]], and [[concepts/evidence-triangulation-for-functional-annotation]]. [src: pgp_pangenome_ecology]

## Open Directions

- Use complete or well-assembled genomes from the pqqC–acdS-positive set, together with operon and genomic-island analysis, to test whether the two genes are physically linked or occur at separate loci. [src: pgp_pangenome_ecology]
- Apply phylogeny-aware co-occurrence models to the PGP gene matrix and ask whether the pqqC–acdS association persists after accounting for shared ancestry. [src: pgp_pangenome_ecology]
- Compare gene neighborhoods, synteny, mobile-element context, and gene-tree reconciliation for pqqC, acdS, hcnC, and ipdC to distinguish vertical conservation from repeated horizontal acquisition. [src: pgp_pangenome_ecology]
- Reanalyze nifH associations after stratifying by environment, lineage, and diazotrophic ecological context to determine whether the negative nifH–pqqC and nifH–hcnC associations reflect ecological separation or sampling structure. [src: pgp_pangenome_ecology]
- Functionally validate representative co-occurring clusters with transcript or phenotype data to test whether annotated pqqC, acdS, hcnC, and ipdC genes are active components of the proposed guild. [src: pgp_pangenome_ecology]
