---
type: "Dataset"
description: "DOE BRaVE PhageFoundry host-specific genome browsers and strain models for phage–host work, including the Acinetobacter genome browser."
sources: ["summaries/acinetobacter_adp1_explorer__REPORT.md", "summaries/berdl_data_atlas__REPORT.md", "summaries/discoveries.md", "summaries/ibd_phage_targeting__REPORT.md", "summaries/pitfalls.md", "summaries/snipe_defense_system__REPORT.md"]
aliases: ["Phage Foundry", "PhageFoundry Acinetobacter genome browser", "phagefoundry", "phagefoundry_acinetobacter_genome_browser", "phagefoundry_strain_modelling"]
---
# PhageFoundry

PhageFoundry (also Phage Foundry) is the DOE BRaVE program's source of host-specific genome browsers and strain models for phage–host work in the KBase Data Lakehouse. [src: berdl_data_atlas] It holds 14% of Lakehouse tables and appeared in 5 audited BERIL projects. [src: berdl_data_atlas] The reports use its strain-modelling database for E. coli phage infection outcomes, and they use its genome browsers for defense-term searches. [src: ibd_phage_targeting, snipe_defense_system]

## Key facts

- The `phagefoundry` tenant is mono-topic. [src: berdl_data_atlas] The mobile_phage topic makes up 14% of Lakehouse tables and is associated with PhageFoundry. [src: berdl_data_atlas] PhageFoundry owns 96 % of that topic. [src: berdl_data_atlas]
- Funding attribution was corrected by the user: phagefoundry is DOE BRaVE, replacing an initial inference of "likely" Defense/HHS. [src: berdl_data_atlas] The earlier topic-map statement that Defense / HHS is mono-topic, represented by PhageFoundry entirely in mobile_phage, reflects the original inference. [src: berdl_data_atlas]
- The inventory lists ~1,950 PhageFoundry host genomes across 5 host species. [src: berdl_data_atlas]
- For phage and mobile genetic elements (MGE), the atlas report recommends `phagefoundry_*` per-host catalogs, joined to host genomes on `ncbi_taxon_id`. [src: berdl_data_atlas]
- Data are split into two database types. [src: pitfalls] A discoveries report found 7 databases in the tenant, not the 5 documented. [src: discoveries] The pitfalls report lists five: Acinetobacter, Klebsiella, P. aeruginosa and P. viridiflava browsers plus strain_modelling. [src: pitfalls]

## Genome browsers

The atlas report lists browser collections for Acinetobacter, Klebsiella, Pseudomonas aeruginosa and Pseudomonas viridiflava. It also lists an E. coli phage genome depot and a separate strain_modelling collection. [src: berdl_data_atlas] The four species browsers share the GenomeDepot schema. [src: pitfalls] They follow the pattern `phagefoundry_{species}_genome_browser_genomedepot` and hold genome annotations only (eggNOG, COG, Pfam) in `browser_*` tables, 10+ per database. [src: pitfalls] COG means clusters of orthologous groups. [src: snipe_defense_system]

The Acinetobacter browser has 37 tables. The ADP1 exploration identified it but did not query it deeply. [src: acinetobacter_adp1_explorer] That report proposes cross-referencing it with phage susceptibility data. [src: acinetobacter_adp1_explorer]

Cross-species queries must run the same SQL once per database, because no unified table exists. [src: pitfalls] The omitted `phagefoundry_ecoliphages_genomedepot` (with a duplicate `_genomedepot` variant) holds E. coli phage genomes relevant to targeting adherent-invasive E. coli (AIEC). [src: discoveries]

### Defense-term search

The SNIPE defense report searched defense-related terms in `browser_eggnog_description` across the 4 species. [src: snipe_defense_system] Counts are below.

| Species | DUF4041 | GIY-YIG | Nuclease | Restriction | Abortive infection |
|---|---|---|---|---|---|
| Klebsiella | 1 [src: snipe_defense_system] | 1 [src: snipe_defense_system] | 98 [src: snipe_defense_system] | 42 [src: snipe_defense_system] | 2 [src: snipe_defense_system] |
| Acinetobacter | 0 [src: snipe_defense_system] | 3 [src: snipe_defense_system] | 91 [src: snipe_defense_system] | 33 [src: snipe_defense_system] | 2 [src: snipe_defense_system] |
| P. aeruginosa | 0 [src: snipe_defense_system] | 2 [src: snipe_defense_system] | 125 [src: snipe_defense_system] | 54 [src: snipe_defense_system] | 2 [src: snipe_defense_system] |
| P. viridiflava | 0 [src: snipe_defense_system] | 0 [src: snipe_defense_system] | 90 [src: snipe_defense_system] | 41 [src: snipe_defense_system] | 1 [src: snipe_defense_system] |

