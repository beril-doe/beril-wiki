---
type: "Summary"
description: "Summary of the ENIGMA Carbon Census, a tiered knowledge census of 83 groundwater and necromass enrichment compounds that links compound identity, pathways, ENIGMA-isolate utilizers, GTDB placement and environmental occurrence, and finds 74 of the 83 compounds organism-dark."
doc_type: "short"
full_text: "sources/enigma_carbon_census_1__REPORT.md"
---
# ENIGMA Carbon Census — Tiered Knowledge Census of 83 Enrichment Compounds

## Overview

The ENIGMA Carbon Census integrates compound identity resolution, pathway and enzyme linkage, ENIGMA-isolate utilization predictions, GTDB strain placement, SSO field occurrence, and global environmental abundance for 83 enrichment compounds: 59 from SSO groundwater and 24 from necromass. All 83 compounds resolved to structures with InChIKeys via PubChem, 54 linked to KEGG, and 9 were callable under the project definition: 8 through an ENIGMA-isolate utilizer call and 1, lauric acid, through a Tier-1 measured RB-TnSeq (random barcode transposon sequencing, a pooled mutant-fitness assay) carbon-source growth experiment in the Fitness Browser, confirmed structurally by an InChIKey re-match. Lauric acid's Fitness Browser organism is a reference bacterium, not an ENIGMA isolate, so the ENIGMA-isolate deliverable was unchanged by its inclusion: lauric acid carries no ENIGMA-isolate strain, genus or field rows and does not appear in deliverable (a). One of the 8 isolate calls, xanthine, was later identified as a carbon-category error (see below). The central result is a resource-defined knowledge gap: 74/83 compounds (89%) were organism-dark, meaning their genetic determinants of utilization were not linkable through the queried the KBase Data Lakehouse and curated resources. [src: enigma_carbon_census_1]

## Key Findings

### Coverage and the organism-dark set

The census funnel was 83 compounds → 83 structure-resolved → 54 KEGG-linked → 9 callable → 74 organism-dark. The dark fraction was similar by source: 53/59 groundwater compounds (90%) and 21/24 necromass compounds (88%) were dark, indicating that the observed gap tracks chemical class more closely than sampling source. The 74 dark compounds comprised 33 KEGG-linked compounds with no reaction in queried genomes, 29 fully orphan compounds with no KEGG link, 6 biosynthesis-known/catabolism-unknown compounds, and 6 compounds represented only by generic reactions. The discovery funnel is shown in `figures/08_funnel.png`. [src: enigma_carbon_census_1]

By chemical class, the report states that the dark set is dominated by exactly the predicted classes: Alkaloids, Shikimates/Phenylpropanoids, Terpenoids, and Fatty acids. The dark-matter taxonomy is shown in `figures/09d_dark_taxonomy.png`. [src: enigma_carbon_census_1]

The 6 biosynthesis-known dark compounds were Tyramine, guanidineacetic acid, cinnamic acid, caffeic acid, palmitic acid, and farnesol; they are targets for external MIBiG and biosynthetic-literature consultation rather than equivalent to fully orphan compounds. They carry annotated biosynthetic-direction signatures but no catabolic call. MIBiG consultation was flagged as an external step because MIBiG was not queried in the KBase Data Lakehouse. The 29 fully orphan compounds are the hardest discovery targets and were disproportionately necromass-derived: 13/24 necromass compounds versus 16/59 groundwater compounds were fully orphan. [src: enigma_carbon_census_1]

### Chemical-class coverage and H1

The 9 nominally callable compounds were overwhelmingly pollutant-adjacent aromatics. The 8 ENIGMA-isolate-callable compounds were salicylic acid, 3-hydroxybenzoic acid, 4-hydroxybenzaldehyde, phthalic acid, terephthalic acid, Phenylethylamine, xanthine, and Abscisic acid. The additional callable compound, lauric acid, was callable only through measured fitness and had no ENIGMA-isolate utilizer rows. The isolate-callable set was concentrated in Shikimates/Phenylpropanoids: salicylic acid, 3-hydroxybenzoic acid, 4-hydroxybenzaldehyde, phthalic acid, and terephthalic acid; the other isolate calls were Phenylethylamine and xanthine in Alkaloids and Abscisic acid in Terpenoids, the last being a single 2-strain call. Lauric acid is a Fatty acid that is callable on a measured-fitness basis only. [src: enigma_carbon_census_1]

