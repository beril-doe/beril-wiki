---
type: Summary
description: Audit of NMDC-labeled BERDL resources, provenance, scale, and currency
doc_type: short
full_text: ../sources/nmdc_context_audit__REPORT.md
title: NMDC Context Audit
sources:
- id: nmdc_context_audit
  resource: ../sources/nmdc_context_audit__REPORT.md
  title: nmdc context audit
---
# NMDC Context Audit

## Overview

This audit evaluates BERDL resources whose names contain `nmdc`, distinguishing provenance, tenant placement, scale, currency, and authority. It finds that 20 database names resolve to 7 real, maintained resources across three tenants and six provenance classes, demonstrating that the `nmdc` label is systematically overloaded rather than a reliable dataset boundary. [^nmdc_context_audit]

## Key Findings

### 1. One label spans three tenants and six provenance classes

The 7 maintained resources comprise genuine NMDC resources (`nmdc.metadata` and `nmdc.results`), an NCBI re-host (`nmdc.ncbi_biosamples`), a Pfam re-host (`nmdc.ref_data`), an Arkin Lab derivative (`kbase.nmdc_arkin`), an NMDC-derived KBase resource (`kbase.nmdc_mags`), and a namesake collision representing NEON rather than NMDC (`kbase.nmdc_neon`). All four predicted confusion modes were observed in actual resources, supporting the audit’s hypothesis that the label is systematically overloaded. [^nmdc_context_audit]

### 2. The `nmdc` tenant is neither all NMDC nor only NMDC

Two of the four databases in the `nmdc` tenant are external re-hosts: `nmdc.ncbi_biosamples` contains an NCBI BioSample harvest with 51,711,888 biosamples and 756,112,544 attribute rows, while `nmdc.ref_data` contains 27,481 Pfam terms. Three NMDC-related databases—`nmdc_arkin`, `nmdc_mags`, and `nmdc_neon`—are instead located in the `kbase` tenant. [^nmdc_context_audit]

The genuine NMDC biosample universe contains 16,640 samples in `nmdc.metadata.biosample_set`, whereas the co-hosted NCBI mirror contains 51,711,888 biosamples; the report identifies this as a ~3,000× scale trap. [^nmdc_context_audit]

The freshest NMDC resource is `kbase.nmdc_mags`, containing 62,346 MAGs, but it is located in the tenant users are least likely to search when looking for NMDC data. [^nmdc_context_audit]

### 3. Currency is distributed across months and is not exposed at discovery

Iceberg snapshot ages—the available data-currency signal—span approximately four months across NMDC-labeled resources. The latest commits are `2026-07-02` for `kbase.nmdc_mags` and `kbase.nmdc_neon`, `2026-05-27` for `kbase.nmdc_arkin`, `2026-05-20` for `nmdc.metadata`, `nmdc.results`, and `nmdc.ref_data`, and `2026-03-09` for `nmdc.ncbi_biosamples`. [^nmdc_context_audit]

The audit recommends surfacing `max(committed_at)` in discovery tooling because tables have no comments, databases have empty properties, and no changelog exposes currency. [^nmdc_context_audit]

### 4. Context is missing across catalog, documentation, and tooling layers

Catalog tables carry no `Comment`, databases have empty `Properties` with owner `tgu2`, the canonical `docs/schemas/nmdc.md` link returns a 404 because `docs/schemas/` does not exist, and `docs/overview.md` does not mention NMDC. The `berdl` skill contains zero NMDC-specific content, while `berdl_inventory.py` groups resources by catalog prefix and therefore does not link `kbase.nmdc_*` resources back to NMDC. [^nmdc_context_audit]

The `berdl_data_atlas` also labels Rhea and Gene Ontology reference ontologies under `nmdc_arkin` as “NMDC integrated,” creating provenance blur even where documentation exists. [^nmdc_context_audit]

### 5. Names and provenance create concrete attribution hazards

`kbase.nmdc_neon` represents the National Ecological Observatory Network (NEON), an NSF program distinct from the National Microbiome Data Collaborative (NMDC) and its DOE-BER context. Treating the namesake as NMDC would create an agency-attribution error. [^nmdc_context_audit]

The audit characterizes co-hosting as intentional and potentially valuable: the NCBI mirror adds an attribute-harmonization layer to 51,711,888 raw NCBI samples, while the Arkin derivative adds embeddings and traits that do not exist upstream. The recommended remedy is therefore to expose provenance and value together rather than relabeling or removing resources. [^nmdc_context_audit]

### 6. Scale can be catalogued cheaply, but metadata access differs from data access

Row counts for all NMDC tables, including `nmdc.results.annotation_kegg_orthology` with 1.83B rows, return instantly through Iceberg metadata using `SELECT COUNT(*)`. [^nmdc_context_audit]

