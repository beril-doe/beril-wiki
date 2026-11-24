---
type: "Dataset"
description: "Strain database whose environment categories were approximated by a rule-based classifier for comparing AMR burden."
sources: ["summaries/amr_strain_variation__REPORT.md", "summaries/bacdive_metal_validation__REPORT.md", "summaries/bacdive_phenotype_metal_tolerance__REPORT.md", "summaries/bacillota_b_subsurface_accessory__REPORT.md", "summaries/berdl_data_atlas__REPORT.md", "summaries/comprehensive_metal_ecology__REPORT.md", "summaries/discoveries.md", "summaries/fw300_metabolic_consistency__REPORT.md", "summaries/gene_function_ecological_agora__REPORT.md", "summaries/lanthanide_methylotrophy_atlas__REPORT.md", "summaries/metal_cross_resistance__REPORT.md", "summaries/pitfalls.md", "summaries/plant_microbiome_ecotypes__REPORT.md"]
aliases: ["BacDive metabolite_utilization", "Bacterial Diversity Metadatabase", "kescience_bacdive"]
---
# BacDive

BacDive (Bacterial Diversity Metadatabase; KBase Data Lakehouse collection kescience_bacdive) is a strain database. In the amr_strain_variation report, a rule-based classifier approximated its environment categories so that antimicrobial-resistance burden could be compared across environments. The evidence below comes from many projects and covers specific matching, coverage and validation analyses, plus table-handling pitfalls. [[entities/kbase-data-lakehouse]] hosts it. [src: berdl_data_atlas]

## Key facts

- The KBase Data Lakehouse inventory lists 97,334 BacDive strain phenotype profiles. [src: berdl_data_atlas]
- The strain table supplies 97K curated strain phenotype profiles. [src: berdl_data_atlas]
- For curated phenotype work, one report recommends kescience_bacdive for organismal traits and kescience_webofmicrobes for carbon utilization, joined via ncbi_taxon_id. [src: berdl_data_atlas]
- Tables used across projects include strain, physiology, metabolite_utilization, enzyme, isolation, taxonomy and sequence_info. [src: bacdive_phenotype_metal_tolerance]
- Another project used metabolite_utilization, strain and taxonomy for species-level metabolite utilization. [src: fw300_metabolic_consistency]
- P4-D1 phenotype anchoring used the sequence_info, strain, metabolite_utilization, physiology and enzyme tables, with 32% species coverage via GCF→GCA fallback. [src: gene_function_ecological_agora]
- The metal_cross_resistance report used the strain and isolation tables for isolation environment validation metadata. [src: metal_cross_resistance]
- The plant microbiome report used the isolation, sequence_info and metabolite_utilization tables for strain-level isolation source and metabolic phenotypes. [src: plant_microbiome_ecotypes]

## Table semantics and join pitfalls

The metabolite_utilization.utilization field has four values: + for utilization, - for no utilization, produced for production, and +/- for variable or ambiguous results. [src: pitfalls] Treating it as binary inflates counts: for P. fluorescens, indole has 60 produced entries and only 1 actual utilization test. [src: pitfalls] Computing species-level percentages from raw counts without excluding produced and +/- entries gives incorrect rates. [src: pitfalls] The recommended method divides positive tests by the sum of explicit positive and negative tests. [src: pitfalls] The report also recommends tracking positive, negative, produced and ambiguous categories separately. [src: pitfalls]

Other handling issues:

- In plant_microbiome_ecotypes, sequence_info.bacdive_id is INT but isolation.bacdive_id is STRING. [src: pitfalls] A direct join returns zero rows because Spark does not implicitly cast across INT/STRING. [src: pitfalls] The fix is to cast sequence_info.bacdive_id to STRING. [src: pitfalls]
- Taxonomy columns are named tax_class and tax_order to avoid SQL (structured query language) reserved words. [src: pitfalls]
- sequence_info.accession uses GCA_*, while pangenome genome_id uses GB_GCA_* or RS_GCF_*, so joins need prefix matching or stripping. [src: pitfalls]
- Linking by NCBI taxid to the Fitness Browser is species-level, not strain-level, which gives many-to-one ambiguity. [src: pitfalls]
- Physiology fields are sparse (Gram stain ~15K/97K, oxygen ~23K/97K), so IS NOT NULL filters are usually required. [src: pitfalls]
- The metabolite test panel is biased toward trehalose, arginine and glucose, so frequency-based ranking is misleading. [src: pitfalls]

