---
type: "Dataset"
description: "kbase_msd_biochemistry reaction and molecule tables used to resolve ADP1 reactions and compounds."
sources: ["summaries/acinetobacter_adp1_explorer__REPORT.md", "summaries/annotation_gap_discovery__REPORT.md", "summaries/berdl_data_atlas__REPORT.md", "summaries/enigma_carbon_census_1__REPORT.md", "summaries/pitfalls.md", "summaries/webofmicrobes_explorer__REPORT.md"]
aliases: ["ModelSEED", "kbase_msd_biochemistry"]
---
# ModelSEED biochemistry

ModelSEED biochemistry (also ModelSEED, kbase_msd_biochemistry) is the biochemistry collection in the [[entities/kbase-data-lakehouse]]. Its reaction and molecule tables serve as the ModelSEED reference for resolving reactions and compounds in several projects. [src: acinetobacter_adp1_explorer, berdl_data_atlas] Evidence comes from direct match counts in the ADP1 and Web of Microbes (WoM) reports, plus a list of usage pitfalls.

## Key facts

- The inventory lists 56,012 ModelSEED reactions [src: berdl_data_atlas] and 45,708 ModelSEED compounds. [src: berdl_data_atlas]
- The reaction and molecule tables supply the ModelSEED biochemistry reference. [src: berdl_data_atlas]
- The ADP1 exploration used them for ModelSEED reaction and compound name resolution. [src: acinetobacter_adp1_explorer] See [[summaries/acinetobacter_adp1_explorer__REPORT]].
- The annotation-gap report used the reaction and reagent tables for gapfilled reaction definitions and stoichiometry. [src: annotation_gap_discovery] See [[summaries/annotation_gap_discovery__REPORT]].
- The ENIGMA carbon census used ModelSEED compound, reaction and enzyme data to link compound to reaction to enzyme at Tier 2/3. [src: enigma_carbon_census_1] See [[entities/enigma]].
- The WoM report used the molecule table for compound name and formula matching for reaction-level annotation. [src: webofmicrobes_explorer]

## Match coverage

In the ADP1 connection scan, 1,210 of 1,330 database reactions matched biochemistry (91%). [src: acinetobacter_adp1_explorer] All 230 database compounds matched (100%). [src: acinetobacter_adp1_explorer] The 120 unmatched reactions (9%) may be custom or draft reactions not yet in ModelSEED. [src: acinetobacter_adp1_explorer] This is a hypothesis, not a tested result.

Separately, the WoM report matched its identified compounds to ModelSEED. Of 257 identified (non-unknown) WoM compounds, 69 (26.8%) have definitive links by exact name match, and this is a high-confidence 1:1 mapping. [src: webofmicrobes_explorer] Another 107 (41.6%) match by formula only. This is low confidence, with an average 1:8.4 expansion to 900 ModelSEED molecules. [src: webofmicrobes_explorer] In all, 176 compounds (68.5%) have a link of mixed confidence [src: webofmicrobes_explorer], and 81 (31.5%) are unmatched. [src: webofmicrobes_explorer]

Formula matches are ambiguous. For example, C5H11NO2 matches valine, norvaline, betaine, 5-aminopentanoate and others. [src: webofmicrobes_explorer] Such matches give candidate sets for manual curation, not definitive identifications. [src: webofmicrobes_explorer] See [[concepts/compound-identifier-ambiguity-in-linking-metabolites-to-metabolic-models]].

## Usage pitfalls

- IDs use a prefix-colon form, such as `seed.reaction:rxn00001` and `seed.compound:cpd00001`, not bare `rxnNNNNN`. [src: pitfalls] See [[concepts/join-key-validity-and-identifier-format-mismatches]].
- The reaction table has no Enzyme Commission (EC) number column, so no EC-to-reaction mapping exists in the Lakehouse. The report suggests bridging through eggNOG KEGG_ko or KEGG_Reaction to reaction.abbreviation, or using GapMind pathways. [src: pitfalls]
- reaction.abbreviation holds KEGG R-numbers for only about 80% of reactions (44,904 / 56,012). The other 20% have no external ID. [src: pitfalls]
- BiGG_Reaction appears in eggNOG annotations but not in ModelSEED tables, so no biochemistry-side BiGG mapping exists. [src: pitfalls]
- reaction_similarity has about 671M rows. Always filter by reaction_1 or reaction_2. [src: pitfalls]
- deltag has extreme outliers. The report recommends a bound such as deltag > -10000000 for aggregations. [src: pitfalls]
- Many molecule rows lack SMILES or InChIKey. Use LEFT JOIN, not INNER JOIN, to structure. [src: pitfalls]

## Interpretive caveat

The ENIGMA carbon census read the structural simplicity of "callable" compounds as at least as much an annotation-coverage ceiling as biological bioavailability. KEGG, ModelSEED and genome_depot annotate simple, common, pollutant-adjacent aromatics. [src: enigma_carbon_census_1] See [[concepts/annotation-coverage-bias-in-chemical-class-callability]].
