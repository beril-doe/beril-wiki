---
type: "Concept"
description: "Discovery should expose provenance, scale, access, and freshness together."
sources: ["summaries/nmdc_context_audit__REPORT.md", "summaries/paperblast_explorer__REPORT.md", "summaries/pitfalls.md", "summaries/soil_frontier_genomics__REPORT.md", "summaries/webofmicrobes_explorer__REPORT.md"]
---
# Provenance, scale, and currency must be exposed during resource discovery

Resource discovery should expose provenance, authority, scale, tenant placement, access conditions, and data currency together rather than treating a name or catalog prefix as a sufficient dataset boundary. The [[summaries/nmdc_context_audit__REPORT]] provides direct evidence that the `nmdc` label is systematically overloaded across maintained resources, while the consequences for user selection remain an inferred hypothesis rather than a directly observed causal effect. The [[summaries/pitfalls]] extends this requirement from catalog interpretation to executable workflows: live namespace, schema, identifier, join, and interface checks are needed before a resource can be treated as a valid analytical input. The [[summaries/soil_frontier_genomics__REPORT]] **supports** the same principle from a spatial-genomics setting: discovery metrics must distinguish sampling gaps, completeness, scale, and analytical validity rather than compressing them into a single index. The [[summaries/webofmicrobes_explorer__REPORT]] **supports** the combined requirement from a cross-collection metabolomics setting: the 2018 Web of Microbes (WoM) snapshot is useful only when its archived provenance, small organism and metabolite scale, available access surfaces, and freshness limitations are presented together. [src: nmdc_context_audit] [src: pitfalls] [src: soil_frontier_genomics] [src: webofmicrobes_explorer]

## Core claim

A resource name is not reliable evidence of what a dataset contains, who maintains it, how large it is, or how current it is. The audit resolved 20 database names containing `nmdc` to 7 real, maintained resources spanning three tenants and six provenance classes. [src: nmdc_context_audit]

The seven resources include genuine NMDC resources (`nmdc.metadata` and `nmdc.results`), an NCBI re-host (`nmdc.ncbi_biosamples`), a Pfam re-host (`nmdc.ref_data`), an Arkin Lab derivative (`kbase.nmdc_arkin`), an NMDC-derived KBase resource (`kbase.nmdc_mags`), and a namesake collision representing NEON rather than NMDC (`kbase.nmdc_neon`). [src: nmdc_context_audit]

This finding **supports** [[concepts/provenance-aware-resource-discovery]] as a distinct discovery requirement: users need provenance and authority annotations at the point of search, not only in downstream documentation. [src: nmdc_context_audit]

The PaperBLAST inventory **supports** the same requirement from a different resource class: `kescience_paperblast` contains 12.4 million rows across 14 tables linking sequences and genes to literature, annotations, structures, and full-text snippets, so a collection name alone does not convey its analytical scope or evidentiary boundaries. [src: paperblast_explorer]

The WoM assessment **refines** this claim by showing that a resource card must also distinguish a historical snapshot from a current service. The project analyzed a 2018 WoM export accessed through the Wayback Machine, and identified GNPS2 and Northen laboratory datasets as possible newer alternatives; the archived export therefore cannot be treated as a current representation without an explicit freshness warning. [src: webofmicrobes_explorer]

The migration from Delta to Iceberg **refines** this claim: live discovery must expose the currently valid address as well as the logical resource identity. Migrated tables use `catalog.namespace.table`, while former Delta references flatten the namespace; migration remains incomplete, so tooling should discover the dotted address and fall back to the underscore form only when necessary. [src: pitfalls]

The soil-frontier analysis **supports** exposing analytical status and metric definitions alongside resource identity. Its Genomic Discovery Index (GDI), defined as OTU Richness / (Mean Genome Completeness + 1), identified uneven genomic representation, but the report cautions that the novel index conflates richness with completeness and can equal 902 even when there are zero genomes. Discovery cards should therefore expose the underlying measures, formula, and validation status rather than presenting a composite score as self-explanatory. [src: soil_frontier_genomics]

## Scale is a selection variable

