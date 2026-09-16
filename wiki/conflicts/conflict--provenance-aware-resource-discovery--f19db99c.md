<!-- tension-hash: f19db99c849a5ba6 -->
# Partial `kbase_uniref*` samples versus dated `refdata_uniref*_2026_01` cluster counts: which collection does "UniRef" name?

Two sources describe collections in the UniRef family on the KBase Data Lakehouse in apparently incompatible terms. One calls the `kbase_uniref*` collections partial/sample datasets. [src: pitfalls] The other reports cluster counts for the dated `refdata_uniref*_2026_01` collections. [src: berdl_data_atlas] Read together, they describe different resources and do not contradict each other. [src: pitfalls, berdl_data_atlas] The tension still matters for [[concepts/provenance-aware-resource-discovery]], because a resource card must carry the exact collection address rather than a family name. A user who searches for "UniRef" without the tenant-qualified name (the collection name including its tenant prefix, such as `kbase_` or `refdata_`) could reach the partial sample when the 2026-01 `refdata` release was intended. [src: pitfalls, berdl_data_atlas] Whether records overlap between the two collections is not reported. [src: pitfalls, berdl_data_atlas]

## Evidence Sides

**Side A: the `kbase_uniref*` collections are partial samples.**
The pitfalls notes describe `kbase_uniref50`, `kbase_uniref90`, and `kbase_uniref100` as partial/sample datasets, not the full UniRef releases, which would be hundreds of millions of clusters. [src: pitfalls] The note gives no row count for these collections. [src: pitfalls]

**Side B: the `refdata_uniref*_2026_01` collections hold large cluster tables.**
The atlas counts the `cluster` tables of `refdata_uniref50_2026_01`, `refdata_uniref90_2026_01`, and `refdata_uniref100_2026_01`. It reports 475,217,233 UniRef100, 188,848,220 UniRef90, and 60,315,044 UniRef50 clusters (2026-01). [src: berdl_data_atlas] These counts concern the `refdata_uniref*_2026_01` collections only, not the `kbase_uniref*` collections. [src: berdl_data_atlas]

**Shared gap.**
Neither source reports whether records overlap between the two collections. Settling that would need a record-level comparison. [src: pitfalls, berdl_data_atlas]

## Possible Reconciliations

- **Hypothesis 1: a naming problem only.** The apparent conflict may arise solely when collections are referenced by family name. Once each is cited by its tenant-qualified name, both sources' statements may stand without further conflict.
- **Hypothesis 2: the sample is a subset of the 2026-01 release.** The `kbase_uniref*` records may be drawn from the same release counted in the `refdata_uniref*_2026_01` tables. Overlap between the collections is not reported, so this is untested. [src: pitfalls, berdl_data_atlas]
- **Hypothesis 3: the sample comes from a different release.** The `kbase_uniref*` records may derive from a UniRef release other than 2026-01. Neither source reports the sample's release vintage, so this is also untested.

## Resolving Work

- **Row counts:** Identify the tables in the `kbase_uniref50`, `kbase_uniref90`, and `kbase_uniref100` collections, count their rows, and set them against the `refdata_uniref*_2026_01` `cluster` counts. This would turn the "partial/sample" label into a measured scale.
- **Identifier overlap:** Join cluster identifiers across the paired collections at each level. This answers whether the `kbase_*` records are a subset of, overlap with, or are disjoint from the 2026-01 release.
- **Release vintage:** Inspect table metadata, build records, or version fields of the `kbase_uniref*` collections to learn which UniRef release the sample came from, distinguishing Hypothesis 2 from Hypothesis 3.
- **Search behaviour:** Run "UniRef" as a catalog search query and record which collections it returns and in what order. This tests whether users without the tenant-qualified name are routed to the partial sample when the 2026-01 release was intended.
