<!-- tension-hash: 5a54a7b7d5f3aa16 -->
# Conflict: Does Pangenome Openness Carry a Lineage Signal, or None at All?

Two projects in this corpus put pangenome openness — the degree to which a species keeps acquiring new genes as more of its genomes are sequenced, rather than saturating at a fixed gene set — on opposite sides of a question about signal. One reports that, in the matched species set, openness does not predict environment or phylogeny effect sizes; the other reports openness associations that depend on lineage. This is a scope tension rather than a head-on contradiction: the two analyses use different response variables, and the corpus does not yet contain a test that would tell whether the lineage-dependent pattern is real structure or the phylogenetic confounding described in [[concepts/phylogenetic-confounding-of-pangenome-associations]]. It matters because openness is widely used as a shorthand for "this species adapts by gene acquisition," and a null on one response variable does not license or forbid that reading on another.

## Evidence Sides

**Openness predicts nothing about environment or phylogeny effects in the matched species set.** In the matched species set, openness did not predict either environment or phylogeny effect sizes. [src: pangenome_openness; amr_pangenome_atlas] The result stands as a null on both response variables within that species set.

**Openness associations are lineage-dependent for antimicrobial resistance genes.** The antimicrobial resistance (AMR) analysis — AMR genes confer resistance to antibiotics — showed lineage-dependent openness associations. [src: pangenome_openness; amr_pangenome_atlas] The tension describes these as within-phylum AMR patterns.

**The unresolved gap between them.** The two results concern different response variables, so they do not establish whether the within-phylum AMR patterns persist after explicit phylogenetic correction. [src: pangenome_openness; amr_pangenome_atlas]

## Possible Reconciliations

- *Response-variable hypothesis*: openness may carry signal for AMR gene content while carrying none for the environment and phylogeny effect sizes tested, in which case both results stand and neither generalizes to the other's response variable.
- *Denominator hypothesis*: the matched species set used for the null may under-represent the lineages in which the AMR openness associations arise, so the null would reflect sampling rather than absence of signal.
- *Confounding hypothesis*: the lineage-dependent AMR associations may themselves be an artifact of shared ancestry, and would shrink or vanish under explicit phylogenetic correction — untested, and therefore a hypothesis only.

## Resolving Work

- Re-fit the openness model on the matched species set with AMR-derived quantities as the response variable, using the same rank-correlation procedure: does openness predict AMR gene content where it fails to predict environment and phylogeny effects?
- Apply PGLS — phylogenetic generalized least squares, regression that discounts similarity due to shared ancestry using a tree — to the within-phylum AMR openness associations: do they survive explicit phylogenetic correction?
- Intersect the AMR species list with the matched species set: are the lineages driving the AMR association present in the set that produced the null?
- Test openness against the environment and phylogeny effect sizes separately within each phylum represented in the matched species set: do within-lineage estimates agree with the null reported for the set?
- Fix the effect-size definitions and significance threshold across both analyses before re-running either, so that "null" and "lineage-dependent" are judged on the same scale.
