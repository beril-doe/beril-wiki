<!-- tension-hash: b4822dc29b20b644 -->
# Tension: do laboratory, atlas, and clustering signals reappear as field-scale ecological structure?

Five projects in [[concepts/environment-embedding-geography]] each pair a pattern detected at one scale — a functional clustering, a global genome atlas, a laboratory tolerance assay, an experimental treatment — with a field-scale community observation, and each pair fails to settle whether the first predicts the second. The disagreement is about the inferential step they share: whether cross-scale correspondence is ecological signal or an artifact of how the field side was measured and powered. It matters because that step underwrites most environment-embedding claims in this corpus; the sharpest instance is a design where treatment alone explained 7.6% (p=0.069) while treatment × horizon explained 41%. [src: gene_function_ecological_agora; genotype_to_phenotype_enigma; harvard_forest_warming; lab_field_ecology; lanthanide_methylotrophy_atlas]

## Evidence Sides

**Signal is present at the scale where it was measured.** Functional cluster alignment is reported, but the tension records it explicitly as *not causal* — correspondence without a demonstrated mechanism. In the warming experiment, the interaction term treatment × horizon explained 41% of variation, a substantial structured effect, in contrast to treatment alone at 7.6% (p=0.069). Global atlas-scale representation of *Pseudomonas* is likewise a real, measured pattern, even though it differs from the ENIGMA (Oak Ridge contaminated-subsurface consortium) environmental clade. On this reading the cross-scale pattern exists and the field comparison is the weaker instrument. [src: gene_function_ecological_agora; genotype_to_phenotype_enigma; harvard_forest_warming; lab_field_ecology; lanthanide_methylotrophy_atlas]

**The field test is where the claim fails.** Every field-side result in the set is null, underpowered, or mismatched. Laboratory metal tolerance was non-significant in field abundance. Rare-earth-element (REE)-impacted samples did not pass FDR — false discovery rate, the multiple-testing correction that controls the expected proportion of false positives among calls — while the REE-affected acid mine drainage set contained only 37 MAGs (metagenome-assembled genomes, draft genomes binned from metagenome assemblies). Treatment alone sat at 7.6% with p=0.069, above a conventional significance threshold, so the strong 41% figure belongs to the interaction, not to treatment. Global *Pseudomonas* representation differs from ENIGMA's environmental clade, so the atlas organisms are not the field organisms. [src: gene_function_ecological_agora; genotype_to_phenotype_enigma; harvard_forest_warming; lab_field_ecology; lanthanide_methylotrophy_atlas]

## Possible Reconciliations

- *Hypothesis:* the field nulls are power-limited rather than true nulls — 37 MAGs and an FDR-corrected test may lack the denominator to detect an effect that exists.
- *Hypothesis:* correspondence is real but conditional, appearing only in interaction terms (treatment × horizon, 41%) and vanishing when a single factor is tested alone (7.6%, p=0.069).
- *Hypothesis:* the two sides address different populations — global atlas taxa versus a site-specific environmental clade — so no amount of added power would make them agree.
- *Hypothesis:* clustering alignment is a shared-ancestry artifact, which would explain correspondence without causality.

## Resolving Work

- Expand the REE-affected acid mine drainage set well beyond 37 MAGs and re-run the same FDR-corrected enrichment test: does the null survive a larger denominator?
- Re-run the warming design with horizons sampled to equal depth and pre-registered power, asking whether treatment alone crosses threshold once the interaction is modelled explicitly.
- Match laboratory metal-tolerance strains to field amplicon lineages at strain rather than genus resolution before testing abundance association.
- Restrict the global *Pseudomonas* atlas to the ENIGMA environmental clade and re-test representation against site abundance.
- Test functional cluster alignment against a phylogeny-aware null to separate causal signal from shared ancestry.
