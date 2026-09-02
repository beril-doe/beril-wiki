---
type: "Concept"
description: "How experiment count constrains the reliability of inferred fitness modules"
sources: ["summaries/fitness_modules__REPORT.md"]
---
# Experimental Depth Limits the Reliability of Fitness-Module Inference

Fitness-module inference uses independent component analysis (ICA), a statistical decomposition method, to identify groups of genes with coordinated fitness patterns across experiments. [src: fitness_modules] The reliability of these modules depends on experimental depth: organisms represented by fewer experiments produce weaker module structure, while broader experiment coverage supports more stable cofitness inference. [src: fitness_modules] This finding refines [[concepts/cofitness-network-architecture]] by treating module strength as a function of both network structure and the number of measured conditions. [src: fitness_modules]

## Evidence from the fitness-module analysis

The study identified 1,116 stable modules across 32 organisms, requiring each organism to have at least 100 experiments. [src: fitness_modules] Within these modules, 94.2% showed significantly elevated within-module cofitness by Mann-Whitney U test at p < 0.05, and within-module mean absolute correlation was 0.34 versus 0.12 in the background, corresponding to a 2.8x correlation enrichment. [src: fitness_modules] These results support the use of sufficiently deep experiment collections for detecting reproducible cofitness structure. [src: fitness_modules]

The report cautions that organisms with fewer than approximately 100 experiments produced weaker modules. [src: fitness_modules] Caulo, despite having 198 experiments, showed only 2.9x correlation enrichment, demonstrating that meeting a nominal experiment-count threshold does not guarantee uniformly strong module recovery. [src: fitness_modules] This observation supports [[concepts/fitness-experiment-depth-and-module-reliability]] as a distinct reliability concern within [[concepts/fitness-module-detection-sensitivity]]. [src: fitness_modules]

The analysis imposed a 40% component cap, meaning that the number of ICA components could not exceed 40% of the number of experiments. [src: fitness_modules] This cap was necessary to avoid FastICA convergence failures but may cause some modules to be missed in organisms with few experiments. [src: fitness_modules] Thus, limited depth can affect inference both by weakening cofitness estimates and by restricting the number of components that can be stably extracted. [src: fitness_modules]

## Interpretation and limits

The reported enrichment statistics indicate that ICA can recover biologically coherent process-level modules when experiment depth is adequate, but they do not establish a universal experiment count at which module inference becomes reliable. [src: fitness_modules] The Caulo result shows that experiment number alone is insufficient because module quality can remain organism-specific even above 100 experiments. [src: fitness_modules]

Module membership should therefore be interpreted as evidence for coordinated biological-process behavior rather than as a direct assignment of individual molecular functions. [src: fitness_modules] In held-out benchmarking, ortholog transfer achieved 95.8% strict precision, 91.2% coverage, and 0.934 F1, whereas Module-ICA achieved <1% strict precision and 23.3% coverage for specific KEGG KO assignments. [src: fitness_modules] This contrast supports [[concepts/gene-essentiality]] and [[concepts/process-level-versus-gene-level-fitness-inference]] by separating the reliability of process-level module detection from the reliability of gene-level annotation. [src: fitness_modules]

The experiment-depth limitation also affects cross-organism comparisons. [src: fitness_modules] Cross-organism alignment produced 1.15M bidirectional-best-hit pairs across 32 organisms and 13,402 ortholog groups, identifying 156 module families spanning 2+ organisms, including 28 spanning 5+, 7 spanning 10+, and 1 spanning 21 organisms. [src: fitness_modules] These conserved families provide evidence for shared co-regulation patterns, but differences in experimental depth and the component cap can influence which modules are detected in each organism. [src: fitness_modules] The resulting interpretation is therefore aligned with [[concepts/pangenome-integration]] while retaining the measurement-depth caveat. [src: fitness_modules]

## Practical implication

Fitness-module studies should report the number and diversity of experiments per organism, test module stability across experiment subsets, and distinguish failures of biological conservation from failures caused by insufficient experimental depth. [src: fitness_modules] Module support should be evaluated alongside within-module correlation enrichment, statistical significance, component-cap sensitivity, and reproducibility under resampling. [src: fitness_modules] These safeguards are especially important when extending module inference to organisms with sparse fitness profiles or when comparing module families across organisms with unequal experiment coverage. [src: fitness_modules]

## Open Directions

- Use matched experiment subsets and bootstrap or split-sample ICA to determine whether the 94.2% significant-module rate and 2.8x correlation enrichment remain stable as experiment count changes. [src: fitness_modules]
- Reanalyze organisms across a controlled range of experiment depths to test whether the approximately 100-experiment threshold predicts module stability and whether the 2.9x enrichment observed for Caulo reflects organism-specific biology or data composition. [src: fitness_modules]
- Vary the 40% component cap together with FastICA convergence diagnostics to quantify how many modules are missed under sparse experimental designs. [src: fitness_modules]
- Compare module recovery after balancing condition classes across organisms to determine whether experimental diversity, rather than experiment count alone, explains differences in module reliability. [src: fitness_modules]
- Test whether cross-organism module families remain detectable after downsampling every organism to the same number of experiments, using the 156 identified families as the reference set. [src: fitness_modules]
