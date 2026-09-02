---
type: "Summary"
description: "Web of Microbes data exploration and cross-collection integration assessment"
doc_type: "short"
full_text: "sources/webofmicrobes_explorer__REPORT.md"
---
# Web of Microbes Data Explorer

## Overview

This project characterized a 2018 snapshot of the Web of Microbes (WoM) database in the BER data lakehouse and assessed links to the Fitness Browser, ModelSEED, GapMind, and pangenome resources. It found that WoM action codes distinguish metabolite amplification from de novo emergence, while cross-collection links support metabolite-to-gene analyses but are limited by absent consumption data, ambiguous compound matching, and a small organism set. [src: webofmicrobes_explorer]

## Key Findings

### Action encoding distinguishes amplification from emergence

WoM uses four action semantics. For the control, “The Environment,” `D` means detected in the starting medium (742 observations) and `N` means not detected (1,023). For organisms, `I` means increased—present in the medium and subsequently higher (1,338)—`E` means emerged—absent from the medium and newly detected, indicating de novo production (1,155)—and `N` means no significant change (7,509). `E` and `I` are mutually exclusive across all 10,744 observations. All 742 `D` observations belong exclusively to the control, and no organism has a decreased or consumption action in this snapshot. [src: webofmicrobes_explorer]

The absence of organism consumption data is notable because Kosina et al. (2018) describes “decrease” as a valid WoM action; the report therefore suggests that consumption data may exist in a newer GNPS2 version rather than in this 2018 export. [src: webofmicrobes_explorer]

### Fitness Browser strain overlap

WoM has two direct Fitness Browser strain matches and two additional same-strain or genus-level matches. *Pseudomonas* sp. FW300-N2E3 matches `pseudo3_N2E3` directly, with 5,854 genes and 211 experiments; *Pseudomonas* sp. GW456-L13 matches `pseudo13_GW456_L13` directly, with 5,243 genes and 106 experiments; *E. coli* BW25113 matches `Keio` as the same strain, with 4,610 genes and 168 experiments; and *Synechococcus* PCC7002 matches `SynE` (PCC 7942) at the genus level, with 2,722 genes and 129 experiments. [src: webofmicrobes_explorer]

The two direct *Pseudomonas* matches are ENIGMA groundwater isolates with substantial Fitness Browser data. Although Keio is the same *E. coli* strain, its WoM record contains only 12 observations focused on sulfur metabolism in ZMMG medium. [src: webofmicrobes_explorer]

### Metabolite production connects to fitness experiments

For `pseudo3_N2E3`, curated matching identified 19 WoM-produced metabolites that are also tested by the Fitness Browser as carbon or nitrogen sources. The matched metabolites are alanine (`I`; L-Alanine and D-Alanine, carbon/nitrogen), arginine (`I`; L-Arginine, nitrogen), glycine (`I`; Glycine, nitrogen), lactate (`E`; Sodium D-Lactate, carbon), proline (`I`; L-Proline, carbon), phenylalanine (`I`; L-Phenylalanine, carbon), tryptophan (`I`; L-Tryptophan, nitrogen), valine (`E`; L-Valine, carbon), lysine (`E`; L-Lysine, nitrogen), threonine (`I`; L-Threonine, nitrogen), trehalose (`I`; D-Trehalose dihydrate, carbon), adenine (`I`; Adenine hydrochloride, nitrogen), adenosine (`I`; Adenosine, nitrogen), inosine (`I`; Inosine, nitrogen), thymine (`E`; Thymine, nitrogen), malate (`I`; L-Malic acid, carbon), nicotinamide (`I`; no listed carbon/nitrogen type), and carnitine (`E`; Carnitine hydrochloride, no listed carbon/nitrogen type). The report states that 5 of the 19 matches are de novo products (`E`) and 14 are amplified metabolites (`I`). [src: webofmicrobes_explorer]

This bridge enables analyses asking which genes are fitness-important when an organism uses a metabolite that it produces; the report gives de novo lactate production by *Pseudomonas* FW300-N2E3 and Fitness Browser lactate-utilization phenotypes as a direct example. [src: webofmicrobes_explorer]

### ModelSEED compound-link quality

Of 257 identified, non-unknown WoM compounds, 69 (26.8%) have definitive ModelSEED links through exact name matching. An additional 107 compounds (41.6%) have formula-only matches, producing 176 compounds with any link (68.5%) and leaving 81 unmatched (31.5%). Formula matching is ambiguous: the 107 WoM compounds expand to 900 ModelSEED molecules, an average of 8.4 ModelSEED molecules per WoM compound; for example, formula C5H11NO2 can match valine, norvaline, betaine, 5-aminopentanoate, and other molecules. [src: webofmicrobes_explorer]

The report treats exact name matches as high-confidence 1:1 mappings and formula-only matches as low-confidence candidate sets for manual curation rather than definitive identifications. [src: webofmicrobes_explorer]

### ENIGMA metabolic novelty rates

Among ENIGMA isolates grown in R2A medium, the fraction of changes representing de novo production (`E`) rather than amplification (`I`) varies from 15.2% to 32.4%. *Pseudomonas* GW456-L13 has 49 increased and 34 emerged metabolites, with 32.4% novel; *Pseudomonas* FW507-14TSA has 44 increased and 33 emerged, with 31.4% novel; *Pseudomonas* FW300-N2A2 has 26 increased and 32 emerged, with 30.5% novel; *Acidovorax* GW101-3E06 has 48 increased and 30 emerged, with 28.6% novel; and *Bacillus* FW507-8R2A has 39 increased and 16 emerged, with 15.2% novel. [src: webofmicrobes_explorer]

