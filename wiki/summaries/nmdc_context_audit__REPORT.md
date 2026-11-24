---
type: "Summary"
description: "Summary of the project NMDC Context Audit."
doc_type: "short"
full_text: "sources/nmdc_context_audit__REPORT.md"
---
# NMDC Context Audit

The NMDC Context Audit asked whether the label "NMDC" (National Microbiome Data Collaborative) is used consistently across the KBase Data Lakehouse. It found that 20 database names containing "nmdc" resolve to 7 real, maintained resources across three tenants and six provenance classes. [src: nmdc_context_audit] The report treats its hypothesis of a systematically overloaded label as supported. [src: nmdc_context_audit] The provenance classes are inferred, not read from an ingestion manifest, and the link between the label and bad resource choices is inferred rather than observed. [src: nmdc_context_audit]

## Key Findings

### The label is overloaded

NMDC is the National Microbiome Data Collaborative, a DOE-BER program. [src: nmdc_context_audit] Every one of the four predicted confusion modes is realized by an actual resource. [src: nmdc_context_audit] The report classifies the resources as follows:

| Resource | Class | Source |
|---|---|---|
| nmdc.metadata, nmdc.results | Genuine NMDC | NMDC program (DOE-BER) [src: nmdc_context_audit] |
| nmdc.ncbi_biosamples | External re-host | NCBI [src: nmdc_context_audit] |
| nmdc.ref_data | External re-host | Pfam consortium [src: nmdc_context_audit] |
| kbase.nmdc_arkin | Other-group derivation | LBNL Arkin Lab [src: nmdc_context_audit] |
| kbase.nmdc_mags | NMDC-derived, kbase tenant | KBase / NMDC [src: nmdc_context_audit] |
| kbase.nmdc_neon | Namesake collision | NEON (NSF), not NMDC [src: nmdc_context_audit] |

Two of the four databases in the nmdc tenant are external data re-hosted, not NMDC output. [src: nmdc_context_audit] nmdc.ncbi_biosamples holds 51,711,888 biosamples and 756,112,544 attribute rows. [src: nmdc_context_audit] nmdc.ref_data holds 27,481 Pfam terms. [src: nmdc_context_audit] NEON is the NSF National Ecological Observatory Network, a different program, so the acronym collision would corrupt agency attribution. [src: nmdc_context_audit]

Three NMDC-related databases (nmdc_arkin, nmdc_mags, nmdc_neon) sit in kbase. The inventory groups by catalog prefix, so they are invisible to anyone browsing the nmdc tenant. [src: nmdc_context_audit] The freshest NMDC resource, kbase.nmdc_mags (62,346 MAGs, metagenome assembled genomes), sits in the tenant where a user is least likely to look for NMDC. [src: nmdc_context_audit] The audit's knowledge inventory also labels kbase.nmdc_mags as the freshest resource. [src: nmdc_context_audit]

### Scale and currency differ widely

The genuine NMDC biosample universe is 16,640 samples in nmdc.metadata.biosample_set. The co-hosted NCBI mirror holds 51.7M, a ~3,000× difference that the names do not signal. [src: nmdc_context_audit] Iceberg snapshot ages differ by ~4 months across the label, and nothing surfaces this to users. [src: nmdc_context_audit]

| Resource | Last committed | Freshness |
|---|---|---|
| kbase.nmdc_mags | 2026-07-02 | freshest (days) [src: nmdc_context_audit] |
| kbase.nmdc_neon | 2026-07-02 | fresh [src: nmdc_context_audit] |
| kbase.nmdc_arkin | 2026-05-27 | ~6 weeks [src: nmdc_context_audit] |
| nmdc.metadata, nmdc.results, nmdc.ref_data | 2026-05-20 | ~7 weeks [src: nmdc_context_audit] |
| nmdc.ncbi_biosamples | 2026-03-09 | stalest (~4 months) [src: nmdc_context_audit] |

Iceberg `.snapshots.committed_at` is the only available currency signal, because the tables have no comments and there is no changelog. [src: nmdc_context_audit]

### Naming hazards

The naming hazards include aliases and globalusers.nmdc_core_test* test databases. [src: nmdc_context_audit] kbase_nmdc_neon is a phantom database with 0 tables. [src: nmdc_context_audit] mamillerpa/my.nmdc_flattened_biosamples is a broken user copy with a dangling Iceberg pointer. [src: nmdc_context_audit]

### Documentation and tooling give no help

The catalog has no table Comment and empty database Properties (owner tgu2), so it offers no human-readable context. [src: nmdc_context_audit] The canonical schema link docs/schemas/nmdc.md returns a 404 because docs/schemas/ does not exist. [src: nmdc_context_audit] docs/overview.md never mentions NMDC. [src: nmdc_context_audit] The berdl skill has zero NMDC content. [src: nmdc_context_audit] berdl_inventory.py groups purely by catalog prefix, so kbase.nmdc_* is never linked back to NMDC. [src: nmdc_context_audit] Even where documentation exists, berdl_data_atlas tags Rhea/GO (Gene Ontology) reference ontologies under nmdc_arkin as "NMDC integrated," which blurs provenance. [src: nmdc_context_audit]

