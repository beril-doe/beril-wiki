---
type: "Method"
description: "Pearson correlation of gene fitness profiles across experiments to find functionally related genes."
sources: ["summaries/amr_cofitness_networks__REPORT.md", "summaries/aromatic_catabolism_network__REPORT.md", "summaries/cofitness_coinheritance__REPORT.md", "summaries/fitness_modules__REPORT.md"]
aliases: ["cofitness", "gene-gene fitness correlation"]
---
# Cofitness analysis

See also [[entities/fitness-browser]] and [[concepts/construction-and-validity-of-cofitness-gene-groups]].

## Key facts

- Price et al. (2018), PMID: 29769716, established the Fitness Browser co-fitness data used in the cofitness_coinheritance report. Co-fitness identifies genes in the same pathway or complex. [src: cofitness_coinheritance]
- The Fitness Browser `cofit` table, read via Spark, supplies the top-20 co-fitness partners per gene. [src: cofitness_coinheritance]
- Sagawa et al. (2017) validated that cofitness recovers transcriptional regulatory relationships in 24 bacteria. [src: amr_cofitness_networks]
- Nichols et al. (2011, Cell) showed that condition-dependent fitness profiles reveal gene function in *E. coli*. [src: amr_cofitness_networks]
- The fitness_modules report uses within-module correlation, or cofitness, as its primary validation metric. It builds on the finding that genes with correlated fitness profiles share biological function. [src: fitness_modules]
- Fitness-module genes showed 22.7x genomic adjacency enrichment, which that report interprets as co-location in operons. [src: fitness_modules]

## Computation

Pearson r subtracts each gene's mean fitness before correlating. Two genes that are uniformly slightly positive would therefore show zero correlation. [src: amr_cofitness_networks]

For organisms without pre-computed co-fitness, such as Ralstonia, the cofitness_coinheritance report proposes calculating pairwise Pearson correlations from raw `genefitness` data. [src: cofitness_coinheritance]

The AMR (antimicrobial resistance) cofitness computation treats missing fitness values as zero in z-score space, using `np.nan_to_num`. This approximates, but does not equal, pairwise-complete Pearson correlation. [src: amr_cofitness_networks] Cached fitness matrices for that work come from `fitness_modules/data/matrices/`. [src: amr_cofitness_networks]

## Applications

### Assigning genes to subsystems in ADP1 quinate catabolism

Co-fitness assigned 44/51 ADP1 quinate-specific genes (86%) to four functional subsystems plus transcriptional regulators. The subsystems were the core aromatic degradation pathway (8 genes), Complex I / NADH (reduced nicotinamide adenine dinucleotide) dehydrogenase (21 genes), iron acquisition (7 genes) and PQQ (pyrroloquinoline quinone) biosynthesis (2 genes). Six transcriptional regulators were also found. [src: aromatic_catabolism_network] See [[entities/respiratory-complex-i-nadh-ubiquinone-oxidoreductase]] and [[concepts/support-gene-networks-around-catabolic-pathways]].

Within-category correlation was dramatically higher than between-category correlation. The Complex I mean r was 0.992 and the aromatic pathway r was 0.961. [src: aromatic_catabolism_network]

Of 23 genes first categorized as Other or Unknown, 16 were assigned to support subsystems with medium or high confidence from growth-profile correlations. [src: aromatic_catabolism_network] Separately, the report states that 16 previously uncharacterized genes were assigned to specific subsystems, including two DUF proteins (ACIAD3137, ACIAD2176) as candidate Complex I accessory factors with r > 0.98. [src: aromatic_catabolism_network] The pairwise correlations among the 51 genes are in `data/cofitness_network.csv`, which has 1,275 rows. [src: aromatic_catabolism_network]

## Caveats

- High cofitness implies shared fitness phenotypes, not direct transcriptional co-regulation. [src: amr_cofitness_networks]
- Functional enrichment in cofitness neighborhoods can reflect shared laboratory experimental context rather than biological co-regulation. [src: amr_cofitness_networks] Genes that are dispensable under experimental conditions may show artifactual co-regulation. The amr_cofitness_networks report says this concern reaches beyond AMR to any cofitness study of lab-grown organisms. [src: amr_cofitness_networks] See [[concepts/shared-dispensability-as-a-confound-in-cofitness-enrichment]].
- The ADP1 analysis uses only 8 conditions, which gives 8-dimensional growth vectors and limits the resolution of gene-gene correlations. [src: aromatic_catabolism_network] The 8-condition matrix provides ~5 independent dimensions. [src: aromatic_catabolism_network] The report states that more conditions would sharpen co-fitness subsystem boundaries. [src: aromatic_catabolism_network]
- The cofitness_coinheritance report found that lab-measured co-fitness weakly but significantly predicts co-inheritance in natural populations, though the effect size is small. [src: cofitness_coinheritance]

Related: [[concepts/guilt-by-association-inference-of-dark-gene-function-from-modules-operons-synteny-and-co-fitness]], [[summaries/amr_cofitness_networks__REPORT]], [[summaries/aromatic_catabolism_network__REPORT]], [[summaries/cofitness_coinheritance__REPORT]], [[summaries/fitness_modules__REPORT]].
