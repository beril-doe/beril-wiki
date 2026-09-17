<!-- tension-hash: d462367f5db0cebf -->
# Conflict: Essential-Gene Core Fraction — 82% or 86.1%?

Two projects in this corpus integrated gene-level fitness data with pangenome conservation (the fraction of genomes in a species' gene repertoire that carry a given gene; "core" genes are present in nearly all of them) and arrived at different core fractions for essential genes — genes for which no viable transposon-insertion mutants are recovered. One reports 82% core across approximately 194,000 genes from 43 bacteria [src: fitness_effects_conservation]; the other reports 86.1% core among 148,826 genes from 33 organisms [src: conservation_vs_fitness]. The gap matters because the essential-gene core fraction anchors the conservation-as-essentiality-predictor argument developed on [[concepts/gene-essentiality]]: it sets how strongly conservation can be used to nominate essential genes in organisms that have never been transposon-mutagenized. The disagreement is methodological rather than biological, and the two estimates must not be averaged into a single headline figure. [src: fitness_effects_conservation] [src: conservation_vs_fitness]

## Evidence Sides

**Side A — 82% core across ~194,000 genes from 43 bacteria.** This integration reports that essential genes are 82% core, and 82.2% core under a strongest-effect grouping in which genes are binned by their single most extreme fitness value rather than by fitness category. The estimate spans approximately 194,000 genes from 43 bacteria. [src: fitness_effects_conservation]

**Side B — 86.1% core among 148,826 genes from 33 organisms.** This integration reports that essential genes are 86.1% core, computed over 148,826 genes from 33 organisms. [src: conservation_vs_fitness]

## Possible Reconciliations

- *Hypothesis: denominator composition drives the gap.* The two analyses divide by different gene sets (approximately 194,000 [src: fitness_effects_conservation] versus 148,826 [src: conservation_vs_fitness]); if the larger set admits genes with weaker or absent pangenome mappings, its core fraction would be depressed without any underlying biological difference.
- *Hypothesis: organism panel drives the gap.* The panels differ (43 bacteria [src: fitness_effects_conservation] versus 33 organisms [src: conservation_vs_fitness]), and per-organism core fractions may be heterogeneous enough that panel membership alone moves the aggregate.
- *Hypothesis: pangenome mapping and core-threshold definitions differ.* "Core" is a threshold on genome presence; two projects applying different thresholds or different orthology-to-pangenome mappings would report different fractions from identical fitness calls.
- *Hypothesis: dataset version and organism filters differ.* The tension is described as involving datasets, organism filters, pangenome mappings, and denominators [src: fitness_effects_conservation] [src: conservation_vs_fitness]; a different release of the underlying fitness data, or a different inclusion filter on which organisms enter the aggregate, could shift the reported fraction with no change in biology.

## Resolving Work

- Recompute both core fractions on the intersection of the two organism panels — the organisms shared between the 43-bacteria and 33-organism sets — and report whether the 82% and 86.1% figures converge on identical inputs.
- Publish each project's gene-to-pangenome mapping coverage and the count of genes dropped for lack of a mapping, to test whether the ~194,000 versus 148,826 denominators explain the gap.
- State each project's numeric core-membership threshold and re-derive both fractions under each threshold in turn, holding essentiality calls fixed.
- Report per-organism core fractions with confidence intervals on both panels, to determine whether the aggregate difference is driven by a minority of organisms.
- Cross-tabulate the two essential-gene call sets on shared organisms and quantify the discordant genes' core status separately.
