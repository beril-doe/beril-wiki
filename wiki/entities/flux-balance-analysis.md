---
type: Method
description: Metabolic-modeling method that predicts fluxes and growth from stoichiometric
  constraints
sources:
- id: acinetobacter_adp1_explorer
  resource: ../summaries/acinetobacter_adp1_explorer__REPORT.md
  title: acinetobacter adp1 explorer
- id: adp1_triple_essentiality
  resource: ../summaries/adp1_triple_essentiality__REPORT.md
  title: adp1 triple essentiality
- id: annotation_gap_discovery
  resource: ../summaries/annotation_gap_discovery__REPORT.md
  title: annotation gap discovery
- id: aromatic_catabolism_network
  resource: ../summaries/aromatic_catabolism_network__REPORT.md
  title: aromatic catabolism network
- id: discoveries
  resource: ../summaries/discoveries.md
  title: discoveries
- id: respiratory_chain_wiring
  resource: ../summaries/respiratory_chain_wiring__REPORT.md
  title: respiratory chain wiring
title: Flux Balance Analysis
---
# Flux Balance Analysis

## What this entity is

**Canonical name:** Flux Balance Analysis.  
**Known alias:** FBA. [^acinetobacter_adp1_explorer]

Flux Balance Analysis is a metabolic-modeling method represented in the ADP1 database through predicted metabolic fluxes and growth phenotypes. [^acinetobacter_adp1_explorer] No stable external identifier for this method is specified in the source document. [^acinetobacter_adp1_explorer]

## Key facts and concordance evidence

FBA flux data covered 15% of the 5,852 genes in the central `genome_features` table. [^acinetobacter_adp1_explorer]

Among 866 genes with both FBA flux predictions and TnSeq essentiality calls, 639 genes, or 73.8%, had concordant results, while 227 genes were discordant. [^acinetobacter_adp1_explorer] The discordant genes were identified as candidates for metabolic-model refinement or as possible examples of regulatory effects not represented by FBA. [^acinetobacter_adp1_explorer]

FBA flux classes changed between rich and minimal media for 177 of the 866 genes, or 20%, indicating condition-dependent metabolic rewiring among the genes with flux data. [^acinetobacter_adp1_explorer]

The newer analysis **refines** this earlier concordance claim by separating prediction tasks: among 478 TnSeq-dispensable genes, FBA class did not predict quantitative growth defects (chi-squared = 0.93, p = 0.63, 2 df; Kruskal-Wallis H = 1.67, p = 0.43). [^adp1_triple_essentiality] In contrast, FBA showed moderate concordance with complete-knockout lethality: rich media yielded recall = 60.8%, precision = 64.0%, specificity = 79.7%, F1 = 0.624, and Cohen’s kappa = 0.486 across 724 genes; minimal media yielded recall = 65.6%, precision = 69.2%, specificity = 78.9%, F1 = 0.673, and Cohen’s kappa = 0.493 across 833 genes. [^adp1_triple_essentiality]

Thus, the earlier 73.8% concordance and the newer null result are not directly contradictory: they concern different comparisons. The newer analysis **supports** FBA as a moderate classifier at the lethal-versus-dispensable boundary but **contradicts** using FBA class to explain growth variation among TnSeq-dispensable genes. [^acinetobacter_adp1_explorer][^adp1_triple_essentiality]

Condition-specific FBA flux correlations with measured growth were weak and mixed, including glucose ρ = -0.021 (p = 0.677; n = 387), acetate ρ = -0.153 (p = 0.004; n = 352), asparagine ρ = -0.257 (p < 0.001; n = 286), and glucarate ρ = +0.246 (p = 0.005; n = 127); the opposite-than-expected glucarate direction suggests condition-specific model inaccuracies. [^adp1_triple_essentiality] Aromatic degradation was enriched among FBA-discordant genes (9 of 11; OR = 9.70; FDR-adjusted q = 0.012), with directional enrichment for FBA under-prediction (OR = 12.0; q = 0.004), **supporting** environmental-assumption gaps as a refinement target. [^adp1_triple_essentiality]

