---
type: "Summary"
description: "Design of commensal consortia to competitively exclude *Pseudomonas aeruginosa* from cystic-fibrosis airways, integrating inhibition assays, carbon-utilization and growth-kinetics profiling, patient meta-omics, PA pangenome and virulence typing, and multi-criterion formulation optimization."
doc_type: "short"
full_text: "sources/cf_formulation_design__REPORT.md"
---
# Rational Design of Protective Microbiome Formulations for Competitive Exclusion of *Pseudomonas aeruginosa* in Cystic Fibrosis Airways

## Overview

This report integrates planktonic inhibition assays, carbon-utilization profiling, growth kinetics, patient metagenomics and metatranscriptomics, pairwise interaction data, and pangenome analysis to design commensal communities that suppress *Pseudomonas aeruginosa* (PA) in cystic-fibrosis airways through metabolic competition and direct antagonism. The study analyzed 4,949 isolates from 175 patient samples, including 220 inhibition-tested isolates, 430 isolates profiled on 21 substrates, 32 isolates with growth kinetics, and 499 pangenome genomes across six species. [src: cf_formulation_design]

The experimental backbone is the PROTECT CF Synbiotic Cocktail Study: its 4,949 isolates from 175 CF/NCFB patient samples were integrated with a KBase Data Lakehouse pangenome containing 293,000 genomes and GapMind metabolic pathway predictions (GapMind scores how complete an amino-acid or carbon catabolic pathway is from genome sequence alone). [src: cf_formulation_design]

The PROTECT study produced 23 structured data tables (30.5M total rows) covering 4,949 isolates from 211 species across 175 patient samples (133 CF, 41 NCFB, 43 subjects, 4 clinical states); the stated CF and NCFB sample subtotals do not add up to the reported 175-sample total, and the report does not reconcile the two. [src: cf_formulation_design]

The collection is dominated by *P. aeruginosa* (655 isolates), *S. aureus* (379), and *Rothia dentocariosa* (318), which the report attributes to the typical CF airway microbiome plus deliberate oversampling of pathogens — so isolate frequencies in this collection cannot be read as natural prevalence. Genome quality is high, with mean completeness 99.8% and median contamination 0.08%. [src: cf_formulation_design]

Species names throughout follow GTDB taxonomy (Parks et al. 2022), which may differ from NCBI names: *Pseudomonas_E* denotes a non-aeruginosa *Pseudomonas* clade distinct from *P. aeruginosa* and must not be merged with it. [src: cf_formulation_design]

*Pseudomonas aeruginosa* chronically colonizes the airways of most CF patients by early adulthood, and is the pathogen this project's formulations target. Citing prior work (Palmer et al. 2005, 2007), the report states that once established PA adapts to the lung environment — switching to amino acid catabolism as its primary carbon source, forming biofilms, and becoming increasingly antibiotic-resistant; this is cited literature background, not a measurement made here. [src: cf_formulation_design]

The study's premise is explicitly framed as theory rather than established mechanism. Its working theory is that *P. aeruginosa* can be excluded by commensal communities that consume the same carbon sources it depends on — primarily amino acids that are abundant in CF sputum (proline, histidine, ornithine, glutamate, aspartate, arginine; Palmer et al. 2007). The report further hypothesizes that prebiotics — substrates that feed commensals but not PA — could give the consortium a biomass advantage before competition begins. [src: cf_formulation_design]

## Key Findings

### Assay cohorts and data overlap

Three experimental assays provide complementary views of competitive potential: planktonic inhibition of PA14 (220 isolates), carbon source utilization profiling (430 isolates on 21 substrates), and growth kinetics (32 isolates with full time-series curves); the core analysis cohort — isolates with both inhibition and carbon-utilization data — comprises 142 isolates from 62 species. The report's own substrate counts are inconsistent and left unreconciled: the assay overview states 21 substrates, the assay description states that PA14 and 430 commensal isolates were tested on 20 amino acids plus glucose and lactate, and later passages refer to 22 tested substrates. [src: cf_formulation_design]

![Isolate species distribution](figures/01_isolate_species_distribution.png)
![Isolate genus distribution — red = known CF pathogens](figures/01_isolate_genus_distribution.png)
![Genome quality: completeness, contamination, reference ANI](figures/01_genome_quality.png)
![Carbon utilization clustermap — top 50 most variable isolates](figures/01_carbon_util_clustermap.png)
![Data type overlap across isolates](figures/01_data_overlap.png)
[src: cf_formulation_design]

### Metabolic competition and inhibition

PA14 preferentially used amino acids under synthetic cystic-fibrosis sputum conditions, with endpoint OD values of 0.60 for proline, 0.56 for histidine, 0.46 for ornithine, 0.40 for glutamate, 0.36 for aspartate, 0.36 for isoleucine, and 0.35 for arginine; glucose supported OD 0.22, while threonine, methionine, cysteine, serine, and glycine each supported essentially no growth at <0.07. The report reads the resulting ranking — proline > histidine > ornithine > glutamate — as mirroring the synthetic cystic-fibrosis sputum medium (SCFM) composition and so as validating its assay system against Palmer et al. (2005, 2007), who established amino acids as PA's primary carbon sources in CF sputum. [src: cf_formulation_design]

The other reporter pathogens (*A. baumannii*, *K. pneumoniae*) show distinct carbon-utilization profiles, so PA14's amino acid specialization is not universal among CF pathogens and formulations may need to be pathogen-specific; the design reported here is therefore PA14-targeted and not demonstrated to generalize across CF pathogens. [src: cf_formulation_design]

![PA14 carbon source utilization profile](figures/01_pa14_carbon_profile.png)
![All reporter pathogen carbon utilization profiles](figures/01_reporter_carbon_heatmap.png)
[src: cf_formulation_design]

Integrating six evidence streams — planktonic inhibition assays (220 isolates), carbon source utilization profiling (430 isolates × 21 substrates), growth kinetics (32 isolates), patient metagenomics (175 samples), pairwise interaction data, and pangenome analysis (499 genomes across 6 species) — the report finds that metabolic overlap with PA14 significantly predicts inhibition but explains only 27% of variance, concluding that the strongest inhibitors combine metabolic competition with direct antagonism mechanisms. Across the 142-isolate analysis cohort with both inhibition and carbon-utilization data, metabolic overlap with PA14, weighted by PA14's substrate preferences, significantly predicted planktonic inhibition (r = 0.384, p = 2.3×10⁻⁶). A multivariate model incorporating metabolic overlap, total growth on PA-preferred substrates, metabolic breadth, and maximum growth explained R² = 0.274 of inhibition variance, increasing to R² = 0.360 after adding genus-level taxonomy — genus explaining an additional 8.6% of variance, which the report attributes to intrinsic species-level mechanisms, likely direct antagonism, contributing independently of metabolism. Five-fold cross-validation yielded CV R² = 0.145 ± 0.142, below the training R² of 0.274, indicating that the multivariate model overfits to the 142-isolate cohort; the report interprets the true out-of-sample predictive power of metabolic features as closer to 15% than 27%, while noting that this does not invalidate the qualitative conclusion — metabolic overlap remains a statistically significant predictor (p = 2.3×10⁻⁶) — but that the effect size should be interpreted conservatively. [src: cf_formulation_design]

