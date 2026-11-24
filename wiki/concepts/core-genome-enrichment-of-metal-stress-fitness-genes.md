---
type: "Concept"
description: "Whether metal-stress fitness genes, by metal, organism and specificity (general, shared, metal-specific), are preferentially core, including robustness to NaCl shared-stress correction; stops at gene-level conservation."
sources: ["summaries/bacdive_metal_validation__REPORT.md", "summaries/counter_ion_effects__REPORT.md", "summaries/discoveries.md", "summaries/field_vs_lab_fitness__REPORT.md", "summaries/metal_cross_resistance__REPORT.md", "summaries/metal_fitness_atlas__REPORT.md", "summaries/metal_specificity__REPORT.md", "summaries/pathway_capability_dependency__REPORT.md"]
---
# Core-genome enrichment of metal-stress fitness genes

Metal-stress fitness genes are mostly core across several reports, with 88% and 87.4% core figures. [src: bacdive_metal_validation, counter_ion_effects] The strongest test is the shared-stress (NaCl) correction in counter_ion_effects, which left the [[entities/metal-fitness-atlas]] core enrichment intact. [src: counter_ion_effects, discoveries] The atlas itself reports 87.4% core versus 76.9% baseline across 22 organisms and 14 metals (OR=2.08, p=4.3e-162). [src: metal_fitness_atlas] Core enrichment is weaker for more metal-specific genes, but the difference is modest. [src: metal_specificity] The metal_specificity report finds metal-specific genes at 88.0% core versus 81.1% baseline, and less core than general sick genes at 90.2% (CMH p=0.011). [src: metal_specificity] Other reports reuse the atlas OR=2.08 figure in their own interpretation. [src: pathway_capability_dependency] Some metals rest on very few genes or one organism, and the page states this where it applies. [src: counter_ion_effects] The page stops at gene-level conservation.

## Overall core fraction

The metal_specificity project reported that metal tolerance genes are 88% core, predominantly conserved across species. [src: bacdive_metal_validation] The original Metal Fitness Atlas reported metal-important genes as 87.4% core (OR=2.08, where OR is odds ratio). [src: counter_ion_effects] The atlas states this reverses the common assumption of accessory enrichment. [src: metal_fitness_atlas] A separate report explains that core enrichment is a within-species pattern, since most metal genes are present in most genomes of a species. Between-species variation in the total number of metal tolerance genes creates the environmental signal. [src: bacdive_metal_validation] One report concludes that the accessory genome contributes only modestly to metal resistance machinery. [src: discoveries]

The pathway_capability_dependency report adopted the atlas's OR-based conservation validation and cross-species aggregation framework, citing 87.4% of metal-fitness genes as core (OR=2.08). [src: pathway_capability_dependency] It uses the atlas finding that fitness-important genes are enriched in the core genome (OR=2.08) in its evolutionary interpretation. [src: pathway_capability_dependency] It describes its own small conservation enrichment for Active Dependencies as aligned in direction with the atlas result. [src: pathway_capability_dependency]

Across organisms, metal-important genes are more core than baseline in 21 of 22 atlas organisms, with 14 significant at p<0.05. [src: metal_fitness_atlas] The one exception, P. fluorescens FW300-N2E3, shows only a negligible negative delta (-0.003, p=0.70). [src: metal_fitness_atlas]

### Interpretation in the atlas

The atlas initially hypothesised (H1a) accessory enrichment for toxic-metal genes, based on a prior DvH finding of 71.2% core for condition-specific heavy-metal genes. The result is the opposite. [src: metal_fitness_atlas] The report attributes the enrichment to core processes vulnerable to metal disruption (cell envelope, DNA repair, central metabolism), not specialized resistance mechanisms. [src: metal_fitness_atlas] It adds protein quality control to the list and says the genes that matter most are not efflux pumps or metal-binding proteins. [src: metal_fitness_atlas] It reads this as metal tolerance being about core genome robustness rather than accessory gene acquisition. [src: metal_fitness_atlas] It reports that this aligns with Borchert et al. (2019). [src: metal_fitness_atlas] It says the finding contradicts the assumption of primarily accessory metal resistance, while noting that Li et al. (2017) and Peng et al. (2022) studied annotated resistance genes such as efflux pumps and czc operons, which are indeed accessory. [src: metal_fitness_atlas]

The report explains the earlier DvH 71.2% figure by selection: that analysis isolated genes important only for metals, whereas the atlas captures all genes with any metal fitness defect. [src: metal_fitness_atlas] Its two-tier model is described as partially supported and needing reframing. [src: metal_fitness_atlas] Tier 1 (core) is general stress response, the majority of metal fitness genes, conserved for essential functions beyond metal tolerance. [src: metal_fitness_atlas] Tier 2 (accessory) is a smaller fraction giving specific resistance, with accessory enrichment visible only after controlling for general stress response. [src: metal_fitness_atlas]

