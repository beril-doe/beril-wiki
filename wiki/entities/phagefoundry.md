---
type: "Dataset"
description: "Dataset of phage, mobile-element, and strain-susceptibility records"
sources: ["summaries/berdl_data_atlas__REPORT.md", "summaries/discoveries.md", "summaries/ibd_phage_targeting__REPORT.md", "summaries/snipe_defense_system__REPORT.md"]
---
# PhageFoundry

## Identity

**Canonical name:** PhageFoundry. [src: berdl_data_atlas]

**Known aliases:** No aliases are specified in the source document. [src: berdl_data_atlas]

**Stable external identifier:** No stable external identifier is specified in the source document. [src: berdl_data_atlas]

PhageFoundry is a BERDL dataset and tenant containing phage, mobile-element, and strain-modelling records. [src: berdl_data_atlas]

## Key Facts

PhageFoundry accounts for 14% of BERDL tables, and the `mobile_phage` topic is 96% owned by PhageFoundry. [src: berdl_data_atlas] The inventory contains 15,677,623 IMG/VR viral sequence records and 933,103 PhageFoundry strain-modelling gene records. [src: berdl_data_atlas]

Among 66 audited BERIL projects, PhageFoundry appears in 5 projects, despite containing 14% of BERDL tables. [src: berdl_data_atlas] The atlas recommends PhageFoundry catalogs for phage and mobile-element data. [src: berdl_data_atlas]

The discoveries log refines the strain-modelling inventory with a database-level example: PhageFoundry contained 17,672 binary infection outcomes from 188 *Escherichia coli* strains and 96 phages, supporting its use for strain–phage susceptibility modelling; an ML model achieved AUC=0.883. [src: discoveries] Lambda infected 1/188 strains (0.5%), compared with 43.4% for Myoviridae, illustrating strong phage-specific variation in the recorded outcomes. [src: discoveries]

The new IBD phage-targeting analysis **supports** this strain–phage modelling use: its PhageFoundry subset contained 96 phages, 188 *Escherichia coli* strains, and 17,672 experimentally tested susceptibility pairs, including 3,929 susceptible pairs and a 22 % susceptibility rate. [src: ibd_phage_targeting] A greedy minimum-set-cover design selected five phages covering 94.7 % of the 188 strains, while an eight-phage design reached 98.4 % coverage. [src: ibd_phage_targeting] These coverage results **refine** the atlas-level recommendation by showing a concrete cocktail-design application, but they apply to tested *E. coli* strains rather than UC Davis patient isolates and do not establish in-vivo efficacy. [src: ibd_phage_targeting]

The discoveries log also supports PhageFoundry as a source for defense-system and mobile-element analyses: the SNIPE defense system occurred in 4,572 gene clusters across 1,696 species and 33 phyla, with 86.7% accessory or singleton. [src: discoveries] The SNIPE analysis **supports and refines** this role by linking PhageFoundry’s strain–phage records to a corrected SNIPE architecture and reporting DUF4041 in *Klebsiella* but not in *Acinetobacter*, *P. aeruginosa*, or *P. viridiflava* in the four-species comparison. [src: snipe_defense_system] It also reports 188 *E. coli* strains, 96 phages, and 17,672 possible binary infection outcomes, of which 3,929 were positive and 13,743 negative; the model achieved AUC = 0.883 and accuracy = 84.3%. [src: snipe_defense_system] These findings refine rather than replace the atlas's inventory-level recommendation: database presence and schema compatibility still do not establish complete value-space overlap or biological comparability. [src: berdl_data_atlas, discoveries]

The atlas identifies an unused UC2 bridge between [[entities/enigma-coral|ENIGMA]] and PhageFoundry with 11 shared keys for studying subsurface prophages, metal resistance, and the Oak Ridge contamination gradient. [src: berdl_data_atlas] UC2 had zero realized use at the time of the audit and requires live-cluster execution because schema-level key compatibility does not establish value-space overlap. [src: berdl_data_atlas]

## Related Pages

- [[summaries/berdl_data_atlas__REPORT]] — source summary for the BERDL Data Atlas inventory and cross-reference analysis.
- [[summaries/discoveries]] — cross-project findings on PhageFoundry strain modelling, defense systems, and data integration.
- [[summaries/ibd_phage_targeting__REPORT]] — metagenome-prioritized phage-cocktail design and its PhageFoundry evidence base.
- [[summaries/snipe_defense_system__REPORT]] — SNIPE defense-system prevalence, architecture, environmental association, and PhageFoundry evidence.
- [[concepts/environmental-resistome]] — environmental resistance, phage, and subsurface integration opportunities.
- [[entities/nmdc-arkin]] — a potential partner dataset for environmental and multi-omics integration.
- [[entities/protect-genomedepot]] — a potential partner dataset for pathogen-genome comparisons.
