---
type: Dataset
description: Dataset for assessing metabolic pathway completeness across genomes and
  communities
sources:
- id: annotation_gap_discovery
  resource: ../summaries/annotation_gap_discovery__REPORT.md
  title: annotation gap discovery
- id: cf_formulation_design
  resource: ../summaries/cf_formulation_design__REPORT.md
  title: cf formulation design
- id: clay_confined_subsurface
  resource: ../summaries/clay_confined_subsurface__REPORT.md
  title: clay confined subsurface
- id: discoveries
  resource: ../summaries/discoveries.md
  title: discoveries
- id: essential_metabolome
  resource: ../summaries/essential_metabolome__REPORT.md
  title: essential metabolome
- id: functional_dark_matter
  resource: ../summaries/functional_dark_matter__REPORT.md
  title: functional dark matter
- id: fw300_metabolic_consistency
  resource: ../summaries/fw300_metabolic_consistency__REPORT.md
  title: fw300 metabolic consistency
- id: genotype_to_phenotype_enigma
  resource: ../summaries/genotype_to_phenotype_enigma__REPORT.md
  title: genotype to phenotype enigma
- id: metabolic_capability_dependency
  resource: ../summaries/metabolic_capability_dependency__REPORT.md
  title: metabolic capability dependency
- id: nmdc_community_metabolic_ecology
  resource: ../summaries/nmdc_community_metabolic_ecology__REPORT.md
  title: nmdc community metabolic ecology
- id: pathway_capability_dependency
  resource: ../summaries/pathway_capability_dependency__REPORT.md
  title: pathway capability dependency
- id: pgp_pangenome_ecology
  resource: ../summaries/pgp_pangenome_ecology__REPORT.md
  title: pgp pangenome ecology
- id: pitfalls
  resource: ../summaries/pitfalls.md
  title: pitfalls
- id: plant_microbiome_ecotypes
  resource: ../summaries/plant_microbiome_ecotypes__REPORT.md
  title: plant microbiome ecotypes
- id: pseudomonas_carbon_ecology
  resource: ../summaries/pseudomonas_carbon_ecology__REPORT.md
  title: pseudomonas carbon ecology
- id: webofmicrobes_explorer
  resource: ../summaries/webofmicrobes_explorer__REPORT.md
  title: webofmicrobes explorer
title: GapMind
---
# GapMind

## Identity

**Canonical name:** GapMind. [^annotation_gap_discovery]

**Known aliases:** GapMind pathway-completeness resource; GapMind pathway analysis. [^annotation_gap_discovery]

**Stable external identifier:** No stable external identifier was reported in the source documents. [^annotation_gap_discovery]

GapMind is a pathway-completeness resource for assessing whether metabolic pathways are present or incomplete in genome annotations. [^annotation_gap_discovery]

## Annotation-gap discovery and pathway interpretation

The [annotation-gap discovery study](../summaries/annotation_gap_discovery__REPORT.md) integrated GapMind with [ModelSEED](modelseed.md) metabolic-model gapfilling, Fitness Browser phenotypes, pangenome annotations, and BLAST homology across 14 organisms and 18 carbon sources, recording 104 GapMind-gapfill pathway pairings. [^annotation_gap_discovery] GapMind commonly identified incomplete pathways with `not_present` or `steps_missing` where ModelSEED required gapfilling, but exact concordance was limited because BERDL represented results as pathway-level step counts rather than individual step identities. [^annotation_gap_discovery]