The aromatic-catabolism analysis **supports and refines** this environmental-gap interpretation: FBA captured 1.76× higher Complex I flux on aromatic substrates than on the comparison condition, with fluxes of 0.55 versus 0.31, but predicted 0% essentiality for Complex I. [^aromatic_catabolism_network] This indicates that growth-optimizing flux redistribution can represent increased respiratory demand without identifying disruption of a multi-subunit respiratory complex as a bottleneck. [^aromatic_catabolism_network] Of 51 quinate-specific genes, 30 had no FBA reaction mappings, including cofactor-supply, iron-acquisition, regulatory, and newly identified Complex I-associated functions, showing that the model represents core metabolism more completely than some supporting infrastructure. [^aromatic_catabolism_network] Independent quinate-specific growth defects in 10/13 Complex I operon subunits further **contradict** interpreting 0% model essentiality as evidence that the corresponding functions are biologically dispensable. [^aromatic_catabolism_network]

The respiratory-chain wiring study **supports and refines** this limitation: FBA predicted zero flux through NDH-2 and ACIAD3522 on all standard media because growth optimization preferentially routed NADH through the higher-ATP-yielding Complex I. [^respiratory_chain_wiring] Consequently, the model can miss alternative respiratory pathways and capacity constraints that force use of suboptimal routes, even when gene-phenotype data indicate condition-specific requirements. [^respiratory_chain_wiring] This interpretation is based on model behavior and theoretical pathway stoichiometry rather than measured flux distributions. [^respiratory_chain_wiring]

The discoveries synthesis **supports** the condition-specific interpretation: in ADP1, each of 8 carbon sources required a distinct respiratory configuration; quinate required only Complex I, acetate required Complex I plus cytochrome bo3 and ACIAD3522 among other components, and glucose had no specifically required component. [^discoveries] Quinate produced 0.57 NADH per carbon versus 1.50 for glucose, yet Complex I was more essential because simultaneous β-ketoadipate products created a concentrated NADH burst. [^discoveries] This **refines** interpretation of flux magnitude alone: a lower total reductant yield can still impose a sharper respiratory bottleneck. [^discoveries]

The same synthesis reports that FBA lacked reaction mappings for 30/51 quinate-specific genes (59%) and predicted 0% Complex I essentiality despite predicting 1.76× higher aromatic flux. [^discoveries] These results **support** treating missing respiratory, cofactor-supply, iron-acquisition, and regulatory reactions as model gaps rather than treating the essentiality prediction as evidence against the measured phenotype. [^discoveries]

## Reaction conservation and gapfilling

Across 1,330 unique metabolic reactions, 1,248, or 94%, were shared across all 14 analyzed genomes and classified as core, 62 were variable, and 20 were genome-unique. [^acinetobacter_adp1_explorer]

Gapfilling accounted for 7.7% of reactions on average, and 243 missing functions were cataloged. [^acinetobacter_adp1_explorer] Of 121,519 growth phenotype predictions across 14 genomes, 105,376, or 87%, required at least one gapfilled reaction, making growth-prediction interpretation tightly dependent on gapfilling quality in this analysis. [^acinetobacter_adp1_explorer]

The annotation-gap study **supports** the importance of this dependency: across 574 organism-carbon source combinations, baseline FBA achieved 42.5% overall accuracy, with recall of 86.5% (244 of 282 growth-positive conditions correctly predicted) and precision of 42.5% (244 of 574 growth predictions correct), producing 330 false positives. [^annotation_gap_discovery] Conditional gapfilling for 38 false-negative cases added 219 reactions: 201 enzymatic, 14 transport, and 12 exchange, averaging 5.8 reactions per case. [^annotation_gap_discovery]

The same study **refines** gapfilling interpretation by showing that evidence triangulation assigned candidate genes to 96 of 201 gapfilled enzymatic reaction-organism pairs (47.8%), including 44 high-confidence, 19 medium-confidence, and 33 low-confidence pairs; 105 pairs (52.2%) remained unresolved. [^annotation_gap_discovery] BLAST alone resolved 70 pairs (34.8%), whereas the full pipeline resolved 96 (47.8%), so no single evidence stream exceeded 35% resolution. [^annotation_gap_discovery] Of 50 EC-less “dark reactions,” only 8 (16%) were resolved, compared with 88 of 151 (58.3%) reactions with known EC numbers, identifying a specific annotation limitation rather than evidence that all gapfills are equally uncertain. [^annotation_gap_discovery]