The report proposes the `E/(E+I)` fraction as a metabolic novelty phenotype that can be cross-referenced with pangenome gene content, while noting that this is a future analysis rather than an established relationship. [src: webofmicrobes_explorer]

### Pangenome representation

All WoM genera have pangenome species clades. The reported top-five species-clade counts and total genomes are: *Bacillus*, 5 species and 2,557 genomes; *Rhizobium*, 5 and 449; *Pseudomonas fluorescens*, 5 and 139; *Synechococcus*, 5 and 88; *Phenylobacterium*, 5 and 80; *Acidovorax*, 5 and 79; *Zymomonas mobilis*, 1 and 26; and *Escherichia coli*, 1 and 2. [src: webofmicrobes_explorer]

Pangenome gene clusters, conservation, and functional annotations are available at genus level for all WoM organism genera, but species-level matching requires strain-to-genome mapping, which this project did not attempt. [src: webofmicrobes_explorer]

### Database scale and collection coverage

The 2018 WoM snapshot contains 37 organisms across 5 ENIGMA-funded projects: 6 biocrust isolates with 5,604 observations in BG11 media; 10 ENIGMA groundwater isolates with 1,050 observations in R2A medium; 4 other isolates including *E. coli*, *Zymomonas*, *Synechococcus*, and *Microcoleus*; 10 triculture time-series entries; 2 native microbiome entries; 4 theoretical auxotroph predictions; and 1 control. [src: webofmicrobes_explorer]

The database tracks 589 metabolites, of which 332 (56.4%) are unidentified with an `Unk_` prefix. Of the 257 identified metabolites, 408 (69.3% of all 589) show at least one change across the database. The most metabolically active compounds are amino acids, including glutamine, proline, and phenylalanine, and nucleotides, including adenine, adenosine, and guanine. [src: webofmicrobes_explorer]

### Cross-collection integration assessment

The report assesses WoM-to-Fitness Browser integration as strong for 3 organisms, with the two *Pseudomonas* strains having more than 5,000 genes and more than 100 experiments each, and with Fitness Browser conditions directly testing metabolites detected as produced by WoM. WoM-to-ModelSEED integration is moderate because 26.8% of identified metabolites have definitive name-based links and 41.6% have ambiguous formula-only links. WoM-to-GapMind integration is blocked by pathway names using internal identifiers rather than simple metabolite names, so a pathway-to-substrate/product lookup table is required. WoM-to-pangenome integration is available at genus level for all WoM organisms, while species-level matching remains incomplete. [src: webofmicrobes_explorer]

## Caveats and Future Directions

The report identifies the lack of consumption data as the fundamental limitation: this snapshot records what organisms produce but not what they consume, preventing tests of whether consumed metabolites predict gene essentiality. The dataset is also small, comprising 37 organisms (20 experimental organisms), and comes from a single laboratory. [src: webofmicrobes_explorer]

The snapshot is frozen in 2018 and was accessed through the Wayback Machine, so it may not represent the current WoM state. The GNPS2-hosted version or Northen laboratory datasets, including the Northen Lab Defined Medium study of 110 soil bacteria, may provide a larger and richer resource with consumption data. [src: webofmicrobes_explorer]

GapMind pathway matching failed because pathway names did not contain simple metabolite names; a dedicated pathway-to-metabolite mapping table is needed. WoM coverage of *E. coli* BW25113 is especially limited despite the richness of its Keio Fitness Browser data, with only 12 WoM observations focused on sulfur and cysteine. [src: webofmicrobes_explorer]

The report proposes obtaining the current WoM dataset from GNPS2 or the Northen laboratory; building a GapMind pathway-to-metabolite lookup table; testing gene fitness against metabolites produced by `pseudo3_N2E3` and `pseudo13_GW456_L13`; testing whether higher `E/(E+I)` ratios associate with more open pangenomes or accessory genes; and re-ingesting WoM when consumption data become available. [src: webofmicrobes_explorer]

## Slots Into

- [[concepts/cross-tenant-data-bridging]] — WoM links metabolite observations to Fitness Browser, ModelSEED, GapMind, and pangenome collections, demonstrating actionable cross-collection integration and its naming and coverage barriers.
- [[concepts/multi-omics-integration]] — The 19-metabolite WoM–Fitness Browser bridge connects exometabolite production with gene-fitness experiments and provides a concrete metabolite-to-gene analysis path.
- [[concepts/metabolic-model-gapfilling]] — Exact and formula-only ModelSEED links quantify compound-annotation coverage and expose the ambiguity that limits reaction-level interpretation.
- [[concepts/gene-essentiality]] — The report proposes testing whether Fitness Browser gene importance on carbon or nitrogen sources is related to metabolites produced by the same organism, while noting that missing consumption data blocks the stronger prediction.
- [[concepts/pangenome-integration]] — Genus-level pangenome representation for all WoM genera enables future comparisons between metabolic novelty rates and gene-content openness.
- [[concepts/provenance-aware-resource-discovery]] — The 2018 archived snapshot, GNPS2/Northen laboratory alternatives, source tables, notebooks, and generated link files document provenance and reproducibility constraints.
