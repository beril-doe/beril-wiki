---
type: "Concept"
description: "Concept page arguing that resource discovery in the KBase Data Lakehouse must expose provenance, authority, scale, tenant placement, access status, content gaps, and data currency together rather than relying on resource names."
sources: ["summaries/nmdc_context_audit__REPORT.md", "summaries/paperblast_explorer__REPORT.md", "summaries/pitfalls.md", "summaries/soil_frontier_genomics__REPORT.md", "summaries/webofmicrobes_explorer__REPORT.md", "summaries/alphafold_msa_annotation__REPORT.md", "summaries/berdl_data_atlas__REPORT.md", "summaries/discoveries.md", "summaries/ibd_phage_targeting__REPORT.md", "summaries/snipe_defense_system__REPORT.md"]
---
# Provenance, scale, and currency must be exposed during resource discovery

Resource discovery should expose provenance, authority, scale, tenant placement, access conditions, and data currency together rather than treating a name or catalog prefix as a sufficient dataset boundary. The [[summaries/nmdc_context_audit__REPORT]] provides direct evidence that the `nmdc` label is systematically overloaded across maintained resources, while the consequences for user selection remain an inferred hypothesis rather than a directly observed causal effect. The [[summaries/pitfalls]] extends this requirement from catalog interpretation to executable workflows: live namespace, schema, identifier, join, and interface checks are needed before a resource can be treated as a valid analytical input. The [[summaries/soil_frontier_genomics__REPORT]] **supports** the same principle from a spatial-genomics setting: discovery metrics must distinguish sampling gaps, completeness, scale, and analytical validity rather than compressing them into a single index. The [[summaries/webofmicrobes_explorer__REPORT]] **supports** the combined requirement from a cross-collection metabolomics setting: the 2018 Web of Microbes (WoM) snapshot is useful only when its archived provenance, small organism and metabolite scale, available access surfaces, and freshness limitations are presented together. [src: nmdc_context_audit] [src: pitfalls] [src: soil_frontier_genomics] [src: webofmicrobes_explorer]

## Core claim

A resource name is not reliable evidence of what a dataset contains, who maintains it, how large it is, or how current it is. The audit resolved 20 database names containing `nmdc` to 7 real, maintained resources in six provenance classes. It describes these as spread across three tenants, but it names those three as `nmdc`, `kbase`, plus broken user copies. The maintained resources it lists all sit in the `nmdc` and `kbase` tenants. The three-tenant figure therefore includes broken user copies and should not be read as the tenant scope of the seven maintained resources alone; the report leaves this inconsistency unreconciled. [src: nmdc_context_audit]

The seven resources include genuine NMDC resources (`nmdc.metadata` and `nmdc.results`), an NCBI re-host (`nmdc.ncbi_biosamples`), a Pfam re-host (`nmdc.ref_data`), an Arkin Lab derivative (`kbase.nmdc_arkin`), an NMDC-derived KBase resource (`kbase.nmdc_mags`), and a namesake collision representing NEON rather than NMDC (`kbase.nmdc_neon`). [src: nmdc_context_audit]

The audit's naming-hazard inventory **supports** this from the residue. Besides the seven maintained resources, the 20 `nmdc` database names include test databases (`globalusers.nmdc_core_test*`), a phantom `kbase_nmdc_neon` alias with 0 tables, and broken user copies such as `mamillerpa/my.nmdc_flattened_biosamples` with a dangling Iceberg pointer; only 7 of 20 are real, maintained resources. The audit reports its hypothesis H1 as supported, with every one of the four predicted confusion modes realized by an actual resource. Its provenance classes are themselves inferences from schema, table properties, tenant metadata, and prior project usage, because no ingestion manifest is exposed in-catalog. [src: nmdc_context_audit]

This finding **supports** [[concepts/provenance-aware-resource-discovery]] as a distinct discovery requirement: users need provenance and authority annotations at the point of search, not only in downstream documentation. [src: nmdc_context_audit]

The PaperBLAST inventory **supports** the same requirement from a different resource class: `kescience_paperblast` contains 12.4 million rows across 14 tables linking sequences and genes to literature, annotations, structures, and full-text snippets, so a collection name alone does not convey its analytical scope or evidentiary boundaries. [src: paperblast_explorer]

The WoM assessment **refines** this claim by showing that a resource card must also distinguish a historical snapshot from a current service. The project analyzed a 2018 WoM export accessed through the Wayback Machine, and identified GNPS2 and Northen laboratory datasets as possible newer alternatives; the archived export therefore cannot be treated as a current representation without an explicit freshness warning. [src: webofmicrobes_explorer]

The migration from Delta to Iceberg **refines** this claim: live discovery must expose the currently valid address as well as the logical resource identity. Migrated tables use `catalog.namespace.table`, while former Delta references flatten the namespace into a single underscore-joined identifier; what is now `kbase.ke_pangenome.genome` was previously `kbase_ke_pangenome.genome`, so only the leading separator changes, not the table name. A query copied verbatim from an older project's README, REPORT, notebook, or `.py` file will use the underscore form and fail with `TABLE_OR_VIEW_NOT_FOUND` or an unresolved-relation error against a migrated collection. Hundreds of archived project files keep underscore-form references and are intentionally not rewritten, because they are historical. Migration remains incomplete, so a collection whose dotted namespace cannot be found may still be Delta-only and correctly addressed in underscore form. Tooling should therefore resolve the current address through live, access-aware catalog discovery (for example `SET` and parsing `spark.sql.catalog.*`, or the notebook helpers) rather than hardcoding either form or applying a blanket underscore-to-dot rewrite. [src: pitfalls]

