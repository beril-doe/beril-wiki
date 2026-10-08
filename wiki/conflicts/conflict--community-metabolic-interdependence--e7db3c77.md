<!-- tension-hash: e7db3c77b9e733d1 -->
# Does Community Provisioning Produce a Common Negative Amino-Acid Pattern, or Does Tyrosine Follow a Different Regime?

This page records a disagreement within [[concepts/community-metabolic-interdependence]]. The simple prediction is that community provisioning should produce a common negative association pattern across amino acids, yet tyrosine shows a positive association [src: discoveries]. This matters because the outlier may reflect ecological specialization, measurement or mapping limitations, or a genuinely different exchange regime [src: discoveries], and the community-scale tests may be confounded by unmeasured environmental gradients [src: nmdc_community_metabolic_ecology].

## Evidence Sides

**Side A: Community provisioning predicts a shared negative pattern**

The simple prediction is that community provisioning should produce a common negative association pattern across amino acids [src: discoveries]. Under this view, higher ambient availability of an amino acid should go with lower community biosynthetic capacity for it, consistently across amino acids [src: discoveries].

**Side B: Tyrosine departs from that pattern**

The tyrosine association is positive, which is a direct tension with the simple prediction [src: discoveries]. The corpus does not establish whether this outlier reflects ecological specialization, measurement or mapping limitations, or a genuinely different exchange regime [src: discoveries].

**Refining evidence: The analysis could not exclude confounders**

The NMDC (National Microbiome Data Collaborative) analysis refines this uncertainty in two ways [src: nmdc_community_metabolic_ecology]:

- **Genomic potential only.** It notes that GapMind, a tool that predicts amino-acid biosynthesis pathway completeness from genomes, measures genomic potential rather than expression [src: nmdc_community_metabolic_ecology].
- **Missing abiotic data.** pH, temperature, and total organic carbon were all NaN (missing values) in the 174-sample analysis matrix [src: nmdc_community_metabolic_ecology]. Their absence prevented partial-correlation tests, which estimate an association while holding other variables constant, from controlling for environmental gradients [src: nmdc_community_metabolic_ecology].

The report states that these variables could confound two of its tests [src: nmdc_community_metabolic_ecology]:

- H1, the amino-acid test.
- H2, the ecosystem-differentiation test.

## Possible Reconciliations

- **Hypothesis 1: Ecological specialization or a different exchange regime.** Tyrosine may reflect ecological specialization or a genuinely different exchange regime from other amino acids [src: discoveries].
- **Hypothesis 2: A measurement or mapping artifact.** The tyrosine signal may reflect measurement or mapping limitations [src: discoveries]. GapMind measures genomic potential rather than expression [src: nmdc_community_metabolic_ecology].
- **Hypothesis 3: Environmental confounding.** Unmeasured pH, temperature, and total organic carbon could confound the amino-acid test (H1) [src: nmdc_community_metabolic_ecology].

## Resolving Work

- **Recover abiotic covariates.** Take NMDC samples with pH, temperature, and total organic carbon recorded, and rerun the amino-acid associations as partial correlations. This asks whether the tyrosine sign and the H1 result survive control for environmental gradients.
- **Test potential against expression.** Pair GapMind pathway completeness with metatranscriptomic (community RNA expression) or metaproteomic (community protein abundance) data from the same samples. This asks whether expressed tyrosine biosynthesis shows the same positive association as genomic potential.
- **Audit the tyrosine mapping.** Trace tyrosine metabolite identifiers to compound records and check the tyrosine pathway definitions. This asks whether the positive association is a mapping artifact.
- **Stratify by ecosystem.** Run the analysis within each ecosystem type. This asks whether the tyrosine outlier is consistent across ecosystems or confined to one.
