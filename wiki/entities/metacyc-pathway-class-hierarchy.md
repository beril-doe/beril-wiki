---
type: "Dataset"
description: "Curated pathway class hierarchy from ModelSEEDDatabase used to categorize HUMAnN3 pathways into IBD themes."
sources: ["summaries/discoveries.md", "summaries/ibd_phage_targeting__REPORT.md"]
aliases: ["MetaCyc", "MetaCyc_Pathways.tbl"]
---
# MetaCyc pathway class hierarchy

This page covers the MetaCyc pathway class hierarchy (MetaCyc_Pathways.tbl), which the ibd_phage_targeting project used to categorize HUMAnN3 pathways into IBD themes. ModelSEEDDatabase distributes it. [src: discoveries] The evidence is one project's categorization, reported in the discoveries digest and the project report. See [[summaries/ibd_phage_targeting__REPORT]] and [[summaries/discoveries]].

## Key facts

- ModelSEEDDatabase provides the hierarchy at /global_share/KBaseUtilities/ModelSEEDDatabase/Biochemistry/Aliases/Provenance/MetaCyc_Pathways.tbl, with 90 %+ coverage of HUMAnN3 outputs. [src: discoveries]
- The ibd_phage_targeting v1.8 categorization combined this hierarchy with a 12-theme inflammatory bowel disease (IBD) overlay. [src: discoveries]
- In v1.8, 357/409 (87 %) of pathways had MetaCyc class data. [src: discoveries]
- In v1.8, 262/409 (64 %) of pathways were assigned to ≥ 1 IBD theme. [src: discoveries]

## Worked example: PWY-5920

MetaCyc's curator-validated hierarchy places PWY-5920 under HEME-SYN, Heme-b-Biosynthesis, Cofactor-Biosynthesis and Tetrapyrrole-Biosynthesis. [src: discoveries] The project report states the same assignment for the v1.8 ModelSEED class hierarchy. [src: ibd_phage_targeting] In v1.7, the 0_other category hid 15+ heme/iron pathways. [src: discoveries]

## Recommendation

The report concludes that ModelSEEDDatabase's hierarchy, at 90 % coverage of HUMAnN3 outputs, should be the default for any pathway category-enrichment test in BERIL projects, in preference to regex on pathway names. [src: ibd_phage_targeting] This became plan norm N17 in ibd_phage_targeting. It prefers curator-validated ontologies or class hierarchies over name-pattern regex, and keeps regex as a sensitivity check. [src: discoveries] The report names KEGG BRITE and the Gene Ontology (GO) biological-process subontology as analogous resources for KEGG / EC-level data. [src: discoveries] For the general argument, see [[concepts/ontology-versus-name-pattern-categorization-in-pathway-enrichment-tests]].
