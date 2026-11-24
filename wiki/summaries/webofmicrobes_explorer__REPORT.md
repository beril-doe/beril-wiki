---
type: "Summary"
description: "Summary of the project Web of Microbes Data Explorer."
doc_type: "short"
full_text: "sources/webofmicrobes_explorer__REPORT.md"
---
# Web of Microbes Data Explorer

This page summarises the Web of Microbes (WoM) Data Explorer project. The report describes the action coding of a 2018 WoM snapshot and its matches to Fitness Browser (FB) strains, ModelSEED compounds and pangenome context. [src: webofmicrobes_explorer] It judges its first hypothesis (H1) partially supported: cross-collection links are real and actionable, and metabolite-to-gene integration is technically feasible. [src: webofmicrobes_explorer] The evidence is counts and matches from a small, single-laboratory snapshot that records production but not consumption. [src: webofmicrobes_explorer]

## Key Findings

### Snapshot contents

The snapshot's largest block is 6 biocrust isolates with 5,604 observations in BG11 media. [src: webofmicrobes_explorer] It also holds 10 ENIGMA groundwater isolates with 1,050 observations in R2A medium. [src: webofmicrobes_explorer] Four other isolates are Escherichia coli, Zymomonas, Synechococcus and Microcoleus. [src: webofmicrobes_explorer] There are 10 triculture time-series entries and 2 native microbiome entries. [src: webofmicrobes_explorer] There are also 4 theoretical auxotroph predictions and 1 control. [src: webofmicrobes_explorer]

WoM tracks 589 metabolites, of which 332 (56.4%) are unidentified and carry the Unk_ prefix. [src: webofmicrobes_explorer] The report says that, of the 257 identified metabolites, 408 (69.3% of all 589) show at least one change across the database. [src: webofmicrobes_explorer] The most metabolically active compounds are the amino acids glutamine, proline and phenylalanine and the nucleotides adenine, adenosine and guanine. [src: webofmicrobes_explorer]

### Action coding and what the snapshot lacks

WoM encodes metabolite observations with a 4-action system whose meaning differs between control and organism entries. [src: webofmicrobes_explorer] The snapshot holds 37 organisms across 5 ENIGMA-funded projects. [src: webofmicrobes_explorer]

| Entry type | Action | Meaning | Observations |
|---|---|---|---|
| Control | D | Detected in starting medium | 742 [src: webofmicrobes_explorer] |
| Control | N | Not detected | 1,023 [src: webofmicrobes_explorer] |
| Organism | I | Increased (present in medium, level went up) | 1,338 [src: webofmicrobes_explorer] |
| Organism | E | Emerged (not in medium, now detected; read as de novo production) | 1,155 [src: webofmicrobes_explorer] |
| Organism | N | No significant change | 7,509 [src: webofmicrobes_explorer] |

The report states that E and I have zero overlap across all 10,744 observations. [src: webofmicrobes_explorer] The five per-action counts in the table add up to more than 10,744, and the report does not explain the difference. [src: webofmicrobes_explorer] The emerged/increased distinction was not prominently documented and required data exploration to decode. [src: webofmicrobes_explorer]

No organism has a consumption ("Decreased") action in this 2018 snapshot, and all 742 D observations belong to the control. [src: webofmicrobes_explorer] The snapshot records only what organisms produce, so it cannot test whether consumed metabolites predict gene essentiality. [src: webofmicrobes_explorer] The original Kosina et al. (2018) paper, which introduced WoM with the same data, describes decrease as a valid action. [src: webofmicrobes_explorer] That confirms consumption belongs to the schema but is absent from this export. [src: webofmicrobes_explorer] See [[concepts/production-versus-consumption-coverage-in-exometabolomic-databases]].

### Cross-collection link assessment

The report rates each link between WoM and other collections separately. The WoM–Fitness Browser link is strong for 3 organisms. [src: webofmicrobes_explorer] The WoM–ModelSEED link is moderate, with an ambiguous formula-only expansion ratio of ~8:1. [src: webofmicrobes_explorer] The WoM–GapMind link is blocked because GapMind internal pathway names do not contain simple metabolite names. [src: webofmicrobes_explorer] Simple name matching failed, and a dedicated pathway-to-metabolite lookup table would enable the link. [src: webofmicrobes_explorer] Pangenome matching is available at genus level for all WoM organisms, but species-level matching needs strain-to-genome mapping, which the project did not attempt. [src: webofmicrobes_explorer]

