---
type: "Summary"
description: "Summary of the project SNIPE Defense System in the KBase Data Lakehouse Pangenome."
doc_type: "short"
full_text: "sources/snipe_defense_system__REPORT.md"
---
# SNIPE Defense System in the KBase Data Lakehouse Pangenome

This report asks whether SNIPE, a phage-defense system, is widespread in the KBase Data Lakehouse pangenome. It also asks how SNIPE relates to the mannose transporter ManXYZ, through whose ManYZ pore SNIPE cleaves phage DNA during entry. [src: snipe_defense_system] It finds SNIPE homologues in 1,696 species across 33 phyla, and the report treats this as strong support for its first hypothesis (H1). [src: snipe_defense_system] The report concludes that H1 is supported on all four axes (evolutionary rationale, prevalence, accessory status and environmental niche) and rejects random distribution for taxonomy and environmental niche. [src: snipe_defense_system] The report states that all notebooks were executed 2026-03-01 and the analysis is complete. [src: snipe_defense_system] It is based on Saxton DS et al., Nature, 2026, PMID 41741653, DOI 10.1038/s41586-026-10207-1. [src: snipe_defense_system]

## Key Findings

### Hypotheses

The null hypothesis (H0) is that SNIPE domain genes are rare or absent in the KBase Data Lakehouse pangenome and randomly distributed with respect to phylum, habitat and pangenome status. [src: snipe_defense_system] The alternative (H1) is that SNIPE homologues occur across bacterial phyla, are predominantly accessory (consistent with defense island mobility), and are enriched in environmental/non-clinical isolates where phage pressure is high. [src: snipe_defense_system] The report concludes H1 is supported on all four axes. [src: snipe_defense_system] It states that SNIPE resolves the ManYZ phage resistance versus metabolic cost trade-off by providing phage defense without sacrificing transporter function. [src: snipe_defense_system] It counts 1,696 species across 33 phyla, exceeding the >500 reported in the original paper. [src: snipe_defense_system] It rejects H0 (random distribution) for taxonomic distribution and environmental niche association. [src: snipe_defense_system]

### Prevalence, mobility and ecology

A Pfam-domain survey of the 293K-genome pangenome found SNIPE homologues in 1,696 species across 33 phyla, against >500 reported in Saxton et al. 2026. [src: snipe_defense_system] The survey detected DUF4041 in 4,572 gene clusters, and the report says this substantially expands the >500 homologues of the original paper. [src: snipe_defense_system] The survey filtered Pfam columns for DUF4041 in kbase_ke_pangenome.eggnog_mapper_annotations and joined gene_cluster and genome tables for taxonomy. [src: snipe_defense_system] SNIPE homologues were identified by the DUF4041 (PF13250 / IPR025280) Pfam domain in eggNOG annotations. [src: snipe_defense_system] Among the DUF4041 clusters, 2,109 have the description T5orf172, the gene family name for DUF4041. [src: snipe_defense_system] See [[concepts/pan-bacterial-prevalence-phylum-distribution-and-mobility-of-anti-phage-defense-systems]].

SNIPE-bearing taxa by phylum in the survey (species, families, genera):

| Phylum | Species | Families | Genera |
|---|---|---|---|
| Pseudomonadota | 556 | 54 | 183 [src: snipe_defense_system] |
| Actinomycetota | 334 | 30 | 105 [src: snipe_defense_system] |
| Bacillota_A | 275 | 28 | 151 [src: snipe_defense_system] |
| Bacillota | 206 | 37 | 83 [src: snipe_defense_system] |
| Bacteroidota | 114 | 32 | 61 [src: snipe_defense_system] |
| Nitrospirota | 45 | 2 | 12 [src: snipe_defense_system] |
| Cyanobacteriota | 28 | 13 | 22 [src: snipe_defense_system] |
| Planctomycetota | 22 | 10 | 18 [src: snipe_defense_system] |

The report calls this patchy distribution across many phyla and families consistent with horizontal gene transfer of defense islands. [src: snipe_defense_system]

Of the SNIPE genes, 86.7% are accessory or singleton, which the report calls consistent with mobile defense island carriage. [src: snipe_defense_system] Pangenome status came from the gene_cluster pangenome_class column for the 4,572 DUF4041 clusters. [src: snipe_defense_system] The split is 13.3% core (604 clusters), 30.7% accessory non-core non-singleton (~1,402 clusters) and 56.1% singleton (2,566 clusters). [src: snipe_defense_system] The report reads the combined 86.7% as strong support for defense island mobility, with SNIPE typically gained or lost rather than vertically inherited. [src: snipe_defense_system]

