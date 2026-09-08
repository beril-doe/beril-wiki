---
type: Concept
description: How ownership, tenancy, and integration practices bias biological data
  coverage
sources:
- id: berdl_data_atlas
  resource: ../summaries/berdl_data_atlas__REPORT.md
  title: berdl data atlas
- id: pitfalls
  resource: ../summaries/pitfalls.md
  title: pitfalls
title: Agency and Tenant Ownership Shape Biological Data Coverage
---
# Agency and Tenant Ownership Shape Biological Data Coverage

The [berdl_data_atlas__REPORT](../summaries/berdl_data_atlas__REPORT.md) shows that biological data availability in BERDL is structured not only by scientific topic but also by ownership, tenant boundaries, and the uneven reuse of cross-tenant links. [^berdl_data_atlas] The atlas inventories 1,740 deduplicated tables across 119 databases, 17 tenants, and 10 funding agencies or programs, covering 17 biological topics. [^berdl_data_atlas]

## Ownership concentration produces coverage bias

DOE accounts for approximately 78% of BERDL tables: DOE-BER contributes 63%, DOE BRaVE 14%, DOE/NSF 0.6%, and DOE-FE 0.4%; ARPA-H contributes 4% and NSF contributes 3.5%. [^berdl_data_atlas] DOE-BER is the only agency covering all 15 biological topics recorded in the agency-coverage analysis. [^berdl_data_atlas] Six topics are more than 75% single-owner, including mobile_phage at 96% PhageFoundry ownership and pangenome at 79% KBase ownership. [^berdl_data_atlas]

This ownership pattern means that apparent topic availability can reflect the location and funding history of data rather than a balanced distribution of independent observations. [^berdl_data_atlas] The field_observational topic represents 40% of tables, mobile_phage 14%, fitness_phenotype 11%, and genome 6.4%, while all other primary topics represent less than 4% each. [^berdl_data_atlas] Sixteen tables, or 0.9%, remain unclassified and consist of personal scratch or one-off survey data. [^berdl_data_atlas]

The [pitfalls](../summaries/pitfalls.md) **supports** treating ownership and provenance as coverage variables: 83,227 of 293,059 genomes, or 28.4%, have AlphaEarth environmental embeddings, while 52.7% of 180,025 genomes have unknown per-genome NCBI environment labels. [^pitfalls] These gaps can reflect missing coordinates or unstructured metadata rather than biological absence, so owner- and tenant-specific coverage should not be interpreted as population absence. [^pitfalls]

## Tenant breadth is uneven

Taxonomy spans 12 tenants and has the broadest cross-tenant surface, whereas several other topics are concentrated within individual tenants. [^berdl_data_atlas] KBase covers 10 topics with entropy 2.87 and is described as the most evenly cross-topic tenant; NMDC covers 11 topics with entropy 2.61; PROTECT covers 6 topics with entropy 2.37; KEScience covers 11 topics with entropy 1.83; and ENIGMA covers 5 topics with entropy 0.43. [^berdl_data_atlas]

These distributions support a distinction between data volume and portfolio breadth: a tenant may contain many tables while still being concentrated in a small number of topics. [^berdl_data_atlas] ENIGMA contains 36% of tables but appears in 6 audited projects, while PhageFoundry contains 14% of tables but appears in 5 projects and PROTECT contains 4% but appears in 2 projects. [^berdl_data_atlas]

The pitfalls evidence **refines** this distinction by showing that tenant ownership is also operational: BERDL’s migration between Delta and Iceberg changes live table addresses, and the `data_lakehouse_ingest` name is a governance-group tenant rather than a database prefix. [^pitfalls] Queries must therefore discover the live catalog and resolve tenant and database names before comparing apparent breadth or concluding that a resource is unavailable. [^pitfalls]

## Ownership affects realized integration

Among 66 audited BERIL projects, 51, or 77%, span multiple tenants. [^berdl_data_atlas] KBase appears in 53/66 projects, or 80%, and KEScience appears in 35/66, or 53%. [^berdl_data_atlas] The realized kbase × kescience bridge accounts for 36 cross-tenant projects, mostly pangenome-by-fitness joins through genome_id and ncbi_taxon_id. [^berdl_data_atlas]

This realized-use pattern supports [cross-tenant-data-bridging](cross-tenant-data-bridging.md): ownership boundaries do not prevent integration when shared identifiers and operational demand connect tenants, but they can make some scientific combinations more visible than others. [^berdl_data_atlas] The atlas identifies 536 unordered cross-tenant bridges at tenant-by-topic-cell granularity from 29 canonical join keys, but only UC1 was sample-validated in the study. [^berdl_data_atlas]

