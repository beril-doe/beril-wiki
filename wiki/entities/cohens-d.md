---
type: "Method"
description: "Cohen's d, the standardized mean-difference effect size, and how BERIL projects used and qualified it in genome-completeness and functional-atlas comparisons."
sources: ["summaries/clay_confined_subsurface__REPORT.md", "summaries/gene_function_ecological_agora__REPORT.md"]
---
Cohen's d is a standardized mean-difference effect size. Corpus projects use it alongside p-values and bootstrap confidence intervals to judge whether group differences are large enough to matter. In this corpus it appears in [[summaries/clay_confined_subsurface__REPORT]] for GapMind pathway-completeness comparisons and in [[summaries/gene_function_ecological_agora__REPORT]] for KO-level class-control and phylogenetic-rank comparisons [src: clay_confined_subsurface, gene_function_ecological_agora].

## Use in clay-confined subsurface genomes

Without quality filtering, deep-clay anchors showed no greater [[entities/gapmind]] pathway completeness than baseline: mean 16.22 for 9 deep anchors versus 16.66 for 150 baseline genomes, Cohen's d=−0.17, p=0.153. This is a null result, not evidence of greater deep-clay completeness [src: clay_confined_subsurface].

Shallow anchors without filtering had higher GapMind pathway completeness than baseline: 17.87 versus 16.66 across 30 and 150 genomes, d=+0.52, p=0.006 [src: clay_confined_subsurface].

After [[entities/checkm]] quality filtering (CheckM≥80), 6 deep anchors had lower mean pathway completeness than 137 baseline genomes: 15.50 versus 17.14, d=−0.84, p=0.009. The unfiltered and filtered deep-anchor effects are both negative. Filtering changed the reported significance, not the direction [src: clay_confined_subsurface].

Under the same CheckM≥80 filter, 30 shallow anchors still had higher mean pathway completeness than 137 baseline genomes: 17.87 versus 17.14, d=+0.43, p=0.029 [src: clay_confined_subsurface].

Within [[entities/bacillota-b]], GapMind means were 16.50 for 4 deep anchors and 16.79 for 19 baseline genomes. With d=−0.13 and p=0.073, the comparison did not establish a difference [src: clay_confined_subsurface].