FBA validation in the annotation-gap study was inconclusive: 23 gene-protein-reaction (GPR) rules—formal links between genes and reactions—were inserted into SBML models, but knockout simulations produced zero wildtype growth because the models required the gapfilled reactions themselves to grow on the tested minimal media. [^annotation_gap_discovery] This **refines** the earlier use of FBA for essentiality assessment by showing that validation can become circular when the tested reaction is itself required for model growth. [^annotation_gap_discovery]

Across 7 Fitness Browser organisms and 23 GapMind pathways, 35.4% of pathway-organism pairs were Active Dependencies, 41.0% Latent Capabilities, 14.9% Incomplete but Important, and 8.7% Missing; all Latent Capabilities became fitness-important under condition-specific analyses. [^discoveries] This **supports** using measured condition-specific fitness to test whether apparently complete FBA pathways are latent rather than biologically irrelevant capabilities.

The aromatic analysis **supports** adding respiratory-chain capacity, PQQ biosynthesis, and iron-homeostasis constraints to ADP1 FBA, because these supporting functions were not fully represented despite their measured association with quinate growth. [^aromatic_catabolism_network]

## Related evidence and pages

The FBA results **support** comparison of metabolic-model predictions with [tnseq](tnseq.md) essentiality measurements and feed into [gene-essentiality](../concepts/gene-essentiality.md). [^acinetobacter_adp1_explorer]

The reaction-conservation and gapfilling results **support** analysis in [metabolic-model-gapfilling](../concepts/metabolic-model-gapfilling.md). [^acinetobacter_adp1_explorer] The aromatic-discordance result **refines** that analysis by identifying missing aromatic substrates or mismatched environmental assumptions as testable model gaps. [^adp1_triple_essentiality] The respiratory-chain study further **supports** this connection by identifying growth optimization and omitted capacity constraints as specific causes of false-negative pathway-use predictions. [^respiratory_chain_wiring]

The annotation-gap workflow further connects FBA to [condition-specific-fitness](../concepts/condition-specific-fitness.md), [pangenome-integration](../concepts/pangenome-integration.md), and [multi-omics-integration](../concepts/multi-omics-integration.md) through fitness, pangenome, pathway, annotation, and homology evidence. [^annotation_gap_discovery] The discoveries synthesis **supports** these connections by showing that pathway completeness and condition-specific fitness can diverge, particularly for latent capabilities. [^discoveries] The respiratory-chain analysis also **supports** [multi-omics-integration](../concepts/multi-omics-integration.md) by combining FBA with gene-phenotype measurements, theoretical stoichiometry, cross-species fitness, and proteomics. [^respiratory_chain_wiring]

The full source-level accounts are [acinetobacter_adp1_explorer__REPORT](../summaries/acinetobacter_adp1_explorer__REPORT.md), [adp1_triple_essentiality__REPORT](../summaries/adp1_triple_essentiality__REPORT.md), [annotation_gap_discovery__REPORT](../summaries/annotation_gap_discovery__REPORT.md), [aromatic_catabolism_network__REPORT](../summaries/aromatic_catabolism_network__REPORT.md), [discoveries](../summaries/discoveries.md), and [respiratory_chain_wiring__REPORT](../summaries/respiratory_chain_wiring__REPORT.md). [^acinetobacter_adp1_explorer][^adp1_triple_essentiality][^annotation_gap_discovery][^aromatic_catabolism_network][^discoveries][^respiratory_chain_wiring]

[^acinetobacter_adp1_explorer]: [acinetobacter adp1 explorer](../summaries/acinetobacter_adp1_explorer__REPORT.md)
[^adp1_triple_essentiality]: [adp1 triple essentiality](../summaries/adp1_triple_essentiality__REPORT.md)
[^aromatic_catabolism_network]: [aromatic catabolism network](../summaries/aromatic_catabolism_network__REPORT.md)
[^respiratory_chain_wiring]: [respiratory chain wiring](../summaries/respiratory_chain_wiring__REPORT.md)
[^discoveries]: [discoveries](../summaries/discoveries.md)
[^annotation_gap_discovery]: [annotation gap discovery](../summaries/annotation_gap_discovery__REPORT.md)