Prior in-repository knowledge covers nmdc_arkin well but leaves the other six resources thinly documented or undocumented. [src: nmdc_context_audit] The report asserts that no prior artifact classifies the provenance of the label or measures its scale and currency spread. [src: nmdc_context_audit] It describes this audit as the first to enumerate all seven real resources with verified counts and snapshot ages, name the six provenance classes, and give a goal-to-resource decision guide. [src: nmdc_context_audit]

### Co-hosting is intentional, so the fix is to surface provenance

The NCBI mirror exists because the lakehouse adds an attribute-harmonization layer that makes 51.7M raw NCBI samples analytically usable. [src: nmdc_context_audit] The Arkin derivative adds embeddings and traits that do not exist upstream. [src: nmdc_context_audit] The report therefore argues against relabeling or removing resources and for surfacing provenance and value together. [src: nmdc_context_audit] It warns that treating the nmdc tenant as one coherent NMDC dataset will mis-scope or mis-attribute data. [src: nmdc_context_audit] NCBI BioSample and Pfam/InterPro are the true authorities for nmdc.ncbi_biosamples and nmdc.ref_data. [src: nmdc_context_audit]

### Practical lessons for lakehouse work

- Row counts on all NMDC tables return instantly through Iceberg metadata with `SELECT COUNT(*)`. This includes nmdc.results.annotation_kegg_orthology at 1.83B rows. [src: nmdc_context_audit]
- DESCRIBE DATABASE EXTENDED kbase.nmdc_* raises ForbiddenException for a kesciencero/microbialdiscoveryforge principal, although COUNT(*) on the same tables succeeds. Metadata introspection and data reads therefore have different access surfaces. [src: nmdc_context_audit]
- get_databases() returns both the dotted Iceberg alias and the underscore Hive alias for every tenant database. Deduplicate to the dotted form to avoid double-counting. [src: nmdc_context_audit] The broader namespace migration is already documented in docs/pitfalls.md. [src: nmdc_context_audit]

### Tables used by the audit

The audit queried specific tables in each resource, each for a stated purpose. [src: nmdc_context_audit]

| Database | Tables | Purpose |
|---|---|---|
| nmdc_metadata | biosample_set, study_set, data_generation_set, workflow_execution_set, functional_annotation_agg | Genuine NMDC metadata; scale/currency [src: nmdc_context_audit] |
| nmdc_results | annotation_kegg_orthology, annotation_statistics, gtdbtk_bacterial_summary, checkm_statistics | Genuine NMDC pipeline outputs [src: nmdc_context_audit] |
| nmdc_ncbi_biosamples | biosamples_flattened, biosamples_attributes, bioprojects_flattened, sra_biosamples_bioprojects | Establish NCBI, not NMDC, provenance and scale [src: nmdc_context_audit] |
| nmdc_ref_data | pfam_terms | Establish Pfam provenance [src: nmdc_context_audit] |
| kbase_nmdc_arkin | taxonomy_dim, metabolomics_gold, embeddings_v1, omics_files_table, study_table | Characterize the Arkin-lab derivation [src: nmdc_context_audit] |
| kbase_nmdc_mags | mag_catalog, bin_catalog, biosample_metadata, study_sample | MAG catalog scale/currency [src: nmdc_context_audit] |
| kbase_nmdc_neon | neon_mag_catalog, sample_data, study_sample | Characterize the NEON namesake [src: nmdc_context_audit] |

### Deliverables and recommended fixes

The primary deliverable is knowledge/, a 15-file Open-Knowledge-Format directory with one topic per file, full cross-links, and provenance, tenant, currency and authority frontmatter. [src: nmdc_context_audit] Its entry points are knowledge/README.md (index), knowledge/nmdc-label-is-overloaded.md (the thesis) and knowledge/nmdc-choosing-the-right-resource.md (a goal-to-resource decision guide). [src: nmdc_context_audit] The README is an index/map with a one-glance summary table, and the thesis file presents 3 tenants × 6 provenance classes. [src: nmdc_context_audit] The decision guide maps goals to resources. [src: nmdc_context_audit]

Other knowledge files cover the following topics:
- The NMDC program versus the nmdc tenant [src: nmdc_context_audit] and the four nmdc.* databases. [src: nmdc_context_audit]
- That nmdc.ncbi_biosamples is NCBI [src: nmdc_context_audit] and that nmdc.ref_data is Pfam. [src: nmdc_context_audit]
- The kbase.nmdc_* blind spot [src: nmdc_context_audit], Arkin-lab enrichment and join pitfalls [src: nmdc_context_audit], and NEON ≠ NMDC. [src: nmdc_context_audit]
- Scale and snapshot ages [src: nmdc_context_audit], and flattening, harmonization and embeddings added in the KBase Data Lakehouse. [src: nmdc_context_audit]
- Aliases, tests, phantom and broken databases [src: nmdc_context_audit], and a prior-project reuse map. [src: nmdc_context_audit]

