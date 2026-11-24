---
type: "Concept"
description: "Covers table addressing during the Delta-to-Iceberg migration, tenant naming for ingestion, access-denied errors and auth-token handling; stops at query execution performance."
sources: ["summaries/nmdc_context_audit__REPORT.md", "summaries/pitfalls.md"]
---
# Lakehouse namespace migration, tenancy and authentication

This page covers Lakehouse namespace migration, tenancy and authentication. Collections are moving from Delta to Iceberg, and addresses changed from underscore-joined to dotted names. [src: pitfalls] The cross-project pitfalls digest documents specific tenant-naming and token pitfalls, such as wrong tenant values and expired .env tokens. [src: pitfalls] Most evidence comes from that digest ([[summaries/pitfalls]]), with one access observation from [[summaries/nmdc_context_audit__REPORT]]. See also [[entities/kbase-data-lakehouse]].

## Table addressing during the Delta-to-Iceberg migration

Collections are migrating from Delta to Iceberg, and the address format changed with them. Iceberg tables use dotted catalog.namespace.table identifiers. Delta used one underscore-joined identifier. For example, kbase.ke_pangenome.genome was previously kbase_ke_pangenome.genome. [src: pitfalls] Only the leading underscore changes. The table name stays the same. [src: pitfalls]

Migration is not finished. If a dotted namespace cannot be found, the collection may still be Delta-only, and the underscore form is then correct. [src: pitfalls] The report advises preferring the dotted form for migrated collections and falling back to the underscore form when the dotted name is not found. [src: pitfalls] It also advises against hardcoding either form. It recommends live, access-aware catalog discovery, which means running SET and parsing spark.sql.catalog.*, or using the notebook helpers. [src: pitfalls]

A query copied verbatim from an older project's README, REPORT, notebook or .py file uses the underscore form. Against the migrated catalog it fails with TABLE_OR_VIEW_NOT_FOUND or an unresolved-relation error. [src: pitfalls] Hundreds of completed-project files use underscore-form names, and these archived files are intentionally not rewritten because they are historical. [src: pitfalls] The nmdc_context_audit report notes that the broader dotted-versus-underscore migration is already documented in docs/pitfalls.md. [src: nmdc_context_audit]

## Tenant naming for ingestion

The tenant is the database prefix. For example, kbase_ke_pangenome belongs to tenant kbase, and kescience_mgnify belongs to tenant kescience. [src: pitfalls] The kbase_ke_pangenome database lives under tenant kbase, not kbase_ke. [src: pitfalls] If an error shows the physical path, the tenant is the path segment after tenant-sql-warehouse/. [src: pitfalls]

In a data_lakehouse_ingest configuration, the tenant field is the MinIO governance group name, not the database name prefix. The library prepends the tenant to the dataset field to form the namespace. [src: pitfalls] The working configuration for kbase_ke_pangenome is tenant "kbase" with dataset "ke_pangenome". [src: pitfalls] Two configurations are wrong:
- tenant="kbase_ke" leaves the user without access and falls back to the personal warehouse. [src: pitfalls]
- dataset="kbase_ke_pangenome" with tenant="kbase" creates "kbase_kbase_ke_pangenome". [src: pitfalls]

To verify tenant access, call get_group_sql_warehouse(tenant_name). ErrorResponse error 20040 means the user is not in that group. [src: pitfalls] The /berdl-ingest initialize() function works only off-cluster. On JupyterHub, the report recommends bypassing it and building the Spark and MinIO clients directly. [src: pitfalls]

## Access-denied errors

Access failures on tables can appear as S3 access denied, 403 Forbidden, Token denied or AccessControlException. These are internal authorization signals, not technical faults, and they mean little to a researcher. [src: pitfalls] Users get a message pointing them to the Tenant Browser to request access. [src: pitfalls] Access errors are expected when exploring databases the user has not been granted. The report says to treat them as a permissions prompt, not an error condition. [src: pitfalls]

Access surfaces differ between metadata and data. In nmdc_context_audit, DESCRIBE DATABASE EXTENDED kbase.nmdc_* raised ForbiddenException for a kesciencero/microbialdiscoveryforge principal, even though COUNT(*) on the same tables succeeded. [src: nmdc_context_audit] This restriction meant some metadata, such as steward-authored notes if any exist, could not be captured. [src: nmdc_context_audit] See also [[concepts/metadata-introspection-versus-data-read-access-in-spark-based-catalogs]].

## Authentication tokens

The .env file uses KBASE_AUTH_TOKEN, not KB_AUTH_TOKEN. [src: pitfalls] In snipe_defense_system, this token expired during long analysis sessions, and all API calls (application programming interface calls) then returned 401/403 errors. [src: pitfalls] On JupyterHub, a fresh token is always at ~/.berdl_kbase_session. The IPython startup script ~/.ipython/profile_default/startup/05-token-sync.py syncs it every 30 seconds. [src: pitfalls] The .env file is not updated automatically, so long-running CLI sessions outside JupyterHub need a manual token re-export. [src: pitfalls] A checklist item says to check ~/.berdl_kbase_session if the .env token fails. [src: pitfalls]

A related network issue arose in essential_metabolome. Off-cluster mc (MinIO client) commands time out unless proxy environment variables are set. [src: pitfalls]

## Open Directions

- Inventory which collections are still Delta-only by running live catalog discovery across all accessible catalogs. This would replace the current "may still be Delta-only" guess with a list.
- Scan archived project files for underscore-form names and report which ones resolve against the migrated catalog. This would show how many historical queries break.
- Test whether other principals see the same split between DESCRIBE DATABASE EXTENDED and COUNT(*). This would show whether the ForbiddenException pattern is general.
- Add a pre-flight check that calls get_group_sql_warehouse and validates the tenant and dataset pair before ingestion. This would catch the two misconfigurations listed above.
