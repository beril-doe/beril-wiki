---
type: Dataset
description: Canonical NMDC biosample metadata resource and its provenance boundaries
sources:
- id: nmdc_context_audit
  resource: ../summaries/nmdc_context_audit__REPORT.md
  title: nmdc context audit
- id: pitfalls
  resource: ../summaries/pitfalls.md
  title: pitfalls
title: Canonical NMDC biosample metadata resource
---
# Canonical NMDC biosample metadata resource

## What this entity is

The canonical name is **NMDC biosample metadata resource**. [^nmdc_context_audit]

The resource is maintained as `nmdc.metadata`, with `nmdc_metadata` reported as its underscore-form Hive alias. [^nmdc_context_audit] Known aliases are `nmdc.metadata` and `nmdc_metadata`. [^nmdc_context_audit] The audit did not report a stable external identifier for this resource. [^nmdc_context_audit]

NMDC refers here to the National Microbiome Data Collaborative of DOE-BER. [^nmdc_context_audit]

## Key facts

`nmdc.metadata` is one of the genuine NMDC resources identified among 7 maintained resources represented by 20 NMDC-named database entries. [^nmdc_context_audit] Its biosample universe contains exactly 16,640 samples in `nmdc.metadata.biosample_set`. [^nmdc_context_audit] The resource uses the NMDC LinkML-based data model and its `*_set` schema. [^nmdc_context_audit] Its latest reported Iceberg commit is dated `2026-05-20`. [^nmdc_context_audit]

The audit contrasts this canonical NMDC resource with [ncbi-biosample](ncbi-biosample.md), whose co-hosted mirror contains exactly 51,711,888 biosamples and 756,112,544 attribute rows. [^nmdc_context_audit] This contrast identifies a scale-selection hazard: the canonical NMDC biosample universe has 16,640 samples, whereas the NCBI mirror has 51,711,888 biosamples. [^nmdc_context_audit]

The resource is located in the `nmdc` tenant, while related resources such as [nmdc-mags](nmdc-mags.md) are located in the `kbase` tenant. [^nmdc_context_audit] This **supports** the audit’s cross-tenant distinction: NMDC classifier and metabolomics tables use separate `file_id` namespaces and must be bridged through `sample_id` using `omics_files_table`, rather than joined directly by file identifier. [^pitfalls]

The audit found that catalog tables have no comments and database properties are empty, so resource currency and provenance are not adequately exposed at discovery. [^nmdc_context_audit] The pitfalls document **refines** this concern by recommending live catalog and schema inspection, because namespace availability, schemas, permissions, and database contents can change. [^pitfalls] The audit recommends surfacing the maximum Iceberg `committed_at` timestamp in discovery tooling so users can assess currency. [^nmdc_context_audit]

NMDC metadata analyses also require care with representation: `abiotic_features` stores unmeasured variables as `0.0` rather than `NULL`, so zeros should be converted to `NaN` before analysis. [^pitfalls]

## Relations to the wider wiki

This resource is central to [cross-tenant-data-bridging](../concepts/cross-tenant-data-bridging.md) because the audit places genuine NMDC resources and NMDC-related derivatives across different tenants. [^nmdc_context_audit]

It also informs [provenance-aware-resource-discovery](../concepts/provenance-aware-resource-discovery.md) because the audit distinguishes canonical NMDC data from the NCBI re-host and recommends exposing provenance and currency together. [^nmdc_context_audit]

The resource is documented in [nmdc_context_audit__REPORT](../summaries/nmdc_context_audit__REPORT.md) and [pitfalls](../summaries/pitfalls.md). [^nmdc_context_audit][^pitfalls]

[^nmdc_context_audit]: [nmdc context audit](../summaries/nmdc_context_audit__REPORT.md)
[^pitfalls]: [pitfalls](../summaries/pitfalls.md)