Data outputs: data/nmdc_landscape.csv classifies each real resource by provenance, scale, currency and authority. [src: nmdc_context_audit] It has 7 rows covering per-resource provenance class, signature-table row count, currency and authority. [src: nmdc_context_audit] data/nmdc_naming_cruft.csv has 5 rows on aliases, test databases, phantom databases and broken NMDC-named databases. [src: nmdc_context_audit] data/provenance_probe.md holds the raw DESCRIBE, count and snapshot probe output. [src: nmdc_context_audit] The notebook 00_nmdc_landscape.ipynb enumerates every NMDC-named database, classifies provenance, counts rows using Iceberg, measures currency and renders figures. [src: nmdc_context_audit]

The report recommends five fixes and does not apply them. [src: nmdc_context_audit]
1. Repair the schema entry point: docs/schema.md:16 links to the nonexistent docs/schemas/nmdc.md. Creating or repointing it is the highest-value documentation fix. [src: nmdc_context_audit]
2. Add a berdl skill module, .claude/skills/berdl/modules/nmdc.md, covering the seven resources, provenance classes, join pitfalls and decision guide. [src: nmdc_context_audit]
3. Have berdl_inventory.py cross-link kbase.nmdc_arkin/mags/neon under the nmdc tenant as related but separate, and flag kbase.nmdc_neon as NEON. [src: nmdc_context_audit]
4. Add max(committed_at) to inventory output, because it is cheap and is the only currency signal users have. [src: nmdc_context_audit]
5. Retag Rhea/GO reference ontologies under nmdc_arkin in berdl_data_atlas as external reference. [src: nmdc_context_audit]

It also recommends two further items:
- Mention NMDC in `docs/overview.md` so top-level orientation acknowledges the collection. [src: nmdc_context_audit]
- Repair or drop the broken `mamillerpa/my.nmdc_flattened_biosamples` copies and the phantom `kbase_nmdc_neon` alias, through a commit/PR rather than ad-hoc filesystem operations. [src: nmdc_context_audit]

## Caveats and Open Work

- The evidence is consistent with the overloaded label driving sub-optimal resource selection. This is inferred from the gap analysis and prior-project usage skew, not from a directly observed wrong choice. [src: nmdc_context_audit]
- Wasted time and compute and weakened conclusions are plausible consequences of such mistakes, not observed outcomes. [src: nmdc_context_audit]
- Provenance classes are inferred from schema, table properties, tenant metadata and prior project usage. No ingestion manifest is exposed in the catalog. [src: nmdc_context_audit]
- kbase.nmdc_* database descriptions are access-restricted, so some metadata, such as steward-authored notes, could not be captured. [src: nmdc_context_audit]
- Completeness is assessed relative to snapshot timestamps. The audit did not compare against live upstream NMDC or NCBI record counts, which would need external API (application programming interface) calls and were out of scope. [src: nmdc_context_audit]
- The recommended fixes are for review and are not yet applied. [src: nmdc_context_audit]

Next analyses proposed by the report:
- Apply the schema-page and berdl skill NMDC module recommendations and measure whether new NMDC projects reach the right resource faster. [src: nmdc_context_audit]
- Add a lightweight currency/provenance annotation to berdl_inventory.py output so disambiguation is dynamic, not just documentary. [src: nmdc_context_audit]
- Extend the provenance-audit method to other overloaded labels in the KBase Data Lakehouse, such as any tenant co-hosting external mirrors. The report asserts that the six-class framework generalizes. [src: nmdc_context_audit]
- Diff nmdc.metadata and nmdc.ncbi_biosamples against live upstream record counts to quantify completeness lag precisely. [src: nmdc_context_audit]

## Slots Into

- [[concepts/provenance-overloading-of-dataset-labels-in-the-data-lakehouse]]: six provenance classes and four realized confusion modes behind the "nmdc" substring. [src: nmdc_context_audit]
- [[concepts/documentation-discovery-and-currency-gaps-in-lakehouse-catalogs-and-tooling]]: no catalog comments, a 404 schema link, and snapshot age as the only currency signal. [src: nmdc_context_audit]
- [[concepts/metadata-introspection-versus-data-read-access-in-spark-based-catalogs]]: DESCRIBE DATABASE EXTENDED is forbidden while COUNT(*) succeeds. [src: nmdc_context_audit]
- [[concepts/lakehouse-namespace-migration-tenancy-and-authentication]]: get_databases() returns dotted and underscore aliases that must be deduplicated. [src: nmdc_context_audit]
- [[entities/nmdc-neon-metagenome-studies]]: kbase.nmdc_neon is NEON (NSF), not NMDC. [src: nmdc_context_audit]
- [[entities/nmdc-integrated-collections]]: Rhea/GO ontologies under nmdc_arkin are tagged "NMDC integrated," which blurs provenance. [src: nmdc_context_audit]
