---
type: "Dataset"
description: "Chemical-identity database used to resolve all 83 census compounds"
sources: ["summaries/enigma_carbon_census_1__REPORT.md"]
---
# PubChem

## What this entity is

PubChem is the canonical name of a chemical-structure and compound-identity dataset used in the ENIGMA Carbon Census. [src: enigma_carbon_census_1]

Known aliases and a stable external identifier were not reported in the source document. [src: enigma_carbon_census_1]

## Key facts from the document

PubChem was used to resolve the identities of all 83 enrichment compounds in the census to structures with InChIKeys. [src: enigma_carbon_census_1]

The 83 compounds comprised 59 compounds from SSO groundwater and 24 compounds from necromass. [src: enigma_carbon_census_1]

After PubChem-based structure resolution, 54 of the 83 compounds were linked to [[entities/kegg]]. [src: enigma_carbon_census_1]

PubChem formed the chemical-identity layer of a workflow that connected compound structures with pathway and enzyme annotations, ENIGMA-isolate utilization predictions, GTDB strain placement, SSO field occurrence, and global environmental abundance. [src: enigma_carbon_census_1]

This use of PubChem supports the broader [[concepts/cross-tenant-data-bridging]] workflow by providing a common compound-identity basis for integrating otherwise distinct resources. [src: enigma_carbon_census_1]

## Related pages

- [[summaries/enigma_carbon_census_1__REPORT]] — source summary for the ENIGMA Carbon Census. [src: enigma_carbon_census_1]
- [[entities/kegg]] — pathway and compound knowledge resource linked after structure resolution. [src: enigma_carbon_census_1]
- [[concepts/cross-tenant-data-bridging]] — cross-resource integration enabled by the census workflow. [src: enigma_carbon_census_1]