The `nmdc` tenant is neither exclusively NMDC nor the only location of NMDC-related resources. Two of its four databases are external re-hosts: `nmdc.ncbi_biosamples` contains 51,711,888 biosamples and 756,112,544 attribute rows, while `nmdc.ref_data` contains 27,481 Pfam terms. [src: nmdc_context_audit]

The genuine NMDC biosample universe contains 16,640 samples in `nmdc.metadata.biosample_set`, whereas the co-hosted NCBI mirror contains 51,711,888 biosamples. The audit identifies this as a ~3,000× scale trap, so discovery interfaces should display row or object counts and resource role before users query a dataset. [src: nmdc_context_audit]

Row counts for NMDC tables, including `nmdc.results.annotation_kegg_orthology` with 1.83B rows, returned instantly through Iceberg metadata using `SELECT COUNT(*)`. [src: nmdc_context_audit]

The PaperBLAST inventory **supports** treating scale as first-class discovery metadata: its largest tables include 3,195,890 gene-to-paper links and 1,951,949 text excerpts, while its sequence analysis clustered 815,571 proteins at multiple identity thresholds. These figures describe distinct objects and should be shown with table or collection roles rather than collapsed into one size number. [src: paperblast_explorer]

Scale metadata should therefore be treated as inexpensive discovery metadata rather than as an expensive exploratory query. This **refines** [[concepts/cross-tenant-data-bridging]] by showing that cross-tenant linking must carry comparable scale information, not merely database names and locations. [src: nmdc_context_audit]

The WoM assessment **supports** making scale and coverage visible before cross-collection use: its 2018 snapshot contains 37 organisms and 589 metabolites, with 332 (56.4%) metabolites unidentified and only 20 experimental organisms. Its 5 ENIGMA-funded projects, media, organism coverage, and single-laboratory origin define a substantially narrower evidence base than the linked Fitness Browser or pangenome resources. [src: webofmicrobes_explorer]

The pitfalls evidence **supports** displaying scale together with execution constraints: pangenome tables include approximately 1B-row `gene` and `gene_genecluster_junction` tables, approximately 421M-row `genome_ani`, approximately 93M-row `eggnog_mapper_annotations`, approximately 833M-row `interproscan_domains`, approximately 572M-row `bakta_db_xrefs`, and approximately 305M-row `gapmind_pathways`. Such resources require key filters before joins and should remain in Spark until the final small output. [src: pitfalls]

The soil-frontier GDI analysis **refines** scale metadata by showing that richness and genome completeness can diverge spatially: forest had GDI = 902.36 and cropland had GDI = 890.82, while grassland had GDI = 503.42 and wetland had GDI = 525.13. Forest and cropland should be described as jointly highest-GDI biomes, not ranked, because their difference was only 1.3% and no bootstrap confidence intervals were reported. [src: soil_frontier_genomics]

## Currency must be visible

Iceberg snapshot age—the available signal for data currency in this audit—spanned approximately four months across NMDC-labeled resources. The latest commits were `2026-07-02` for `kbase.nmdc_mags` and `kbase.nmdc_neon`, `2026-05-27` for `kbase.nmdc_arkin`, `2026-05-20` for `nmdc.metadata`, `nmdc.results`, and `nmdc.ref_data`, and `2026-03-09` for `nmdc.ncbi_biosamples`. [src: nmdc_context_audit]

The audit recommends surfacing `max(committed_at)` in discovery tooling because catalog tables had no comments, databases had empty properties, and no changelog exposed currency. [src: nmdc_context_audit]

The freshest NMDC-related resource was `kbase.nmdc_mags`, containing 62,346 MAGs, but it was located in the `kbase` tenant rather than the `nmdc` tenant. [src: nmdc_context_audit]

PaperBLAST **supports** making temporal coverage and snapshot information visible: its collection contains papers from 1951 to 2026, publications peak around 2020–2021, and the report identifies an early-2026 snapshot. Publication-year coverage is not equivalent to ingestion currency, so resource cards should distinguish the two rather than use either as a substitute for `max(committed_at)`. [src: paperblast_explorer]

WoM **supports** the same distinction between temporal coverage and ingestion currency: the analyzed data are a frozen 2018 snapshot retrieved through the Wayback Machine, while the report points to GNPS2 or Northen laboratory datasets as potentially newer sources. The snapshot's action semantics and missing consumption records must therefore be labeled as properties of that export, not assumed to describe the current WoM resource. [src: webofmicrobes_explorer]

