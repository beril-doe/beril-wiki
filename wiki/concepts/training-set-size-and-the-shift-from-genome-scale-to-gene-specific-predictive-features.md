---
type: "Concept"
description: "How the number of genomes and genome-condition pairs determines whether interpretable models learn genome-size proxies or condition-specific genes, including correlated-feature grouping in SHAP attribution; it stops at external validation of the features."
sources: ["summaries/genotype_to_phenotype_enigma__REPORT.md"]
---
# Training-set size and the shift from genome-scale to gene-specific predictive features

In the genotype_to_phenotype_enigma report, the number of training examples changed what an interpretable growth model learned. With 7 strains, SHAP (Shapley additive explanations) attribution was dominated by condition class (45.9%) and genome-scale features (25.3%). [src: genotype_to_phenotype_enigma] With 46K training pairs, condition-specific catabolic genes emerged. [src: genotype_to_phenotype_enigma] See also [[summaries/genotype_to_phenotype_enigma__REPORT]].

## Literature Context

The two candidate papers address genome-based phenotype prediction in bacteria, and neither tests how training-set size changes which features a model uses. One study compared growth dynamics of clinical and environmental bacterial isolates with their phylogenetic relationships. It found little correlation between genetic distance and phenotypic distance, which it describes as underscoring the challenge of inferring phenotypes from genomics [PMID 32747578](https://pubmed.ncbi.nlm.nih.gov/32747578/). The abstract reports that growth dynamics alone could predict antibiotic responses. That finding concerns identity and traits, not interpretable gene-level attribution.

The second study curated optimal growth temperature (OGT) and genomic data for 2,869 bacterial species. It found that models built on genome composition were less accurate for species whose OGT shifted rapidly from their ancestors, including psychrophiles. Adding gene presence/absence information tied to those rapid shifts improved psychrophile prediction [PMID 41930963](https://pubmed.ncbi.nlm.nih.gov/41930963/). The authors frame this as integrating long-term adaptation, seen in genome composition, with short-term adaptation, seen in specific genes. They suggest the framework may apply to other microbial physiological phenotypes [PMID 41930963](https://pubmed.ncbi.nlm.nih.gov/41930963/).

The genotype_to_phenotype_enigma report is consistent with this picture in a loose, qualitative way. Its small model, trained on 7 strains and 486 genome-condition pairs and reaching AUC 0.633, was dominated by condition class (45.9%) and a 63-feature genome-scale axis (25.3%). Its larger model, trained on 46K pairs, shifted toward condition-specific catabolic genes such as rbsC and pcaB. This parallels the finding that genome-wide properties carry broad signal while specific gene presence adds trait-specific signal [PMID 41930963](https://pubmed.ncbi.nlm.nih.gov/41930963/). The report's weak concordance with Fitness Browser (1.19× enrichment) also fits the caution that genetic relatedness maps imperfectly onto phenotype [PMID 32747578](https://pubmed.ncbi.nlm.nih.gov/32747578/).

The candidates do not cover the report's central claims. These are the dependence of attribution on training-set size, the estimate that the shift needs hundreds of genomes per condition, and the grouping of correlated KOs at |r|>0.8 for SHAP. They are novel relative to these candidates. The two models also differ in more than size: the small one is counted in strains (7) and pairs (486), and the large one is counted only in pairs (46K). The comparison therefore does not isolate the number of genomes from the number of genome-condition pairs. It rests on one report with two models, so the size-dependence claim remains an unreplicated hypothesis. The OGT study is a different task, species-level regression on 2,869 species, so it cannot confirm or contradict the report's thresholds.

## The small-corpus model: genome scale

The initial analysis used leave-one-strain-out validation on 7 strains: 4 Pseudomonas_E and 1 each of Cupriavidus, Acidovorax and Pedobacter. [src: genotype_to_phenotype_enigma] It did not test cross-genus generalization, per-condition prediction quality, or condition-specific features. [src: genotype_to_phenotype_enigma] Nested LightGBM GBDT (gradient boosted decision tree) models with leave-one-strain-out cross-validation on 486 pairs reached AUC (area under curve) 0.633 for binary growth with the full feature set. [src: genotype_to_phenotype_enigma]

SHAP analysis of this model was dominated by a 63-feature genome-scale axis, which held 25.3% of total SHAP, and by condition class, which held 45.9%. [src: genotype_to_phenotype_enigma] The axis comprises genome size, gene count, operons, rRNA/tRNA and co-inherited KOs (KEGG orthologs). [src: genotype_to_phenotype_enigma] Specific KO blocks for membrane adaptation, tRNA modification, aromatic catabolism and flagellar motility contributed only about 2% each, though the report calls them biologically coherent. [src: genotype_to_phenotype_enigma] The report summarizes the model as learning that "big genomes grow on amino acids". It calls this biologically real but not the condition-specific prediction needed for practical use. [src: genotype_to_phenotype_enigma]

## The large-corpus model: condition-specific genes

With the full corpus of 46K pairs (NB07), SHAP importance shifted to condition-specific catabolic genes, unlike the n=7 model. [src: genotype_to_phenotype_enigma] The named genes are:

- K03762, proP, a proline/betaine transporter
- K10440, rbsC, a ribose transporter
- K01857, pcaB, protocatechuate cycloisomerase for aromatic catabolism
- K13633, ftrA, an AraC-family regulator
- K01214, treX, isoamylase for complex carbohydrates [src: genotype_to_phenotype_enigma]

The report presents this as a qualitative shift and says the n=7 to n=46K comparison quantifies the corpus size needed for it. [src: genotype_to_phenotype_enigma] It concludes that the shift needs hundreds of genomes per condition, not a handful. [src: genotype_to_phenotype_enigma] The report calls the features mechanistically coherent: the ribose transporter predicts ribose growth and protocatechuate cycloisomerase predicts aromatic catabolism. [src: genotype_to_phenotype_enigma] It also reports only weak concordance with Fitness Browser (1.19× enrichment). Its explanation is that gene presence across genera and gene essentiality within one strain are different biological questions. [src: genotype_to_phenotype_enigma]

## Correlated-feature grouping in SHAP

Naive SHAP on 4,305 KOs splits credit across correlated gene blocks. [src: genotype_to_phenotype_enigma] The report therefore groups features correlated at |r|>0.8 into connected-component blocks. [src: genotype_to_phenotype_enigma] This grouping exposes the 63-feature genome-scale axis that dominates with small training sets. [src: genotype_to_phenotype_enigma] SHAP summed within a group gives group-level importance and avoids credit-splitting among redundant features. Individual SHAP values inside a group should be read as "this group matters", not "this specific KO matters". [src: genotype_to_phenotype_enigma]

## Open Directions

- Train on subsamples of the 46K-pair corpus (for example 7, 100, 1,000 and 10,000 pairs) and track the genome-scale share of grouped SHAP. This would replace the two-point comparison with a curve and locate the transition.
- Test cross-genus generalization and per-condition prediction quality in the large model, since the initial analysis tested neither. Compare the splits with [[entities/xgboost-with-phylogenetic-blocked-cross-validation]].
- Apply the |r|>0.8 grouping to the NB07 model, so that the condition-specific KOs are also reported at group level.
- Examine why concordance with Fitness Browser is weak (1.19× enrichment), for example by restricting to conditions with many genomes.