Per-compound counts from the project's callable table (source; class; evidence tier; ENIGMA-isolate strains; high-certainty strains; genera; field genera; top field prevalence):
- salicylic acid — groundwater; Shikimates/Phenylpropanoids; T2_3_reaction; 129 strains; 2 high-certainty; 24 genera; 20 field genera; top field prevalence 0.86. [src: enigma_carbon_census_1]
- 3-hydroxybenzoic acid — groundwater; Shikimates/Phenylpropanoids; T2_3_reaction; 127 strains; 18 high-certainty; 42 genera; 33 field genera; top field prevalence 0.90. [src: enigma_carbon_census_1]
- 4-hydroxybenzaldehyde — groundwater; Shikimates/Phenylpropanoids; T2_3_reaction; 125 strains; 10 high-certainty; 34 genera; 25 field genera; top field prevalence 0.86. [src: enigma_carbon_census_1]
- phthalic acid — necromass; Shikimates/Phenylpropanoids; T2_3_reaction; 36 strains; 0 high-certainty; 15 genera; 12 field genera; top field prevalence 0.75. [src: enigma_carbon_census_1]
- terephthalic acid — necromass; Shikimates/Phenylpropanoids; T2_3_reaction; 34 strains; 34 high-certainty (a single-reaction-signature artifact, see below); 17 genera; 10 field genera; top field prevalence 0.67. [src: enigma_carbon_census_1]
- Phenylethylamine — groundwater; Alkaloids; T2_3_reaction; 28 strains; 0 high-certainty; 11 genera; 7 field genera; top field prevalence 0.61. [src: enigma_carbon_census_1]
- xanthine — groundwater; Alkaloids; T3_kegg; 13 strains; 0 high-certainty; 6 genera; 4 field genera; top field prevalence 0.75. It is listed only because the committed table was not regenerated, and its carbon-catabolism call is erroneous. [src: enigma_carbon_census_1]
- Abscisic acid — groundwater; Terpenoids; T2_3_reaction; 2 strains; 0 high-certainty; 1 genus; 1 field genus; top field prevalence 0.02. [src: enigma_carbon_census_1]
- lauric acid — necromass; Fatty acids; T1_measured; 0 strains; 0 high-certainty; 0 genera; 0 field genera; no field prevalence, because its Tier-1 call comes from a reference bacterium rather than an ENIGMA isolate. [src: enigma_carbon_census_1]

The report contains an unresolved count discrepancy. The callable table lists five Shikimates/Phenylpropanoids compounds: salicylic acid, 3-hydroxybenzoic acid, 4-hydroxybenzaldehyde, phthalic acid, and terephthalic acid. However, the report's interpretation states that six of the eight callable compounds route through well-characterized aromatic catabolism (salicylate, the hydroxybenzoates/-aldehyde, and the two phthalates converging on protocatechuate/catechol and the β-ketoadipate pathway). The report does not reconcile the two counts, and this page does not resolve them. The same interpretation assigns phenylethylamine to the phenylacetyl-CoA (*paa*) ring-cleavage route and describes xanthine as a purine (nitrogen) pathway mis-included in the callable set. [src: enigma_carbon_census_1]

H1, the hypothesis of a coverage gradient by chemical class, was not formally supported: the pre-registered null of uniform coverage across chemical classes was not rejected. A chi-square test on the 8 ENIGMA-isolate-callable compounds gave χ²=5.07, p=0.53, df=6, using class counts of Shikimates 5/25, Alkaloids 2/26, Terpenoids 1/17, Fatty acids 0/10, Polyketides 0/2, AA/Peptides 0/2, and mixed 0/1. Adding measured-fitness lauric acid did not change the verdict. The pattern remains directionally useful for enrichment design but is underpowered and confounded with annotation coverage. [src: enigma_carbon_census_1]

Xanthine was mis-scored as carbon-catabolic because allowlisted reaction R02107, xanthine→urate, represents purine nitrogen acquisition rather than carbon catabolism. The effective carbon-callable set is therefore 8 rather than 9; R02107 was removed from the carbon allowlist, but committed tables still contain xanthine because they were not regenerated. The fix was made in `build_nb03.py`, and a re-run of NB03→NB04→NB08 would drop xanthine. The error is specific to the R02107 nitrogen-route reaction and should not be generalized to all purine carbon catabolism. The report notes that a bacterial carbon route for purines exists, but it is a distinct anaerobic gene cluster that this project does not score. [src: enigma_carbon_census_1]

### Co-occurrence, specialization, and H2