This **supports** [[concepts/pangenome-integration]] by establishing that resource selection for MAG-based analyses depends on both catalog scale and snapshot currency, while tenant placement can conceal the relevant resource. [src: nmdc_context_audit]

The pitfalls document **refines** freshness metadata into an operational requirement: schemas, namespace availability, permissions, database contents, and naming conventions can change, so archived reports and notebooks should be treated as historical records rather than automatically valid executable instructions. [src: pitfalls]

The soil-frontier report **supports** treating validation status as part of freshness and provenance. Its clay-shield and GDI analyses were complete, but spatial validation and figures remained pending; the report also required re-running from BERIL Observatory 16S tables and `kbase_ke_pangenome` completeness data because no local CSV output was available. [src: soil_frontier_genomics]

## Provenance and authority are separate fields

The authority context is heterogeneous: NMDC is the National Microbiome Data Collaborative of DOE-BER; NEON is the National Ecological Observatory Network of NSF; NCBI BioSample is the authority for `nmdc.ncbi_biosamples`; and Pfam/InterPro is the authority for `nmdc.ref_data`. [src: nmdc_context_audit]

`kbase.nmdc_neon` represents NEON rather than NMDC, so interpreting the namesake as NMDC would create an agency-attribution error. [src: nmdc_context_audit]

The audit also found provenance blur in the KBase Data Lakehouse data atlas, which labels Rhea and Gene Ontology reference ontologies under `nmdc_arkin` as “NMDC integrated.” [src: nmdc_context_audit]

Provenance should describe both origin and transformation. The NCBI mirror adds an attribute-harmonization layer to 51,711,888 raw NCBI samples, while the Arkin derivative adds embeddings and traits that do not exist upstream. [src: nmdc_context_audit]

The PaperBLAST analysis **refines** this requirement by identifying a specific transformation and coverage boundary: it combines database inventory with text-mined PubMed Central full-text links, curated annotations, structural records, and MMseqs2 sequence clustering. PMC-only mining misses paywalled literature, and the report estimates that only 19% of SwissProt is represented, so provenance cards should expose both source inputs and missing-coverage mechanisms. [src: paperblast_explorer]

These observations **support** [[concepts/multi-omics-integration]]: value-added derivatives can be useful integration resources, but their derived status, upstream authority, and added data products must remain explicit. [src: nmdc_context_audit]

The WoM bridge **supports** preserving provenance at the level of compound identity and cross-collection mapping. Of 257 identified, non-unknown compounds, 69 (26.8%) had definitive ModelSEED links through exact name matching, while 107 (41.6%) had formula-only candidate links; those 107 expanded to 900 ModelSEED molecules, making formula-only matches unsuitable as definitive identifications. [src: webofmicrobes_explorer]

The pitfalls evidence **supports** preserving provenance at join level, not only collection level. Short ENIGMA strain names are not globally unique: one erroneous linkage matched ENIGMA MT20 (*Rhodanobacter glycinis*) to GTDB MT20 (*Streptococcus pneumoniae*), involving 8,434 genomes including 1,751 clinical genomes; 12 of 32 pangenome linkages through `ncbi_strain_identifiers` were incorrect genus matches. Assembly accessions such as `GCF_*`, genus checks, synonymy layers, and explicit bridge keys therefore belong in resource metadata and workflow provenance. [src: pitfalls]

The soil-frontier analysis **refines** provenance requirements by separating database sampling gaps from biological or technical assembly gaps. Frontier areas with GDI > 1000 had mean pH = 6.74, compared with mean pH = 5.94 in mapped areas, a +0.8 pH unit gap; however, the report notes that this could reflect fewer sequenced samples from those pH ranges rather than harder assembly or lower study effort. The number of 16S samples per pH bin must therefore accompany completeness and richness before the gap is interpreted biologically. [src: soil_frontier_genomics]

## Discovery has multiple access surfaces

`get_databases()` returns dotted Iceberg aliases such as `nmdc.metadata` and underscore Hive aliases such as `nmdc_metadata` for every tenant database, so consumers must de-duplicate to the dotted form before iteration to avoid double-counting. [src: nmdc_context_audit]