In support of H1, the report cites 3 organisms with direct WoM–FB connections and substantial fitness data. [src: webofmicrobes_explorer] It also cites 19 metabolites produced by N2E3 that are tested as FB carbon or nitrogen sources. [src: webofmicrobes_explorer] It cites 26.8% of identified metabolites with definitive ModelSEED links. [src: webofmicrobes_explorer] Separately, 41.6% match by formula only, which is ambiguous, and 68.5% have a link of any confidence. [src: webofmicrobes_explorer] And it notes that all genera have pangenome representation. [src: webofmicrobes_explorer]

### Matching WoM organisms to Fitness Browser

Two WoM Pseudomonas strains match FB directly. FW300-N2E3 matches pseudo3_N2E3 (5,854 genes, 211 experiments). [src: webofmicrobes_explorer] GW456-L13 matches pseudo13_GW456_L13 (5,243 genes, 106 experiments). [src: webofmicrobes_explorer] Both are ENIGMA groundwater isolates with rich FB data. [src: webofmicrobes_explorer] E. coli BW25113 is the same strain as FB Keio (4,610 genes, 168 experiments). [src: webofmicrobes_explorer] However, its WoM data are limited to 12 observations in ZMMG medium, with a sulfur-metabolism focus only. [src: webofmicrobes_explorer] This is minimal despite Keio being one of the richest FB organisms. [src: webofmicrobes_explorer] Synechococcus PCC7002 matches FB SynE (PCC 7942) only at genus level (2,722 genes, 129 experiments). [src: webofmicrobes_explorer]

### Metabolites linking WoM to FB conditions for FW300-N2E3

Curated matching for pseudo3_N2E3 found 19 metabolites that the organism produces in WoM and that FB tests as carbon or nitrogen sources. [src: webofmicrobes_explorer] Of these, 5 are de novo products (E) and 14 are amplified metabolites (I). [src: webofmicrobes_explorer] The report lists these pairs (WoM action, then FB condition):

- Alanine, I: L-Alanine and D-Alanine, carbon/nitrogen. [src: webofmicrobes_explorer]
- Arginine, I: L-Arginine, nitrogen source. [src: webofmicrobes_explorer]
- Glycine, I: Glycine, nitrogen source. [src: webofmicrobes_explorer]
- Lactate, E: Sodium D-Lactate, carbon source. [src: webofmicrobes_explorer]
- Proline, I: L-Proline, carbon source. [src: webofmicrobes_explorer]
- Phenylalanine, I: L-Phenylalanine, carbon source. [src: webofmicrobes_explorer]
- Tryptophan, I: L-Tryptophan, nitrogen source. [src: webofmicrobes_explorer]
- Valine, E: L-Valine, carbon source. [src: webofmicrobes_explorer]
- Lysine, E: L-Lysine, nitrogen source. [src: webofmicrobes_explorer]
- Threonine, I: L-Threonine, nitrogen source. [src: webofmicrobes_explorer]
- Trehalose, I: D-Trehalose dihydrate, carbon source. [src: webofmicrobes_explorer]
- Adenine, I: Adenine hydrochloride, nitrogen source. [src: webofmicrobes_explorer]
- Adenosine, I: Adenosine, nitrogen source. [src: webofmicrobes_explorer]
- Inosine, I: Inosine, nitrogen source. [src: webofmicrobes_explorer]
- Thymine, E: Thymine, nitrogen source. [src: webofmicrobes_explorer]
- Malate, I: L-Malic acid, carbon source. [src: webofmicrobes_explorer]
- Nicotinamide, I: Nicotinamide, source type unspecified. [src: webofmicrobes_explorer]
- Carnitine, E: Carnitine hydrochloride, source type unspecified. [src: webofmicrobes_explorer]

See [[concepts/matching-exometabolite-profiles-to-gene-fitness-experiments]].

