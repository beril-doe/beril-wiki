---
type: "Concept"
description: "How well flux balance analysis and draft automated model predictions agree with experimental gene essentiality (TnSeq or knockout lethality) and carbon-source growth, and how gapfilling and media assumptions limit that agreement; stops at growth-rate prediction within dispensable genes."
sources: ["summaries/acinetobacter_adp1_explorer__REPORT.md", "summaries/adp1_triple_essentiality__REPORT.md", "summaries/annotation_gap_discovery__REPORT.md", "summaries/aromatic_catabolism_network__REPORT.md", "summaries/respiratory_chain_wiring__REPORT.md"]
---
# Concordance of genome-scale metabolic model predictions with experimental data

This page covers how well flux balance analysis (FBA) and draft automated model predictions agree with experimental gene essentiality and carbon-source growth. FBA models of Acinetobacter baylyi ADP1 agree moderately with experimental essentiality (κ≈0.49, F1≈0.62-0.67). [src: adp1_triple_essentiality] Baseline FBA on carbon sources has 42.5% accuracy because draft models are overly permissive. [src: annotation_gap_discovery] For Acinetobacter growth predictions, the report says accuracy is tightly coupled to gapfilling quality. [src: acinetobacter_adp1_explorer] The ADP1 respiratory and aromatic-catabolism reports add that FBA misses specific biology: genes without reaction mappings, and Complex I effects that growth optimization hides. [src: aromatic_catabolism_network, respiratory_chain_wiring] The evidence comes mainly from one organism (ADP1) plus one multi-organism carbon-source test. See [[entities/flux-balance-analysis]].

## Literature Context

