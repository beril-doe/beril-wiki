<!-- tension-hash: 72138c3244fd8817 -->
# Module Core Enrichment vs. a Weak Genome-Wide Fitness–Conservation Link

Two analyses disagree about how tightly fitness importance tracks pangenome conservation — how often a gene sits in the *core* genome, the set of genes shared across essentially all genomes of a species. One works at the level of fitness modules: co-regulated functional units recovered by independent component analysis (ICA), a statistical decomposition of correlated fitness measurements. [src: module_conservation] [src: conservation_fitness_synthesis] It finds module genes clearly enriched in the core, which reads as coordinated evolutionary retention of whole functional units. The other works genome-wide across fitness categories and finds the association only weak, cautioning that some of the signal may be a detection limitation rather than biology. [src: fitness_effects_conservation] The two are not measuring the same quantity over the same gene set, which is itself part of the disagreement. What hangs on it: whether "this module is core" licenses an inference about the module's fitness importance, or merely describes where its genes sit in the pangenome. This page covers the single disagreement in the input tension; other tensions on [[concepts/fitness-module-detection-sensitivity]] are not treated here.

## Evidence Sides

**Side A — Module genes are measurably more core than background.** The module-conservation analysis found an 86.0% core fraction for module genes versus 81.5% for all genes. [src: module_conservation] The later synthesis reports the same contrast, 86% core module genes against an 81.5% baseline, across 1,116 modules. [src: conservation_fitness_synthesis]

**Side B — The genome-wide association is weak, and part of it may be a coverage artifact.** The genome-wide fitness-conservation analysis found only a weak association between fitness importance and conservation, and emphasized that novel singleton genes *may* appear neutral because of poor transposon coverage. [src: fitness_effects_conservation] That analysis spans approximately 194,000 genes. [src: fitness_effects_conservation] The synthesis likewise finds only a modest conservation gradient and documents that core genes may be laboratory-burdensome. [src: conservation_fitness_synthesis]

**Where the sides are not measuring the same thing.** These findings are not numerically identical estimands: the module result is conditional on detected, non-essential module members and selected module thresholds, whereas the genome-wide result spans broader fitness categories and approximately 194,000 genes. [src: module_conservation] [src: fitness_effects_conservation] The synthesis's position is that the enrichment stands but its interpretation is qualified — module conservation is compatible with coordinated retention, yet does not establish that modules are uniformly fitness-beneficial, environmentally essential, or independent of threshold and callability constraints. [src: conservation_fitness_synthesis]

## Possible Reconciliations

These are hypotheses, not established findings.

- **Estimand mismatch (strongest candidate).** Both sides may be right about different quantities: a conditional enrichment among callable, non-essential module members versus an unconditional gradient across all fitness categories. [src: module_conservation] [src: fitness_effects_conservation]
- **Selection by detectability.** If poor transposon coverage makes novel singleton genes appear neutral, module membership may itself select for well-measured genes, inflating module core fractions. [src: fitness_effects_conservation]
- **Threshold dependence.** The module core fraction is conditional on selected module thresholds; a different membership rule could move 86.0% with no change in biology. [src: module_conservation]
- **Conservation ≠ benefit.** Core genes may be laboratory-burdensome, so genuine core enrichment need not imply modules are fitness-beneficial under assay conditions. [src: conservation_fitness_synthesis]

## Resolving Work

- Recompute the module core fraction across a sweep of membership thresholds, reporting 86.0% versus 81.5% as a curve rather than a point, to test whether the offset survives threshold choice. [src: module_conservation]
- Restrict the genome-wide analysis to the same callable, non-essential gene set modules are drawn from, and ask whether the weak association strengthens once estimands are matched. [src: module_conservation] [src: fitness_effects_conservation]
- Stratify the approximately 194,000 genes by transposon coverage and re-estimate the association within well-covered strata only, quantifying how much weakness is callability rather than biology. [src: fitness_effects_conservation]
- Build a background set matched to module genes on coverage and essentiality, and test whether the 81.5% baseline rises toward 86% under matching. [src: module_conservation] [src: conservation_fitness_synthesis]
- Ask, for the 1,116 modules, whether core fraction predicts any independent measure of fitness importance; a null would sever conservation from fitness benefit at module level. [src: conservation_fitness_synthesis]
