---
type: "Finding"
description: "Among 6,760 PA genomes (5,199 with metadata), 1,796 are from lung/respiratory or CF sources, and seven GapMind pathways differ significantly (FDR < 0.05) between lung and non-lung PA, all carbon-source pathways with lower scores in lung PA, such as sorbitol (\u22120.165), mannitol (\u22120.204) and gluconate (\u22120.185); the report infers from this lung metabolic streamlining under relaxed selection, which is an evolutionary interpretation rather than a measured loss."
finding_id: "cf_formulation_design--460ed03a"
result: "inference"
source: "cf_formulation_design"
quantities: [{"value": "1,796", "what": "lung/respiratory or CF PA genomes", "unit": "genomes", "denominator": "6,760 PA genomes (5,199 with metadata)", "scope": "pangenome"}, {"value": "Seven", "what": "GapMind pathways differing between lung and non-lung PA", "unit": "pathways", "denominator": "", "scope": "FDR < 0.05"}, {"value": "\u22120.204", "what": "mannitol pathway score difference, lung vs non-lung PA", "unit": "", "denominator": "", "scope": "GapMind"}]
caveat: "Retention of amino acid catabolic pathways at 97%+ conservation supports a prediction, not a demonstration, that PA strains will respond similarly to the formulation."
first_added: "2026-10-27"
source_hash: "06931c95e1ee4b3b3a4a95563e11b057ffbada9817b91426fd15b4be9ef75bfe"
---
# Lung P. aeruginosa genomes score lower on sugar pathways than non-lung genomes

Among 6,760 PA genomes (5,199 with metadata), 1,796 are from lung/respiratory or CF sources, and seven GapMind pathways differ significantly (FDR < 0.05) between lung and non-lung PA, all carbon-source pathways with lower scores in lung PA, such as sorbitol (−0.165), mannitol (−0.204) and gluconate (−0.185); the report infers from this lung metabolic streamlining under relaxed selection, which is an evolutionary interpretation rather than a measured loss. [src: cf_formulation_design]

## Key figures

- **1,796 genomes**: lung/respiratory or CF PA genomes (denominator 6,760 PA genomes (5,199 with metadata); scope pangenome) [src: cf_formulation_design]
- **Seven pathways**: GapMind pathways differing between lung and non-lung PA (scope FDR < 0.05) [src: cf_formulation_design]
- **−0.204**: mannitol pathway score difference, lung vs non-lung PA (scope GapMind) [src: cf_formulation_design]

## Evidence

> Among 6,760 PA genomes (5,199 with metadata), 1,796 are from lung/respiratory or CF sources. Seven GapMind pathways differ significantly (FDR < 0.05) between lung and non-lung PA — and all are **carbon source pathways that lung PA is losing**: sorbitol (−0.165), mannitol (−0.204), gluconate (−0.185). Lung PA is undergoing metabolic streamlining: in the amino acid-rich sputum environment, sugar catabolism is dispensable and under relaxed selection. This validates that PA's amino acid dependence is not just a preference — it is an **evolutionary adaptation**. [src: cf_formulation_design]

From the report [[summaries/cf_formulation_design__REPORT]].

## Caveat

Retention of amino acid catabolic pathways at 97%+ conservation supports a prediction, not a demonstration, that PA strains will respond similarly to the formulation. [src: cf_formulation_design]

> However, since all strain groups retain the same amino acid catabolic pathways (97%+ conservation, NB11), the extra genes are likely conditionally expressed accessory functions (prophages, mobile elements, niche-specific adaptations) that affect virulence and persistence rather than amino acid growth rate. Within-species genome size variation is a much weaker predictor of growth rate than cross-species variation (Vieira-Silva & Rocha 2010). We therefore predict that **PA strains will respond similarly to our formulation**, because the competitive targets — amino acid catabolism — are invariant across the species. Where PA strains are expected to differ is in virulence, antibiotic resistance, and biofilm properties — factors that matter for disease severity but not for the metabolic competition mechanism our formulation exploits. [src: cf_formulation_design]

## Other caveats in this report

- Competitive metabolic exclusion is the study's working theory; the listed CF-sputum amino acids are proposed shared resources. [src: cf_formulation_design]
- Selective prebiotic biomass pre-loading is explicitly a hypothesis. [src: cf_formulation_design]
- GTDB taxonomy is used; Pseudomonas_E is a non-aeruginosa clade and should not be merged with P. aeruginosa. [src: cf_formulation_design]
- The three named organisms have the largest reported isolate counts; pathogen oversampling limits interpretation of collection frequencies as natural prevalence. [src: cf_formulation_design]
- Acinetobacter baumannii and Klebsiella pneumoniae are other named reporter pathogens; their distinct profiles limit generalization of the PA14-targeted formulation. [src: cf_formulation_design]
