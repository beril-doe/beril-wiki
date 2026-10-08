---
type: "Concept"
description: "Tenant-group membership and authentication-token expiry are recurring preconditions and failure modes for data access in analysis sessions on the KBase Data Lakehouse."
sources: ["summaries/pitfalls.md"]
---
# Credential Expiry and Tenant Membership Are Analysis-Session Failure Modes

Every query an analysis makes against the KBase Data Lakehouse depends on two separate preconditions. First, the user must belong to the tenant group that owns the data. Second, the authentication token the session presents must still be valid. Either one can fail even when the analysis code has not changed. That makes them part of a project's reproducibility conditions rather than its scientific logic. All guidance on this page comes from one source, the central pitfalls digest ([[summaries/pitfalls]]). The digest records operational practice, not measured failure rates [src: pitfalls].

## Tenant Membership

The pitfalls digest names `get_group_sql_warehouse(tenant_name)` as the way to check whether a user has access to a tenant. It states that an `ErrorResponse` with error 20040 means the user is not in that group [src: pitfalls]. This is a group-membership (authorization) failure, not an expired-credential failure. The check is a cheap pre-flight test that separates a membership problem from a query or schema problem. It relates to the access-path issues collected in [[concepts/cross-tenant-data-bridging]] and [[concepts/execution-environment-dependent-access-paths]] [src: pitfalls].

## Token Variable Naming

The `.env` file stores the authentication token as `KBASE_AUTH_TOKEN`, not `KB_AUTH_TOKEN`. Code that reads the wrong variable name will not pick up the stored credential [src: pitfalls].

## Token Expiry During Long Sessions

The token stored in `.env` (`KBASE_AUTH_TOKEN`) can expire during long analysis sessions. When it does, all KBase Data Lakehouse API calls return 401/403 errors [src: pitfalls]. This **supports** treating long-running jobs as a distinct reliability regime, as argued in [[concepts/long-running-analysis-execution-reliability]]. A failure that appears hours into a run may come from an expired credential rather than from a data or code fault [src: pitfalls].

On JupyterHub, a fresh token is always available in the literal file `~/.berdl_kbase_session`. The IPython startup script `~/.ipython/profile_default/startup/05-token-sync.py` syncs this file every 30 seconds [src: pitfalls].

The `.env` file is not automatically updated. For long-running command-line sessions outside JupyterHub, the token must be re-exported manually [src: pitfalls]. The digest guarantees only that the JupyterHub session file is kept synchronized. It does not say that a credential already loaded into a running notebook or process is refreshed. To benefit from the sync, a notebook session must read the fresh token from `~/.berdl_kbase_session` rather than rely on a value loaded earlier from `.env` [src: pitfalls].

## Evidence Grade

These statements are documented operational guidance from one central digest, not results of a systematic study. The digest gives no frequency of token expiry, no typical token lifetime and no count of affected analyses. The size of the problem across projects is therefore untested here [src: pitfalls].

## Open Directions

- Log access failures with timestamps across long-running project notebooks, recording authentication failures (401/403 responses) separately from tenant-nonmembership authorization failures (error 20040). Estimate how often reruns or partial outputs trace to an expired credential, to missing group membership or to code faults. This would close the gap left by the digest, which gives no frequency for either failure mode [src: pitfalls].
- Run the same long query workload two ways: as `.env`-based CLI runs, and as JupyterHub runs that explicitly re-read the synced session file before each call. This would test whether reading from the 30-second-synced file removes mid-run 401/403 failures in practice [src: pitfalls].
- Add a pre-flight step that calls `get_group_sql_warehouse(tenant_name)` for every tenant a project touches, and record the result in project provenance. Later audits could then tell a missing-membership failure apart from an empty-result query [src: pitfalls].
