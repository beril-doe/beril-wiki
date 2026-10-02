<!-- tension-hash: 52b853b5ce3a2fc8 -->
# How wide is the essentiality–conservation gap: 86.1% versus 81.2%, or 82% versus 66%?

Two analyses in this corpus quantify how much more often essentiality-associated genes fall in the *core* genome — the genes present across effectively all genomes of a clade's pangenome — and they report gaps of very different size, measured against different comparison classes. Both point the same direction, so the disagreement is not about sign but about magnitude, and about whether the magnitude is a property of bacteria or of the analysis. This matters because the width of the gap is what decides whether a core/auxiliary boundary can be used as a proxy for viability requirements at all, a question that runs through [[concepts/core-genome-burden-paradox]], [[concepts/essentiality-assay-discordance]] and [[concepts/pangenome-core-boundary-and-clade-size-bias]]. One limit is fixed at the outset: the two results are directionally consistent but differ in category definitions and organism sets, and neither resolves the poor binary agreement between insertion assays and complete-knockout assays. [src: fitness_effects_conservation, conservation_vs_fitness]

## Evidence Sides

**The wide gradient (43 organisms, essential vs always-neutral).** One conservation analysis reports 82% core for essential genes versus 66% core for always-neutral genes — genes with no detected fitness effect in any experiment — across 43 bacteria. [src: fitness_effects_conservation, conservation_vs_fitness] The same 82%-versus-66% gradient is carried by the 43-organism synthesis and an independent analysis. [src: conservation_vs_fitness, conservation_fitness_synthesis, fitness_effects_conservation]

**The narrow enrichment (33 organisms, essential vs non-essential).** The newer linkage analysis, which joins fitness data to pangenome clusters, reports 86.1% core for essential genes versus 81.2% for non-essential genes across 33 organisms. [src: fitness_effects_conservation, conservation_vs_fitness] This result **supports** a positive essentiality–conservation association, while the differing effect sizes leave the magnitude sensitive to dataset composition and operational definitions. [src: conservation_vs_fitness]

**The comparability objection.** Both concept pages record that the two sets of figures are not directly comparable, because the cohorts and classifications differ. [src: conservation_vs_fitness, conservation_fitness_synthesis, fitness_effects_conservation] They should not be reconciled silently: they arise from different organism sets, phenotype categories, and integration procedures, so the difference is itself evidence that the estimated conservation boundary is analysis-dependent. [src: conservation_vs_fitness; fitness_effects_conservation]

## Possible Reconciliations

- *Hypothesis — denominator contrast:* the wide gap may reflect a contrast against always-neutral genes specifically, while the narrow gap contrasts against all non-essential genes, a category that would absorb conserved-but-non-essential genes. Neither source tests this directly. [src: fitness_effects_conservation, conservation_vs_fitness]
- *Hypothesis — cohort composition:* the 33-organism and 43-organism sets may differ in clade representation enough to shift both core fractions upward together, as the higher baselines on the narrow side suggest. [src: conservation_vs_fitness; fitness_effects_conservation]
- *Hypothesis — integration procedure:* differing gene-to-cluster linkage procedures may set the core boundary at different strictness, making the boundary itself the analysis-dependent quantity. [src: conservation_vs_fitness; fitness_effects_conservation]

## Resolving Work

- Re-run both classifications on the intersection of the 33- and 43-organism cohorts, holding phenotype categories fixed: does the gap converge when organism set is controlled?
- Recompute the 33-organism linkage using an always-neutral rather than a non-essential comparison class: how much of the gap difference is the denominator?
- Report core fractions across a sweep of core-membership thresholds for both analyses: is the reported gap stable, or a threshold artifact?
- Hold the gene-to-cluster integration procedure constant across both analyses and compare per-organism gaps: does the procedure, not biology, set the magnitude?
- Report per-organism gaps rather than pooled fractions on both sides: is the discrepancy driven by a few clades or distributed?