## Linking BacDive to pangenomes

Species-name matching links under half of BacDive strains to GTDB species, and the reports give slightly different counts. [src: bacdive_metal_validation, bacdive_phenotype_metal_tolerance]

- The bacdive_metal_validation report linked 42,227 strains (43.4% of 97,334) to metal tolerance scores across 6,426 unique GTDB species. [src: bacdive_metal_validation] The discoveries digest repeats this, and says the match uses exact names plus GTDB suffix removal. [src: discoveries]
- The pitfalls digest breaks this down: direct species-name matching captures 34.5% of strains, and base-name matching (stripping GTDB suffixes) adds another 8.9% for 43.4% total. [src: pitfalls] It says the unmatched 56.6% are different species concepts or genera absent from GTDB r214. [src: pitfalls]
- Of the linked strains, 25,089 have isolation source metadata. [src: bacdive_metal_validation]
- The bacdive_phenotype_metal_tolerance report matched 37,368 strains (38.4%) to pangenome and metal score, across 5,647 unique GTDB species, from a bridge of 97,334 strains. [src: bacdive_phenotype_metal_tolerance] Its bridge file has 97,334 rows and its matched-strain file has 37,368 rows. [src: bacdive_phenotype_metal_tolerance] The current bridge uses species name matching (38.4%). [src: bacdive_phenotype_metal_tolerance]
- The two reports give different matched counts and species counts. I do not reconcile them here. [src: bacdive_metal_validation, bacdive_phenotype_metal_tolerance]
- The discoveries digest attributes the 56.6% unmatched strains to GTDB species boundaries that differ from LPSN/DSMZ taxonomy. [src: discoveries]
- The bridge allows cross-referencing BacDive phenotypes with pangenome predictions without Spark queries. [src: discoveries]
- Phenotype coverage through a GCF→GCA fallback is 32%. [src: discoveries] The P4-D1 audit of 18,989 species found 32% (6,066 species) covered, and all matched species had metabolite, physiology and enzyme rows. [src: gene_function_ecological_agora]
- For the atlas, 6,066 species representatives with BacDive matches were tabulated per focal clade. [src: gene_function_ecological_agora] BacDive anchors cover 32% of atlas species. [src: gene_function_ecological_agora]
- Coverage can be too thin for some clades. Cyanobacteriia had only n=4 species, so phenotype anchoring was not feasible. [src: gene_function_ecological_agora] The Mycobacteriaceae set had n=318 BacDive species. [src: gene_function_ecological_agora]
- In the Bacillota_B subsurface work, BacDive expansion added zero Bacillota_B in that run. The 10-genome deep-clay anchor came almost entirely from ncbi_env keyword search. [src: bacillota_b_subsurface_accessory]
- In amr_strain_variation, the BacDive-approximating classifier assigned environments to 35% of species (459/1,307). [src: amr_strain_variation] The bridge table behind this has 1,307 rows. [src: amr_strain_variation] Both this and the NCBI keyword classifier are approximate, and the report says dedicated metadata curation would improve ecotype analyses. [src: amr_strain_variation]
- In metal_cross_resistance, BacDive matching used genus+species substring search. This is imprecise for genus-only identifications such as Acidovorax sp., so the fuzzy matches should be treated with caution. [src: metal_cross_resistance]

## Plant-association cross-validation

BacDive isolation records identified 2,482 plant strains but yielded 0 new upgrades in the plant-association census. [src: plant_microbiome_ecotypes] The report reads this as complete overlap with ncbi_env metadata for the plant-associated genome set. [src: plant_microbiome_ecotypes] Separately, BacDive metabolite utilization cross-validated GapMind predictions at 83.1% consistency, which the report interprets as confirming that pathway completeness scores are reliable. [src: plant_microbiome_ecotypes]

## Metal tolerance validation

The tests below use different populations and methods, so each is stated on its own. [src: discoveries, metal_cross_resistance]

