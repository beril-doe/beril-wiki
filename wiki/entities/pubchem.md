---
type: Dataset
description: Chemical-identity database used to resolve all 83 census compounds
sources:
- id: enigma_carbon_census_1
  resource: ../summaries/enigma_carbon_census_1__REPORT.md
  title: enigma carbon census 1
title: PubChem
---
# PubChem

## What this entity is

PubChem is the canonical name of a chemical-structure and compound-identity dataset used in the ENIGMA Carbon Census. [^enigma_carbon_census_1]

Known aliases and a stable external identifier were not reported in the source document. [^enigma_carbon_census_1]

## Key facts from the document

PubChem was used to resolve the identities of all 83 enrichment compounds in the census to structures with InChIKeys. [^enigma_carbon_census_1]

The 83 compounds comprised 59 compounds from SSO groundwater and 24 compounds from necromass. [^enigma_carbon_census_1]

After PubChem-based structure resolution, 54 of the 83 compounds were linked to [kegg](kegg.md). [^enigma_carbon_census_1]

PubChem formed the chemical-identity layer of a workflow that connected compound structures with pathway and enzyme annotations, ENIGMA-isolate utilization predictions, GTDB strain placement, SSO field occurrence, and global environmental abundance. [^enigma_carbon_census_1]

This use of PubChem supports the broader [cross-tenant-data-bridging](../concepts/cross-tenant-data-bridging.md) workflow by providing a common compound-identity basis for integrating otherwise distinct resources. [^enigma_carbon_census_1]

## Related pages

- [enigma_carbon_census_1__REPORT](../summaries/enigma_carbon_census_1__REPORT.md) — source summary for the ENIGMA Carbon Census. [^enigma_carbon_census_1]
- [kegg](kegg.md) — pathway and compound knowledge resource linked after structure resolution. [^enigma_carbon_census_1]
- [cross-tenant-data-bridging](../concepts/cross-tenant-data-bridging.md) — cross-resource integration enabled by the census workflow. [^enigma_carbon_census_1]

[^enigma_carbon_census_1]: [enigma carbon census 1](../summaries/enigma_carbon_census_1__REPORT.md)