The results support metabolic competition as a real but incomplete mechanism: approximately 73% of inhibition variance remained unexplained by metabolism alone, while genus contributed an additional 8.6% of explained variance and likely captured species-specific direct-antagonism mechanisms. Positive residuals identified *Streptococcus salivarius* ASMA-737 (+74.1%), *Gemella sanguinis* ASMA-3044 (+62.2%), and *Neisseria mucosa* ASMA-3643 (+57.2%) as candidate dual-mechanism inhibitors. The dual-mechanism label is an interpretation of large positive residuals — the report states these organisms appear to combine metabolic competition with direct antagonism, making them particularly valuable — rather than a mechanism isolated experimentally here. [src: cf_formulation_design]

![Metabolic overlap vs inhibition — initial preview (r=0.384)](figures/01_overlap_vs_inhibition_preview.png)
![Three metabolic features vs inhibition with regression lines](figures/03_metabolic_features_vs_inhibition.png)
![Predicted vs observed inhibition from metabolic model (R² = 0.274)](figures/03_predicted_vs_observed.png)
[src: cf_formulation_design]

![Inhibition distribution — all measurements and per-isolate best](figures/01_inhibition_distribution.png)
![Inhibition by genus — full isolate collection (top 20)](figures/01_inhibition_by_genus.png)
![Inhibition by genus in the analysis cohort](figures/03_inhibition_by_genus_cohort.png)
[src: cf_formulation_design]

### Growth kinetics and patient ecology

Growth kinetic parameters — μ_max (maximum growth rate), lag time, carrying capacity, and AUC (area under the growth curve) — were extracted from 676,000 fitted curve points across 32 isolates. [src: cf_formulation_design]

PA14 was generally the fastest grower on preferred substrates: commensals exceeded its maximum growth rate in only 13.8% of substrate comparisons, but commensals began growing earlier in 43.1% of comparisons. Growth kinetic parameters were moderately correlated with endpoint OD (r ≈ 0.40), and adding kinetics to the metabolic model increased the fit to R² = 0.311 for the 29 isolates with all three assay types. [src: cf_formulation_design]

At the summary level the report states that no individual commensal outgrows PA14 on any tested substrate, requiring community-level niche coverage; this abstract-level null is stated alongside, and not reconciled with, the kinetic comparison in which commensals beat PA14's maximum growth rate on 13.8% of substrate comparisons. From the lag-versus-rate asymmetry the report suggests that pre-establishing commensals before pathogen exposure — e.g., via prebiotic biomass pre-loading — could be more important than raw growth rate; this is a suggestion drawn from assay patterns, not a demonstrated intervention. [src: cf_formulation_design]

![Growth curves: PA14 (dashed) vs representative commensals](figures/02_growth_curve_gallery.png)
![Growth rate advantage vs PA14 per isolate × substrate](figures/02_rate_advantage_heatmap.png)
![Growth parameter distributions — K, mu_max, lag, AUC](figures/02_parameter_distributions.png)
![Growth kinetic parameters vs endpoint OD — correlated but not redundant](figures/02_kinetics_vs_endpoint.png)
![Kinetic advantage vs inhibition (n=29)](figures/03_kinetic_advantage_vs_inhibition.png)
[src: cf_formulation_design]

The engraftability screen used paired metagenomic (DNA abundance) and metatranscriptomic (RNA activity) data from 175 patient samples to identify species that are both prevalent and metabolically active; 134 species were detected across patient metagenomes. The engraftability score was defined as prevalence × log(activity ratio), where activity ratio = metaRS CPM / metaG CPM (counts per million in RNA versus DNA) captures transcriptional engagement per unit DNA. Among inhibition-tested species, *Neisseria mucosa* stands out with the highest engraftability (1.595), combining high prevalence with strong transcriptional activity; *Rothia dentocariosa* (0.422) and *Streptococcus salivarius* (0.172) are also above the median among inhibition-tested species. The score is a computed proxy from patient prevalence and transcriptional activity rather than observed therapeutic engraftment. [src: cf_formulation_design]

![Species prevalence vs transcriptional activity — blue = has PROTECT isolate](figures/04_prevalence_vs_activity.png)
[src: cf_formulation_design]

### Formulation optimization

A multi-criterion scoring function evaluated formulations of 1–5 organisms on (1) PA14 niche coverage — the fraction of PA's preferred substrates covered by at least one member; (2) internal complementarity — metabolic dissimilarity among members; (3) mean inhibition; (4) engraftability; and (5) FDA safety. The optimization ran in two stages, permissive safety (excluding only well-known pathogens) and strict safety (additionally excluding all *Pseudomonas*, Enterobacteriaceae, and *Staphylococcus*), so the strict-safe winners below are conditioned on that exclusion rule. [src: cf_formulation_design]

The permissive filter identified the organisms with the highest inhibition — *Leclercia adecarboxylata* (102%), *Pseudomonas_E juntendi* (94%), and *S. epidermidis* (99%) — but the report flags all three as clinically problematic (Enterobacteriaceae, non-aeruginosa *Pseudomonas*, nosocomial *Staphylococcus*), which is why the strict filter was imposed. The report characterizes strict filtering as costing roughly 15% inhibition ceiling while doubling engraftability. [src: cf_formulation_design]

Strict safety-filter optimization identified a five-species core consisting of *N. mucosa*, *S. salivarius*, *Micrococcus luteus*, *R. dentocariosa*, and *G. sanguinis*. The best strict-safe formulations were: k=1, *N. mucosa*, with 18% niche coverage, 88% inhibition, and engraftability 1.595; k=2, *R. dentocariosa* + *N. mucosa*, with 18% coverage, 84% inhibition, and engraftability 0.820; k=3, *M. luteus* + *N. mucosa* + *S. salivarius*, with 100% coverage, 75% inhibition, and engraftability 0.140; k=4, *R. dentocariosa* + *M. luteus* + *N. mucosa* + *S. salivarius*, with 100% coverage, 76% inhibition, and engraftability 0.185; and k=5, the five-species core, with 100% coverage, 78% inhibition, and engraftability 0.188. [src: cf_formulation_design]

