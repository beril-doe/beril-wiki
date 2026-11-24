---
type: "Concept"
description: "Whether genes that predict growth across genera in a model are also genes whose disruption alters fitness in matched RB-TnSeq experiments, and why the two can disagree; it stops at model performance itself."
sources: ["summaries/genotype_to_phenotype_enigma__REPORT.md"]
---
# Concordance between cross-genus predictive genes and within-strain gene fitness

Genes that predict growth across genera in the bacterial growth model are only weakly concordant with genes whose disruption alters fitness in matched experiments in the [[entities/fitness-browser]]. The single report behind this page measured 1.19× enrichment and attributes the gap to the two datasets answering different biological questions. The evidence comes from one project (see [[summaries/genotype_to_phenotype_enigma__REPORT]]). The report's own statements about whether its validation is complete are not consistent with each other (see Limits). [src: genotype_to_phenotype_enigma]

## How concordance was measured

The report extracted top Shapley additive explanations (SHAP) features from the model trained on the full corpus. It expanded them into correlation-grouped gene blocks (connected components at |r|>0.8) and mapped them to Fitness Browser (FB) loci via fb_pangenome_link.tsv. It then tested whether those loci show significant fitness effects (|t|>4) in matched FB experiments, against a genome-wide random baseline. [src: genotype_to_phenotype_enigma] The expansion covered 57 KEGG orthologs (KOs), giving 335 FB loci. [src: genotype_to_phenotype_enigma] The report describes this as the first integration of ENIGMA growth curves with Fitness Browser gene fitness at condition-matched scale, with 486 pairs. [src: genotype_to_phenotype_enigma]

## Result: weak positive concordance

Condition-matched concordance was 18.7% against a 16.3% random baseline, reported as 1.19x enrichment. [src: genotype_to_phenotype_enigma] The report reads this as a weak positive: the model's features are barely more fitness-significant than random genes under matched conditions. [src: genotype_to_phenotype_enigma] Per-strain enrichment ranged from 1.72x in Cup4G11 to 0.83x in pseudo1_N1B4, which showed no enrichment. [src: genotype_to_phenotype_enigma]

## Why the two can disagree

The report's main explanation is that cross-genus gene presence (the prediction task) and within-strain gene essentiality (the FB fitness task) are different biological questions. [src: genotype_to_phenotype_enigma] The report says weak concordance does not make the features non-mechanistic. It points to coherent examples: a ribose transporter predicts ribose growth, and a protocatechuate cycloisomerase predicts aromatic catabolism. [src: genotype_to_phenotype_enigma] The report argues that K10440 (ribose transporter) predicting ribose growth shows the model uses condition-specific gene-level features. [src: genotype_to_phenotype_enigma] It also states that growth prediction (AUC, area under curve, 0.78 for amino acids) works through combinations of prevalence-variable KOs acting as genus-level proxies, not individually causal genes. [src: genotype_to_phenotype_enigma]

The report offers two possible mechanisms for the disagreement. The cited quotes do not say whether it tested them.
- A gene can be critical for prediction across genera, because genera lacking it do not grow on the substrate. Yet it may show no defect when disrupted in one strain, because that strain has redundant pathways or the lab condition differs from the growth assay. [src: genotype_to_phenotype_enigma]
- SHAP spreads credit across correlated features, so the causal gene may be a correlated neighbor of the highlighted one, which dilutes concordance. [src: genotype_to_phenotype_enigma]

## Limits

The report's statements about completeness conflict. It computed the 1.19× result with correlation-expanded blocks (57 KOs to 335 loci). [src: genotype_to_phenotype_enigma] Yet it also says hypothesis H3 (biological meaningfulness) is only partially addressable, because full FB concordance validation with correlation-group expansion "remains to be done". [src: genotype_to_phenotype_enigma]

## Open Directions

- Expand each top-SHAP KO to all KOs in its KEGG module and recompute concordance. This would separate "wrong feature, right pathway" from "wrong pathway".
- Clarify which correlation-group expansion was run for the 1.19× result and which remains undone, to resolve the inconsistency in the report's status for H3.
- Examine the per-strain spread (1.72x to 0.83x) against strain features such as pathway redundancy, to test whether redundancy explains missing fitness defects.
- Compare concordance for SHAP-highlighted KOs with that for their correlated neighbors, to test whether credit dilution hides the causal gene.
