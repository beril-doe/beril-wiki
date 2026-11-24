---
type: "Concept"
description: "Missing catalog comments, broken doc links and tool mis-grouping that leave users without context on a resource, including snapshot age and row counts as the only currency signals; stops at specific proposed fixes."
sources: ["summaries/discoveries.md", "summaries/nmdc_context_audit__REPORT.md", "summaries/pitfalls.md"]
---
# Documentation, discovery and currency gaps in lakehouse catalogs and tooling

This page covers documentation, discovery and currency gaps in the KBase Data Lakehouse catalog and tooling. In the audited NMDC-labeled resources, the catalog carries no table comments and one canonical schema link is broken. The inventory tool groups resources by catalog prefix, which hides their origin. [src: nmdc_context_audit] For the audited resources, snapshot age is the only available currency signal. [src: nmdc_context_audit]

## Missing catalog context

In the audited catalog, tables carry no `Comment` and databases have empty `Properties` (owner `tgu2`), so the lakehouse itself gives no human-readable context. [src: nmdc_context_audit] For the audited resources, Iceberg `.snapshots.committed_at` is the only available data-currency signal, because there are no table comments and no changelog. [src: nmdc_context_audit]

## Broken or absent documentation

- The canonical NMDC schema link `docs/schemas/nmdc.md` returns a 404 because `docs/schemas/` does not exist. [src: nmdc_context_audit]
- `docs/overview.md` never mentions NMDC. [src: nmdc_context_audit]
- Even where docs exist, `berdl_data_atlas` tags Rhea/GO (Gene Ontology) reference ontologies under `nmdc_arkin` as "NMDC integrated," which blurs provenance. [src: nmdc_context_audit]
- Prior in-repository knowledge covers `nmdc_arkin` well but leaves the other six resources thinly documented or undocumented. [src: nmdc_context_audit]
- The report says no prior artifact classifies the provenance of the NMDC label or measures its scale and currency spread. [src: nmdc_context_audit]

## Tool mis-grouping

The `berdl` skill has zero NMDC content. [src: nmdc_context_audit] `berdl_inventory.py` groups purely by catalog prefix, so `kbase.nmdc_*` is never linked back to NMDC. [src: nmdc_context_audit] NMDC-derived data therefore sits in two tenant homes (`nmdc.*` and `kbase.nmdc_*`) with no cross-link. The freshest NMDC resource, `kbase.nmdc_mags` (62,346 MAGs, metagenome assembled genomes), is in the tenant a user is least likely to search for NMDC. [src: nmdc_context_audit]

The report also lists naming hazards. `kbase_nmdc_neon` is a phantom with 0 tables. [src: nmdc_context_audit] `mamillerpa/my.nmdc_flattened_biosamples` is a broken user copy with a dangling Iceberg pointer. [src: nmdc_context_audit]

## Scale and currency are invisible

Names do not signal scale. The genuine NMDC biosample universe in `nmdc.metadata.biosample_set` is 16,640 samples. The co-hosted NCBI mirror is 51.7M, a ~3,000× difference. [src: nmdc_context_audit] That mirror, `nmdc.ncbi_biosamples`, holds 51,711,888 biosamples and 756,112,544 attribute rows. [src: nmdc_context_audit] `nmdc.ref_data` is Pfam with 27,481 terms. [src: nmdc_context_audit]

Iceberg snapshot ages differ by ~4 months across the NMDC label, and nothing surfaces this to a user choosing a resource. [src: nmdc_context_audit] Last-commit dates from the report:

| Resource | Last committed | Freshness |
|---|---|---|
| `kbase.nmdc_mags` | 2026-07-02 | freshest (days) [src: nmdc_context_audit] |
| `kbase.nmdc_neon` | 2026-07-02 | fresh [src: nmdc_context_audit] |
| `kbase.nmdc_arkin` | 2026-05-27 | ~6 weeks [src: nmdc_context_audit] |
| `nmdc.metadata` / `nmdc.results` / `nmdc.ref_data` | 2026-05-20 | ~7 weeks [src: nmdc_context_audit] |
| `nmdc.ncbi_biosamples` | 2026-03-09 | stalest (~4 months) [src: nmdc_context_audit] |