Composite scores for these strict-safe winners were 0.753 at k=1, 0.588 at k=2, 0.562 at k=3, and 0.578 at k=4. The report reads k=1 — *N. mucosa* [ASMA-3643], at 18% coverage, 88% inhibition and engraftability 1.595 — as the best single organism, combining the highest engraftability with strong inhibition, but notes that its low 18% coverage limits monotherapy. The k=2 option, *R. dentocariosa* [ASMA-2935] + *N. mucosa* [ASMA-3643], retains only 18% coverage despite 84% mean inhibition and engraftability 0.820, and both members are lung-adapted species (33–38% respiratory in the pangenome). The k=3 option, *M. luteus* [ASMA-2965] + *N. mucosa* [ASMA-3643] + *S. salivarius* [ASMA-737], is labelled the minimum viable formulation — the first size to achieve full niche coverage — at 100% PA niche coverage, 75% mean inhibition and engraftability 0.140, while k=4 adds *R. dentocariosa* for lung tropism and direct-antagonism depth at 100% coverage, 76% inhibition, and engraftability 0.185. [src: cf_formulation_design]

The k=3 formulation was the minimum size achieving complete PA14 niche coverage because *M. luteus* grew on 9 of PA14's 11 preferred substrates — including proline, histidine, glutamate, aspartate, arginine, and glucose — covering the amino-acid substrates that *N. mucosa* and *S. salivarius* do not reach individually; the report describes its carbon-utilization profile as the widest among all strict-safe candidates, producing the 18% → 100% coverage jump, at 75% mean inhibition and engraftability 0.140. 100% niche coverage means that at least one formulation member grows on every amino acid PA14 can use. Exhaustive enumeration of C(97,3) = 147,440 possible triples from the full strict-safe candidate pool produced 127,598 valid unique-species formulations, and the same *M. luteus* + *N. mucosa* + *S. salivarius* triple emerged as the global optimum with composite score 0.562, which the report reads as confirming that the optimization result is not an artifact of restricting the candidate pool. [src: cf_formulation_design]

The full five-member option is reported as k=5 — *R. dentocariosa* [ASMA-2935] + *M. luteus* [ASMA-2965] + *G. sanguinis* [ASMA-3044] + *N. mucosa* [ASMA-3643] + *S. salivarius* [ASMA-737] — with composite 0.587, 100% coverage, 78% mean inhibition, and engraftability 0.188, described as offering maximum redundancy and inhibition depth. [src: cf_formulation_design]

Bootstrap resampling over 1,000 replicates produced 95% composite-score confidence intervals of [0.753, 0.753] for k=1, [0.514, 0.588] for k=2, [0.551, 0.562] for k=3, [0.534, 0.578] for k=4, and [0.520, 0.587] for k=5; the k=2 through k=5 intervals overlapped, so formulation sizes were not statistically distinguishable on the composite score, which the report takes as supporting its recommendation of k=2 as the practical primary candidate. [src: cf_formulation_design]

The same five-species core recurs across all formulation sizes, which the report reads as a robust solution rather than an optimization artifact, with exhaustive enumeration and bootstrap analysis further supporting the robustness of the rankings. [src: cf_formulation_design]

![Core species frequency in top strict-safe formulations](figures/05b_strict_safe_species_frequency.png)
![Bootstrap confidence intervals on formulation composite scores](figures/05b_bootstrap_ci.png)
![Best formulation composite score by size](figures/05_formulation_scores_by_size.png)
[src: cf_formulation_design]

The report recommends k=2 (*R. dentocariosa* + *N. mucosa*) as the primary clinical candidate because both species are lung-adapted (33–38% respiratory genomes in the pangenome), both are described as dual-mechanism inhibitors combining metabolic competition with direct antagonism, they provide 84% mean inhibition, and their combined engraftability 0.820 is nearly 6× higher than the k=3 formulation's 0.140. While k=2 achieves only 18% PA niche coverage, the report suggests that its high per-organism inhibition means direct antagonism may matter more than niche coverage for clinical efficacy — stated explicitly as a hypothesis testable in the mouse model (Proposed Experiment 4.5), not a demonstrated result. [src: cf_formulation_design]

The k=3 formulation (*M. luteus* + *N. mucosa* + *S. salivarius*) is an aspirational second-line candidate contingent on demonstrating *M. luteus* lung engraftment in vivo; in parallel the report proposes a systematic search for a lung-adapted broad-spectrum metabolizer to replace *M. luteus*, screening oral/respiratory Actinobacteria with broad carbon-utilization profiles — e.g. *Kocuria*, *Dermacoccus*, or other Micrococcaceae with respiratory isolation records — against the PA14 carbon-utilization panel. [src: cf_formulation_design]

Core-species profiles were: *N. mucosa*, 88% best inhibition, engraftability 1.595, 15 pangenome genomes, 16/18 conserved amino-acid pathways, and 5 lung genomes (33%); *S. salivarius*, 98%, 0.172, 153 genomes, 18/18 pathways, and 5 lung genomes (4%); *R. dentocariosa*, 79%, 0.422, 29 genomes, 14/18 pathways, and 10 lung genomes (38%); *G. sanguinis*, 85%, 0.202, 7 genomes, 7/18 pathways, and 1 lung genome; and *M. luteus*, 38%, 0.000, 295 genomes, 18/18 pathways, and 0 lung genomes. [src: cf_formulation_design]

The report assigns each core species a distinct role. *S. salivarius* provides the direct-antagonism backbone: highest individual inhibition (98%), an established probiotic precedent (BLIS K12), and a dual-mechanism residual of +74% beyond metabolic prediction. *R. dentocariosa* is lung-adapted (38% respiratory) with strong inhibition (79%) and a dual-mechanism residual of +57%, plus published evidence for colonization resistance via a secreted endopeptidase (Stubbendieck et al. 2023). *G. sanguinis* contributes strong inhibition (85%) and a +62% residual and adds depth at k=5, but has the smallest pangenome (7 genomes), making strain selection most critical for this species. [src: cf_formulation_design]

The residual attributions are internally inconsistent and left unreconciled: the residual table lists *Neisseria mucosa* ASMA-3643 at +57.2%, while the per-species rationale assigns the +57% dual-mechanism residual to *R. dentocariosa*. [src: cf_formulation_design]

### Prebiotics and pangenome conservation

Selectivity ratios were computed as commensal mean OD divided by PA14 OD, to ask whether any carbon source selectively feeds commensals while starving PA14. The stated substrate count differs between passages and is not reconciled: the methods sentence says ratios were computed for all 20 tested substrates, while the section conclusion refers to the 22 tested substrates. [src: cf_formulation_design]

PA14 outgrew the average commensal on every tested substrate, and no tested amino acid or simple sugar provided a clear commensal growth advantage; the most selective substrates (cysteine, threonine, methionine) had commensal-to-PA14 ratios of only 0.77–0.96. The report concludes that among the 22 tested substrates no selective prebiotic exists, so competitive exclusion must work through community-level resource depletion — multiple organisms collectively consuming the resource pool faster than PA14 alone — rather than individual substrate advantage, and this null motivated the genomic search for untested substrates. [src: cf_formulation_design]

![Carbon source selectivity ratios — no substrate favors commensals over PA14](figures/06_prebiotic_selectivity.png)
[src: cf_formulation_design]

