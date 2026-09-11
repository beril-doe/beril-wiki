---
type: "Concept"
description: "How ownership, tenancy, and integration practices bias biological data coverage"
sources: ["summaries/berdl_data_atlas__REPORT.md", "summaries/pitfalls.md"]
---
# Agency and Tenant Ownership Shape Biological Data Coverage

The [[summaries/berdl_data_atlas__REPORT]] shows that biological data availability in the KBase Data Lakehouse is structured not only by scientific topic but also by ownership, tenant boundaries, and the uneven reuse of cross-tenant links. [src: berdl_data_atlas] The atlas inventories 1,740 deduplicated tables across 119 databases, 17 tenants, and 10 funding agencies or programs, covering 17 biological topics. [src: berdl_data_atlas]

## Ownership concentration produces coverage bias

DOE accounts for approximately 78% of the KBase Data Lakehouse tables: DOE-BER contributes 63%, DOE BRaVE 14%, DOE/NSF 0.6%, and DOE-FE 0.4%; ARPA-H contributes 4% and NSF contributes 3.5%. [src: berdl_data_atlas] DOE-BER is the only agency covering all 15 biological topics recorded in the agency-coverage analysis. [src: berdl_data_atlas] Six topics are more than 75% single-owner, including mobile_phage at 96% PhageFoundry ownership and pangenome at 79% KBase ownership. [src: berdl_data_atlas]

This ownership pattern means that apparent topic availability can reflect the location and funding history of data rather than a balanced distribution of independent observations. [src: berdl_data_atlas] The field_observational topic represents 40% of tables, mobile_phage 14%, fitness_phenotype 11%, and genome 6.4%, while all other primary topics represent less than 4% each. [src: berdl_data_atlas] Sixteen tables, or 0.9%, remain unclassified and consist of personal scratch or one-off survey data. [src: berdl_data_atlas]

The [[summaries/pitfalls]] **supports** treating ownership and provenance as coverage variables: 83,227 of 293,059 genomes, or 28.4%, have AlphaEarth environmental embeddings, while 52.7% of 180,025 genomes have unknown per-genome NCBI environment labels. [src: pitfalls] These gaps can reflect missing coordinates or unstructured metadata rather than biological absence, so owner- and tenant-specific coverage should not be interpreted as population absence. [src: pitfalls]

## Tenant breadth is uneven

Taxonomy spans 12 tenants and has the broadest cross-tenant surface, whereas several other topics are concentrated within individual tenants. [src: berdl_data_atlas] KBase covers 10 topics with entropy 2.87 and is described as the most evenly cross-topic tenant; NMDC covers 11 topics with entropy 2.61; PROTECT covers 6 topics with entropy 2.37; KEScience covers 11 topics with entropy 1.83; and ENIGMA covers 5 topics with entropy 0.43. [src: berdl_data_atlas]

These distributions support a distinction between data volume and portfolio breadth: a tenant may contain many tables while still being concentrated in a small number of topics. [src: berdl_data_atlas] ENIGMA contains 36% of tables but appears in 6 audited projects, while PhageFoundry contains 14% of tables but appears in 5 projects and PROTECT contains 4% but appears in 2 projects. [src: berdl_data_atlas]

The pitfalls evidence **refines** this distinction by showing that tenant ownership is also operational: KBase Data Lakehouse’s migration between Delta and Iceberg changes live table addresses, and the `data_lakehouse_ingest` name is a governance-group tenant rather than a database prefix. [src: pitfalls] Queries must therefore discover the live catalog and resolve tenant and database names before comparing apparent breadth or concluding that a resource is unavailable. [src: pitfalls]

## Ownership affects realized integration

Among 66 audited BERIL projects, 51, or 77%, span multiple tenants. [src: berdl_data_atlas] KBase appears in 53/66 projects, or 80%, and KEScience appears in 35/66, or 53%. [src: berdl_data_atlas] The realized kbase × kescience bridge accounts for 36 cross-tenant projects, mostly pangenome-by-fitness joins through genome_id and ncbi_taxon_id. [src: berdl_data_atlas]

