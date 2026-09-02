---
type: "Dataset"
description: "NCBI BioSample harvest re-hosted as nmdc.ncbi_biosamples"
sources: ["summaries/nmdc_context_audit__REPORT.md"]
---
# NCBI BioSample resource re-hosted under an NMDC-labeled database

## What this entity is

**Canonical name:** NCBI BioSample resource re-hosted under an NMDC-labeled database. [src: nmdc_context_audit]

**Known aliases:** `nmdc.ncbi_biosamples`; NCBI BioSample mirror; NCBI re-host. [src: nmdc_context_audit]

**Stable external identifier:** No stable external identifier is specified in the audit. [src: nmdc_context_audit]

This dataset is an NCBI BioSample harvest hosted under the `nmdc` tenant rather than a genuine NMDC-curated biosample resource. [src: nmdc_context_audit] Its placement illustrates the overloaded `nmdc` label and creates a provenance distinction from [[entities/nmdc-metadata]], the genuine NMDC biosample universe. [src: nmdc_context_audit]

## Key facts

- `nmdc.ncbi_biosamples` contains **51,711,888 biosamples** and **756,112,544 attribute rows**. [src: nmdc_context_audit]
- The genuine NMDC biosample universe in `nmdc.metadata.biosample_set` contains **16,640 samples**. [src: nmdc_context_audit]
- The audit characterizes the difference between the NCBI mirror and the genuine NMDC biosample universe as a **~3,000× scale trap**. [src: nmdc_context_audit]
- The resource is one of the external re-hosts found among four databases in the `nmdc` tenant; the other identified external re-host is [[entities/pfam]] reference data in `nmdc.ref_data`. [src: nmdc_context_audit]
- Its latest reported Iceberg commit is **2026-03-09**. [src: nmdc_context_audit]
- The audit recommends exposing provenance and value together rather than relabeling or removing the resource, because the NCBI mirror provides an attribute-harmonization layer over raw NCBI samples. [src: nmdc_context_audit]
- The audit did not test completeness against live upstream NCBI record counts, so the resource’s completeness lag remains unquantified. [src: nmdc_context_audit]

## Discovery and attribution risks

The shared `nmdc` label can lead users seeking NMDC-curated microbiome metadata to select this NCBI mirror, work at the wrong scale, or misinterpret its authority. [src: nmdc_context_audit] The audit treats these as plausible consequences inferred from resource structure, documentation gaps, and prior-project usage skew rather than as directly observed user errors. [src: nmdc_context_audit]

The authoritative source for this resource is NCBI BioSample, whereas NMDC is the National Microbiome Data Collaborative of DOE-BER. [src: nmdc_context_audit] Provenance should therefore be distinguished from related NMDC resources such as [[entities/nmdc-results]] and [[entities/nmdc-metadata]]. [src: nmdc_context_audit]

## Access and scale inspection

Row counts for BERDL tables, including this resource, can be retrieved through Iceberg metadata with `SELECT COUNT(*)`; the audit reports that these counts return instantly. [src: nmdc_context_audit] `get_databases()` returns both dotted Iceberg aliases and underscore Hive aliases, so consumers must de-duplicate the dotted form before iteration to avoid double-counting. [src: nmdc_context_audit]

## Source

- [[summaries/nmdc_context_audit__REPORT]] — audit of provenance, tenant placement, scale, currency, authority, and discovery risks for NMDC-labeled BERDL resources. [src: nmdc_context_audit]
