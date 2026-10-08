---
type: "Summary"
description: "Summary of the fitness_modules project, which used independent component analysis on RB-TnSeq fitness data from 32 bacteria to find co-regulated fitness modules, align them into cross-organism module families, and give hypothetical proteins process-level function context."
doc_type: "short"
full_text: "sources/fitness_modules__REPORT.md"
---
# Pan-bacterial Fitness Modules via Independent Component Analysis

## Overview

This report tests independent component analysis (ICA) on RB-TnSeq fitness data across 32 organisms. ICA is a statistical decomposition into independent signals. RB-TnSeq (random barcode transposon sequencing) measures genome-wide mutant fitness by pooled barcoded transposon libraries. The goal is to find pan-bacterial fitness modules. The approach finds co-regulated biological-process modules rather than assigning precise molecular functions to individual genes, and ortholog transfer remains the stronger gene-level function-prediction method. [src: fitness_modules]

## Methods and Data

The project drew RB-TnSeq fitness scores, gene metadata, experiment conditions and ortholog mappings from the Fitness Browser, using the `kescience_fitnessbrowser` tables `genefitness`, `gene`, `exps` and `ortholog` ([[data/kescience-fitnessbrowser]]). [src: fitness_modules]

The `kbase_ke_pangenome` `gene_cluster` table supplied pangenome gene-cluster assignments for cross-organism alignment ([[data/kbase-ke-pangenome]]). [src: fitness_modules]

## Key Findings

### Module membership and annotation choices

The report calls a strict module-membership threshold critical: |weight| >= 0.3, with at most 50 genes per module. The initial D'Agostino K-squared approach gave 100-280 genes per module with weak cofitness signal (59% enriched, 1-17x correlation). After the switch to absolute weight thresholds, modules became biologically coherent (94% enriched, 2.8x correlation enrichment). [src: fitness_modules]

Two changes raised the module annotation rate from 8% to 80%, from 92 to 890 modules, and unlocked 7.6x more function predictions. The changes were adding PFam domains and lowering the enrichment-overlap threshold from 3 to 2. PFam gave the broadest annotation coverage. KEGG KOs were too gene-specific for module-level enrichment. [src: fitness_modules]

### Module quality

ICA found 1,116 stable modules across 32 organisms, all with >=100 experiments. [src: fitness_modules]

Module sizes are reported as a median of 7-50 genes per module, which the report calls the biologically correct range. The report gives a range of medians, not a single pooled median. [src: fitness_modules]

94.2% of modules showed significantly elevated within-module cofitness (Mann-Whitney U test, a rank-based nonparametric comparison; p < 0.05). [src: fitness_modules]

Within-module mean |r| was 0.34, compared with a background |r| of 0.12. The report gives this as a 2.8x enrichment. [src: fitness_modules]

Module genes showed 22.7x genomic-adjacency enrichment. The report reads this as module genes being co-located in operons. [src: fitness_modules]

### Held-out function-prediction benchmark

In the held-out evaluation, 20% of KEGG-annotated genes were withheld and 4 methods predicted their KO groups. [src: fitness_modules]

Strict benchmark results (precision / coverage / F1) [src: fitness_modules]:
- Ortholog transfer: 95.8% / 91.2% / 0.934
- Domain-based: 29.1% / 66.6% / 0.401
- Module-ICA: <1% / 23.3% / no F1 reported (null result for strict KO precision)
- Cofitness voting: <1% / 73.0% / no F1 reported (null result for strict KO precision)

Module-ICA and cofitness had near-zero strict KO precision because KEGG KO groups are gene-level assignments (~1.2 genes per unique KO). A module with 20 annotated members typically has 20 different KOs. The report therefore says function predictions should be read as biological-process context, not exact KO assignments. [src: fitness_modules]

### Cross-organism module families

Cross-organism alignment used 1.15M bidirectional-best-hit (BBH) pairs across 32 organisms to form 13,402 ortholog groups. [src: fitness_modules]

The alignment found 156 module families spanning 2+ organisms. Of these, 28 spanned 5+ organisms, 7 spanned 10+ and 1 spanned 21. The report calls the largest family, spanning 21 organisms, a pan-bacterial fitness module. [src: fitness_modules]

145 annotated families carried consensus functional labels (93%). [src: fitness_modules]

### Function predictions for hypothetical proteins

The analysis made 6,691 function predictions for hypothetical proteins across all 32 organisms. Of these, 2,455 (37%) were family-backed, meaning cross-organism conservation supports them. The other 4,236 were module-only predictions. [src: fitness_modules]

The predictions rest on module enrichment using KEGG, SEED, TIGRFam and PFam annotations. [src: fitness_modules]

### Interpretation

The report calls Module-ICA complementary to sequence-based methods. It is good at finding co-regulated gene groups (biological-process modules) but should not be used to predict specific molecular functions. For that task ortholog transfer is far better and remains the gold standard for gene-level function prediction (95.8% precision). Module-ICA fills a different niche: identifying which biological processes an uncharacterized gene takes part in. [src: fitness_modules]

The 6,691 function predictions for hypothetical proteins should be read as "involved in [biological process]" rather than "has function [specific KO]." [src: fitness_modules]

