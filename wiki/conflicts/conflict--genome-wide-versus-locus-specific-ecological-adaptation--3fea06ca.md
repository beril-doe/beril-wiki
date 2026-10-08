<!-- tension-hash: 3fea06ca438a69c6 -->
# Weak Genome-Wide Environmental Signal: Locus-Specific Adaptation or Measurement Limits?

This page records a disagreement within [[concepts/genome-wide-versus-locus-specific-ecological-adaptation]] over what a weak genome-wide environmental signal in bacterial gene content means. One reading treats it as biological. Ecological adaptation would then sit in particular genes or functions rather than across the whole genome. The other reading attributes it to measurement limits: incomplete coverage, imprecise metadata, or environmental embeddings (numeric vector representations of environmental data) that miss relevant variation. [src: ecotype_analysis] The answer decides whether a weak result should send the corpus toward locus-level analyses or toward better environmental characterisation first.

## Evidence Sides

**Side A: the weak signal reflects locus-specific adaptation**

- The ecotype functional differentiation study found functional differentiation between gene-content ecotypes (within-species subpopulations defined by shared accessory genes). [src: ecotype_functional_differentiation]
- That study did not assign ecotypes to environments and did not apply phylogenetic control (adjustment for shared ancestry among genomes). [src: ecotype_functional_differentiation]
- On that basis, it **supports** the locus-specific hypothesis while leaving the ecological interpretation unresolved. [src: ecotype_functional_differentiation]
- This side is a hypothesis, not an established finding: the functional differences are not tied to any environment, and shared ancestry has not been ruled out as their cause. [src: ecotype_functional_differentiation]

**Side B: the weak signal may be a measurement limit**

- The absence of a strong genome-wide environmental signal *may* indicate locus-specific adaptation. [src: ecotype_analysis]
- It may also result from other sources:
  - Incomplete AlphaEarth coverage. [src: ecotype_analysis]
  - Imprecise metadata. [src: ecotype_analysis]
  - Environmental embeddings that do not capture biologically relevant variation. [src: ecotype_analysis]

## Possible Reconciliations

- **Hypothesis 1:** Both sides are partly right. Environment acts on a small set of loci, and those effects are diluted in genome-wide similarity measures. Coarse embeddings would weaken detection further.
- **Hypothesis 2:** The functional differentiation between ecotypes reflects shared ancestry or other non-environmental causes. In that case it would not support locus-specific ecological adaptation.
- **Hypothesis 3:** Locus-specific adaptation may be detectable only in species whose environmental metadata are reliable, so detection would differ by species even if the underlying biology does not.

## Resolving Work

- **Linking ecotypes to environments.** Using the ecotype assignments from the functional differentiation study, test whether ecotype membership associates with AlphaEarth embeddings or curated isolation metadata. The question is whether the functionally distinct ecotypes are also environmentally distinct.
- **Adding phylogenetic control.** Re-test the functional categories that separate ecotypes with a phylogeny-aware comparison, such as PGLS (phylogenetic generalised least squares, a regression that accounts for shared ancestry). The question is whether functional differentiation survives once ancestry is controlled.
- **Testing measurement limits.** Restrict the genome-wide environment–gene-content analysis to genomes with complete AlphaEarth coverage and high-precision metadata. The question is whether the environmental signal strengthens when measurement noise is reduced.
- **Running a locus-level scan.** For the species studied in the ecotype correlation analysis, test environment associations gene by gene or pathway by pathway, controlling for phylogeny. The question is whether specific loci carry environmental signal that the genome-wide measure misses.
- **Benchmarking the embeddings.** Compare AlphaEarth embeddings against direct environmental variables, such as habitat categories, for the same samples. The question is whether the embeddings capture the variation that matters biologically.
