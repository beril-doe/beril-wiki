---
type: "Concept"
description: "How often the available cross-tenant bridges are actually used by analysis projects, which are idle, and why use concentrates on a few tenants; stops at the design of new analyses."
sources: ["summaries/berdl_data_atlas__REPORT.md"]
---
# Realized versus theoretical cross-collection data reuse

This page covers realized versus theoretical cross-collection data reuse in the KBase Data Lakehouse. It asks how often available cross-tenant bridges are used, which sit idle, and why use concentrates on a few tenants. Most audited projects span tenants, but use is concentrated on one axis, and the audit method gives only a lower bound. [src: berdl_data_atlas] See also [[summaries/berdl_data_atlas__REPORT]].

## Literature Context

The candidate papers do not measure cross-collection reuse in a microbial data platform. They do show that reuse is a recognised problem in other biomedical fields, and that FAIR (Findable, Accessible, Interoperable, Reusable) principles are the usual response. Several papers describe work that makes data easier to find and combine. ImmuneData gives integrated discovery access to five immunology repositories by mapping their metadata into a uniform schema [PMID 35262674](https://pubmed.ncbi.nlm.nih.gov/35262674/). BRAinS-Graph links ClinicalTrials.gov, the Portal for Medical Data Models, UMLS and MeSH in one graph database to improve study findability. Its use cases illustrate its potential [PMID 42611793](https://pubmed.ncbi.nlm.nih.gov/42611793/). Immunemap addresses intravital microscopy data that remain siloed in individual labs [PMID 41266653](https://pubmed.ncbi.nlm.nih.gov/41266653/).

Other papers name barriers to reuse. Nutrition research lacks standardised terminologies and documentation, and the review calls for community standards [PMID 33494105](https://pubmed.ncbi.nlm.nih.gov/33494105/). Pooled analysis of nutritional epidemiology data needs study-quality descriptors for correct reuse [PMID 28916566](https://pubmed.ncbi.nlm.nih.gov/28916566/). Core facilities face variable formats and metadata that hinder cross-study integration [PMID 42847107](https://pubmed.ncbi.nlm.nih.gov/42847107/). The Clinical Research Informatics review says that data integration and semantic interoperability are making real-world data more reusable, and that governance remains an active research area [PMID 32823317](https://pubmed.ncbi.nlm.nih.gov/32823317/). A dental EHR study found poorly documented relational databases and no common schema. Its proof of concept used data from a single practice [PMID 32819435](https://pubmed.ncbi.nlm.nih.gov/32819435/).

Project Tycho is the closest precedent for measuring realized use. Its authors analyzed their user database and ran online searches. They report 3174 registered users, 18 new peer-reviewed papers and 27 other creative works from version 1 data [PMID 30321381](https://pubmed.ncbi.nlm.nih.gov/30321381/). That is an empirical count of downstream use for one repository. It does not compare realized use with possible links between collections.

The corpus's central finding is that 77% (51/66) of audited projects span multiple tenants, and that use concentrates on kbase × kescience. This sits alongside the literature's concern with discoverability and standardisation, but it is not tested by these papers. The literature supports the plausibility of the corpus's coordination-not-technology reading, because documentation and community standards recur as barriers. However, those papers are about other domains and do not test the corpus's explanations for concentration. The first overlay of realized use against 536 schema-level bridges, with five idle bridges flagged, appears novel relative to these candidates. Tycho counts use of a single repository, and the other papers propose infrastructure. The audit's README-based lower bound is the corpus's own caveat, and none of these papers supports or contradicts it. The corpus is therefore consistent with the field's emphasis on reuse barriers, and it extends that emphasis to an observed, bridge-level usage audit in a microbial data platform.

## How much cross-tenant use is realized

Most audited projects already combine tenants. 77% (51/66) of audited BERIL projects span multiple tenants. [src: berdl_data_atlas] The report reads this, together with 536 schema-level cross-tenant bridges, as evidence that the architecture delivers cross-program synergy. [src: berdl_data_atlas] That reading is the report's interpretation.

The report claims the first overlay of realized against theoretical bridges. It surfaces the 51 cross-tenant projects and flags unused high-leverage bridges. [src: berdl_data_atlas] The audit was README-based, so it may miss data-source mentions in research plans or notebooks. True per-project tenant breadth is therefore a lower bound. [src: berdl_data_atlas] See [[concepts/audit-blind-spots-in-inventories-of-data-and-its-use]].

## Where use concentrates

Realized use concentrates on one axis, kbase × kescience, with 36 projects. [src: berdl_data_atlas] These projects mostly join pangenome and fitness data through genome_id and ncbi_taxon_id. [src: berdl_data_atlas] The bridge builds on the FitnessBrowser pangenome cross-reference of Price et al. (2018). [src: berdl_data_atlas] See [[entities/fitness-browser]].

Tenant frequencies match this pattern. kbase appears in 53/66 projects (80%). [src: berdl_data_atlas] kescience appears in 35/66 (53%). [src: berdl_data_atlas]

The report offers two explanations for the concentration. They are the report's own accounts, and the cited quotes do not describe a test of them.
- The report attributes the dominance of the kbase × kescience axis to both tenants being intra-DOE-BER, well-documented, and covering the most cross-tenant topics (genome × phenotype). [src: berdl_data_atlas]
- The report calls DOE-BER the broad backbone: 63% of tables, every topic covered, and 80% of BERIL projects. [src: berdl_data_atlas] It identifies the concentration of DOE-BER biological references (KBase, KE Science, NMDC, ENIGMA, refdata) in one queryable space as the largest contributor to BERIL throughput. [src: berdl_data_atlas] See [[concepts/funding-agency-and-topic-coverage-of-a-shared-data-platform]].

## Tenants with many tables but few projects

For three tenants, table share and project count differ sharply. ENIGMA holds 36% of tables but appears in only 6 projects. [src: berdl_data_atlas] PhageFoundry holds 14% of tables and appears in 5 projects. [src: berdl_data_atlas] PROTECT holds 4% of tables and appears in 2 projects. [src: berdl_data_atlas] These are three tenants, not a general relationship between table share and use. The report says DOE BRaVE (PhageFoundry) and ARPA-H (PROTECT) are under-leveraged for cross-program work: each appears in fewer than 8 projects despite spanning relevant topics. [src: berdl_data_atlas] See [[entities/enigma]], [[entities/phagefoundry]] and [[entities/protect-genome-depot]].

The report treats ibd_phage_targeting and cf_formulation_design as existing bridge patterns. It calls scaling them a coordination problem, not a technical one. [src: berdl_data_atlas]

## Idle bridges

Five high-leverage bridges had zero realized use at audit time. The counts are shared keys per bridge.
- kescience ↔ refdata: 12 keys, including AlphaFold IDs (ID = identifier) [src: berdl_data_atlas]
- enigma ↔ phagefoundry: 11 keys [src: berdl_data_atlas]
- kbase ↔ refdata: 11 keys, including gtdb_taxonomy [src: berdl_data_atlas]
- nmdc ↔ protect: 10 keys [src: berdl_data_atlas]
- nmdc ↔ refdata: 9 keys [src: berdl_data_atlas]

Because the audit is a lower bound, these zeros mean no use was found by the README-based audit. [src: berdl_data_atlas] See [[concepts/untapped-cross-program-synergy-use-cases-for-environmental-and-clinical-microbiology]].

## Data products

The report supplies four tables. realized_use.csv has 66 rows of per-project tenant and database usage, with a cross_tenant flag and topic focus. [src: berdl_data_atlas] theoretical_vs_realized.csv has 72 rows overlaying shared keys and realized project counts for tenant pairs. [src: berdl_data_atlas] untapped_bridges.csv has 20 rows of the highest-leverage unrealized bridges, each with at least 1 shared key and 0 realized projects. [src: berdl_data_atlas] tenant_reuse_frequency.csv has 9 rows of per-tenant project counts and percentages. [src: berdl_data_atlas]

## Open Directions

- Re-run the audit on research plans and notebook source, not only READMEs. This would test whether the five zero-use bridges are truly idle, closing the lower-bound gap.
- Pilot one analysis per idle bridge, starting with kbase ↔ refdata through gtdb_taxonomy and kescience ↔ refdata through AlphaFold IDs. This would show whether the zeros reflect missing demand or missing awareness.
- Model projects per tenant against table share and documentation quality. This would test the report's explanations for concentration on kbase × kescience.
- Use the ibd_phage_targeting and cf_formulation_design patterns as templates for projects joining PhageFoundry or PROTECT to other tenants. This would test whether coordination, not technology, limits use.