H2, the hypothesis of broad cross-module modularity, was not supported beyond a shared aromatic funnel. Among 8 ENIGMA-isolate-callable capacities across genomes carrying at least 1 capacity, the mean versatility was ~1.19, the median was 1, and the maximum was 4 capacities per genome. Co-occurrence was first reported with the φ coefficient. However, φ compresses toward zero when a capacity is rare, and most capacities are present in only tens-to-hundreds of 3109 genomes, so φ can hide a real multiplicative enrichment. A review reanalysis therefore recomputed two effect sizes from the saved 2×2 counts without a Spark re-run: Haldane-corrected odds ratios (ORs) with 95% confidence intervals, and Jaccard indices. Within-aromatic pairs had median OR 1.12, with 3/10 pairs having confidence intervals entirely above 1, and median Jaccard 0.026. Within-other pairs had median OR 7.43, with 1/3 intervals above 1, but this estimate was driven by the Haldane correction on near-zero counts. Cross-block pairs, which link distinct lower pathways and are the genuine modularity test, had median OR 2.28, with 4/15 confidence intervals entirely above 1 and median Jaccard approximately 0. Figures: `figures/05_cooccurrence.png` and `figures/05b_odds_ratio_forest.png`. [src: enigma_carbon_census_1]

The strongest cross-block signals involved Phenylethylamine and aromatic-funnel acids: 4-hydroxybenzaldehyde + Phenylethylamine had OR 2.84, 95% CI 1.49–5.40, q=0.035, n11=11; phthalic acid + Phenylethylamine had OR 3.37, 95% CI 1.46–7.75, q=0.071, n11=6. The report treats this signal, which the OR surfaced and φ hid, as expected and mechanistically coherent. Phenylethylamine is itself an aromatic-derived substrate: it is deaminated to phenylacetate and then catabolized through the *paa*/phenylacetyl-CoA route, so versatile aromatic degraders tend to carry both capacities. Their Jaccard remained approximately 0.04, meaning only ~4% of genomes with either capacity carried both. Cross-module co-occurrence was near-zero in share terms (Jaccard ≈ 0): only 25 of 3109 genomes (0.8%) carried both an aromatic and a non-aromatic capacity. A Haldane odds ratio did surface a modest phenylethylamine×aromatic enrichment (OR ≈ 2.8–3.4), but that enrichment is itself aromatic-derived. The verdict was no broad cross-module modularity: the one positive signal reflects co-occurrence within the broad aromatic-catabolism phenotype, not modular co-assembly of mechanistically distinct modules. The result supports phylogenetic concentration rather than a portable, broadly co-assembled module set. [src: enigma_carbon_census_1]

The callable phenotype was specialist-dominated: 675 genomes carried exactly 1 of the 8 aromatic/alkaloid capacities, whereas 18 carried at least 3, with a maximum of 4. Generalist chassis were concentrated in Paraburkholderia (5), Burkholderia (4), and Hydrogenophaga (2), with the rest scattered across Burkholderiaceae. Burkholderiales dominated utilizer counts. The high-versatility genera Polaromonas, Alcaligenes, Burkholderia, Paraburkholderia, Comamonas, and Hydrogenophaga clustered in that order, which the report reads as evidence that versatility is a clade trait rather than a widely portable module. Compound-specific conservation was observed within the called set, including approximately 100% 3-hydroxybenzoic-acid capacity in Castellaniella and Hylemonella, approximately 92–100% 4-hydroxybenzaldehyde capacity in Novosphingobium and Sphingobium, 100% phthalic-acid capacity in Paenarthrobacter, and 92% and 85% Comamonas capacity for 3-hydroxybenzoic acid and 4-hydroxybenzaldehyde, respectively. These conservation fractions are denominated over depot genomes that already carry some catabolic call, not over all genomes of each genus. They therefore describe within-called-set specialization rather than absolute prevalence. Capacity breadth across the chassis was led by 3-hydroxybenzoic acid (296 genomes, 53 genera) and salicylic acid (197 genomes, 28 genera); Abscisic acid was a 2-genome edge case. Figures: `figures/05_genus_versatility.png`, `figures/09b_chassis.png`, and `figures/09c_clade_conservation.png`. [src: enigma_carbon_census_1]

### Source tracking and H3

