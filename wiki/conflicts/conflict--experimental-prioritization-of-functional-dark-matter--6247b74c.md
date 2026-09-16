<!-- tension-hash: 6247b74c28584b0b -->
# Stress dominance versus stress depletion among strong-phenotype dark genes

Two projects describe the role of stress conditions in dark-gene fitness phenotypes in apparently opposite directions. One reports that stress conditions dominate among dark genes with strong fitness effects. [src: functional_dark_matter] The other reports that "truly dark" genes, which remain hypothetical after modern reannotation, are depleted in stress relative to "annotation-lag" genes. [src: truly_dark_genes] This matters because framing dark genes as stress-response candidates shapes how they are ranked for experiments in [[concepts/experimental-prioritization-of-functional-dark-matter]]. Neither analysis is normalized by condition coverage, the bias described in [[concepts/fitness-condition-coverage-prioritization-bias]]. [src: functional_dark_matter, truly_dark_genes, caulobacter_fur_lipida_loss]

## Evidence Sides

**Side A: stress dominates among dark genes overall**

The overall dark-gene analysis reports that stress conditions produce the largest concentration of strong dark-gene phenotypes. [src: functional_dark_matter] Put another way, stress conditions dominate among dark genes with strong fitness effects. [src: functional_dark_matter] This side describes overall composition and makes no comparison between dark-gene subsets.

**Side B: truly dark genes are depleted in stress relative to annotation-lag genes**

Among strong-phenotype genes, the truly dark analysis reports stress proportions of 28.7% for truly dark genes versus 43.2% for annotation-lag genes, with odds ratio (OR, the odds of a stress phenotype in one group divided by the odds in the other) = 0.53 and p < 0.001 (p, the probability of a difference at least this large if the groups did not differ). [src: truly_dark_genes] The same report separately gives stress at 43.3% versus 54.7% in another comparison. [src: truly_dark_genes] The concept page places the 43.3% vs 54.7% pair in the report's Results and the 28.7% vs 43.2% pair in its Key Findings. [src: truly_dark_genes] The central digest also records OR=0.53, p<0.001. [src: discoveries] This side contrasts two dark-gene subsets. The two internal pairs of figures are reported as given and are not reconciled.

## Possible Reconciliations

- **Hypothesis 1: different denominators.** Stress may be prominent among dark genes overall [src: functional_dark_matter] while being less characteristic of the residual genes that resist reannotation. [src: truly_dark_genes] On this reading, Side A describes overall composition and Side B contrasts two subsets, so the two need not conflict.
- **Hypothesis 2: coverage artifact.** Neither analysis is normalized by condition coverage. Stress dominance may therefore partly reflect how numerous stress experiments are, as in the 95 stress experiments of the *Caulobacter* compendium. [src: functional_dark_matter, truly_dark_genes, caulobacter_fur_lipida_loss]
- **Hypothesis 3: internal inconsistency.** The two stress-proportion pairs reported within the truly dark analysis may come from different gene sets or condition classifications. If so, how large the depletion is depends on which comparison is used. [src: truly_dark_genes]

## Resolving Work

- Using the Fitness Browser condition metadata, recompute stress phenotype rates per experiment rather than per gene. This tests whether Side A's stress dominance persists once the number of stress experiments is controlled for.
- On the shared dark-gene table, apply one common denominator and one strong-phenotype threshold to compute stress proportions for the overall set, the annotation-lag subset and the truly dark subset. This tests whether the two sides disagree once their definitions are aligned.
- Trace both reported pairs in the truly dark report (28.7% vs 43.2% and 43.3% vs 54.7%) back to their gene sets and condition categories. This identifies which comparison the OR = 0.53 belongs to.
- Within organisms that have deep stress coverage, such as the *Caulobacter* compendium, fit a stratified model of truly dark versus annotation-lag status crossed with condition class. This tests whether the depletion holds once each organism's coverage is accounted for.
