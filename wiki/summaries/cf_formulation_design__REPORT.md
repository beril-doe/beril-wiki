---
type: "Summary"
description: "Summary of the project Rational Design of Protective Microbiome Formulations for Competitive Exclusion of *Pseudomonas aeruginosa* in Cystic Fibrosis Airways."
doc_type: "short"
full_text: "sources/cf_formulation_design__REPORT.md"
---
# Rational Design of Protective Microbiome Formulations for Competitive Exclusion of *Pseudomonas aeruginosa* in Cystic Fibrosis Airways

This page summarises a project that asked whether rationally designed commensal communities can suppress *Pseudomonas aeruginosa* in cystic fibrosis (CF) airways through metabolic competitive exclusion, by consuming the amino acid carbon sources that PA14 depends on. [src: cf_formulation_design] The motivation is that chronic *P. aeruginosa* infection is the primary driver of lung function decline in CF. [src: cf_formulation_design] Metabolic overlap with PA14 significantly predicts inhibition but explains only part of the variance, and the strongest inhibitors combine metabolic competition with direct antagonism. [src: cf_formulation_design] The report also states that community-level niche coverage is required, because no individual commensal outgrows PA14 on any tested substrate. [src: cf_formulation_design] The analysis integrates several assay types, patient metagenomics and a pangenome analysis. [src: cf_formulation_design]

## Key Findings

### Metabolic overlap predicts inhibition only partly

Across the integrated analysis, metabolic overlap with PA14 significantly predicts inhibition (r = 0.384, p = 2.3×10⁻⁶). [src: cf_formulation_design] It explains only 27% of variance. [src: cf_formulation_design] The strongest inhibitors combine metabolic competition with direct antagonism mechanisms. [src: cf_formulation_design] The analysis integrated planktonic inhibition assays (220 isolates), carbon source utilization profiling (430 isolates × 21 substrates), growth kinetics (32 isolates), patient metagenomics (175 samples), pairwise interaction data and pangenome analysis (499 genomes across 6 species). [src: cf_formulation_design] See [[concepts/metabolic-competition-versus-direct-antagonism-in-pathogen-inhibition]].

### Community-level coverage and a candidate formulation

No individual commensal outgrows PA14 on any tested substrate, which the report says requires community-level niche coverage. [src: cf_formulation_design] Multi-criterion optimization identifies a five-organism FDA-safe formulation: *Neisseria mucosa*, *Streptococcus salivarius*, *Micrococcus luteus*, *Rothia dentocariosa* and *Gemella sanguinis*. It achieves 100% coverage of PA14's amino acid niche with 78% mean inhibition. [src: cf_formulation_design] See [[concepts/multi-criterion-design-of-protective-microbiome-formulations]] and [[concepts/community-level-niche-coverage-and-resource-depletion-for-competitive-exclusion]].

### Conservation and lung adaptation

Pangenome analysis confirms the measured metabolic capabilities as species-level traits, with >95% conservation across hundreds of genomes. [src: cf_formulation_design] The two anchor species, *R. dentocariosa* and *N. mucosa*, are described as naturally lung-adapted, with 33–38% of pangenome genomes from respiratory sources. [src: cf_formulation_design] See [[concepts/species-level-conservation-of-metabolic-pathways-across-pangenomes]] and [[concepts/engraftability-and-lung-adaptation-of-candidate-commensals]].

### Candidate prebiotics

Genomic pathway comparison identifies sugar alcohols (xylitol, myoinositol, arabinose, xylose) as candidate prebiotics, meaning substrates commensals can metabolize but PA14 cannot. [src: cf_formulation_design] See [[concepts/selective-prebiotics-for-commensal-consortia]].

### Pairwise interactions

Pairwise testing shows near-additive PA14 inhibition for *N. mucosa* combinations. [src: cf_formulation_design] Some pairs show modest antagonism. [src: cf_formulation_design] The report uses this to inform which combinations to advance to mouse models. [src: cf_formulation_design] See [[concepts/pairwise-interaction-among-commensals-in-competition-assays]].

## Summary; Introduction

This part of the report sets out the clinical problem, the working theory that commensals can exclude the pathogen by consuming its carbon sources, the formulation design criteria and the integrated data. [src: cf_formulation_design]

### Clinical problem and working theory

Chronic *Pseudomonas aeruginosa* infection is the primary driver of lung function decline in cystic fibrosis (CF). [src: cf_formulation_design] The report states that the pathogen chronically colonizes the airways of most CF patients by early adulthood. [src: cf_formulation_design] Once established, it adapts to the lung by switching to amino acid catabolism as its primary carbon source, forming biofilms, and becoming increasingly antibiotic-resistant. [src: cf_formulation_design] Current treatments rely on repeated antibiotic courses that select for resistance and disrupt the commensal microbiome. [src: cf_formulation_design]

The report investigates whether rationally designed commensal communities can suppress *P. aeruginosa* through metabolic competitive exclusion. They would do this by consuming the amino acid carbon sources that PA14 depends on in the CF airway. [src: cf_formulation_design] The working theory is that commensals can exclude the pathogen by consuming its carbon sources. These are primarily proline, histidine, ornithine, glutamate, aspartate and arginine, which are abundant in CF sputum. [src: cf_formulation_design] The report hypothesizes that if a consortium depletes these substrates faster than the pathogen can use them, the pathogen's growth becomes resource-limited. [src: cf_formulation_design] It further hypothesizes that prebiotics, meaning substrates that feed commensals but not the pathogen, could give the consortium a biomass advantage before competition begins. [src: cf_formulation_design]

### Design criteria

The report requires formulations to meet five criteria:

1. Cover the pathogen's metabolic niche. [src: cf_formulation_design]
2. Avoid internal metabolic competition among members. [src: cf_formulation_design]
3. Persist in the patient airway, which is the engraftability criterion. [src: cf_formulation_design]
4. Be FDA-acceptable as live biotherapeutic products. [src: cf_formulation_design]
5. Ideally combine metabolic competition with direct antagonism mechanisms. [src: cf_formulation_design]

### Data integrated

The report integrates experimental data from the PROTECT CF Synbiotic Cocktail Study, with 4,949 isolates from 175 CF/NCFB patient samples. It combines these with the KBase Data Lakehouse pangenome of 293,000 genomes and GapMind metabolic pathway predictions. [src: cf_formulation_design] The analyses include patient metagenomics (175 samples) and a pangenome analysis of 499 genomes across 6 species. [src: cf_formulation_design] Species names follow GTDB taxonomy, which may differ from NCBI names. [src: cf_formulation_design] *Pseudomonas_E* denotes a non-aeruginosa Pseudomonas clade distinct from *P. aeruginosa*. [src: cf_formulation_design]

### Headline results previewed

- Metabolic overlap with PA14 significantly predicts inhibition (r = 0.384, p = 2.3×10⁻⁶). It explains only 27% of variance. [src: cf_formulation_design]
- The strongest inhibitors combine metabolic competition with direct antagonism mechanisms. [src: cf_formulation_design]
- No individual commensal outgrows PA14 on any tested substrate, so community-level niche coverage is required. [src: cf_formulation_design]
- Multi-criterion optimization identifies a five-organism FDA-safe formulation of *Neisseria mucosa*, *Streptococcus salivarius*, *Micrococcus luteus*, *Rothia dentocariosa* and *Gemella sanguinis*. It achieves 100% coverage of PA14's amino acid niche with 78% mean inhibition. [src: cf_formulation_design]
- Pangenome analysis confirms these metabolic capabilities as species-level traits, with >95% conservation across hundreds of genomes. [src: cf_formulation_design]
- The anchor species *R. dentocariosa* and *N. mucosa* are naturally lung-adapted, with 33–38% of pangenome genomes from respiratory sources. [src: cf_formulation_design]
- Genomic pathway comparison identifies xylitol, myoinositol, arabinose and xylose as candidate prebiotics. Commensals can metabolize them but PA14 cannot. [src: cf_formulation_design]
- Pairwise interaction testing reveals near-additive inhibition for *N. mucosa* combinations. [src: cf_formulation_design] It also reveals modest antagonism in some pairs, which informs which combinations to advance to mouse models. [src: cf_formulation_design]

## Results: PA14 Is an Amino Acid Specialist in Synthetic CF Sputum Conditions

This part of the report describes the PROTECT isolate collection, the three assays run on it, and what the assays show about how commensals might compete with or inhibit *Pseudomonas aeruginosa* PA14. Metabolic overlap predicts inhibition significantly, but only modestly out of sample. [src: cf_formulation_design]

### The isolate collection

