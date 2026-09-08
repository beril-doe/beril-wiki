---
type: Dataset
description: NMDC analysis-results dataset and its provenance-aware access boundary
sources:
- id: nmdc_context_audit
  resource: ../summaries/nmdc_context_audit__REPORT.md
  title: nmdc context audit
- id: pitfalls
  resource: ../summaries/pitfalls.md
  title: pitfalls
title: NMDC analysis-results resource
---
# NMDC analysis-results resource

## What this entity is

**Canonical name:** NMDC analysis-results resource. [^nmdc_context_audit]

**Known alias:** `nmdc.results`. [^nmdc_context_audit]

**Stable external identifier:** No stable external identifier was reported in the audit. [^nmdc_context_audit]

This is a genuine NMDC resource hosted in the `nmdc` tenant and distinct from the NCBI BioSample re-host, Pfam re-host, Arkin derivative, MAG catalog, and NEON namesake resources discussed in the audit. [^nmdc_context_audit]

## Key facts

- The `nmdc.results` resource had a latest reported Iceberg commit of `2026-05-20`. [^nmdc_context_audit]
- The `nmdc.results.annotation_kegg_orthology` table contains 1.83B rows. [^nmdc_context_audit]
- Row counts for NMDC tables, including `nmdc.results.annotation_kegg_orthology`, returned instantly through Iceberg metadata using `SELECT COUNT(*)`. [^nmdc_context_audit]
- The audit found that metadata introspection and data reads have different access surfaces, because `DESCRIBE DATABASE EXTENDED kbase.nmdc_*` raised `ForbiddenException` for a `kesciencero`/`microbialdiscoveryforge` principal even when `COUNT(*)` on the same tables succeeded. [^nmdc_context_audit]
- The resource is part of a broader naming problem in which 20 database names containing `nmdc` resolve to 7 real, maintained resources across three tenants and six provenance classes. [^nmdc_context_audit]
- The audit recommends exposing Iceberg `max(committed_at)` during discovery because database properties were empty and catalog tables had no comments. [^nmdc_context_audit]
- The pitfalls document **refines** this access and discovery guidance: NMDC classifier and metabolomics tables use distinct `file_id` namespaces (`nmdc:dobj-11-*` and `nmdc:dobj-12-*`) and must be bridged through `sample_id` in `omics_files_table`, which contains 385,562 rows. [^pitfalls]
- The same document **supports** provenance-aware interpretation by warning that NMDC `taxonomy_features` is a wide matrix with numeric taxon-ID columns, while `abiotic_features` stores unmeasured variables as `0.0` rather than `NULL`; these representations require schema inspection and explicit handling before analysis. [^pitfalls]

## Relations to the corpus

The resource is part of the NMDC-related cross-tenant discovery problem described in [cross-tenant-data-bridging](../concepts/cross-tenant-data-bridging.md). [^nmdc_context_audit]

It should be interpreted alongside the maintained [nmdc-metadata](nmdc-metadata.md) resource and the NMDC-derived [nmdc-mags](nmdc-mags.md) catalog rather than as a stand-alone boundary for all resources whose names contain `nmdc`. [^nmdc_context_audit]

The audit's complete discussion is summarized in [nmdc_context_audit__REPORT](../summaries/nmdc_context_audit__REPORT.md), while the operational safeguards are summarized in [pitfalls](../summaries/pitfalls.md). [^nmdc_context_audit][^pitfalls]

[^nmdc_context_audit]: [nmdc context audit](../summaries/nmdc_context_audit__REPORT.md)
[^pitfalls]: [pitfalls](../summaries/pitfalls.md)
