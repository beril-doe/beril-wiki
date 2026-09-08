---
type: Dataset
description: Bacterial strain database linking phenotypes and isolation metadata to
  genome analyses
sources:
- id: bacdive_metal_validation
  resource: ../summaries/bacdive_metal_validation__REPORT.md
  title: bacdive metal validation
- id: bacdive_phenotype_metal_tolerance
  resource: ../summaries/bacdive_phenotype_metal_tolerance__REPORT.md
  title: bacdive phenotype metal tolerance
- id: berdl_data_atlas
  resource: ../summaries/berdl_data_atlas__REPORT.md
  title: berdl data atlas
- id: fw300_metabolic_consistency
  resource: ../summaries/fw300_metabolic_consistency__REPORT.md
  title: fw300 metabolic consistency
- id: gene_function_ecological_agora
  resource: ../summaries/gene_function_ecological_agora__REPORT.md
  title: gene function ecological agora
- id: metal_cross_resistance
  resource: ../summaries/metal_cross_resistance__REPORT.md
  title: metal cross resistance
- id: pitfalls
  resource: ../summaries/pitfalls.md
  title: pitfalls
- id: plant_microbiome_ecotypes
  resource: ../summaries/plant_microbiome_ecotypes__REPORT.md
  title: plant microbiome ecotypes
title: BacDive
---
# BacDive

## What it is

**Canonical name:** BacDive. [^bacdive_metal_validation]

BacDive is a bacterial strain database providing strain isolation-environment and phenotype metadata. [^bacdive_metal_validation] The BERDL Data Atlas inventories 97,334 BacDive strain phenotype profiles, **supporting** the corpus size used by the metal-tolerance studies. [^berdl_data_atlas]

**Known aliases:** No aliases were reported in the source documents. [^bacdive_metal_validation]  
**Stable external identifier:** No stable external identifier was reported in the source documents. [^bacdive_metal_validation]

BacDive taxonomy must be reconciled with [gtdb](gtdb.md) naming before joins: its species names can differ from GTDB names, and the pitfalls report identifies BacDive–GTDB naming differences as a source of unmatched species concepts rather than evidence of biological absence. [^pitfalls]

The plant-microbiome analysis identified 2,482 plant-related BacDive strains, but these records contributed zero additional genome upgrades beyond `ncbi_env`; this **refines** BacDive's role in plant-association analyses as a phenotype and metadata resource rather than an independent source of genome assignments. [^plant_microbiome_ecotypes]

## Key facts from BacDive–metal-tolerance studies

BacDive strain records have been linked to [gtdb](gtdb.md) pangenome metal-tolerance scores from the [metal-fitness-atlas](metal-fitness-atlas.md) to test whether isolation environments and classical phenotypes validate or independently predict genome-based tolerance. [^bacdive_metal_validation][^bacdive_phenotype_metal_tolerance]

The isolation-environment validation matched 42,227 of 97,334 BacDive strains (43.4%) to 6,426 GTDB species, including 25,089 matched strains with isolation-source metadata. [^bacdive_metal_validation] Exact species-name agreement accounted for 33,535 strains (34.5%), while GTDB suffix removal produced 8,692 additional matches (8.9%); 55,107 strains (56.6%) remained unmatched. [^bacdive_metal_validation]

A later phenotype bridge used the same 97,334-strain BacDive corpus but a different matching and filtering procedure: 37,368 strains (38.4%) matched a pangenome species and metal score, representing 5,647 GTDB species, including 3,994 species with at least 5 phenotype features. This **refines** the earlier coverage estimate by showing that usable matching depends on the analysis endpoint and phenotype requirements. [^bacdive_phenotype_metal_tolerance]

Bacteria isolated from heavy-metal contamination sites had a median metal score of 0.240, a mean of 0.236, a median delta of +0.053, and Cohen's d of +1.00 relative to the environmental baseline; the comparison had Mann-Whitney p=0.006 and n=10. [^bacdive_metal_validation] The environmental baseline had a median metal score of 0.187 and a mean of 0.195. [^bacdive_metal_validation] The reported contamination gradient was heavy metal (+1.00) > waste/sludge (+0.57) > all contamination (+0.43) > industrial (+0.20). [^bacdive_metal_validation] Waste/sludge isolates had n=305 and d=+0.57, all-contamination isolates had n=176 and d=+0.43, and industrial isolates had n=796 and d=+0.20. [^bacdive_metal_validation]