Because no tested amino acid served as a selective prebiotic, the search was expanded genomically: GapMind predicts pathway completeness for approximately 80 carbon and amino-acid pathways, many of them not among the 22 tested substrates, and these predictions were compared between the five core commensals and *P. aeruginosa* across the pangenome. [src: cf_formulation_design]

Genomic pathway comparison identified six pathways complete in at least one core commensal species but absent or nearly absent in PA14: myoinositol, xylitol, xylose, arabinose, fucose, and rhamnose. PA pathway completeness was 0% for myoinositol, xylitol, xylose, and arabinose, and 1% for fucose and rhamnose; corresponding selectivity values were 1.00 for the first four and 0.99 for the latter two. Each of these pathways is carried by only 1–2 of the 5 core species, so they are species-specific capabilities rather than consortium-wide ones. Patient metatranscriptomics additionally identified 47 KEGG (Kyoto Encyclopedia of Genes and Genomes) pathways with a >2× commensal-to-PA expression ratio in vivo, dominated by PTS (phosphotransferase system) sugar transport systems — maltose, trehalose, and N-acetylmuramic acid — that the report describes as exclusively commensal-expressed. [src: cf_formulation_design]

Per pathway, the reported PA completeness, commensal carriers, and selectivity were: myoinositol, PA 0%, *R. dentocariosa* (100%), selectivity 1.00; xylitol, PA 0%, *S. salivarius* (98%) and *G. sanguinis* (100%), selectivity 1.00; xylose, PA 0%, *N. mucosa* (100%) and *G. sanguinis* (100%), selectivity 1.00; arabinose, PA 0%, *N. mucosa* (100%) and *G. sanguinis* (100%), selectivity 1.00; fucose, PA 1%, *N. mucosa* (100%) and *G. sanguinis* (100%), selectivity 0.99; and rhamnose, PA 1%, *N. mucosa* (100%) and *G. sanguinis* (100%), selectivity 0.99. [src: cf_formulation_design]

![Pathway completeness: PA14 vs core commensals](figures/09_pathway_selectivity_heatmap.png)
[src: cf_formulation_design]

The report's summary-level phrasing identifies sugar alcohols (xylitol, myoinositol, arabinose, xylose) as candidate prebiotics — substrates commensals can metabolize but PA14 cannot — whereas its pathway section instead groups xylitol and myoinositol as sugar alcohols and xylose, arabinose, fucose and rhamnose as pentoses; the two classifications are inconsistent within the report and are not reconciled here. The proposed prebiotic strategy therefore shifts from amino-acid competition to sugar alcohols and pentoses: xylitol is predicted to support *S. salivarius*, myoinositol to support *R. dentocariosa*, and xylose and arabinose to support *N. mucosa* and *G. sanguinis*. From the per-species specificity the report draws a pairing rule — xylitol benefits *S. salivarius*, the top inhibitor, while xylose, arabinose, and fucose benefit *N. mucosa*, the engraftment anchor, and *G. sanguinis* — and suggests the hypothesis that a multi-prebiotic cocktail targeting different formulation members may be more effective than a single prebiotic. These predictions require experimental validation before use. [src: cf_formulation_design]

The report's prebiotic conclusion nominates sugar alcohols (xylitol, myoinositol) and pentoses (xylose, arabinose, fucose, rhamnose) as strong candidates on five stated grounds: genomic completeness in the formulation species, absence from PA14's metabolic repertoire, active transport by commensals in patient airways, commercial availability and FDA-GRAS status, and, for xylitol, existing use in CF airway products for other indications. This is a nomination from genomic and expression evidence rather than demonstrated selective growth; the absence claim concerns the PA14 strain, whereas the 1% completeness reported for fucose and rhamnose concerns the broader PA genome collection and does not contradict PA14-specific absence. [src: cf_formulation_design]

The conservation analysis asks whether a design built on the carbon-utilization profiles of specific PROTECT isolates would fail when different strains of the same species are used clinically; GapMind pathway conservation was therefore examined across 499 pangenome genomes of the five core species. [src: cf_formulation_design]

GapMind pathway conservation across 499 genomes supported species-level robustness. Each count below is the number of pathways conserved at >95% within that species, and the parenthetical percentage is the fraction of that species' pathways meeting the >95% criterion — not a genome-level conservation level. *M. luteus* had 18/18 (100%) amino-acid pathways and 39/39 (100%) carbon pathways across 295 genomes; *S. salivarius* had 18/18 (100%) and 32/35 (91%) across 153 genomes; *R. dentocariosa* had 14/18 (78%) and 39/41 (95%) across 29 genomes; *N. mucosa* had 16/16 (100%) and 27/27 (100%) across 15 genomes; and *G. sanguinis* had 7/18 (39%) and 37/39 (95%) across only 7 genomes. The *N. mucosa* denominators differ between sections of the report — 16/16 in the conservation table versus 16/18 in the core-species profile — and the report does not reconcile them. [src: cf_formulation_design]

![Amino acid pathway conservation heatmap](figures/07_aa_pathway_conservation.png)
![Carbon source pathway conservation heatmap](figures/07_carbon_pathway_conservation.png)
[src: cf_formulation_design]

The report treats this as strong support for its conservation hypothesis: the measured metabolic capabilities are species-level traits conserved across hundreds of genomes, so for four of the five species any well-characterized strain should provide equivalent metabolic competition. *G. sanguinis* is the exception, showing the most pathway variability alongside its small 7-genome pangenome, so the report concludes that strain selection matters most for that species. [src: cf_formulation_design]

The report summarizes these as species-level traits (>95% conservation across hundreds of genomes), with two anchor species, *R. dentocariosa* and *N. mucosa*, naturally lung-adapted (33–38% of pangenome genomes from respiratory sources). Of 21 lung/respiratory genomes identified, *R. dentocariosa* contributes 10 (38% of its species) and *N. mucosa* contributes 5 (33%), which the report reads as these being naturally respiratory organisms rather than gut commensals being repurposed; *M. luteus*, with 0 lung genomes, is primarily skin/environmental and may face engraftment challenges despite its metabolic contribution. Lung-adapted *S. salivarius* genomes show enrichment for L-malate (+0.39 score) and depletion for sorbitol (−0.82), suggesting metabolic adaptation to the airway carbon landscape. [src: cf_formulation_design]

The report notes this is consistent with prior work: Rigauts et al. (2022) showed *Rothia mucilaginosa* enrichment in healthy airways, and Stubbendieck et al. (2023) demonstrated *R. dentocariosa*-mediated colonization resistance in the nasal tract. [src: cf_formulation_design]

### Pairwise interactions and PA diversity

Formulation scoring assumes additive inhibition — a combination's effect equals the mean of its members — so synergy would mean the scores underestimate and antagonism that they overestimate. The assay's stated scope is internally inconsistent and unreconciled: the rationale says the competition assay tested 3 commensal pairs against PA14 at multiple inoculation densities, while the results table and conclusion report 5 unique pairs. [src: cf_formulation_design]