The pitfalls document **supports** the need for that value-space validation: in one pangenome linkage example, 12 of 32 joins through `ncbi_strain_identifiers` were incorrect genus matches, including an MT20 collision between *Rhodanobacter glycinis* and *Streptococcus pneumoniae*. [^pitfalls] It also **refines** the bridge audit by showing that NMDC classifier and metabolomics `file_id` namespaces do not overlap and require a `sample_id` bridge through `omics_files_table`. [^pitfalls]

The contrast between possible and realized integration also refines [cross-tenant-data-bridging](cross-tenant-data-bridging.md): five high-leverage bridges had zero realized use at audit time, including proposed links between ENIGMA and PhageFoundry, NMDC and PROTECT, and NMDC and refdata. [^berdl_data_atlas] Schema-level compatibility does not establish value-space overlap because identifiers such as genome_id can represent different identifier systems in KBase, NCBI, and MAG pipelines. [^berdl_data_atlas]

## Implications for biological inference

Ownership concentration should be treated as a coverage-bias variable when comparing topics, tenants, agencies, or biological systems. [^berdl_data_atlas] In particular, the 79% KBase ownership of pangenome data and 96% PhageFoundry ownership of mobile_phage data indicate that conclusions about these topics may be strongly coupled to the methods, sampling frames, and curation practices of their dominant owners. [^berdl_data_atlas]

The atlas therefore supports [data-landscape-ownership-and-coverage-bias](data-landscape-ownership-and-coverage-bias.md) as a provenance-aware complement to [pangenome-integration](pangenome-integration.md) and [provenance-aware-resource-discovery](provenance-aware-resource-discovery.md). [^berdl_data_atlas] Data discovery should record both the biological topic and the tenant or agency distribution, while cross-tenant analyses should validate identifier value spaces before interpreting apparent coverage or association patterns. [^berdl_data_atlas] The pitfalls evidence **supports** this workflow requirement because archived SQL may use obsolete namespace forms, large tables require live schema inspection and key-filtered joins, and missing metadata or failed joins can produce incomplete coverage without indicating biological absence. [^pitfalls]

## Boundary conditions

The realized-use audit mined project README files, so data-source mentions in research plans or notebook source may have been missed and the reported tenant breadth is therefore a lower bound. [^berdl_data_atlas] Two tenant-to-agency mappings, evaluation and lambda, remain unverified by program documentation and account for 4 tables total. [^berdl_data_atlas] Across-tenant deduplication was not performed, so apparent inventory differences may include duplicated records across refdata, KBase, ENIGMA, and genome-depot layers. [^berdl_data_atlas]

The pitfalls document **refines** these boundaries by warning that schemas, namespace availability, permissions, API behavior, and naming conventions can change; archived reports and notebooks are historical records rather than automatically valid executable instructions. [^pitfalls]

## Open Directions

- Re-audit all 66 BERIL projects using README files, notebooks, research plans, and workflow metadata to test whether the observed tenant breadth remains a lower bound and whether underused owners contribute more realized data sources than reported. [^berdl_data_atlas]
- Recompute agency and tenant concentration after deduplicating shared records across refdata, KBase, ENIGMA, and genome-depot layers to determine how much of the apparent ownership imbalance reflects duplicated inventory. [^berdl_data_atlas]
- Execute UC2–UC5 with value-space validation for their proposed join keys to test whether ownership-separated datasets provide usable biological coverage rather than only schema-level bridges. [^berdl_data_atlas]
- Compare topic-level scientific conclusions with and without tenant or agency-stratified sampling to measure whether dominant owners alter observed associations, taxonomic coverage, or phenotype distributions. [^berdl_data_atlas]
- Verify the evaluation and lambda agency mappings against program documentation and assess whether correcting the 4 affected tables changes agency concentration estimates. [^berdl_data_atlas]
- Recalculate coverage and cross-tenant bridge rates after live catalog discovery, explicit identifier reconciliation, and filtering of missing environmental metadata to distinguish ownership effects from namespace, metadata, and join failures. [^pitfalls]

[^berdl_data_atlas]: [berdl data atlas](../summaries/berdl_data_atlas__REPORT.md)
[^pitfalls]: [pitfalls](../summaries/pitfalls.md)
