---
type: Other
description: National Microbiome Data Collaborative dataset ecosystem and provenance
  authority
sources:
- id: nmdc_context_audit
  resource: ../summaries/nmdc_context_audit__REPORT.md
  title: nmdc context audit
- id: phb_granule_ecology
  resource: ../summaries/phb_granule_ecology__REPORT.md
  title: phb granule ecology
- id: prophage_ecology
  resource: ../summaries/prophage_ecology__REPORT.md
  title: prophage ecology
title: National Microbiome Data Collaborative authority and data ecosystem
---
# National Microbiome Data Collaborative authority and data ecosystem

## What this entity is

**Canonical name:** National Microbiome Data Collaborative (NMDC). [^nmdc_context_audit]

**Known alias:** NMDC. [^nmdc_context_audit]

**Stable external identifier:** None was reported in this audit. [^nmdc_context_audit]

The National Microbiome Data Collaborative is a DOE-BER authority associated with a heterogeneous data ecosystem that includes canonical NMDC resources, derivatives, external re-hosts, and a namesake collision with NEON. [^nmdc_context_audit]

Related resources include [nmdc-metadata](nmdc-metadata.md), [nmdc-results](nmdc-results.md), nmdc.ncbi_biosamples, [nmdc-mags](nmdc-mags.md), [nmdc-arkin](nmdc-arkin.md), and kbase.nmdc_neon.

## Key facts from the context audit

The audit resolved 20 NMDC-named database entries to 7 real, maintained resources spanning three tenants and six provenance classes. [^nmdc_context_audit]

The seven maintained resources include genuine NMDC resources, an NCBI BioSample re-host, a Pfam re-host, an Arkin Lab derivative, an NMDC-derived KBase resource, and a namesake resource representing the National Ecological Observatory Network rather than NMDC. [^nmdc_context_audit]

The `nmdc` tenant is not exclusively NMDC: `nmdc.ncbi_biosamples` contains an NCBI BioSample harvest with 51,711,888 biosamples and 756,112,544 attribute rows, while `nmdc.ref_data` contains 27,481 Pfam terms. [^nmdc_context_audit]

The canonical NMDC biosample universe contains 16,640 samples in `nmdc.metadata.biosample_set`, compared with 51,711,888 biosamples in the co-hosted NCBI mirror, creating an approximately 3,000× scale trap for resource selection. [^nmdc_context_audit]

The freshest NMDC-related resource identified by the audit is [nmdc-mags](nmdc-mags.md), with 62,346 metagenome-assembled genomes (MAGs), although it is located in the `kbase` tenant rather than the `nmdc` tenant. [^nmdc_context_audit]

Iceberg snapshot ages span approximately four months across NMDC-labeled resources: the latest commits were `2026-07-02` for `kbase.nmdc_mags` and `kbase.nmdc_neon`, `2026-05-27` for `kbase.nmdc_arkin`, `2026-05-20` for `nmdc.metadata`, `nmdc.results`, and `nmdc.ref_data`, and `2026-03-09` for `nmdc.ncbi_biosamples`. [^nmdc_context_audit]

The report recommends exposing `max(committed_at)` in discovery tooling because catalog tables have no comments, databases have empty properties, and no changelog exposes resource currency. [^nmdc_context_audit]

The NMDC data model is LinkML-based and defines the `*_set` schema used in `nmdc.metadata`. [^nmdc_context_audit]

The resource ecosystem has heterogeneous authority: NMDC is the authority for NMDC resources, NEON is the authority for `kbase.nmdc_neon`, NCBI BioSample is the authority for `nmdc.ncbi_biosamples`, and Pfam/InterPro is the authority for `nmdc.ref_data`. [^nmdc_context_audit]

The audit found that `kbase.nmdc_neon` represents the National Ecological Observatory Network, an NSF program distinct from NMDC and its DOE-BER context, so treating the namesake as NMDC would create an agency-attribution error. [^nmdc_context_audit]

The Arkin derivative adds embeddings and traits that do not exist upstream, while the NCBI mirror adds an attribute-harmonization layer to 51,711,888 raw NCBI samples. [^nmdc_context_audit]

The NMDC ecosystem also includes `nmdc.results.annotation_kegg_orthology`, which contains 1.83B rows; row counts for NMDC tables returned instantly through Iceberg metadata using `SELECT COUNT(*)`. [^nmdc_context_audit]

Metadata introspection and data reads have different access surfaces: `DESCRIBE DATABASE EXTENDED kbase.nmdc_*` raised `ForbiddenException` for a `kesciencero`/`microbialdiscoveryforge` principal even when `COUNT(*)` on the same tables succeeded. [^nmdc_context_audit]