The same report queried `browser_eggnog_description` and `browser_annotation` for ManYZ-related terms and Pfam domains. [src: snipe_defense_system] Because PhageFoundry has genome annotations only and no fitness or TnSeq (transposon sequencing) tables, it gave no Klebsiella-specific SNIPE or ManYZ fitness data. [src: snipe_defense_system] See also [[entities/klebsiella]].

## Strain modelling database

`phagefoundry_strain_modelling` is separate from the GenomeDepot browsers. It holds experimental phage-host interaction data and an ML model in 18 tables, including organism, interaction and feature. [src: pitfalls, discoveries] It had been overlooked as "timed out during discovery". [src: snipe_defense_system] It contains the Gaborieau et al. 2024 (Nature Microbiology) dataset. [src: snipe_defense_system]

- **Design:** 188 E. coli strains (ECOR, NILS, clinical/environmental isolates) × 96 phages (41 Podoviridae, 32 Myoviridae, 23 Siphoviridae) give 17,672 binary infection outcomes. [src: snipe_defense_system]
- **Outcomes:** 3,929 susceptible and 13,743 resistant pairs, a 22 % susceptibility rate. [src: ibd_phage_targeting, snipe_defense_system]
- **Model:** AUC (area under curve) = 0.883 and accuracy = 84.3%, trained on 1,582 gene cluster presence/absence features with SHAP (Shapley additive explanations) importance scores. [src: snipe_defense_system, discoveries]
- **Tables used:** `strainmodelling_interaction`, `strainmodelling_organism`, `strainmodelling_organism_metadata` and `strainmodelling_experiment_metric`. [src: snipe_defense_system]
- **Gene table:** PhageFoundry has 933,103 strain-modelling gene records. [src: berdl_data_atlas] The table has only `locus_tag` and `protein_seq`, so genes cannot be searched by name. [src: pitfalls] The `strainmodelling_feature` and `strainmodelling_protein_family` tables link gene clusters to SHAP-scored model features and work around this. [src: pitfalls]

### Use in IBD phage targeting

The IBD phage-targeting report calls this the definitive E. coli AIEC phage-cocktail design dataset for that project. [src: ibd_phage_targeting] Its notebook NB13 used 96 phages × 188 strains × 17,672 pairs from Gaborieau 2025-10-02. [src: ibd_phage_targeting] For a ≥95 % coverage target, 5 phages (DIJ07_P2 + LF73_P1 + AL505_Ev3 + 55989_P2 + LF110_P2) covered 94.7 % of strains. [src: ibd_phage_targeting] The report states that 65 of 94 phages (69 %) were isolated against B2/D phylogroup hosts and calls them strongly AIEC-relevant. [src: ibd_phage_targeting]

## Caveats

- There is no explicit AIEC-vs-commensal annotation. The 188 strains include LF82, LF73, 536, NIC06 and BCH953 as named isolation hosts, but accurate AIEC coverage needs a literature cross-reference. [src: ibd_phage_targeting]
- The susceptibility matrix is binary, with no titer or burst size. Real-world dosing also depends on burst size, receptor binding kinetics and gastric passage survival, which were outside project scope. [src: ibd_phage_targeting]
- Exploring only the GenomeDepot databases can wrongly suggest PhageFoundry has no experimental data. [src: pitfalls] The report recommends checking all databases that share a project prefix. [src: pitfalls]
- For rarely accessed databases, including this one, Spark warm-up can make `/count` return correct results while `/query` and `/sample` return 0 rows or empty results. [src: pitfalls]

## Cross-program use

DOE BRaVE (PhageFoundry) and ARPA-H (PROTECT) are under-leveraged for cross-program work: each appears in fewer than 8 projects. [src: berdl_data_atlas] The enigma ↔ phagefoundry bridge had 11 keys and zero realized use at audit time. [src: berdl_data_atlas] See [[concepts/realized-versus-theoretical-cross-collection-data-reuse]].