H3, the groundwater-versus-necromass source-tracking hypothesis, was untestable and confounded. Only 2 of the 8 ENIGMA-isolate-callable compounds were necromass-sourced—terephthalic acid and phthalic acid—and both were phthalate-class aromatics with Actinomycetota-heavy utilizers. Lauric acid was also necromass-sourced but had only a reference-bacterium measured-fitness call, no ENIGMA-isolate rows, and no field data. The project therefore reported an SSO field-occurrence atlas rather than a statistical source contrast. [src: enigma_carbon_census_1]

The SSO field atlas, built from Zhou Lab 16S data in the `enigma_coral` bricks, detected 62 of the implicated utilizer genera at genus resolution, with top field prevalences approximately 0.7–0.9; 3-hydroxybenzoic-acid utilizers reached 0.90 field prevalence. [src: enigma_carbon_census_1]

### Tiered isolate and phylogenetic deliverables

Deliverable (a) contained 569 ENIGMA-isolate utilizer prediction rows across the 8 ENIGMA-isolate-callable compounds. Counts were salicylic acid 129 strains, 3-hydroxybenzoic acid 127, 4-hydroxybenzaldehyde 125, phthalic acid 36, terephthalic acid 34, Phenylethylamine 28, xanthine 13, and Abscisic acid 2. Lauric acid had 0 ENIGMA-isolate rows because its call was based only on measured fitness in a reference bacterium. [src: enigma_carbon_census_1]

Deliverable (b) placed 494 strain records representing 359 distinct strains on GTDB taxonomy. The placements included 64 high-certainty records based on gene-complete Tier-2 pathways, 387 medium-certainty records based on Tier-2 pathways, and 43 medium-certainty records based on Tier-3 signature enzymes. Utilizers were concentrated in Pseudomonadota and Burkholderiales, with compound-specific contributions from Pseudomonadales and Sphingomonadales, including 47 Sphingomonadales strains for 4-hydroxybenzaldehyde. H4 was partially supported: it was strongly supported for the 8 ENIGMA-isolate-callable compounds and null for the other 75 Tier 0 compounds lacking isolate-level placement. Lauric acid is callable only on measured RB-TnSeq fitness in a reference bacterium. It contributes no ENIGMA-isolate phylogenetic prediction and so sits outside both arms. Figures: `figures/04_utilizer_genera.png` and `figures/06_phylo_order_map.png`. [src: enigma_carbon_census_1]

Terephthalic acid had 34/34 high-certainty records, but this was a single-reaction-signature artifact rather than strong evidence of pathway completeness. Certainty is based on the raw number of carried signature reactions divided by required reactions, and is not directly comparable across compounds with different signature lengths. Terephthalic acid's signature has 1 required reaction and trivially scores 1.0 for any carrier, whereas phthalic acid's 3-reaction signature cannot. The report therefore treats the terephthalic 34/34 high-certainty headline as the weakest completeness call, not the strongest. As literature context rather than a project finding, the report describes terephthalate proceeding via terephthalate dioxygenase to protocatechuate, concentrated in Pseudomonadota (Ideonella/Comamonas) and actinobacterial degraders. Figure: `figures/06_certainty_composition.png`. [src: enigma_carbon_census_1]

### Environmental abundance atlas

The global environmental atlas covered 86 implicated genera using 3825 taxonomy-bearing NMDC metagenomes and 302 Planet Microbe marine runs. In NMDC, 83/86 genera were detected in 1719 metagenomes, and 99% of samples were labeled through two independent ontology systems. Macro-environment counts were soil 2260, freshwater 723, periphyton 472, plant 119, and sediment 42. The local and global atlases measure organismal abundance or occurrence, not catabolic activity, because no environmental dataset measured the census compounds. Genus abundance indicates where the organisms live, not where the compounds are degraded. Figure: `figures/07b_env_atlas_heatmap.png`. [src: enigma_carbon_census_1]

An exploratory soil-versus-freshwater abundance contrast recovered textbook biogeography. Soil-enriched genera were classic soil taxa, including Mycobacterium (log2 +5.09), Terriglobus (+5.29), Nitrobacter (+4.79), Afipia, Streptomyces, Nocardioides, and Mesorhizobium. Freshwater-enriched genera were aquatic Betaproteobacteria, including Cellvibrio (log2 −2.19), Curvibacter, Rhodoferax, Comamonas, and Acidovorax. The contrast's significance values are not calibrated (see Caveats). Figure: `figures/07b_soil_fresh_enrichment.png`. [src: enigma_carbon_census_1]