`get_databases()` returns both dotted Iceberg aliases, such as `nmdc.metadata`, and underscore Hive aliases, such as `nmdc_metadata`, for every tenant database, so consumers must de-duplicate to the dotted form before iteration. [^nmdc_context_audit]

The PHB ecology analysis **refines** this resource picture by using NMDC metagenomes as a cross-validation layer rather than treating NMDC as a single homogeneous dataset: 3,014/3,492 NMDC taxon columns (86.3%) mapped to GTDB genera with known PHB status across 6,365 samples, with a median 87.2% of taxonomic abundance matched to pangenome genera. [^phb_granule_ecology] The analysis matched 693 genera between pangenomes and NMDC metagenomes; genera with at least 50% phaC prevalence had significantly higher NMDC abundance than lower-prevalence genera (Mann–Whitney p = 8.41 x 10^-22). [^phb_granule_ecology]

The prophage ecology study **supports and refines** this cross-validation picture by using taxonomy-based prophage-burden inference across 6,365 NMDC metagenomic samples, achieving 87.2% median matching coverage and identifying 57 significant module–abiotic correlations at FDR < 0.05. [^prophage_ecology] Concordance between pangenome enrichment and NMDC correlations was reported for head morphogenesis, tail, and anti-defense modules, while packaging, lysis, integration, and lysogenic regulation were significant in NMDC data without pangenome enrichment beyond phylogenetic expectation. [^prophage_ecology] This is an indirect bridge that assumes genus-level conservation of prophage content and had not been independently validated for prophage genes. [^prophage_ecology]

## Provenance and discovery implications

The `nmdc` label is systematically overloaded rather than being a reliable dataset boundary, because the audit observed four predicted confusion modes across tenant placement, provenance, scale, and namesake identity. [^nmdc_context_audit]

This **supports** [cross-tenant-data-bridging](../concepts/cross-tenant-data-bridging.md): NMDC-related resources are split between the `nmdc` and `kbase` tenants, while prefix-based inventory can fail to connect `kbase.nmdc_*` resources to NMDC. [^nmdc_context_audit]

This **supports** [provenance-aware-resource-discovery](../concepts/provenance-aware-resource-discovery.md): provenance, authority, scale, and snapshot currency need to be surfaced together rather than inferred from a database name. [^nmdc_context_audit] The PHB cross-validation **supports** this requirement: its mapping depended on an explicit two-tier bridge from NMDC taxon columns to GTDB genera, rather than on the NMDC label alone. [^phb_granule_ecology] The prophage analysis **further supports** it: NMDC was used as a derived metagenomic validation layer whose taxonomy matching and genus-level conservation assumption must be exposed alongside its correlations. [^prophage_ecology]

The audit inferred provenance classes from schema, table properties, tenant metadata, and prior project usage because no ingestion manifest was exposed in the catalog. [^nmdc_context_audit]

The interpretation that label overload causes sub-optimal resource selection remains a hypothesis rather than a directly measured user-behavior finding, because the audit did not directly observe users choosing the wrong resource. [^nmdc_context_audit]

The PHB study’s NMDC correlations with environmental variables were statistically significant but modest, with all reported absolute Spearman correlations below 0.12; because NMDC measurements were point-in-time values rather than direct measures of temporal variability, they provide cross-validation but do not by themselves establish the feast/famine interpretation. [^phb_granule_ecology]

The prophage study adds a distinct environmental-use case: its strongest NMDC correlations were packaging with pH (Spearman rho=0.519), all modules with pH (rho=0.474), all modules with temperature (rho=0.399), all modules with depth (rho=0.361), and all modules with total nitrogen (rho=0.333). [^prophage_ecology] The positive pH association is explicitly a hypothesis about alkaline conditions or pH-linked ecology, not a causal conclusion, because the burden inference was indirect. [^prophage_ecology]

## Related source

- [nmdc_context_audit__REPORT](../summaries/nmdc_context_audit__REPORT.md) — Summary of the NMDC context audit, including resource provenance, tenant placement, scale, currency, access surfaces, and proposed remediation. [^nmdc_context_audit]
- [phb_granule_ecology__REPORT](../summaries/phb_granule_ecology__REPORT.md) — PHB pathway ecology analysis using NMDC metagenomic cross-validation and GTDB pangenome mappings. [^phb_granule_ecology]
- [prophage_ecology__REPORT](../summaries/prophage_ecology__REPORT.md) — Prophage module ecology, environmental associations, TerL lineages, and NMDC metagenomic cross-validation. [^prophage_ecology]

[^nmdc_context_audit]: [nmdc context audit](../summaries/nmdc_context_audit__REPORT.md)
[^phb_granule_ecology]: [phb granule ecology](../summaries/phb_granule_ecology__REPORT.md)
[^prophage_ecology]: [prophage ecology](../summaries/prophage_ecology__REPORT.md)
