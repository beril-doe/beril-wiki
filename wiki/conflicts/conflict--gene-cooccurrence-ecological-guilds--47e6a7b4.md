<!-- tension-hash: 47e6a7b460cf1b72 -->
# Does co-occurrence mark a guild of shared selection or of complementary provisioning?

This page records a disagreement within [[concepts/gene-cooccurrence-ecological-guilds]]. One project reads the pairing of plant growth-promoting (PGP) genes pqqC and acdS as an ecological guild [src: pgp_pangenome_ecology]. Another finds that plant-associated genera that co-occur are slightly *less* complementary than random pairs [src: plant_microbiome_ecotypes]. The two findings are not mutually exclusive. They differ in what "guild" is taken to mean: shared environmental selection, or complementary metabolic provisioning. That choice decides how co-occurrence evidence across the corpus should be read.

## Evidence Sides

**Side A: co-occurrence supports a pqqC–acdS guild.**
The PGP analysis supports reading pqqC and acdS as an ecological guild. Two lines of evidence back this: a strong pairwise association between the genes across genomes, and their enrichment in particular environments [src: pgp_pangenome_ecology]. This is a gene-level association measured across genomes. It does not show that the genes are physically linked, and it does not show that they act together metabolically [src: pgp_pangenome_ecology].

**Side B: co-occurring genera are slightly less complementary than random pairs.**
The plant-microbiome complementarity analysis compared co-occurring genus pairs with random genus pairs. Co-occurring pairs were slightly less complementary, with Cohen's d ≈ −0.4 and permutation p < 0.001 [src: plant_microbiome_ecotypes]. Cohen's d is a standardized difference in means. A permutation p-value is the probability of a result at least this extreme under a null distribution built by permutation. The negative direction is read as consistent with functional redundancy rather than complementarity, at a small effect size [src: plant_microbiome_ecotypes].

## Possible Reconciliations

- **Hypothesis 1: guilds reflect shared selection, not provisioning.** On this reading, pqqC–acdS co-occurrence reflects a common environmental filter acting on similar organisms. That would fit the finding that co-occurring genera are less complementary than random pairs.
- **Hypothesis 2: the two analyses measure different units.** Side A analyses gene pairs across genomes [src: pgp_pangenome_ecology]. Side B analyses genus pairs in communities [src: plant_microbiome_ecotypes]. Co-occurrence of complementary genes within genomes could coexist with redundancy between genera.
- **Hypothesis 3: complementarity is pathway- or activity-specific.** If the complementarity score aggregates many functions, redundancy in the aggregate could hide complementarity in a few specific pathways. Only pathway-level and activity-level tests could show this.

## Resolving Work

- **Genome-level complementarity:** Take the pqqC- and acdS-carrying genomes from pgp_pangenome_ecology. Build pathway-completeness profiles for each and test whether pqqC+acdS carriers are more or less complementary to their co-occurring partners than to random partners. This asks whether the guild is provisioning or selection.
- **Environment-conditioned null:** Repeat the plant_microbiome_ecotypes genus-pair permutation with a null model restricted to the same environment. This asks whether the redundancy signal survives once shared habitat filtering is controlled for.
- **Pathway-resolved complementarity:** Break the complementarity score into individual pathways, starting with phosphate solubilization and ethylene reduction. This asks whether pathways tied to the PGP guild show complementarity while the overall profile shows redundancy.
- **Activity-level evidence:** Where fitness or expression data exist for pqqC or acdS carriers, test whether both genes contribute under the same plant-associated conditions. This asks whether co-occurrence reflects joint function or only co-presence.
- **Physical linkage check:** Measure how often pqqC and acdS sit near each other in the genome versus apart. This asks whether association at the guild level is confounded with linkage at the locus level.