### ModelSEED compound matching

Of 257 identified (non-unknown) WoM compounds, 69 (26.8%) have definitive ModelSEED links by exact name match. [src: webofmicrobes_explorer] Exact-name matches are high-confidence 1:1 mappings. [src: webofmicrobes_explorer] Formula-only matches cover 107 compounds (41.6%) and are low confidence, with an average 1:8.4 expansion (107 WoM compounds to 900 ModelSEED molecules). [src: webofmicrobes_explorer] In total 176 compounds (68.5%) have some link of mixed confidence, and 81 (31.5%) are unmatched. [src: webofmicrobes_explorer] The formula C5H11NO2 illustrates the ambiguity: it matches valine, norvaline, betaine, 5-aminopentanoate and others. [src: webofmicrobes_explorer] Formula matches therefore give candidate sets for manual curation, not definitive identifications. [src: webofmicrobes_explorer] See [[concepts/compound-identifier-ambiguity-in-linking-metabolites-to-metabolic-models]].

### Metabolic novelty across ENIGMA isolates

The report states that the fraction of changes that are de novo (E) rather than amplified (I) varies 2-fold across ENIGMA isolates in R2A medium. [src: webofmicrobes_explorer] It calls the 15–32% range a new phenotypic measure, a "metabolic novelty rate", enabled by the E/I distinction. [src: webofmicrobes_explorer]

| Isolate | I | E | Novelty rate |
|---|---|---|---|
| Pseudomonas GW456-L13 | 49 | 34 | 32.4% [src: webofmicrobes_explorer] |
| Pseudomonas FW507-14TSA | 44 | 33 | 31.4% [src: webofmicrobes_explorer] |
| Pseudomonas FW300-N2A2 | 26 | 32 | 30.5% [src: webofmicrobes_explorer] |
| Acidovorax GW101-3E06 | 48 | 30 | 28.6% [src: webofmicrobes_explorer] |
| Bacillus FW507-8R2A | 39 | 16 | 15.2% [src: webofmicrobes_explorer] |

GW456-L13 has the highest novelty rate and FW507-8R2A the lowest. [src: webofmicrobes_explorer] The report proposes this rate as a potential phenotype for cross-referencing with pangenome gene content. This is a proposal, not a tested result. [src: webofmicrobes_explorer]

### Pangenome context

Pangenome context (gene clusters, conservation, functional annotations) is available for all WoM organism genera. [src: webofmicrobes_explorer]

| Taxon | Species | Genomes |
|---|---|---|
| Bacillus | 5 | 2,557 [src: webofmicrobes_explorer] |
| Rhizobium | 5 | 449 [src: webofmicrobes_explorer] |
| Pseudomonas fluorescens | 5 | 139 [src: webofmicrobes_explorer] |
| Synechococcus | 5 | 88 [src: webofmicrobes_explorer] |
| Phenylobacterium | 5 | 80 [src: webofmicrobes_explorer] |
| Acidovorax | 5 | 79 [src: webofmicrobes_explorer] |
| Zymomonas mobilis | 1 | 26 [src: webofmicrobes_explorer] |
| Escherichia coli | 1 | 2 [src: webofmicrobes_explorer] |

### Context from the literature

The report claims the first characterization of WoM data in a multi-collection lakehouse context. [src: webofmicrobes_explorer] De Raad et al. (2022) developed the Northen Lab Defined Medium (NLDM), which supports growth of 108/110 phylogenetically diverse soil bacteria, with all metabolites trackable via LC-MS/MS. [src: webofmicrobes_explorer] The report says the NLDM study tested 110 soil bacteria with full consumption and production tracking. [src: webofmicrobes_explorer] It suggests this dataset likely contains consumption data and may be available in the current GNPS2 version of WoM. [src: webofmicrobes_explorer] Jacoby & Kopriva (2019) reviewed exometabolomics for cross-feeding and resource competition and noted its complementarity with genomics. [src: webofmicrobes_explorer] Douglas (2020) framed the exometabolome as an ecological resource and stressed the need for databases linking exometabolomics to genomics. [src: webofmicrobes_explorer]

## Data and Methods

