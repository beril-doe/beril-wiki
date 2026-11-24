---
type: "Concept"
description: "Undercounting and double-counting risks in table inventories and README-based usage audits, including unmapped tenants and missing deduplication; stops at remedies for specific projects."
sources: ["summaries/berdl_data_atlas__REPORT.md", "summaries/discoveries.md", "summaries/nmdc_context_audit__REPORT.md"]
---
# Audit blind spots in inventories of data and its use

Undercounting and double-counting risks in table inventories and README-based usage audits, including unmapped tenants and missing deduplication; stops at remedies for specific projects.

## Literature Context

The single candidate paper is a review of data management and sharing in experimental biomedical research. It is an abstract-only source, and it is not an audit of data inventories or of data reuse [PMID 38451234](https://pubmed.ncbi.nlm.nih.gov/38451234/). Its relevance is therefore general. It argues that well-organized and well-documented data are central to scientific integrity and reproducibility, and that data management covers organization, documentation, storage, sharing and preservation [PMID 38451234](https://pubmed.ncbi.nlm.nih.gov/38451234/). It also says that accurate documentation and extensive metadata matter, and that well-managed data can be revisited and contribute to cumulative knowledge [PMID 38451234](https://pubmed.ncbi.nlm.nih.gov/38451234/). The review adds that publicly funded research carries a responsibility for transparency, for resource allocation and for avoiding redundancy. It also notes that funding agencies increasingly expect standards, comprehensive documentation and wide sharing of data and code [PMID 38451234](https://pubmed.ncbi.nlm.nih.gov/38451234/).

The corpus findings fit this general framing but go beyond what the abstract reports. The review gives no evidence on undercounting or double-counting in catalog inventories. It says nothing about prefix-based grouping, duplicate catalog aliases or README-based usage audits. The corpus makes these points from its own project audits. NMDC-related databases (nmdc_arkin, nmdc_mags and nmdc_neon) sit in kbase and are invisible to anyone browsing the nmdc tenant. get_databases() returns both dotted and underscore aliases, so results must be deduplicated. The BERDL Data Atlas (berdl_data_atlas) does not deduplicate across tenants, and its README-based tenant breadth is a lower bound. These are novel, project-specific observations. The literature candidate does not support or contradict them.

The review's emphasis on documentation, metadata and avoiding redundancy is consistent with the corpus's concern with mapping tenants to agencies. The evaluation and lambda tenants (4 tables total) remain unmapped, and their mappings are not yet verified by program documentation. It is also consistent with the concern about overlapping records, such as UniProt entries held in both refdata and kbase. The link is only conceptual, because the review is a general best-practice summary and does not measure audit blind spots. The open directions on the hub page, including scanning research plans and notebooks, using COUNT(DISTINCT) on entity keys and testing value-space overlap beyond UC1, therefore rest on the corpus's own evidence. See [[concepts/realized-versus-theoretical-cross-collection-data-reuse]] and [[concepts/join-key-validity-and-identifier-format-mismatches]].

## Undercounting

Static or prefix-based inventories can hide data. Historical static inventory files lagged the live catalog and omitted several databases relevant to gut-microbiome and phage work. [src: discoveries]

Grouping by catalog prefix hides related databases. Three NMDC-related databases (nmdc_arkin, nmdc_mags and nmdc_neon) live in kbase, outside the nmdc tenant. Because the inventory groups by catalog prefix, they are filed under "kbase" and are invisible to anyone browsing the nmdc tenant. [src: nmdc_context_audit] The berdl_inventory.py tool groups purely by catalog prefix and never links kbase.nmdc_* back to NMDC. [src: nmdc_context_audit]

Tenant-to-agency mapping can also be incomplete. The evaluation and lambda tenants (4 tables total) remain unmapped to agencies, and the report says their mappings are not yet verified by program documentation. [src: berdl_data_atlas] User-confirmed corrections assign phagefoundry to DOE BRaVE and msyscolo to DOE/NSF. They replace initial inferences of likely Defense/HHS and NSF/USDA (National Science Foundation/USDA). [src: berdl_data_atlas] The unclassified residual is small, at 0.9% (16 rows), all personal scratch or one-off survey data. [src: berdl_data_atlas] See [[concepts/funding-agency-and-topic-coverage-of-a-shared-data-platform]] and [[entities/phagefoundry]].

The README-based realized-use audit may miss data-source mentions buried in research plans or notebooks. Reported per-project tenant breadth is therefore a lower bound. [src: berdl_data_atlas] See [[concepts/realized-versus-theoretical-cross-collection-data-reuse]].

## Double-counting

The catalog listing itself can inflate counts. get_databases() returns both the dotted Iceberg alias (nmdc.metadata) and the underscore Hive alias (nmdc_metadata) for every tenant database. Results must be deduplicated to the dotted form before iterating. [src: nmdc_context_audit] The atlas audit notebook does this for dotted-namespace duplicates when it tags tables by tenant, agency and topic. [src: berdl_data_atlas]

The atlas depth counts use COUNT(*) row totals for most tables. Only the canonical KBase genome count uses COUNT(DISTINCT genome_id). [src: berdl_data_atlas] See [[concepts/entity-class-depth-and-data-volume-of-a-biological-data-platform]].

The atlas does not deduplicate across tenants. [src: berdl_data_atlas] refdata and kbase may hold the same UniProt entries through different cluster indices. ENIGMA and the genome-depot tables share genome records with the ENIGMA SDT layer. [src: berdl_data_atlas]

## Schema versus value validity

The bridge atlas shows that the schema admits a join, not that values overlap. Value-space validity is established only for UC1 (use case 1). [src: berdl_data_atlas] See [[concepts/join-key-validity-and-identifier-format-mismatches]].

## Open Directions

- Verify the evaluation and lambda tenant-to-agency mappings against program documentation, to close the 4-table gap.
- Scan research plans and notebook source, not only READMEs, for data-source mentions. This would turn the lower bound on tenant breadth into a measured value.
- Recompute depth counts with COUNT(DISTINCT) on the entity key, to compare rows with entities.
- Compare UniProt entries across refdata and kbase, and genome records across ENIGMA and genome-depot, to size the cross-tenant overlap.
- Group the inventory by database-name family as well as catalog prefix, so that nmdc_* databases in kbase link back to NMDC.
- Test value-space overlap for joins beyond UC1.