SNIPE-bearing species occupy statistically distinct environmental niches in 22/64 AlphaEarth dimensions (p < 0.05, Bonferroni-corrected). [src: snipe_defense_system] The comparison used SNIPE-bearing species (n=1,069) and non-SNIPE species (n=13,977). [src: snipe_defense_system] Dimensions were compared with Welch's t-test and Bonferroni correction for 64 tests, and effect sizes were Cohen's d with pooled standard deviation. [src: snipe_defense_system] The largest effect was dimension A19 (Cohen's d = 0.26, p = 5.0e-14). [src: snipe_defense_system] Effect sizes were small-to-medium (|d| = 0.11–0.26), which the report reads as a modest environmental shift rather than strict habitat segregation. [src: snipe_defense_system] PCA (principal component analysis) shows SNIPE species broadly distributed with a detectable environmental bias. [src: snipe_defense_system] AlphaEarth dimensions derive from satellite remote-sensing imagery at sample collection coordinates and capture signals such as vegetation, temperature, precipitation and land cover. [src: snipe_defense_system] The data came from the alphaearth_embeddings table (64 dimensions, 83K genomes). [src: snipe_defense_system] Two caveats limit this result. The analysis does not map individual dimensions to named environmental variables. [src: snipe_defense_system] AlphaEarth covers 28.4% of genomes and is biased toward environmental isolates with latitude/longitude data. [src: snipe_defense_system]

SNIPE was also detected in Klebsiella, a key phage therapy target. [src: snipe_defense_system] The report proposes that SNIPE could affect phage therapy efficacy in this pathogen. [src: snipe_defense_system]

### Functional annotation of DUF4041 clusters

The functional annotation analysis used the description and COG_category (COG = clusters of orthologous groups) columns of the eggnog_mapper_annotations table for the 4,572 DUF4041 clusters. [src: snipe_defense_system] The most common descriptions were T5orf172 (2,109) [src: snipe_defense_system], Domain of unknown function (DUF4041) (1,566) [src: snipe_defense_system], Histidine kinase (319) [src: snipe_defense_system] and seryl-tRNA aminoacylation (238). [src: snipe_defense_system] COG categories were D (cell cycle, 1,533) [src: snipe_defense_system], T (signal transduction, 1,118) [src: snipe_defense_system], J (translation, 1,066) [src: snipe_defense_system] and M (cell wall/membrane, 834). [src: snipe_defense_system] The report considers the M count aligned with SNIPE inner membrane localization. [src: snipe_defense_system]

The report considers the T5orf172 and DUF4041 descriptions, 3,675/4,572 clusters (80.4%), bona fide SNIPE-family proteins. [src: snipe_defense_system] The remaining ~20% (897 clusters) may carry DUF4041 as a secondary domain and likely represent annotation noise rather than functional SNIPE proteins. [src: snipe_defense_system] The report states that a stricter filter would retain ~80% of clusters without substantially affecting the 86.7% accessory rate or taxonomic patterns. [src: snipe_defense_system]

### Domain definitions and search strategy

Searching by the wrong Pfam family misses SNIPE. The original paper named "DUF4041" and "GIY-YIG" without citing Pfam accessions. [src: snipe_defense_system] The report resolves them as follows:

- The binding domain DUF4041 is PF13250, InterPro IPR025280, with 1,612 proteins and 2,466 species. [src: snipe_defense_system] The InterPro/UniProt dataset for IPR025280 gave 1,612 SNIPE proteins across 1,373 species. [src: snipe_defense_system] It is the report's diagnostic SNIPE domain. [src: snipe_defense_system] InterPro renamed IPR025280 "SNIPE associated domain" on the strength of the paper's functional work. [src: snipe_defense_system]
- The SNIPE nuclease is PF13455 (Mug113). It sits in GIY-YIG clan CL0418 but is not the canonical GIY-YIG family PF01541. [src: snipe_defense_system] PF13455 and PF01541 are distinct Pfam families in the same clan, which explains the paper's superfamily-level "GIY-YIG" description. [src: snipe_defense_system]
- Canonical GIY-YIG is PF01541 (IPR000305), with 68,148 proteins including restriction enzymes and DNA repair proteins. It is not the SNIPE nuclease. [src: snipe_defense_system] The report identifies the 74,686 PF01541 clusters as non-SNIPE family members. [src: snipe_defense_system]
- Searching for PF01541 co-occurrence with DUF4041 gave zero hits. [src: snipe_defense_system] The report attributes this to genuinely different Pfam families, not to annotation artifacts. [src: snipe_defense_system]
- Among the 4,572 DUF4041 clusters, 54 carry the description "Meiotically up-regulated gene 113", consistent with full-length SNIPE proteins annotated with both domains. [src: snipe_defense_system] Only 54/4,572 show Mug113 co-annotation, suggesting many SNIPE nuclease domains go undetected. [src: snipe_defense_system]
- The recommended search uses PF13250 (or the names DUF4041 / T5orf172) for the binding domain and PF13455 for the nuclease. [src: snipe_defense_system]
- The Escherichia coli SNIPE protein A0A0A1A5Z2 (558 aa) carries PF13250 at positions 232–333 and PF13455 at positions 443–520. [src: snipe_defense_system] The first is the DNA/TMP-binding domain and the second the nuclease. [src: snipe_defense_system] The InterPro/UniProt analysis identifies the nuclease domain as PF13455, not PF01541. [src: snipe_defense_system]

Co-occurrence used the eggnog_mapper_annotations Pfam columns. The E. coli architecture was verified through InterPro and UniProt REST (representational state transfer) APIs (application programming interfaces). [src: snipe_defense_system] See [[concepts/domain-based-marker-detection-and-annotation-method-bias]].

### Mechanism and the resistance–cost trade-off

Saxton et al. (2026) showed that SNIPE sits constitutively in the inner membrane. It cleaves phage DNA as the DNA passes through the ManYZ mannose transporter pore. [src: snipe_defense_system] The report says SNIPE targets the adsorption/injection step this way. [src: snipe_defense_system] The report argues that SNIPE avoids the cost of losing ManYZ, drawing on published knockout and coevolution studies that are not from the KBase Data Lakehouse. [src: snipe_defense_system] Phage lambda phenotypes come from Burmeister et al. 2021 (PMID 34032565), which used the E. coli BW25113 Keio collection. [src: snipe_defense_system] See [[concepts/phage-resistance-versus-metabolic-cost-trade-off-at-receptor-transporters]].

- manY (JW1807) knockouts gave zero phage growth after 24h, with loss of mannose transport and a partial glucose transport defect. [src: snipe_defense_system]
- manZ (JW1808) knockouts reduced phage growth by 5 orders of magnitude, with the same metabolic cost. [src: snipe_defense_system]
- The report lists manX (b1817) with specific fitness defects on D-mannose and D-glucosamine, citing Price et al. 2018. [src: snipe_defense_system]
- In coevolution experiments, man mutants sweep to >95% frequency under phage pressure. They decline sharply when phages evolve alternative injection mechanisms. [src: snipe_defense_system]
- The report concludes that SNIPE-bearing strains keep full transporter function and gain resistance without the metabolic cost of man knockouts. [src: snipe_defense_system] This is the report's interpretation, not a direct measurement.

## Phage-host interaction dataset

The report also mined the phagefoundry_strain_modelling database, which had been overlooked as "timed out during discovery" and holds 18 tables of experimental phage-host phenotype data. [src: snipe_defense_system] It contains the complete phage-host interaction dataset from Gaborieau et al. 2024, Nature Microbiology. [src: snipe_defense_system] It provides binary infection outcomes and an ML model for 188 Escherichia coli strains × 96 phages. [src: snipe_defense_system] The tables used were strainmodelling_interaction, strainmodelling_organism, strainmodelling_organism_metadata and strainmodelling_experiment_metric. [src: snipe_defense_system] The dataset has 188 E. coli strains (ECOR, NILS and clinical/environmental isolates) and 96 phages (41 Podoviridae, 32 Myoviridae, 23 Siphoviridae), giving 17,672 binary infection outcomes. [src: snipe_defense_system] The overall infection rate is 22% (3,929 positive / 13,743 negative). [src: snipe_defense_system] The paper's machine-learning model reached AUC (area under curve) = 0.883 and accuracy = 84.3%, trained on 1,582 gene cluster presence/absence features with SHAP (Shapley additive explanations) importance scores. [src: snipe_defense_system]

Infection rates differ by family. Myoviridae infect 43.4% (2,531/5,828) of pairs, read as broad host range via tail fibers rather than ManYZ dependence. [src: snipe_defense_system] Podoviridae infect 13.0% (978/7,520), read as moderate host range. [src: snipe_defense_system] Siphoviridae infect 9.7% (420/4,324), read as narrow host range. [src: snipe_defense_system]

Lambdavirus 411_P1 infects only 1 of 188 strains (NILS06), a 0.5% infection rate and the lowest of any phage in the dataset. [src: snipe_defense_system] The report calls this consistent with widespread ManYZ variation or loss conferring near-universal lambda resistance. [src: snipe_defense_system] That is an interpretation, not a measurement.

The report states that the Gaborieau paper identifies adsorption factors (surface receptors), not antiphage defense systems, as the primary predictors of phage-host interaction. It says this supports SNIPE's niche at the adsorption/injection interface. [src: snipe_defense_system]

## ManXYZ fitness in Escherichia coli K-12

In E. coli K-12, the fitness data show ManXYZ is severely and specifically required on mannose and glucosamine. [src: snipe_defense_system] The data are RB-TnSeq (random barcode transposon sequencing) fitness for E. coli K-12 (Keio collection, 168 experiments; Price et al. 2018). [src: snipe_defense_system] The scores are log2 ratios. [src: snipe_defense_system] They were queried locally from the Fitness Browser SQLite database feba.db, downloaded from Figshare. [src: snipe_defense_system] The tables used were GeneDomain and GeneFitness, also available as kescience_fitnessbrowser in the KBase Data Lakehouse. [src: snipe_defense_system] The Lakehouse API was experiencing a 503 outage during the analysis. [src: snipe_defense_system] The database has 48 organisms, 228K genes and 27M fitness scores [src: snipe_defense_system]; the report also gives 7,552 experiments. [src: snipe_defense_system] The feba.db file is 7.4 GB. [src: snipe_defense_system] See [[concepts/substrate-specificity-of-the-mannose-pts-manxyz-from-genome-wide-fitness]] and [[entities/manxyz-mannose-phosphotransferase-system]].

| Gene | Experiments | Worst fitness | Avg fitness | Conditions fit < -1 | Conditions fit < -2 |
|---|---|---|---|---|---|
| manX | 168 | -3.93 | -0.249 | 6 | 4 [src: snipe_defense_system] |
| manY | 168 | -3.82 | -0.171 | 10 | 4 [src: snipe_defense_system] |
| manZ | 168 | -4.14 | -0.082 | 7 | 4 [src: snipe_defense_system] |

Mean fitness on selected sole carbon sources, and under one stress:

| Condition | manX | manY | manZ |
|---|---|---|---|
| D-glucosamine | -3.79 | -2.79 | -3.63 [src: snipe_defense_system] |
| D-mannose | -2.75 | -3.00 | -2.74 [src: snipe_defense_system] |
| D-trehalose | -1.27 | -1.49 | no value shown [src: snipe_defense_system] |
| Sodium chlorite | -1.47 | -1.32 | -1.08 [src: snipe_defense_system] |

The three genes are tightly co-fitness correlated (manX↔manZ r=0.851, manX↔manY r=0.705, manY↔manZ r=0.725). The report reads this as confirming a single operon. [src: snipe_defense_system]

UniProt annotates ManX as a fructose-specific PTS component. [src: snipe_defense_system] The fitness data contradict that label. Against fruA, the fitness values were:

| Substrate | manX | manY | manZ | fruA |
|---|---|---|---|---|
| D-mannose | -2.75 | -3.00 | -2.74 | -0.06 [src: snipe_defense_system] |
| D-glucosamine | -3.79 | -2.79 | -3.63 | -1.02 [src: snipe_defense_system] |
| D-fructose | -0.22 | +0.15 | -0.07 | -1.44 [src: snipe_defense_system] |

ManXYZ mutants grow normally on fructose (fitness ≈ 0) but are crippled on mannose and glucosamine. [src: snipe_defense_system] FruA, the actual fructose PTS, shows the opposite pattern. [src: snipe_defense_system] The report concludes that ManYZ is a mannose/glucosamine-specific transporter, consistent with its role as the phage lambda entry receptor. [src: snipe_defense_system]

Among the 48 Fitness Browser organisms, ManXYZ is present only in E. coli K-12, with fitness data for 168 conditions. [src: snipe_defense_system] No Klebsiella strain in the Fitness Browser carries ManXYZ by gene name. [src: snipe_defense_system] This limits any fitness test of the SNIPE–ManXYZ link in Klebsiella. See [[concepts/fitness-data-coverage-gaps-for-defense-genes]].

## SNIPE in the Fitness Browser

The Fitness Browser holds one archaeal SNIPE protein, from Methanococcus maripaludis JJ (MMJJ_RS01635), with DUF4041 and Mug113 nuclease domains and 129 experiments. [src: snipe_defense_system] It is the only Fitness Browser organism with the full two-domain architecture (PF13250 + PF13455). [src: snipe_defense_system] It is also annotated with PF10544 (DUF2525). [src: snipe_defense_system] Across the 48 organisms, 7 genes carry PF13455, spread over 6 organisms: Azospirillum brasilense, Bacteroides thetaiotaomicron, Cupriavidus, Desulfovibrio vulgaris, Paraburkholderia kururiensis and M. maripaludis. [src: snipe_defense_system] The report calls M. maripaludis the first organism with both a confirmed SNIPE protein and genome-wide fitness data. [src: snipe_defense_system] See [[entities/methanococcus-maripaludis]].

The gene shows mild fitness defects under specific conditions, with a minimum fitness of -1.16 on formate/acetate. [src: snipe_defense_system] It is dispensable under most conditions. [src: snipe_defense_system] As an archaeon, its phage biology context differs significantly from the Enterobacterales phage lambda system. [src: snipe_defense_system]

## Klebsiella in PhageFoundry

Klebsiella is the only PhageFoundry species with both SNIPE and the PF00358 ManX-family PTS domain by exact Pfam accession. [src: snipe_defense_system] PhageFoundry Genome Browsers comprise 4 species-specific databases for Acinetobacter, Klebsiella, P. aeruginosa and P. viridiflava. [src: snipe_defense_system] The data came from the PhageFoundry browser_eggnog_description and browser_annotation tables. [src: snipe_defense_system] The defense-term search covered four species in the browser_eggnog_description tables. [src: snipe_defense_system] See [[entities/phagefoundry]] and [[entities/klebsiella]].

Defense-related term counts from the PhageFoundry search:

| Species | DUF4041 | GIY-YIG | Nuclease | Restriction | Abortive infection |
|---|---|---|---|---|---|
| Klebsiella | 1 | 1 | 98 | 42 | 2 [src: snipe_defense_system] |
| Acinetobacter | 0 | 3 | 91 | 33 | 2 [src: snipe_defense_system] |
| P. aeruginosa | 0 | 2 | 125 | 54 | 2 [src: snipe_defense_system] |
| P. viridiflava | 0 | 0 | 90 | 41 | 1 [src: snipe_defense_system] |

- DUF4041 (SNIPE) is represented by 1 description and 3 proteins of 558 aa each in Klebsiella. Acinetobacter, Pseudomonas aeruginosa and Pseudomonas viridiflava each have 0. [src: snipe_defense_system]
- The three proteins (JJW41_17025, KFB13_RS08150, KFB31_RS01490) match the length of E. coli SNIPE A0A0A1A5Z2. This strongly suggests full-length two-domain SNIPE proteins. [src: snipe_defense_system]
- Klebsiella has 28 proteins with mannose PTS IID (ManZ) eggNOG annotations. [src: snipe_defense_system] It has 1 with a mannose PTS IIA (ManX) eggNOG annotation. [src: snipe_defense_system]
- PF02378 / PTS_EIIC (ManY family) annotations number 4,619 in Klebsiella, 891 in Acinetobacter, 1,067 in Pseudomonas aeruginosa and 260 in Pseudomonas viridiflava. [src: snipe_defense_system]
- PF00358 / PTS_EIIA_1 (ManX family) annotations number 571 in Klebsiella and 0 in each of the other three. [src: snipe_defense_system]

The report reads the co-occurrence of SNIPE and the mannose transporter as consistent with SNIPE defending ManYZ pores that provide a phage entry route. [src: snipe_defense_system] This is an interpretation from co-occurrence alone.

## Data and Methods

The report combines these sources:

- A Pfam-domain survey of the 293K-genome pangenome. [src: snipe_defense_system] The kbase_ke_pangenome dataset contains 293K genomes, 93M eggNOG annotations with Pfam domains, and 132M gene clusters with core/accessory/singleton status. [src: snipe_defense_system]
- Local Fitness Browser queries of feba.db. [src: snipe_defense_system] The Fitness Browser is described with 48 organisms, 228K genes, 27M fitness scores and 7,552 experiments (Price et al. 2018). [src: snipe_defense_system]
- PhageFoundry annotation tables. [src: snipe_defense_system]
- The phagefoundry_strain_modelling database (Gaborieau et al. 2024). [src: snipe_defense_system]
- AlphaEarth embeddings joined to SNIPE species labels. [src: snipe_defense_system]
- NMDC (National Microbiome Data Collaborative) metagenome annotations. [src: snipe_defense_system]

The phage lambda phenotypes and coevolution results are taken from the published literature. [src: snipe_defense_system]

Output tables from the analysis include duf4041_clusters.csv (4,572 gene clusters with DUF4041) [src: snipe_defense_system], snipe_both_domains.csv (all 4,572 DUF4041 hits, used as the primary SNIPE marker; the name reflects the original "both domains" query, abandoned after zero DUF4041+PF01541 overlaps) [src: snipe_defense_system], and snipe_taxonomy.csv (taxonomy for 1,696 SNIPE species). [src: snipe_defense_system]

## Caveats and Open Work

- Published knockout and coevolution data used for the cost argument are not from the KBase Data Lakehouse. [src: snipe_defense_system]
- The M. maripaludis SNIPE is archaeal, so its phage context differs from the phage lambda system. [src: snipe_defense_system] Its gene is mostly dispensable. [src: snipe_defense_system]
- ManXYZ fitness exists only for E. coli K-12, and no Klebsiella strain in the Fitness Browser carries ManXYZ by gene name. [src: snipe_defense_system]
- PhageFoundry provides genome annotations only (GenomeDepot format), with no fitness/TnSeq (transposon sequencing) tables, so no Klebsiella-specific SNIPE or ManYZ fitness data exist here. [src: snipe_defense_system] Generating them would need new mutant libraries in natural SNIPE carriers such as K. pneumoniae NCTC9140 or HS11286. [src: snipe_defense_system] The report has developed PLAN_fitness_data_curation.md to curate external K. pneumoniae Tn-Seq datasets. [src: snipe_defense_system]
- The Klebsiella SNIPE inference rests on protein length, and the report says only that this strongly suggests two domains. [src: snipe_defense_system]
- AlphaEarth results cover only 28.4% of genomes and do not name the environmental variables behind each dimension. [src: snipe_defense_system]
- eggNOG Pfam annotations may miss divergent SNIPE homologues. [src: snipe_defense_system] DUF4041 (T5orf172) is strongly associated with SNIPE, but some hits may represent non-SNIPE proteins. [src: snipe_defense_system]
- The planned comparison of COG V defense gene density in SNIPE versus non-SNIPE species could not be completed via REST API, because the 93M × 132M row join requires Spark Connect. [src: snipe_defense_system]
- The NMDC metagenome ecosystem breakdown was limited because only 2 samples matched the API query format. The report suggests interactive MCP tool queries would improve coverage. [src: snipe_defense_system]

## Slots Into

- [[concepts/pan-bacterial-prevalence-phylum-distribution-and-mobility-of-anti-phage-defense-systems]]: SNIPE is found in 1,696 species across 33 phyla, and 86.7% of its genes are accessory or singleton. [src: snipe_defense_system]
- [[concepts/environmental-niche-association-of-defense-system-carriers]]: SNIPE-bearing species differ in 22/64 AlphaEarth dimensions. [src: snipe_defense_system]
- [[concepts/domain-based-marker-detection-and-annotation-method-bias]]: GIY-YIG PF01541 versus PF13455 shows that the wrong Pfam accession misses SNIPE. [src: snipe_defense_system]
- [[concepts/substrate-specificity-of-the-mannose-pts-manxyz-from-genome-wide-fitness]]: ManXYZ is crippled on mannose and glucosamine but normal on fructose. [src: snipe_defense_system]
- [[concepts/phage-resistance-versus-metabolic-cost-trade-off-at-receptor-transporters]]: The report proposes that SNIPE gives the resistance of man knockouts without their cost. [src: snipe_defense_system]
- [[concepts/fitness-data-coverage-gaps-for-defense-genes]]: Only M. maripaludis has SNIPE fitness data, and no Klebsiella strain in the Fitness Browser carries ManXYZ. [src: snipe_defense_system]
- [[concepts/adsorption-receptors-versus-defense-systems-as-determinants-of-phage-host-range]]: ManYZ is a phage lambda entry receptor that SNIPE defends. [src: snipe_defense_system] The report cites Gaborieau et al. as naming surface receptors as the main predictors of host range. [src: snipe_defense_system]