- Bacteria isolated from heavy metal contamination sites had metal tolerance scores above the environmental baseline (Cohen's d = +1.00, Mann-Whitney p=0.006, n=10). [src: discoveries] The effect is dose-dependent: heavy metal (+1.00) > waste/sludge (+0.57) > all contamination (+0.43) > industrial (+0.20). [src: discoveries]
- Host-associated isolates (n=12,086) had median score 0.194, mean 0.201, median delta +0.007, Cohen's d +0.14, p<0.0001. [src: bacdive_metal_validation] The digest notes this contradicts the expectation that host niches have lower metal exposure. [src: discoveries]
- In metal_cross_resistance, multi-metal tolerance scores did not correlate with BacDive isolation from metal environments at the Fitness Browser species scale (Spearman rho ~ -0.02, p > 0.8). [src: metal_cross_resistance] That validation set excluded 2 organisms without tier classification data (azobra and BFirm, with <3 metals). [src: metal_cross_resistance] It collapsed multiple Fitness Browser strains of a species into one entry, including 5 P. fluorescens strains sharing the same BacDive pool. [src: metal_cross_resistance] The effective sample size was 20 independent species, which the report considers far too small for a meaningful correlation test. [src: metal_cross_resistance]
- The report calls its phenotype test the first large-scale test of BacDive phenotypes as metal tolerance predictors (5,647 species, 10 phenotype features). [src: bacdive_phenotype_metal_tolerance] It tested 10 features (8 binary, 2 continuous). [src: bacdive_phenotype_metal_tolerance]
- Classical phenotypes capture metal tolerance signal (R²=0.16 alone, 7/10 significant after FDR, false discovery rate). [src: discoveries] They are entirely phylogenetically confounded. Adding them to a taxonomy-based model gave no improvement (delta R²=-0.009). [src: discoveries] The report names genome metal-resistance gene count as the true predictor (full model R²=0.63). [src: discoveries]
- Only 24 BacDive metal utilization test records (iron, manganese, arsenate, chromate, cobalt, zinc) matched strains with metal tolerance scores. [src: bacdive_metal_validation]
- Lanthanide/methanol coverage is absent from metabolite_utilization. [src: lanthanide_methylotrophy_atlas]

## Pseudomonas fluorescens utilization

- In BacDive, 0/52 P. fluorescens strains could use tryptophan as a carbon source, even though FW300-N2E3 produces it and has a complete biosynthesis pathway. [src: discoveries]
- The FW300-N2E3 comparison matched 8/58 (14%) Web of Microbes metabolites to BacDive utilization data. [src: fw300_metabolic_consistency] BacDive was the only variable part of cross-database concordance, with 3/7 = 43% of matched metabolites utilized. [src: fw300_metabolic_consistency]
- Counts use per-strain consensus, a majority vote among duplicate records per strain. [src: fw300_metabolic_consistency] The summary file has 83 rows. [src: fw300_metabolic_consistency]
- BacDive aggregates P. fluorescens strains across a broad clade, Pseudomonas_E fluorescens_E, under GTDB reclassification. [src: fw300_metabolic_consistency]
- Compound coverage varies from 1 to 51 strains. Raw records can be higher because of duplicate entries per strain. [src: fw300_metabolic_consistency]

## Caveats

- BacDive represents culturable, described strains, so metal-tolerant extremophiles may be under-represented. [src: bacdive_metal_validation]
- Testing is biased toward well-studied organisms such as Pseudomonas and E. coli. Poorly studied species have sparse data. [src: bacdive_phenotype_metal_tolerance]
- The API (application programming interface) may hold extra metal tolerance data, such as MIC data and growth inhibition, that the metabolite_utilization table lacks. [src: bacdive_metal_validation]
- The BacDive niche-breadth analysis (NB09, using isolation, strain and taxonomy tables) is pending. [src: comprehensive_metal_ecology] Its PGLS (phylogenetic generalized least squares) schema is confirmed but the main analysis is pending. [src: comprehensive_metal_ecology] Schema discovery is complete, but the country-count aggregation and PGLS have not run. [src: comprehensive_metal_ecology]
- The report proposes BacDive culture-based cosmopolitanism as a fully independent, non-16S-derived niche-breadth replication. [src: comprehensive_metal_ecology]
