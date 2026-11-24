---
type: "Concept"
description: "How tables in a multi-tenant data lakehouse distribute across funding agencies, tenants and biological topics, including ownership concentration and breadth versus depth; stops at project-level usage."
sources: ["summaries/berdl_data_atlas__REPORT.md"]
---
# Funding-agency and topic coverage of a shared data platform

The KBase Data Lakehouse inventory holds 1,740 deduplicated tables across 119 databases, 17 tenants and 10 funding agencies or programs, spanning 17 biological topics. [src: berdl_data_atlas] Ownership is concentrated: DOE-BER supplies most tables and covers every topic, while small agencies hold few tables but distinctive samples. [src: berdl_data_atlas] All figures come from one report, the [[summaries/berdl_data_atlas__REPORT|berdl_data_atlas summary]], which counts tables and stops short of project-level usage. See also [[entities/kbase-data-lakehouse]].

## Funding agencies

DOE dominates: about 78% of tables, made up of DOE-BER 63%, DOE BRaVE 14%, DOE/NSF 0.6% and DOE-FE 0.4%. [src: berdl_data_atlas] The report calls DOE-BER the broad backbone, with 63% of tables, every topic covered and 80% of BERIL projects. [src: berdl_data_atlas] It spans 15 of 15 biological topics. [src: berdl_data_atlas]

Outside DOE, ARPA-H (PROTECT) contributes 4% of tables [src: berdl_data_atlas] and NSF (Planet Microbe) 3.5%. [src: berdl_data_atlas] DOI (USGS) and the academic, multi and user namespaces fill the rest. [src: berdl_data_atlas] ARPA-H (PROTECT) spans 6 topics. [src: berdl_data_atlas] See [[entities/phagefoundry]] and [[entities/protect-genome-depot]].

The report's topic map labels a Defense / HHS agency group as mono-topic, represented by PhageFoundry entirely in mobile_phage. [src: berdl_data_atlas] That label reflects the earlier inference. User-confirmed corrections now assign phagefoundry to DOE BRaVE. [src: berdl_data_atlas] The mono-topic finding therefore describes PhageFoundry itself, not a separate agency.

NSF (Planet Microbe), DOE-FE (NETL) and DOI (USGS) are narrow in topic but cover unique sample types. [src: berdl_data_atlas] The report proposes them as external validation sets for DOE-BER-anchored analyses, because their small collections have unique open-ocean and produced-water provenance. [src: berdl_data_atlas] See [[entities/planet-microbe]].

## Topics

Table counts are skewed toward a few topics. field_observational is 40% of tables, dominated by ENIGMA SDT/DDT structure. [src: berdl_data_atlas] mobile_phage is 14% (PhageFoundry) [src: berdl_data_atlas], fitness_phenotype 11% [src: berdl_data_atlas] and genome 6.4%. [src: berdl_data_atlas] Every other topic is under 4%. [src: berdl_data_atlas] The unclassified residual is 0.9% (16 rows), all personal scratch or one-off survey data. [src: berdl_data_atlas] See [[entities/enigma]].

## Ownership concentration

Six topics are more than 75% single-owner. [src: berdl_data_atlas] PhageFoundry owns 96% of mobile_phage [src: berdl_data_atlas], kbase owns 79% of pangenome [src: berdl_data_atlas] and refdata owns 78% of reference_protein. [src: berdl_data_atlas] By contrast, 7 topics are cross-tenant, with a top-tenant share of 55% or less. [src: berdl_data_atlas] Taxonomy spans 12 tenants and is the broadest cross-tenant surface. [src: berdl_data_atlas] See [[entities/kbase-ke-pangenome]].

## Breadth versus depth by tenant

The report scores tenants by number of topics and by entropy. It defines per-tenant synergy capacity as distinct topics × entropy. [src: berdl_data_atlas] It calls kbase the most evenly cross-topic tenant, which fits its highest entropy of 2.87. [src: berdl_data_atlas]

| Tenant | Topics | Entropy | Report's description |
|---|---|---|---|
| kbase | 10 | 2.87 | most evenly cross-topic; biological reference hub [src: berdl_data_atlas] |
| nmdc | 11 | 2.61 | broadest coverage [src: berdl_data_atlas] |
| protect | 6 | 2.37 | punches above its size [src: berdl_data_atlas] |
| kescience | 11 | 1.83 | knowledge-engine layer [src: berdl_data_atlas] |
| enigma | 5 | 0.43 | deep-but-narrow [src: berdl_data_atlas] |

The phagefoundry and usgs tenants are mono-topic. [src: berdl_data_atlas] See [[entities/nmdc-integrated-collections]].

## Caveats

The evaluation and lambda tenants, 4 tables in total, remain unmapped to agencies and need verification against program documentation. [src: berdl_data_atlas] User-confirmed corrections assign phagefoundry to DOE BRaVE and msyscolo to DOE/NSF. They replace earlier inferences of Defense/HHS and NSF/USDA. [src: berdl_data_atlas] The report presents its catalog as the first comprehensive machine-readable one with tenant, agency, program and topic provenance. [src: berdl_data_atlas] These counts describe table inventory, not use; see [[concepts/audit-blind-spots-in-inventories-of-data-and-its-use]] and [[concepts/realized-versus-theoretical-cross-collection-data-reuse]].

## Open Directions

- Verify the evaluation and lambda tenant-to-agency mappings against program documentation. This would close the only unmapped gap.
- Re-run the agency × topic analysis weighting by rows or data volume rather than table count. This would test whether ENIGMA SDT/DDT structure inflates field_observational.
- Run a DOE-BER-anchored analysis and validate it on Planet Microbe, NETL and USGS samples. This would test the proposed external-validation role.
- Compare the tenant synergy scores with actual cross-tenant queries. This would test whether high-entropy tenants are used more broadly.
