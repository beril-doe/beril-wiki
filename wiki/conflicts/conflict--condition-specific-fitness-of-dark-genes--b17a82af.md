<!-- tension-hash: b17a82af36840c0d -->
# Stress Dominance Versus Stress Depletion in Dark-Gene Fitness: Two Comparisons in Tension

Dark genes are genes that lack functional annotation. This page records a disagreement about the conditions in which dark genes with strong fitness effects show those effects, which is covered in [[concepts/condition-specific-fitness-of-dark-genes]]. One claim says stress conditions dominate dark genes with strong effects overall. Another says truly dark genes with strong effects are depleted in stress relative to annotation-lag genes. The two claims use different comparisons, so they may not conflict directly. It matters because a reader could take the two statements as contradictory when they may describe different contrasts. Stating each comparison exactly keeps the question open.

## Evidence Sides

**Side A: stress dominates dark genes with strong effects overall**

- Across dark genes with strong effects, stress conditions dominate. [src: functional_dark_matter]
- Direction: stress is the leading condition class. The comparison is across all dark genes with strong effects overall. [src: functional_dark_matter]

**Side B: truly dark genes are depleted in stress relative to annotation-lag genes**

- Truly dark genes with strong effects are depleted in stress conditions relative to annotation-lag genes. [src: discoveries, truly_dark_genes]
- Direction: depletion of stress. The comparison is between truly dark genes and annotation-lag genes, not against all dark genes. [src: discoveries, truly_dark_genes]
- Polar effects (a mutation disturbing expression of downstream genes in the same operon) may inflate some phenotypes. [src: truly_dark_genes]

The input gives no numbers or thresholds for either side. Neither side is a null result.

## Possible Reconciliations

- **Hypothesis: different reference groups.** Side A describes the overall distribution of conditions. Side B describes a relative contrast between two subgroups. Stress could be the largest class in both subgroups while truly dark genes have a smaller share of it than annotation-lag genes. The input does not test this.
- **Hypothesis: polar effects distort one subgroup.** If polar effects inflate phenotypes unevenly, they could change the apparent stress share of one group. [src: truly_dark_genes] This is untested.

## Resolving Work

- Data: the strong-effect dark genes in both sources. Method: tabulate condition classes (stress, nutrient, community) separately for truly dark genes and annotation-lag genes, using one shared definition of strong effect. Question: is stress the largest class in both groups?
- Data: the same gene sets. Method: compare stress share between groups with one denominator, stated explicitly. Question: is the depletion still present when both claims use the same denominator?
- Data: operon structure for strong-effect truly dark genes. Method: flag genes where polar effects are plausible and repeat the stress comparison with and without them. Question: do polar effects change the direction of the depletion?
- Data: the gene lists behind each claim. Method: measure overlap between the groups. Question: do the two claims describe the same genes or different ones?
