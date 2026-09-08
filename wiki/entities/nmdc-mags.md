---
type: Dataset
description: KBase-hosted NMDC-derived catalog containing 62,346 MAGs.
sources:
- id: nmdc_context_audit
  resource: ../summaries/nmdc_context_audit__REPORT.md
  title: nmdc context audit
title: KBase-hosted NMDC-derived metagenome-assembled genome catalog
---
# KBase-hosted NMDC-derived metagenome-assembled genome catalog

## What this entity is

The canonical name is **KBase-hosted NMDC-derived metagenome-assembled genome catalog**. [^nmdc_context_audit]

Known alias: `kbase.nmdc_mags`. [^nmdc_context_audit]

Stable external identifier: none is reported in the audit. [^nmdc_context_audit]

This dataset is a KBase-hosted resource derived from the National Microbiome Data Collaborative (NMDC) ecosystem and is one of seven maintained resources identified among 20 databases whose names contain `nmdc`. [^nmdc_context_audit]

## Key facts

`kbase.nmdc_mags` contains **62,346 metagenome-assembled genomes (MAGs)**. [^nmdc_context_audit]

The resource is located in the `kbase` tenant rather than the `nmdc` tenant. [^nmdc_context_audit]

It had the latest reported commit among the NMDC-labeled resources, with an Iceberg snapshot date of **2026-07-02**. [^nmdc_context_audit]

The audit identifies this catalog as the freshest NMDC resource, while also noting that it is located in the tenant users are least likely to search when looking for NMDC data. [^nmdc_context_audit]

The catalog is distinct from the genuine NMDC resources `nmdc.metadata` and `nmdc.results`, the NCBI BioSample re-host `nmdc.ncbi_biosamples`, the Pfam re-host `nmdc.ref_data`, the Arkin Lab derivative `kbase.nmdc_arkin`, and the namesake NEON resource `kbase.nmdc_neon`. [^nmdc_context_audit]

The audit treats explicit provenance and currency annotations as necessary for selecting this catalog correctly within the broader [cross-tenant-data-bridging](../concepts/cross-tenant-data-bridging.md) problem. [^nmdc_context_audit]

The catalog contributes to [multi-omics-integration](../concepts/multi-omics-integration.md) and [pangenome-integration](../concepts/pangenome-integration.md) as an NMDC-derived resource whose scale and currency must be distinguished from those of related re-hosts and derivatives. [^nmdc_context_audit]

## Source

- [nmdc_context_audit__REPORT](../summaries/nmdc_context_audit__REPORT.md) — audit of NMDC-labeled BERDL resources, including provenance, tenant placement, scale, currency, and authority. [^nmdc_context_audit]

[^nmdc_context_audit]: [nmdc context audit](../summaries/nmdc_context_audit__REPORT.md)
