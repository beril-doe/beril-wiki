<!-- tension-hash: 485af690b3df249c -->
# Conservation and Fitness Importance: Module-Level Enrichment Versus a Weak Genome-Wide Association

Two projects in this corpus disagree about how tightly a gene's fitness importance tracks its conservation across a species' pangenome — the set of genes present in some or all sequenced genomes of a lineage, whose "core" fraction is present in essentially all of them. The module-conservation analysis reports a higher core fraction for fitness-module genes than for all genes, while the genome-wide fitness-conservation analysis reports only a weak association and warns that the measurement itself may be biased. The disagreement matters because the strength of this link determines whether conservation can serve as a cheap proxy for fitness relevance when fitness data are missing, and because the two analyses do not measure the same quantity — a fact that is itself part of the dispute rather than a resolution of it. It bears directly on [[concepts/fitness-module-detection-sensitivity]], where module membership is already known to depend on thresholds.

## Evidence Sides

**Modules skew toward the conserved core.** The module-conservation analysis found an 86.0% core fraction for module genes versus 81.5% for all genes. [src: module_conservation] This estimate is conditional on detected, non-essential module members and on selected module thresholds — that is, on genes that ICA (independent component analysis, a decomposition of correlated fitness measurements into components) actually placed in a module under a chosen membership cutoff. [src: module_conservation]

**Genome-wide, the association is weak and possibly artefactual.** The genome-wide fitness-conservation analysis found only a weak association between fitness importance and conservation, and emphasized that novel singleton genes may appear neutral because of poor transposon coverage — a sampling gap in which too few insertion mutants are recovered to detect a real fitness effect. [src: fitness_effects_conservation] This analysis spans broader fitness categories and approximately 194,000 genes. [src: fitness_effects_conservation]

## Possible Reconciliations

- **Hypothesis: different estimands, not different worlds.** The two results may both be correct because they are not numerically identical estimands — one conditional on module membership, the other spanning broader fitness categories and approximately 194,000 genes. [src: module_conservation] [src: fitness_effects_conservation]
- **Hypothesis: threshold-induced enrichment.** Module membership selection may preferentially retain conserved genes, so the 86.0% versus 81.5% contrast could shrink or vanish under different module thresholds. [src: module_conservation]
- **Hypothesis: detection bias suppresses the genome-wide signal.** If poorly covered singleton genes are misclassified as neutral, the genome-wide association would be attenuated rather than genuinely weak. [src: fitness_effects_conservation]

## Resolving Work

- Recompute the module core fraction across a sweep of module membership thresholds, asking whether the 86.0% versus 81.5% gap is threshold-stable. [src: module_conservation]
- Restrict the genome-wide analysis to genes with adequate transposon coverage and re-test the fitness–conservation association, asking how much of its weakness is detection bias. [src: fitness_effects_conservation]
- Define one shared estimand — the same gene set, fitness categories and conservation measure — and estimate it under both pipelines, asking whether the directions still diverge. [src: module_conservation] [src: fitness_effects_conservation]
- Model module membership and conservation jointly on the broader gene set, asking whether module status carries information beyond fitness importance alone. [src: module_conservation] [src: fitness_effects_conservation]
