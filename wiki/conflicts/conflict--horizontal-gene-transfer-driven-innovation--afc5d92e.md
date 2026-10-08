<!-- tension-hash: afc5d92e6457bc08 -->
# Do Strict Housekeeping Classes Show a ~1× or a 2.3× Recent-to-Ancient Acquisition Ratio?

This tension concerns how gene-acquisition events for strict housekeeping gene classes split between recent and ancient depths in the bacterial tree. The central digest reports a ~1× recent-to-ancient ratio for strict housekeeping classes that include tRNA-synth, the aminoacyl-tRNA synthetases (enzymes that attach amino acids to their transfer RNAs, or tRNAs). The project report lists tRNA-synth at 2.3×. [src: discoveries, gene_function_ecological_agora] The disagreement is recorded on [[concepts/horizontal-gene-transfer-driven-innovation]]. Until it is settled, neither figure can be cited as the housekeeping acquisition ratio. The sources do not reconcile the class definitions behind the two figures. [src: discoveries, gene_function_ecological_agora]

## Evidence Sides

**Side A: the digest's ~1× figure for strict housekeeping**

The central digest reports a ~1× recent-to-ancient ratio for strict housekeeping classes, and tRNA-synth is among the classes it includes. [src: discoveries, gene_function_ecological_agora] The assigned passages do not state which classes the digest pooled or how it computed the ratio. Its ~1× figure for strict housekeeping therefore remains unexplained. [src: gene_function_ecological_agora, discoveries]

**Side B: the project's per-class strict depth table**

The project report lists tRNA-synth at 2.3×. [src: discoveries, gene_function_ecological_agora] Its strict-class depth table names neg_trna_synth_strict, at 2.3 (24.7 / 10.7), as its most ancient-skewed class. [src: gene_function_ecological_agora, discoveries] Two other strict housekeeping classes are reported only partly:

- neg_ribosomal_strict (ribosomal proteins) had 6.3% ancient gains. [src: gene_function_ecological_agora, discoveries]
- neg_rnap_core_strict (core RNA polymerase subunits) had 6.0% ancient gains. [src: gene_function_ecological_agora, discoveries]

The assigned passages give no recent-to-ancient ratio for either class. [src: gene_function_ecological_agora, discoveries] The table **refines** the tension: it pins the project's figure to a single named class but does not supply a pooled figure that could be compared with the digest's. [src: gene_function_ecological_agora, discoveries]

## Possible Reconciliations

- **Hypothesis 1: different class definitions.** The digest's "strict housekeeping" grouping may pool several classes, or define them differently, while the project's 2.3× refers to neg_trna_synth_strict alone. The sources do not reconcile the class definitions behind the two figures, so this remains untested.
- **Hypothesis 2: a different depth binning or normalisation.** The two figures may use different boundaries for "recent" and "ancient," or a different denominator. Either could move a ratio substantially without any change in the underlying gain events.
- **Hypothesis 3: a transcription or summarisation discrepancy.** The digest may approximate or misstate the project's result. This cannot be assessed until the digest's derivation is traced.

None of these is established. The page does not prefer either figure.

## Resolving Work

- **Trace the digest's grouping.** Use the digest's source tables to ask which strict classes and which gain events produce its ~1× figure, and whether tRNA-synth enters it as neg_trna_synth_strict.
- **Recompute pooled ratios.** Apply the project's per-class depth table to neg_ribosomal_strict and neg_rnap_core_strict, using the project's own recent and ancient bins. Then test whether pooling all three strict classes yields a ratio near the digest's figure.
- **Audit depth-bin definitions.** Compare the recent and ancient depth cutoffs used by the digest and by the project report to ask whether a binning difference alone could separate a ~1× result from a 2.3× result.
- **Check sensitivity to strictness.** Rerun the recent-to-ancient calculation for strict and non-strict versions of each housekeeping class to ask whether the ratio depends on how tightly the class membership is filtered.
