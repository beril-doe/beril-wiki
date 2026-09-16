<!-- tension-hash: 07876551f760b60e -->
# Pooled Versus Lineage-Stratified Pangenome–AMR Associations

Four related disagreements about antimicrobial resistance (AMR — genes annotated as conferring resistance to antimicrobials) are recorded on [[concepts/phylogenetic-confounding-of-pangenome-associations]], and this page covers all four. (1) A pooled analysis of pangenome openness (the tendency of a species' gene repertoire to keep growing as more genomes are added) against AMR burden reports a near-zero correlation, while the same data stratified by phylum reports positive associations in most tested lineages. (2) A prophage-density analysis reports an AMR association that holds across every major phylum tested and after a sampling control, while an openness analysis finds openness predicts nothing about environmental or phylogenetic structuring. (3) The openness and AMR analyses differ in *scope* rather than in sign — they model different response variables and neither tests the other's. (4) Environmental and within-species analyses report ecological structuring of resistomes that they cannot generalize, because of coverage, metadata, and annotation limits. What is at stake is whether "openness predicts resistance" and "ecology shapes the resistome" are findings or are artifacts of which taxa and which samples happen to be in the underlying data. No figures are used here beyond those in the recorded tension text.

## Evidence Sides

### Disagreement 1 — Pooled near-zero versus within-phylum positive

**Side A: the aggregate signal is near zero.** The overall openness–AMR correlation was near zero (rho=0.006). [src: amr_pangenome_atlas]

**Side B: the stratified signal is positive in most tested lineages.** Openness positively correlated with AMR count in 8/10 tested phyla, including Bacillota and Bacillota_C. [src: amr_pangenome_atlas]

The report attributes the discrepancy to phylogenetic dominance of the aggregate signal rather than resolving it as a causal effect. [src: amr_pangenome_atlas] Both sides come from the same project, so this is an internal tension between two analyses of one dataset, not a disagreement between groups.

### Disagreement 2 — Does prophage density escape phylogeny where openness explains nothing?

**Side A: the prophage–AMR association holds across phyla and a sampling control.** Prophage marker density (a per-species count of phage-derived marker genes taken as evidence of integrated prophage) remained associated with AMR repertoire breadth across all five reported major phyla and after controlling for genome count. [src: prophage_amr_comobilization]

**Side B: openness predicts neither environment nor phylogeny effects.** The openness analysis found that openness did not predict the magnitude of environment or phylogeny effects. [src: pangenome_openness] This is a null for one summary metric, openness, and does not speak to other genomic predictors.

These results concern different predictors and different response variables, so they do not establish whether prophage density is independent of shared ancestry or whether the association reflects open-pangenome lineages acquiring multiple mobile elements. [src: prophage_amr_comobilization]

### Disagreement 3 — A scope gap, not a sign reversal

**Side A: openness relates to AMR in a lineage-dependent way.** The AMR analysis shows lineage-dependent openness associations. [src: amr_pangenome_atlas]

**Side B: openness predicts nothing about what drives gene content.** In the matched species set, openness did not predict either environment or phylogeny effect sizes. [src: pangenome_openness]

The two results concern different response variables, so they do not establish whether the within-phylum AMR patterns persist after explicit phylogenetic correction — that is, after a model that discounts similarity attributable to shared ancestry. [src: pangenome_openness; amr_pangenome_atlas] The recorded tension therefore treats the openness-effects result as a scope tension that qualifies the AMR result rather than contradicting it. [src: pangenome_openness; amr_pangenome_atlas]

### Disagreement 4 — Ecological structuring that cannot be generalized

**Side A: ecology structures the resistome where it can be tested.** Significant effects within five of six phyla and 20 of 141 families support an ecological association. [src: amr_environmental_resistome] At finer resolution, case-study AMR ecotypes (within-species clusters of strains with similar AMR gene presence/absence profiles) showed visible environmental structuring. [src: amr_strain_variation]

**Side B: the generalization is not supported by the data at hand.** The majority of families were not testable or significant because of limited environmental breadth. [src: amr_environmental_resistome] Species-level classifications, sampling imbalance, and AMRFinderPlus-focused annotation (a single resistance-gene annotation tool) leave unresolved how much of the clinical contrast reflects lineage, representation, or unrecognized environmental resistance. [src: amr_environmental_resistome] In the within-species analysis, the visible structuring was not matched by a general statistical demonstration because metadata and within-species environmental diversity were insufficient. [src: amr_strain_variation]

## Possible Reconciliations

These are hypotheses, not findings; none is established by the evidence above.

- **Simpson-type cancellation (Disagreement 1).** Hypothesis: within-phylum slopes are positive but sit on different baselines, so pooling across phyla yields rho=0.006 while the 8/10 stratified result records the within-lineage relationship. [src: amr_pangenome_atlas] Under this hypothesis both numbers are correct and the pooled one is the wrong estimand.
- **Different predictors, different failure modes (Disagreement 2).** Hypothesis: prophage density indexes a countable mobilization mechanism, whereas openness is a derived summary statistic whose species-to-species noise could swamp any relation to effect sizes — so both results can hold without either predictor validating the other. [src: prophage_amr_comobilization; pangenome_openness]
- **Shared-ancestry alternative (Disagreement 2).** Competing hypothesis: open-pangenome lineages acquire multiple mobile elements, so prophage density and AMR breadth are both downstream of the same lineage propensity, and the pan-phylum consistency reflects that shared cause rather than independence from ancestry. [src: prophage_amr_comobilization]
- **Non-overlapping estimands (Disagreement 3).** Hypothesis: "openness relates to AMR count within phyla" and "openness predicts the environment/phylogeny effect size" are questions about different response variables, and the corpus currently contains no analysis that would force them to agree. [src: pangenome_openness; amr_pangenome_atlas]
- **Ascertainment rather than ecology (Disagreement 4).** Hypothesis: the clinical contrast is partly an artifact of which taxa are represented and which determinants the annotation catalogue can see, so the five-of-six-phyla and 20-of-141-family results hold within the tested subset but do not extrapolate to families that could not be tested. [src: amr_environmental_resistome]
- **Power, not absence (Disagreement 4).** Hypothesis: the within-species ecotype structuring is genuine but undetectable at corpus scale because metadata and within-species environmental diversity are insufficient, making the missing general demonstration a sampling result rather than a negative biological result. [src: amr_strain_variation]

## Resolving Work

**Disagreement 1 — pooled versus stratified openness–AMR**
- Refit the openness–AMR relationship as a mixed-effects or hierarchical model with phylum as a random effect over the same pangenome species set, reporting the pooled slope alongside per-phylum slopes: does a lineage-aware pooled estimate depart from rho=0.006? [src: amr_pangenome_atlas]
- Run the stratification at additional ranks (class, order, family) to test whether the 8/10-phyla pattern is specific to phylum-level grouping or persists at every level of the hierarchy. [src: amr_pangenome_atlas]
- Report the two phyla that did not show a positive association separately, with their sample sizes, to distinguish genuine sign heterogeneity from low power. [src: amr_pangenome_atlas]
- Apply a phylogenetic comparative model (e.g. phylogenetic generalized least squares, PGLS — regression that discounts covariance expected from the tree) to openness and AMR count, and ask whether any association survives. [src: amr_pangenome_atlas; pangenome_openness]

**Disagreement 2 — prophage density versus openness as predictors**
- Fit prophage density and openness as joint predictors of AMR repertoire breadth in one model on the species shared by both analyses, reporting each predictor's partial contribution. [src: prophage_amr_comobilization; pangenome_openness]
- Repeat the prophage-density–AMR-breadth test under explicit phylogenetic correction rather than per-phylum stratification plus genome-count control, to test whether pan-phylum consistency implies independence from ancestry. [src: prophage_amr_comobilization]
- Test the "open lineages collect mobile elements" hypothesis directly: within each phylum, ask whether prophage density and openness are correlated, and whether the prophage–AMR association attenuates when openness is held fixed. [src: prophage_amr_comobilization; pangenome_openness]
- Stratify the prophage result by the five reported major phyla *and* by clade within them, to see whether the association is carried by a few dense subclades. [src: prophage_amr_comobilization]

**Disagreement 3 — scope gap between response variables**
- Run the openness-effects analysis with AMR count as an additional response variable on the matched species set, closing the gap between the two estimands directly. [src: pangenome_openness; amr_pangenome_atlas]
- Compute environment and phylogeny effect sizes for the species used in the within-phylum AMR analysis, and test whether phyla with positive openness–AMR associations (such as Bacillota and Bacillota_C) are also the phyla with large environment effects. [src: amr_pangenome_atlas; pangenome_openness]
- Report the overlap between the matched species set and the AMR-tested species set; a small overlap would make the two results non-comparable rather than discordant. [src: pangenome_openness; amr_pangenome_atlas]

**Disagreement 4 — ecological structuring versus untestable coverage**
- Re-annotate a stratified sample of environmental genomes with a resistance catalogue broader than AMRFinderPlus and re-run the environment comparison, to test how much of the clinical contrast is annotation-driven. [src: amr_environmental_resistome]
- Build an explicit power budget in two parts: for families excluded from the 141 tested, record why they could not be tested (insufficient environmental breadth, too few genomes); for the tested-but-non-significant remainder of the 141, record the power available at their sample sizes. [src: amr_environmental_resistome]
- Subsample clinical and environmental genomes to matched counts per family to test whether the five-of-six-phyla effect survives correction for sampling imbalance. [src: amr_environmental_resistome]
- Target metadata curation or new isolate sequencing at the case-study species whose AMR ecotypes showed visible environmental structuring, so the within-species test has the environmental diversity it currently lacks. [src: amr_strain_variation]
- Re-run the within-species analysis restricted to species that pass an explicit metadata-completeness threshold, reporting how many species qualify — a demonstration on a defensible subset is more informative than a null on an underpowered whole. [src: amr_strain_variation]