The [functional dark matter study](../summaries/functional_dark_matter__REPORT.md) **supports** GapMind as a scalable source of pathway hypotheses: it identified 1,256 organism–pathway pairs across 44 Fitness Browser-linked species where nearly complete `steps_missing_low` pathways co-occurred with strongly fitness-active dark genes. [^functional_dark_matter] The most frequent gaps were fucose utilization in 32 organisms, rhamnose utilization in 31, sorbitol utilization in 30, myoinositol utilization in 28, gluconate utilization in 26, and asparagine biosynthesis in 24. [^functional_dark_matter] It **refines** interpretation because these are organism-level co-occurrences, not direct gene–enzyme assignments: domain matching produced 42,239 gene–pathway candidates across 3,186 unique dark genes, including 5,398 high-confidence EC-prefix matches, 4,687 medium-confidence Pfam-family matches, and 32,154 low-confidence keyword matches; assignments require EC matching, structure prediction, enzymology, or other validation. [^functional_dark_matter]

## Community-scale integration

The [NMDC community metabolic ecology study](../summaries/nmdc_community_metabolic_ecology__REPORT.md) **extends** GapMind to community-weighted pathway potential using 305M records covering 27,690 GTDB species, NMDC taxonomy, and metabolomics across 220 samples and 80 pathways. [^nmdc_community_metabolic_ecology] The matrix contained 18 amino-acid and 62 carbon-utilization pathways; mean taxonomy-bridge coverage was 94.6%, all 220 samples passed the 30% quality-control threshold, and 92% mapped at least 85% of community abundance to GTDB pangenome species. [^nmdc_community_metabolic_ecology]

This study **supports** GapMind completeness as a community-scale ecological predictor while **refining** pathway-presence interpretation: among 13 testable amino-acid pathways, 11 (85%) negatively correlated with ambient amino-acid intensity, including leucine r = −0.390, q = 0.022, n = 62, and arginine r = −0.297, q = 0.049, n = 80. [^nmdc_community_metabolic_ecology] These were weak support for community-scale Black Queen Hypothesis dynamics, not evidence of pathway expression or activity. [^nmdc_community_metabolic_ecology] PCA of the 220-sample × 80-pathway matrix explained 49.4% of variance in PC1 and 16.6% in PC2; Soil and Freshwater differed in PC1 (Mann-Whitney U = 3,674, p < 0.0001; median PC1 values +3.86 and −6.28), and 17 of 18 amino-acid pathways differed by ecosystem after Benjamini-Hochberg correction. [^nmdc_community_metabolic_ecology]

These findings **refine** comparative claims because 33 Freshwater samples lacked paired metabolomics, abiotic measurements were unavailable, and GapMind measures genomic potential rather than activity. [^nmdc_community_metabolic_ecology] The analysis used binary `frac_complete` (score 5) and `frac_likely_complete` (score at least 4); approximately 1,352 Centrifuge taxa matched multiple GTDB clades, representing approximately 6.5% of mapped abundance, with alphabetical tiebreaking. [^nmdc_community_metabolic_ecology] String matching caused an isoleucine/leucine collision that was corrected; KEGG compound IDs had a 2% annotation rate; cysteine, histidine, and lysine remained untestable; chorismate used upstream shikimic acid and 3-dehydroshikimic acid proxies; the H1 dataset contained 131 samples, 125/131 (95%) from one NMDC study, and the full merged matrix contained 174 samples. [^nmdc_community_metabolic_ecology]

## Comparative and fitness validation

The [discoveries log](../summaries/discoveries.md) and [metabolic capability versus dependency study](../summaries/pathway_capability_dependency__REPORT.md) **support** comparative pathway-capability screening. Across 7 Fitness Browser organisms and 23 GapMind pathways, 35.4% of 161 pairs were Active Dependency, 41.0% Latent Capability, 14.9% Incomplete but Important, and 8.7% Missing. [^discoveries] [^pathway_capability_dependency] All 66 Latent Capability pairs became fitness-important under at least one condition, especially nitrogen limitation, stress, and carbon limitation. [^pathway_capability_dependency] Active Dependency required a complete pathway containing fitness-important genes; Latent Capability required completeness without standard-condition defects; Incomplete but Important contained important mapped genes despite incompleteness; Missing was neither complete nor important. [^pathway_capability_dependency] The composite importance score weighted essentiality at 40%, fitness breadth at 30%, and fitness magnitude at 30%. [^pathway_capability_dependency]

