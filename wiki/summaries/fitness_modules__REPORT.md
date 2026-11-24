---
type: "Summary"
description: "Summary of the project Pan-bacterial Fitness Modules via Independent Component Analysis."
doc_type: "short"
full_text: "sources/fitness_modules__REPORT.md"
---
# Pan-bacterial Fitness Modules via Independent Component Analysis

Summary of the project Pan-bacterial Fitness Modules via Independent Component Analysis.

## Key Findings

### Module quality

Fitness ICA gave 1,116 stable modules across 32 organisms, all with >=100 experiments. [src: fitness_modules] Median module size was 7-50 genes, described as a biologically correct range. [src: fitness_modules] Of the modules, 94.2% showed significantly elevated within-module cofitness (Mann-Whitney U, p < 0.05). [src: fitness_modules] Within-module mean |r| was 0.34 versus background |r| of 0.12, a 2.8x enrichment. [src: fitness_modules] Module genes showed 22.7x genomic adjacency enrichment, which the report interprets as co-location in operons. [src: fitness_modules]

The membership threshold was critical. [src: fitness_modules] The initial D'Agostino K-squared approach gave 100-280 genes per module with weak cofitness signal (59% enriched, 1-17x correlation). [src: fitness_modules] Switching to absolute weight thresholds (|weight| >= 0.3, max 50 genes) gave coherent modules with 94% enriched and 2.8x correlation enrichment. [src: fitness_modules]

### Annotation

Adding PFam domains and lowering the enrichment overlap threshold from 3 to 2 raised module annotation from 8% to 80% (92 to 890 modules). This unlocked 7.6x more function predictions. [src: fitness_modules] PFam gave the broadest coverage. [src: fitness_modules] KEGG KOs (KEGG orthologs) were too gene-specific for module-level enrichment. [src: fitness_modules] PFam annotations are domain-level and may overcount functional associations. [src: fitness_modules]

### Benchmark against other methods

In a held-out test, 20% of KEGG-annotated genes were withheld and 4 methods predicted KO groups. [src: fitness_modules] Ortholog transfer was far better on strict precision. The rows below give strict precision, coverage and F1.

- Ortholog transfer: 95.8%, 91.2%, 0.934. [src: fitness_modules]
- Domain-based: 29.1%, 66.6%, 0.401. [src: fitness_modules]
- Module-ICA: <1%, 23.3%, F1 not reported. [src: fitness_modules]
- Cofitness voting: <1%, 73.0%, F1 not reported. [src: fitness_modules]

The report attributes the near-zero KO precision of Module-ICA and cofitness to KEGG KO groups being gene-level assignments (~1.2 genes per unique KO). [src: fitness_modules] A module with 20 annotated members typically has 20 different KOs. [src: fitness_modules] Predictions should therefore be read as biological process context, not exact KO assignments. [src: fitness_modules] Module-ICA is complementary to sequence-based methods. It finds co-regulated gene groups but should not predict specific molecular functions, where ortholog transfer is far superior. [src: fitness_modules]

### Cross-organism families

Alignment used 1.15M bidirectional best hit (BBH) pairs across 32 organisms to obtain 13,402 ortholog groups. [src: fitness_modules] It identified 156 module families spanning 2+ organisms (28 spanning 5+, 7 spanning 10+, 1 spanning 21). [src: fitness_modules] Of these, 145 (93%) had consensus functional labels. [src: fitness_modules] The largest family spans 21 organisms and is described as a pan-bacterial fitness module. [src: fitness_modules] The report reads this as showing conserved fitness regulons across diverse bacterial phyla. It also reads it as evidence for deeply conserved co-regulation programs. [src: fitness_modules]

### Function predictions

The analysis generated 6,691 function predictions for hypothetical proteins across all 32 organisms. [src: fitness_modules] Of these, 2,455 (37%) were family-backed, supported by cross-organism conservation, and 4,236 were module-only. [src: fitness_modules] Predictions were backed by module enrichment (KEGG, SEED, TIGRFam, PFam). [src: fitness_modules]

### Context

Sastry et al. (2019) showed the E. coli transcriptome consists largely of independently regulated modules recoverable by ICA. [src: fitness_modules] This project extends the approach from transcriptomic to fitness data across 32 organisms. It reports biologically coherent co-regulation structure in phenotypic compendia. [src: fitness_modules] Price et al. (2018) showed that mutant fitness data across thousands of conditions reveals gene function at scale. [src: fitness_modules] The report uses cofitness as its primary validation metric, building on the finding that correlated fitness profiles indicate shared function. [src: fitness_modules]

## Data and Methods

The data come from the Fitness Browser database kescience_fitnessbrowser (tables genefitness, gene, exps, ortholog). [src: fitness_modules] Pangenome gene cluster assignments come from kbase_ke_pangenome (gene_cluster table). [src: fitness_modules] ICA module definitions, gene weights and 32 per-organism parameter files are kept in data/modules. [src: fitness_modules] The data/annotations directory holds KEGG, SEED, TIGRFam and PFam functional annotations. [src: fitness_modules] The data/orthologs directory holds BBH ortholog pairs and ortholog groups. [src: fitness_modules]

## Caveats and Open Work

- Organisms with fewer than ~100 experiments give weaker modules. Caulo, with 198 experiments, showed only 2.9x correlation enrichment. [src: fitness_modules]
- The component cap (components <= 40% of experiments) avoids FastICA convergence failures but may miss modules in low-experiment organisms. [src: fitness_modules]
- Proposed next steps are to extend to more organisms as new RB-TnSeq datasets appear. [src: fitness_modules] The report also proposes integrating module predictions with core, auxiliary and singleton pangenome classes. [src: fitness_modules] It would test which modules are enriched in accessory genes. [src: fitness_modules] It would also build a web interface for browsing module families and predictions. [src: fitness_modules]

## Slots Into

- [[concepts/construction-and-validity-of-cofitness-gene-groups]]: the absolute weight threshold gave 94% enriched modules versus 59% for the initial approach. [src: fitness_modules]
- [[concepts/conservation-of-cofitness-modules-across-genomes-and-organisms]]: 156 cross-organism module families, with one spanning 21 organisms. [src: fitness_modules]
- [[concepts/function-prediction-for-uncharacterized-genes-by-guilt-by-association-and-ortholog-transfer]]: ortholog transfer reached 95.8% strict precision, while Module-ICA reached <1%. [src: fitness_modules]
- [[concepts/annotation-coverage-and-resolution-in-genome-wide-cofitness-analysis]]: PFam raised module annotation from 8% to 80%, while KEGG KOs were too gene-specific. [src: fitness_modules]