The metal_specificity report also argues the atlas's 87.4% core finding is not an artifact. Removing all pleiotropic genes leaves a metal-specific set that is 88% core, so general stress genes did not inflate it. [src: metal_specificity] It finds the two-tier model partially supported: general stress is more core than specific resistance, but both tiers are strongly core-enriched and the accessory contribution is small. [src: metal_specificity]

## Per-metal core enrichment in the atlas

Core enrichment is individually significant at p<0.05 for 12 of 14 metals. [src: metal_fitness_atlas] The strongest deltas are manganese (+0.198, all 30 important genes core), zinc (+0.151), molybdenum (+0.148), tungsten (+0.145) and iron (+0.116). [src: metal_fitness_atlas] Essential-metal tolerance genes (Fe, Mo, W, Se, Mn) have a mean core-fraction delta of +0.148, nearly double the toxic-metal delta of +0.081 (Mann-Whitney U=39, p=0.015, one-sided). [src: metal_fitness_atlas]

| Metal | Type | Important genes | Core fraction | Delta | OR | p |
|---|---|---|---|---|---|---|
| Manganese | essential | 30 | 1.000 | +0.198 | inf | 2.0e-03 [src: metal_fitness_atlas] |
| Zinc | toxic | 1,517 | 0.890 | +0.151 | 2.94 | 2.0e-49 [src: metal_fitness_atlas] |
| Molybdenum | essential | 302 | 0.950 | +0.148 | 5.32 | 1.3e-14 [src: metal_fitness_atlas] |
| Tungsten | essential | 303 | 0.947 | +0.145 | 4.98 | 5.3e-14 [src: metal_fitness_atlas] |
| Mercury | toxic | 106 | 0.934 | +0.132 | 3.62 | 1.6e-04 [src: metal_fitness_atlas] |
| Selenium | essential | 134 | 0.933 | +0.131 | 3.59 | 2.9e-05 [src: metal_fitness_atlas] |
| Iron | essential | 651 | 0.919 | +0.116 | 3.07 | 8.5e-18 [src: metal_fitness_atlas] |
| Aluminum | toxic | 1,381 | 0.898 | +0.107 | 2.37 | 1.2e-26 [src: metal_fitness_atlas] |
| Copper | toxic | 2,139 | 0.867 | +0.090 | 1.91 | 3.8e-27 [src: metal_fitness_atlas] |
| Nickel | toxic | 1,760 | 0.877 | +0.088 | 1.93 | 3.0e-22 [src: metal_fitness_atlas] |
| Cobalt | toxic | 1,859 | 0.859 | +0.072 | 1.67 | 8.1e-16 [src: metal_fitness_atlas] |
| Chromium | toxic | 262 | 0.710 | +0.060 | 1.33 | 4.0e-02 [src: metal_fitness_atlas] |
| Uranium | toxic | 178 | 0.685 | +0.035 | 1.18 | 3.4e-01 [src: metal_fitness_atlas] |
| Cadmium | toxic | 92 | 0.522 | -0.010 | 0.96 | 9.2e-01 [src: metal_fitness_atlas] |

Only cadmium (1 organism) and uranium (2 organisms) are not significant, likely due to limited organism coverage. [src: metal_fitness_atlas] For uranium, the report leaves open whether the genes are truly neutral or the effect was underpowered. [src: metal_fitness_atlas] Manganese and tungsten each rest on one organism (DvH), with delta +0.198 and +0.145 respectively. [src: metal_fitness_atlas]

## Robustness to shared-stress (NaCl) correction

The correction did not remove the enrichment. It strengthened it for several metals. The concern was that osmotic-stress genes are core cellular machinery, so shared-stress overlap could inflate the original atlas result. [src: counter_ion_effects] After removing the ~40% shared-stress genes and restricting to metal-specific genes, enrichment was fully preserved for 12 of 14 metals. [src: counter_ion_effects, discoveries] The report states that shared-stress genes are ~90% core, so removing them leaves metal-specific genes that are still highly core. [src: counter_ion_effects] Core enrichment increased for 7 of 14 metals: Mo, W, Hg, Se, Ni, Cr and U. [src: counter_ion_effects] The report concludes that the atlas result is not an artifact of shared-stress overlap. [src: counter_ion_effects, discoveries] It rejected hypothesis H1c, which predicted weaker enrichment after correction. [src: counter_ion_effects] It also says atlas users need not filter NaCl-responsive genes. [src: counter_ion_effects] It reads the result as strengthening the core genome robustness model, in which metal fitness genes are core because they represent fundamental cellular processes. [src: counter_ion_effects]

### Per-metal values