This result **refines** the discoveries interpretation because condition-specific median thresholds can cause reclassification by construction and require independent calibration. [^pathway_capability_dependency] Fitness Browser genes were mapped through besthitkegg-to-keggmember-to-EC-to-KEGG-map-to-GapMind; only 7 of 48 Fitness Browser organisms matched GapMind data: *Desulfovibrio vulgaris* Hildenborough, *Shewanella oneidensis* MR-1, *Pseudomonas putida* KT2440, *Pseudomonas stutzeri* RCH2, *Caulobacter crescentus*, *Sinorhizobium meliloti*, and *Azospirillum brasilense*. [^pathway_capability_dependency] Their Active Dependencies had mean core completeness 0.986 versus 0.975 for Latent Capabilities. [^pathway_capability_dependency]

The earlier [metabolic capability versus dependency study](../summaries/metabolic_capability_dependency__REPORT.md) **refines** this comparison: among 1,695 complete pathway-organism pairs from 48 organisms, 267 (15.8%) were latent, 547 (32.3%) intermediate, and 881 (51.9%) active; pathway category predicted class (χ²=163.6, df=4, p=2.5×10⁻³⁴). [^metabolic_capability_dependency] Carbon pathways were latent in 217/892 cases (24.3%) versus 48/735 amino-acid cases (6.5%); the latent fraction varied from 4.7% to 21.1% across threshold combinations. [^metabolic_capability_dependency] Pathway conservation did not distinguish latent from active classes (active mean 0.829, intermediate 0.907, latent 0.869; active-versus-latent Mann–Whitney U p = 0.94, rank-biserial r = 0.052), while latent-capability rate correlated with pangenome openness (Spearman ρ = 0.69, p = 0.0004, n = 22 clades). [^metabolic_capability_dependency]

The same work **refines** broad concordance claims: in FW300-N2E3, all 13 Web of Microbes metabolites mapped to GapMind had complete pathways and Fitness Browser growth, but the 94% four-database concordance was structurally driven because Fitness Browser was 21/21, GapMind 13/13, and BacDive 3/7. [^discoveries] The [FW300-N2E3 study](../summaries/fw300_metabolic_consistency__REPORT.md) supports this 13/13 result but notes that only 13/58 metabolites mapped to GapMind and comparisons covered 21/58; Fitness Browser used minimal medium, whereas Web of Microbes used R2A rich medium, and gene-to-step mapping was deferred. [^fw300_metabolic_consistency]

The [Web of Microbes data-explorer study](../summaries/webofmicrobes_explorer__REPORT.md) **refines** this bridge by showing that GapMind pathway matching was blocked when pathway names used internal identifiers rather than simple metabolite names; a pathway-to-substrate/product lookup table is required. [^webofmicrobes_explorer] The same study reports that 19 Web of Microbes-produced metabolites for `pseudo3_N2E3` matched Fitness Browser carbon or nitrogen-source experiments, but it does not establish that the corresponding GapMind pathways are complete or that production predicts fitness. [^webofmicrobes_explorer] The Web of Microbes snapshot contains 37 organisms and 589 metabolites, so its proposed GapMind integration is a small, future analysis rather than a validated community-scale result. [^webofmicrobes_explorer]

The essential-metabolome pilot **supports** comparative use: 17 of 18 amino-acid biosynthesis pathways were complete in all 7 successfully mapped organisms and serine was complete in 6 of 7, but the *Desulfovibrio vulgaris* serine gap is a computational hypothesis requiring growth testing on serine-free medium. [^essential_metabolome] The [ENIGMA genotype-to-phenotype study](../summaries/genotype_to_phenotype_enigma__REPORT.md) **refines** performance expectations: GapMind achieved AUC 0.646, 78.8% accuracy, and 24.3% coverage on 118 genome–condition pairs, with 96.5% recall and 79% precision; approximately 76% of conditions lacked GapMind or Carbon Source Phenotypes training data, and prediction there fell to approximately AUC 0.63. [^genotype_to_phenotype_enigma]