The PROTECT study produced 23 structured data tables with 30.5M total rows. [src: cf_formulation_design] They cover 4,949 isolates from 211 species across 175 patient samples (133 CF, 41 NCFB, 43 subjects, 4 clinical states). [src: cf_formulation_design] CF is cystic fibrosis. The collection is dominated by *P. aeruginosa* (655 isolates), *S. aureus* (379) and *Rothia dentocariosa* (318). [src: cf_formulation_design] This reflects the typical CF airway microbiome plus deliberate oversampling of pathogens, so the collection is not a random sample of the airway. [src: cf_formulation_design] Genome quality is high, with mean completeness 99.8% and median contamination 0.08%. [src: cf_formulation_design]

Three assays give complementary views of competitive potential. [src: cf_formulation_design] They are planktonic inhibition of PA14 (220 isolates), carbon source utilization profiling (430 isolates on 21 substrates), and growth kinetics (32 isolates with full time-series curves). [src: cf_formulation_design] The core analysis cohort, with both inhibition and carbon utilization data, has 142 isolates from 62 species. [src: cf_formulation_design]

### PA14 carbon utilization

PA14 shows a clear amino acid preference hierarchy in the carbon source utilization assay. [src: cf_formulation_design] The assay tested PA14 and 430 commensal isolates on 20 amino acids plus glucose and lactate. [src: cf_formulation_design] PA14 reached these optical densities (OD):

| Substrate | PA14 OD |
|---|---|
| Proline | 0.60 [src: cf_formulation_design] |
| Histidine | 0.56 [src: cf_formulation_design] |
| Ornithine | 0.46 [src: cf_formulation_design] |
| Glutamate | 0.40 [src: cf_formulation_design] |
| Aspartate | 0.36 [src: cf_formulation_design] |
| Isoleucine | 0.36 [src: cf_formulation_design] |
| Arginine | 0.35 [src: cf_formulation_design] |

Glucose supports only moderate growth (0.22). [src: cf_formulation_design] Threonine, methionine, cysteine, serine and glycine support essentially no growth (<0.07). [src: cf_formulation_design] The report reads this profile as consistent with amino acid-rich CF sputum and as validating the metabolic relevance of the assay conditions. [src: cf_formulation_design]

*A. baumannii* and *K. pneumoniae* show distinct profiles. [src: cf_formulation_design] PA14's amino acid specialization is therefore not universal among CF pathogens, which suggests formulations may need to be pathogen-specific. [src: cf_formulation_design]

### Metabolic overlap and inhibition

Across the 142-isolate cohort, metabolic overlap with PA14, weighted by PA14's substrate preferences, significantly predicts planktonic inhibition (r = 0.384, p = 2.3×10⁻⁶). [src: cf_formulation_design] A multivariate model uses metabolic overlap, total growth on PA-preferred substrates, metabolic breadth and maximum growth. It explains R² = 0.274. [src: cf_formulation_design] Adding genus-level taxonomy raises this to R² = 0.360. The report reads the extra 8.6% of variance as intrinsic species-level mechanisms, likely direct antagonism, acting independently of metabolism. [src: cf_formulation_design]

Cross-validation (CV) limits this result. Five-fold CV gives R² = 0.145 ± 0.142, below the training R² of 0.274, which indicates overfitting to the 142-isolate cohort. [src: cf_formulation_design] The report puts true out-of-sample predictive power closer to 15% than 27%. It says the qualitative conclusion stands but the effect size should be read conservatively. [src: cf_formulation_design] The report judges hypothesis H1 (metabolic competition) supported but incomplete, with approximately 73% of variance unexplained by metabolism alone. [src: cf_formulation_design]

Isolates whose inhibition substantially exceeds metabolic predictions are candidate direct antagonists. [src: cf_formulation_design] The top positive residuals are *S. salivarius* ASMA-737 (+74.1%), *G. sanguinis* ASMA-3044 (+62.2%) and *N. mucosa* ASMA-3643 (+57.2%). [src: cf_formulation_design] These species later dominate the report's FDA-safe formulations. The report suggests they combine metabolic competition with direct antagonism. [src: cf_formulation_design] See [[concepts/metabolic-competition-versus-direct-antagonism-in-pathogen-inhibition]].

### Growth kinetics

Endpoint OD shows whether an organism can grow on a substrate, not how fast. [src: cf_formulation_design] The report therefore extracted maximum growth rate (μ_max), lag time, carrying capacity and area under the curve (AUC) from 676,000 fitted curve points across 32 isolates. [src: cf_formulation_design] Commensals beat PA14's maximum growth rate on only 13.8% of substrate comparisons, so PA14 is generally the fastest grower. [src: cf_formulation_design] Commensals start growing before PA14 on 43.1% of comparisons (lag advantage > 0). [src: cf_formulation_design] The report suggests that pre-establishing commensals before pathogen exposure, for example by prebiotic biomass pre-loading, could matter more than raw growth rate. [src: cf_formulation_design]

Kinetic parameters correlate moderately with endpoint OD (r ≈ 0.40) but are not redundant. [src: cf_formulation_design] For the 29 isolates with all three assay types, adding kinetic features to the metabolic overlap model improves prediction to R² = 0.311. [src: cf_formulation_design]

The report ties these analyses to notebooks 01_data_integration_eda.ipynb, 02_growth_kinetics.ipynb and 03_explaining_inhibition.ipynb. [src: cf_formulation_design]

## Results: Unified Formulation Rankings

This part of the report uses patient metagenome and metatranscriptome data to rank candidate species by engraftability. It then uses that ranking, with inhibition and niche-coverage data, to build strict-safe formulations of 1 to 5 organisms. Neisseria mucosa anchors every size, and k=3 is the first size with full niche coverage. [src: cf_formulation_design]

### Patient ecology and engraftability

The report used paired metagenomic (DNA abundance) and metatranscriptomic (RNA activity) data from 175 patient samples to find species that are both prevalent and active. [src: cf_formulation_design] It detected 134 species across the patient metagenomes. [src: cf_formulation_design] Engraftability score is prevalence × log(activity ratio), where activity ratio is metaRS CPM / metaG CPM, the transcriptional engagement per unit DNA. [src: cf_formulation_design]

Among inhibition-tested species, [[entities/neisseria-mucosa|Neisseria mucosa]] has the highest engraftability (1.595). It combines high prevalence with strong transcriptional activity. [src: cf_formulation_design] [[entities/rothia-dentocariosa|Rothia dentocariosa]] (0.422) and [[entities/streptococcus-salivarius|Streptococcus salivarius]] (0.172) are also above the median. [src: cf_formulation_design]

### Optimization design and safety filters

The scoring function evaluates formulations of 1–5 organisms on five criteria: PA14 niche coverage, internal metabolic complementarity, mean inhibition, engraftability, and FDA safety. [src: cf_formulation_design]

The report ran two safety stages. The permissive stage excluded only well-known pathogens. The strict stage also excluded all Pseudomonas, Enterobacteriaceae and Staphylococcus. [src: cf_formulation_design]

The permissive filter picks the most inhibitory organisms: Leclercia adecarboxylata (102%), Pseudomonas_E juntendi (94%) and S. epidermidis (99%). The report calls these clinically problematic. They are respectively an Enterobacteriaceae member, a non-aeruginosa Pseudomonas and a nosocomial Staphylococcus. [src: cf_formulation_design] The strict filter costs roughly 15% inhibition ceiling but doubles engraftability. [src: cf_formulation_design]

### Robustness of the optimum

An exhaustive search checked whether restricting the candidate pool hid better triples. It enumerated all C(97,3) = 147,440 triples from the strict-safe pool and scored 127,598 valid unique-species formulations. The same M. luteus + N. mucosa + S. salivarius triple was the global optimum (score 0.562). [src: cf_formulation_design]

Bootstrap resampling (1,000 times over the raw inhibition measurements) gave 95% confidence intervals (CIs) on the composite scores. [src: cf_formulation_design] The CIs by formulation size k were:
- k=1: [0.753, 0.753]. [src: cf_formulation_design]
- k=2: [0.514, 0.588]. [src: cf_formulation_design]
- k=3: [0.551, 0.562]. [src: cf_formulation_design]
- k=4: [0.534, 0.578]. [src: cf_formulation_design]
- k=5: [0.520, 0.587]. [src: cf_formulation_design]

All k=2 through k=5 CIs overlap, so those sizes are not statistically distinguishable on composite score. The report cites this in support of k=2 as the practical primary candidate. [src: cf_formulation_design] The five-species core recurs across all formulation sizes. The report reads this as a robust solution, not an optimization artifact. [src: cf_formulation_design]

### Recommended strict-safe formulations

