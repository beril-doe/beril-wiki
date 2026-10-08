<!-- tension-hash: d89b8efaaad71d4f -->
# Does Genomic and Metabolic Evidence for Tryptophan Imply Measured Growth on It?

Two projects bear on whether genomic and metabolic signals for tryptophan correspond to a measured growth phenotype, but they measure different endpoints, and whether their findings truly conflict is itself open. One found that tryptophan increased in WoM (Web of Microbes, an exometabolomics resource), had 231 significant Fitness Browser genes (Fitness Browser is a collection of genome-wide mutant fitness assays) and a complete GapMind pathway (GapMind is a pathway-completeness predictor), yet 0/50 *P. fluorescens* strains used it as a carbon source [src: fw300_metabolic_consistency]. Another reports that binary growth on tryptophan could be predicted with AUC (area under the receiver operating characteristic curve, a measure of how well a model separates growers from non-growers) 0.933 [src: genotype_to_phenotype_enigma]. This matters for [[concepts/cross-tenant-data-bridging]]: if joining resources in the KBase Data Lakehouse yields agreement on presence but not on use, then concordance across resources cannot stand in for phenotype.

## Evidence Sides

**Side A: production and pathway evidence do not imply utilization.** Tryptophan increased in WoM, had 231 significant Fitness Browser genes (Fitness Browser is a collection of genome-wide mutant fitness assays), and had a complete GapMind pathway (GapMind is a pathway-completeness predictor). Even so, 0/50 *P. fluorescens* strains used tryptophan as a carbon source. The project concludes that "production therefore does not imply utilization" [src: fw300_metabolic_consistency]. This is a null result for utilization in that strain set, and it is stated as a semantic mismatch between data types.

**Side B: binary growth on tryptophan is predictable.** Binary (growth / no-growth) phenotypes could be predicted for tryptophan (AUC 0.933), phenylalanine (0.932) and valine (0.927) [src: genotype_to_phenotype_enigma]. In the same project, continuous phenotypes had negative R² (coefficient of determination; a negative value means the model fits worse than predicting the mean) [src: genotype_to_phenotype_enigma]. The project thus reports successful binary prediction for these substrates but unsuccessful continuous-phenotype prediction in its tested setting.

## Possible Reconciliations

- *Hypothesis 1:* The two sides measure different things. Side A asks whether production, gene fitness and pathway completeness co-occur with carbon-source use. Side B asks whether a model can discriminate growers from non-growers. A high AUC can coexist with a panel in which non-growers are common.
- *Hypothesis 2:* The strain panels may differ. Side A's 0/50 refers to *P. fluorescens* strains; the membership of Side B's panel and its overlap with those strains have not been checked here, so taxonomic scope remains only a candidate explanation.
- *Hypothesis 3:* Tryptophan genes and a complete pathway may support biosynthesis or nitrogen use rather than use as a carbon source. In that case, "pathway present" and "carbon utilization" are not the same claim.

## Resolving Work

- Using the genotype_to_phenotype_enigma tryptophan model, compare its predictions with observed growth labels, tabulating class balance and per-class errors at chosen thresholds, to see how growers and non-growers are each classified behind AUC 0.933.
- Apply that trained model to the 50 *P. fluorescens* strains and compare its calls to the observed 0/50. This tests whether the model reproduces the null result.
- Split the 231 Fitness Browser tryptophan genes by experimental condition (tryptophan as carbon source versus as nitrogen source versus rich medium). This tests Hypothesis 3: whether the fitness signal reflects carbon catabolism at all.
- Cross-check GapMind pathway completeness for tryptophan catabolism, as distinct from biosynthesis, across both strain panels. The question is whether "complete pathway" refers to the same pathway on both sides.