## Pangenome, ecology, and Pseudomonas integration

The [Pseudomonas carbon ecology study](../summaries/pseudomonas_carbon_ecology__REPORT.md) **extends** GapMind to a 12,732-genome, 433-species-clade analysis using 62 carbon pathways. [^pseudomonas_carbon_ecology] It found strong pathway loss in *Pseudomonas* s.s. relative to *Pseudomonas_E*: among 7 versus 189 species, 43/62 pathways differed at q < 0.05, with xylose completeness 0.0% versus 74.4%, ribose 27.9% versus 92.0%, arabinose 0.0% versus 62.6%, and myo-inositol 0.0% versus 58.8%. [^pseudomonas_carbon_ecology] Core amino-acid and organic-acid pathways remained near-universal (>99%) in both groups, while rhamnose and fucose were more complete in *P. aeruginosa* (66.8%) than in the *P. fluorescens* group (41.3% and 45.1%), without significant FDR-adjusted differences. [^pseudomonas_carbon_ecology]

The study **supports** the hypothesis that host-associated clades lose plant-derived sugar pathways but **refines** ecological prediction: among 54 free-living or plant-associated species, pathway profiles associated with environment (999-permutation p = 0.006; between-group mean distance 2.054 versus within-group 1.890), yet a Random Forest achieved balanced accuracy 0.408 +/- 0.169 versus a 0.250 chance baseline. [^pseudomonas_carbon_ecology] The dominant PCA separation was subgenus, not lifestyle; the first 5 components explained 74.9% of variance. [^pseudomonas_carbon_ecology] This supports using GapMind for ecological signal detection but indicates that carbon profiles alone are insufficient for fine-grained environment classification. [^pseudomonas_carbon_ecology]

The study **refines** broader pangenome interpretations by showing that pathway variation can reflect deep phylogenetic structure: *Pseudomonas* s.s. contained 19 species and 6,905 genomes, *Pseudomonas_E* 398 species and 5,687 genomes, and *P. aeruginosa* comprised 6,760/12,732 genomes (53%). [^pseudomonas_carbon_ecology] It recommends aromatic-pathway modules, PGLS (phylogenetic generalized least squares), phylogenetic logistic regression, genome-level prediction, within-species ecotype analysis, and validation against RB-TnSeq fitness data. [^pseudomonas_carbon_ecology]

The [plant microbiome ecotypes study](../summaries/plant_microbiome_ecotypes__REPORT.md) **extends** GapMind across 293,059 genomes, 1,136 plant-associated species, and 7,995 plant-associated genomes using 80 pathways; agreement with BacDive was 83.1%, but the core-level completeness score was 0% across compartments and may be too stringent. [^plant_microbiome_ecotypes] Corrected compartment separation was pseudo-F = 23.2, p = 0.001, R² = 0.071, with db-RDA location-only R² = 0.060; complementarity was weak or negative (Cohen’s d = −0.39), and 62/322 genera (19.3%) were lost in the NMDC bridge. [^plant_microbiome_ecotypes]

The [PGP pangenome ecology study](../summaries/pgp_pangenome_ecology__REPORT.md) **extends** GapMind to 27,690 species and 291,279 genomes: complete tryptophan pathways were associated with ipdC in 2.5% versus 0.9% of incomplete-pathway species (Fisher OR = 2.81, p = 6.3e-10; logistic OR = 2.81, 95% CI 1.97–4.01, p = 1.4e-08, n = 11,272), while tyrosine gave OR = 3.62, p = 2.3e-11. [^pgp_pangenome_ecology] The association reversed in 1,039 soil/rhizosphere species (OR = 0.30, p = 0.02) and remained positive in 10,233 non-soil species (OR = 3.56, p = 7.7e-13); because ipdC occurred in 214 species (1.9%), the soil result is hypothesis-generating. [^pgp_pangenome_ecology]