- **k=1:** N. mucosa ASMA-3643, with composite 0.753, 18% coverage, 88% inhibition and engraftability 1.595. [src: cf_formulation_design]
- **k=2:** R. dentocariosa ASMA-2935 + N. mucosa ASMA-3643, with composite 0.588, 18% coverage, 84% mean inhibition and engraftability 0.820. [src: cf_formulation_design]
- **k=3:** M. luteus ASMA-2965 + N. mucosa ASMA-3643 + S. salivarius ASMA-737, with composite 0.562, 100% PA niche coverage, 75% mean inhibition and engraftability 0.140. [src: cf_formulation_design]
- **k=4:** the k=3 members plus R. dentocariosa ASMA-2935, with composite 0.578, 100% coverage, 76% inhibition and engraftability 0.185. [src: cf_formulation_design]
- **k=5:** the k=4 members plus G. sanguinis ASMA-3044, with composite 0.587, 100% coverage, 78% mean inhibition and engraftability 0.188. [src: cf_formulation_design]

N. mucosa is the best single organism, with the highest engraftability and strong inhibition. Its low niche coverage limits monotherapy. [src: cf_formulation_design] At k=2, the report describes both members as lung-adapted species, with 33–38% respiratory representation in the pangenome. [src: cf_formulation_design]

The report calls k=3 the minimum viable formulation, because it is the first size with full niche coverage. [src: cf_formulation_design] The jump from 18% to 100% occurs because Micrococcus luteus grows on 9 of PA14's 11 preferred substrates. These include proline, histidine, glutamate, aspartate, arginine and glucose. They cover the amino acid substrates that N. mucosa and S. salivarius do not reach individually. [src: cf_formulation_design] M. luteus has the widest carbon utilization profile among strict-safe candidates and closes every remaining PA substrate gap in one addition. [src: cf_formulation_design]

At k=4, R. dentocariosa is added for lung tropism and direct antagonism depth. [src: cf_formulation_design] The full five-species formulation gives maximum redundancy and inhibition depth. [src: cf_formulation_design]

### Core-species profiles

Each entry gives best inhibition, engraftability, pangenome size, amino acid (AA) pathway conservation and lung genomes.
- **N. mucosa:** 88%, 1.595, 15 genomes (8 in PROTECT clade), 16/18 (18/18 in PROTECT clade), 5 (33%) lung genomes. [src: cf_formulation_design]
- **S. salivarius:** 98%, 0.172, 153 genomes, 18/18, 5 (4%) lung genomes. [src: cf_formulation_design]
- **R. dentocariosa:** 79%, 0.422, 29 genomes, 14/18, 10 (38%) lung genomes. [src: cf_formulation_design]
- **G. sanguinis:** 85%, 0.202, 7 genomes, 7/18, 1 lung genome. [src: cf_formulation_design]
- **M. luteus:** 38%, 0.000, 295 genomes, 18/18, 0 lung genomes. [src: cf_formulation_design]

The report assigns each species a role:
- **N. mucosa:** the indispensable anchor at every k, with near-additive pairwise interactions. [src: cf_formulation_design]
- **S. salivarius:** it has the highest individual inhibition (98%) and a residual of +74% beyond metabolic prediction. It provides the direct antagonism backbone. [src: cf_formulation_design] The report names BLIS K12 as probiotic precedent for this species. [src: cf_formulation_design]
- **R. dentocariosa:** its residual is +57%. [src: cf_formulation_design] The report cites Stubbendieck et al. 2023 for colonization resistance via a secreted endopeptidase. [src: cf_formulation_design]
- **G. sanguinis:** its residual is +62%, and it adds depth at k=5. [src: cf_formulation_design] It has the smallest pangenome (7 genomes), so strain selection is most critical for this species. [src: cf_formulation_design]

## Results: Pairwise Interactions Are Near-Additive for Key Species

This part of the report asks whether any tested substrate, or any pathway found by genomic extension, could selectively feed commensals over [[entities/pseudomonas-aeruginosa-pa14|Pseudomonas aeruginosa PA14]]. The report finds no selective prebiotic among its tested substrates, so competitive exclusion must rest on community-level depletion. [src: cf_formulation_design] It then checks that the metabolic traits are conserved across strains, notes lung association, tests pair interactions, and finds a few untested pathways that may work as prebiotics. [src: cf_formulation_design]

### No selective prebiotic among tested substrates

The report computed selectivity as commensal mean optical density (OD) divided by PA14 OD for all 20 tested substrates. [src: cf_formulation_design] PA14 outgrew the average commensal on every tested substrate. [src: cf_formulation_design] The most selective substrates (cysteine, threonine and methionine) had ratios of only 0.77–0.96. [src: cf_formulation_design] No amino acid or simple sugar gave commensals a clear growth advantage. [src: cf_formulation_design] The report states its conclusion as "among the 22 tested substrates, no selective prebiotic exists". [src: cf_formulation_design] The report gives 20 substrates for the ratio computation [src: cf_formulation_design] and 22 for the conclusion. [src: cf_formulation_design] It does not explain the difference, and this page does not reconcile the two counts. It infers that exclusion must work through community-level resource depletion, with several organisms together consuming the resource pool faster than PA14 alone, rather than through an advantage on any one substrate. [src: cf_formulation_design] This result motivated the genomic extension analysis for untested substrates. [src: cf_formulation_design] The analysis is in notebook 06_prebiotic_pairing.ipynb. [src: cf_formulation_design]

### Conservation of metabolic traits across strains

The report asked whether PROTECT isolate carbon-use profiles generalize between strains. It used GapMind pathway conservation across 499 pangenome genomes in the 5 core commensal species. [src: cf_formulation_design] Conservation at >95% was complete or near-complete in most species, and lowest for amino acid pathways in *Gemella sanguinis*:

- *M. luteus*: 295 genomes, 18/18 (100%) amino acid pathways and 39/39 (100%) carbon pathways. [src: cf_formulation_design]
- *S. salivarius*: 153 genomes, 18/18 (100%) amino acid pathways and 32/35 (91%) carbon pathways. [src: cf_formulation_design]
- *R. dentocariosa*: 29 genomes, 14/18 (78%) amino acid pathways and 39/41 (95%) carbon pathways. [src: cf_formulation_design]
- *N. mucosa*: 15 genomes, 16/16 (100%) amino acid pathways and 27/27 (100%) carbon pathways. [src: cf_formulation_design]
- *G. sanguinis*: 7 genomes, 7/18 (39%) amino acid pathways and 37/39 (95%) carbon pathways. [src: cf_formulation_design]

The report calls hypothesis H5 (conservation) strongly supported. It concludes that the measured capabilities are species-level traits conserved across hundreds of genomes. [src: cf_formulation_design] For the other four species, any well-characterized strain should give equivalent metabolic competition. [src: cf_formulation_design] *G. sanguinis* is the exception. It showed the most pathway variability, but its pangenome is small (7 genomes), so strain selection matters most for it. [src: cf_formulation_design]

### Lung association of the formulation species

The report queried NCBI environmental metadata for all pangenome genomes of its five species. [src: cf_formulation_design] Of 21 lung/respiratory genomes, *Rothia dentocariosa* contributed 10 (38% of its species). [src: cf_formulation_design] *Neisseria mucosa* contributed 5 (33%). [src: cf_formulation_design] The report describes both as naturally respiratory organisms, not gut commensals being repurposed. [src: cf_formulation_design] It cites Rigauts et al. (2022) for *Rothia mucilaginosa* enrichment in healthy airways. [src: cf_formulation_design] It cites Stubbendieck et al. (2023) for *R. dentocariosa*-mediated colonization resistance in the nasal tract. [src: cf_formulation_design]

*M. luteus* had 0 lung genomes and is mainly skin/environmental. The report suggests it may face engraftment challenges despite its metabolic contribution. [src: cf_formulation_design] Lung-adapted *Streptococcus salivarius* genomes showed L-malate enrichment (+0.39 score). [src: cf_formulation_design] They also showed sorbitol depletion (−0.82), which the report reads as adaptation to the airway carbon landscape. [src: cf_formulation_design]

### Pairwise interactions among commensals

Formulation scoring assumes additive inhibition, meaning the combination effect equals the mean of its members. This would underestimate synergy and overestimate antagonistic combinations. [src: cf_formulation_design] The interaction analysis relies solely on the RFU-based competition assay. [src: cf_formulation_design] Results per pair (mean pair inhibition, mean single best inhibition, synergy):

- *N. mucosa* + ASMA-2260: 47%, 42%, +5.3%. [src: cf_formulation_design]
- ASMA-3913 + ASMA-2260: 52%, 51%, +1.4%. [src: cf_formulation_design]
- *N. mucosa* + ASMA-2464: 40%, 42%, −2.2%. [src: cf_formulation_design]
- ASMA-3913 + ASMA-2464: 37%, 51%, −14.2%. [src: cf_formulation_design]
- ASMA-1478 + ASMA-1197: −3%, 17%, −19.8%. [src: cf_formulation_design]

Overall mean synergy was −5.8%, which indicates mildly antagonistic interactions on average. [src: cf_formulation_design] *N. mucosa* pairs were near-additive (+5.3% and −2.2%), which supports its role as a formulation anchor that does not interfere with partners. [src: cf_formulation_design]

