---
type: "Summary"
description: "GTDB-scale atlas of gene innovation, acquisition depth, ecology, and phenotype"
doc_type: "short"
full_text: "sources/gene_function_ecological_agora__REPORT.md"
---
# Gene Function Ecological Agora

## Overview

The Gene Function Ecological Agora project completed Phases 1A, 1B, 2, 3, Phase 4 deliverables P4-D1 through P4-D5, and the NB28 synthesis across 28 notebooks. It produced a GTDB-r214 atlas spanning 18,989 species representatives, 13.74M rank × clade × KO producer/participation scores, 17.07M Sankoff-parsimony gain events, 3.94M KO × genus MGE-machinery records, and environmental, phenotype, and gene-neighborhood integrations. Two of four pre-registered hypotheses were confirmed, one was qualified/reframed, and the Alm 2006 point estimate was not reproduced at GTDB scale. [src: gene_function_ecological_agora]

The project’s central methodological framework classifies clade × function tuples by producer and participation behavior as Innovator-Isolated, Innovator-Exchange, Sink/Broker-Exchange, or Stable. Sankoff parsimony with M22 recipient-rank attribution replaced the earlier parent-rank dispersion metric, while D2 annotation-density residualization and leaf_consistency supplied bias and within-clade-structure diagnostics. [src: gene_function_ecological_agora]

## Key findings

### Hypothesis verdicts

- **Bacteroidota × PUL CAZymes:** the original absolute-zero Innovator-Exchange criterion was falsified at UniRef50 resolution, but Sankoff diagnostics recovered a small relative HGT signal of Cohen’s d = 0.15; the final synthesis labels the result a qualified pass/reframed finding rather than evidence for the original strong criterion. [src: gene_function_ecological_agora]
- **Mycobacteriaceae × mycolic acid:** supported at family rank with producer d = +0.31 and consumer d = −0.19, and at order rank with producer d = +0.288 and consumer d = −0.285; the family-rank Innovator-Isolated subset contained 67 of 582 tuples, or 11.51%, versus an atlas-wide 5.85%. [src: gene_function_ecological_agora]
- **Cyanobacteriia × PSII:** supported at class rank with producer d = +1.50 and consumer d = +0.70, with producer p = 2×10⁻⁵ and consumer p = 2×10⁻⁴; genus, family, and order tests were STABLE with producer d values of +0.08, +0.20, and +0.19, respectively. [src: gene_function_ecological_agora]
- **Alm 2006 reproduction:** the reported r ≈ 0.74 was not reproduced across 18,989 species representatives; four framings yielded Pearson r values of 0.288, 0.157, 0.100, and 0.105, with Spearman r values of 0.333, 0.222, 0.152, and 0.106. The qualitative TCS-HK architectural result remained supported by consumer-side KO-to-architecture concordance of r = 0.673, while producer concordance was exploratory at r = 0.093. [src: gene_function_ecological_agora]
- **Regulatory versus metabolic functions:** no test met the pre-registered d ≥ 0.3 threshold. Producer d = +0.059 and consumer d = −0.211 were reported for the primary score tests, while recent-acquisition d = +0.141; the consumer direction supports the Jain 1999 complexity-hypothesis direction at small effect size and is independently consistent with Burch et al. 2023. [src: gene_function_ecological_agora]

### Acquisition-depth signatures

M22 assigned 17,073,194 Sankoff gain events to recipient-rank depth bins. Recent-to-ancient ratios separated function classes: CRISPR-Cas had 58.7% recent and 2.4% ancient gains, a 24.5× ratio; TCS histidine kinases had 45.1% and 4.4%, a 10.3× ratio; β-lactamases had 44.2% and 4.9%, a 9.0× ratio; and clean tRNA-synthetase controls had 24.7% and 10.7%, a 2.3× ratio. [src: gene_function_ecological_agora]