Within Pseudomonadota, contamination isolates had metal scores delta=+0.040 above environmental isolates (p<0.001; n=85 contamination and n=5,655 environmental), while within Actinomycetota the delta was +0.035 (p<0.001; n=62 and n=772, respectively). [^bacdive_metal_validation] These environmental associations **support** BacDive metadata as an ecological validation signal, but the phenotype bridge **refines** that interpretation by showing that curated phenotypes often track taxonomy rather than adding independent predictive power. [^bacdive_metal_validation][^bacdive_phenotype_metal_tolerance]

The phenotype bridge tested 10 features; seven passed FDR (false discovery rate) correction at q < 0.05: Gram stain (d = -0.610, q = 4.0e-60), oxidase (d = +0.530, q = 1.3e-24), motility (d = +0.345, q = 7.2e-23), urease (d = -0.175, q = 9.1e-06), enzyme breadth (rho = -0.058, q = 8.2e-04), nitrate reduction (d = +0.100, q = 7.4e-03), and catalase (d = +0.104, q = 4.1e-02). H₂S production did not pass correction (d = -0.867, q = 7.3e-02), while metabolite breadth (rho = -0.013, q = 4.7e-01) and acetate utilization (d = +0.005, q = 7.9e-01) were not significant. [^bacdive_phenotype_metal_tolerance]