Caveat: the deep cohort of n=9 genomes is power-limited. The report states that only large effect sizes (Cohen's d > 0.7) are reliably detectable in unfiltered comparisons. It says p-values for marginal effects, such as the within-Bacillota_B p=0.07, should be treated as descriptive [src: clay_confined_subsurface].

## Use in the gene-function ecological agora

The M18 amplification gate passed on the cleanest housekeeping controls (tRNA-synthetase and RNAP core). Cohen's d rose from 0.146 at the UniRef50 baseline (NB08c, positives versus all housekeeping) to 0.665–3.558 at KO resolution (NB09c, best pairs). The report describes this as a 4–25× amplification, depending on positive class, and states that the substrate-hierarchy claim survives at KO resolution [src: gene_function_ecological_agora].

The M18 pass verdict from NB09c, which used a 2.69M-row panel subset, was reproduced at full atlas scale. All 6/6 strict pairs met Cohen's d ≥ 0.3 with a 95% bootstrap confidence-interval lower bound > 0. What reproduced is the pass verdict, not necessarily the panel effect sizes [src: gene_function_ecological_agora].

| Comparison | n_pos | n_neg | Cohen's d | 95% CI | Pass | Source |
|---|---|---|---|---|---|---|
| pos_crispr_cas vs neg_trna_synth_strict | 6 | 21 | 2.504 | [1.31, 16.16] | ✓ | [src: gene_function_ecological_agora] |
| pos_crispr_cas vs neg_rnap_core_strict | 6 | 3 | 1.905 | [1.55, 11.58] | ✓ | [src: gene_function_ecological_agora] |
| pos_betalac vs neg_trna_synth_strict | 110 | 21 | 0.792 | [0.68, 0.90] | ✓ | [src: gene_function_ecological_agora] |
| pos_betalac vs neg_rnap_core_strict | 110 | 3 | 0.753 | [0.66, 0.86] | ✓ | [src: gene_function_ecological_agora] |
| pos_tcs_hk vs neg_trna_synth_strict | 310 | 21 | 0.647 | [0.54, 0.80] | ✓ | [src: gene_function_ecological_agora] |
| pos_tcs_hk vs neg_rnap_core_strict | 310 | 3 | 0.665 | [0.58, 0.82] | ✓ | [src: gene_function_ecological_agora] |

The full-atlas table above lists the six strict class-control comparisons: [[entities/crispr-cas]], [[entities/beta-lactamases]] and [[entities/two-component-system-histidine-kinases]] positives, each tested against strict housekeeping negatives. Cohen's d ranges from 0.647 to 2.504. Some groups are small. The CRISPR-Cas positive class has n_pos = 6, and the RNAP-core strict negative class has n_neg = 3, while the tRNA-synthetase strict negatives have n_neg = 21. The report does not say what drives the wide confidence intervals on the CRISPR-Cas pairs [src: gene_function_ecological_agora].

Tension in effect-size reporting: the report says the full-atlas d values "match the NB09c panel-only test almost exactly" and attributes small drift to sample composition. However, its NB09c best d = 3.558 (n_pos = 6, n_neg = 20) differs substantially from the full-atlas CRISPR-Cas versus tRNA-synthetase d = 2.504 (n_pos = 6, n_neg = 21). The pass verdict replicated; the near-exact effect-size agreement claim is in tension with the reported values [src: gene_function_ecological_agora].

The project's summary has the same tension. It reports 6/9 strict panel pairs passing at d ≥ 0.3 with best d = 3.56, and 6/6 full-atlas pairs passing with best d = 2.50. It then asserts that the two runs match within Cohen's d ≤ 0.04 across all comparable pairs. That assertion conflicts with the reported best values, so the pass verdict and the effect-size agreement should be treated as distinct claims [src: gene_function_ecological_agora].

In responding to review, the project accepted that the UniRef50 baseline d=0.146 is small. It argued that the KO-level effects should not be conflated with that baseline. Under Cohen 1988 conventions (d=0.2 small, 0.5 medium, 0.8 large), it classed the Phase 2 KO d values of 0.665 (medium-large), 0.753, 0.792, 1.905, 2.504 and 3.558 (very large) as not below biological significance [src: gene_function_ecological_agora].

The project also accepted a reviewer point that effect-size reporting was inconsistent across phases. Plan v2.10 M24 standardizes Cohen's d plus 95% bootstrap CI as the canonical format for all primary statistical comparisons going forward [src: gene_function_ecological_agora].

Null result at genus rank: 137 pooled Cyanobacteria genera and 2,350 KOs gave producer d=+0.08 and consumer d=−0.53, with both [[entities/mann-whitney-u-test]] p values at 1.00; the verdict was STABLE [src: gene_function_ecological_agora].

On small-sample effect-size inflation, the report acknowledges that Cohen's d has higher variance at small N. It argues that a stable d=1.50 with a bootstrap CI whose lower bound is positive, at α=2×10⁻⁵, is a real effect detected at small N rather than "inflation by chance". It also notes that the smaller-N, larger-d pattern partly reflects small-N tests needing larger d to clear significance. This is the project's own argument, not an independent check [src: gene_function_ecological_agora].

Under D2 annotation-density residualization, all hypothesis verdicts kept their direction and significance. These include NB11 H1 REFRAMED (consumer-side d −0.21), NB12 H1 SUPPORTED ([[entities/mycobacteriaceae]] × [[entities/mycolic-acid]] Innovator-Isolated) and NB16 H1 SUPPORTED at class rank (Cyanobacteria × [[entities/photosystem-ii]] Innovator-Exchange). The largest attenuation was NB12 family-rank consumer-side, d −0.19 → −0.16 (~16% relative attenuation, still significant) [src: gene_function_ecological_agora].

## Related

See [[concepts/null-results-under-limited-statistical-resolution]] for how small cohorts limit what effect sizes can show, and [[entities/gapmind]] and [[entities/checkm]] for the inputs to the clay-subsurface comparisons.
