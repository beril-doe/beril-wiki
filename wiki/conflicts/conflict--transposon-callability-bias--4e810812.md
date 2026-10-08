<!-- tension-hash: 4e810812bf7ff21b -->
# Does Excluding Putative Essential Genes Raise or Lower the Baseline Core Fraction?

Fitness-based conservation analyses compare genes that matter under a condition against a baseline core fraction. That baseline is the share of genes classified as core in a species pangenome, which is the full gene repertoire across its sequenced genomes. Both analyses here exclude putatively essential genes from their fitness-based baselines. Projects in this corpus disagree about which way that exclusion moves the baseline. [src: metal_specificity, field_vs_lab_fitness] The direction matters because it decides whether reported core-enrichment effects are conservative or inflated. It also bears on a wider risk, described in [[concepts/transposon-callability-bias]]. Transposon mutants are strains carrying an inserted mobile DNA element, and the risk is that a gene with no such insertion is read as essential when technical or sequence features prevented insertion or detection.

## Evidence Sides

**Exclusion inflates the baseline (metal-specificity analysis)**

The metal-specificity analysis states that excluding putative essentials biases all categories toward core enrichment. On that basis its true baseline core fraction is likely lower than 81%. [src: metal_specificity]

**Exclusion deflates the baseline (field-versus-lab analysis)**

The field-versus-lab analysis states that including its 678 excluded essential genes (80.1% core) would raise its overall baseline slightly. [src: field_vs_lab_fitness] It adds that this would not change its condition-class comparisons, which are among non-essential genes only. [src: field_vs_lab_fitness]

**Scope note**

The two claims concern different organism sets and baselines. They are recorded here as study-specific assertions, not reconciled. [src: metal_specificity, field_vs_lab_fitness]

## Possible Reconciliations

- *Hypothesis:* The direction depends on how core the excluded essentials are relative to each study's non-essential baseline. Under this hypothesis, the claims could both hold, because they apply to different organisms and pangenome resolutions.
- *Hypothesis:* The claims address different quantities. The first concerns bias across all categories when essentials are absent. The second concerns the overall baseline when essentials are added back, while comparisons stay restricted to non-essential genes.
- *Hypothesis:* Callability bias, meaning genes that lack insertions for technical rather than biological reasons, puts different non-essential genes into the excluded set in each study. Under this hypothesis, the composition of the excluded set differs between studies and so does the direction of its effect.

## Resolving Work

- **Recompute both baselines.** Take each study's organism set and pangenome core/accessory calls, and compute the baseline core fraction with and without the putatively essential genes. Does the sign of the change match each study's stated direction?
- **Harmonize the essentiality calls.** Apply a single essentiality-calling rule, based on transposon insertion density and gene length, to both studies' organisms. Does the conflict persist once "putatively essential" is defined the same way in both?
- **Test the effect on reported comparisons.** Re-run the metal-specificity category enrichments both against a baseline restricted to non-essential genes and against an all-gene baseline. Does the baseline choice shift the enrichments in the direction that analysis states?
- **Test callability as a confounder.** Model each gene's core status against its exclusion status, adding gene length and insertion-site density as covariates (additional explanatory variables in the model). Does exclusion predict core status once callability is controlled?