Pairwise competition data showed mean synergy scores of +5.3% for *N. mucosa* + ASMA-2260 (47% mean pair inhibition versus 42% best single), +1.4% for ASMA-3913 + ASMA-2260 (52% versus 51%), −2.2% for *N. mucosa* + ASMA-2464 (40% versus 42%), −14.2% for ASMA-3913 + ASMA-2464 (37% versus 51%), and −19.8% for ASMA-1478 + ASMA-1197 (−3% versus 17%). Overall mean synergy was −5.8%, indicating mildly antagonistic interactions on average, but the analysis included only 8 comparisons across 5 unique pairs — an underpowered sample — so additive formulation scoring remains provisional until the complete 10-pair interaction matrix for the five-species core is measured. The report reads this pattern as near-additive inhibition for *N. mucosa* combinations, supporting its role as a formulation anchor that does not interfere with partners, with strong antagonism in some pairs (ASMA-1478 + ASMA-1197 at −19.8%) highlighting the need to test specific combinations; it uses this to decide which combinations to advance to mouse models. [src: cf_formulation_design]

![Single vs pair inhibition distributions, and synergy score distribution](figures/08_pair_vs_single_inhibition.png)
![Dose-response: pair inhibition vs total inoculation density](figures/08_dose_response_pairs.png)
[src: cf_formulation_design]

### PA pangenome: target conservation and metabolic streamlining

Across 1,796 lung or respiratory PA genomes, amino-acid catabolic pathways were 97.4% conserved (mean completeness), and proline utilization — PA14's top substrate — was complete in 97% of lung isolates. The main axis of variation among lung PA (PC1 = 79% of variance in principal-component analysis) lay instead in carbon-source pathways that the formulation does not target, which the report reads as evidence that its amino-acid targets are robust across lung PA. [src: cf_formulation_design]

The lung-versus-non-lung comparison drew on 6,760 PA genomes, 5,199 of them with metadata, of which 1,796 came from lung/respiratory or CF sources. Seven GapMind pathways differed significantly (FDR < 0.05; FDR = false discovery rate, the expected fraction of false positives among calls declared significant) between lung and non-lung PA, and all were carbon-source pathways that lung PA is losing: sorbitol (−0.165), mannitol (−0.204), and gluconate (−0.185), consistent with metabolic streamlining toward amino-acid dependence. The report's further claim that this reflects relaxed selection on sugar catabolism in amino-acid-rich sputum, and so validates PA's amino-acid dependence as an evolutionary adaptation, is an interpretation of the pathway differences rather than a measured evolutionary result. [src: cf_formulation_design]

![PA genome sources in pangenome](figures/10_pa_genome_sources.png)
![PA metabolic pathways by isolation source](figures/10_pa_lung_vs_nonlung_pathways.png)
![Formulation target robustness across lung PA](figures/10_pa_target_robustness.png)
[src: cf_formulation_design]

Patient metatranscriptomics showed that during acute exacerbation PA downregulated 170 of 207 measured pathways, including amino-acid biosynthesis (cysteine and methionine 10× lower) and imipenem resistance (OprD 13× lower), with only phosphate transport upregulated (64×). The report infers that such metabolically quiescent PA, dependent on scavenging host-derived amino acids, is potentially more vulnerable to competitive exclusion during acute episodes; that vulnerability is a stated possibility, not a demonstrated effect. [src: cf_formulation_design]

![PA pathway expression: acute vs stable patients](figures/10_pa_sick_vs_stable_pathways.png)
[src: cf_formulation_design]

Within lung PA the report describes two metabolic subpopulations: a major cluster of 1,743 genomes (97%) with full metabolic capacity and a minor cluster of 53 genomes (3%) lacking TCA-cycle intermediates. The minor cluster is CF-enriched (25% CF versus 16%) and is proposed to represent chronically adapted PA that is even more dependent on external metabolites and potentially more vulnerable to competitive exclusion; that interpretation is speculative. [src: cf_formulation_design]

CF-derived PA showed 6 FDR-significant differences from non-CF lung PA, but all were in sugar-related pathways and there were zero amino-acid differences. From this null the report infers that formulations designed for general lung PA should work equivalently for CF PA; the inference is not tested here. [src: cf_formulation_design]

![PA lung metabolic subpopulations and CF vs non-CF](figures/10_pa_lung_clusters.png)
[src: cf_formulation_design]

Within the PROTECT collection, the 15 PA strain groups span genome sizes from 6.12 Mb (5,668 CDS, protein-coding sequences) to 7.35 Mb (7,026 CDS) — a 24% difference in gene content — and the largest strain group (725, 98 isolates) carries 1,358 extra genes compared with the smallest. [src: cf_formulation_design]

Because all strain groups retain the same amino-acid catabolic pathways (97%+ conservation), the report argues the extra genes are likely conditionally expressed accessory functions — prophages, mobile elements, niche-specific adaptations — that affect virulence and persistence rather than amino-acid growth rate, citing Vieira-Silva & Rocha (2010) that within-species genome-size variation is a much weaker predictor of growth rate than cross-species variation. It therefore predicts that PA strains will respond similarly to the formulation, with strain differences expected in virulence, antibiotic resistance and biofilm properties instead; this is a prediction from pathway conservation, not a measured outcome. [src: cf_formulation_design]

![PROTECT PA genome variation (655 isolates, 15 strain groups)](figures/10_protect_pa_genome_variation.png)
[src: cf_formulation_design]

PA's genome (6.58 Mb, 6,177 CDS) is 2.5–3× larger than the commensal species used here (2.1–2.7 Mb, 2,200–3,000 CDS). Despite that size difference, the growth-curve data show PA14 outgrowing most commensals on its preferred amino-acid substrates, which the report reads as confirming that PA's catabolic enzyme efficiency, not its ribosomal translation rate, drives its competitive advantage on amino acids — an interpretation of the growth data rather than a direct enzymatic measurement. Its codon-usage-bias analysis of ribosomal proteins varied across species, but that cross-species comparison is confounded by GC content ranging from 31% for *G. sanguinis* to 73% for *M. luteus*, so it cannot reliably distinguish growth-rate differences between these species; the laboratory growth data remains the report's definitive measure of competitive dynamics on amino-acid substrates. [src: cf_formulation_design]

Codon usage bias (CUB — the preferential use of particular synonymous codons, often read as a proxy for growth-rate optimization) varied across species in ribosomal proteins, but cross-species CUB comparison is confounded by GC content, which ranges from 31% for *G. sanguinis* to 73% for *M. luteus*; organisms with extreme GC composition have inflated CUB scores regardless of growth optimization. The report therefore concludes that CUB cannot reliably distinguish growth-rate differences or growth-rate potential among these species, and both the results and the discussion treat the laboratory growth data as the definitive, ground-truth measure of competitive dynamics on amino-acid substrates. [src: cf_formulation_design]

![Growth rate prediction: CUB scores and genome size for PA vs commensals](figures/12_growth_rate_prediction.png)
[src: cf_formulation_design]