Periphyton, representing freshwater biofilms such as epilithon, epipsammon, and epiphyton, was separated out from bulk freshwater as its own ENVO/GOLD class. That separation surfaced a strong Burkholderiales/Comamonadaceae reservoir which bulk-water labels hide: listed genera (Rhizobacter, Variovorax, Polaromonas, Methylibium, Sphingomonas, Hydrogenophaga) reached approximately 96–97% prevalence with mean relative abundance approximately 0.005–0.009. Label-free abundance outliers peaked in periphyton and soil, including Nocardioides at 0.43 in epipsammon, Hydrogenophaga at 0.28 in epiphyton, and Mycobacterium at 0.22 in soil; outliers occurred for 34 genera in periphyton and 32 in soil. The freshwater-biofilm/periphyton enrichment of this clade (~97% prevalence in periphyton samples) rests primarily on the project's own NB07b abundance data rather than a comparative-microbiology citation. The report asks that it be read as this project's observation pending a targeted literature anchor. [src: enigma_carbon_census_1]

The marine arm was primarily a negative biome contrast. All 68/68 listed genera showed positive abundance across 302 Planet Microbe runs, but terrestrial/freshwater genera generally occurred at approximately 1e-3 to 1e-4 abundance in open ocean. Alteromonas was a genuine marine member, occurring at 0.048 in 240/302 runs with prevalence 0.79; Pseudomonas and Sphingomonas had abundances 0.011 and 0.0063, respectively. [src: enigma_carbon_census_1]

### Physicochemistry and annotation ceiling

PubChem physicochemical descriptors were resolved for all 83 compounds and contrasted between callable and dark sets. With only n=9 callable compounds, these comparisons were directional rather than inferential: Mann–Whitney tests were reported as direction plus uncorrected p-values. Callable compounds had median Complexity 133 versus 207 for dark compounds, p=0.034; median MolecularWeight 152 versus 179, p=0.066; and median HeavyAtomCount 11 versus 13, p=0.057. Callable compounds also showed directionally higher polarity, with TPSA 57 versus 41 and hydrogen-bond donors 2 versus 1. The result may reflect an annotation-coverage ceiling as much as biological bioavailability: simple, common, pollutant-adjacent aromatics are also the compounds most likely to be represented in KEGG, ModelSEED, and genome-depot annotations. No physicochemical separation was detected between groundwater and necromass compounds (all contrasts p>0.14), reinforcing that source does not predict chemistry in this compound set. Figures: `figures/09a_physicochem_callable_dark.png` and `figures/09a_bioavailability_space.png`. [src: enigma_carbon_census_1]

## Caveats and Limitations

“Organism-dark” means not linkable through the queried the KBase Data Lakehouse and curated resources, not unknown to science. Class-level catabolic literature exists for compounds including monoterpenes and nicotine, while the project’s zero literature rescues resulted from a shallow PubMed-title-only screen. A PaperBLAST or abstract-level search could reclassify part of the dark set. [src: enigma_carbon_census_1]

The dark fraction depends on the catabolic-direction filter: the 8 ENIGMA-isolate calls used a genome-prevalence-<10% signature-reaction filter retaining reactions that were catabolic according to KEGG degradation-map membership or a 3-reaction curated allowlist. The filter yielded 846 Tier-2 pathway and 102 Tier-3 signature genome-compound calls. Biosynthetic-only signatures were excluded and landed in the dark set. A different filter could change the callable/dark boundary. Lauric acid was independently callable through measured fitness and was not subject to this filter. [src: enigma_carbon_census_1]

Soil-versus-freshwater enrichment statistics were exploratory and not calibrated. Treating each metagenome as independent in rank tests over compositional, zero-inflated relative abundances can inflate significance; all 83 genera reached q<0.05, with many q values near 1e-70. Direction and rank were considered more trustworthy than the p-values, and label-free outlier discovery was the more defensible signal. [src: enigma_carbon_census_1]

The environmental atlas is a biome-occupancy proxy, not evidence of compound degradation or activity. Genus occurrence does not validate the upstream compound→pathway→organism inference and cannot show that any genus degrades a census compound in any sampled environment. The H3 contrast was genuinely untestable because only 2 necromass compounds were ENIGMA-isolate-callable and both were phthalate-class aromatics. The marine arm was small and gene-blind, with 302 runs and presence/abundance data only, so it is suitable only as a negative biome contrast. [src: enigma_carbon_census_1]

The callable-versus-dark physicochemical analysis was descriptive rather than calibrated inference because n=9 callable compounds were available and the Mann–Whitney p-values were uncorrected. Xanthine remains a category error in the carbon census until downstream tables are regenerated after excluding R02107. [src: enigma_carbon_census_1]