These conclusions rest on only 8 comparisons across 5 unique pairs, an underpowered sample. [src: cf_formulation_design] The `fact_pairwise_interaction` table proved identical to `fact_carbon_utilization` (correlation = 1.0), so per-substrate co-culture effects cannot be assessed from endpoint OD data. [src: cf_formulation_design] The report calls the complete 10-pair matrix for the 5-species core a critical gap. It treats the additive scoring assumption as provisional until that matrix is measured. [src: cf_formulation_design]

### Untested pathways as candidate prebiotics

GapMind predicts completeness for ~80 carbon and amino acid pathways, many outside the 22 tested substrates. [src: cf_formulation_design] The report compared pathway completeness between the 5 core commensals and *P. aeruginosa* across the pangenome. [src: cf_formulation_design] It found six pathways complete in at least one commensal but absent in PA14. Each is carried by only 1–2 of the 5 core species, so these are species-specific capabilities, not consortium-wide ones. [src: cf_formulation_design] For each pathway: PA completeness, commensal carriage, selectivity.

- Myoinositol: 0%; *R. dentocariosa* (100%); 1.00. [src: cf_formulation_design]
- Xylitol: 0%; *S. salivarius* (98%), *G. sanguinis* (100%); 1.00. [src: cf_formulation_design]
- Xylose: 0%; *N. mucosa* (100%), *G. sanguinis* (100%); 1.00. [src: cf_formulation_design]
- Arabinose: 0%; *N. mucosa* (100%), *G. sanguinis* (100%); 1.00. [src: cf_formulation_design]
- Fucose: 1%; *N. mucosa* (100%), *G. sanguinis* (100%); 0.99. [src: cf_formulation_design]
- Rhamnose: 1%; *N. mucosa* (100%), *G. sanguinis* (100%); 0.99. [src: cf_formulation_design]

The report proposes pairing xylitol with *S. salivarius*, the top inhibitor. It proposes pairing xylose, arabinose and fucose with *N. mucosa*, the engraftment anchor, and with *G. sanguinis*. [src: cf_formulation_design] It hypothesizes that a multi-prebiotic cocktail aimed at different formulation members may work better than a single prebiotic. [src: cf_formulation_design] This is a hypothesis, not a tested result.

## Results: Formulation Robustness: PA's Amino Acid Core Is Invariant Across Lung Variants

This part of the report argues that sugar alcohols and pentoses are good prebiotic candidates because commensals use them and PA14 cannot access them. [src: cf_formulation_design] Separately, it reports that lung *Pseudomonas aeruginosa* (PA) isolates are losing some other sugar pathways (sorbitol, mannitol, gluconate), and that PA's amino acid catabolism is stable across lung and CF isolates. [src: cf_formulation_design] The evidence comes from genome-based pathway predictions across 6,760 PA genomes, patient metatranscriptomics and a codon-usage analysis. Several of the conclusions are predictions, not tests. [src: cf_formulation_design]

### Candidate prebiotics

The report names sugar alcohols (xylitol, myoinositol) and pentoses (xylose, arabinose, fucose, rhamnose) as strong prebiotic candidates. [src: cf_formulation_design] It says these substrates are genomically complete in the formulation species, absent from PA14's metabolic repertoire and actively transported by commensals in patient airways. [src: cf_formulation_design] It also calls them commercially available and FDA-GRAS, and says xylitol is already used in CF (cystic fibrosis) airway products for other indications. [src: cf_formulation_design] The report presents this as a different strategy from amino acid supplementation. Instead of competing on PA14's substrates, it feeds commensals on substrates PA14 cannot access. [src: cf_formulation_design]

Patient metatranscriptomics is the in vivo support. In patients, 47 KEGG pathways had a commensal-to-PA expression ratio above 2×. These were dominated by PTS sugar transport systems for maltose, trehalose and N-acetylmuramic acid, which only commensals expressed. [src: cf_formulation_design]

### Lung PA is losing some sugar catabolism

The PA pangenome analysis covered 6,760 genomes. Of these, 5,199 had metadata and 1,796 came from lung/respiratory or CF sources. [src: cf_formulation_design] Seven GapMind pathways differed between lung and non-lung PA at FDR (false discovery rate) < 0.05. All were carbon source pathways that lung PA is losing. [src: cf_formulation_design] The reported differences were:

| Pathway | Lung vs non-lung difference |
|---|---|
| sorbitol | −0.165 [src: cf_formulation_design] |
| mannitol | −0.204 [src: cf_formulation_design] |
| gluconate | −0.185 [src: cf_formulation_design] |

The report interprets this as metabolic streamlining. In amino acid-rich sputum, sugar catabolism is dispensable and under relaxed selection. It takes this to show that PA's amino acid dependence is an evolutionary adaptation, not only a preference. [src: cf_formulation_design] This is an interpretation of the pathway data, not a separate measurement.

### Amino acid catabolism is conserved in lung PA

Across the 1,796 lung PA genomes, amino acid catabolic pathways were 97.4% conserved (mean completeness). [src: cf_formulation_design] Proline, PA14's top substrate, had a complete pathway in 97% of lung isolates. [src: cf_formulation_design] The main variation among lung PA (PC1, principal component 1, = 79%) was in the sorbitol, mannitol and gluconate pathways, which the formulation does not target. [src: cf_formulation_design]

Lung PA split into two metabolic clusters. The major cluster had 1,743 genomes (97%) with full metabolic capacity. [src: cf_formulation_design] The minor cluster had 53 genomes (3%) lacking TCA (tricarboxylic acid) cycle intermediates. [src: cf_formulation_design] The minor cluster was CF-enriched (25% CF vs 16%). [src: cf_formulation_design] The report suggests it may be chronically adapted PA that depends more on external metabolites and may be more vulnerable to competitive exclusion. [src: cf_formulation_design]

CF-derived PA showed 6 FDR-significant differences from non-CF lung PA, all in sugar-related pathways. It showed zero amino acid differences. [src: cf_formulation_design] The report therefore predicts that formulations designed for general lung PA should work equivalently for CF PA. [src: cf_formulation_design]

### Expression in acute exacerbation

During acute exacerbation, patient PA downregulated 170 of 207 measured pathways. [src: cf_formulation_design] Cysteine and methionine biosynthesis expression was 10× lower. [src: cf_formulation_design] OprD, which the report describes as imipenem resistance, was 13× lower. [src: cf_formulation_design] Only phosphate transport was upregulated, by 64×. [src: cf_formulation_design] The report suggests that this quiescent PA scavenges host-derived amino acids and may be more vulnerable to competitive exclusion during acute episodes. [src: cf_formulation_design] This vulnerability is a suggestion, not a measured result. The analysis is in notebook 10_pa_lung_adaptation.ipynb. [src: cf_formulation_design]

### Genome size and growth rate

PA's genome (6.58 Mb, 6,177 CDS) is 2.5–3× larger than the formulation commensals (2.1–2.7 Mb, 2,200–3,000 CDS). [src: cf_formulation_design] Even so, NB02 growth curves showed PA14 outgrowing most commensals on its preferred amino acids. The report reads this as showing that catabolic enzyme efficiency, not ribosomal translation rate, drives PA's advantage on amino acids. [src: cf_formulation_design]

Codon usage bias (CUB) analysis of ribosomal proteins (NB12) showed variation across species. [src: cf_formulation_design] Cross-species comparisons were confounded by GC content, which ranged from 31% for *G. sanguinis* to 73% for *M. luteus*. Extreme GC composition inflates CUB scores regardless of growth optimization. [src: cf_formulation_design] The report concludes that CUB cannot reliably distinguish growth rates among its species. It treats laboratory growth data as the definitive measure of competition on amino acids. [src: cf_formulation_design]

### Variation among PA strains

Among 15 PROTECT PA strain groups, genome size ranged from 6.12 Mb (5,668 CDS) to 7.35 Mb (7,026 CDS), a 24% difference in gene content. [src: cf_formulation_design] The largest group (725, 98 isolates) carried 1,358 extra genes compared with the smallest. [src: cf_formulation_design] All groups kept the same amino acid catabolic pathways, with 97%+ conservation in NB11. [src: cf_formulation_design]

The report hypothesizes that the extra genes are conditionally expressed accessory functions. These include prophages, mobile elements and niche-specific adaptations that affect virulence and persistence, not amino acid growth rate. [src: cf_formulation_design] It notes that within-species genome size variation predicts growth rate much more weakly than cross-species variation. [src: cf_formulation_design] From this it predicts that PA strains will respond similarly to the formulation, because amino acid catabolism, the competitive target, is invariant across the species. [src: cf_formulation_design] It expects strains to differ in virulence, antibiotic resistance and biofilm properties. These affect disease severity but not the metabolic competition mechanism. [src: cf_formulation_design]

## Results: PA Virulence System Distribution: PA14 Is Not Representative of CF

