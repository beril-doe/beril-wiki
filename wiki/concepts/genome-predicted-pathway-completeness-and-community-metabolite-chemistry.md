---
type: "Concept"
description: "Whether GapMind pathway completeness aggregated across taxa predicts community metabolite chemistry; stops at gene presence versus expression and annotation limits."
sources: ["summaries/discoveries.md", "summaries/nmdc_community_metabolic_ecology__REPORT.md"]
---
# Genome-predicted pathway completeness and community metabolite chemistry

Community-weighted GapMind pathway completeness correlates modestly with ambient amino acid levels across NMDC soil samples, in the direction the Black Queen Hypothesis (BQH) predicts. Only two of 13 testable pathways reach false discovery rate (FDR) significance. [src: discoveries] The data measure gene presence, not expression. [src: nmdc_community_metabolic_ecology] The evidence comes from a single analysis of public data. See [[concepts/black-queen-dynamics-in-amino-acid-biosynthesis]] and [[entities/gapmind]].

## What was tested

The analysis correlated community-weighted GapMind amino acid biosynthesis completeness with ambient amino acid metabolomics across 131 NMDC soil samples, using Spearman correlation. [src: discoveries] Completeness was the binary frac_complete metric, the fraction of community taxa with GapMind score ≥ 5 and no missing steps. [src: nmdc_community_metabolic_ecology] The report chose score 5 over frac_likely_complete (score ≥ 4). It argued that an unambiguous complete call maps directly onto the BQH prediction that taxa lacking a complete pathway depend on environmental supply. [src: nmdc_community_metabolic_ecology] frac_likely_complete was computed in NB03 for sensitivity comparisons. [src: nmdc_community_metabolic_ecology]

## Results

Eleven of 13 tested amino acid pathways trend in the BQH-predicted negative direction, with a binomial sign test p = 0.011. [src: discoveries] Negative r means lower community completeness co-occurs with higher ambient metabolite concentration. [src: discoveries]

Two pathways reach FDR significance. Leucine gives r = −0.390, q = 0.022, n = 62. [src: discoveries] Arginine gives r = −0.297, q = 0.049, n = 80. [src: discoveries] See also [[entities/leucine-biosynthesis]] and [[entities/arginine]]. Methionine has the largest effect (r = −0.496) but is underpowered and not significant (n = 18, q = 0.117). [src: discoveries]

In its literature comparison, the report gives leucine r = −0.33 and arginine r = −0.30 at environmental scale. It calls these weaker than, but directionally consistent with, Gowda et al. (2022), who showed that metabolite dynamics in model communities are predictable from gene content. [src: nmdc_community_metabolic_ecology] The report also calls H1 consistent with Mallick et al. (2019) and Noecker et al. (2016), who showed that community metabolomics is partially predictable from genomic or metagenomic functional profiles. [src: nmdc_community_metabolic_ecology] It says its pathway-level completeness predictor differs from flux-based or PICRUSt-style models but reaches comparable conclusions. [src: nmdc_community_metabolic_ecology]

The report claims this is the first demonstration that community-weighted pangenome completeness correlates with measured metabolite pools at landscape scale using public multi-omics data. [src: discoveries] It also says this is, to its knowledge, the first application of GapMind community-weighted completeness to predict environmental metabolomics across a large cross-habitat NMDC dataset. [src: nmdc_community_metabolic_ecology] It presents the integration as a scalable approach for testing metabolic ecological hypotheses from public data lakehouses. [src: nmdc_community_metabolic_ecology] These are the authors' priority claims, not independent findings.

## Limits: gene presence and annotation

Gene presence is not expression. Pathway completeness indicates whether genes are present, not whether they are actively expressed. Transcriptomics would be needed to learn whether expressed biosynthesis correlates more strongly with metabolite pools. [src: nmdc_community_metabolic_ecology] The report proposes pairing metatranscriptomics with metabolomics in a subset of NMDC samples. That would compare expressed pathway completeness, genomic potential, and metabolite abundance, and test whether expression drives the BQH signal. [src: nmdc_community_metabolic_ecology] See also [[concepts/reliability-and-coverage-limits-of-gapmind-pathway-predictions]].

Metabolite matching is a second limit. Metabolites were matched to pathways by string-based compound names. [src: nmdc_community_metabolic_ecology] KEGG compound identifiers (IDs) in the NMDC data have only a 2% annotation rate, which limits KEGG-based matching. [src: nmdc_community_metabolic_ecology] Cysteine, histidine, and lysine remain untestable because their compounds were not detected. [src: nmdc_community_metabolic_ecology] The metabolomics_gold annotations currently lack KEGG compound annotations for these three pathways. [src: nmdc_community_metabolic_ecology] The report proposes improving those annotations to expand the H1 test set from 13 to 16 testable pathways and improve statistical power. [src: nmdc_community_metabolic_ecology] Related issues are in [[concepts/compound-identifier-ambiguity-in-linking-metabolites-to-metabolic-models]] and annotation and environmental metadata table gaps in the data lakehouse.

The chorismate result needs caution. Shikimic acid and 3-dehydroshikimic acid serve as metabolomics proxies for chorismate pathway activity. [src: nmdc_community_metabolic_ecology] They are upstream intermediates whose concentrations reflect precursor availability rather than chorismate pool size, so the chorismate BQH correlation (r = −0.038) should be interpreted cautiously. [src: nmdc_community_metabolic_ecology]

Taxonomy mapping adds uncertainty. About 1,352 Centrifuge taxa match multiple GTDB clades within a genus. The report chose one representative clade by alphabetical tiebreaking on gtdb_species_clade_id, documented in NB03 cell-17. [src: nmdc_community_metabolic_ecology] Genus-proxy-ambiguous taxa account for ~6.5% of mapped abundance, which bounds the sensitivity of completeness scores to this choice. [src: nmdc_community_metabolic_ecology] See [[concepts/taxonomy-bridging-between-metagenomic-classifiers-and-reference-pangenomes]] and [[concepts/genus-level-taxonomy-bridging-to-pangenome-clades-and-its-coverage-limits]].

## Open Directions

- Pair metatranscriptomics with metabolomics in a subset of NMDC samples. Compare expressed pathway completeness, genomic potential, and metabolite abundance to test whether expression, not just gene presence, drives the BQH signal.
- Improve KEGG compound annotations in metabolomics_gold for cysteine, histidine, and lysine. This would expand the H1 test set from 13 to 16 testable pathways and add statistical power.
- Add samples with methionine measurements. The strongest effect (n = 18) is underpowered, and more samples would show whether it holds.
- Measure chorismate or downstream products directly. This would replace the upstream intermediate proxies and settle the near-zero chorismate result.
- Rerun the correlations under alternative representative-clade choices and with frac_likely_complete. This would check the robustness of the signal.