The report presents the cross-organism module families, the largest spanning 21 organisms, as evidence of conserved fitness co-regulation across diverse bacteria. This is the report's interpretation of an alignment result and keeps the line between process-level module context and gene-level function identity. [src: fitness_modules]

### Literature context

As external context, the report cites Sastry et al. (2019), "The Escherichia coli transcriptome mostly consists of independently regulated modules," *Nat Commun* 10, 5536, PMID 31767856. That study showed ICA recovers independently regulated modules from the *E. coli* transcriptome. The report says its cofitness-based approach extends this framework from transcriptomic data to fitness data across 32 organisms. That extension is the report's interpretation. [src: fitness_modules]

The report also cites Price et al. (2018), "Mutant phenotypes for thousands of bacterial genes of unknown function," *Nature* 557, 503--509, PMID 29769716. That study showed mutant fitness data across thousands of conditions reveals gene function at scale. The project's use of within-module cofitness as its main validation metric builds on Price et al.'s finding that genes with correlated fitness profiles share biological function. [src: fitness_modules]

## Figures

The report includes these figures [src: fitness_modules]:
- PCA eigenvalue spectrum used to select components across organisms.
- Distribution of module sizes across all 32 organisms.
- Cofitness validation: within-module versus background correlation distributions.
- Strict benchmark: precision and coverage by method.
- Neighborhood benchmark: performance when nearby KO matches are allowed.
- Cross-organism module families: size distribution and taxonomic span.
- Functional enrichment of modules by annotation source.
- Function prediction summary: family-backed versus module-only predictions.

## Caveats

The report warns that organisms with fewer than ~100 experiments produce weaker modules. Its example is Caulo, with 198 experiments and only 2.9x correlation enrichment. That example does not fall below the stated ~100-experiment threshold, so it is internally inconsistent as written and is not clear support for the threshold. [src: fitness_modules]

A 40% component cap (components <= 40% of experiments) was needed to avoid FastICA convergence failures. It may cause some modules to be missed in low-experiment organisms. [src: fitness_modules]

PFam-based annotations gave the best coverage, but they work at the domain level and may overcount functional associations. [src: fitness_modules]

The module and annotation results depend on analysis choices. The initial D'Agostino K-squared membership approach gave oversized, weakly enriched modules. The reported improvements came only after the switch to absolute weight thresholds and a lower enrichment-overlap threshold. [src: fitness_modules]

The cross-organism alignment used BBH ortholog pairs and ortholog groups. The 156 module families and their consensus labels therefore show aligned conservation patterns, not proof that every member has an identical molecular function. [src: fitness_modules]

## Slots Into

- [[concepts/fitness-module-detection-sensitivity]] — the |weight| >= 0.3 / max-50 threshold versus D'Agostino K-squared, the 8% to 80% annotation jump from PFam and a lower overlap threshold, the 40% component cap, and the problematic ~100-experiment warning all show how much module detection depends on analysis choices. [src: fitness_modules]
- [[concepts/ontology-and-category-schema-sensitivity]] — PFam's broad but domain-level coverage, compared with gene-specific KEGG KOs (~1.2 genes per unique KO), shows annotation-schema granularity driving enrichment and benchmark outcomes. [src: fitness_modules]
- [[concepts/evidence-triangulation-for-functional-annotation]] — the held-out benchmark (ortholog transfer 95.8% precision versus <1% for Module-ICA and cofitness voting) and the split of 6,691 predictions into family-backed and module-only show how fitness, domain and ortholog evidence complement one another. [src: fitness_modules]
- [[concepts/pathway-versus-reaction-evidence-resolution]] — near-zero strict KO precision alongside process-level coherence supports reading module predictions as process context, not exact KO assignments. [src: fitness_modules]
- [[concepts/cofitness-network-architecture]] — 1,116 ICA modules, 94.2% with elevated within-module cofitness, mean |r| of 0.34 versus 0.12, and 156 cross-organism module families describe modular cofitness structure. [src: fitness_modules]
- [[concepts/genomic-dispersal-functional-coupling]] — 22.7x genomic-adjacency enrichment of module genes links co-regulated fitness modules to operon co-location. [src: fitness_modules]
- [[concepts/cross-species-fitness-transferability]] — 1.15M BBH pairs, 13,402 ortholog groups, 156 module families (1 spanning 21 organisms) and 145 consensus-labelled families test how far fitness modules carry across species. [src: fitness_modules]
- [[concepts/experimental-prioritization-of-functional-dark-matter]] — 6,691 process-level predictions for hypothetical proteins are candidates to prioritize for experimental follow-up. [src: fitness_modules]
- [[concepts/gene-essentiality]] — the held-out benchmark shows cofitness modules give process-level context, while ortholog transfer gives stronger gene-level function prediction. [src: fitness_modules]
- [[concepts/pangenome-integration]] — the BBH pairs, ortholog groups and pangenome gene-cluster input connect fitness modules to conserved and hypothetical genes across organisms. [src: fitness_modules]
- [[concepts/condition-specific-fitness]] — the analysis extends condition-dependent fitness profiling from single-gene associations to independently regulated modules across fitness experiments. [src: fitness_modules]