The soil-frontier analysis **supports** exposing analytical status and metric definitions alongside resource identity. Its Genomic Discovery Index (GDI), defined as OTU Richness / (Mean Genome Completeness + 1), identified uneven genomic representation, but the report cautions that the novel index conflates richness with completeness and can equal 902 even when there are zero genomes. Discovery cards should therefore expose the underlying measures, formula, and validation status rather than presenting a composite score as self-explanatory. [src: soil_frontier_genomics]

## Scale is a selection variable

The `nmdc` tenant is neither exclusively NMDC nor the only location of NMDC-related resources. Two of its four databases are external re-hosts: `nmdc.ncbi_biosamples` contains 51,711,888 biosamples and 756,112,544 attribute rows, while `nmdc.ref_data` contains 27,481 Pfam terms. Conversely, three NMDC-related databases (`nmdc_arkin`, `nmdc_mags`, `nmdc_neon`) live in the `kbase` tenant. Because the inventory groups by catalog prefix, they are filed under "kbase" and are invisible to anyone browsing the `nmdc` tenant. [src: nmdc_context_audit]

The genuine NMDC biosample universe contains 16,640 samples in `nmdc.metadata.biosample_set`, whereas the co-hosted NCBI mirror contains 51,711,888 biosamples. The audit identifies this as a ~3,000× scale trap, so discovery interfaces should display row or object counts and resource role before users query a dataset. [src: nmdc_context_audit]

Row counts for NMDC tables, including `nmdc.results.annotation_kegg_orthology` with 1.83B rows, returned instantly through Iceberg metadata using `SELECT COUNT(*)`. [src: nmdc_context_audit]

The PaperBLAST inventory **supports** treating scale as first-class discovery metadata: its largest tables include 3,195,890 gene-to-paper links and 1,951,949 text excerpts, while its sequence analysis clustered 815,571 proteins at multiple identity thresholds. These figures describe distinct objects and should be shown with table or collection roles rather than collapsed into one size number. [src: paperblast_explorer]

Scale metadata should therefore be treated as inexpensive discovery metadata rather than as an expensive exploratory query. This **refines** [[concepts/cross-tenant-data-bridging]] by showing that cross-tenant linking must carry comparable scale information, not merely database names and locations. [src: nmdc_context_audit]

The WoM assessment **supports** making scale and coverage visible before cross-collection use: its 2018 snapshot contains 37 organisms and 589 metabolites, with 332 (56.4%) metabolites unidentified and only 20 experimental organisms. Its 5 ENIGMA-funded projects, media, organism coverage, and single-laboratory origin define a substantially narrower evidence base than the linked Fitness Browser or pangenome resources. [src: webofmicrobes_explorer]

The pitfalls evidence **supports** displaying scale together with execution constraints: pangenome tables include approximately 1B-row `gene` and `gene_genecluster_junction` tables, approximately 421M-row `genome_ani`, approximately 93M-row `eggnog_mapper_annotations`, approximately 833M-row `interproscan_domains`, approximately 572M-row `bakta_db_xrefs`, and approximately 305M-row `gapmind_pathways`. Such resources require key filters before joins and should remain in Spark until the final small output. [src: pitfalls]

The soil-frontier GDI analysis **refines** scale metadata by showing that richness and genome completeness can diverge spatially: forest had GDI = 902.36 and cropland had GDI = 890.82, while grassland had GDI = 503.42 and wetland had GDI = 525.13. Forest and cropland should be described as jointly highest-GDI biomes, not ranked, because their difference was only 1.3% and no bootstrap confidence intervals were reported. [src: soil_frontier_genomics]

The BERDL Data Atlas project **supports** treating scale as first-class discovery metadata. It also **refines** that requirement: each count must state its counting unit. Its depth inventory queried 65 curated headline tables on the live cluster with `COUNT(*)` or `COUNT(DISTINCT)`. It found the KBase Data Lakehouse simultaneously deep across genomes, genes, proteins, structures, phenotype/fitness, samples, community profiles, mass spec, viruses, biochemistry, ontology, environment, and literature. The single largest entity table was `kbase_ke_pangenome.gene` at 1,011,650,903 rows (~3.4K genes × 293K genomes). Most of these depth counts are row totals. Only the canonical KBase genome count uses `COUNT(DISTINCT genome_id)`. A pangenome gene row is one genome–gene pair, so the report relates 1.01B genes to 293K genomes × ~3.4K genes per genome. The volumes are plotted in two figures. `nb05_volume_by_entity_class.png` shows per-entity-class volume on a log scale with exact counts. `nb05_volume_per_table.png` shows every headline table on a log scale, colored by entity class. [src: berdl_data_atlas]

