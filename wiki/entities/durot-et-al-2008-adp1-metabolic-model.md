---
type: "Dataset"
description: "Genome-scale metabolic model of Acinetobacter baylyi ADP1 providing FBA predictions."
sources: ["summaries/adp1_triple_essentiality__REPORT.md", "summaries/aromatic_catabolism_network__REPORT.md"]
aliases: ["ADP1 FBA model", "ModelSEED ADP1 model"]
---
# Durot et al. 2008 ADP1 metabolic model

The Durot et al. 2008 ADP1 metabolic model is the source of flux balance analysis (FBA) predictions for Acinetobacter baylyi ADP1 in the ADP1 reports. [src: adp1_triple_essentiality] Also known as the ADP1 FBA model or ModelSEED ADP1 model. The evidence below comes from two project reports.

## Key facts

- The adp1_triple_essentiality report cites Durot et al. (2008), "Iterative reconstruction of a global metabolic model of *Acinetobacter baylyi* ADP1 using high-throughput growth phenotype and gene essentiality data" (*BMC Systems Biology* 2:85), as the source of FBA metabolic-model predictions for both studies. [src: adp1_triple_essentiality]
- That report builds on the Durot et al. (2008) FBA metabolic model. [src: adp1_triple_essentiality]
- It attributes an original report of ~75% FBA-TnSeq concordance to Durot et al. (2008). [src: adp1_triple_essentiality]
- Minimal-media predictions used `minimal_media_class` for 866 genes. [src: adp1_triple_essentiality]
- Rich-media predictions used `rich_media_class` for 866 genes. [src: adp1_triple_essentiality]

See [[summaries/adp1_triple_essentiality__REPORT]] and [[concepts/concordance-of-genome-scale-metabolic-model-predictions-with-experimental-data]].

## Limits seen on aromatic substrates

In the aromatic_catabolism_network report, the model sees increased demand but misses the bottleneck. [src: aromatic_catabolism_network] See [[summaries/aromatic_catabolism_network__REPORT]] and [[concepts/systematic-blind-spots-of-flux-balance-models-for-condition-specific-requirements]].

- The model predicts 1.76× higher Complex I flux on aromatic substrates (0.55 vs 0.31). [src: aromatic_catabolism_network]
- It nonetheless predicts 0% Complex I essentiality. [src: aromatic_catabolism_network]
- The report explains this by saying FBA models optimize for growth rate and can redistribute flux through alternative pathways. [src: aromatic_catabolism_network]
- It adds that Complex I is a single multi-subunit complex, where loss of any subunit eliminates function. This threshold effect is not captured by FBA's linear programming framework. [src: aromatic_catabolism_network]
- 30/51 quinate-specific genes have no FBA reaction mappings. Cofactor supply chains (pyrroloquinoline quinone (PQQ), iron) and regulatory genes are therefore invisible to the model. [src: aromatic_catabolism_network]