### Reference strains differ qualitatively

PA14 and PAO1 differ in type III secretion system (T3SS) effectors (ExoU versus ExoS), in biofilm polysaccharides (Pel-only versus Pel+Psl), and in regulatory state (a ladS mutation). [src: cf_formulation_design] The public-genome analysis covers 6,760 P. aeruginosa genomes, with environmental metadata for 4,769. [src: cf_formulation_design] See also [[concepts/pseudomonas-aeruginosa-strain-diversity-and-representativeness-of-reference-strains]].

### T3SS effectors across isolation contexts

ExoS+ genomes dominate in CF, and ExoU+ genomes become more common in other contexts. The table gives the percentage of genomes carrying each effector. [src: cf_formulation_design]

| Source | ExoS+ | ExoU+ | Both | Genomes |
|---|---|---|---|---|
| CF patient | 94% | 5% | 0% | 291 [src: cf_formulation_design] |
| Lung/respiratory | 82% | 16% | 1% | 1,505 [src: cf_formulation_design] |
| Other clinical | 63% | 33% | 3% | 1,731 [src: cf_formulation_design] |
| Environmental | 62% | 35% | 1% | 370 [src: cf_formulation_design] |

The report reads this as consistent with ExoU being an acute cytotoxic effector rather than a chronic colonization factor. [src: cf_formulation_design] It also suggests that ExoS dominance in CF may help. ExoS mediates slower, apoptotic killing than ExoU's rapid cytotoxic lysis, which may give competitive exclusion a wider time window. This is a suggestion, not a measurement. [src: cf_formulation_design]

### Biofilm and regulatory genes

The PAO1-like Pel+Psl biofilm architecture is the common one: 96.4% of genomes carry both Pel and Psl operons. [src: cf_formulation_design] Only 3.5% are Pel-only (PA14-like), with slight enrichment in CF (8%) compared with environmental genomes (3%). [src: cf_formulation_design] The report states that PA14's psl deletion is a rare variant, not representative of the species. [src: cf_formulation_design] Bakta annotation detects ladS in only 0.5% of genomes. [src: cf_formulation_design] The report calls PA14's ladS frameshift an extreme outlier that locks the strain into an acute-virulence regulatory state, unrepresentative of natural infection dynamics. [src: cf_formulation_design]

### Implications for the formulation

Amino acid catabolic pathways were identical between ExoU+ and ExoS+ P. aeruginosa. GapMind score differences were <0.03 on a 1–5 scale, and no pathway was significant after false discovery rate (FDR) correction. [src: cf_formulation_design] The report therefore predicts that one formulation should work against all variants regardless of T3SS effector type, because its competitive-exclusion targets are independent of virulence genotype. [src: cf_formulation_design] This is a prediction, not a tested result. Its PA14-based inhibition assays tested a minority (<5%) CF variant. [src: cf_formulation_design] Proposed Experiment 4.6, which extends testing to PAO1 and clinical strains, is therefore elevated in importance. Confirming inhibition against ExoS+ strains is essential. [src: cf_formulation_design] See [[entities/pseudomonas-aeruginosa-pa14]] and [[concepts/generalizability-limits-of-planktonic-single-strain-inhibition-assays]].

### PROTECT isolate profiling

The report profiled all 643 annotated PROTECT genomes for 32 virulence genes. The genes span T3SS effectors, biofilm operons, alginate biosynthesis, quorum sensing, iron acquisition and type VI secretion system (T6SS). [src: cf_formulation_design] Each isolate was classed as PAO1-like, PA14-like or intermediate, using ExoU/ExoS status, biofilm architecture and ladS presence. [src: cf_formulation_design] Of the 643, 304 (47%) are PAO1-like (ExoS+). [src: cf_formulation_design] 48 (7%) are PA14-like (ExoU+). [src: cf_formulation_design] The other 291 (45%) are intermediate because GenomeDepot lacks a clear T3SS annotation for them. [src: cf_formulation_design] A related count for the 651-genome PROTECT collection gives 47% exoS and 7% exoU, with 45% unannotated. [src: cf_formulation_design] That gap comes from GenomeDepot gene-name coverage. [src: cf_formulation_design] Among classifiable isolates, 86% are PAO1-like. The report takes this as confirming at isolate level that PA14 is not representative of the PROTECT CF collection. [src: cf_formulation_design] Strain groups are uniformly PAO1-like or uniformly PA14-like. The report interprets this as T3SS effector type being clonal within lineages, not horizontally transferred. [src: cf_formulation_design] See [[entities/protect-genome-depot]].

### Pfam-based phylogeny

Gene names are unreliable for comparing PROTECT and pangenome genomes, because GenomeDepot and bakta/eggNOG use different annotation pipelines. [src: cf_formulation_design] The report therefore built a tree from Pfam protein domain profiles, a pipeline-independent vocabulary. [src: cf_formulation_design] The two databases share 2,850 standardized Pfam domains, with ~3,200 unique domains per genome. [src: cf_formulation_design] The tree spans 165 genomes: 13 PROTECT strain group representatives, 150 sampled lung/airway pangenome genomes, and the PAO1 and PA14 references. [src: cf_formulation_design] It uses Jaccard distances on 1,557 variable Pfam domains present in 5–95% of genomes. These resolve the accessory-genome variation that distinguishes PAO1-like from PA14-like strains. [src: cf_formulation_design]

PROTECT isolates are spread across lung P. aeruginosa diversity, not clustered in one lineage. The report reads this as the collection sampling the breadth of CF genomic variation. [src: cf_formulation_design] ExoU+ isolates cluster separately from the ExoS+ majority. This is consistent with PAPI-1/PAPI-2 pathogenicity island acquisition as a deep phylogenetic event. [src: cf_formulation_design] The Newick file data/pa_pfam_tree.nwk allows re-visualization with other annotation schemes as new metadata appears. [src: cf_formulation_design]

## Discussion: The M. luteus Engraftment Question

This part of the report argues that effective commensal formulations suppress *Pseudomonas aeruginosa* through at least three mechanisms at once. It then works through the design tension this creates for the k=3 formulation, the resulting recommendation, and the literature that supports the framework. [src: cf_formulation_design]

### Three mechanisms and what they explain

The report attributes about 27% of PA14 inhibition variance to metabolic competition, meaning depletion of PA14's preferred amino acid substrates. It says the metabolic overlap–inhibition correlation validates this quantitatively. [src: cf_formulation_design] Taxonomy adds a further 9% through direct antagonism, likely bacteriocins, secreted enzymes or contact-dependent killing that act independently of resource competition. [src: cf_formulation_design] Streptococcus salivarius, Neisseria mucosa and Gemella sanguinis show strong positive residuals in the metabolic model. [src: cf_formulation_design] The report suggests the remaining 64% of variance reflects unmeasured factors: biofilm dynamics, pH effects, iron competition, quorum sensing interference and stochastic variation in the planktonic assay. [src: cf_formulation_design] This is the report's own interpretation, not a measured decomposition of those factors.

### Why a consortium is needed

PA14 outgrows most commensals on its preferred amino acids. Only 13.8% of pairwise comparisons show a commensal rate advantage, and the report attributes this to PA's specialized amino acid catabolic enzymes. [src: cf_formulation_design] No individual commensal outgrows PA14 on any tested substrate. A 3–5 organism consortium collectively covers 100% of PA14's metabolic niche, which the report calls an emergent community property that individual profiles cannot predict. [src: cf_formulation_design] The report treats the lab growth data as ground truth. Cross-species codon usage bias comparison (NB12) is confounded by GC content variation (31–73%) and cannot reliably distinguish growth rate potential. [src: cf_formulation_design]

The report gives three reasons the consortium can still win:
- Commensals start growing before PA14 in 43.1% of comparisons. The report suggests delivering commensals before pathogen exposure, or boosting them first with prebiotics, could exploit this window. [src: cf_formulation_design]
- Community biomass matters more than individual growth rate. A 3-organism consortium with each member growing at half PA14's rate depletes resources 1.5× faster collectively. [src: cf_formulation_design]
- The k=3 formulation's 100% niche coverage neutralizes PA's fast growth on any single substrate, because all substrates are contested at once. [src: cf_formulation_design]

### Strain invariance of the target

All 15 PROTECT *P. aeruginosa* strain groups retain the same core amino acid catabolism pathways, with 97%+ conservation. [src: cf_formulation_design] Genome sizes range from 6.1–7.4 Mb, with 24% gene content variation. The report suggests the extra genes are likely accessory functions, such as prophages and resistance islands, that affect virulence and persistence but not amino acid growth rate. [src: cf_formulation_design] It therefore predicts the formulation should be equally effective across PA variants, because the metabolic competition targets are invariant. This is a prediction, not a tested result. [src: cf_formulation_design] Strain variation is expected to matter more for virulence, biofilm formation and antibiotic resistance, which are orthogonal to competitive exclusion. [src: cf_formulation_design]

