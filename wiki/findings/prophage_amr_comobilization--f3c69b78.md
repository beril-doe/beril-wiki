---
type: "Finding"
description: "Across the full pangenome inventory, 83,008 AMR gene clusters and 3.47 million prophage marker clusters were identified, and 14,669 of 27,702 species (52.9%) carry both AMR and prophage markers."
finding_id: "prophage_amr_comobilization--f3c69b78"
result: "observation"
source: "prophage_amr_comobilization"
quantities: [{"value": "14,669", "what": "species carrying both AMR and prophage markers", "unit": "species", "denominator": "27,702 species in the pangenome", "scope": "full pangenome inventory"}, {"value": "52.9%", "what": "share of species carrying both AMR and prophage markers", "unit": "", "denominator": "27,702 species", "scope": "full pangenome inventory"}, {"value": "83,008", "what": "AMR gene clusters identified", "unit": "clusters", "denominator": "", "scope": "full pangenome inventory"}]
caveat: "Prophage identification uses keyword/Pfam matching on bakta_annotations rather than dedicated tools such as PHASTER or geNomad, and may include false positives such as phage-defense systems and miss divergent prophages."
first_added: "2026-10-27"
source_hash: "f58710893c456806b9a06f5e9bd3687468082c34ffcf93be308e037eb59268b5"
---
# Over half of species carry both AMR and prophage markers

Across the full pangenome inventory, 83,008 AMR gene clusters and 3.47 million prophage marker clusters were identified, and 14,669 of 27,702 species (52.9%) carry both AMR and prophage markers. [src: prophage_amr_comobilization]

## Key figures

- **14,669 species**: species carrying both AMR and prophage markers (denominator 27,702 species in the pangenome; scope full pangenome inventory) [src: prophage_amr_comobilization]
- **52.9%**: share of species carrying both AMR and prophage markers (denominator 27,702 species; scope full pangenome inventory) [src: prophage_amr_comobilization]
- **83,008 clusters**: AMR gene clusters identified (scope full pangenome inventory) [src: prophage_amr_comobilization]

## Evidence

> Across the full pangenome inventory, 83,008 AMR gene clusters and 3.47 million prophage marker clusters were identified. Prophage markers are overwhelmingly accessory (83.8%) and frequently singleton (53.8%), while AMR genes are also predominantly accessory (69.7%) but less singleton (36.1%). Of 27,702 species in the pangenome, 14,669 (52.9%) carry both AMR and prophage markers. [src: prophage_amr_comobilization]

From the report [[summaries/prophage_amr_comobilization__REPORT]].

## Caveat

Prophage identification uses keyword/Pfam matching on bakta_annotations rather than dedicated tools such as PHASTER or geNomad, and may include false positives such as phage-defense systems and miss divergent prophages. [src: prophage_amr_comobilization]

> - **Prophage identification**: Uses keyword/Pfam matching on bakta_annotations rather than dedicated prophage prediction tools (e.g., PHASTER, geNomad). May include false positives (e.g., phage-defense systems) and miss divergent prophages. [src: prophage_amr_comobilization]

## Other caveats in this report

- The proximity–accessory association depends on the distance threshold and is heterogeneous across species: only 33 of 74 testable species had OR>1. [src: prophage_amr_comobilization]
- The fitness dataset covered only 48 model organisms with RB-TnSeq data and poorly overlapped the analyzed GTDB species. [src: prophage_amr_comobilization]
- The species-level association is consistent with two non-exclusive explanations—direct prophage transduction and shared gene-acquisition propensity—but does not distinguish them. [src: prophage_amr_comobilization]
- H1's aggregate difference was 2.1 percentage points and varied among species. Proposed explanations for the near-range reversal and broad-range strengthening are interpretations, not demonstrated mechanisms. [src: prophage_amr_comobilization]
- Reported gene distances are ordinal positions parsed from gene identifiers, not base-pair distances. [src: prophage_amr_comobilization]