The [pathway capability study](../summaries/pathway_capability_dependency__REPORT.md) further **supports** a relationship between pathway variation and genome fluidity: across 2,810 GTDB species and approximately 293,000 genomes, variable pathway count correlated with pangenome openness (raw rho=0.327, p=7.2e-71; partial rho=0.530, p=2.83e-203), with significant within-genus results for Clostridium, Eubacterium, Mesorhizobium, Pseudomonas, and Streptomyces. [^pathway_capability_dependency] All-gene versus core-only completeness showed accessory contributions: leucine and valine 0.614 versus 0.468 (gap 0.146), arginine 0.613 versus 0.472 (0.141), lysine 0.804 versus 0.664 (0.140), and threonine 0.803 versus 0.663 (0.140). [^pathway_capability_dependency] This contrasts with the PGP study, where PGP-marker richness negatively correlated with openness (ρ = −0.195, p = 2.0e-97, n = 11,272). [^pgp_pangenome_ecology]

The Web of Microbes study **supports** the feasibility of extending this pangenome comparison to exometabolite novelty: all WoM genera had pangenome species clades, including *Bacillus* with 5 species and 2,557 genomes, *Rhizobium* with 5 and 449, *Pseudomonas fluorescens* with 5 and 139, *Synechococcus* with 5 and 88, *Phenylobacterium* with 5 and 80, *Acidovorax* with 5 and 79, *Zymomonas mobilis* with 1 and 26, and *Escherichia coli* with 1 and 2. [^webofmicrobes_explorer] It proposes testing whether the fraction of de novo products, `E/(E+I)`, associates with open pangenomes or accessory genes, but this relationship remains untested. [^webofmicrobes_explorer] Species-level matching requires strain-to-genome mapping, which the project did not attempt. [^webofmicrobes_explorer]

## Formulation, cultured cohorts, and scope

The formulation-design study **supports** comparative use across 499 commensal genomes: complete conservation exceeded 95% for 18/18 amino-acid and 39/39 carbon pathways in *Micrococcus luteus*, 18/18 and 32/35 in *Streptococcus salivarius*, 14/18 and 39/41 in *Rothia dentocariosa*, 16/16 and 27/27 in *Neisseria mucosa*, and 7/18 and 37/39 in *Gemella sanguinis*. [^cf_formulation_design] In 1,796 lung or respiratory *Pseudomonas aeruginosa* genomes, amino-acid catabolic pathways were 97.4% conserved and proline utilization complete in 97%, whereas myoinositol, xylitol, xylose, and arabinose were 0% complete and fucose and rhamnose 1%; six pathways were present in at least one core commensal but absent or nearly absent in PA14. [^cf_formulation_design]

The [clay-confined subsurface study](../summaries/clay_confined_subsurface__REPORT.md) **refines** high-completeness interpretation: deep cultured genomes averaged 16.22/18 versus 16.66/18 unfiltered (p = 0.153, d = −0.17) and 15.50/18 versus 17.14/18 filtered (p = 0.009, d = −0.84); shallow genomes were 17.87/18 versus 16.66/18 unfiltered (p = 0.006, d = +0.52) and 17.87/18 versus 17.14/18 filtered (p = 0.029, d = +0.43). [^clay_confined_subsurface] The 18-pathway metric saturates, so finer EC-level analysis was recommended. [^clay_confined_subsurface]

GapMind covers approximately 80 carbon and amino-acid pathways, not cofactor, lipid, or secondary metabolism, and is therefore one evidence stream within [metabolic-model gapfilling](../concepts/metabolic-model-gapfilling.md) and [evidence integration](../concepts/multi-omics-integration.md). [^annotation_gap_discovery] [^pathway_capability_dependency] The metabolic-capability study excluded deoxyribonate and myoinositol without matching SEED roles, required `phe` and `tyr` abbreviation matching, excluded alanine below 3 SEED genes, and warned that SEED proxies can create false positives. [^metabolic_capability_dependency] GapMind does not establish growth kinetics, regulatory state, enzyme activity, expression, metabolite exchange, gene essentiality, or strain-level performance. [^genotype_to_phenotype_enigma] [^essential_metabolome] [^plant_microbiome_ecotypes]