### The Micrococcus luteus design tension

*Micrococcus luteus* is the keystone species for niche coverage: adding it at k=3 is what achieves 100% PA substrate coverage. [src: cf_formulation_design] It has zero engraftability, because it was not detected in any patient metagenome. It also has zero lung genomes in the pangenome, which is primarily skin/environmental. [src: cf_formulation_design] The report calls this a fundamental design tension: the species most important for metabolic coverage is the least likely to persist in the lung. [src: cf_formulation_design]

The report weighs three paths:
- Accept the risk and test k=3 in mice. *M. luteus*'s broad carbon utilization may compensate for low natural prevalence if delivered at sufficient dose. [src: cf_formulation_design]
- Prioritize the k=2 formulation (*Rothia dentocariosa* + *N. mucosa*). It has combined 84% inhibition and 0.820 engraftability, and it sacrifices niche coverage for colonization reliability. [src: cf_formulation_design]
- Search lung-adapted species for an alternative broad-spectrum metabolizer to replace *M. luteus*'s niche coverage role. [src: cf_formulation_design]

### Recommendation

The report recommends the k=2 formulation as the primary clinical candidate. [src: cf_formulation_design] Both species are naturally lung-adapted, with 33–38% respiratory genomes in the pangenome. Both are dual-mechanism inhibitors, combining metabolic inhibition and direct antagonism. Their combined engraftability of 0.820 is nearly 6× higher than the k=3 formulation's 0.140. [src: cf_formulation_design]

The k=2 formulation achieves only 18% PA niche coverage. Its 84% mean per-organism inhibition suggests the hypothesis that direct antagonism may matter more than niche coverage for clinical efficacy. The report says the mouse model (Proposed Experiment 4.5) can test this. [src: cf_formulation_design]

The k=3 formulation (*M. luteus* + *N. mucosa* + *S. salivarius*) is an aspirational second-line candidate. It is contingent on demonstrating *M. luteus* lung engraftment in vivo. [src: cf_formulation_design] In parallel, the report proposes screening oral/respiratory Actinobacteria with broad carbon utilization, such as *Kocuria*, *Dermacoccus* or other Micrococcaceae with respiratory isolation records, against the PA14 carbon utilization panel. [src: cf_formulation_design]

### Prebiotics

The report found a complete absence of selective amino acid prebiotics, because PA14 is too metabolically versatile on amino acids. [src: cf_formulation_design] The genomic extension instead identifies sugar alcohols and pentoses that commensals can metabolize but PA14 cannot. [src: cf_formulation_design] The report describes xylitol as already FDA-approved for CF airway use, with mucolytic/antimicrobial properties. It sees this as a dual-purpose prebiotic opportunity. [src: cf_formulation_design]

### Link to the literature

The report cites several studies as context for the framework:
- Palmer et al. (2005, 2007) established that amino acids are PA's primary carbon sources in CF sputum. The report's PA14 utilization ranking (proline > histidine > ornithine > glutamate) mirrors the SCFM composition, which it takes as validating its assay system. [src: cf_formulation_design]
- Rigauts et al. (2022) showed *Rothia mucilaginosa* suppresses NF-κB inflammation in CF airways. Stubbendieck et al. (2023) identified a *R. dentocariosa* peptidoglycan endopeptidase that inhibits *Moraxella catarrhalis*. [src: cf_formulation_design] The report proposes that its *R. dentocariosa* isolates likely use similar mechanisms, which would explain their high inhibition residuals. [src: cf_formulation_design]
- Widder et al. (2022) identified eight pulmotypes driven by ecological competition. The report's community-level niche coverage model operationalizes this concept for therapeutic design. [src: cf_formulation_design]
- Rogers et al. (2015) demonstrated competitive exclusion between PA and *H. influenzae* in bronchiectasis, supporting the ecological framework. [src: cf_formulation_design]
- Anderson et al. (2017) reviewed CF probiotic trials and found suggestive but inconclusive results, attributing this partly to lack of rational strain selection. The report states its multi-criterion optimization directly addresses this gap. [src: cf_formulation_design]
- *S. salivarius* BLIS K12 has established respiratory probiotic credentials (Tagg et al. 2025; Burton et al. 2011). [src: cf_formulation_design]

## Discussion: Literature Context

This part of the report places its results against the literature. It reports agreement with clinical xylitol studies and with ExoS-dominance surveys of CF (cystic fibrosis) *Pseudomonas aeruginosa*. It also reports one contrast with published probiotic work and states several limits on its own assays. [src: cf_formulation_design]

### Pangenome conservation and probiotic safety

Shao et al. (2026) used pangenome analysis for *Bifidobacterium* probiotic design and found strong strain-level functional divergence that requires careful strain selection. [src: cf_formulation_design] The report finds >95% metabolic conservation, which it calls the opposite scenario and equally valuable for translational confidence. [src: cf_formulation_design] It presents this as pangenome validation of metabolic robustness across hundreds of genomes, supporting species-level formulation design. [src: cf_formulation_design]

Drost and Fuhrmann (2025) showed that *Lactiplantibacillus plantarum*, a commonly proposed probiotic, enhanced PA (*P. aeruginosa*) pathogenicity in a CF sputum–epithelial cell model. [src: cf_formulation_design] The report says this underscores its strict FDA safety filtering and species-specific validation, in place of generic "probiotic" organisms. [src: cf_formulation_design]

### Xylitol as a selective prebiotic

The report identifies xylitol as a selective prebiotic and cites clinical support. [src: cf_formulation_design] Durairaj et al. (2007) demonstrated the safety of inhaled xylitol in CF patients. [src: cf_formulation_design] Singh et al. (2020) ran a randomized controlled trial of aerosolized hypertonic xylitol versus saline during CF exacerbations. [src: cf_formulation_design] The report says these studies establish the delivery route and safety profile its prebiotic strategy would use. [src: cf_formulation_design] It describes the discovery of sugar alcohol prebiotics through genomic pathway comparison as qualitatively different from amino acid supplementation. [src: cf_formulation_design] See [[entities/xylitol]] and [[concepts/selective-prebiotics-for-commensal-consortia]].

### Colonization context for *Neisseria mucosa*

Weyand (2017) reviewed *Neisseria* colonization models in the upper respiratory tract and noted the prevalence of *N. mucosa* in oral tissue. [src: cf_formulation_design] Clark (2020) reviewed how upper respiratory commensals regulate infection susceptibility. [src: cf_formulation_design] The report uses these as ecological context for its *N. mucosa* engraftment assumptions, which remain assumptions. [src: cf_formulation_design] See [[entities/neisseria-mucosa]].

### Strain representativeness: PAO1-like versus PA14

Grace et al. (2022) reviewed PAO1 versus PA14 genomic and phenotypic differences, including the ExoU/ExoS type III secretion system (T3SS) distinction, psl deletion and ladS frameshift. [src: cf_formulation_design] The report's pangenome-scale analysis finds CF PA is 94% ExoS+ (PAO1-like) [src: cf_formulation_design] and 92% Pel+Psl+. [src: cf_formulation_design] It concludes that PA14 is a poor model for chronic CF infection. [src: cf_formulation_design] T3SS typing of 6,760 PA genomes gives the same 94% ExoS+ figure for CF isolates, while PA14 is ExoU+. [src: cf_formulation_design]

Earlier clinical work agrees. Hu et al. (2013) found a "predominantly exoS+/exoU–" genotype in longitudinal CF isolates from young children. [src: cf_formulation_design] Sarges et al. (2020) reported similar ExoS dominance, with the atypical exoS+/exoU+ virulotype as a rare variant. [src: cf_formulation_design] The report says its 94% ExoS+ finding is consistent with these studies and extends them to 291 genomes. [src: cf_formulation_design] Song et al. (2023) described emerging hypervirulent exoS+/exoU+ co-expressing strains. The report detected them in 1.5% of PA genomes, concentrated in non-CF clinical settings. [src: cf_formulation_design] See [[concepts/pseudomonas-aeruginosa-strain-diversity-and-representativeness-of-reference-strains]] and [[entities/pseudomonas-aeruginosa-pa14]].

### Claimed contributions

The report lists these as its contributions:

