---
type: "Concept"
description: "README-based audits undercount actual cross-tenant data reuse."
sources: ["summaries/berdl_data_atlas__REPORT.md"]
---
# Project Documentation Makes Reported Data Reuse a Lower Bound

Reported data reuse in the BERDL corpus is partly an observability problem: an audit can only count a data source when project documentation exposes it. The [[summaries/berdl_data_atlas__REPORT]] audit mined project README files, so mentions located only in research plans or notebook source may have been missed; consequently, reported tenant breadth and cross-tenant reuse are lower bounds rather than complete measurements. [src: berdl_data_atlas]

## Evidence

The atlas audited 66 BERIL projects and found that 51, or 77%, spanned multiple tenants. [src: berdl_data_atlas] Because the audit relied on README files, this 51-project count and the associated 77% estimate should be interpreted as documented cross-tenant use, not as the total amount of reuse actually conducted. [src: berdl_data_atlas]

KBase appeared in 53 of 66 projects, or 80%, while KEScience appeared in 35 of 66 projects, or 53%. [src: berdl_data_atlas] The realized kbase × kescience bridge accounted for 36 cross-tenant projects, mostly pangenome-by-fitness joins through genome_id and ncbi_taxon_id. [src: berdl_data_atlas] These counts establish a documented-use baseline for [[concepts/cross-tenant-data-bridging]], but they cannot determine how many additional projects used those tenants or joins without recording the relevant activity outside README files. [src: berdl_data_atlas]

The same visibility limitation affects comparisons between data availability and use. [src: berdl_data_atlas] ENIGMA contained 36% of BERDL tables but appeared in 6 projects, while PhageFoundry contained 14% of tables but appeared in 5 projects and PROTECT contained 4% but appeared in 2 projects. [src: berdl_data_atlas] These ratios may reflect genuine differences in research use, incomplete documentation, or both; the audit does not distinguish those explanations. [src: berdl_data_atlas]

The atlas also identified five high-leverage bridges with zero realized use at audit time: UC1 kescience ↔ refdata, UC2 enigma ↔ phagefoundry, UC3 kbase ↔ refdata, UC4 nmdc ↔ protect, and UC5 nmdc ↔ refdata. [src: berdl_data_atlas] “Zero realized use” means zero use was found in the audited project documentation, not that no researcher had used the bridges in unobserved notebooks, plans, or other materials. [src: berdl_data_atlas] UC1 was the only one of the five bridges validated by live-cluster execution; UC2–UC5 still require live-cluster execution. [src: berdl_data_atlas]

## Interpretation

This finding **refines** [[concepts/potential-versus-realized-data-integration]] by separating three states: data and schema compatibility, documented project use, and technically validated value-space overlap. [src: berdl_data_atlas] The atlas identified 536 unordered cross-tenant bridges at tenant-by-topic-cell granularity, but schema-level compatibility does not establish value-space overlap. [src: berdl_data_atlas] Thus, a bridge may be technically possible yet undocumented, documented yet unvalidated, or validated through an executed join. [src: berdl_data_atlas]

The finding also **supports** [[concepts/provenance-aware-resource-discovery]]: reliable reuse discovery requires provenance records that capture notebooks, research plans, executed queries, and other artifacts in addition to README descriptions. [src: berdl_data_atlas] Without those records, the apparent distribution of tenant use can be biased toward projects with more complete or more standardized documentation. [src: berdl_data_atlas]

## Measurement Implications

README mining is useful for producing a reproducible lower-bound inventory, but it should not be treated as a census of data reuse. [src: berdl_data_atlas] A stronger reuse estimate would combine project documentation with notebook and query histories, then deduplicate evidence at the project–tenant–dataset and project–bridge levels. [src: berdl_data_atlas] The comparison should preserve the original README-derived counts so that newly discovered reuse can be distinguished from changes in the underlying research activity. [src: berdl_data_atlas]

The distinction is especially important for high-volume or highly centralized resources. [src: berdl_data_atlas] DOE-BER accounted for 63% of BERDL tables, KBase appeared in 53 of 66 audited projects, and KEScience appeared in 35 of 66 projects. [src: berdl_data_atlas] Documentation gaps could therefore alter both apparent tenant centrality and conclusions about which bridges are most actively used. [src: berdl_data_atlas]

## Open Directions

- Combine README files, research plans, notebook source, and query logs, then ask how many additional project–tenant and project–bridge uses are recovered beyond the documented baseline of 51 of 66 multi-tenant projects. [src: berdl_data_atlas]
- Execute UC2–UC5 on the live cluster and compare validated value-space overlap with the README-derived finding of zero realized use, asking whether the bridges are unused, undocumented, or merely unvalidated. [src: berdl_data_atlas]
- Build a provenance-aware project–dataset graph from project artifacts and deduplicate records by project, tenant, dataset, and canonical join key, asking whether tenant-use rankings change from the README audit. [src: berdl_data_atlas]
- Audit notebook and query artifacts for the 36 documented kbase × kescience projects, asking whether their pangenome-by-fitness joins are reproducible and whether additional join keys beyond genome_id and ncbi_taxon_id were used. [src: berdl_data_atlas]