Each row gives core fraction (original → corrected), baseline, delta (original → corrected) and the report's label for one metal. [src: counter_ion_effects]

| Metal | Core fraction | Baseline | Delta | Label |
|---|---|---|---|---|
| Manganese | 1.000 → 1.000 | 0.818 | +0.182 → +0.182 | unchanged [src: counter_ion_effects] |
| Molybdenum | 0.950 → 0.964 | 0.818 | +0.132 → +0.145 | stronger [src: counter_ion_effects] |
| Tungsten | 0.947 → 0.952 | 0.818 | +0.129 → +0.134 | stronger [src: counter_ion_effects] |
| Mercury | 0.934 → 0.951 | 0.818 | +0.116 → +0.133 | stronger [src: counter_ion_effects] |
| Selenium | 0.933 → 0.949 | 0.818 | +0.115 → +0.131 | stronger [src: counter_ion_effects] |
| Zinc | 0.895 → 0.865 | 0.750 | +0.145 → +0.115 | weaker [src: counter_ion_effects] |
| Nickel | 0.882 → 0.892 | 0.794 | +0.088 → +0.098 | stronger [src: counter_ion_effects] |
| Copper | 0.882 → 0.876 | 0.792 | +0.090 → +0.084 | slightly weaker [src: counter_ion_effects] |
| Cobalt | 0.866 → 0.866 | 0.790 | +0.076 → +0.076 | unchanged [src: counter_ion_effects] |
| Aluminum | 0.897 → 0.866 | 0.799 | +0.099 → +0.068 | weaker [src: counter_ion_effects] |
| Chromium | 0.710 → 0.723 | 0.654 | +0.056 → +0.069 | stronger [src: counter_ion_effects] |
| Uranium | 0.685 → 0.694 | 0.654 | +0.031 → +0.040 | slightly stronger [src: counter_ion_effects] |
| Cadmium | 0.522 → 0.422 | 0.530 | -0.008 → -0.108 | reversed (n=92, 1 org) [src: counter_ion_effects] |
| Iron | 0.778 → 1.000 | 0.818 | -0.040 → +0.182 | reversed but n=9, 1 org [src: counter_ion_effects] |

The report calls Mo, W, Hg and Se essential metals, and these showed stronger enrichment after correction. [src: counter_ion_effects, discoveries] Toxic metals with broad cellular effects, Al and Zn, showed modest decreases. [src: counter_ion_effects]

### Limits on the correction result

- The report names cadmium as the only metal that reverses, with 92 original genes from 1 organism and very low statistical power. [src: counter_ion_effects] The table also labels iron as reversed, but with n=9 from 1 organism. [src: counter_ion_effects]
- Cadmium (n=92) and iron (n=9), each from one organism, have statistically unreliable corrected deltas. [src: counter_ion_effects]
- Manganese (n=30, 1 organism) is low-powered, but the report considers its 100% core result robust by ceiling effect. [src: counter_ion_effects]
- Putative essential genes (~14.3% of protein-coding genes) lack transposon insertions and are absent from both datasets. They are 82% core, and excluding them affects the original and corrected analyses equally. [src: counter_ion_effects]
- The atlas report adds that essential genes (~14.3% of protein-coding genes, ~82% core) are absent from its fitness data, so it calls the observed core enrichment a conservative estimate. [src: metal_fitness_atlas]
- The atlas defines metal-important broadly (fit < -1 OR n_sick ≥ 1, ~3.3% of genes), and most of these are general stress genes rather than metal-specific. [src: metal_fitness_atlas]

## Specificity tiers

Core fraction falls as genes become more metal-specific, but every tier stays mostly core. In metal_cross_resistance, 8,162 metal-important genes across 28 organisms fell into three tiers. [src: metal_cross_resistance] The report defines general-stress genes as pleiotropic, important across many conditions. Metal-shared genes are cross-resistance drivers important for ≥2 metals. Metal-specific genes are important for exactly 1 metal. [src: metal_cross_resistance] The gradient was general stress most conserved, metal-shared intermediate, and metal-specific least conserved. [src: metal_cross_resistance] The report cites the atlas's 87.4% core figure and describes this finer gradient within metal genes (92%, 91%, 90%) as reflecting the evolutionary history of metal tolerance. [src: metal_cross_resistance]

- General stress: 1,484 genes, 18.2% of total, mean core 92.0%, fully core (≥95%) 57.2%. [src: metal_cross_resistance]
- Metal-shared: 2,306 genes, 28.3% of total, mean core 91.0%, fully core (≥95%) 50.4%. [src: metal_cross_resistance]
- Metal-specific: 4,372 genes, 53.6% of total, mean core 89.8%, fully core (≥95%) 45.7%. [src: metal_cross_resistance]