Mycobacteriaceae mycolic-acid gains showed 79.87% recent, 16.72% older-recent, 3.41% mid, 0.00% older, and 0.00% ancient events among 53,916 gains, compared with 48.79%, 31.81%, 9.60%, 6.12%, and 3.68% across all mycolic-acid gains. Cyanobacteria PSII gains showed 2.05% ancient events versus 14.90% atlas-wide, consistent with a class-level donor-origin signature but not establishing donor identity. [src: gene_function_ecological_agora]

The synthesis-stage leaf_consistency metric, defined as the fraction of species in a recipient clade carrying a KO, had mean values of 0.34 for recent gains and 0.20 for ancient gains. Hypothesis-specific values were 0.88 for Cyanobacteriia × PSII, 0.41 for Bacteroidota × PUL, and 0.15 for Mycobacteriaceae × mycolic acid, against an atlas reference of 0.20. The low Mycobacteriaceae value revealed that the family-level mycolic result is a mixture of within-family sub-clades rather than a uniform family property. [src: gene_function_ecological_agora]

A follow-up sub-clade analysis found producer d = +0.394 for the mycolic-positive sub-clade comprising 10 of 13 genera, compared with family-rank d = +0.309 and mycolic-low sub-clade d = +0.211. Consumer d was +0.006 for the mycolic-positive sub-clade, indicating that the original consumer-side Innovator-Isolated signal is rank-dependent and strongest at family aggregation. [src: gene_function_ecological_agora]

### Ecology and phenotype consistency

The three focal clades were statistically consistent with expected environments: Cyanobacteriia showed 2.77× photic-aquatic enrichment with p < 10⁻⁵², Mycobacteriaceae showed 7.88× host-pathogen enrichment with p < 10⁻⁴⁵, and Bacteroidota showed 1.40× gut/rumen enrichment with p < 10⁻³⁵. Mycobacteriaceae was not soil-enriched: its soil fold was 0.88× with p = 0.87. [src: gene_function_ecological_agora]

BacDive phenotype profiles were consistent with the atlas interpretations. Among 318 Mycobacteriaceae species, 95% of recorded cell shapes were rod-shaped, 99% were non-motile, and 89.4% were aerobic-leaning; among 577 Bacteroidota species, the profile was saccharolytic and glycoside-hydrolase-rich, with anaerobic phenotypes at 33.2% versus 22.0% atlas-wide. Cyanobacteriia phenotype coverage was too thin for interpretation at n = 4. [src: gene_function_ecological_agora]

AlphaEarth k = 10 environmental clustering recovered ecological structure. Among 90 Cyanobacteriia species with embeddings, 35.6% were in a marine+sponge-dominant cluster; among 50 Mycobacteriaceae species, 34.0% were in a gut+sludge cluster and 20.0% in another gut cluster; and 729 Bacteroidota species were distributed across marine and gut-associated clusters. [src: gene_function_ecological_agora]

### Mobile-genetic-element context

The atlas-wide MGE-machinery baseline was 1.37% of KO-bearing gene clusters. The focal hypothesis sets had 0.57% for Mycobacteriaceae mycolic-acid, 0.00% for Cyanobacteriia PSII, and 0.00% for Bacteroidota PUL. These results indicate that the focal KOs are not themselves predominantly phage, transposase, integrase, plasmid, insertion-sequence, or recombinase products. [src: gene_function_ecological_agora]

PSII gene-neighborhood analysis examined 27,148 focal features and 218,321 neighbor pairs. A total of 10.91% of PSII focal features had at least one MGE neighbor within ±5 kb, compared with a Poisson baseline expectation of 10.6%; the mean MGE-neighbor fraction was 1.65%. PUL and mycolic gene-neighborhood scans were deferred because large-scale Spark and pandas joins exceeded memory limits. [src: gene_function_ecological_agora]

### Methodological contributions

The project contributed a per-rank Producer × Participation framework, Sankoff parsimony with recipient-rank gain attribution, D2 annotation-density residualization, a pangenome-to-genome-context MGE cross-walk, leaf_consistency for within-clade uncertainty, and exploratory genus-rank tree-based donor inference. The full atlas contained 11,829,746 Stable, 803,196 Innovator-Isolated, 741,587 Sink/Broker-Exchange, and 50,026 Innovator-Exchange tuples, with 314,607 insufficient-data tuples. [src: gene_function_ecological_agora]