The atlas inventory shows why resource cards need per-collection counts rather than a single size. For genomes, pangenomes, and clusters it lists:
- 293,059 KBase ke_pangenome genomes
- 27,690 GTDB species clades / pangenomes
- 132.5M gene clusters
- 1,011,650,903 KBase pangenome genes
- 1,158,553 SPIRE MAGs (metagenome-assembled genomes) and 52,515 JGI GEM-MAGs in refdata
- 3,110 ENIGMA depot genomes (6,705 ENIGMA SDT genomes)
- 4,923 PROTECT MIND genomes
- ~1,950 PhageFoundry host genomes across 5 host species [src: berdl_data_atlas]

For proteins and structures it lists 215,130,942 UniProt proteins; 475,217,233 UniRef100, 188,848,220 UniRef90, and 60,315,044 UniRef50 clusters (2026-01); 241,070,489 AlphaFold predicted structures; and ~253K PDB experimental structures. [src: berdl_data_atlas]

Phenotype holdings come in different units again: 27,410,721 FitnessBrowser per-gene fitness measurements across 7,552 experiments and 228,709 genes; 97,334 BacDive strain phenotype profiles; 57,302 carbon-source phenotype measurements; and 10,744 Web of Microbes growth observations across 37 organisms. Field and environmental holdings include:
- 463,972 MicrobeAtlas 16S samples (98,919 OTUs, 260,831,135 OTU-count rows)
- 114,943 USGS produced-water samples
- 16,640 NMDC biosamples
- 5,438 NETL produced-water DNA samples
- 4,346 ENIGMA SDT samples plus 579 ENIGMA DDT measurement “bricks”
- 2,371 Planet Microbe samples
- 218,510 ENIGMA SDT ASVs (amplicon sequence variants, exact-sequence 16S units)
- 83,287 AlphaEarth environment embeddings indexed to KBase genomes [src: berdl_data_atlas]

The atlas's 16,640 NMDC biosamples **support** the genuine-biosample count from the NMDC audit. Its 37 Web of Microbes organisms **support** the organism count of the WoM snapshot reported above. [src: berdl_data_atlas, nmdc_context_audit, webofmicrobes_explorer]

Community, viral, and reference holdings add further distinct units:
- 75,119,498 metatranscriptomic abundance rows (NMDC GOLD)
- 29,023,980 kraken and 482,669 gottcha taxonomic profile rows
- 9,928,244 NOM mass spec assignments
- 24,435,662 MetaVR and 15,677,623 IMG/VR viral sequence records (refdata)
- 933,103 PhageFoundry strain-modelling gene records
- 56,012 ModelSEED reactions, 45,708 compounds, and 17,783 Rhea reactions
- 48,196 GO terms and 8,813 EC terms, which the atlas labels “NMDC integrated”
- 255,096 PaperBLAST curated genes plus 39,994,988 PubMed article records [src: berdl_data_atlas]

The atlas also **refines** how such counts may be combined. Its inventory audit walks the Spark catalog and tags every table by tenant, agency, and biological topic. It deduplicates dotted-namespace duplicates and audits an unclassified residual of 0.9 %. This **supports** the alias de-duplication requirement described under access surfaces below. That catalog-level deduplication is distinct from record-level deduplication, because across-tenant deduplication is not performed. Refdata and kbase may both house the same UniProt entries through different cluster indices. ENIGMA and the genome-depot tables share genome records with the ENIGMA SDT layer. Counts from different tenants therefore cannot be added into a unique-entity total without explicit cross-tenant reconciliation. [src: berdl_data_atlas]

## Currency must be visible

Iceberg snapshot age—the available signal for data currency in this audit—spanned approximately four months across NMDC-labeled resources. Nothing surfaced this difference to a user choosing a resource. The latest commits were `2026-07-02` for `kbase.nmdc_mags` and `kbase.nmdc_neon`, `2026-05-27` for `kbase.nmdc_arkin`, `2026-05-20` for `nmdc.metadata`, `nmdc.results`, and `nmdc.ref_data`, and `2026-03-09` for `nmdc.ncbi_biosamples`. [src: nmdc_context_audit]

Iceberg `.snapshots.committed_at` is the only available data-currency signal for these resources. Catalog tables carry no `Comment`, databases have empty `Properties`, and there is no changelog. The lakehouse itself therefore provides zero human-readable context for them. The audit recommends surfacing `max(committed_at)` in discovery tooling. Completeness was accordingly assessed relative to snapshot timestamps, not by diffing against live upstream NMDC or NCBI record counts; the audit placed that comparison out of scope because it would require external API calls. [src: nmdc_context_audit]

A project-level data mart shows what the missing catalog context could look like. It **refines** the recommendation from a single timestamp to a documentation bundle. The UC Davis / Arkin CrohnsPhage data mart ships with four kinds of documentation:
- a `lineage.yaml` file holding ETL provenance, a changelog, and known gaps
- a `schema_overview.yaml` table inventory by category
- per-table `*.yaml` dictionaries with columns, dtypes, null counts, unique counts, and sample values
- a `ref_missing_data_codes` table whose sentinel codes, such as `PENDING_DAVE_LAB`, `PENDING_KUEHL`, and `PENDING_HMP2_RAW`, distinguish real NULLs from known-pending data [src: discoveries]