### PA virulence typing and reference-strain representativeness

PA14 and PAO1 differ qualitatively in T3SS (type III secretion system) effectors (ExoU versus ExoS), biofilm polysaccharides (Pel-only versus Pel+Psl), and regulatory state (the ladS mutation), which is the rationale for asking how representative PA14 is of CF PA. [src: cf_formulation_design]

Across 6,760 PA genomes, with environmental metadata for 4,769, T3SS effector typing revealed a gradient by environment: CF patient isolates were 94% ExoS+, 5% ExoU+ and 0% both (n = 291); lung/respiratory isolates were 82%, 16% and 1% (n = 1,505); other clinical isolates were 63%, 33% and 3% (n = 1,731); and environmental isolates were 62%, 35% and 1% (n = 370). [src: cf_formulation_design]

CF PA is therefore overwhelmingly ExoS+, and the PA14 ExoU+ phenotype represents only 5% of CF isolates. The report notes that ExoU prevalence increases in acute/invasive infection contexts (33% in other clinical, 35% in environmental) and reads this as consistent with ExoU acting as an acute cytotoxic effector rather than a chronic colonization factor; that reading is an interpretation of the distribution. [src: cf_formulation_design]

![T3SS effector type and biofilm polysaccharide distribution by environment](figures/13_t3ss_by_environment.png)
[src: cf_formulation_design]

The PA amino-acid target set showed no detectable difference across virulence backgrounds: amino-acid catabolic pathways did not differ significantly between ExoU+ and ExoS+ PA, with GapMind score differences <0.03 on a 1–5 scale and zero FDR-significant pathways. The report itself describes these pathways as "identical", but that wording is its interpretation — sub-threshold score differences and zero significant calls are a statistical null, not established identity. CF PA was 94% ExoS+ and 5% ExoU+ among 291 CF genomes, whereas PA14 is ExoU+; 96.4% of PA genomes carried both Pel and Psl operons, and only 3.5% were Pel-only. [src: cf_formulation_design]

Among regulatory genes, ladS was detected in only 0.5% of PA genomes by bakta annotation. The report treats PA14's ladS frameshift mutation as an extreme outlier that locks it into an acute-virulence regulatory state unrepresentative of natural infection dynamics; the detection rate is annotation-qualified and the outlier characterization is the report's interpretation rather than a measured regulatory phenotype. [src: cf_formulation_design]

![PA virulence systems summary across environments](figures/13_pa_virulence_summary.png)
[src: cf_formulation_design]

The report draws a formulation implication from this: its PA14-based inhibition assays tested the formulation against a minority (<5%) CF PA variant. It argues the dominance of ExoS+ PA in CF lungs is favorable because ExoS mediates slower, apoptotic killing versus ExoU's rapid cytotoxic lysis, potentially providing a wider time window for competitive exclusion — a proposed, not measured, advantage — and it elevates Proposed Experiment 4.6 (PAO1 and clinical-strain extension) in importance, since confirming inhibition against ExoS+ strains is essential. [src: cf_formulation_design]

In the PROTECT collection (651 PA genomes), 47% carried exoS and 7% carried exoU, with 45% unannotated for T3SS effectors; the report attributes the unannotated fraction to an annotation coverage gap for GenomeDepot gene names rather than to absence of the effectors. [src: cf_formulation_design]

![PROTECT PA virulence gene prevalence](figures/13_protect_pa_virulence.png)
[src: cf_formulation_design]

All 643 annotated PROTECT PA genomes were profiled for 32 virulence genes spanning T3SS effectors, biofilm operons, alginate biosynthesis, quorum sensing, iron acquisition and T6SS, and each isolate was classified as PAO1-like, PA14-like or intermediate from its ExoU/ExoS status, biofilm architecture and ladS presence: 304 (47%) were PAO1-like (ExoS+), 48 (7%) were PA14-like (ExoU+), and 291 (45%) were intermediate, lacking clear T3SS annotation in GenomeDepot. Among classifiable isolates, 86% were PAO1-like, which the report reads as confirming at individual-isolate level that PA14 is not representative of the PROTECT CF collection. [src: cf_formulation_design]

Strain-group assignment was strongly correlated with virulence type — entire strain groups were either uniformly PAO1-like or uniformly PA14-like — which the report reads as indicating that T3SS effector type is a clonal trait inherited within lineages rather than a horizontally transferred variable. [src: cf_formulation_design]

![ASMA PA virulence profiles: T3SS, model similarity, gene prevalence, and strain group breakdown](figures/14_asma_virulence_profiles.png)
[src: cf_formulation_design]

Cross-database comparison relied on Pfam protein domain profiles as a pipeline-independent vocabulary, because PROTECT genomes (annotated by GenomeDepot) and pangenome genomes (annotated by bakta/eggNOG) use different annotation pipelines, making gene names unreliable across databases; Pfam domain IDs are standardized, with 2,850 domains shared between the two databases and ~3,200 unique domains per PA genome. [src: cf_formulation_design]

The resulting Pfam-based tree spans 165 PA genomes — 13 PROTECT strain-group representatives, 150 sampled lung/airway PA from the pangenome, and the PAO1 and PA14 reference strains — with Jaccard distances computed on 1,557 variable Pfam domains present in 5–95% of genomes to resolve the accessory-genome variation that distinguishes PAO1-like from PA14-like strains. [src: cf_formulation_design]

![Circular Pfam-based tree: 165 PA genomes annotated with T3SS type, biofilm, source, and identity. ASMA isolates (red) distributed across lung PA diversity.](figures/14_pa_phylogenetic_tree.png)
[src: cf_formulation_design]

In that tree the PROTECT isolates were distributed across the broader lung-PA diversity rather than clustering in a single lineage, which the report reads as confirming that the PROTECT collection samples the breadth of CF PA genomic variation. ExoU+ isolates clustered separately from the ExoS+ majority; the report's attribution of this split to PAPI-1/PAPI-2 pathogenicity-island acquisition as a deep phylogenetic event is interpretive. [src: cf_formulation_design]

The Newick tree file (`data/pa_pfam_tree.nwk`) is retained so the tree can be re-visualized with alternative annotation schemes as new metadata becomes available. [src: cf_formulation_design]

### Mechanistic synthesis and design tensions

The discussion frames three mechanisms. The first, metabolic competition, is quoted as approximately 27% of variance — direct resource depletion of PA14's preferred amino-acid substrates, the "eat their lunch" mechanism. That figure is shorthand for the four-feature multivariate model's training R² = 0.274, not for the metabolic-overlap correlation alone (r = 0.384), and the five-fold cross-validation reported above (CV R² = 0.145 ± 0.142) identifies overfitting within the 142-isolate cohort, so out-of-sample explanatory power is lower than the headline number. [src: cf_formulation_design]