## Gaps outside NMDC

- Historical static inventories lagged the live catalog and omitted several databases relevant to gut-microbiome and phage work. [src: discoveries]
- [[entities/phagefoundry]] has 7 databases in the tenant, not the 5 documented. [src: discoveries] The pitfalls report lists five: four genome browsers sharing the GenomeDepot schema, plus `phagefoundry_strain_modelling`, whose schema is unknown. [src: pitfalls]
- `pangenome_build_protocol`, `genomad_mobile_elements` and `IMG_env` are referenced by other tables or project docs but do not exist, so `protocol_id` is a dangling reference. [src: pitfalls]
- Many `enigma_coral` tables timed out during ingest introspection. Schemas may be partial, so confirm them with `DESCRIBE EXTENDED`. [src: pitfalls]
- `kbase_uniref50`, `kbase_uniref90` and `kbase_uniref100` are partial or sample datasets, so completeness cannot be assumed for cluster lookups. [src: pitfalls]

## Proposed fixes

The report recommends these fixes but did not apply them. [src: nmdc_context_audit]

1. Create `docs/schemas/nmdc.md` or repoint the link at `docs/schema.md:16`. The report calls this the single highest-value documentation fix. [src: nmdc_context_audit]
2. Add `.claude/skills/berdl/modules/nmdc.md`, covering the seven resources, provenance classes, join pitfalls and the decision guide. [src: nmdc_context_audit]
3. Have `berdl_inventory.py` note under the `nmdc` tenant that `kbase.nmdc_arkin/mags/neon` are related but separate, and flag `kbase.nmdc_neon` as NEON rather than NMDC. [src: nmdc_context_audit]
4. Add `max(committed_at)` to inventory output, since it is cheap and is the only currency signal users have. [src: nmdc_context_audit]
5. Retag Rhea/GO ontologies under `nmdc_arkin` in `berdl_data_atlas` as external reference. [src: nmdc_context_audit]
6. Mention NMDC in `docs/overview.md`. [src: nmdc_context_audit]
7. Repair or drop the broken `mamillerpa` copies and the phantom `kbase_nmdc_neon` alias, via commit or PR. [src: nmdc_context_audit]

The report's own next steps are to apply the schema page and NMDC skill module and measure whether new NMDC projects reach the right resource faster. [src: nmdc_context_audit] It also proposes lightweight currency and provenance annotations in `berdl_inventory.py` output, so disambiguation is dynamic rather than only documentary. [src: nmdc_context_audit] A third step is to diff `nmdc.metadata` and `nmdc.ncbi_biosamples` against live upstream record counts to quantify completeness lag. [src: nmdc_context_audit]

## Caveats

Completeness is judged relative to snapshot timestamps, not against live upstream NMDC or NCBI counts. Those comparisons were out of scope because they need external API (application programming interface) calls. [src: nmdc_context_audit] The report calls its audit the first to enumerate all seven real resources with verified counts and snapshot ages, name six provenance classes, and give a goal-to-resource decision guide. [src: nmdc_context_audit]

## Open Directions

- Apply the schema page and the `berdl` NMDC module, then measure whether new NMDC projects reach the right resource faster. This would test whether the documentation fixes work.
- Add currency and provenance annotations to `berdl_inventory.py` output, so disambiguation is dynamic rather than only documentary.
- Diff `nmdc.metadata` and `nmdc.ncbi_biosamples` against live upstream record counts to quantify completeness lag. This would close the snapshot-only caveat.
- Check whether the dangling `protocol_id` and the partial `enigma_coral` schemas have comparable catalog-level flags. This would show whether gaps beyond NMDC need the same fixes.