The digest proposes this pattern as a BERIL convention because it makes large local marts agent-readable without live queries. It is a single-mart example, not a tested lakehouse-wide standard. [src: discoveries]

The freshest NMDC-related resource was `kbase.nmdc_mags`, containing 62,346 MAGs, but it was located in the `kbase` tenant rather than the `nmdc` tenant. NMDC-derived data are split across two tenant homes (`nmdc.*` and `kbase.nmdc_*`) with no cross-link. The freshest NMDC resource therefore sits in the tenant a user is least likely to search for NMDC. [src: nmdc_context_audit]

PaperBLAST **supports** making temporal coverage and snapshot information visible: its collection contains papers from 1951 to 2026, publications peak around 2020–2021 with 30.6% of records from 2020 onwards, and the 2025 data include 125,438 records from 22,271 papers. The early-2026 snapshot date is inferred from the presence of 1,425 records from 2026, not read from snapshot metadata. Publication-year coverage is not equivalent to ingestion currency, so resource cards should distinguish the two rather than use either as a substitute for `max(committed_at)`. [src: paperblast_explorer]

WoM **supports** the same distinction between temporal coverage and ingestion currency: the analyzed data are a frozen 2018 snapshot retrieved through the Wayback Machine, while the report points to GNPS2 or Northen laboratory datasets as potentially newer sources. The snapshot's action semantics and missing consumption records must therefore be labeled as properties of that export, not assumed to describe the current WoM resource. The report adds that the Wayback Machine archive may not reflect the current state of WoM. It names the GNPS2-hosted version or the Northen laboratory's internal datasets, including the NLDM 110-organism panel from de Raad et al. 2022, as substantially richer, but those datasets were not analyzed. [src: webofmicrobes_explorer] The pitfalls notes independently **support** this freshness label: they describe the WoM data as a 2018 frozen snapshot whose newer data live elsewhere (GNPS2). [src: pitfalls]

This **supports** [[concepts/pangenome-integration]] by establishing that resource selection for MAG-based analyses depends on both catalog scale and snapshot currency, while tenant placement can conceal the relevant resource. [src: nmdc_context_audit]

The pitfalls document **refines** freshness metadata into an operational requirement: schemas, namespace availability, permissions, database contents, and naming conventions can change, so archived reports and notebooks should be treated as historical records rather than automatically valid executable instructions. [src: pitfalls]

The central digest and the atlas **support** this historical-record caution for inventories themselves. Historical static inventory files lagged the live lakehouse catalog. [src: discoveries] The atlas designs `build_inventory.py` and `data_volume.py` to be re-run. They rebuild the canonical CSVs from the live cluster in ~95 s and ~60 s respectively, and the report recommends re-running them at each major ingest milestone. [src: berdl_data_atlas]

Snapshot currency also matters for derived structural features. The KBase Data Lakehouse AlphaFold database is a single version-6 snapshot. Newly deposited UniProt entries may change MSA (multiple sequence alignment) depths as databases grow, so MSA-depth annotations should carry the snapshot version. This is a caveat stated by a single project, not a measured drift. [src: alphafold_msa_annotation] The pitfalls notes **support** the single-version description. All entries are model version v6, and the `model_version` column exists but currently has no variation, so the field does not yet record any version difference. [src: pitfalls]

The soil-frontier report **supports** treating validation status as part of freshness and provenance. Its clay-shield and GDI analyses were complete, but spatial validation and figures remained pending; the report also required re-running from BERIL Observatory 16S tables and `kbase_ke_pangenome` completeness data because no local CSV output was available. [src: soil_frontier_genomics]

## Provenance and authority are separate fields

The authority context is heterogeneous: NMDC is the National Microbiome Data Collaborative of DOE-BER; NEON is the National Ecological Observatory Network of NSF; NCBI BioSample is the authority for `nmdc.ncbi_biosamples`; and Pfam/InterPro is the authority for `nmdc.ref_data`. [src: nmdc_context_audit]

`kbase.nmdc_neon` represents NEON rather than NMDC, so interpreting the namesake as NMDC would create an agency-attribution error. [src: nmdc_context_audit]

The audit also found provenance blur in the KBase Data Lakehouse data atlas, which labels Rhea and Gene Ontology reference ontologies under `nmdc_arkin` as “NMDC integrated.” [src: nmdc_context_audit]

The BERDL Data Atlas **supports** keeping provenance fields separate. It produced a machine-readable catalog (`table_topic_map.csv`) with tenant, agency, program, and biological-topic provenance, which the report describes as the first comprehensive such catalog. The audit's provenance-blur finding **qualifies** that support. A provenance field is only as reliable as its assignment, and the atlas's own “NMDC integrated” label on reference ontologies is the error the audit identifies. [src: berdl_data_atlas, nmdc_context_audit]

Provenance should also extend to the evidence behind inventory numbers. The atlas describes NMDC's metabolomics (3.1M), proteomics (346K), and lipidomics (1.4M) layers as largely untapped despite being a primary cross-validation source. It attributes those counts only to agent memory, not to its measured live-cluster inventory. They should therefore be treated as unverified until re-counted. [src: berdl_data_atlas]