The Web of Microbes snapshot **refines** the scope of cross-collection integration: its 2018 archive contains 37 organisms across 5 ENIGMA-funded projects and 589 metabolites, of which 332 (56.4%) are unidentified; the project found 69 of 257 identified compounds (26.8%) with definitive ModelSEED links, 107 (41.6%) with formula-only links, 176 (68.5%) with any link, and 81 (31.5%) unmatched. [^webofmicrobes_explorer] Formula-only matching expanded 107 WoM compounds to 900 ModelSEED molecules, so the resulting candidate sets are not definitive pathway or substrate identifications. [^webofmicrobes_explorer]

## Reproducibility and provenance safeguards

The [BERDL pitfalls reference](../summaries/pitfalls.md) **refines** all comparisons: multiple records can exist per genome–pathway pair, with `complete`, `likely_complete`, `steps_missing_low`, `steps_missing_medium`, and `not_present`; the best score must be selected before aggregation. [^pitfalls] For `sequence_scope = 'core'`, `score_simplified` is binary (0.0 or 1.0) and should use `MAX(score_simplified)` at species level; metabolic categories are `aa` and `carbon`, not `amino_acid`. [^pitfalls]

Taxonomy joins must use `genome_id`, not `gtdb_taxonomy_id`; `clade_name` contains the full `gtdb_species_clade_id`, including representative accession. [^pitfalls] Missing joins, orphan records, schema changes, and incorrect identifiers can create apparent absence without biological absence. [^pitfalls] Records should be queried through live catalog and schema discovery; prefer `catalog.namespace.table` during Delta-to-Iceberg migration, cast string and `DECIMAL` fields explicitly, and use shared representations such as COG, KEGG orthologs, or Pfam when comparing gene clusters across species. [^pitfalls]

These identifier and provenance safeguards **also apply** to Web of Microbes integration: exact name matches were treated as high-confidence 1:1 ModelSEED mappings, whereas formula-only matches were treated as low-confidence candidate sets requiring manual curation. [^webofmicrobes_explorer] The archived 2018 snapshot was accessed through the Wayback Machine; current GNPS2 or Northen laboratory datasets may differ and may contain consumption data absent from this export. [^webofmicrobes_explorer]

Coverage limitations remain substantial: the essential-metabolome collection contained 305M predictions across 293K genomes, but only 7/45 essential-gene organisms mapped and *Escherichia coli* K-12 had 0 relevant predictions. [^essential_metabolome] The plant study found only 7,995/293,059 genomes (2.7%) with plant-associated annotations and 11.7% Jaccard overlap between 487 pangenome-derived plant genera and 438 MGnify rhizosphere genera. [^plant_microbiome_ecotypes] Its original compartment result fell from R² = 0.527 to 0.072 after removing three genome-rich species per compartment, an 86% loss. [^plant_microbiome_ecotypes]

The formulation, clay, PGP, NMDC, and Web of Microbes studies therefore **support** GapMind as a comparative screening resource while **refining** claims of biological sufficiency: predictions require experimental validation, taxonomy and score definitions must be reported, missing records must not be interpreted as missing pathways, and metabolite-to-pathway links require curated compound-name and strain mappings. [^cf_formulation_design] [^clay_confined_subsurface] [^pgp_pangenome_ecology] [^pitfalls] [^webofmicrobes_explorer]

## Related pages

