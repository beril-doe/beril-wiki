---
type: "Concept"
description: "How ICA module calls change with membership thresholds and decomposition limits"
sources: ["summaries/fitness_modules__REPORT.md"]
---
# Fitness-Module Discovery Depends on Thresholds and Decomposition Constraints

Independent component analysis (ICA), a statistical decomposition method, can identify co-regulated fitness modules from RB-TnSeq fitness data, but the resulting module structure is sensitive to membership thresholds, annotation settings, experiment count, and the allowed number of components. [src: fitness_modules] The method is therefore best interpreted as a process-level discovery tool rather than a direct assignment of precise molecular functions to individual genes. [src: fitness_modules]

## Threshold choice changes module quality

The initial D'Agostino K-squared membership approach produced modules containing 100-280 genes, with 59% enrichment and 1-17x correlation enrichment. [src: fitness_modules] Replacing that rule with an absolute component-weight threshold of |weight| >= 0.3 and limiting each module to a maximum of 50 genes produced biologically coherent modules, with 94% enrichment and 2.8x correlation enrichment. [src: fitness_modules] These results show that thresholding is not a cosmetic post-processing choice: it changes module size and the strength of the recovered cofitness signal. [src: fitness_modules]

The final analysis identified 1,116 stable modules across 32 organisms, with each organism represented by at least 100 experiments. [src: fitness_modules] Module sizes had a median range of 7-50 genes. [src: fitness_modules] Of these modules, 94.2% showed significantly elevated within-module cofitness by Mann-Whitney U test at p < 0.05. [src: fitness_modules] Within-module mean |r| was 0.34 versus 0.12 in the background, corresponding to a 2.8x enrichment, while module genes showed 22.7x genomic-adjacency enrichment. [src: fitness_modules] The adjacency result supports the interpretation that many recovered modules reflect operon co-localization as well as correlated fitness behavior. [src: fitness_modules]

## Decomposition constraints limit what can be recovered

The analysis imposed a 40% component cap, meaning that the number of components could not exceed 40% of the number of experiments, to avoid FastICA convergence failures. [src: fitness_modules] This constraint improves computational stability but may cause some modules to be missed in organisms with few experiments. [src: fitness_modules] The report also notes that organisms with fewer than approximately 100 experiments produced weaker modules, while the example of Caulo, with 198 experiments, showed only 2.9x correlation enrichment. [src: fitness_modules] Together, these observations indicate that experiment count and decomposition limits affect both the sensitivity and comparability of module discovery across organisms. [src: fitness_modules]

## Annotation thresholds do not equal discovery thresholds

Lowering the enrichment-overlap threshold from 3 to 2 and adding PFam domains increased the module annotation rate from 8% to 80%. [src: fitness_modules] The number of annotated modules increased from 92 to 890, and the resulting changes unlocked 7.6x more function predictions. [src: fitness_modules] PFam provided the broadest annotation coverage, whereas KEGG KOs were too gene-specific for module-level enrichment. [src: fitness_modules] Because PFam operates at the domain level, its broader coverage may overcount functional associations. [src: fitness_modules]

These annotation choices should be distinguished from the component-membership threshold: the |weight| >= 0.3 rule determines which genes enter a module, whereas the enrichment-overlap threshold affects how module content is associated with functional annotations. [src: fitness_modules] The report's contrast between the initial D'Agostino K-squared approach and the absolute-weight approach shows that both module construction and downstream annotation settings can alter apparent biological yield. [src: fitness_modules]

## Process-level modules are not gene-level function calls

In a held-out benchmark withholding 20% of KEGG-annotated genes, ortholog transfer achieved 95.8% strict precision, 91.2% coverage, and 0.934 F1. [src: fitness_modules] Domain-based prediction achieved 29.1% precision, 66.6% coverage, and 0.401 F1. [src: fitness_modules] Module-ICA achieved <1% strict precision and 23.3% coverage, while cofitness voting achieved <1% strict precision and 73.0% coverage. [src: fitness_modules] These results support using ortholog transfer for specific molecular-function prediction and using ICA modules for biological-process context. [src: fitness_modules]

Module-ICA and cofitness had near-zero strict KEGG KO precision because KEGG KO groups are gene-level assignments, averaging approximately 1.2 genes per unique KO, whereas a module with 20 annotated members typically contained 20 different KOs. [src: fitness_modules] The 6,691 function predictions generated for hypothetical proteins should therefore be interpreted as process-level evidence rather than proof of a specific KO-defined function. [src: fitness_modules] Of those predictions, 2,455 were family-backed, representing 37% and carrying cross-organism conservation support, while 4,236 were module-only predictions. [src: fitness_modules]

## Cross-organism stability is also alignment-dependent

Cross-organism alignment produced 1.15M bidirectional-best-hit (BBH) pairs across 32 organisms and 13,402 ortholog groups. [src: fitness_modules] It identified 156 module families spanning 2+ organisms, including 28 spanning 5+, 7 spanning 10+, and 1 spanning 21 organisms. [src: fitness_modules] A total of 145 families had consensus functional labels, representing 93% of the families. [src: fitness_modules] These results provide evidence for conserved fitness regulons across diverse bacterial phyla, but the BBH-based alignment represents conserved co-regulation patterns rather than proof that every family member has an identical molecular function. [src: fitness_modules]

The threshold and decomposition sensitivities therefore qualify, rather than invalidate, the cross-organism result: stable modules can reveal conserved process-level structure, but their membership and annotation depend on the analysis regime. [src: fitness_modules] This finding **supports** [[concepts/cofitness-network-architecture]] by quantifying how module construction affects recovered network structure. [src: fitness_modules] It **refines** [[concepts/condition-specific-fitness]] by extending condition-dependent fitness analysis from individual genes to independently regulated modules. [src: fitness_modules] It also **supports** [[concepts/gene-essentiality]] and [[concepts/pangenome-integration]] by separating gene-level ortholog evidence from module-level functional context and by connecting module families to cross-organism ortholog groups. [src: fitness_modules]

The full project report is available at [[summaries/fitness_modules__REPORT]]. [src: fitness_modules]

## Open Directions

- Re-run ICA across organisms after systematically varying the |weight| threshold, the 50-gene maximum, and the 40% component cap; test which settings preserve the 94.2% within-module significance rate, 2.8x correlation enrichment, and 22.7x genomic-adjacency enrichment. [src: fitness_modules]
- Use matched experiment subsampling and convergence diagnostics to quantify how module recovery changes below and above approximately 100 experiments, including the Caulo case with 198 experiments and 2.9x correlation enrichment. [src: fitness_modules]
- Compare PFam, KEGG KO, and other annotation layers at fixed module memberships to determine whether the increase from 8% to 80% annotation reflects genuine biological coverage or domain-level overcounting. [src: fitness_modules]
- Benchmark module-level predictions against independently measured phenotypes or perturbation data to test whether process-level predictions improve biological interpretation despite <1% strict KEGG KO precision. [src: fitness_modules]
- Reconstruct cross-organism module families under alternative orthology definitions and test whether the 156 families, including the family spanning 21 organisms, remain stable without assuming identical molecular functions. [src: fitness_modules]