The architecture census found median architectures per KO of 1 for PSII, 5 for mycolic-acid KOs, 15 for TCS-HK KOs, and 46 for mixed-category KOs. This supports the exploratory hypothesis that architectural diversity is associated with cross-clade exchange, while the focused architecture census does not establish causation. [src: gene_function_ecological_agora]

A multiple-testing correction pass enumerated 16 formal tests across four pre-registered hypotheses, six ecology tests, and six residualization replications. Fourteen of 16 survived family-wise Bonferroni correction; the two that did not were already reported nulls: Mycobacteriaceae × soil enrichment and the NB11 regulatory-versus-metabolic producer test. Leaf_consistency and M26 donor labels were descriptive classifications rather than hypothesis-test families. [src: gene_function_ecological_agora]

## Caveats and limits

The project did not identify donors at deep ranks because per-CDS sequence data were unavailable in queryable KBase Data Lakehouse schemas. M26 tree-based donor inference is exploratory and algebraically counts potential family-mate donors, which biases toward Open-Innovator classifications; composition-based confirmation and full DTL reconciliation remain future work. [src: gene_function_ecological_agora]

The PSII result is specifically a class-rank finding: the class-level sample had n = 21 PSII KOs, whereas genus, family, and order results were STABLE, and the phylum consumer statistic was unavailable because of insufficient reference data. The class-rank interpretation is consistent with PSII being a class-defining, ancient innovation, but it should not be generalized to all taxonomic ranks. [src: gene_function_ecological_agora]

The Alm 2006 quantitative correlation was not reproduced because the project’s 18,989-species substrate differs from the original 207-genome substrate, M22 measures tree-attributed gain events rather than all per-genome paralog expansion, and the definition of “recent” differs between the analyses. [src: gene_function_ecological_agora]

PUL and mycolic gene-neighborhood analyses were scale-bounded by a 723K-feature × 210K-contig join and pandas spatial-merge memory failures. The non-phage-borne conclusion for these systems therefore relies on per-cluster MGE-machinery rates and literature context, not complete cargo-neighborhood scans. [src: gene_function_ecological_agora]

Cyanobacteria BacDive coverage was only n = 4, the pangenome-openness cross-validation was null at atlas scale with Spearman r = −0.011 across 894 genera, and the targeted Mycobacteriaceae and Cyanobacteriia openness tests were underpowered with n = 10 and n = 83 genera, respectively. [src: gene_function_ecological_agora]

Cross-phase uncertainty was not propagated into a unified atlas confidence interval, bootstrap confidence intervals for individual M22 events were deferred, and Sankoff results were not comprehensively cross-validated against DTLOR or other modern reconciliation methods. Ecology results establish association or consistency with expected environments, not causal effects of environment on gene innovation. [src: gene_function_ecological_agora]

## Slots Into

- [[concepts/cofitness-network-architecture]] — Producer × Participation categories and the finding that architectural diversity is associated with cross-clade exchange.
- [[concepts/ecotype-environment-gene-content]] — Clade-specific gene-function patterns refined by biome consistency, phenotype anchors, and within-clade leaf_consistency.
- [[concepts/environment-embedding-geography]] — AlphaEarth environmental embeddings, k = 10 clustering, and focal-clade environmental concentration.
- [[concepts/environmental-resistome]] — Recent-to-ancient acquisition signatures for β-lactamases, CRISPR-Cas, TCS-HK, and housekeeping controls.
- [[concepts/pangenome-integration]] — Integration of KO presence, pangenome openness, GTDB phylogeny, and genome-context MGE measurements.
- [[concepts/multi-omics-integration]] — Cross-substrate convergence across phylogenomic scores, environmental metadata, phenotype tables, and gene-neighborhood evidence.
- [[concepts/gene-function-acquisition-depth]] — New concept candidate for Sankoff-derived acquisition depth, recent-to-ancient function-class signatures, and M22/leaf_consistency synthesis.