Gram-negative species had higher metal tolerance scores than Gram-positive species (Cohen's d = -0.61, p < 1e-60, n = 3,272 species), but the signal was almost entirely between lineages, especially Actinomycetes and Proteobacteria, so the association is phylogenetically confounded. [^bacdive_phenotype_metal_tolerance] Urease-positive species likewise had lower scores (d = -0.18, p < 1e-5), driven by Actinomycetes (d = -0.59, p < 1e-16) and disappearing within Gammaproteobacteria (d = +0.08, ns) and Bacilli (d = +0.06, ns); this **contradicts** a general prediction that urease-associated nickel handling confers higher tolerance. [^bacdive_phenotype_metal_tolerance] Catalase showed a Simpson's-paradox pattern: the overall association was positive (d = +0.10), but catalase-negative species scored higher within Actinomycetes (d = -0.62, p < 1e-5), Gammaproteobacteria (d = -0.49, p = 0.004), and Betaproteobacteria (d = -0.51, p = 0.006). [^bacdive_phenotype_metal_tolerance]

The anaerobe-aerobe difference was negligible (d = -0.016, p = 0.55) among 3,751 species; facultative anaerobes had mean score 0.221, compared with 0.216 for aerobes and 0.215 for anaerobes, although the three-group Kruskal-Wallis test was marginally significant (H = 8.53, p = 0.014). [^bacdive_phenotype_metal_tolerance] Thus the new analysis **contradicts** a broad anaerobe advantage and finds the effect biologically trivial. [^bacdive_phenotype_metal_tolerance]

The Gene Function Ecological Agora analysis **supports** BacDive as a phenotype anchor for genome-derived ecological interpretations: among 318 Mycobacteriaceae species, 95% of recorded cell shapes were rod-shaped, 99% were non-motile, and 89.4% were aerobic-leaning; among 577 Bacteroidota species, anaerobic phenotypes occurred at 33.2% versus 22.0% atlas-wide and the profile was saccharolytic and glycoside-hydrolase-rich. [^gene_function_ecological_agora] These observations are consistent with, but do not independently establish, the corresponding atlas ecological patterns. Cyanobacteriia coverage was too thin for interpretation at n = 4, which **refines** the scope of phenotype-based validation. [^gene_function_ecological_agora]

Taxonomy alone explained 35.4% of metal tolerance variance, phenotype features alone explained 16.3%, and taxonomy plus phenotype yielded R² = 0.345, slightly below taxonomy alone (delta R² = -0.009). Adding `n_metal_clusters` increased the full model to R² = 0.633, making genome-encoded resistance repertoire the strongest predictor in this analysis. [^bacdive_phenotype_metal_tolerance] In 5-fold phylogenetic-blocked cross-validation, gene-count-only, phenotype-only, taxonomy-only, taxonomy-plus-phenotype, and full models had R² values of 0.063, 0.163, 0.354, 0.345, and 0.633, respectively, with RMSE values 0.045, 0.043, 0.038, 0.038, and 0.028; every model used n = 3,994 species. [^bacdive_phenotype_metal_tolerance] SHAP (Shapley additive explanation) importance placed taxonomic class/order codes and `n_metal_clusters` among the top predictors, while phenotype features contributed minimally after taxonomy was included. [^bacdive_phenotype_metal_tolerance]

Only 24 matched strains had metal-utilization records covering iron, manganese, arsenate, chromate, cobalt, or zinc; 8 results were positive and 16 were negative. [^bacdive_metal_validation] The exploratory comparison of positive utilizers with other strains had Mann-Whitney p=0.14 and Cohen's d=-0.57, so the direction was inconclusive. [^bacdive_metal_validation]

BacDive utilization is four-valued rather than binary: `+`, `-`, `produced`, and `+/-`; only explicit `+` and `-` observations should enter utilization percentages. [^pitfalls] For *Pseudomonas fluorescens*, indole had 60 “produced” entries and 1 actual utilization test, illustrating why production records must not be counted as utilization positives. [^pitfalls]

The newer gene-resolution cross-resistance study **contradicts** a strong interpretation of BacDive as an independently validated predictor at species scale: across 28 organisms, its multi-metal tolerance scores showed no correlation with BacDive metal-associated isolation at the Fitness Browser species scale (Spearman rho approximately -0.02, p > 0.8). [^metal_cross_resistance] After excluding 2 organisms without tier-classification data and collapsing multiple Fitness Browser strains from the same species, the effective sample size was 20 independent species, which the study considered too small for a meaningful correlation test. [^metal_cross_resistance] The report also notes that genus-plus-species substring matching was imprecise for organisms identified only to genus level, such as Acidovorax sp. [^metal_cross_resistance] This **refines** the earlier positive environmental validation by distinguishing genome-level cross-resistance structure from the underpowered species-scale isolation-environment test. [^metal_cross_resistance]

The study's heavy-metal estimate was imprecise because only n=10 matched heavy-metal isolates were available; at n=10 versus approximately 5,000 environmental-baseline strains, the minimum detectable effect size at 80% power was approximately d=0.93, compared with the observed d=1.00. [^bacdive_metal_validation] The phenotype study likewise had sparse feature coverage, ranging from 43,378 strains with isolation-source data and 29,784 with metabolite-breadth data to 5,254 with H₂S-production data and 1,980 with acetate-utilization data. [^bacdive_phenotype_metal_tolerance] The new validation reports n = 26 at Fitness Browser organism scale but n = 20 after matching and collapsing to independent species, a discrepancy that further **refines** the documented power limitation. [^metal_cross_resistance]

The direct Fitness Browser–BacDive validation contained 12 organisms representing 6 unique species: Cupriavidus basilensis, Methanococcus maripaludis, Ralstonia solanacearum, Pseudomonas simiae, [azospirillum-brasilense](azospirillum-brasilense.md), and Pseudomonas fluorescens. [^bacdive_phenotype_metal_tolerance] All Gram-typed organisms were Gram-negative, all urease-typed organisms were urease-negative yet routinely tested against nickel, and the single anaerobe had only 1 metal tested versus 4–5 for aerobes, preventing interpretable within-set tests. [^bacdive_phenotype_metal_tolerance]

## Plant microbiome and pathway-validation evidence

The plant-microbiome analysis **supports** BacDive as an independent check on GapMind pathway predictions: BacDive metabolite-utilization data agreed with GapMind predictions at 83.1% consistency. [^plant_microbiome_ecotypes] However, the GapMind core-level completeness score was 0% across compartments and may be too stringent for broad taxonomic comparisons, so this agreement does not establish complete pathway activity. [^plant_microbiome_ecotypes]

This analysis also **refines** interpretation of BacDive's plant metadata: 2,482 plant-related strains were identified, but they produced zero additional genome upgrades beyond `ncbi_env`; plant compartment assignments therefore remained primarily dependent on NCBI isolation-source metadata. [^plant_microbiome_ecotypes] The broader plant-associated census contained 7,995 genomes among 293,059 GTDB r214 genomes, and only 2.7% had plant-associated annotations, underscoring the limited coverage of isolation metadata. [^plant_microbiome_ecotypes]

The corrected analysis found weakly negative rather than complementary pathway profiles among co-occurring plant-associated genera, with Cohen's d approximately −0.39 for prevalence weighting; the BacDive–GapMind agreement supports the pathway measurements but does not independently validate the ecological complementarity inference. [^plant_microbiome_ecotypes]

## FW300-N2E3 metabolic utilization evidence

A cross-database study of *Pseudomonas* FW300-N2E3 **supports** BacDive as a complementary species-level utilization resource: 8 of 58 WoM exometabolites (14%) could be matched to *P. fluorescens* BacDive utilization data, compared with 28 of 58 (48%) matched to Fitness Browser conditions and 13 of 58 (22%) to GapMind predictions. [^fw300_metabolic_consistency] Among 7 WoM-produced metabolites with BacDive matches, 3/7 (43%) were utilized; this was not higher than the overall *P. fluorescens* baseline of 22/80 (27.5%; p = 0.40). [^fw300_metabolic_consistency]

BacDive was the variable component of the comparison: 3/7 matched metabolites were utilized, while tryptophan had 0+/50- utilization, trehalose 1+/5-, lysine 0+/3-, and glycine 0+/1-. [^fw300_metabolic_consistency] The tryptophan result is the strongest discordance between production and species-level utilization, but its interpretation is limited because BacDive aggregates *P. fluorescens* strains and does not establish that FW300-N2E3 itself cannot grow on tryptophan. [^fw300_metabolic_consistency] The sample-size gradient **refines** interpretation of BacDive negatives: tryptophan is high confidence at n=50, trehalose is moderate confidence at n=6, lysine is moderate confidence at n=3, and glycine is low confidence at n=1. [^fw300_metabolic_consistency]

Three metabolites provided four-way consistency across WoM production, Fitness Browser growth, BacDive utilization, and GapMind pathway prediction: malate was utilized by 49/49 strains (100%), arginine by 40/48 strains (83%), and valine by 1/1 strain. [^fw300_metabolic_consistency] These findings **support** using BacDive utilization records alongside, rather than as a substitute for, organism-specific fitness and pathway evidence; production and non-utilization are not intrinsically contradictory because exometabolomics can reflect overflow, byproduct release, or ecological secretion. [^fw300_metabolic_consistency]

FW300-N2E3 was isolated from groundwater at the Oak Ridge Field Research Center in an ENIGMA SFA context, and the study notes that *P. fluorescens* BacDive records span a broad clade identified under GTDB reclassification as *Pseudomonas_E fluorescens_E*. [^fw300_metabolic_consistency] BacDive counts use per-strain consensus, applying majority vote among duplicate records per strain, and compound coverage varies from 1 to 51 strains; raw records can therefore exceed the number of strains. [^fw300_metabolic_consistency]

BacDive represents culturable, described strains rather than the full diversity of environmental bacteria, and culture-collection bias may under-represent metal-tolerant extremophiles. [^bacdive_metal_validation] It is also biased toward well-studied organisms, including Pseudomonas and [escherichia-coli](escherichia-coli.md), while poorly studied species have sparse data. [^bacdive_phenotype_metal_tolerance] The Metal Fitness Atlas scores are genome-based predictions rather than direct metal-tolerance measurements, so these results remain phenotype-to-genome correlations rather than phenotype-to-phenotype measurements. [^bacdive_phenotype_metal_tolerance] The FW300-N2E3 comparison **refines** this limitation by showing that strain aggregation, taxonomy breadth, and sample size constrain species-level utilization inference. [^fw300_metabolic_consistency] The Agora analysis further **refines** it by showing that phenotype coverage is uneven across clades, with Cyanobacteriia represented by only n = 4 species. [^gene_function_ecological_agora] The plant analysis likewise shows that BacDive pathway validation is useful but that plant-linked strain coverage does not necessarily add genome assignments. [^plant_microbiome_ecotypes]

The cross-resistance analysis identifies metal concentration differences, unequal numbers of metal experiments, lack of non-metal stress controls, and non-independent organism sampling as limitations requiring concentration normalization, controls, and phylogenetic methods such as PGLS (phylogenetic generalized least squares). [^metal_cross_resistance]

BacDive–GTDB and cross-database analyses should therefore use live schema and identifier inspection rather than copied historical joins, because naming conventions and database contents can change; unmatched records, orphan pangenomes, and naming differences must not be interpreted as biological absence. [^pitfalls]

## Related pages

- [bacdive_metal_validation__REPORT](../summaries/bacdive_metal_validation__REPORT.md) — summary of the BacDive isolation-environment and metal-tolerance validation study. [^bacdive_metal_validation]
- [bacdive_phenotype_metal_tolerance__REPORT](../summaries/bacdive_phenotype_metal_tolerance__REPORT.md) — summary of the BacDive phenotype-signature and phylogenetic-confounding study. [^bacdive_phenotype_metal_tolerance]
- [berdl_data_atlas__REPORT](../summaries/berdl_data_atlas__REPORT.md) — inventory and cross-reference analysis placing BacDive among BERDL phenotype resources. [^berdl_data_atlas]
- [fw300_metabolic_consistency__REPORT](../summaries/fw300_metabolic_consistency__REPORT.md) — cross-database metabolic consistency analysis for *Pseudomonas* FW300-N2E3. [^fw300_metabolic_consistency]
- [gene_function_ecological_agora__REPORT](../summaries/gene_function_ecological_agora__REPORT.md) — GTDB-scale integration of BacDive phenotype profiles with clade-function and ecological analyses. [^gene_function_ecological_agora]
- [metal_cross_resistance__REPORT](../summaries/metal_cross_resistance__REPORT.md) — gene-resolution cross-resistance study and its underpowered BacDive isolation-environment validation. [^metal_cross_resistance]
- [plant_microbiome_ecotypes__REPORT](../summaries/plant_microbiome_ecotypes__REPORT.md) — plant-associated ecotypes, compartment-specific functions, and BacDive–GapMind pathway validation. [^plant_microbiome_ecotypes]
- [pitfalls](../summaries/pitfalls.md) — database naming, utilization coding, identifier reconciliation, and interpretation safeguards relevant to BacDive integration. [^pitfalls]
- [environmental-resistome](../concepts/environmental-resistome.md) — ecological validation and genome-encoded predictors of metal tolerance. [^bacdive_metal_validation][^bacdive_phenotype_metal_tolerance][^metal_cross_resistance]
- [pangenome-integration](../concepts/pangenome-integration.md) — BacDive–GTDB species matching and pangenome coverage. [^bacdive_metal_validation][^bacdive_phenotype_metal_tolerance]
- [multi-omics-integration](../concepts/multi-omics-integration.md) — integration of genome-derived scores with curated isolation and utilization phenotypes. [^bacdive_metal_validation]
- [ecotype-environment-gene-content](../concepts/ecotype-environment-gene-content.md) — phenotype anchors for interpreting clade-specific gene-function and environmental patterns. [^gene_function_ecological_agora][^plant_microbiome_ecotypes]
- [condition-specific-fitness](../concepts/condition-specific-fitness.md) — need for per-metal analyses and matched-strain experiments to test metal-specific tolerance. [^bacdive_phenotype_metal_tolerance]
- [metabolic-model-gapfilling](../concepts/metabolic-model-gapfilling.md) — BacDive utilization records and GapMind pathway predictions as complementary metabolic evidence. [^plant_microbiome_ecotypes]
- [metal-fitness-atlas](metal-fitness-atlas.md) — source of the genome-based metal-tolerance scores used in the comparisons. [^bacdive_metal_validation][^bacdive_phenotype_metal_tolerance]

[^bacdive_metal_validation]: [bacdive metal validation](../summaries/bacdive_metal_validation__REPORT.md)
[^berdl_data_atlas]: [berdl data atlas](../summaries/berdl_data_atlas__REPORT.md)
[^pitfalls]: [pitfalls](../summaries/pitfalls.md)
[^plant_microbiome_ecotypes]: [plant microbiome ecotypes](../summaries/plant_microbiome_ecotypes__REPORT.md)
[^bacdive_phenotype_metal_tolerance]: [bacdive phenotype metal tolerance](../summaries/bacdive_phenotype_metal_tolerance__REPORT.md)
[^gene_function_ecological_agora]: [gene function ecological agora](../summaries/gene_function_ecological_agora__REPORT.md)
[^metal_cross_resistance]: [metal cross resistance](../summaries/metal_cross_resistance__REPORT.md)
[^fw300_metabolic_consistency]: [fw300 metabolic consistency](../summaries/fw300_metabolic_consistency__REPORT.md)