- First quantification of metabolic competition's predictive power for PA14 inhibition (R² = 0.274), establishing resource competition as a real but partial mechanism. [src: cf_formulation_design]
- Dual-mechanism species that combine metabolic competition with direct antagonism, a design principle it says was not previously articulated for respiratory pathogens. [src: cf_formulation_design]
- Community-level competitive exclusion, where no individual organism dominates but combinations achieve complete niche coverage. [src: cf_formulation_design]
- A multi-criterion framework that integrates inhibition, metabolism, kinetics, engraftability, safety and interaction data into one formulation score. [src: cf_formulation_design]
- Lung PA genomes lose sugar utilization pathways (sorbitol, mannitol, gluconate) while amino acid catabolism remains invariant. The report reads this as confirming that competition targets are evolutionarily stable. [src: cf_formulation_design]
- Amino acid pathways are 97.4% conserved across 1,796 lung PA genomes. [src: cf_formulation_design] CF and non-CF PA show zero amino acid pathway differences. [src: cf_formulation_design] The report proposes that one formulation should work across PA variants. [src: cf_formulation_design]
- All 127,598 valid k=3 triples from 97 candidates confirm the globally optimal formulation. [src: cf_formulation_design] Bootstrap confidence intervals (CIs) show k=2 through k=5 are statistically indistinguishable, which supports a minimalist k=2 approach. [src: cf_formulation_design]

See [[concepts/multi-criterion-design-of-protective-microbiome-formulations]], [[concepts/pathogen-metabolic-adaptation-in-the-lung-and-stability-of-competition-targets]] and [[concepts/metabolic-competition-versus-direct-antagonism-in-pathogen-inhibition]].

### Limits stated by the report

**Reference strain.** All inhibition assays used PA14, which is ExoU+ and Pel-only and represents <5% of CF PA isolates. [src: cf_formulation_design] The pangenome analysis confirms identical amino acid catabolism across ExoU+ and ExoS+ strains, and the report reads this as showing the mechanism is independent of virulence genotype. [src: cf_formulation_design] The inhibition measurements themselves have not been validated against ExoS+/PAO1-type strains. [src: cf_formulation_design]

**Planktonic assays.** The assays measure planktonic competition. PA14 in CF lungs grows mainly in biofilms, where metabolic dynamics, diffusion gradients and spatial structure differ substantially. [src: cf_formulation_design] See [[concepts/generalizability-limits-of-planktonic-single-strain-inhibition-assays]].

**Carbon sources.** The report tested 22 carbon sources. These cover major amino acids and glucose/lactate. They omit mucins, lipids, iron, polyamines and the sugar alcohols its genomic analysis predicts as important. [src: cf_formulation_design]

**Cohort size and composition.** The 142-isolate core cohort, where inhibition and carbon utilization data overlap, limits multivariate model power. Growth kinetics exist for only 32 isolates. [src: cf_formulation_design] The core cohort covers 62 of 211 species (29%). [src: cf_formulation_design] It is enriched for species with multiple assay types and may over-represent organisms prioritized for deeper characterization. [src: cf_formulation_design] Rothia is 22% of the core cohort versus 6% of the full collection. [src: cf_formulation_design] Streptococcus is 15% versus 8%. [src: cf_formulation_design] Neisseria is 8% versus 3%. [src: cf_formulation_design] Gemella is 7% versus 3%. [src: cf_formulation_design] The report attributes the enrichment to deliberate selection of inhibition-tested species. [src: cf_formulation_design] It expects the metabolic overlap–inhibition relationship to generalize, but absolute R² may differ for under-represented taxa. [src: cf_formulation_design]

**Pairwise interactions.** Only 3 A × 3 B isolate combinations were tested. This limits prediction of interactions for the full formulation. [src: cf_formulation_design] See [[concepts/pairwise-interaction-among-commensals-in-competition-assays]].

## Discussion; Proposed Experiments

This part of the report lists the limits of the analysis and then proposes validation experiments. The limits include inferred engraftability, sparse lung metadata and an uninformative interaction table. The proposals run from pairwise interactions and prebiotic growth tests to biofilm, mouse and strain-diversity work. [src: cf_formulation_design]

### Limits on the analysis

Patient prevalence stands in for engraftability. It does not measure colonization persistence after probiotic administration. [src: cf_formulation_design] The lung adaptation comparison rests on only 21 lung genomes across 5 species. [src: cf_formulation_design]

NB08 found that fact_pairwise_interaction and fact_carbon_utilization hold identical values (correlation = 1.0, mean difference = 0.0). [src: cf_formulation_design] The endpoint optical density (OD) data therefore do not capture co-culture metabolic interactions, and per-substrate interaction analysis is not possible with current data. The RFU-based competition assay does capture pairwise effects. [src: cf_formulation_design]

### Neisseria mucosa clade sensitivity

The pangenome contains two *N. mucosa* clades. NB07 uses s__Neisseria_mucosa_A (15 genomes). The PROTECT reference genome GCA_003028315.1 maps to s__Neisseria_mucosa (8 genomes). [src: cf_formulation_design] The 8-genome clade shows stronger conservation: 18/18 amino acid pathways at >95%, against 16/18 for the 15-genome clade. [src: cf_formulation_design] It also has 37/62 carbon pathways, against 27/62. [src: cf_formulation_design] That clade has 1 respiratory genome. [src: cf_formulation_design] The report concludes that the primary analysis, if anything, understates conservation for the formulation anchor species. [src: cf_formulation_design]

### Proposed experiments

**Pairwise interaction matrix (highest priority).** The report proposes measuring all 10 pairwise combinations of the 5 core species in the PA14 competition assay at multiple inoculation densities. [src: cf_formulation_design] NB08 found some strongly antagonistic pairs, with synergy as low as −19.8%. Current data cover only 5 of the 10 possible pairs. [src: cf_formulation_design] One antagonistic interaction between untested core members could invalidate the formulation design. The additive scoring behind the NB05 and NB05b rankings stays provisional until the full matrix exists. [src: cf_formulation_design] The matrix should validate or correct the additive scores and identify combinations to avoid. It should also guide which 3- and 4-member subsets go to mouse models. [src: cf_formulation_design] See [[concepts/pairwise-interaction-among-commensals-in-competition-assays]].

**Sugar alcohol and sugar prebiotics.** The report proposes testing the 5 core species and PA14 on xylitol, myoinositol, xylose, arabinose, fucose and rhamnose as sole carbon sources. It would use endpoint OD and growth curves. [src: cf_formulation_design] The genomic prediction of 100% commensal pathway completeness versus 0% for PA is strong but needs experimental validation. [src: cf_formulation_design] The expected result is that commensals grow and PA14 does not. Selectivity ratios should be >10, against <1 for all tested amino acids. [src: cf_formulation_design] See [[concepts/selective-prebiotics-for-commensal-consortia]].

**Biofilm challenge.** The report proposes establishing PA14 biofilms on CF bronchial epithelial cell cultures (CFBE). Formulation organisms would then challenge them, and PA14 CFU and biofilm biomass would be measured over 48 hours. [src: cf_formulation_design] The reason is that planktonic inhibition may not translate to biofilm disruption in the structured CF lung. [src: cf_formulation_design] See [[concepts/generalizability-limits-of-planktonic-single-strain-inhibition-assays]].

**Mechanism of direct antagonism.** The report proposes comparative genomics of the top direct antagonists against low-inhibition isolates of the same species. The antagonists are ASMA-737 *S. salivarius*, ASMA-3044 *G. sanguinis* and ASMA-3643 *N. mucosa*. The search targets bacteriocin gene clusters, type VI secretion system (T6SS) loci and secreted enzymes. [src: cf_formulation_design] The rationale is that dual-mechanism species show 57–74% more inhibition than their metabolic overlap predicts. [src: cf_formulation_design] See [[concepts/metabolic-competition-versus-direct-antagonism-in-pathogen-inhibition]].

**Mouse models.** The report proposes testing k=2 (*R. dentocariosa* + *N. mucosa*), k=3 (*M. luteus* + *N. mucosa* + *S. salivarius*) and k=5 formulations in a chronic PA14 lung infection model. Each would run with and without xylitol + xylose supplementation. [src: cf_formulation_design] The k=2 versus k=3 comparison addresses the *M. luteus* engraftment question. It asks whether 100% niche coverage (k=3) outperforms a lung-adapted pair (k=2) with only 18% coverage but high engraftability. [src: cf_formulation_design] The k=5 arm tests whether additional species give in vivo benefit. [src: cf_formulation_design] The prebiotic arm tests xylitol for *S. salivarius* and xylose for *N. mucosa*. [src: cf_formulation_design] See [[concepts/engraftability-and-lung-adaptation-of-candidate-commensals]].

**Clinical and strain diversity.** The report proposes repeating the inhibition and carbon utilization assays against PAO1 and 3–5 mucoid clinical PA isolates from the PROTECT collection. [src: cf_formulation_design] PA14 is a reference strain, and clinical CF isolates may respond differently, especially mucoid variants adapted to chronic infection. [src: cf_formulation_design] It also proposes characterizing the 15 PROTECT PA strain groups for virulence factors (type III secretion system (T3SS) effectors, exotoxins), biofilm formation and antibiotic resistance. These traits would be correlated with the 1,358-gene accessory genome that distinguishes the largest from the smallest strain groups. [src: cf_formulation_design]

