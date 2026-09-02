---
type: "Concept"
description: "Fitness modules reveal biological-process context, not specific gene functions."
sources: ["summaries/fitness_modules__REPORT.md"]
---
# Process-Level Context Does Not Establish Gene-Level Function

Independent component analysis (ICA), a statistical method that decomposes correlated measurements into components, can identify co-regulated fitness modules without establishing the precise molecular function of each member gene. [src: fitness_modules] This distinction refines [[concepts/cofitness-network-architecture]] and [[concepts/gene-essentiality]]: fitness covariance is informative about process-level context, whereas sequence-based ortholog transfer is substantially stronger for gene-level function prediction. [src: fitness_modules]

## Evidence from Pan-Bacterial Fitness Modules

The [[summaries/fitness_modules__REPORT]] analyzed RB-TnSeq fitness data, a pooled transposon-mutant method for measuring gene fitness across conditions, from 32 organisms and identified 1,116 stable modules with at least 100 experiments per organism. [src: fitness_modules] Using an absolute component-weight threshold of |weight| >= 0.3 and a maximum of 50 genes per module produced biologically coherent modules with 94% enrichment and 2.8x correlation enrichment, whereas the initial D'Agostino K-squared membership approach produced modules containing 100-280 genes with 59% enrichment and 1-17x correlation. [src: fitness_modules]

The resulting modules showed strong internal structure: 94.2% had significantly elevated within-module cofitness by Mann-Whitney U test, a rank-based test of distributional differences, at p < 0.05; within-module mean |r| was 0.34 versus 0.12 in the background, giving a 2.8x enrichment; and module genes had 22.7x genomic-adjacency enrichment. [src: fitness_modules] These measurements support the interpretation that ICA modules capture coordinated biological processes and frequent operon co-localization, but they do not by themselves identify the exact function of every gene. [src: fitness_modules]

## Why Module Membership Is Not a KO Assignment

In held-out benchmarking, ortholog transfer achieved 95.8% strict precision, 91.2% coverage, and 0.934 F1, where F1 is the harmonic mean of precision and recall. [src: fitness_modules] Domain-based prediction achieved 29.1% precision, 66.6% coverage, and 0.401 F1, while Module-ICA achieved <1% strict precision and 23.3% coverage, and cofitness voting achieved <1% strict precision and 73.0% coverage. [src: fitness_modules]

The near-zero strict precision of Module-ICA and cofitness for specific KEGG KO assignments is explained by the resolution mismatch between modules and gene-level labels: KEGG KO groups averaged approximately 1.2 genes per unique KO, so a module with 20 annotated members typically contained 20 different KOs. [src: fitness_modules] Thus, module membership can indicate that a hypothetical protein participates in a shared process or co-regulated program, but it cannot establish that the protein has any particular KO-defined molecular function. [src: fitness_modules]

This evidence supports [[concepts/process-level-versus-gene-level-fitness-inference]] as a boundary on interpretation rather than a rejection of cofitness analysis. [src: fitness_modules] Module-ICA is effective for identifying co-regulated gene groups and biological-process context, whereas ortholog transfer is substantially better for predicting specific molecular functions. [src: fitness_modules]

## Annotation Coverage Does Not Remove the Resolution Problem

Adding PFam domains and lowering the enrichment-overlap threshold from 3 to 2 increased the module annotation rate from 8% to 80%, expanded annotated modules from 92 to 890, and unlocked 7.6x more function predictions. [src: fitness_modules] PFam provided the broadest annotation coverage, whereas KEGG KOs were too gene-specific for module-level enrichment. [src: fitness_modules] The improved annotation coverage therefore increases the amount of process-level interpretation available from modules, but it does not convert module associations into validated gene-level assignments. [src: fitness_modules]

Across the 32 organisms, the analysis generated 6,691 function predictions for hypothetical proteins, including 2,455 family-backed predictions representing 37% and 4,236 module-only predictions. [src: fitness_modules] The predictions used enrichment from KEGG, SEED, TIGRFam, and PFam, so their evidential basis ranged from cross-organism conservation to module-level or domain-level association rather than uniformly demonstrating a precise molecular function. [src: fitness_modules]

## Cross-Organism Conservation Is Still Not Identity

Cross-organism alignment produced 1.15M bidirectional-best-hit (BBH) pairs, where BBH denotes reciprocal best sequence matches, across 32 organisms and 13,402 ortholog groups. [src: fitness_modules] It identified 156 module families spanning 2+ organisms, including 28 spanning 5+, 7 spanning 10+, and 1 spanning 21 organisms; 145 families had consensus functional labels, representing 93% of the families. [src: fitness_modules]

These conserved module families provide evidence for recurring fitness-associated co-regulation across diverse bacterial phyla, including one family spanning 21 organisms. [src: fitness_modules] However, because the alignment used BBH ortholog pairs and ortholog groups, conserved module membership and consensus labels represent aligned conservation patterns rather than proof that every family member has an identical molecular function. [src: fitness_modules] This finding supports [[concepts/pangenome-integration]] while preserving the distinction between conservation of process context and identity of gene function. [src: fitness_modules]

## Interpretation Boundary

The appropriate claim from a fitness module is that a gene is associated with a coordinated biological process under the measured experimental conditions, not that the gene has a specific molecular function. [src: fitness_modules] A gene-level assignment requires independent evidence such as ortholog transfer or another direct functional validation, because module-level cofitness and domain-level enrichment do not provide the same resolution as a specific molecular-function assignment. [src: fitness_modules]

The interpretation is also conditional on data scale and analysis choices: organisms with fewer than approximately 100 experiments produced weaker modules, Caulo with 198 experiments showed only 2.9x correlation enrichment, and a 40% component cap was required to avoid FastICA convergence failures but may cause some modules to be missed in organisms with few experiments. [src: fitness_modules] PFam-based annotations provided the best coverage but operate at the domain level and may overcount functional associations. [src: fitness_modules]

## Open Directions

- Combine the 6,691 hypothetical-protein predictions with ortholog transfer, domain architectures, and targeted gene-level experiments to test which module-only predictions acquire specific molecular-function support. [src: fitness_modules]
- Reanalyze the held-out benchmark with process-level gold standards in addition to KEGG KO labels to ask whether Module-ICA has useful precision when evaluated against biological-process membership rather than gene-level identity. [src: fitness_modules]
- Use larger, condition-diverse RB-TnSeq datasets and compare module stability before and after the 40% component cap to determine which conserved modules are missed in organisms with fewer experiments. [src: fitness_modules]
- Test the 156 cross-organism module families with gene-neighborhood, domain-combination, and experimental perturbation data to determine whether shared module membership reflects conserved regulation, conserved pathway involvement, or recurrent genomic organization. [src: fitness_modules]
