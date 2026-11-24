---
type: "Concept"
description: "Relative predictive power of gene counts, taxonomy and phenotypes for genome-based metal tolerance scores, and the caveat that scores are genome-derived."
sources: ["summaries/bacdive_phenotype_metal_tolerance__REPORT.md", "summaries/discoveries.md", "summaries/metal_fitness_atlas__REPORT.md"]
---
# Genome-encoded metal resistance repertoire versus phenotype as predictor of metal tolerance

In a BacDive analysis, taxonomy explained more variance in genome-based metal tolerance scores than phenotypes did. The number of metal resistance gene clusters in a genome (n_metal_clusters) added the most once it was combined with taxonomy. [src: bacdive_phenotype_metal_tolerance] The scores are themselves genome-derived, so the result does not show that gene count predicts directly measured tolerance. [src: bacdive_phenotype_metal_tolerance] See [[entities/bacdive]], [[entities/metal-fitness-atlas]] and [[entities/xgboost-with-phylogenetic-blocked-cross-validation]].

## Literature Context

Several candidate papers compare metal-resistance genotype with measured phenotype in single isolate collections. In Salmonella enterica and Escherichia coli from swine feed mills (33 and 30 isolates), all isolates that possessed the copper resistance operon were resistant to the highest concentration tested (40 mM) [PMID 37290750](https://pubmed.ncbi.nlm.nih.gov/37290750/). The abstract reports 99% and 98.3% genotype–phenotype concordance for Salmonella and E. coli, but that figure is for antimicrobial resistance, not metals [PMID 37290750](https://pubmed.ncbi.nlm.nih.gov/37290750/). In Xanthomonas arboricola pv. pruni, deleting both copies of a plasmid copper cluster abolished resistance. The copL-D genes were the main contributors, and adding copF-cusB raised resistance further [PMID 41363119](https://pubmed.ncbi.nlm.nih.gov/41363119/). This was a single strain, so it is evidence of gene function, not of a population-level predictor. In multidrug-resistant Salmonella (19 isolates tested for metal susceptibility), reduced susceptibility to zinc, copper, silver, arsenic and tellurite was attributed to specific genes such as zitB, pcoA/pcoD and silA/silE, and isolates often carried several metal resistance genes [PMID 30480469](https://pubmed.ncbi.nlm.nih.gov/30480469/).

Other candidates describe metal genes or tolerance without a quantitative link between them. Environmental Pseudomonas aeruginosa isolates were tolerant mainly to copper, cadmium and zinc and carried metal tolerance genes related to these metals [PMID 37221353](https://pubmed.ncbi.nlm.nih.gov/37221353/). Among 60 ESBL E. coli from chicken meat, zitB, copA and cueO were highly prevalent, but the abstract reports no matched metal tolerance measurements [PMID 35843029](https://pubmed.ncbi.nlm.nih.gov/35843029/). Electroplating-sludge isolates showed multiple resistance genotypes and phenotypes, and the strain with the most resistance gene sequences (10) resisted seven metal categories [PMID 31228823](https://pubmed.ncbi.nlm.nih.gov/31228823/). Taxonomic partitioning of phenotype was not tested in any of these studies.

The hub's central claim is that taxonomy explained more variance in genome-based tolerance scores than phenotypes did, and that n_metal_clusters added the most once combined with taxonomy (R² = 0.633 in the full model). This is consistent in direction with the isolate studies. Those studies link gene content to measured copper phenotypes in small collections [PMID 37290750](https://pubmed.ncbi.nlm.nih.gov/37290750/) [PMID 41363119](https://pubmed.ncbi.nlm.nih.gov/41363119/). They do not test the hub's actual comparison of gene count, taxonomy and phenotype across 3,994 genomes. The gene-count-only R² of 0.063 is also lower than the phenotype-only R² of 0.163, which these papers neither support nor contradict. The literature therefore gives only qualitative support. The hub's own caveat stands: its scores are genome-derived, so it does not show that gene count predicts directly measured tolerance.

The corpus extends this literature with a cross-taxon, phylogenetically blocked model comparison, which none of the candidates attempt. The candidates do suggest a test the corpus lacks. Gene-to-phenotype concordance for metals could be checked against measured tolerance in matched isolates, as in the Salmonella and E. coli feed-mill work [PMID 37290750](https://pubmed.ncbi.nlm.nih.gov/37290750/). The candidates do not address the Metal Fitness Atlas report's tension, that gene presence alone failed validation and regulatory or expression information may be needed.

## Relative predictive power

Taxonomy explained far more variance than phenotypes. Gene count added the most once it joined taxonomy, which led the report to call genome-encoded metal resistance repertoire the true predictor. [src: bacdive_phenotype_metal_tolerance]

The report defines n_metal_clusters as the number of metal resistance gene clusters. [src: bacdive_phenotype_metal_tolerance] Models were compared with 5-fold phylogenetic-blocked cross-validation (CV). [src: bacdive_phenotype_metal_tolerance]

| Model | R² | RMSE (root mean square error) | n | Features |
|---|---|---|---|---|
| Gene count only | 0.063 | 0.045 | 3,994 | 1 [src: bacdive_phenotype_metal_tolerance] |
| Phenotype only | 0.163 | 0.043 | 3,994 | 13 [src: bacdive_phenotype_metal_tolerance] |
| Taxonomy only | 0.354 | 0.038 | 3,994 | 3 [src: bacdive_phenotype_metal_tolerance] |
| Taxonomy + Phenotype | 0.345 | 0.038 | 3,994 | 16 [src: bacdive_phenotype_metal_tolerance] |
| Full (all combined) | 0.633 | 0.028 | 3,994 | 17 [src: bacdive_phenotype_metal_tolerance] |

In the table, the gene-count-only model (R² = 0.063) scored lower than the phenotype-only model (R² = 0.163) and the taxonomy-only model (R² = 0.354). [src: bacdive_phenotype_metal_tolerance] The report separately states that gene content explains more variance than all phenotype features combined and substantially more than taxonomy alone. [src: bacdive_phenotype_metal_tolerance] This statement sits uneasily with the standalone gene-count R² in the table, and the claims do not reconcile the two. [src: bacdive_phenotype_metal_tolerance] What the report does show is that gene count gave a delta R² of +0.28 over taxonomy alone, and that the full model reached R² = 0.63. [src: bacdive_phenotype_metal_tolerance] Shapley additive explanations (SHAP) importance in the full model ranked taxonomic class/order codes and n_metal_clusters highest. [src: bacdive_phenotype_metal_tolerance]

## Phenotypes add nothing beyond taxonomy

Phenotypes carry real signal (R² = 0.16), but taxonomy already supplies it. [src: bacdive_phenotype_metal_tolerance] Taxonomy alone explained 35.4% of variance and phenotype alone 16.3%. Their combination gave R² = 34.5%, slightly worse than taxonomy alone. [src: bacdive_phenotype_metal_tolerance] The report gives delta R² = -0.009 for adding phenotypes to taxonomy. [src: bacdive_phenotype_metal_tolerance] It reads this as phenotypes being noisier proxies for taxonomy, not independent predictors. [src: bacdive_phenotype_metal_tolerance] SHAP agrees: phenotype features contribute minimally once taxonomy is included. [src: bacdive_phenotype_metal_tolerance] This is the phylogenetic confounding covered in [[concepts/phylogenetic-confounding-of-phenotype-metal-tolerance-associations]].

## Support and the genome-derived caveat

The report presents this as support for genome-based prediction, the Metal Fitness Atlas, over phenotype-based screening. [src: discoveries] It cites Schwan et al. (2023), who found strong genotype–phenotype concordance for metal resistance gene presence in *Salmonella* and *E. coli*. [src: bacdive_phenotype_metal_tolerance]

Metal Fitness Atlas scores are genome-based predictions, not direct tolerance measurements. [src: bacdive_phenotype_metal_tolerance] The report mitigates circularity by controlling for n_metal_clusters in partial correlations. Even so, the phenotype–score associations are phenotype-to-genome correlations, not phenotype-to-phenotype. [src: bacdive_phenotype_metal_tolerance]

## Tensions

- The BacDive result favours the gene-count repertoire as the true predictor of tolerance scores. [src: bacdive_phenotype_metal_tolerance, discoveries] The Metal Fitness Atlas report says its repertoire prediction failed validation. It states that simple gene presence/absence does not predict metal tolerance and that a regulatory or expression-based model is needed. [src: metal_fitness_atlas]
- That report links the failure to Rosconi et al. (2022): gene essentiality is context-dependent and cannot be predicted from gene presence alone. [src: metal_fitness_atlas]
- Within the BacDive report, the statement that gene content explains more variance than all phenotype features [src: bacdive_phenotype_metal_tolerance] sits against the gene-count-only R² of 0.063 versus phenotype-only R² of 0.163. [src: bacdive_phenotype_metal_tolerance]

## Open Directions

- Test the gene-count model against measured tolerance (for example MIC or growth data) to remove the circularity of genome-derived scores.
- Add regulatory or expression features to the gene-count model and check whether they improve on the repertoire in fitness data.
- Repeat the model comparison in other datasets and with other phylogenetic blocking levels, to see if the +0.28 gain holds.
- Recompute the gene-count-only versus phenotype-only comparison to resolve the gap between the table and the variance statement.