The report states that amino acid catabolism is invariant across PA strains (97%+ conservation). [src: cf_formulation_design] It predicts that the competitive exclusion mechanism should be equally effective regardless of PA strain. [src: cf_formulation_design] It cautions that clinical outcomes also depend on virulence and biofilm properties that vary between strains. [src: cf_formulation_design] Accessory-gene differences could show whether some patients need formulation plus antibiotics. They could also show whether biofilm-adapted strains resist exclusion through spatial refuge rather than metabolic advantage, and which strain groups to prioritize for mouse testing. [src: cf_formulation_design] The expected outcome is annotation linking strain-group differences to virulence, biofilm and resistance rather than metabolic competition. That would confirm that one formulation design serves all PA variants. [src: cf_formulation_design] See [[concepts/pseudomonas-aeruginosa-strain-diversity-and-representativeness-of-reference-strains]].

**Expanded substrate and stress panel.** The report proposes testing the 5 core species on N-acetylglucosamine, putrescine/spermidine, iron-limited conditions and pH 6.5 (CF sputum pH). [src: cf_formulation_design] N-acetylglucosamine is a mucin component, and putrescine and spermidine are polyamines. [src: cf_formulation_design] The CF lung contains nutrients beyond amino acids. Iron limitation and acidic pH may reveal additional competitive advantages or vulnerabilities. [src: cf_formulation_design]

## Data; Supporting Evidence

This part of the report names the three data collections it draws on and the derived tables built from them. [src: cf_formulation_design]

### Source data

The report draws on three data collections.

- **PROTECT Gold** (`~/protect/gold/`) has 23 tables (30.5M rows). It holds the isolate catalog, inhibition assays, carbon utilization, growth kinetics, patient metagenomics and pairwise interactions. [src: cf_formulation_design]
- **[[entities/kbase-ke-pangenome]]** supplies the `genome`, `gapmind_pathways` and `ncbi_env` tables. These give [[entities/gapmind]] metabolic predictions and environmental metadata for 499+ genomes in 6 species clades. [src: cf_formulation_design]
- **protect_genomedepot** supplies the `browser_genome` and `browser_gene_sampled` tables. These hold PROTECT isolate genome annotations, including reference genome linkage. [src: cf_formulation_design]

### Derived tables: isolates, kinetics and formulations

| File | Rows | Content |
|---|---|---|
| `isolate_master.tsv` | 429 | Master analysis table: taxonomy, carbon utilization, inhibition and metabolic overlap [src: cf_formulation_design] |
| `growth_parameters.tsv` | 1,352 | Growth kinetic parameters per isolate × condition × assay [src: cf_formulation_design] |
| `kinetic_advantage.tsv` | 654 | Per-substrate kinetic advantage scores vs PA14 [src: cf_formulation_design] |
| `single_isolate_scores.tsv` | 429 | Composite scores: metabolic, inhibition, safety, overall [src: cf_formulation_design] |
| `species_engraftability.tsv` | 134 | Per-species prevalence, activity, engraftability [src: cf_formulation_design] |
| `formulations_ranked.tsv` | 22,389 | Permissive-filter formulation scores (k=1–5) [src: cf_formulation_design] |
| `formulations_strict_safety.tsv` | 146,379 | Strict-safety formulation scores, including exhaustive k=3 enumeration [src: cf_formulation_design] |
| `carbon_selectivity.tsv` | 20 | Per-substrate selectivity ratio [src: cf_formulation_design] |
| `pairwise_synergy.tsv` | 8 | Pairwise interaction synergy scores [src: cf_formulation_design] |

### Derived tables: pangenome conservation and pathways

- `pangenome_conservation.tsv` has 400 rows of GapMind pathway conservation per species × pathway. [src: cf_formulation_design]
- `isolation_sources.tsv` has 443 rows of environmental source classification. [src: cf_formulation_design]
- `gapmind_pathway_comparison.tsv` has 80 rows of GapMind pathway completeness across 6 species. [src: cf_formulation_design]
- `kegg_expression_comparison.tsv` has 252 rows of KEGG pathway expression, commensals vs *Pseudomonas aeruginosa* (PA) in vivo. [src: cf_formulation_design]

### Derived tables: *P. aeruginosa* lung adaptation and virulence

- `pa_genome_sources.tsv` has 5,199 rows of PA genome isolation source classifications. [src: cf_formulation_design]
- `pa_lung_vs_nonlung_pathways.tsv` has 80 rows of PA lung vs non-lung pathway false discovery rate (FDR) tests. [src: cf_formulation_design]
- `pa_sick_vs_stable_pathways.tsv` has 207 rows of PA pathway expression in acute vs stable patients. [src: cf_formulation_design]
- `pa_target_robustness.tsv` has 22 rows of PA amino acid and carbon pathway conservation in lung isolates. [src: cf_formulation_design]
- `pa_virulence_systems.tsv` has 6,760 rows of PA virulence gene presence, type III secretion system (T3SS) type, biofilm type and environment. [src: cf_formulation_design]
- `asma_pa_virulence_profiles.tsv` has 643 rows of per-ASMA-isolate virulence gene profiles with model classification. [src: cf_formulation_design]
- `pa_tree_annotations.tsv` has 153 rows of annotation metadata for phylogenetic tree genomes. [src: cf_formulation_design]
- `pa_pfam_tree.nwk` is a Newick tree file of 165 genomes and 1,557 variable Pfam domains. [src: cf_formulation_design]

### Analysis steps

- Data integration covers loading, merging and exploratory analysis of the isolate catalog, patients, inhibition and carbon utilization. [src: cf_formulation_design]
- Growth kinetics covers parameter extraction and kinetic advantage computation. [src: cf_formulation_design]
- The inhibition analysis uses multivariate regression of metabolic overlap on inhibition, plus residual analysis. [src: cf_formulation_design]
- Patient ecology covers species prevalence, transcriptional activity and engraftability scoring. [src: cf_formulation_design]
- The permissive-filter optimization is multi-criterion and scores 22,389 formulations. [src: cf_formulation_design] The strict version applies an FDA safety filter with a staged comparison. [src: cf_formulation_design]
- Prebiotic pairing covers carbon source selectivity. [src: cf_formulation_design]
- Pangenome conservation covers GapMind pathway conservation, environmental source analysis and lung adaptation. [src: cf_formulation_design]
- Interaction modeling covers pairwise synergy and antagonism classification and dose-response patterns. [src: cf_formulation_design]
- The genomic carbon extension identifies prebiotic candidates from genomic and transcriptomic data. [src: cf_formulation_design]
- The PA lung adaptation analysis covers formulation robustness, disease severity and PROTECT PA diversity. [src: cf_formulation_design]
- The growth-rate analysis applies codon usage bias to growth rate prediction. [src: cf_formulation_design]
- The virulence analysis covers the distribution of T3SS, pel/psl and ladS by environment. [src: cf_formulation_design]
- Isolate profiling covers per-ASMA isolate virulence profiling and a Pfam-based phylogenetic tree. [src: cf_formulation_design]

## Caveats and Open Work

- Metabolic overlap explains only 27% of inhibition variance, and the strongest inhibitors combine competition with direct antagonism, so metabolic competition alone does not account for them. [src: cf_formulation_design]
- No individual commensal outgrows PA14 on any tested substrate, so the report requires community-level niche coverage. [src: cf_formulation_design]
- Modest antagonism in some pairs means combinations are not uniformly additive. The report uses pairwise results to inform which combinations to advance to mouse models. [src: cf_formulation_design]

## Slots Into

- [[concepts/metabolic-competition-versus-direct-antagonism-in-pathogen-inhibition]]: overlap predicts inhibition (r = 0.384) but explains 27% of variance, and the strongest inhibitors also use direct antagonism. [src: cf_formulation_design]
- [[concepts/community-level-niche-coverage-and-resource-depletion-for-competitive-exclusion]]: no individual commensal outgrows PA14 on any tested substrate. [src: cf_formulation_design]
- [[concepts/multi-criterion-design-of-protective-microbiome-formulations]]: the five-organism formulation reaches 100% amino acid niche coverage with 78% mean inhibition. [src: cf_formulation_design]
- [[concepts/species-level-conservation-of-metabolic-pathways-across-pangenomes]]: capabilities are >95% conserved across hundreds of genomes. [src: cf_formulation_design]
- [[concepts/engraftability-and-lung-adaptation-of-candidate-commensals]]: 33–38% of pangenome genomes of the anchor species come from respiratory sources. [src: cf_formulation_design]
- [[concepts/selective-prebiotics-for-commensal-consortia]]: xylitol, myoinositol, arabinose and xylose are candidate prebiotics. [src: cf_formulation_design]
- [[concepts/pairwise-interaction-among-commensals-in-competition-assays]]: near-additive inhibition for *N. mucosa* combinations, with modest antagonism in some pairs. [src: cf_formulation_design]