The project also identified data-pipeline requirements: NMDC and Planet Microbe inputs were species-level, so genus abundance required species-to-genus aggregation; the NMDC denominator was 3825 taxonomy-bearing covstats files rather than approximately 6700 sample-file-lookup rows (using the lookup count deflates relative abundances by ~1.75×); and sample-level environment labels from biosample_set provided 99% coverage across two ontologies, compared with approximately 13% from study-table GOLD labels. [src: enigma_carbon_census_1]

The report's interpretation section says "75 dark compounds" are not a failure of method, which conflicts with the revised headline count of 74. The report's generated-data description identifies 75 as the pre-reclassification count. This page uses the headline 74 and records the stale 75 here rather than silently dropping it. [src: enigma_carbon_census_1]

Data sources and their roles:
- PubChem PUG-REST supplied identity resolution (name → CID → InChIKey/SMILES) plus KEGG, ChEBI and ModelSEED cross-references.
- ModelSEED biochemistry supplied compound → reaction → enzyme linkage for Tier 2/3 inference.
- Fitness Browser RB-TnSeq carbon-source experiments supplied the Tier-1 measured-utilization channel.
- The ENIGMA SSO field data (Zhou Lab 16S, `enigma_coral` bricks) supplied local genus occurrence.
- NMDC collections (`covstats_taxonomy_rollup`, `sample_file_lookup`, `biosample_set`) supplied terrestrial/freshwater genus abundance with ENVO/GOLD environment labels.
- Planet Microbe (`planetmicrobe.planetmicrobe`: `run_to_taxonomy`, `taxonomy`, and `run`/`experiment`/`sample`/`project`/`campaign` tables) supplied the marine genus-abundance contrast for global deliverable (c).
- The pangenome↔ENIGMA taxonomic bridge is genus-level at best, so the project avoided isolate-specific transfer of pangenome Tier-2 reconstructions in favor of direct genome_depot annotation.
- The report cites these core data sources: PubChem (Kim et al., *Nucleic Acids Res.* 2023); KBase (Arkin et al., *Nat. Biotechnol.* 2018); Fitness Browser / RB-TnSeq (Price et al., *Nature* 2018); GTDB (Parks et al., *Nucleic Acids Res.* 2022); ModelSEED (Henry et al., *Nat. Biotechnol.* 2010); NMDC (Eloe-Fadrosh et al., *Nat. Microbiol.* 2022); and Planet Microbe (Ponsero et al., *GigaScience* 2021). [src: enigma_carbon_census_1]

## Workflow, Generated Data and Figures

Analysis notebooks and their roles:
- `00_compound_profile.ipynb` loads the compound spreadsheet and profiles the 83 compounds by class, source and MW/LogP.
- `01_identity_resolution.ipynb` maps each name to a PubChem CID, then to InChIKey/SMILES, and adds cross-references.
- `02_pathway_linkage.ipynb` and `02b_linkage_deepening.ipynb` link compounds to pathways and enzymes through multiple channels, with a Phase-1 gate.
- `02c_fb_inchikey_rematch.ipynb` is the review-I1 structural re-match (name→PubChem→InChIKey) of Fitness Browser Tier-1 carbon-source experiments.
- `03_organism_mapping.ipynb` maps pathways and enzymes to organisms and applies the catabolic-direction filter.
- `04_enigma_utilizers.ipynb` builds deliverable (a), the ENIGMA isolate utilizer table.
- `05_cooccurrence.ipynb` covers H2: within-block and cross-block co-occurrence and versatility.
- `05b_cooccurrence_effects.ipynb` is review I4, which computes Haldane OR + CI and Jaccard effect sizes from saved counts.
- `06_phylo_maps.ipynb` builds deliverable (b), the GTDB strain placements with certainty.
- `07_environmental_atlas.ipynb` builds the local part of deliverable (c), the SSO field-occurrence atlas.
- `07b_environmental_atlas_global.ipynb` builds the global part of deliverable (c), the NMDC + Planet Microbe abundance atlas.
- `08_synthesis.ipynb` assembles the three deliverables and the gap map into the master table. There a compound counts as callable if it has an isolate call OR measured fitness (review I1).
- `09_deepening.ipynb` covers physicochemistry/bioavailability, chassis specialists and generalists, per-clade conservation, and dark-matter taxonomy. [src: enigma_carbon_census_1]