The second mechanism, direct antagonism, is credited in the discussion with an additional 9% from taxonomy, rounded from the 8.6% reported in the modelling section. Bacteriocins, secreted enzymes (Stubbendieck et al. 2023) and contact-dependent killing are offered as proposed rather than established explanations; the top formulation species — *S. salivarius*, *N. mucosa* and *G. sanguinis* — all show strong positive residuals in the metabolic model. [src: cf_formulation_design]

The third mechanism, community-level niche saturation, is presented as an emergent community property not predictable from individual organism profiles: a 3–5 organism consortium collectively covers 100% of PA14's metabolic niche even though, the discussion asserts categorically, no individual commensal outgrows PA14 on any tested substrate. That assertion is in tension with the report's own finding of a commensal growth-rate advantage in 13.8% of pairwise comparisons; whether "outgrows" refers to another metric or comparison set is left unresolved, and niche coverage is in any case distinct from relative growth rate. [src: cf_formulation_design]

The remaining 64% of variance is, in the report's words, likely attributable to unmeasured factors — biofilm dynamics, pH effects, iron competition, quorum-sensing interference and stochastic variation in the planktonic assay. These are offered as possible contributors rather than an established attribution; none of them were measured here. [src: cf_formulation_design]

The report also states the central obstacle plainly: PA14 outgrows most commensals on its preferred amino-acid substrates, with only 13.8% of pairwise comparisons showing a commensal rate advantage, an advantage it attributes to PA's specialized amino-acid catabolic enzymes. This restates the unreconciled tension with the summary-level claim that no individual commensal outgrows PA14 on any tested substrate. [src: cf_formulation_design]

Against that obstacle the report sets the lag advantage: commensals have a lag advantage in 43.1% of comparisons, starting to grow before PA14, so delivering commensals before pathogen exposure — or boosting them with prebiotics first — could exploit that window. [src: cf_formulation_design]

It further argues that community biomass matters more than individual growth rate, illustrating the point with a three-organism consortium each growing at half PA14's rate that would still deplete resources 1.5× faster collectively; this is an illustrative arithmetic argument rather than a measurement, although the k=3 formulation's 100% niche coverage is a reported result. [src: cf_formulation_design]

Third, the discussion argues PA's amino-acid catabolism is invariant across strains: all 15 PROTECT strain groups retain the same core pathways at 97%+ conservation, and although genome sizes range from 6.1–7.4 Mb (24% gene-content variation), the extra genes are taken to be accessory functions such as prophages and resistance islands. From this the report predicts the formulation should be equally effective across PA variants, with strain-level variation mattering for virulence, biofilm formation and antibiotic resistance instead; equal efficacy across variants remains a prediction, not a measured result. [src: cf_formulation_design]

The sharpest design tension is *M. luteus*: it is the keystone species for niche coverage, since its addition at k=3 is what achieves 100% PA substrate coverage, yet it has zero engraftability — not detected in any patient metagenome — and zero lung genomes in the pangenome, being primarily skin/environmental. The species most important for metabolic coverage is thus the least likely to persist in the lung. [src: cf_formulation_design]

Three paths forward are considered: accept the risk and test k=3 in mice, on the possibility that *M. luteus*'s broad carbon utilization compensates for low natural prevalence if delivered at sufficient dose; prioritize the k=2 formulation (*R. dentocariosa* + *N. mucosa*, combined 84% inhibition and 0.820 engraftability), sacrificing niche coverage for colonization reliability; or search for an alternative broad-spectrum metabolizer among lung-adapted species to replace *M. luteus*'s niche-coverage role. Successful k=3 engraftment remains speculative. [src: cf_formulation_design]

The report records the complete absence of selective amino-acid prebiotics as a key surprise, attributing it to PA14 being simply too metabolically versatile on amino acids. Its genomic extension then suggests an entirely different strategy: sugar alcohols and pentoses that the genomic analysis predicts commensals can metabolize and PA14 cannot, which would shift the design from competing on PA14's turf to feeding the consortium on a field PA14 is predicted not to access. Xylitol is nominated as a particularly attractive candidate because it is already FDA-approved for CF airway use (mucolytic/antimicrobial properties), creating what the report calls a dual-purpose prebiotic opportunity; selective commensal growth on these substrates is a genomic prediction and remains experimentally unvalidated. [src: cf_formulation_design]

### Relation to prior work

*R. dentocariosa*'s high inhibition residuals are explained by analogy to prior work rather than by mechanism measured here: Rigauts et al. (2022) showed *Rothia mucilaginosa* suppressing NF-κB inflammation in CF airways, and Stubbendieck et al. (2023) identified a *R. dentocariosa* peptidoglycan endopeptidase that inhibits *Moraxella catarrhalis*. The report's statement that its *R. dentocariosa* isolates likely employ similar mechanisms is extrapolated from inhibition of a different target organism and was not demonstrated against PA in this work. [src: cf_formulation_design]

The community-level niche-coverage model is positioned as operationalizing prior CF community ecology for therapeutic design: Widder et al. (2022) identified eight pulmotypes driven by ecological competition, and Rogers et al. (2015) demonstrated competitive exclusion between PA and *H. influenzae* in bronchiectasis, which the report cites as support for the ecological framework. [src: cf_formulation_design]

On probiotic precedent, Anderson et al. (2017) reviewed CF probiotic trials and found suggestive but inconclusive results, attributed partly to a lack of rational strain selection that this report's multi-criterion optimization is intended to address; *S. salivarius* BLIS K12 is cited as having established respiratory probiotic credentials (Tagg et al. 2025; Burton et al. 2011). [src: cf_formulation_design]

The >95% metabolic conservation found here is explicitly contrasted with Shao et al. (2026), whose pangenome-guided *Bifidobacterium* probiotic design found strong strain-level functional divergence requiring careful strain selection; the report presents its own result as the opposite scenario and equally valuable for translational confidence. [src: cf_formulation_design]

Xylitol's proposed delivery route and safety profile rest on clinical precedent: Durairaj et al. (2007) demonstrated safety of inhaled xylitol in CF patients, and Singh et al. (2020) conducted a randomized controlled trial of aerosolized hypertonic xylitol versus saline during CF exacerbations. [src: cf_formulation_design]

## Caveats and Limitations

The inhibition assays were planktonic and used PA14, whereas PA in cystic-fibrosis lungs primarily occupies structured biofilms. The carbon panel contained 22 tested substrates and omitted mucins, lipids, iron, polyamines, and the sugar alcohols identified genomically. [src: cf_formulation_design]

The metabolic model was based on 142 isolates covering 62 of 211 species (29%), and growth kinetics were available for only 32 isolates; the core cohort was enriched for deeply characterized taxa, including *Rothia*, *Streptococcus*, *Neisseria*, and *Gemella*. [src: cf_formulation_design]

Pairwise interaction data covered only 3 A × 3 B isolate combinations, and the complete 10-pair interaction matrix for the five-species core has not been measured. Moreover, `fact_pairwise_interaction` was identical to `fact_carbon_utilization`, with correlation = 1.0 and mean difference = 0.0, so endpoint OD data cannot assess per-substrate co-culture effects; current interaction conclusions rely on the RFU-based competition assay. [src: cf_formulation_design]