`DESCRIBE DATABASE EXTENDED kbase.nmdc_*` raises `ForbiddenException` for a `kesciencero`/`microbialdiscoveryforge` principal even when `COUNT(*)` on the same tables succeeds, showing that metadata introspection and data reads have different access surfaces. [^nmdc_context_audit]

`get_databases()` returns both dotted Iceberg aliases such as `nmdc.metadata` and underscore Hive aliases such as `nmdc_metadata` for every tenant database; consumers must de-duplicate to the dotted form before iteration to avoid double-counting. [^nmdc_context_audit]

### 7. Primary deliverable and proposed remediation

The project’s primary deliverable is a 15-file Open-Knowledge-Format directory containing an index, a thesis on label overload, a goal-to-resource decision guide, resource-specific provenance pages, scale and currency guidance, naming-cruft documentation, and prior-project usage information. [^nmdc_context_audit]

The report proposes, but does not apply, seven fixes: repair or repoint the broken schema entry point; add an NMDC module to the `berdl` skill; cross-link `nmdc` and `kbase.nmdc_*` homes in inventory output; surface Iceberg snapshot currency; correct provenance-blur labels; mention NMDC in `docs/overview.md`; and repair or drop broken user copies and the phantom `kbase_nmdc_neon` alias through a commit or pull request. [^nmdc_context_audit]

## Interpretation

The evidence is consistent with the overloaded label contributing to sub-optimal resource selection, but this interpretation is inferred from gap analysis and prior-project usage skew rather than from a directly observed wrong choice. A user seeking NMDC-curated microbiome metadata could select `nmdc.ncbi_biosamples`, work at the wrong scale, omit the freshest MAG catalog by searching only the `nmdc` tenant, or misattribute NEON data as NMDC; the report treats the resulting time, compute, and interpretive costs as plausible consequences rather than directly measured outcomes. [^nmdc_context_audit]

The authority context is also heterogeneous: NMDC is the National Microbiome Data Collaborative of DOE-BER; NEON is the National Ecological Observatory Network of NSF; NCBI BioSample is the authority for `nmdc.ncbi_biosamples`; and Pfam/InterPro is the authority for `nmdc.ref_data`. The NMDC data model is LinkML-based and defines the `*_set` schema used in `nmdc.metadata`. [^nmdc_context_audit]

## Caveats and Limitations

The provenance classes are inferred from schema, table properties, tenant metadata, and prior project usage rather than an ingestion manifest, because no ingestion manifest is exposed in the catalog. [^nmdc_context_audit]

Descriptions for `kbase.nmdc_*` databases are access-restricted by `ForbiddenException`, so steward-authored notes, if any, could not be captured. [^nmdc_context_audit]

Completeness is assessed relative to snapshot timestamps and was not tested by comparison with live upstream NMDC or NCBI record counts; such comparison would require external API calls and was out of scope. [^nmdc_context_audit]

The report does not directly observe users choosing the wrong resource. Its interpretation that label overload drives sub-optimal selection is based on gap analysis and prior-project reuse skew, so that causal claim remains inferred. [^nmdc_context_audit]

The audit enumerates 7 real, maintained resources among 20 NMDC-named database entries, but also records aliases, test databases including `globalusers.nmdc_core_test*`, a phantom `kbase_nmdc_neon` with 0 tables, and broken user copies including `mamillerpa/my.nmdc_flattened_biosamples` with a dangling Iceberg pointer. [^nmdc_context_audit]

## Future Directions

The report proposes applying the documentation and tooling fixes, measuring whether subsequent NMDC projects reach the appropriate resource faster, adding lightweight provenance and currency annotations to inventory output, extending the provenance-audit method to other overloaded BERDL labels, and comparing `nmdc.metadata` and `nmdc.ncbi_biosamples` with live upstream record counts to quantify completeness lag. [^nmdc_context_audit]

## Slots Into

- [cross-tenant-data-bridging](../concepts/cross-tenant-data-bridging.md) — The audit directly documents NMDC-related resources split across `nmdc` and `kbase` tenants, prefix-based discovery failure, aliases, and the need for cross-tenant provenance links.
- [multi-omics-integration](../concepts/multi-omics-integration.md) — The audit identifies value-added NMDC-related products containing embeddings, traits, metabolomics, omics files, and MAG catalog data, while emphasizing that these derivatives require explicit provenance and authority context.
- [pangenome-integration](../concepts/pangenome-integration.md) — The audit highlights the scale and currency of the NMDC MAG catalog and distinguishes NMDC-derived resources from external re-hosts and namesake databases.

[^nmdc_context_audit]: [nmdc context audit](../sources/nmdc_context_audit__REPORT.md)
