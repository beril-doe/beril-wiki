<!-- tension-hash: 3e64aa342e7232f6 -->
# Distributed Metal-Type Signal or Near-Threshold Result: Reading Metal Diversity and Niche Breadth

This page records a disagreement about how metal-related gene content relates to ecological niche breadth, which is the range of habitats a taxon occupies. In the MicrobeAtlas genus-level analysis, leave-one-out models (refits that drop one metal at a time) lose significance. That loss could mean a distributed signal, or a near-threshold result weakened by lost power. [src: microbeatlas_metal_ecology] The MAG analysis (MAG means metagenome-assembled genome) finds every metal-specific set significant. [src: comprehensive_metal_ecology] The question matters because it decides whether metal-diversity effects should be attributed to one metal or to metal types as a group. The concept page is [[concepts/single-metal-dominance-versus-distributed-metal-type-diversity-effects]].

## Evidence Sides

**Side A: leave-one-out loss of significance in MicrobeAtlas**

- Leave-one-out models lose significance. [src: microbeatlas_metal_ecology]
- One reading is that this reflects a distributed signal. [src: microbeatlas_metal_ecology]
- The other reading is that it is a near-threshold result weakened by lost power. [src: microbeatlas_metal_ecology]
- No MicrobeAtlas leave-one-out model is significant. [src: microbeatlas_metal_ecology]

**Side B: metal-specific significance in the MAG analysis**

- The MAG analysis finds every metal-specific set significant. [src: comprehensive_metal_ecology]

**Relation between the sides**

- These tests ask different questions, so the contrast is not a conflict in the same measure. [src: microbeatlas_metal_ecology]

## Possible Reconciliations

- **Hypothesis 1: the effect is distributed across metal types.** Under this hypothesis, no single metal carries the association. Dropping any one metal would weaken it, while every metal-specific set could still be significant on its own in the MAG data. This is untested.
- **Hypothesis 2: the MicrobeAtlas result sits near the significance threshold.** Under this hypothesis, each leave-one-out model loses power and so loses significance. The metal-specific MAG results would then show the same underlying association in a better-powered setting. This is untested.
- **Hypothesis 3: the two analyses measure different things.** If so, both results can hold together, because the tests ask different questions. [src: microbeatlas_metal_ecology]

## Resolving Work

- **Data:** MicrobeAtlas genus-level data with the full set of leave-one-out fits. **Method:** a power analysis that simulates the loss of data from each exclusion. **Question:** is the loss of significance explained by lost power?
- **Data:** the same genera in both datasets. **Method:** fit one shared model form to MicrobeAtlas and MAG inputs. **Question:** do the two datasets still differ when the test is the same?
- **Data:** MAG metal-specific sets. **Method:** run leave-one-out exclusions on the MAG data, mirroring the MicrobeAtlas design. **Question:** does significance survive each exclusion there?
- **Data:** per-metal effect estimates from both analyses. **Method:** compare the direction and size of the estimates, not only significance. **Question:** is the pattern consistent with a distributed signal?
