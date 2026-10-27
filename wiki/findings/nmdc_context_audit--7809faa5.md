---
type: "Finding"
description: "The 20 database names containing \"nmdc\" resolve to 7 real, maintained resources across three tenants (`nmdc`, `kbase`, plus broken user copies), falling into six provenance classes."
finding_id: "nmdc_context_audit--7809faa5"
result: "observation"
source: "nmdc_context_audit"
quantities: [{"value": "20", "what": "database names containing \"nmdc\"", "unit": "database names", "denominator": "", "scope": ""}, {"value": "7", "what": "real, maintained resources", "unit": "resources", "denominator": "20 database names", "scope": ""}, {"value": "three", "what": "tenants", "unit": "tenants", "denominator": "", "scope": "`nmdc`, `kbase`, plus broken user copies"}, {"value": "six", "what": "provenance classes", "unit": "classes", "denominator": "", "scope": ""}]
caveat: "Provenance classes were inferred from schema, table properties, tenant metadata, and prior project usage, not from an ingestion manifest, since none is exposed in-catalog."
first_added: "2026-10-27"
source_hash: "0f4c987b31cd4df5a18862ca0ce3d3589a6cdbd46b7cbf0496b2f325c91f5d92"
---
# The nmdc label covers many names but few real resources

The 20 database names containing "nmdc" resolve to 7 real, maintained resources across three tenants (`nmdc`, `kbase`, plus broken user copies), falling into six provenance classes. [src: nmdc_context_audit]

## Key figures

- **20 database names**: database names containing "nmdc" [src: nmdc_context_audit]
- **7 resources**: real, maintained resources (denominator 20 database names) [src: nmdc_context_audit]
- **three tenants**: tenants (scope `nmdc`, `kbase`, plus broken user copies) [src: nmdc_context_audit]
- **six classes**: provenance classes [src: nmdc_context_audit]

## Evidence

> Searching BERDL for `nmdc` returns resources that share only the substring — not provenance, scope, scale, or currency. The 20 database names containing "nmdc" resolve to **7 real, maintained resources** across **three tenants** (`nmdc`, `kbase`, plus broken user copies), falling into six provenance classes: [src: nmdc_context_audit]

From the report [[summaries/nmdc_context_audit__REPORT]].

## Caveat

Provenance classes were inferred from schema, table properties, tenant metadata, and prior project usage, not from an ingestion manifest, since none is exposed in-catalog. [src: nmdc_context_audit]

> - Provenance classes are inferred from schema, table properties, tenant metadata, and prior project usage — not from an ingestion manifest (none is exposed in-catalog). [src: nmdc_context_audit]

## Other caveats in this report

- The BERDL Data Atlas labels Rhea/GO reference ontologies under `nmdc_arkin` as NMDC integrated, blurring their external provenance. [src: nmdc_context_audit]
- `DESCRIBE DATABASE EXTENDED kbase.nmdc_*` is forbidden for the stated principal even though `COUNT(*)` succeeds on the same tables; metadata and data reads have different access permissions. [src: nmdc_context_audit]
- `get_databases()` returns both dotted Iceberg and underscore Hive aliases for every tenant database; using the dotted form for de-duplication avoids double counting. [src: nmdc_context_audit]
- The suggested link between overloaded labels and poor resource choice is inferred from gap analysis and prior-project usage skew, not a directly observed wrong choice. Costs to compute or conclusions are plausible, not measured. [src: nmdc_context_audit]
- Earlier repository knowledge covers `nmdc_arkin` but leaves the other six resources thinly documented or undocumented. [src: nmdc_context_audit]