The analysis used KBase Data Lakehouse collections: kescience_webofmicrobes (compound, environment, organism, project, observation tables) for production and excretion profiles. [src: webofmicrobes_explorer] It used kescience_fitnessbrowser (organism, gene, experiment) for organism overlap and condition matching. [src: webofmicrobes_explorer] It used kbase_msd_biochemistry (molecule) for compound name and formula matching. [src: webofmicrobes_explorer] It used kbase_ke_pangenome (pangenome, gapmind_pathways) for species clade counts and pathway predictions. [src: webofmicrobes_explorer]

## Caveats and Open Work

- The snapshot has no organism consumption action. Newer GNPS2 data may add consumption. [src: webofmicrobes_explorer]
- The report predicts that ingesting NLDM would resolve the no-consumption limitation and increase the organism count 3–5×. [src: webofmicrobes_explorer]
- The data are small (37 organisms, 5 projects) and from a single laboratory. [src: webofmicrobes_explorer] 37 organisms (20 experimental) is too few for statistical analyses across organism groups. [src: webofmicrobes_explorer]
- The frozen 2018 Wayback Machine snapshot may not reflect current WoM. The report expects the GNPS2-hosted version or Northen lab internal datasets, including the NLDM 110-organism panel, to be substantially richer. [src: webofmicrobes_explorer]
- E. coli BW25113 is the same strain as Keio, but WoM data cover only 12 observations in one medium. [src: webofmicrobes_explorer]
- The Synechococcus match is at genus level only. [src: webofmicrobes_explorer]
- Formula-only ModelSEED matches are ambiguous and need manual curation. [src: webofmicrobes_explorer]
- 81 identified compounds have no ModelSEED link. [src: webofmicrobes_explorer]
- GapMind linkage is blocked until a pathway-to-substrate/product lookup table exists. [src: webofmicrobes_explorer]
- Species-level pangenome matching was not attempted. [src: webofmicrobes_explorer]
- The report proposes using metabolic novelty rate as a phenotype to cross-reference with pangenome gene content. [src: webofmicrobes_explorer]

Next analyses the report proposes:

- Obtain the current WoM dataset from GNPS2 or the Northen lab to address the missing consumption data. [src: webofmicrobes_explorer]
- Build a GapMind pathway-to-metabolite lookup table from the GapMind documentation, enabling the WoM–GapMind link that failed in notebook 02. [src: webofmicrobes_explorer]
- For pseudo3_N2E3 and pseudo13_GW456_L13, identify genes that are fitness-important on carbon sources the same organism produces, testing whether metabolic output predicts gene essentiality. [src: webofmicrobes_explorer]
- Test whether organisms with higher E/(E+I) ratios have more open pangenomes or more accessory genes. [src: webofmicrobes_explorer]
- Re-run the ingestion pipeline (data/wom_ingest/) when newer WoM data are available, to update kescience_webofmicrobes and enable the blocked consumption analyses. [src: webofmicrobes_explorer]

## Slots Into

- [[concepts/production-versus-consumption-coverage-in-exometabolomic-databases]]: the 2018 snapshot has no organism consumption action. [src: webofmicrobes_explorer]
- [[concepts/matching-exometabolite-profiles-to-gene-fitness-experiments]]: 19 metabolites for pseudo3_N2E3 link WoM production to FB carbon or nitrogen conditions. [src: webofmicrobes_explorer]
- [[concepts/compound-identifier-ambiguity-in-linking-metabolites-to-metabolic-models]]: only 69 compounds (26.8%) have exact-name ModelSEED links. [src: webofmicrobes_explorer]
- [[concepts/linking-exometabolic-phenotypes-to-pangenome-gene-content]]: novelty rate is proposed as a pangenome-linkable phenotype. [src: webofmicrobes_explorer]
- [[concepts/linking-isolate-and-strain-records-to-reference-genome-databases]]: strain-level and genus-level FB matches differ across WoM organisms. [src: webofmicrobes_explorer]
- [[concepts/taxonomic-and-single-laboratory-coverage-limits-of-exometabolomic-data]]: the data come from 37 organisms and 5 projects in a single laboratory. [src: webofmicrobes_explorer]