This realized-use pattern supports [[concepts/cross-tenant-data-bridging]]: ownership boundaries do not prevent integration when shared identifiers and operational demand connect tenants, but they can make some scientific combinations more visible than others. [src: berdl_data_atlas] The atlas identifies 536 unordered cross-tenant bridges at tenant-by-topic-cell granularity from 29 canonical join keys, but only UC1 was sample-validated in the study. [src: berdl_data_atlas]

The pitfalls document **supports** the need for that value-space validation: in one pangenome linkage example, 12 of 32 joins through `ncbi_strain_identifiers` were incorrect genus matches, including an MT20 collision between *Rhodanobacter glycinis* and *Streptococcus pneumoniae*. [src: pitfalls] It also **refines** the bridge audit by showing that NMDC classifier and metabolomics `file_id` namespaces do not overlap and require a `sample_id` bridge through `omics_files_table`. [src: pitfalls]

The contrast between possible and realized integration also refines [[concepts/cross-tenant-data-bridging]]: five high-leverage bridges had zero realized use at audit time, including proposed links between ENIGMA and PhageFoundry, NMDC and PROTECT, and NMDC and refdata. [src: berdl_data_atlas] Schema-level compatibility does not establish value-space overlap because identifiers such as genome_id can represent different identifier systems in KBase, NCBI, and MAG pipelines. [src: berdl_data_atlas]

## Implications for biological inference

Ownership concentration should be treated as a coverage-bias variable when comparing topics, tenants, agencies, or biological systems. [src: berdl_data_atlas] In particular, the 79% KBase ownership of pangenome data and 96% PhageFoundry ownership of mobile_phage data indicate that conclusions about these topics may be strongly coupled to the methods, sampling frames, and curation practices of their dominant owners. [src: berdl_data_atlas]

The atlas therefore supports [[concepts/data-landscape-ownership-and-coverage-bias]] as a provenance-aware complement to [[concepts/pangenome-integration]] and [[concepts/provenance-aware-resource-discovery]]. [src: berdl_data_atlas] Data discovery should record both the biological topic and the tenant or agency distribution, while cross-tenant analyses should validate identifier value spaces before interpreting apparent coverage or association patterns. [src: berdl_data_atlas] The pitfalls evidence **supports** this workflow requirement because archived SQL may use obsolete namespace forms, large tables require live schema inspection and key-filtered joins, and missing metadata or failed joins can produce incomplete coverage without indicating biological absence. [src: pitfalls]

## Boundary conditions

The realized-use audit mined project README files, so data-source mentions in research plans or notebook source may have been missed and the reported tenant breadth is therefore a lower bound. [src: berdl_data_atlas] Two tenant-to-agency mappings, evaluation and lambda, remain unverified by program documentation and account for 4 tables total. [src: berdl_data_atlas] Across-tenant deduplication was not performed, so apparent inventory differences may include duplicated records across refdata, KBase, ENIGMA, and genome-depot layers. [src: berdl_data_atlas]

The pitfalls document **refines** these boundaries by warning that schemas, namespace availability, permissions, API behavior, and naming conventions can change; archived reports and notebooks are historical records rather than automatically valid executable instructions. [src: pitfalls]

## Open Directions

- Re-audit all 66 BERIL projects using README files, notebooks, research plans, and workflow metadata to test whether the observed tenant breadth remains a lower bound and whether underused owners contribute more realized data sources than reported. [src: berdl_data_atlas]
- Recompute agency and tenant concentration after deduplicating shared records across refdata, KBase, ENIGMA, and genome-depot layers to determine how much of the apparent ownership imbalance reflects duplicated inventory. [src: berdl_data_atlas]
- Execute UC2–UC5 with value-space validation for their proposed join keys to test whether ownership-separated datasets provide usable biological coverage rather than only schema-level bridges. [src: berdl_data_atlas]
- Compare topic-level scientific conclusions with and without tenant or agency-stratified sampling to measure whether dominant owners alter observed associations, taxonomic coverage, or phenotype distributions. [src: berdl_data_atlas]
- Verify the evaluation and lambda agency mappings against program documentation and assess whether correcting the 4 affected tables changes agency concentration estimates. [src: berdl_data_atlas]
- Recalculate coverage and cross-tenant bridge rates after live catalog discovery, explicit identifier reconciliation, and filtering of missing environmental metadata to distinguish ownership effects from namespace, metadata, and join failures. [src: pitfalls]