Provenance should describe both origin and transformation. The NCBI mirror adds an attribute-harmonization layer to 51,711,888 raw NCBI samples, while the Arkin derivative adds embeddings and traits that do not exist upstream. [src: nmdc_context_audit]

The PaperBLAST analysis **refines** this requirement by identifying a specific transformation and coverage boundary: it combines database inventory with text-mined PubMed Central full-text links, curated annotations, structural records, and MMseqs2 sequence clustering. PMC-only mining misses paywalled literature, and the report estimates that only 19% of SwissProt is represented, so provenance cards should expose both source inputs and missing-coverage mechanisms. [src: paperblast_explorer]

These observations **support** [[concepts/multi-omics-integration]]: value-added derivatives can be useful integration resources, but their derived status, upstream authority, and added data products must remain explicit. [src: nmdc_context_audit]

The WoM bridge **supports** preserving provenance at the level of compound identity and cross-collection mapping. Of 257 identified, non-unknown compounds, 69 (26.8%) had definitive ModelSEED links through exact name matching, while 107 (41.6%) had formula-only candidate links; those 107 expanded to 900 ModelSEED molecules, making formula-only matches unsuitable as definitive identifications. [src: webofmicrobes_explorer]

The pitfalls evidence **supports** preserving provenance at join level, not only collection level. Short ENIGMA strain names are not globally unique: one erroneous linkage matched ENIGMA MT20 (*Rhodanobacter glycinis*) to GTDB MT20 (*Streptococcus pneumoniae*), involving 8,434 genomes including 1,751 clinical genomes; 12 of 32 pangenome linkages through `ncbi_strain_identifiers` were incorrect genus matches. Assembly accessions such as `GCF_*`, genus checks, synonymy layers, and explicit bridge keys therefore belong in resource metadata and workflow provenance. [src: pitfalls]

The soil-frontier analysis **refines** provenance requirements by separating database sampling gaps from biological or technical assembly gaps. Frontier areas with GDI > 1000 had mean pH = 6.74, compared with mean pH = 5.94 in mapped areas, a +0.8 pH unit gap; however, the report notes that this could reflect fewer sequenced samples from those pH ranges rather than harder assembly or lower study effort. The number of 16S samples per pH bin must therefore accompany completeness and richness before the gap is interpreted biologically. [src: soil_frontier_genomics]

Resource cards should also expose known content gaps. The atlas's validated UC1 cohort (use case 1, a proposed structural fitness atlas) contains 55,454 genes. However, `kescience_alphafold.alphafold_entries` does not carry per-residue pLDDT (AlphaFold's per-residue prediction-confidence score) or structural-feature data. Those features would need to be ingested or computed from PDB files as a derived collection. [src: berdl_data_atlas]

Referenced-but-absent tables are a further content gap. As of 2026-02-11, `phylogenetic_tree` and `phylogenetic_tree_distance_pairs` were available. By contrast, `pangenome_build_protocol`, `genomad_mobile_elements`, and `IMG_env` are referenced by other tables or project docs but were not found in the KBase Data Lakehouse. Because a `protocol_id` column exists, it is a dangling reference. A resource card that lists declared references without checking them would overstate what can be joined. [src: pitfalls]

Empty and mirrored tables need the same labelling. In the PlanetMicrobe databases `planetmicrobe_planetmicrobe` and `planetmicrobe_planetmicrobe_raw`, the `project` and `library` tables are empty (count=0), so joins through them return nothing. The `_raw` database mirrors the curated one structurally, so each query should pick one explicitly. Separately, four structural-biology tables start empty and grow only with Phenix agent usage, so cross-project queries return nothing until projects accumulate. A schema listing alone would present all of these tables as available data. [src: pitfalls]

Registration is not ingestion. In ENIGMA CORAL, 221 METALS/ICTOC/ISOTOPES/NH3NO2 sample tubes from the SSO Subsurface Observatory campaign are registered in `sdt_sample`, but zero `Assay Geochemistry` processes are linked. The analytical measurement values were never ingested. A sample count alone would therefore overstate the measurement data available. [src: discoveries]

Citation provenance can likewise live outside the record that uses it. In the IBD phage-targeting project, the gut-microbiome biosynthetic gene cluster catalog (Elmassry et al., 2025) is referenced through `ref_bgc_catalog` metadata. The strain-frequency / IBD-adaptation reference (Kumbhari et al., 2024) comes from `ref_kumbhari_s7_*` supplementary material. For both, the report states that the full citation is held in `dim_studies`. Resource cards for derived tables should therefore carry or link that study dimension. [src: ibd_phage_targeting]

## Discovery has multiple access surfaces

`get_databases()` returns dotted Iceberg aliases such as `nmdc.metadata` and underscore Hive aliases such as `nmdc_metadata` for every tenant database, so consumers must de-duplicate to the dotted form before iteration to avoid double-counting. [src: nmdc_context_audit]

`DESCRIBE DATABASE EXTENDED kbase.nmdc_*` raised `ForbiddenException` for a `kesciencero`/`microbialdiscoveryforge` principal even when `COUNT(*)` on the same tables succeeded, demonstrating that metadata introspection and data reads have different access surfaces. As a result, some metadata for the `kbase.nmdc_*` databases, such as any steward-authored notes, could not be captured. [src: nmdc_context_audit]

