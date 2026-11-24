---
type: "Dataset"
description: "Curated growth observations across organisms, held as kescience_webofmicrobes."
sources: ["summaries/berdl_data_atlas__REPORT.md", "summaries/discoveries.md", "summaries/fw300_metabolic_consistency__REPORT.md", "summaries/genotype_to_phenotype_enigma__REPORT.md", "summaries/pitfalls.md", "summaries/webofmicrobes_explorer__REPORT.md"]
aliases: ["WoM", "kescience_webofmicrobes"]
---
# Web of Microbes

Web of Microbes (WoM; KBase Data Lakehouse collection kescience_webofmicrobes) is a curated set of exometabolomic growth observations. It holds 10,744 observations across 37 organisms. [src: berdl_data_atlas] Its main limits are that it is small, comes from one laboratory, and records production but not consumption. [src: webofmicrobes_explorer]

## Key facts

- The collection is a 2018 frozen snapshot, and newer data lives in GNPS2 rather than here. [src: pitfalls]
- Kosina et al. (2018) introduced WoM with the same data the explorer report analyzed. [src: webofmicrobes_explorer]
- The observation and organism tables supply the curated growth observations. [src: berdl_data_atlas] The explorer report also uses the compound, environment and project tables. [src: webofmicrobes_explorer]
- The report recommends kescience_bacdive for organismal traits and kescience_webofmicrobes for carbon utilization, joined via ncbi_taxon_id. [src: berdl_data_atlas] See [[entities/bacdive]].
- Roughly 56% of compound names are unidentified (Unk_* prefix) and should be filtered out for named-metabolite analyses. [src: pitfalls] Another count gives 589 tracked metabolites, of which 332 (56.4%) are unidentified. [src: webofmicrobes_explorer]
- The most metabolically active compounds are amino acids (glutamine, proline, phenylalanine) and nucleotides (adenine, adenosine, guanine). [src: webofmicrobes_explorer]
- One sentence of the explorer report says 408 metabolites (69.3% of all 589) show at least one change. That sentence refers to the 257 identified metabolites, so the figures do not obviously agree. [src: webofmicrobes_explorer]

## Action encoding

Control and organism entries use different action codes, so the actor must be known before an action is read. [src: webofmicrobes_explorer, pitfalls]

| Actor | Code | Meaning | Observations |
|---|---|---|---|
| Control ("The Environment") | D | Detected in starting medium | 742 [src: webofmicrobes_explorer] |
| Control | N | Not detected | 1,023 [src: webofmicrobes_explorer] |
| Organisms | I | Increased (present in medium, level went up) | 1,338 [src: webofmicrobes_explorer] |
| Organisms | E | Emerged (not in medium, now detected; de novo production) | 1,155 [src: webofmicrobes_explorer] |
| Organisms | N | No significant change | 7,509 [src: webofmicrobes_explorer] |

E and I are mutually exclusive, with zero overlap across all 10,744 observations. [src: webofmicrobes_explorer, discoveries, pitfalls] The E/I distinction was not prominently documented and had to be decoded by data exploration. [src: webofmicrobes_explorer]

A plain SELECT of the action field returns raw codes, not a binary produced/consumed label. [src: pitfalls] The ENIGMA genotype-to-phenotype notebooks NB02 and NB08 define produced as action IN ('I', 'E'). [src: pitfalls] That counts a compound as produced if it increased in supernatant or emerged from below the detection limit. [src: pitfalls] Including N makes every strain look like a production generalist and collapses the signal. [src: pitfalls] Excluding E misses genuinely novel production. [src: pitfalls]

## No consumption data

The 2018 snapshot has no organism Decreased (consumption) action. All 742 D observations belong to the control, so the database records production but not consumption. [src: discoveries, webofmicrobes_explorer] This is by design, not a query bug. [src: pitfalls] See [[concepts/production-versus-consumption-coverage-in-exometabolomic-databases]].

## Contents

The snapshot covers 37 organisms across 5 ENIGMA-funded projects. [src: webofmicrobes_explorer] See [[entities/enigma]]. The groups are:

- 6 biocrust isolates, with 5,604 observations in BG11 media, the largest data block. [src: webofmicrobes_explorer]
- 4 other isolates: Escherichia coli, Zymomonas, Synechococcus and Microcoleus. [src: webofmicrobes_explorer]
- 10 triculture time-series entries and 2 native microbiome entries. [src: webofmicrobes_explorer]
- 4 theoretical auxotroph predictions and 1 control. [src: webofmicrobes_explorer]

## Links to other resources

Two WoM organisms are exact strain matches to Fitness Browser (FB) organisms. Pseudomonas sp. FW300-N2E3 matches pseudo3_N2E3, with 5,854 genes and 211 experiments. [src: discoveries] Pseudomonas sp. GW456-L13 matches pseudo13_GW456_L13, with 5,243 genes and 106 experiments. [src: discoveries] See [[entities/pseudomonas-fluorescens-fw300-n2e3]] and [[entities/pseudomonas-sp-gw456-l13]]. E. coli BW25113 is the same strain as Keio in the FB. This enables direct metabolite-to-gene-fitness linking. [src: discoveries] See [[entities/escherichia-coli]] and [[concepts/matching-exometabolite-profiles-to-gene-fitness-experiments]].

For these matched organisms, FB carbon-source experiments test metabolites that WoM detects as produced, with 109 metabolite-condition name overlaps. [src: discoveries]

Of 257 identified (non-unknown) WoM compounds, 69 match ModelSEED molecules by exact name and 107 by formula. [src: discoveries] That totals 176 (68.5%) and enables reaction-level annotation for the majority of metabolites. [src: discoveries] See [[concepts/compound-identifier-ambiguity-in-linking-metabolites-to-metabolic-models]].

### FW300-N2E3 profile

Starting from 58 WoM metabolites (27 Emerged, 31 Increased) [src: fw300_metabolic_consistency], 21 could be cross-referenced against at least one other database. [src: fw300_metabolic_consistency] Among these, 17/21 (81%) were fully concordant across all matched databases, 4/21 (19%) were partially concordant, and none were fully discordant. The mean concordance score was 0.94. [src: fw300_metabolic_consistency] See [[concepts/cross-database-concordance-of-metabolite-evidence]].

The WoM profile was measured on R2A rich medium, whereas FB used minimal medium with single C/N sources. Some WoM metabolites may therefore be produced only on rich media. [src: fw300_metabolic_consistency] See [[entities/r2a-medium]].

In the genotype-to-phenotype ENIGMA analysis, WoM covers 6 strains and 630 metabolite observations, with 105 compounds per strain. [src: genotype_to_phenotype_enigma] That analysis uses an FB-cognate feature set of 156 KOs (KEGG orthologs). These are KOs with significant rich-media fitness in Pseudomonas FB anchors that also vary across the 6 WoM strains. [src: genotype_to_phenotype_enigma]

## Caveats

The data are small (37 organisms, 5 projects) and come from a single laboratory. [src: webofmicrobes_explorer] The 37 organisms (20 experimental) are too few for statistical analyses across organism groups. [src: webofmicrobes_explorer] See [[concepts/taxonomic-and-single-laboratory-coverage-limits-of-exometabolomic-data]] and [[concepts/gene-metabolite-association-discovery-in-small-exometabolomic-datasets]]. The explorer report claims the first characterization of WoM in a multi-collection lakehouse context. [src: webofmicrobes_explorer]