- [metabolic-model-gapfilling](../concepts/metabolic-model-gapfilling.md)
- [multi-omics-integration](../concepts/multi-omics-integration.md)
- [condition-specific-fitness](../concepts/condition-specific-fitness.md)
- [pangenome-integration](../concepts/pangenome-integration.md)
- [gene-essentiality](../concepts/gene-essentiality.md)
- [gene-function-acquisition-depth](../concepts/gene-function-acquisition-depth.md)
- [modelseed](modelseed.md)
- [kbase-ke-pangenome](kbase-ke-pangenome.md)
- [gtdb](gtdb.md)
- [annotation_gap_discovery__REPORT](../summaries/annotation_gap_discovery__REPORT.md)
- [functional_dark_matter__REPORT](../summaries/functional_dark_matter__REPORT.md)
- [cf_formulation_design__REPORT](../summaries/cf_formulation_design__REPORT.md)
- [clay_confined_subsurface__REPORT](../summaries/clay_confined_subsurface__REPORT.md)
- [essential_metabolome__REPORT](../summaries/essential_metabolome__REPORT.md)
- [discoveries](../summaries/discoveries.md)
- [fw300_metabolic_consistency__REPORT](../summaries/fw300_metabolic_consistency__REPORT.md)
- [genotype_to_phenotype_enigma__REPORT](../summaries/genotype_to_phenotype_enigma__REPORT.md)
- [metabolic_capability_dependency__REPORT](../summaries/metabolic_capability_dependency__REPORT.md)
- [nmdc_community_metabolic_ecology__REPORT](../summaries/nmdc_community_metabolic_ecology__REPORT.md)
- [pathway_capability_dependency__REPORT](../summaries/pathway_capability_dependency__REPORT.md)
- [pgp_pangenome_ecology__REPORT](../summaries/pgp_pangenome_ecology__REPORT.md)
- [plant_microbiome_ecotypes__REPORT](../summaries/plant_microbiome_ecotypes__REPORT.md)
- [pitfalls](../summaries/pitfalls.md)
- [pseudomonas_carbon_ecology__REPORT](../summaries/pseudomonas_carbon_ecology__REPORT.md)
- [webofmicrobes_explorer__REPORT](../summaries/webofmicrobes_explorer__REPORT.md)

[^annotation_gap_discovery]: [annotation gap discovery](../summaries/annotation_gap_discovery__REPORT.md)
[^functional_dark_matter]: [functional dark matter](../summaries/functional_dark_matter__REPORT.md)
[^nmdc_community_metabolic_ecology]: [nmdc community metabolic ecology](../summaries/nmdc_community_metabolic_ecology__REPORT.md)
[^discoveries]: [discoveries](../summaries/discoveries.md)
[^pathway_capability_dependency]: [pathway capability dependency](../summaries/pathway_capability_dependency__REPORT.md)
[^metabolic_capability_dependency]: [metabolic capability dependency](../summaries/metabolic_capability_dependency__REPORT.md)
[^fw300_metabolic_consistency]: [fw300 metabolic consistency](../summaries/fw300_metabolic_consistency__REPORT.md)
[^webofmicrobes_explorer]: [webofmicrobes explorer](../summaries/webofmicrobes_explorer__REPORT.md)
[^essential_metabolome]: [essential metabolome](../summaries/essential_metabolome__REPORT.md)
[^genotype_to_phenotype_enigma]: [genotype to phenotype enigma](../summaries/genotype_to_phenotype_enigma__REPORT.md)
[^pseudomonas_carbon_ecology]: [pseudomonas carbon ecology](../summaries/pseudomonas_carbon_ecology__REPORT.md)
[^plant_microbiome_ecotypes]: [plant microbiome ecotypes](../summaries/plant_microbiome_ecotypes__REPORT.md)
[^pgp_pangenome_ecology]: [pgp pangenome ecology](../summaries/pgp_pangenome_ecology__REPORT.md)
[^cf_formulation_design]: [cf formulation design](../summaries/cf_formulation_design__REPORT.md)
[^clay_confined_subsurface]: [clay confined subsurface](../summaries/clay_confined_subsurface__REPORT.md)
[^pitfalls]: [pitfalls](../summaries/pitfalls.md)