Generated data files and their row counts:
- `data/census_master_summary.tsv` has 83 rows, one per compound; it is the master census table.
- `data/compound_organism_dark.tsv` has 75 rows listing organism-dark compounds with reasons. It predates review I1: lauric acid was reclassified as callable downstream, leaving 74 dark compounds in the master table.
- `data/cooccurrence_effects.tsv` has 28 rows of H2 effect sizes from review I4, giving Haldane OR + 95% CI and Jaccard per pair.
- `data/environmental_atlas.tsv` has 156 rows for local deliverable (c), giving SSO field genus occurrence.
- `data/env_atlas_global.tsv` has 400 rows for global deliverable (c), giving genus × biome abundance from NMDC and Planet Microbe.
- `data/env_enrichment_soil_fresh.tsv` has 83 rows holding the soil-vs-freshwater abundance contrast, which the report labels exploratory.
- `data/env_outlier_samples.tsv` has 249 rows of label-free top genus×sample abundance spikes. [src: enigma_carbon_census_1]

Report figures:
- `00_class_composition.png` and `00_mw_logp.png` show compound class composition and MW/LogP space.
- `02_linkage_coverage.png` and `02b_linkage_deepened.png` show pathway-linkage coverage by class.
- `03_organism_calls.png` shows organism-mapping call counts.
- `04_utilizer_genera.png` shows the utilizer genera of deliverable (a).
- `05_cooccurrence.png`, `05_genus_versatility.png` and `05_versatility.png` show H2 co-occurrence and versatility.
- `05b_odds_ratio_forest.png` is a forest plot of H2 effect sizes (Haldane OR + 95% CI) by pair class, from review I4.
- `06_phylo_order_map.png` and `06_certainty_composition.png` show the phylogeny and certainty of deliverable (b).
- `07_field_occurrence.png` shows SSO field occurrence in the local atlas.
- `07b_env_atlas_heatmap.png` and `07b_soil_fresh_enrichment.png` show the global biome abundance atlas and the soil/freshwater contrast.
- `08_funnel.png` shows the discovery funnel (83 → callable).
- `09a_physicochem_callable_dark.png` and `09a_bioavailability_space.png` compare callable and dark physicochemistry and map bioavailability space.
- `09b_chassis.png` shows chassis specialists and generalists and capacity breadth.
- `09c_clade_conservation.png` shows per-clade (genus × compound) carrier-fraction conservation.
- `09d_dark_taxonomy.png` shows the dark-matter taxonomy: 74 dark compounds by bucket and source. [src: enigma_carbon_census_1]

## Recommended Next Analyses

The report proposes the following next steps as future directions; their outcomes are not demonstrated in this report:
- **Enrichment of the dark compounds.** The 74 organism-dark compounds are framed as discovery-mode enrichment targets, ranked by why they are dark (NB09 Part 4). The proposal starts with the hardest 29 fully orphan (no-KEGG) compounds, especially the necromass-heavy alkaloids and terpenoids, using anonymous community enrichment plus metagenomics.
- **Literature review first for 6 compounds.** The 6 biosynthesis-known compounds (Tyramine, guanidineacetic acid, cinnamic acid, caffeic acid, palmitic acid and farnesol) should go to a separate MIBiG/biosynthetic-literature consult before any wet-lab effort is committed.
- **Enzyme mining.** Targeted PaperBLAST/PubMed mining for alkaloid and terpenoid catabolic enzymes, searched back into the genomes, could convert some dark compounds to callable without new experiments. The report does not show such a conversion.
- **Better enrichment statistics.** The per-sample rank test should be replaced by a study-aware mixed model, or by a sample-level permutation that respects study structure. This would give defensible enrichment statistics in place of the current exploratory ranking.
- **Periphyton inocula.** The reported Comamonadaceae periphyton reservoir suggests using freshwater-biofilm inocula for the aromatic-utilizer enrichments. This rests on organismal occupancy data, not measured degradation. [src: enigma_carbon_census_1]

## Slots Into