Static and dynamic documentation also omit the NMDC provenance link. The canonical NMDC schema link `docs/schemas/nmdc.md` returns a 404 because `docs/schemas/` does not exist, and `docs/overview.md` never mentions NMDC. The platform's discovery skill has zero NMDC content. The `berdl_inventory.py` tool groups resources purely by catalog prefix and therefore never links `kbase.nmdc_*` resources back to NMDC. Prior in-repo knowledge in `docs/pitfalls.md` and `docs/discoveries.md` covers `nmdc_arkin` well. However, it leaves the other six resources thinly documented or undocumented, consistent with the audit's gap analysis. [src: nmdc_context_audit]

The central discoveries digest **supports** walking the live catalog rather than relying on documentation. It lists resources that were present in the tenant but missing from, or misdescribed in, documentation:
- `kescience_mgnify`: EBI MGnify, relevant for IBD-cohort cross-validation, and the correct name for a mis-recalled `ke_science_magnify`
- `phagefoundry_ecoliphages_genomedepot` plus a duplicate `_genomedepot` variant: an E. coli phage collection relevant for targeting adherent-invasive E. coli (AIEC); PhageFoundry has 7 databases in the tenant, not the 5 documented
- `kescience_interpro`: InterPro domain annotations
- `kescience_pubmed`: literature text mining, sibling to `kescience_paperblast`
- `pangenome_bakta`: a Bakta-pangenome slice distinct from `kbase_ke_pangenome`
- `arkinlab_microbeatlas`: described as 464K global 16S samples [src: discoveries]

The digest's 464K MicrobeAtlas figure and the atlas's 463,972 MicrobeAtlas 16S samples are reported at different precision. [src: discoveries, berdl_data_atlas]

PhageFoundry shows how splitting a collection across databases can hide its experimental core. The GenomeDepot browser databases (`phagefoundry_{species}_genome_browser_genomedepot`) contain genome annotations only, from eggNOG, COG (Clusters of Orthologous Groups), and Pfam, in `browser_*` tables (10+ tables each). The separate `phagefoundry_strain_modelling` database holds experimental phage-host interaction data and a machine-learning model in 18 tables. These are the actual experimental results of Gaborieau et al. 2024 (*Nature Microbiology*), so searching only the browsers would miss them. [src: pitfalls] The SNIPE project **supports** this as a realized discovery failure. The strain-modelling database was previously overlooked and documented as "timed out during discovery", yet it contains 18 tables of experimental phage-host phenotype data. [src: snipe_defense_system] Within it, `strainmodelling_gene` has 933K genes but only `locus_tag` and `protein_seq` columns, with no `gene_name`, `product`, or functional annotation fields, so genes cannot be searched by name. Instead, the `strainmodelling_feature` and `strainmodelling_protein_family` tables link gene clusters to model features with SHAP (Shapley additive explanation) importance scores. [src: pitfalls] The atlas's 933,103 PhageFoundry strain-modelling gene records and the pitfalls figure of 933K are reported at different precision. [src: berdl_data_atlas, pitfalls]

These constraints **refine** [[concepts/provenance-aware-resource-discovery]]: discovery tooling should expose an access-aware resource card using available table metadata, while not assuming that database-description APIs are universally readable. [src: nmdc_context_audit]

The PaperBLAST collection provides a further **supporting** example for access-aware linkage: 129,823 VIMSS cross-references connect its literature records to Fitness Browser phenotypes, creating a useful bridge whose meaning depends on preserving both collection provenance and cross-tenant identifiers. [src: paperblast_explorer]

WoM **supports** recording access surfaces and integration status separately from biological content. Its source tables, notebooks, and generated link files enabled links to Fitness Browser, ModelSEED, GapMind, and pangenomes, but GapMind matching was blocked by internal pathway identifiers, and species-level pangenome matching was not attempted. These are discoverability and reproducibility constraints, not evidence that the underlying biological relationships are absent. [src: webofmicrobes_explorer]

The pitfalls document **supports** separating access status from resource identity. Tenant and dataset names can be mis-combined—for example, `kbase_ke` is not the tenant for the `kbase.ke_pangenome` dataset—and access failures should identify the unreachable table and tenant without exposing internal service strings. Direct Spark SQL is preferred for complex or large queries because REST requests can return 504, 524, or 503 errors, while REST `/count` and `/schema` are unreliable for repeated or large-table discovery. [src: pitfalls]

Documented schemas can also be wrong. Several Fitness Browser tables differ from their documented schema:
- `keggmember` uses `keggOrg`/`keggId` rather than `orgId`/`locusId` and must be joined through `besthitkegg`
- `kgroupec` uses `ecnum` rather than `ec`
- `seedclass` has `orgId, locusId, type, num` rather than a subsystem/category hierarchy
- `fitbyexp_*` tables are long format (columns `expName, locusId, fit, t`) rather than pre-pivoted as documented. They are equivalent to a per-organism slice of `genefitness`, so `genefitness` with an `orgId` filter can be used directly [src: discoveries, pitfalls]

This **supports** the pitfalls requirement for live schema checks: a resource card should carry the observed schema, not only the documented one. [src: discoveries, pitfalls]

