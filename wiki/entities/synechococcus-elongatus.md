---
type: "Organism"
description: "Synechococcus elongatus (SynE) is a cyanobacterium in the BERIL fitness corpus that is notably sensitive to metals and is the outlier in NaCl dose-response experiments that inflates shared-stress overlap statistics."
sources: ["summaries/counter_ion_effects__REPORT.md", "summaries/discoveries.md", "summaries/metal_fitness_atlas__REPORT.md", "summaries/pitfalls.md"]
---
# Synechococcus elongatus

**Synechococcus elongatus** is a cyanobacterium (see [[entities/cyanobacteriia]]) analysed in the corpus's gene-fitness projects [src: metal_fitness_atlas]. Reports refer to it by the alias **SynE** [src: pitfalls, counter_ion_effects, discoveries].

## Metal sensitivity

In the [[entities/metal-fitness-atlas]], 3.3% of all gene × metal records (12,838 / 383,349) show significant fitness defects (fit < -1, |t| > 4). Within that atlas, SynE is described as notably metal-sensitive, with 33.6% of genes important across just 2 metals. By comparison, [[entities/desulfovibrio-vulgaris-hildenborough]] (DvH) has 1,366 metal-important genes (49.8% of its genome across 13 metals). The SynE figure covers only 2 metals, compared with 13 for DvH. It should therefore be read as a result for one organism with narrow metal coverage [src: metal_fitness_atlas].

## NaCl dose-response outlier

SynE has 12 [[entities/sodium-chloride]] (NaCl) dose-response experiments spanning 0.5–250 mM, far more than any other organism (1–6 NaCl experiments). It is a dramatic outlier in the metal–NaCl comparison, at 88.6% shared-stress (565/638 genes) [src: counter_ion_effects, discoveries, pitfalls].

This outlier status is a recorded pitfall. Using `n_sick >= 1` (at least one NaCl experiment with fit < -1) as an NaCl-importance threshold is biased by the number of NaCl experiments per organism, and the threshold is much easier to satisfy with 12 experiments. Under it, SynE flags 32.6% of genes as NaCl-important, 3× higher than the next organism, which inflates cross-condition overlap statistics [src: pitfalls, counter_ion_effects, discoveries].

Sensitivity check: excluding SynE, overall metal–NaCl overlap drops from 39.8% to 36.7% (3,739/10,183). The project describes this as a modest drop that confirms the pooled finding is not driven by this outlier [src: counter_ion_effects, discoveries, pitfalls]. The next-highest organisms (Korea 58.6%, Phaeo 56.4%, Pedo557 53.0%) have typical NaCl experiment counts [src: counter_ion_effects]. When comparing conditions with unequal experiment counts, the recommended mitigation is either to require `n_sick >= 2` or use `mean_fit < threshold` instead of `n_sick >= 1`, or to report results with and without outlier organisms. This feeds [[concepts/shared-stress-versus-stressor-specific-fitness]] [src: pitfalls].

## Sources

- [[summaries/counter_ion_effects__REPORT]]
- [[summaries/metal_fitness_atlas__REPORT]]
- [[summaries/discoveries]]
- [[summaries/pitfalls]]
