---
type: "Summary"
description: "Summary of the project BacDive Phenotype Signatures of Metal Tolerance."
doc_type: "short"
full_text: "sources/bacdive_phenotype_metal_tolerance__REPORT.md"
---
# BacDive Phenotype Signatures of Metal Tolerance

This report asks whether classical BacDive phenotypes (Gram stain, oxidase, urease, oxygen tolerance and others) predict metal tolerance across bacterial species. Seven of the ten phenotype features tested pass FDR correction (false discovery rate, q < 0.05). [src: bacdive_phenotype_metal_tolerance] Gram-negative species score higher than Gram-positive species, the largest effect tested (Cohen's d = -0.61, n = 3,272 species). [src: bacdive_phenotype_metal_tolerance] Urease-positive species score lower (d = -0.18, p < 1e-5), opposite to the nickel-import-based prediction. [src: bacdive_phenotype_metal_tolerance] Taxonomy alone explains 35.4% of metal-tolerance variance, and adding phenotype yields R² = 34.5%, slightly worse than taxonomy alone. [src: bacdive_phenotype_metal_tolerance] The report concludes that the phenotype signal is entirely captured by phylogenetic structure [src: bacdive_phenotype_metal_tolerance], and that phenotype features add nothing beyond taxonomy (Delta R² = -0.009). [src: bacdive_phenotype_metal_tolerance] It describes this as the first large-scale test of BacDive phenotypes as metal tolerance predictors, covering 5,647 species and 10 phenotype features cross-referenced to Metal Fitness Atlas genome-based scores. [src: bacdive_phenotype_metal_tolerance] See [[concepts/phylogenetic-confounding-of-phenotype-metal-tolerance-associations]] and [[entities/bacdive]].

Of six pre-stated hypotheses, H1a (Gram-negative tolerance) is supported univariately but phylogenetically confounded [src: bacdive_phenotype_metal_tolerance]; H1b (anaerobes) is not supported [src: bacdive_phenotype_metal_tolerance]; H1c (metabolite breadth) is not supported [src: bacdive_phenotype_metal_tolerance]; H1d (catalase) is marginally supported [src: bacdive_phenotype_metal_tolerance]; H1e (urease and nickel) is reversed [src: bacdive_phenotype_metal_tolerance]; and H1f (H₂S) is unreliable. [src: bacdive_phenotype_metal_tolerance] A direct check against Fitness Browser organisms covers 12 organisms that match BacDive by taxonomy ID. [src: bacdive_phenotype_metal_tolerance]

## Key Findings

### Univariate associations
Seven BacDive phenotype features pass FDR correction at q < 0.05. [src: bacdive_phenotype_metal_tolerance]

The BacDive analysis tested 10 phenotype features (8 binary, 2 continuous). [src: bacdive_phenotype_metal_tolerance]

| Feature | Effect | n species | FDR q |
|---|---|---|---|
| Gram stain (+) | d = -0.610 | 3,272 | 4.0e-60 [src: bacdive_phenotype_metal_tolerance] |
| Oxidase (+) | d = +0.530 | 1,799 | 1.3e-24 [src: bacdive_phenotype_metal_tolerance] |
| Motility | d = +0.345 | 3,138 | 7.2e-23 [src: bacdive_phenotype_metal_tolerance] |
| Urease (+) | d = -0.175 | 3,035 | 9.1e-06 [src: bacdive_phenotype_metal_tolerance] |
| Enzyme breadth | rho = -0.058 | 3,746 | 8.2e-04 [src: bacdive_phenotype_metal_tolerance] |
| Nitrate reduction | d = +0.100 | 3,088 | 7.4e-03 [src: bacdive_phenotype_metal_tolerance] |
| Catalase (+) | d = +0.104 | 2,930 | 4.1e-02 [src: bacdive_phenotype_metal_tolerance] |

H₂S production is not significant (d = -0.867, n = 880, FDR q = 7.3e-02). [src: bacdive_phenotype_metal_tolerance] Metabolite breadth is not significant (rho = -0.013, n = 3,930, FDR q = 4.7e-01). [src: bacdive_phenotype_metal_tolerance] Acetate utilization is not significant (d = +0.005, n = 422, FDR q = 7.9e-01). [src: bacdive_phenotype_metal_tolerance] The H₂S effect size is unreliable because only 8 negative controls exist, and it is likely inflated by small-sample bias. [src: bacdive_phenotype_metal_tolerance] Only 8 H₂S-negative species occur in the matched set, so d = -0.87 is unreliable. [src: bacdive_phenotype_metal_tolerance]

### Gram stain
Gram-negative species have higher metal tolerance scores than Gram-positive species (Cohen's d = -0.61, p < 1e-60, n = 3,272 species), the largest phenotype effect tested. [src: bacdive_phenotype_metal_tolerance]

The report describes the Gram-negative outer membrane as a permeability barrier restricting metal cation uptake, making the association mechanistically plausible but phylogenetically confounded. [src: bacdive_phenotype_metal_tolerance] It calls the advantage real but predictively indistinguishable from being a Proteobacterium. [src: bacdive_phenotype_metal_tolerance]

The Gram-stain association cannot be tested within taxonomic classes and is almost entirely a between-lineage signal involving Actinomycetes versus Proteobacteria. [src: bacdive_phenotype_metal_tolerance] The matched data contain no Gram-positive Proteobacteria and no Gram-negative Actinomycetes. [src: bacdive_phenotype_metal_tolerance]

### Urease
Urease-positive species have lower metal tolerance (d = -0.18, p < 1e-5), opposite to the nickel-import-based prediction. [src: bacdive_phenotype_metal_tolerance]

The urease effect is driven by Actinomycetes (d = -0.59, p < 1e-16), whose urease-positive species form a distinct low-metal-score subgroup. [src: bacdive_phenotype_metal_tolerance] The report attributes the surprising urease-negative, higher-tolerance association entirely to Actinomycetes. [src: bacdive_phenotype_metal_tolerance]

Within Gammaproteobacteria, the urease effect disappears (d = +0.08, ns). [src: bacdive_phenotype_metal_tolerance]

Within Bacilli, the urease effect disappears (d = +0.06, ns). [src: bacdive_phenotype_metal_tolerance] Within other classes, the report finds the urease effect is zero. [src: bacdive_phenotype_metal_tolerance]

Urease-positive bacteria require nickel import and handling machinery, so they might be expected to tolerate nickel. [src: bacdive_phenotype_metal_tolerance] The report says this is not a true paradox, because urease positivity correlates with Actinomycetes and other lineages with fewer metal resistance genes overall. [src: bacdive_phenotype_metal_tolerance] It adds that the nickel-handling machinery is narrowly specific to nickel and does not confer general metal tolerance. [src: bacdive_phenotype_metal_tolerance] It also says tight coupling between urease activity and nickel efflux makes nickel homeostasis in urease producers a balancing act, not a broad tolerance mechanism. [src: bacdive_phenotype_metal_tolerance]

### Catalase
Overall, catalase-positive species have slightly higher metal scores (d = +0.10), which marginally supports H1d. [src: bacdive_phenotype_metal_tolerance]

Within Actinomycetes, catalase-negative species score higher (d = -0.62, p < 1e-5). [src: bacdive_phenotype_metal_tolerance]

Within Gammaproteobacteria, catalase-negative species score higher (d = -0.49, p = 0.004). [src: bacdive_phenotype_metal_tolerance]

Within Betaproteobacteria, catalase-negative species score higher (d = -0.51, p = 0.006). [src: bacdive_phenotype_metal_tolerance]

The report reads the overall positive effect as a between-class composition artifact, the same Simpson's paradox pattern as urease. [src: bacdive_phenotype_metal_tolerance]

### Oxygen tolerance
Among 3,751 species with oxygen tolerance data, the anaerobe–aerobe metal-tolerance difference is negligible (d = -0.016, p = 0.55). [src: bacdive_phenotype_metal_tolerance]

Facultative anaerobes have the highest mean metal score (0.221), versus aerobes (0.216) and anaerobes (0.215). [src: bacdive_phenotype_metal_tolerance]

The comparison across all three groups is marginally significant by Kruskal-Wallis (H = 8.53, p = 0.014), but the report calls the effect biologically trivial. [src: bacdive_phenotype_metal_tolerance]

### Metabolic versatility
The report did not support the hypothesis that metabolically versatile organisms harbor more resistance genes. [src: bacdive_phenotype_metal_tolerance]

Metabolite utilization breadth shows no correlation with metal score (rho = -0.01), which the report tentatively attributes to metabolic versatility operating in different genomic neighborhoods from metal resistance. [src: bacdive_phenotype_metal_tolerance]

### Prediction: taxonomy absorbs phenotype
Taxonomy alone (phylum/class/order) explains 35.4% of metal-tolerance variance, phenotype alone explains 16.3%, and their combination yields R² = 34.5%, slightly worse than taxonomy alone. [src: bacdive_phenotype_metal_tolerance]

Adding phenotype to the taxonomy model lowers predictive power slightly (delta R² = -0.009), which the report reads as phenotypes being noisier proxies for taxonomy, not independent predictors. [src: bacdive_phenotype_metal_tolerance]

Phenotype features alone capture signal at R² = 0.16. [src: bacdive_phenotype_metal_tolerance] Models used 5-fold phylogenetic-blocked cross-validation (CV). [src: bacdive_phenotype_metal_tolerance] See [[entities/xgboost-with-phylogenetic-blocked-cross-validation]].

| Model | R² | RMSE | n | Features |
|---|---|---|---|---|
| Gene count only | 0.063 [src: bacdive_phenotype_metal_tolerance] | 0.045 | 3,994 | 1 |
| Phenotype only | 0.163 [src: bacdive_phenotype_metal_tolerance] | 0.043 | 3,994 | 13 |
| Taxonomy only | 0.354 [src: bacdive_phenotype_metal_tolerance] | 0.038 | 3,994 | 3 |
| Taxonomy + phenotype | 0.345 [src: bacdive_phenotype_metal_tolerance] | 0.038 | 3,994 | 16 |
| Full (all combined) | 0.633 [src: bacdive_phenotype_metal_tolerance] | 0.028 | 3,994 | 17 |

In the BacDive model, n_metal_clusters is the number of metal resistance gene clusters, and the report identifies genome-encoded metal resistance repertoire as the true predictor. [src: bacdive_phenotype_metal_tolerance] Gene content from the Metal Fitness Atlas explains more variance than all phenotype features combined and substantially more than taxonomy alone. [src: bacdive_phenotype_metal_tolerance] The full model reaches R² = 0.63, with gene count adding delta R² = +0.28 over taxonomy alone. [src: bacdive_phenotype_metal_tolerance] Shapley additive explanations (SHAP) importance in the full model ranks taxonomic class/order codes and n_metal_clusters as the top predictors. [src: bacdive_phenotype_metal_tolerance] Phenotype features contribute minimally to individual predictions once taxonomy is included, which the report interprets as classical phenotypes being phylogenetic proxies. [src: bacdive_phenotype_metal_tolerance] The report notes that this aligns with Schwan et al. (2023), who found strong genotype-phenotype concordance for metal resistance genes in Salmonella and E. coli. [src: bacdive_phenotype_metal_tolerance] It also cites Goberna & Verdú (2016), whose meta-analysis showed that bacterial trait-environment associations routinely reflect shared ancestry. [src: bacdive_phenotype_metal_tolerance] It cites Van Assche & Álvarez (2017), who found phylogenetic signal up to λ = 0.98 for chemical sensitivity traits in Acinetobacter. [src: bacdive_phenotype_metal_tolerance] See [[concepts/genome-encoded-metal-resistance-repertoire-versus-phenotype-as-predictor-of-metal-tolerance]].

### Hypothesis outcomes
- H1a, predicting higher metal scores in Gram-negative species, is supported univariately (d = -0.61) but phylogenetically confounded. [src: bacdive_phenotype_metal_tolerance]
- H1b, predicting better redox-metal tolerance in anaerobes, is not supported (d = -0.02, ns). [src: bacdive_phenotype_metal_tolerance]
- H1c, predicting greater tolerance with broader metabolism, is not supported (rho = -0.01, ns). [src: bacdive_phenotype_metal_tolerance]
- H1d, predicting catalase-positive tolerance of Cu, Cr, and Fe, is marginally supported (d = +0.10, q = 0.04). [src: bacdive_phenotype_metal_tolerance]
- H1e, predicting better nickel handling by urease-positive species, is reversed (d = -0.18) and driven by Actinomycetes. [src: bacdive_phenotype_metal_tolerance]
- H1f, predicting H₂S-producer tolerance of Zn, Cu, and Cd, is unreliable (d = -0.87) because only 8 negatives likely inflate the effect. [src: bacdive_phenotype_metal_tolerance]

### Direct Fitness Browser validation
Twelve Fitness Browser organisms match BacDive by taxonomy ID, representing 6 unique species: Cupriavidus basilensis, Methanococcus maripaludis, Ralstonia solanacearum, Pseudomonas simiae, Azospirillum brasilense, and Pseudomonas fluorescens. [src: bacdive_phenotype_metal_tolerance]

All Gram-typed organisms in this validation are Gram-negative, preventing within-set testing of H1a. [src: bacdive_phenotype_metal_tolerance]

All urease-typed organisms are urease-negative yet routinely tested against nickel, which the report describes as consistent with urease status not predicting metal tolerance at pangenome scale. [src: bacdive_phenotype_metal_tolerance] See [[entities/fitness-browser]].

The single anaerobe, Methanococcus, has only 1 metal tested versus 4–5 for aerobes, and the report considers n = 1 not interpretable. [src: bacdive_phenotype_metal_tolerance]

## Data and Methods

The BacDive bridge contains 97,334 strains. [src: bacdive_phenotype_metal_tolerance] The analysis matched 37,368 strains (38.4%) to pangenome and metal score. [src: bacdive_phenotype_metal_tolerance] It includes 5,647 unique GTDB species. [src: bacdive_phenotype_metal_tolerance] It includes 3,994 species with ≥5 phenotype features. [src: bacdive_phenotype_metal_tolerance] It includes 9 taxonomic classes with ≥50 species. [src: bacdive_phenotype_metal_tolerance] See [[concepts/coverage-and-bias-in-linking-strain-phenotype-databases-to-pangenomes]].

Phenotype features for 97K strains came from the kescience_bacdive tables strain, physiology, metabolite_utilization, enzyme, isolation, taxonomy and sequence_info. [src: bacdive_phenotype_metal_tolerance] Genome-based metal tolerance predictions for 27,702 species came from kbase_ke_pangenome via Metal Fitness Atlas scores. [src: bacdive_phenotype_metal_tolerance] The 12 direct Fitness Browser–BacDive organism matches and metal experiment metadata came from kescience_fitnessbrowser. [src: bacdive_phenotype_metal_tolerance]

Coverage per feature (BacDive strains, matched strains, species with metal score):

| Feature | Strains | Matched | Species |
|---|---|---|---|
| Isolation source | 43,378 | 22,581 | 4,531 [src: bacdive_phenotype_metal_tolerance] |
| Metabolite breadth | 29,784 | 16,454 | 3,930 [src: bacdive_phenotype_metal_tolerance] |
| Enzyme breadth | 28,836 | 16,005 | 3,746 [src: bacdive_phenotype_metal_tolerance] |
| Oxygen tolerance | 23,252 | 11,708 | 3,751 [src: bacdive_phenotype_metal_tolerance] |
| Gram stain | 15,194 | 7,411 | 3,272 [src: bacdive_phenotype_metal_tolerance] |
| Motility | 13,759 | 6,474 | 3,138 [src: bacdive_phenotype_metal_tolerance] |
| Nitrate reduction | 20,726 | 11,357 | 3,088 [src: bacdive_phenotype_metal_tolerance] |
| Urease | 24,438 | 14,343 | 3,035 [src: bacdive_phenotype_metal_tolerance] |
| Catalase | 15,295 | 7,876 | 2,930 [src: bacdive_phenotype_metal_tolerance] |
| Oxidase | 7,813 | 5,014 | 1,799 [src: bacdive_phenotype_metal_tolerance] |
| H₂S production | 5,254 | 2,611 | 880 [src: bacdive_phenotype_metal_tolerance] |
| Acetate utilization | 1,980 | 475 | 422 [src: bacdive_phenotype_metal_tolerance] |

## Caveats and Open Work

- The Gram-stain effect cannot be tested within classes. [src: bacdive_phenotype_metal_tolerance]
- The urease effect vanishes within Gammaproteobacteria and Bacilli, which the report takes as further evidence of phylogenetic confounding. [src: bacdive_phenotype_metal_tolerance]
- The H₂S estimate rests on 8 negatives and is likely inflated. [src: bacdive_phenotype_metal_tolerance]
- The direct Fitness Browser check has no Gram-positive organisms. [src: bacdive_phenotype_metal_tolerance] The report considers the 12-organism validation underpowered. [src: bacdive_phenotype_metal_tolerance]
- Metal Fitness Atlas scores are genome-based predictions, not direct measurements. Controlling for n_metal_clusters in partial correlations mitigates circularity, but the associations remain phenotype-to-genome, not phenotype-to-phenotype. [src: bacdive_phenotype_metal_tolerance]
- Species-name matching reaches only 38.4% (5,647/27,702 GTDB species). GCA accession matching could recover additional links but was not implemented. [src: bacdive_phenotype_metal_tolerance]
- BacDive testing is biased toward well-studied organisms such as Pseudomonas and E. coli, while poorly studied species have sparse data. [src: bacdive_phenotype_metal_tolerance]
- The analysis uses only measured phenotype values. [src: bacdive_phenotype_metal_tolerance]
- The report suggests adding GCA accession matching, which could recover 10–30% more species. [src: bacdive_phenotype_metal_tolerance]
- The report suggests including BacDive's ML-predicted Gram stain, motility and oxygen tolerance, which could raise coverage substantially. [src: bacdive_phenotype_metal_tolerance] This would introduce model-dependent bias. [src: bacdive_phenotype_metal_tolerance]
- The report proposes using PGLS (phylogenetic generalized least squares) or phylogenetic PCA (principal component analysis) to formally remove phylogenetic signal before testing phenotype-metal associations. [src: bacdive_phenotype_metal_tolerance]
- The report proposes per-metal phenotype analysis, such as catalase for copper and urease for nickel, instead of composite scores. [src: bacdive_phenotype_metal_tolerance] This would require per-metal scores for the 27K species. [src: bacdive_phenotype_metal_tolerance]
- The report proposes testing the H₂S-to-chalcophilic-metal hypothesis (d = -0.87, underpowered) with sulfate-reducing bacteria under zinc/copper challenge. [src: bacdive_phenotype_metal_tolerance]
- The report proposes per-metal fitness profiling of urease+ versus urease- bacteria from the same class, ideally Gammaproteobacteria, where the pangenome-scale urease effect is near zero. [src: bacdive_phenotype_metal_tolerance]
- The report proposes RB-TnSeq (random barcode transposon sequencing) with matched urease+/- strains under nickel versus other metals to test nickel-specific tolerance directly. [src: bacdive_phenotype_metal_tolerance]

> **Erratum.** The report gives 38.4% for two different denominators. 37,368 of 97,334 matched strains is 38.4%; 5,647 of 27,702 GTDB species, the figure this sentence uses, is about one fifth, roughly half what the percentage suggests. [src: bacdive_phenotype_metal_tolerance]

## Slots Into

- [[concepts/phylogenetic-confounding-of-phenotype-metal-tolerance-associations]]: Gram stain and urease effects vanish or cannot be tested within classes, and catalase reverses within classes. [src: bacdive_phenotype_metal_tolerance]
- [[concepts/genome-encoded-metal-resistance-repertoire-versus-phenotype-as-predictor-of-metal-tolerance]]: adding n_metal_clusters boosts the full model to R² = 0.63. [src: bacdive_phenotype_metal_tolerance]
- [[concepts/metabolic-versatility-oxygen-tolerance-and-metal-tolerance]]: the anaerobe–aerobe difference is negligible (d = -0.016). [src: bacdive_phenotype_metal_tolerance]
- [[concepts/coverage-and-bias-in-linking-strain-phenotype-databases-to-pangenomes]]: 37,368 strains (38.4%) matched to pangenome and metal score. [src: bacdive_phenotype_metal_tolerance]