The candidate papers speak to the modeling framework behind this page more than to the ADP1 concordance figures. They are abstracts only, and none of them tests essentiality or carbon-source growth in Acinetobacter. One paper reports that the biomass objective function (BOF) strongly shapes growth phenotype predictions from genome-scale metabolic models. It presents BOFdat, which builds a BOF from experimental data, and applies it to the E. coli model iML1515. The BOFdat BOF gave the most concordant biomass composition, growth rate and gene essentiality prediction accuracy compared with other methods [PMID 31009451](https://pubmed.ncbi.nlm.nih.gov/31009451/). This suggests that part of any model-versus-experiment disagreement comes from objective-function and media assumptions as well as from missing reactions. The hub does not test that possibility.

A second line of work shows that constraint-based predictions can match measured phenotypes in a well-studied organism. A phenotypic phase plane for the Saccharomyces cerevisiae network gave growth and secretion predictions that were concordant with in vivo data for three growth conditions: aerobic glucose-limited, oxidative-fermentative and microaerobic [PMID 15355549](https://pubmed.ncbi.nlm.nih.gov/15355549/). That is concordance for growth and secretion rates under defined conditions. It does not address essentiality calls.

Two further papers address what plain FBA lacks. IGM is a mixed-integer linear programming framework that integrates gene expression across multiple conditions. Its abstract describes conventional FBA as often giving ambiguous results because condition-specific data are not used consistently. In E. coli models, IGM improved correlation with experimentally measured fluxes and reduced flux ambiguity [PMID 41662246](https://pubmed.ncbi.nlm.nih.gov/41662246/). A Sirtuin1 regulatory-metabolic extension of Recon3D reports that genome-scale models typically lack explicit transcriptional regulation. In Caco-2 cells, predicted and measured intracellular metabolite trends were concordant for 10 of 12 metabolites (83%) [PMID 42570864](https://pubmed.ncbi.nlm.nih.gov/42570864/). This is an in vitro, human-cell result and not a microbial one.

The corpus findings sit mostly alongside this literature and do not conflict with it. The ADP1 reports find moderate FBA agreement with knockout lethality (kappa about 0.49, F1 about 0.62-0.67). They also find 73.8% concordance with TnSeq. These are different metrics on different gene sets. These results are broadly consistent with the view that models need better constraints than growth-optimal FBA provides. The hub raises regulation only as one possible reason for the discordant 26% of genes, along with model refinement, and the candidates do not settle which applies. The Complex I result is a separate, better-supported point. The reports say FBA's linear programming framework misses the threshold effect of losing a Complex I subunit, and that growth optimization redistributes flux. The candidates do not test that mechanism, so it is not supported or contradicted by them.

The corpus extends the literature in two ways. It quantifies how heavily draft-model growth predictions depend on gapfilling, with 87% needing at least one gapfilled reaction. It also reports that FBA does not predict growth defects among TnSeq-dispensable genes (p=0.63). The candidates have no counterpart to either result. The work on biomass objectives and expression integration suggests two untested routes for ADP1: refining the BOF, and adding expression constraints.

## Gene essentiality: FBA versus TnSeq and knockouts

In the ADP1 database, 639 of 866 genes (73.8%) with both FBA flux predictions and TnSeq (transposon sequencing) essentiality calls are concordant. [src: acinetobacter_adp1_explorer] FBA flux data cover only 15% of genes, the sparsest modality, which limits this comparison to 866 genes. [src: acinetobacter_adp1_explorer] The ADP1 report attributes an original report of ~75% FBA-TnSeq concordance to Durot et al. (2008). [src: adp1_triple_essentiality] See [[entities/durot-et-al-2008-adp1-metabolic-model]].

A separate analysis compared FBA with knockout lethality. It found moderate concordance. [src: adp1_triple_essentiality] The two media gave these results:

| Medium | Genes | TP / FP / FN / TN | Recall | Precision | Specificity | F1 | Kappa |
|---|---|---|---|---|---|---|---|
| Rich | 724 | 164 / 92 / 106 / 362 [src: adp1_triple_essentiality] | 60.8% | 64.0% | 79.7% [src: adp1_triple_essentiality] | 0.624 | 0.486 [src: adp1_triple_essentiality] |
| Minimal | 833 | 229 / 102 / 120 / 382 [src: adp1_triple_essentiality] | 65.6% | 69.2% | 78.9% [src: adp1_triple_essentiality] | 0.673 | 0.493 [src: adp1_triple_essentiality] |

Performance was better in minimal media (F1=0.67) than in rich media (F1=0.62). [src: adp1_triple_essentiality] The report tentatively attributes this to tighter metabolic constraints and FBA assumptions that better match reality. [src: adp1_triple_essentiality] It interprets FBA as a reasonable predictor with ~60-70% accuracy. [src: adp1_triple_essentiality] It recommends FBA as a first-pass screen and says predictions need experimental validation. [src: adp1_triple_essentiality]

This concordance applies at the essential/dispensable boundary. [src: adp1_triple_essentiality] FBA is a threshold classifier. It predicts whether a knockout reduces growth to zero, not how much growth falls. [src: adp1_triple_essentiality] The report also finds that FBA does not predict growth defects among TnSeq-dispensable genes (p=0.63). [src: adp1_triple_essentiality] That is where this page stops.

The discordant 26% of genes may need model refinement, or they may reflect regulatory effects that FBA does not capture. [src: acinetobacter_adp1_explorer] The report proposes testing the 227 genes with discordant FBA and TnSeq calls for pathway or regulatory-function enrichment to guide refinement. [src: acinetobacter_adp1_explorer] In ADP1, 20% of genes (177/866) change FBA flux class between rich and minimal media. [src: acinetobacter_adp1_explorer] Related limits are in [[concepts/systematic-blind-spots-of-flux-balance-models-for-condition-specific-requirements]]. For example, the ADP1 model predicts 1.76× higher Complex I flux on aromatic substrates (0.55 vs 0.31). [src: aromatic_catabolism_network] It still predicts 0% Complex I essentiality. [src: aromatic_catabolism_network]

### Why FBA misses the Complex I bottleneck

The ADP1 FBA model predicts zero flux through both NDH-2 and ACIAD3522 on all standard media, because growth-rate optimization favors Complex I for its higher ATP (adenosine triphosphate) yield per NADH (reduced nicotinamide adenine dinucleotide). [src: respiratory_chain_wiring] The aromatic-catabolism report likewise says the model fails to identify the Complex I bottleneck because FBA optimizes growth rate and can redistribute flux through alternative pathways. [src: aromatic_catabolism_network] It adds that loss of any Complex I subunit eliminates function entirely, a threshold effect that FBA's linear programming framework does not capture. [src: aromatic_catabolism_network] The respiratory report calls this the fundamental reason FBA fails to predict condition-specific respiratory requirements: it assumes the optimal pathway is always used and misses capacity constraints that force alternative, suboptimal pathways at high flux. [src: respiratory_chain_wiring]

### Genes outside the model

In ADP1, 30 of 51 quinate-specific genes have no FBA reaction mappings. Cofactor supply chains (PQQ, pyrroloquinoline quinone, and iron) and regulatory genes are therefore invisible to the metabolic model. [src: aromatic_catabolism_network]

## Carbon-source growth and draft models

Draft models are permissive. Baseline FBA across 574 organism-carbon source combinations had 42.5% overall accuracy. [src: annotation_gap_discovery] Recall was 86.5% (244 of 282 growth-positive conditions correctly predicted). [src: annotation_gap_discovery] Precision was only 42.5% (244 of 574 growth predictions correct), with 330 false positives attributed to overly permissive draft models. [src: annotation_gap_discovery] The report says draft models built from automated RAST annotations contain systematic errors. [src: annotation_gap_discovery]

The report proposes that gapseq could reduce false-positive predictions in initial reconstruction. [src: annotation_gap_discovery] It calls gapseq its closest methodological comparator. [src: annotation_gap_discovery] gapseq focuses on model reconstruction and does not integrate transposon fitness data. [src: annotation_gap_discovery] The report sees its own triangulation pipeline as complementary. [src: annotation_gap_discovery] See [[concepts/multi-evidence-triangulation-of-metabolic-annotation-gaps]].

## Gapfilling limits agreement

In the ADP1 database, gapfilling accounts for 7.7% of reactions on average, with 243 missing functions cataloged. [src: acinetobacter_adp1_explorer] Of 121,519 growth predictions across 14 Acinetobacter genomes, 105,376 (87%) need at least one gapfilled reaction. [src: acinetobacter_adp1_explorer] The report says this ties prediction accuracy tightly to gapfilling quality. [src: acinetobacter_adp1_explorer] It proposes assessing gapfill confidence with pangenome conservation data to improve reliability. [src: acinetobacter_adp1_explorer] False negatives have higher mean gap counts than correct predictions. [src: acinetobacter_adp1_explorer] The report calls the 243 missing functions genuine gaps in genomic evidence that affect reliability. [src: acinetobacter_adp1_explorer]

Conditional gapfilling of 38 false-negative cases added 219 reactions (201 enzymatic, 14 transport, 12 exchange), averaging 5.8 reactions per case. [src: annotation_gap_discovery] Multiple valid gapfill solutions may exist, and default ModelSEED gapfilling minimizes added reactions without guaranteeing biological optimality. [src: annotation_gap_discovery] Mapping 109 carbon-source names to compound IDs (identifiers) was manual, and errors would produce spurious false negatives. [src: annotation_gap_discovery]

Knockout validation of the gapfilled models was inconclusive. Wildtype growth was zero on minimal carbon media. [src: annotation_gap_discovery] The report calls this expected, because the models need the gapfilled reactions to grow. [src: annotation_gap_discovery] It calls single-gene knockout analysis circular in this context. [src: annotation_gap_discovery] Validation did insert 23 gene-protein-reaction rules into SBML models for high/medium-confidence NB03 candidates. [src: annotation_gap_discovery]

## Tensions

- Concordance is 73.8% in the database comparison. [src: acinetobacter_adp1_explorer] It is κ≈0.49 and F1≈0.62-0.67 in the knockout comparison. [src: adp1_triple_essentiality] The reports use different metrics and gene sets, so the figures are not directly comparable.

## Open Directions

- Test the discordant genes for pathway or regulatory enrichment. This would show whether the errors are metabolic or regulatory. See [[concepts/pangenome-conservation-of-metabolic-model-discordant-genes]].
- Assess gapfill confidence with pangenome conservation data, since 87% of growth predictions depend on gapfilling.
- Rebuild the initial models with gapseq and recompute carbon-source precision. This would show whether false positives fall.
- Compare knockout validation with gapfilled reactions fixed against validation without them. This would address the circularity problem.
- Add reactions or constraints for the 30 unmapped quinate-specific genes and for Complex I subunit loss, then test whether predicted Complex I essentiality changes from 0%.