`DESCRIBE DATABASE EXTENDED kbase.nmdc_*` raised `ForbiddenException` for a `kesciencero`/`microbialdiscoveryforge` principal even when `COUNT(*)` on the same tables succeeded, demonstrating that metadata introspection and data reads have different access surfaces. [src: nmdc_context_audit]

The `berdl_inventory.py` tool groups resources by catalog prefix and therefore does not link `kbase.nmdc_*` resources back to NMDC. [src: nmdc_context_audit]

These constraints **refine** [[concepts/provenance-aware-resource-discovery]]: discovery tooling should expose an access-aware resource card using available table metadata, while not assuming that database-description APIs are universally readable. [src: nmdc_context_audit]

The PaperBLAST collection provides a further **supporting** example for access-aware linkage: 129,823 VIMSS cross-references connect its literature records to Fitness Browser phenotypes, creating a useful bridge whose meaning depends on preserving both collection provenance and cross-tenant identifiers. [src: paperblast_explorer]

WoM **supports** recording access surfaces and integration status separately from biological content. Its source tables, notebooks, and generated link files enabled links to Fitness Browser, ModelSEED, GapMind, and pangenomes, but GapMind matching was blocked by internal pathway identifiers, and species-level pangenome matching was not attempted. These are discoverability and reproducibility constraints, not evidence that the underlying biological relationships are absent. [src: webofmicrobes_explorer]

The pitfalls document **supports** separating access status from resource identity. Tenant and dataset names can be mis-combined—for example, `kbase_ke` is not the tenant for the `kbase.ke_pangenome` dataset—and access failures should identify the unreachable table and tenant without exposing internal service strings. Direct Spark SQL is preferred for complex or large queries because REST requests can return 504, 524, or 503 errors, while REST `/count` and `/schema` are unreliable for repeated or large-table discovery. [src: pitfalls]

## Tensions

The audit identifies a tension between intentional co-hosting and unambiguous attribution. Co-hosting can provide useful re-hosted and value-added resources, but the same naming pattern can cause users to confuse NMDC, NCBI, Pfam/InterPro, Arkin-derived, and NEON resources. [src: nmdc_context_audit]

The audit also identifies a tension between a compact catalog view and accurate cross-tenant discovery: prefix-based grouping is simple, but it can hide `kbase.nmdc_mags`, `kbase.nmdc_arkin`, and `kbase.nmdc_neon` from searches focused on the `nmdc` tenant. [src: nmdc_context_audit]

The report does not directly observe users choosing the wrong resource; the hypothesis that label overload causes sub-optimal selection is based on gap analysis and prior-project usage skew. [src: nmdc_context_audit]

PaperBLAST introduces a related tension between apparent literature coverage and functional evidence: text-mined mentions may be incidental, and 65.6% of genes with a paper link have exactly one paper, while 25.6% of genes in its gene table have no text-mined paper link. Thus a large or well-linked resource may still provide uneven functional coverage rather than authoritative characterization. [src: paperblast_explorer]

WoM introduces a related tension between apparent metabolite integration and biological interpretability. The snapshot records increased or newly emerged metabolites but no organism consumption actions; although “decrease” is described as a valid WoM action elsewhere, the absence of consumption data in this export prevents testing whether consumed metabolites predict gene essentiality. The report suggests that newer GNPS2 data may contain such records, but this remains a version-dependent possibility rather than an established property of the snapshot. [src: webofmicrobes_explorer]

There is also an interface-specific tension between metadata availability and operational reliability. Iceberg metadata counts succeeded for the audited NMDC tables, whereas the pitfalls report finds REST `/count` particularly unreliable for loops over many tables and `/schema` prone to timeout on large tables. These findings are not contradictory because they concern different access surfaces; discovery cards should record the interface and query path used to establish each claim. [src: nmdc_context_audit] [src: pitfalls]

The soil-frontier result introduces a related interpretive tension: all clay-shield model families had negative out-of-sample R², but this does not distinguish spatial distributional shift, high-leverage outliers, and genuine global-scale unpredictability. The report therefore **contradicts** any discovery interpretation that treats a completed analysis as a settled biological null: spatial blocking and leverage diagnostics are required before the result can be used as evidence about soil function. [src: soil_frontier_genomics]

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
