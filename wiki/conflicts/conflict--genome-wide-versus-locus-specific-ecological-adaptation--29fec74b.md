<!-- tension-hash: 29fec74b06bb98c4 -->
# Does Pangenome Openness Speak to Where Ecological Adaptation Acts?

Two projects in this corpus bear on the same question from different levels of resolution, and their results sit uneasily together without cancelling each other. A pangenome-openness test — pangenome openness being the degree to which a species keeps acquiring new genes as more genomes are sampled, rather than saturating at a fixed gene complement — returned a null relationship with both environment and phylogeny effects. A separate line of evidence finds ecological signal concentrated in particular functional categories within species. The disagreement is about what a genome-summarizing metric is entitled to say about locus-level ecology, and it matters because a null at the whole-pangenome scale is easy to read as a null about ecological adaptation generally. This tension is recorded on [[concepts/genome-wide-versus-locus-specific-ecological-adaptation]].

## Evidence Sides

**Openness is uninformative about eco-phylo dominance.** The null relationship between pangenome openness and environment or phylogeny effects **qualifies** the interpretation that broad pangenome structure can explain genome-wide versus locus-specific ecological dynamics: openness did not predict either effect. [src: pangenome_openness] This is a null result and stays one — it is the absence of a predictive relationship, not evidence that environment fails to shape gene content. Its scope is the pangenome-level summary statistic, not the genes underneath it.

**The null does not reach the loci where ecology is claimed to act.** The openness test did not directly compare individual loci or functional categories. [src: pangenome_openness] It therefore does not contradict the evidence for functional differentiation, while leaving unresolved whether openness metrics conceal category-specific ecological associations. [src: pangenome_openness, ecotype_functional_differentiation] On this side the claim is a scope objection rather than a counter-measurement: the denominator of the openness test is species-level pangenome structure, whereas the functional-differentiation claim is indexed to categories of genes.

## Possible Reconciliations

- *Hypothesis:* openness and locus-level ecology are genuinely independent axes, so a null at the pangenome scale and a positive signal at the category scale can both hold without contradiction. [src: pangenome_openness, ecotype_functional_differentiation]
- *Hypothesis:* openness aggregates ecologically responsive and ecologically inert accessory genes into a single number, and averaging across categories cancels opposing associations, producing a null that conceals structure. [src: pangenome_openness]
- *Hypothesis:* gene acquisition tracks opportunity rather than niche, so open pangenomes need not be environment-driven even where specific loci are. [src: pangenome_openness]

## Resolving Work

- Recompute environment and phylogeny effects per functional category within each species, then test openness against each category's effect separately — does any category recover the association the pooled test missed?
- Partition accessory genes by category before estimating openness, yielding category-specific openness curves — do ecologically differentiated categories have different saturation behaviour from the rest?
- Test whether species with strong within-species functional differentiation are distinguishable from those without on any pangenome-level statistic — is the null specific to openness or general to genome-summarizing metrics?
- Re-run the openness test on the species subset in which gene-content subpopulations were actually detected, to check whether the null is driven by species where the locus-level claim does not apply. [src: pangenome_openness, ecotype_functional_differentiation]
