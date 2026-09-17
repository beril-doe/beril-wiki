<!-- tension-hash: 3fea06ca438a69c6 -->
# Locus-Specific Adaptation or Measurement Artifact? Reading a Weak Genome-Wide Environmental Signal

Across the corpus, genome-wide gene-content similarity tracks phylogeny more consistently than it tracks environment. Two incompatible readings of that weak environmental signal circulate and neither has been retired. One treats it as a biological result: ecological adaptation is real but concentrated at particular loci, so it does not show up when gene content is averaged genome-wide. The other treats it as a measurement result: the signal is weak because the environmental side of the comparison is poorly resolved — incomplete coverage in the AlphaEarth environmental embeddings (the environmental descriptors that supply the environment term in these comparisons), imprecise metadata, or embeddings that do not capture biologically relevant variation. The distinction matters because the two readings point analysis in opposite directions: one says look harder at individual genes, the other says fix the environmental variables first. This page records the disagreement carried on [[concepts/genome-wide-versus-locus-specific-ecological-adaptation]].

## Evidence Sides

**Adaptation is locus-specific.** The absence of a strong genome-wide environmental signal may indicate that ecological adaptation is locus-specific [src: ecotype_analysis]. Supporting this direction, the ecotype study adds functional differentiation without environmental assignment or phylogenetic control, so it **supports** the locus-specific hypothesis while leaving the ecological interpretation unresolved [src: ecotype_functional_differentiation]. This side is therefore backed by one line of within-species functional evidence that is explicitly uncontrolled for ancestry and unlinked to environment; it remains a hypothesis, not a demonstrated finding.

**The signal is limited by measurement.** The same absence may also result from incomplete AlphaEarth coverage, imprecise metadata, or environmental embeddings that do not capture biologically relevant variation [src: ecotype_analysis]. On this reading the genome-wide test is underpowered rather than informative, and a null environmental result is a null result about the available environmental variables — not about ecology.

## Possible Reconciliations

- *Hypothesis:* both are partly true — adaptation is concentrated at a minority of loci **and** the environmental variables are too coarse to detect even that concentrated signal, so the genome-wide null is jointly produced.
- *Hypothesis:* the ecotype functional differentiation reflects ancestry or population structure rather than environment, in which case the locus-specific reading loses its main support without the measurement critique being needed.
- *Hypothesis:* the two readings are not currently separable — because the ecotype study supplies functional differentiation without environmental assignment or phylogenetic control [src: ecotype_functional_differentiation], the same observation stays compatible with either reading, making the disagreement presently untestable rather than merely unresolved.

## Resolving Work

- Restrict the genome-wide test to genomes with complete AlphaEarth embedding coverage and high-confidence coordinates, re-running the same phylogeny-versus-environment comparison: does the direction change when the measurement critique is removed by construction?
- Run a per-gene association scan against environmental embeddings under PGLS (phylogenetic generalised least squares, regression that discounts similarity due to shared ancestry): do individual loci show environmental association where the genome-wide average does not?
- Assign environmental coordinates to the ecotype-clustered genomes and test ecotype membership by db-RDA (distance-based redundancy analysis, which partitions genomic distance among explanatory variables): are gene-content ecotypes environmentally structured, or only functionally distinct?
- Validate the embeddings themselves against curated isolation-source metadata: do the embeddings separate habitats that annotation says are distinct?
- Simulate genomes with known locus-specific adaptation and pass them through the genome-wide pipeline: what effect size would this test have detected, and was it powered at all?