Further pitfalls entries **refine** that requirement, adding table roles and completeness to the observed schema:
- In `enigma_coral`, prefixes distinguish scientific data (`sdt_*`), numerical bricks/arrays (`ddt_*`), and system/metadata tables (`sys_*`). The `sys_*` tables are not primary scientific data and should not be queried for biology.
- Many `enigma_coral` tables timed out during introspection at ingest. Their schemas may be partial and should be confirmed with `DESCRIBE EXTENDED` before writing queries.
- `protect_genomedepot` exposes sampled variants (`browser_gene_sampled`, `browser_annotation_sampled`) instead of full tables. Queries should use the sampled tables, not the un-suffixed names.
- `kbase_uniref50`, `kbase_uniref90`, and `kbase_uniref100` are described as partial/sample datasets, not the full UniRef releases, so no cluster lookup should assume completeness. [src: pitfalls]

## Tensions

The audit identifies a tension between intentional co-hosting and unambiguous attribution. Co-hosting can provide useful re-hosted and value-added resources, but the same naming pattern can cause users to confuse NMDC, NCBI, Pfam/InterPro, Arkin-derived, and NEON resources. [src: nmdc_context_audit]

The audit also identifies a tension between a compact catalog view and accurate cross-tenant discovery: prefix-based grouping is simple, but it can hide `kbase.nmdc_mags`, `kbase.nmdc_arkin`, and `kbase.nmdc_neon` from searches focused on the `nmdc` tenant. [src: nmdc_context_audit]

The report does not directly observe users choosing the wrong resource; the hypothesis that label overload causes sub-optimal selection is based on gap analysis and prior-project usage skew. It gives three illustrative failure modes. The first is pulling `nmdc.ncbi_biosamples` for NMDC-curated metadata at 3,000× the scale. The second is missing the freshest MAG catalog by searching only the `nmdc` tenant. The third is citing `kbase.nmdc_neon` as NMDC and so mis-attributing an NSF program. The report says such mistakes would plausibly cost time and compute and weaken conclusions; those costs are plausible, not measured. [src: nmdc_context_audit]

PaperBLAST introduces a related tension between apparent literature coverage and functional evidence: text-mined mentions may be incidental, and 65.6% of genes with a paper link have exactly one paper, while 25.6% of genes in its gene table have no text-mined paper link. Thus a large or well-linked resource may still provide uneven functional coverage rather than authoritative characterization. [src: paperblast_explorer]

WoM introduces a related tension between apparent metabolite integration and biological interpretability. The snapshot records increased or newly emerged metabolites but no organism consumption actions; although “decrease” is described as a valid WoM action elsewhere, the absence of consumption data in this export prevents testing whether consumed metabolites predict gene essentiality. The report suggests that newer GNPS2 data may contain such records, but this remains a version-dependent possibility rather than an established property of the snapshot. [src: webofmicrobes_explorer]

The WoM report is also internally uneven about the evidence for that possibility. Its Literature Context section cites Kosina et al. (2018), which introduced WoM with the same data and describes "decrease" as a valid action. That confirms consumption data are part of the WoM schema but absent from this specific export. The same section reports that the Northen Lab Defined Medium (NLDM) of de Raad et al. (2022) supported growth of 108/110 phylogenetically diverse soil bacteria, with all metabolites trackable by LC-MS/MS. It says this dataset likely contains consumption data and may be available in the current GNPS2 version of WoM. The Future Directions section asserts more strongly that the NLDM study tested 110 soil bacteria with full consumption and production tracking. It then projects that ingesting this dataset would resolve the no-consumption limitation and increase the organism count 3–5×. Neither ingestion nor that increase occurred in the project, so the stronger wording is a conditional projection, not a verified property of the newer data. [src: webofmicrobes_explorer]

There is also an interface-specific tension between metadata availability and operational reliability. Iceberg metadata counts succeeded for the audited NMDC tables, whereas the pitfalls report finds REST `/count` particularly unreliable for loops over many tables and `/schema` prone to timeout on large tables. These findings are not contradictory because they concern different access surfaces; discovery cards should record the interface and query path used to establish each claim. [src: nmdc_context_audit] [src: pitfalls]

The soil-frontier result introduces a related interpretive tension: all clay-shield model families had negative out-of-sample R², but this does not distinguish spatial distributional shift, high-leverage outliers, and genuine global-scale unpredictability. The report therefore **contradicts** any discovery interpretation that treats a completed analysis as a settled biological null: spatial blocking and leverage diagnostics are required before the result can be used as evidence about soil function. [src: soil_frontier_genomics]

The BERDL Data Atlas and the NMDC audit disagree on catalog provenance labels. The atlas presents `table_topic_map.csv` as a machine-readable catalog with tenant, agency, program, and biological-topic provenance. It inventories 48,196 GO terms and 8,813 EC terms as “NMDC integrated”. The audit treats the “NMDC integrated” tagging of Rhea/GO reference ontologies under `nmdc_arkin` as provenance blur that hides external authority. The disagreement concerns label semantics rather than counts. It remains unresolved until the catalog distinguishes the hosting resource from the upstream authority. [src: berdl_data_atlas, nmdc_context_audit]