The fully core gradient is an 11.5 percentage point spread. [src: metal_cross_resistance] The report reads this as support for an evolutionary model running from ancestral general-stress defense, through slower-evolving shared metal defense, to faster-evolving, more accessory specialized resistance. This is an interpretation, not a measurement. [src: metal_cross_resistance] The report proposes the three-tier decomposition with its core gradient as a framework for metal tolerance evolution. [src: metal_cross_resistance] Keyword analysis found general-stress genes enriched for energy/respiration and cell-envelope functions. [src: metal_cross_resistance] Metal-specific genes were enriched for transporters/efflux and iron/metal-related functions. [src: metal_cross_resistance]

### Pooled and organism-mean core fractions (metal_specificity)

The metal_specificity report compares pooled core fractions (total core / total genes) and organism-mean fractions (mean of per-organism core fractions) across the 22 organisms with pangenome links. [src: metal_specificity]

| Category | Pooled core | Organism-mean core | Mean delta | Positive/total | Significant/total |
|---|---|---|---|---|---|
| Metal-specific | 84.8% (2,969/3,500) [src: metal_specificity] | 88.0% [src: metal_specificity] | +6.9% | 19/22 | 12/22 |
| Metal+stress | 94.3% (467/495) [src: metal_specificity] | 93.6% [src: metal_specificity] | +10.9% | 13/13 | 1/13 |
| General sick | 90.2% (2,183/2,420) [src: metal_specificity] | 90.2% [src: metal_specificity] | +9.0% | 21/21 | 8/21 |
| Baseline | 79.8% (73,957/92,650) [src: metal_specificity] | 81.1% | — | — | — |

The pooled metal-specific fraction (84.8%) is below the organism mean (88.0%), reflecting organisms with large gene sets and lower core fractions. [src: metal_specificity] All three categories are significantly core-enriched above baseline, and metal-specific genes are least enriched, consistent with a modest tendency for specialized resistance to sit in the accessory genome. [src: metal_specificity] The Cochran-Mantel-Haenszel test finds metal-specific genes less core-enriched than general sick genes across organisms (p=0.011). [src: metal_specificity] The report reads this as a modest but real difference: specialized metal resistance genes are slightly more likely to be accessory than general stress genes. [src: metal_specificity] It interprets the 2% gap between metal-specific (88%) and general sick genes (90.2%) as a detectable signal of accessory genome contribution, while the metal-specific genes remain overwhelmingly conserved. [src: metal_specificity] The report notes that about 14% of genes (~82% core) are absent from fitness data, biasing all categories toward core enrichment. [src: metal_specificity] It says the true baseline is likely below 81%, making the deltas conservative. [src: metal_specificity]

The discoveries digest agrees on direction using a different comparison. Metal-specific genes were 84.8% core (pooled), versus 90.2% for general sick genes (Cochran-Mantel-Haenszel p=0.011). [src: discoveries] Both categories exceeded the 79.8% baseline. [src: discoveries] The report says this partially supports the Metal Atlas two-tier model, because general stress is more core than specialized metal resistance, but both are predominantly core. [src: discoveries] The counter_ion_effects report notes that the earlier atlas found genes important only for metals to be less core. It suggests its gene classification could refine that analysis. [src: counter_ion_effects]

## Tensions

- In Desulfovibrio vulgaris Hildenborough (DvH), heavy-metals important genes (198 genes) are 71.2% core, OR 0.77 versus baseline, FDR q=0.14 (FDR is false discovery rate). [src: field_vs_lab_fitness] They trend below baseline but not significantly, as do lab-antibiotic genes. [src: field_vs_lab_fitness] The report calls heavy-metal resistance genes among the least conserved, against a 76.3% baseline. [src: field_vs_lab_fitness] Core percentages for the class were 70.6%, 71.2%, 76.7% and 76.7% at fitness thresholds -3.0, -2.0, -1.5 and -1.0. [src: field_vs_lab_fitness] This single-organism result contrasts with the multi-organism enrichment above. The atlas report attributes the difference to gene selection (condition-specific versus any metal defect), but the page does not treat that as settled. [src: metal_fitness_atlas]

## Open Directions

- Re-run the shared-stress correction for cadmium, iron and manganese with more organisms. This would test whether the cadmium and iron reversals survive adequate power.
- Test whether DvH's below-baseline heavy-metal core fraction recurs in other organisms using one baseline and one gene definition. This would show whether DvH is an exception or reflects a field-versus-lab difference.
- Combine the NaCl-corrected gene classes with the three-tier classification. This would show whether the specificity gradient in core fraction survives shared-stress removal.
- Compare the 82%-core essential genes with the corrected metal gene sets. This would test whether the exclusion affects conclusions per metal.
- Add organisms for uranium and cadmium, and test manganese and tungsten outside DvH. This would show whether their weak or single-organism enrichment is true neutrality or low power.