- [[concepts/pangenome-integration]] — the census links pathway and enzyme annotations across 3109 genomes to ENIGMA-isolate utilizer predictions and GTDB strain placements. [src: enigma_carbon_census_1]
- [[concepts/cross-tenant-data-bridging]] — the project bridges PubChem, KEGG, ModelSEED, Fitness Browser, ENIGMA genome-depot, GTDB, SSO, NMDC, and Planet Microbe resources into a tiered compound-to-environment workflow. [src: enigma_carbon_census_1]
- [[concepts/ecotype-environment-gene-content]] — the environmental atlas compares implicated utilizer genera across soil, freshwater, periphyton, sediment, plant, and marine environments while explicitly separating abundance from catabolic activity. [src: enigma_carbon_census_1]
- [[concepts/metabolic-model-gapfilling]] — the 74 organism-dark compounds, including 33 KEGG-linked/no-reaction cases and 29 fully orphan cases, define pathway-linkage and enrichment targets for metabolic knowledge expansion. [src: enigma_carbon_census_1]
- [[concepts/multi-omics-integration]] — the census combines chemical identity, reaction and genome annotations, measured fitness, taxonomy, field occurrence, and metagenomic abundance into a tiered evidence framework. [src: enigma_carbon_census_1]
- [[concepts/organism-dark-compounds]] — 74/83 compounds (89%) were organism-dark, split into KEGG-linked/no-reaction, fully orphan, biosynthesis-known, and generic-reaction buckets. [src: enigma_carbon_census_1]
- [[concepts/genomic-under-representation]] — darkness is resource-darkness rather than biological absence, and callability tracks what KEGG, ModelSEED and genome-depot annotate. [src: enigma_carbon_census_1]
- [[concepts/callability-limited-comparative-inference]] — with only 9 callable compounds, the class-gradient χ² test was underpowered, the source contrast was untestable at n=2, and physicochemical contrasts were directional only. [src: enigma_carbon_census_1]
- [[concepts/homology-search-negative-evidence]] — zero literature rescues came from a shallow PubMed-title screen, which is a method floor rather than evidence of absence. [src: enigma_carbon_census_1]
- [[concepts/pathway-versus-reaction-evidence-resolution]] — Tier-2 pathway and Tier-3 signature calls, generic-reaction-only compounds, and certainty scored as signature reactions carried over required reactions. [src: enigma_carbon_census_1]
- [[concepts/functional-marker-validation]] — the xanthine R02107 nitrogen-versus-carbon mis-scoring, the terephthalic-acid single-reaction-signature artifact, and the biosynthetic-only signatures. [src: enigma_carbon_census_1]
- [[concepts/confirmatory-exploratory-ecological-association-discordance]] — the pre-registered uniform-class null was not rejected, and groundwater and necromass compounds showed no physicochemical separation. [src: enigma_carbon_census_1]
- [[concepts/metabolic-capacity-specialization]] — 675 specialist versus 18 generalist genomes, with versatility read as a Burkholderiales clade trait. [src: enigma_carbon_census_1]
- [[concepts/gene-cooccurrence-ecological-guilds]] — φ hid enrichment that odds ratios surfaced, yet there was no broad cross-module modularity beyond the aromatic funnel. [src: enigma_carbon_census_1]
- [[concepts/occurrence-versus-catabolic-activity]] — the SSO, NMDC and Planet Microbe atlases measure organismal occupancy, not compound degradation. [src: enigma_carbon_census_1]
- [[concepts/adversarial-research-quality-assurance]] — unresolved internal count discrepancies (five versus six aromatic callables; 75 versus 74 dark compounds) and xanthine tables awaiting regeneration. [src: enigma_carbon_census_1]
- [[concepts/computational-pathway-prediction-validation]] — calls depend on a genome-prevalence-<10% catabolic-direction filter, and signature-completeness certainty is not comparable across signature lengths. [src: enigma_carbon_census_1]
- [[concepts/pooled-run-pseudoreplication-and-metadata-label-noise]] — treating non-independent metagenomes as independent drove all 83 genera to q<0.05 in the soil–freshwater contrast. [src: enigma_carbon_census_1]
- [[concepts/study-batch-confounding-of-environmental-associations]] — uncalibrated soil–freshwater significance motivates study-aware mixed models or sample-level permutation. [src: enigma_carbon_census_1]
- [[concepts/taxonomic-resolution-dependent-functional-inference]] — the pangenome↔ENIGMA bridge is genus-level at best, so pangenome Tier-2 reconstructions were not transferred to isolates. [src: enigma_carbon_census_1]
- [[concepts/taxonomic-nomenclature-reconciliation]] — NMDC covstats and Planet Microbe taxonomy names are species-level and need species-to-genus aggregation before any genus-level abundance claim. [src: enigma_carbon_census_1]
- [[concepts/cross-condition-metabolic-comparability]] — Fitness Browser Tier-1 carbon-source experiments were re-matched structurally (name→PubChem→InChIKey) rather than by compound name. [src: enigma_carbon_census_1]