UniRef illustrates why resource cards must carry the exact collection address rather than a family name, but the two sources here describe different resources and do not contradict each other. The pitfalls notes call `kbase_uniref50`, `kbase_uniref90`, and `kbase_uniref100` partial/sample datasets, not the full UniRef releases, which would be hundreds of millions of clusters. [src: pitfalls] The atlas instead counts the `cluster` tables of `refdata_uniref50_2026_01`, `refdata_uniref90_2026_01`, and `refdata_uniref100_2026_01`, reporting 475,217,233 UniRef100, 188,848,220 UniRef90, and 60,315,044 UniRef50 clusters (2026-01). [src: berdl_data_atlas] A user who searches for "UniRef" without the tenant-qualified name could reach the partial `kbase_uniref*` sample when the 2026-01 `refdata` release was intended. Whether records overlap between the two collections is not reported and would need record-level comparison. [src: pitfalls, berdl_data_atlas]

## Open Directions

- Compare `nmdc.metadata` and `nmdc.ncbi_biosamples` with live upstream record counts using external API calls, and ask how much completeness lag each resource has. [src: nmdc_context_audit]
- Add provenance, authority, tenant, object-count, and `max(committed_at)` fields to inventory output, then test whether users can identify the appropriate NMDC-related resource without opening separate documentation. [src: nmdc_context_audit]
- De-duplicate dotted and underscore database aliases before inventory iteration, then verify whether reported resource counts and cross-tenant links become consistent. [src: nmdc_context_audit]
- Apply the proposed documentation and tooling fixes and measure subsequent NMDC project resource selection time and reuse patterns to test whether better context reduces selection errors. [src: nmdc_context_audit]
- Extend the provenance-audit method to other overloaded KBase Data Lakehouse labels and ask whether the same combination of name collisions, tenant separation, scale traps, and hidden currency recurs. [src: nmdc_context_audit]
- Join the 129,823 PaperBLAST–Fitness Browser cross-references to resource cards, then test whether exposing source, text-mining coverage, and phenotype linkage changes selection of literature-to-fitness resources. [src: paperblast_explorer]
- Compare PaperBLAST’s PMC-derived coverage with curatedgene, GeneRIF, and SwissProt-only annotations to quantify which missing-literature patterns reflect access limitations versus genuinely unstudied proteins. [src: paperblast_explorer]
- Build live resource cards that record dotted and fallback namespace, tenant, access surface, schema-discovery time, row/object counts, and `max(committed_at)`, then test whether the cards prevent duplicate aliases and invalid historical references. [src: pitfalls]
- Evaluate identifier bridges using genus consistency and assembly-accession checks, and quantify how many cross-resource links remain valid after synonymy and taxonomy-version reconciliation. [src: pitfalls]
- Re-run the soil-frontier analysis with spatial blocking and leverage diagnostics to decompose negative out-of-sample R² into distributional shift, outliers, and true unpredictability; report rarefaction-corrected GDI, biome bootstrap 95% CIs, and 16S-sample-adjusted pH-bin comparisons to distinguish sampling gaps from completeness or assembly gaps. [src: soil_frontier_genomics]
- Re-ingest the current WoM or Northen laboratory dataset, record its snapshot and access path, and test whether consumption actions are present and whether the 2018 production-only patterns persist. [src: webofmicrobes_explorer]
- Add curated WoM compound-to-ModelSEED and GapMind pathway-to-metabolite bridges, preserving exact versus formula-only confidence, then test whether metabolite-production links support reproducible gene-fitness analyses. [src: webofmicrobes_explorer]
- Re-run the atlas's `build_inventory.py` and `data_volume.py` at the next ingest milestone and join the output to per-table `max(committed_at)`. Then test whether static-inventory lag and undocumented databases, such as the PhageFoundry database-count mismatch, are caught automatically. [src: berdl_data_atlas, discoveries]
- Reconcile across-tenant duplicates in two places: UniProt entries shared by refdata and kbase, and genome records shared by ENIGMA genome-depot and SDT tables. Then report unique-entity counts alongside row totals. [src: berdl_data_atlas]
- Re-count the NMDC metabolomics, proteomics, and lipidomics layers from the live cluster to replace the agent-memory figures. Add a field that distinguishes hosting resource from upstream authority for GO, EC, and Rhea terms. [src: berdl_data_atlas, nmdc_context_audit]
- Audit ENIGMA CORAL for registered samples with no linked assay processes beyond the SSO tubes, and expose ingestion status on resource cards. [src: discoveries]
- Compare cluster identifiers in the partial `kbase_uniref*` tables with the `refdata_uniref*_2026_01` cluster tables. This would quantify record-level overlap, and the comparison could then be used to label each collection's role (sample versus release) on resource cards. [src: pitfalls, berdl_data_atlas]
- Add an empty/sampled/partial flag to resource cards. Test it on PlanetMicrobe `project` and `library`, the `protect_genomedepot` sampled tables, and the Phenix structural-biology tables. [src: pitfalls]
- Index the PhageFoundry strain-modelling tables alongside the GenomeDepot browsers in discovery tooling. Then check whether projects reach the experimental phage-host data without manual discovery. [src: pitfalls, snipe_defense_system]
