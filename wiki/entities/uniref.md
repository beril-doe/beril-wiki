---
type: "Dataset"
description: "UniRef protein clusters at three redundancy levels (UniRef100, UniRef90, UniRef50) as held in the KBase Data Lakehouse, with snapshot counts, dataset variants and query caveats."
sources: ["summaries/berdl_data_atlas__REPORT.md", "summaries/pitfalls.md"]
---
**UniRef** is a set of protein clusters at three redundancy levels: UniRef100, UniRef90 and UniRef50. In the KBase Data Lakehouse it appears in two groups. One is the `refdata_uniref*` reference-data collections. The other is the `kbase_uniref*` datasets [src: berdl_data_atlas, pitfalls].

## Collections in the KBase Data Lakehouse

The reference-data collections `refdata_uniref50_2026_01`, `refdata_uniref90_2026_01` and `refdata_uniref100_2026_01` each contain a `cluster` table. They hold UniRef protein clusters at the three redundancy levels, taken from a 2026-01 snapshot [src: berdl_data_atlas].

The platform's protein and structure inventory lists 215,130,942 [[entities/uniprot]] proteins. It lists 475,217,233 UniRef100, 188,848,220 UniRef90 and 60,315,044 UniRef50 clusters as of 2026-01. It also lists 241,070,489 AlphaFold predicted structures ([[entities/kescience-alphafold]]) and ~253K experimental PDB structures ([[entities/protein-data-bank]]). These are inventory counts reported directly by the source [src: berdl_data_atlas].

A separate group of datasets is named `kbase_uniref50`, `kbase_uniref90` and `kbase_uniref100`. These are partial or sample datasets, not the full UniRef releases, which would be hundreds of millions of clusters. A cluster lookup against them should not assume completeness [src: pitfalls].

## Query Caveats

To join UniRef100 to UniProt, you must strip the `UniRef100_` prefix, for example `REPLACE(uniref100, 'UniRef100_', '') = uniprot_accession`. This is a per-row string operation, so for large joins it may help to materialize a mapping table first [src: pitfalls].

## Tensions

The two sources describe UniRef coverage differently. The data atlas reports full-scale 2026-01 cluster counts and names the `refdata_uniref*` collections [src: berdl_data_atlas]. The pitfalls digest warns that the `kbase_uniref*` datasets are partial samples, not full releases [src: pitfalls]. The two sources name different table groups, so both statements may hold for their own tables. Neither source says how the `refdata_*` and `kbase_*` collections relate. Before assuming a query is complete, check which collection it uses [src: berdl_data_atlas, pitfalls].

## Related

- [[data/kbase-uniref]] is the data page for the `kbase_uniref*` datasets [src: pitfalls].
- [[summaries/berdl_data_atlas__REPORT]] is the source of the inventory counts and the snapshot date [src: berdl_data_atlas].
- [[summaries/pitfalls]] is the source of the join and completeness caveats [src: pitfalls].
