---
type: "Concept"
description: "Covers how Iceberg metadata queries, namespace aliases and permission surfaces behave when auditing lakehouse databases; stops at this access pattern."
sources: ["summaries/nmdc_context_audit__REPORT.md", "summaries/pitfalls.md"]
---
# Metadata introspection versus data-read access in Spark-based catalogs

This page covers metadata introspection versus data-read access in Spark-based catalogs of the [[entities/kbase-data-lakehouse]]. Metadata introspection and data reads go through different access surfaces. [src: nmdc_context_audit] The evidence comes from one audit of the NMDC collections ([[entities/nmdc-integrated-collections]]) and from guidance in the pitfalls digest.

## Row counts through Iceberg metadata

Cataloguing scale is cheap. In the NMDC audit, row counts on all NMDC tables returned instantly through Iceberg metadata using SELECT COUNT(*). That included nmdc.results.annotation_kegg_orthology, which has 1.83B rows. [src: nmdc_context_audit]

## Introspection can be blocked while reads succeed

DESCRIBE DATABASE EXTENDED kbase.nmdc_* raised ForbiddenException for a kesciencero/microbialdiscoveryforge principal, even though COUNT(*) on the same tables succeeded. [src: nmdc_context_audit] As a result, some metadata, such as steward-authored notes if any exist, could not be captured. [src: nmdc_context_audit]

The pitfalls digest explains how to read such failures. Errors such as S3 access denied, 403 Forbidden, Token denied or AccessControlException are internal authorization signals, not technical faults. [src: pitfalls] Such errors are expected when exploring databases the user has not been granted, and should be treated as a permissions prompt, not an error condition. [src: pitfalls]

## Namespace aliases

get_databases() returns both the dotted Iceberg alias (nmdc.metadata) and the underscore Hive alias (nmdc_metadata) for every tenant database. Deduplicate to the dotted form before iterating, to avoid double-counting. [src: nmdc_context_audit] The broader dotted-versus-underscore migration is documented repo-wide in docs/pitfalls.md. [src: nmdc_context_audit] See [[concepts/lakehouse-namespace-migration-tenancy-and-authentication]] for that migration. The pitfalls digest advises against hardcoding either form. It recommends live, access-aware catalog discovery: SET plus parsing spark.sql.catalog.*, or notebook helpers. [src: pitfalls]

## Open Directions

- Test whether DESCRIBE succeeds for other principals on the nmdc_* databases. This would show whether the ForbiddenException is specific to the kesciencero/microbialdiscoveryforge principal.
- Compare Iceberg-metadata COUNT(*) against full scans on a few large tables. This would confirm that metadata counts match the data.
- Add deduplication of dotted and underscore aliases to audit scripts, then check earlier inventories for double-counted tables (see [[concepts/audit-blind-spots-in-inventories-of-data-and-its-use]]).