Engraftability was inferred from patient prevalence and transcriptional activity rather than measured after administration. Only 21 lung genomes across 5 species were available for lung-adaptation comparisons, and *M. luteus* had zero lung genomes and zero detected patient engraftability despite its central role in achieving 100% niche coverage. [src: cf_formulation_design]

PA14-based inhibition measurements have not been validated against PAO1 or ExoS+ clinical strains, although the pangenome analysis found no amino-acid pathway differences between ExoU+ and ExoS+ PA. The report therefore prioritizes testing PAO1 and 3–5 mucoid clinical PA isolates. [src: cf_formulation_design]

The primary *N. mucosa* conservation analysis used a 15-genome clade even though the PROTECT reference mapped to an 8-genome clade; the 8-genome sensitivity check showed stronger conservation, with 18/18 amino-acid pathways at >95% versus 16/18 in the 15-genome clade, 37/62 carbon pathways versus 27/62, and 1 respiratory genome. [src: cf_formulation_design]

## Slots Into

- [[concepts/condition-specific-fitness]] — links substrate-specific growth, lag advantage, inhibition, engraftability, and PA lung adaptation to condition-dependent competitive fitness. [src: cf_formulation_design]
- [[concepts/multi-omics-integration]] — integrates inhibition, carbon utilization, growth kinetics, metagenomics, metatranscriptomics, and pangenome pathway predictions in formulation design. [src: cf_formulation_design]
- [[concepts/pangenome-integration]] — uses 499 commensal genomes and 1,796 lung PA genomes to assess pathway conservation, lung adaptation, and formulation robustness, with Pfam domains substituted for gene names across annotation pipelines. [src: cf_formulation_design]
- [[concepts/metabolic-model-gapfilling]] — applies GapMind pathway completeness comparisons to identify metabolic gaps between PA14 and candidate commensals, including selective prebiotic targets. [src: cf_formulation_design]
- [[concepts/cofitness-network-architecture]] — contributes pairwise inhibition and synergy measurements showing near-additive *N. mucosa* interactions and antagonistic pairs. [src: cf_formulation_design]
- [[concepts/competitive-exclusion-consortium-design]] — metabolic overlap predicts PA14 inhibition significantly but incompletely, so consortium design needs community niche coverage plus direct antagonism and an engraftability criterion. [src: cf_formulation_design]
- [[concepts/capability-versus-kinetic-predictability]] — kinetic parameters correlate only moderately with endpoint OD and add little to capability-based inhibition models, which overfit in cross-validation. [src: cf_formulation_design]
- [[concepts/computational-pathway-prediction-validation]] — GapMind-predicted sugar-alcohol and pentose prebiotic targets remain genomic predictions awaiting experimental validation. [src: cf_formulation_design]
- [[concepts/taxonomic-nomenclature-reconciliation]] — GTDB names used here diverge from NCBI, with *Pseudomonas_E* a non-aeruginosa clade that must not be merged with *P. aeruginosa*. [src: cf_formulation_design]
- [[concepts/adversarial-research-quality-assurance]] — internal count inconsistencies (21 versus 22 substrates; CF plus NCFB subtotals versus the 175-sample total) and discussion-level rounding of model statistics surface only on cross-checking the report's own tables. [src: cf_formulation_design]
- [[concepts/cultivation-collection-bias-in-ecological-genomics]] — deliberate pathogen oversampling makes isolate-collection frequencies unusable as natural prevalence estimates, and the keystone *M. luteus* is absent from patient metagenomes entirely. [src: cf_formulation_design]
- [[concepts/phylogenetic-confounding-of-pangenome-associations]] — adding genus-level taxonomy raises explained inhibition variance by 8.6%, and PA strain groups are uniformly one virulence type, so lineage carries signal beyond measured features. [src: cf_formulation_design]
- [[concepts/sample-size-aware-phenotype-consensus]] — pathway-conservation calls rest on pangenomes ranging from 295 genomes (*M. luteus*) to 7 (*G. sanguinis*), and the smallest clade shows the most apparent pathway variability. [src: cf_formulation_design]
- [[concepts/pangenome-core-boundary-and-clade-size-bias]] — *G. sanguinis*'s 7-genome pangenome yields 7/18 conserved amino-acid pathways against 37/39 carbon pathways; whether clade size drives this apparent variability is an unresolved sampling concern here, not an effect the report analyzes. [src: cf_formulation_design]
- [[concepts/callability-limited-comparative-inference]] — `fact_pairwise_interaction` duplicated `fact_carbon_utilization` (correlation = 1.0), and 45% of PROTECT PA genomes are unannotated for T3SS effectors, so both co-culture effects and effector status are partly uncallable. [src: cf_formulation_design]
- [[concepts/reference-strain-representativeness]] — PA14 is ExoU+ while CF PA is 94% ExoS+ and 86% of classifiable PROTECT isolates are PAO1-like, so the assay strain is a minority variant. [src: cf_formulation_design]
- [[concepts/ecotype-environment-gene-content]] — T3SS effector frequencies grade from CF to environmental sources and lung PA loses sugar pathways, tying gene content to isolation environment. [src: cf_formulation_design]
- [[concepts/ecotype-clustering-validity]] — the 1,743-genome major and 53-genome minor lung-PA clusters rest on pathway-completeness clustering with a CF-enrichment contrast of 25% versus 16%. [src: cf_formulation_design]
- [[concepts/within-species-conservation-between-species-functional-divergence]] — amino-acid catabolism is 97.4% conserved across lung PA while carbon pathways carry the variation, and commensal core species conserve pathways at >95%. [src: cf_formulation_design]
- [[concepts/two-speed-bacterial-genome]] — 24% gene-content variation across PROTECT PA strain groups coexists with invariant core amino-acid catabolism. [src: cf_formulation_design]
- [[concepts/functional-marker-validation]] — codon usage bias fails as a cross-species growth-rate marker here because GC content spans 31–73%. [src: cf_formulation_design]
- [[concepts/homology-search-negative-evidence]] — ladS detected in only 0.5% of PA genomes by bakta annotation is an annotation-limited absence, not established gene loss. [src: cf_formulation_design]
- [[concepts/genome-wide-versus-locus-specific-ecological-adaptation]] — ExoU+ and ExoS+ PA differ at a virulence locus and in tree position while genome-wide amino-acid catabolism shows no significant difference. [src: cf_formulation_design]
- [[concepts/cross-condition-metabolic-comparability]] — PA14's substrate ranking is read as mirroring SCFM composition, the report's basis for treating its assay conditions as comparable to sputum. [src: cf_formulation_design]
- [[concepts/occurrence-versus-catabolic-activity]] — prebiotic nominations rest on genomic pathway presence plus transcript ratios rather than measured catabolism of those substrates. [src: cf_formulation_design]
