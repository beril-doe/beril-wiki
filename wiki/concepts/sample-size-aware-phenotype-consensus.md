---
type: "Concept"
description: "Species-level phenotype claims should report strain count and consensus strength"
sources: ["summaries/fw300_metabolic_consistency__REPORT.md"]
---
# Species-level utilization claims require sample-size-aware strain consensus

Species-level utilization claims should be based on per-strain consensus and reported with the number of strains supporting each result. Per-strain consensus applies a majority vote among duplicate records for each strain before calculating the species-level utilization rate, preventing duplicate records from being treated as independent strains. [src: fw300_metabolic_consistency]

## Why sample size changes interpretation

A utilization percentage without its strain count can obscure whether a result is broadly supported, strain-variable, or based on too little evidence. In the FW300-N2E3 cross-database analysis, BacDive utilization counts ranged from 1 to 51 strains, and raw records could be higher because of duplicate entries per strain. [src: fw300_metabolic_consistency] The report therefore treats sample size as part of the evidence rather than as supplementary metadata. [src: fw300_metabolic_consistency]

This approach is especially important when [[entities/bacdive]] species-level phenotypes are used to interpret metabolite production by one isolate. BacDive aggregates *P. fluorescens* strains and, under GTDB reclassification, spans a broad clade identified as *Pseudomonas_E fluorescens_E*; consequently, a species-level rate may not represent the phenotype of FW300-N2E3 specifically. [src: fw300_metabolic_consistency] This limitation connects species-level phenotype inference to [[concepts/environmental-resistome]] and [[concepts/taxonomic-resolution-dependent-functional-inference]].

## Evidence from FW300-N2E3

The strongest example was tryptophan. FW300-N2E3 increased tryptophan in the WoM exometabolome, had 231 genes with significant fitness effects when grown on tryptophan in the Fitness Browser, and had a complete tryptophan biosynthesis pathway prediction from GapMind. [src: fw300_metabolic_consistency] In contrast, 0 out of 50 *P. fluorescens* strains in BacDive could utilize tryptophan as a carbon source, with high confidence based on n=50 and pct_positive=0.0 using per-strain consensus. [src: fw300_metabolic_consistency] This is the most robust production-versus-utilization discordance in the report, but it does not establish that FW300-N2E3 itself cannot grow on tryptophan. [src: fw300_metabolic_consistency]

The evidentiary strength of other BacDive non-utilization results was lower or more heterogeneous. Trehalose had 1 positive and 5 negative strains, or 1/6, and was classified with moderate confidence. [src: fw300_metabolic_consistency] Lysine had 0 positive and 3 negative strains, or 0/3, also with moderate confidence. [src: fw300_metabolic_consistency] Glycine had 0 positive and 1 negative strain, or 0/1, with low confidence. [src: fw300_metabolic_consistency] These results support treating trehalose as potentially strain-variable, lysine as consistently negative within a small sample, and glycine as insufficient for a conclusion rather than treating all three as equivalent species-level findings. [src: fw300_metabolic_consistency]

The report also records a denominator discrepancy that should remain visible: its primary tryptophan result reports 0+/50- with n=50, while its literature-context discussion states that only tryptophan, with n=52, has sufficient data for a confident conclusion. [src: fw300_metabolic_consistency] The values should not be silently reconciled or averaged. [src: fw300_metabolic_consistency]

## Relationship to cross-database concordance

BacDive was the variable component of the cross-database comparison. Among 41 individual metabolite-database comparisons, 37 were concordant, or 90.2%; Fitness Browser comparisons were concordant for 21/21, or 100%, and GapMind comparisons were concordant for 13/13, or 100%, whereas BacDive utilization was positive for only 3/7 matched metabolites, or 43%. [src: fw300_metabolic_consistency] The 3/7 rate for WoM-produced metabolites was compared with the overall *P. fluorescens* baseline of 22/80, or 27.5%, using a binomial test that gave p = 0.40. [src: fw300_metabolic_consistency]

These results **refine** [[concepts/multi-omics-integration]] by showing that apparent cross-database disagreement can reflect the resolution and sample size of the phenotype resource, not only biological inconsistency. [src: fw300_metabolic_consistency] They also **support** [[concepts/phenotype-database-coverage-bias]] because only 8/58 WoM metabolites, or 14%, could be matched to BacDive *P. fluorescens* utilization data. [src: fw300_metabolic_consistency]

The distinction between production and utilization is also necessary. WoM exometabolomics can measure overflow metabolism, biosynthetic byproduct release, or active secretion, whereas BacDive growth assays measure utilization as a growth capability. [src: fw300_metabolic_consistency] Therefore, production by FW300-N2E3 and non-utilization at the aggregated species level are not intrinsically contradictory. [src: fw300_metabolic_consistency]

## Interpretation rule

A species-level utilization claim should report at least the per-strain positive and negative counts, the resulting utilization fraction, the confidence or evidentiary category, and whether duplicate records were collapsed by per-strain consensus. [src: fw300_metabolic_consistency] Claims based on large samples, such as tryptophan at 0+/50- with n=50, can support stronger conclusions than claims based on 0/1 or 0/3 strains. [src: fw300_metabolic_consistency] Even a high-confidence species-level result remains a population-level constraint on interpreting FW300-N2E3, not a direct measurement of that isolate's phenotype. [src: fw300_metabolic_consistency]

## Open Directions

- Extend the FW300-N2E3 crosswalk to additional isolates, including *Pseudomonas stutzeri* RCH2, and test whether BacDive utilization rates are reproducible across isolates rather than driven by the current strain composition. [src: fw300_metabolic_consistency]
- Expand WoM–BacDive matching with InChIKey or CHEBI identifiers, then reassess whether the observed 8/58 BacDive coverage and 3/7 utilization rate change when nomenclature-based missed matches are reduced. [src: fw300_metabolic_consistency]
- Reanalyze BacDive records with explicit per-strain consensus and sample-size thresholds, asking which utilization claims remain stable after duplicate records and low-n comparisons are separated. [src: fw300_metabolic_consistency]
- Compare strain-resolved BacDive phenotypes with isolate-specific Fitness Browser and WoM data, asking whether species-level non-utilization predicts or obscures FW300-N2E3-specific growth and secretion. [src: fw300_metabolic_consistency]
