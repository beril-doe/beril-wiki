---
type: "Dataset"
description: "KBase-hosted NMDC-derived catalog containing 62,346 MAGs."
sources: ["summaries/nmdc_context_audit__REPORT.md"]
---
# KBase-hosted NMDC-derived metagenome-assembled genome catalog

## What this entity is

The canonical name is **KBase-hosted NMDC-derived metagenome-assembled genome catalog**. [src: nmdc_context_audit]

Known alias: `kbase.nmdc_mags`. [src: nmdc_context_audit]

Stable external identifier: none is reported in the audit. [src: nmdc_context_audit]

This dataset is a KBase-hosted resource derived from the National Microbiome Data Collaborative (NMDC) ecosystem and is one of seven maintained resources identified among 20 databases whose names contain `nmdc`. [src: nmdc_context_audit]

## Key facts

`kbase.nmdc_mags` contains **62,346 metagenome-assembled genomes (MAGs)**. [src: nmdc_context_audit]

The resource is located in the `kbase` tenant rather than the `nmdc` tenant. [src: nmdc_context_audit]

It had the latest reported commit among the NMDC-labeled resources, with an Iceberg snapshot date of **2026-07-02**. [src: nmdc_context_audit]

The audit identifies this catalog as the freshest NMDC resource, while also noting that it is located in the tenant users are least likely to search when looking for NMDC data. [src: nmdc_context_audit]

The catalog is distinct from the genuine NMDC resources `nmdc.metadata` and `nmdc.results`, the NCBI BioSample re-host `nmdc.ncbi_biosamples`, the Pfam re-host `nmdc.ref_data`, the Arkin Lab derivative `kbase.nmdc_arkin`, and the namesake NEON resource `kbase.nmdc_neon`. [src: nmdc_context_audit]

The audit treats explicit provenance and currency annotations as necessary for selecting this catalog correctly within the broader [[concepts/cross-tenant-data-bridging]] problem. [src: nmdc_context_audit]

The catalog contributes to [[concepts/multi-omics-integration]] and [[concepts/pangenome-integration]] as an NMDC-derived resource whose scale and currency must be distinguished from those of related re-hosts and derivatives. [src: nmdc_context_audit]

## Source

- [[summaries/nmdc_context_audit__REPORT]] — audit of NMDC-labeled KBase Data Lakehouse resources, including provenance, tenant placement, scale, currency, and authority. [src: nmdc_context_audit]
