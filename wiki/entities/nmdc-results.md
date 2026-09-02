---
type: "Dataset"
description: "NMDC analysis-results dataset and its provenance-aware access boundary"
sources: ["summaries/nmdc_context_audit__REPORT.md", "summaries/pitfalls.md"]
---
# NMDC analysis-results resource

## What this entity is

**Canonical name:** NMDC analysis-results resource. [src: nmdc_context_audit]

**Known alias:** `nmdc.results`. [src: nmdc_context_audit]

**Stable external identifier:** No stable external identifier was reported in the audit. [src: nmdc_context_audit]

This is a genuine NMDC resource hosted in the `nmdc` tenant and distinct from the NCBI BioSample re-host, Pfam re-host, Arkin derivative, MAG catalog, and NEON namesake resources discussed in the audit. [src: nmdc_context_audit]

## Key facts

- The `nmdc.results` resource had a latest reported Iceberg commit of `2026-05-20`. [src: nmdc_context_audit]
- The `nmdc.results.annotation_kegg_orthology` table contains 1.83B rows. [src: nmdc_context_audit]
- Row counts for NMDC tables, including `nmdc.results.annotation_kegg_orthology`, returned instantly through Iceberg metadata using `SELECT COUNT(*)`. [src: nmdc_context_audit]
- The audit found that metadata introspection and data reads have different access surfaces, because `DESCRIBE DATABASE EXTENDED kbase.nmdc_*` raised `ForbiddenException` for a `kesciencero`/`microbialdiscoveryforge` principal even when `COUNT(*)` on the same tables succeeded. [src: nmdc_context_audit]
- The resource is part of a broader naming problem in which 20 database names containing `nmdc` resolve to 7 real, maintained resources across three tenants and six provenance classes. [src: nmdc_context_audit]
- The audit recommends exposing Iceberg `max(committed_at)` during discovery because database properties were empty and catalog tables had no comments. [src: nmdc_context_audit]
- The pitfalls document **refines** this access and discovery guidance: NMDC classifier and metabolomics tables use distinct `file_id` namespaces (`nmdc:dobj-11-*` and `nmdc:dobj-12-*`) and must be bridged through `sample_id` in `omics_files_table`, which contains 385,562 rows. [src: pitfalls]
- The same document **supports** provenance-aware interpretation by warning that NMDC `taxonomy_features` is a wide matrix with numeric taxon-ID columns, while `abiotic_features` stores unmeasured variables as `0.0` rather than `NULL`; these representations require schema inspection and explicit handling before analysis. [src: pitfalls]

## Relations to the corpus

The resource is part of the NMDC-related cross-tenant discovery problem described in [[concepts/cross-tenant-data-bridging]]. [src: nmdc_context_audit]

It should be interpreted alongside the maintained [[entities/nmdc-metadata]] resource and the NMDC-derived [[entities/nmdc-mags]] catalog rather than as a stand-alone boundary for all resources whose names contain `nmdc`. [src: nmdc_context_audit]

The audit's complete discussion is summarized in [[summaries/nmdc_context_audit__REPORT]], while the operational safeguards are summarized in [[summaries/pitfalls]]. [src: nmdc_context_audit, pitfalls]
