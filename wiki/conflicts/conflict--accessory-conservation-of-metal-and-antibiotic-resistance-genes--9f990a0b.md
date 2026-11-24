<!-- tension-hash: 9f990a0bacd6ec50 -->
# Tension: Least-Conserved Metal and Antibiotic Genes in DvH Versus Core-Enriched Metal Fitness Genes in the Atlas

Two analyses disagree on how conserved metal-related and antibiotic-related genes are. Conservation here means the share of genes that are core, meaning present across the genomes compared, rather than accessory. A single-organism study of Desulfovibrio vulgaris Hildenborough (DvH) reported metal and antibiotic genes as the least conserved classes, but the differences were not significant. A multi-organism atlas found a high core share for metal-defect genes. The question matters because it is unclear what the compared gene sets represent: genes with any metal fitness defect, or only genes specific to metal stress. The answer determines what conservation can say about acquired versus core functions. See [[concepts/accessory-conservation-of-metal-and-antibiotic-resistance-genes]].

## Evidence Sides

**Side A: DvH shows the lowest conservation, without significance**
- DvH reported metal and antibiotic genes as the least conserved classes (71.2%, 73.4%). [src: field_vs_lab_fitness]
- The differences were not significant. [src: field_vs_lab_fitness] This is a null result and stays one.
- The metal-specificity follow-up shows only a small gap. [src: metal_specificity]

**Side B: the atlas shows high core conservation**
- The atlas found 87.4% core for metal-defect genes. [src: metal_fitness_atlas]
- The atlas attributes the discrepancy to condition-specific versus any-defect gene selection. [src: metal_fitness_atlas] This is the atlas's own explanation, not a tested result.

## Possible Reconciliations

- **Hypothesis 1: gene-set definition.** DvH may isolate genes important only under particular conditions, while the atlas counts any metal defect. Each would then measure a different population, so neither number overrides the other. This is the atlas's attribution. [src: metal_fitness_atlas]
- **Hypothesis 2: organism scope.** DvH is a single organism, and the atlas spans many. The DvH trend may be organism-specific. This is untested.
- **Hypothesis 3: a small real accessory signal.** The small gap in the metal-specificity result may be a modest accessory contribution that the DvH test, with its non-significant differences, could not resolve. [src: metal_specificity]

## Resolving Work

- **Data:** DvH fitness data with the atlas's any-defect and condition-specific definitions applied side by side. **Method:** recompute the core fraction under each definition. **Question:** does the DvH gene set move toward the atlas figure when the definition matches?
- **Data:** per-organism core fractions from the atlas. **Method:** a per-organism comparison with an odds ratio (a measure of enrichment relative to baseline) and a false discovery rate (FDR, a multiple-testing correction). **Question:** is DvH an outlier among the organisms, or typical?
- **Data:** metal-specific and general-stress gene sets. **Method:** a stratified test such as Cochran-Mantel-Haenszel (CMH), which pools comparisons across strata. **Question:** is the small accessory tilt reproducible across organisms? [src: metal_specificity]
- **Data:** gene annotations for the antibiotic and metal classes. **Method:** classify genes as specialized resistance mechanisms or general cellular processes, then compare conservation. **Question:** do specialized resistance genes differ from general stress genes in conservation?
- **Data:** mobile-element context for the genes. **Method:** test colocalization with mobile elements. **Question:** is low conservation linked to acquisition, or only to the gene-set definition?
