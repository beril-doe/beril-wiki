<!-- tension-hash: 8a1793daa1cb84a7 -->
# Pangenome Openness: Associated With Pathway Variability, Null Against Environment and Phylogeny Effects

This page records a disagreement over what pangenome openness predicts. Pangenome openness is the degree to which a species' gene repertoire keeps expanding across its sequenced genomes. One analysis found that openness rises with the number of variable metabolic pathways [src: pathway_capability_dependency; pangenome_openness]. Broader pangenome analyses found no relationship between openness and the effect sizes of environment or phylogeny on gene content [src: pathway_capability_dependency; pangenome_openness]. The outcome determines whether openness should be read as a marker of ecologically meaningful gene turnover. That reading bears on how condition-specific fitness results connect to genome-content variation in [[concepts/condition-specific-fitness]].

## Evidence Sides

**Side A: openness is positively associated with pathway variability**

Variable pathway count was positively associated with pangenome openness after genome-count control (rho=0.530, p=2.83e-203) [src: pathway_capability_dependency; pangenome_openness]. Here rho is the rank correlation coefficient adjusted for genome count, and p is its p-value: the probability, under a null model of no association, of a correlation at least as extreme as the one observed.

Genome-count control adjusts for how many genomes were sequenced per species, a potential confounder.

This is a correlational measurement; it does not establish that metabolic gain and loss drives openness [src: pathway_capability_dependency; pangenome_openness].

**Side B: openness shows no relationship to environment or phylogeny effects**

Broader pangenome analyses reported null relationships between openness and environment or phylogeny effect sizes [src: pathway_capability_dependency; pangenome_openness]. These are null results. They report no detected relationship, which is not the same as a demonstrated independence.

**Scope of the disagreement**

The corpus states that this evidence refines rather than resolves the conflict, for two reasons [src: pathway_capability_dependency; pangenome_openness]:

- Pathway variability is a narrower predictor [src: pathway_capability_dependency; pangenome_openness].
- The new analysis did not compute full phylogenetic independent contrasts, a method that accounts for the statistical non-independence among species attributable to shared ancestry [src: pathway_capability_dependency; pangenome_openness].

## Possible Reconciliations

- **Hypothesis 1: different predictors.** Pathway variability may capture a specific functional slice of accessory-gene turnover (accessory genes are those whose presence varies among a species' genomes). Aggregate environment and phylogeny effect sizes may average over many gene classes and dilute that slice. Both results could hold at once.
- **Hypothesis 2: phylogenetic confounding.** The positive association may partly reflect shared ancestry among species. Full phylogenetic independent contrasts would test this. If the association collapses under them, the two sides would align on a null.
- **Hypothesis 3: openness reflects opportunistic gene flux.** Openness may track pathway turnover without tracking environmental structure. In that case "variable pathways" and "environment effect" measure different processes rather than conflicting ones.

## Resolving Work

- **Phylogenetic correction:** Rerun the pathway-variability vs. openness correlation using full phylogenetic independent contrasts on a species tree from the corpus. This asks whether the positive association survives removal of shared ancestry.
- **Matched species sets:** Restrict both analyses to the same species with genome-count control applied identically. Then test whether the environment and phylogeny nulls persist where the pathway association is detected.
- **Pathway-class partitioning:** Split variable pathways by functional class, such as amino acid biosynthesis vs. others. Correlate each class with environment effect sizes to see whether the narrower predictor carries environmental signal that the aggregate measures miss.
- **Linking to fitness data:** Cross-reference variable pathways with Fitness Browser condition-specific fitness scores. This asks whether openness-associated pathways are the ones whose genes show condition-dependent fitness effects.
