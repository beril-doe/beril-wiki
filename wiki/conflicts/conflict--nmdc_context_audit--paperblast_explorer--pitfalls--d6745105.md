<!-- tension-hash: 14ff5da037852c4f -->
# Discovery-surface signals versus the evidence they are taken to license

Six distinct disagreements in this corpus share one axis: a signal visible at discovery time — a resource name, a catalog prefix, a literature link, an integrated metabolite table, a successful metadata call, or a completed model fit — is taken to license a claim that the underlying evidence does not actually support. The projects do not disagree about any single measurement; they disagree about what a surface signal *means*, and the resulting guidance pulls in opposite directions: make the catalog compact and co-hosted, or make it unambiguous and cross-linked; treat a well-linked resource as characterized, or as thinly evidenced; treat a completed analysis as a result, or as an undiagnosed failure. This page records all six. Three of the "A" sides below (3A, 4A, 6A) are **this page's own framing of the naive reading** that a report argues against — no project in the corpus asserts them, and in the soil case the report explicitly rejects it; citations on those subsections attach only to the measured facts and to the report's own naming of the tension, never to the framing. One disagreement — the interface-reliability pair — is described by its own sources as *not* contradictory, and is kept here because it still yields conflicting operational advice about which access surface to trust. These tensions were first recorded on [[concepts/provenance-aware-resource-discovery]].

## Evidence Sides

**Side 1A — Co-hosting is a service, and the shared label reflects a real relationship.** The audit accepts that co-hosting is intentional and that it can provide useful re-hosted and value-added resources. [src: nmdc_context_audit]

**Side 1B — The same label destroys unambiguous attribution.** The audit finds that the same naming pattern can cause users to confuse NMDC, NCBI, Pfam/InterPro, Arkin-derived, and NEON resources — different origins presented under one substring, so that a resource's name no longer identifies whose work it is. (NMDC and NEON are distinct programs; Pfam/InterPro are protein-family reference resources; "Arkin-derived" denotes a laboratory-derived product rather than program output.) [src: nmdc_context_audit] Critically, the audit does not directly observe users choosing the wrong resource; the hypothesis that label overload causes sub-optimal selection is based on gap analysis and prior-project usage skew — so Side 1B's *harm* claim is an inference, while its *ambiguity* claim is an observation. [src: nmdc_context_audit]

**Side 2A — Prefix-based grouping keeps the catalog compact.** The audit grants that prefix-based grouping is simple, giving a compact catalog view. [src: nmdc_context_audit]

**Side 2B — Prefix grouping breaks cross-tenant discovery.** The same grouping can hide `kbase.nmdc_mags`, `kbase.nmdc_arkin`, and `kbase.nmdc_neon` from searches focused on the `nmdc` tenant — resources that a topic-scoped search will silently miss because they are filed under a different prefix. (A *tenant* here is the top-level catalog namespace that owns a set of databases; "MAGs" are metagenome-assembled genomes.) [src: nmdc_context_audit]

**Side 3A — The naive reading: a large, well-linked literature resource looks like functional characterization.** This side is the page's framing of the pole the PaperBLAST report argues against; no project in the corpus asserts it. The report itself names this pole "apparent literature coverage". [src: paperblast_explorer]

**Side 3B — Text-mined links are thin and often absent.** PaperBLAST introduces a tension between apparent literature coverage and functional evidence: text-mined mentions (links inferred by scanning article text for gene names, rather than curated by a human) may be incidental, and 65.6% of genes with a paper link have exactly one paper, while 25.6% of genes in its gene table have no text-mined paper link. Thus a large or well-linked resource may still provide uneven functional coverage rather than authoritative characterization. [src: paperblast_explorer]

**Side 4A — The naive reading: the Web of Microbes snapshot looks like an integrated metabolite resource.** Again the page's framing of the pole the report argues against, not a project's position. The report names this pole "apparent metabolite integration", and records that the snapshot does contain increased or newly emerged metabolites. [src: webofmicrobes_explorer]

**Side 4B — The snapshot cannot support the biological question it appears to enable.** WoM introduces a tension between apparent metabolite integration and biological interpretability: the snapshot records no organism consumption actions; although "decrease" is described as a valid WoM action elsewhere, the absence of consumption data in this export prevents testing whether consumed metabolites predict gene essentiality. The report suggests that newer GNPS2 data may contain such records, but this remains a version-dependent possibility rather than an established property of the snapshot. [src: webofmicrobes_explorer]

**Side 5A — Metadata queries are cheap and reliable.** Iceberg metadata counts succeeded for the audited NMDC tables, so cataloguing scale via table metadata is a workable discovery step. [src: nmdc_context_audit]

**Side 5B — Metadata endpoints are unreliable at scale.** The pitfalls report finds REST `/count` particularly unreliable for loops over many tables and `/schema` prone to timeout on large tables. [src: pitfalls] The sources themselves state that these findings are not contradictory because they concern different access surfaces, and prescribe that discovery cards should record the interface and query path used to establish each claim. [src: nmdc_context_audit] [src: pitfalls]

**Side 6A — The naive reading: a completed analysis with a negative result is a biological null.** This reading is the page's framing and is the one the soil-frontier report explicitly rejects; it is stated here only so the disagreement has two poles. The measured fact behind it is that all clay-shield model families had negative out-of-sample R² — a cross-validated coefficient of determination below zero, meaning the models predicted held-out data worse than the training mean. [src: soil_frontier_genomics]

**Side 6B — That result is undiagnosed and cannot be read biologically yet.** The soil-frontier result does not distinguish spatial distributional shift, high-leverage outliers, and genuine global-scale unpredictability. The report therefore **contradicts** any discovery interpretation that treats a completed analysis as a settled biological null: spatial blocking and leverage diagnostics are required before the result can be used as evidence about soil function. [src: soil_frontier_genomics]

## Possible Reconciliations

Each of the following is a **hypothesis** about how both sides could be simultaneously correct; none is established by the cited evidence.

*Scope hypothesis (1, 2).* Co-hosting and prefix grouping may be correct at the storage layer and wrong at the discovery layer. If the catalog's job is to say where bytes live, prefix grouping is accurate; if its job is to answer "what belongs to this program," it is not. Under this hypothesis both sides describe a different consumer of the same structure, and the fix would be an additional provenance/topic facet rather than a re-layout. [src: nmdc_context_audit]

*Unobserved-harm hypothesis (1).* Side 1B's ambiguity may be real while its downstream harm is small, because expert users disambiguate from context. This is directly compatible with the audit's own statement that the causal claim rests on gap analysis and prior-project usage skew rather than observed mis-selection. [src: nmdc_context_audit]

*Definitional hypothesis (3).* "Coverage" and "characterization" may simply be different quantities. A resource can be complete as an index of *mentions* while being sparse as an index of *functional evidence*; the reported 65.6% single-paper share and 25.6% unlinked share would then be properties of the mention layer, not defects of the resource. [src: paperblast_explorer]

*Version hypothesis (4).* The WoM disagreement may be an artifact of the export rather than of the database design, since "decrease" is described as a valid WoM action elsewhere and newer GNPS2 data may contain such records. If so, both sides are right about different versions — but the report explicitly marks this as a version-dependent possibility, not an established property. [src: webofmicrobes_explorer]

*Measurement-surface hypothesis (5).* This is the reconciliation the sources themselves assert: the two reliability findings concern different access surfaces, so a count that succeeds through Iceberg metadata and a `/count` that fails through REST are both true reports about different query paths. The operational consequence is that the interface and query path must be recorded alongside each claim. [src: nmdc_context_audit] [src: pitfalls]

*Diagnostic-incompleteness hypothesis (6).* Sides 6A and 6B could both hold if genuine global-scale unpredictability is in fact the operative cause — but that cannot be asserted until spatial distributional shift and high-leverage outliers are excluded, which is precisely what the report says has not been done. [src: soil_frontier_genomics]

## Resolving Work

**Co-hosting versus attribution (1).**
- Instrument resource selection: log which resources users open after a label-scoped search, and test whether selections cross provenance classes — converting the gap-analysis hypothesis into an observed rate. [src: nmdc_context_audit]
- Attach an explicit provenance/authority field to every co-hosted resource and re-run the confusion analysis to see whether the confusion among NMDC, NCBI, Pfam/InterPro, Arkin-derived, and NEON resources is eliminated by annotation alone. [src: nmdc_context_audit]
- Audit downstream project artifacts for actual mis-attribution of NEON-origin data to NMDC, which would convert the inferred harm into direct evidence. [src: nmdc_context_audit]
- Compare selection accuracy with and without provenance annotations in a controlled task, holding the co-hosting layout fixed. [src: nmdc_context_audit]

**Prefix grouping versus cross-tenant discovery (2).**
- Measure recall of a tenant-scoped `nmdc` search against a hand-built ground-truth set, and report specifically whether `kbase.nmdc_mags`, `kbase.nmdc_arkin`, and `kbase.nmdc_neon` are returned. [src: nmdc_context_audit]
- Build a topic facet independent of catalog prefix and re-measure the same recall, quantifying the gain against the cost of a larger catalog view. [src: nmdc_context_audit]
- Check the inverse error rate: how often a topic facet pulls in a namesake-collision resource such as `kbase.nmdc_neon` that a prefix view correctly excludes. [src: nmdc_context_audit]

**Literature coverage versus functional evidence (3).**
- Stratify genes by paper count and manually adjudicate a sample of single-paper links as functional versus incidental mentions, producing a per-stratum precision estimate for the 65.6% single-paper class. [src: paperblast_explorer]
- Characterize the 25.6% of genes with no text-mined paper link: determine whether they are genuinely unstudied or simply missed by text mining, using an independent curated source. [src: paperblast_explorer]
- Define and report a "functional evidence" tier separate from "has a paper link," and re-derive coverage statistics under that definition. [src: paperblast_explorer]
- Test whether downstream analyses that filter to multi-paper genes reach different conclusions than those that accept any link. [src: paperblast_explorer]

**Metabolite integration versus interpretability (4).**
- Obtain and profile the newer GNPS2 data for organism consumption actions, and report presence or absence explicitly rather than assuming it. [src: webofmicrobes_explorer]
- If consumption records exist, run the blocked test — do consumed metabolites predict gene essentiality? — which the current export prevents. [src: webofmicrobes_explorer]
- Re-verify that "decrease" is instantiated for organisms, not only described as a valid action, before any analysis depends on it. [src: webofmicrobes_explorer]
- Version-stamp every WoM-derived claim so that conclusions drawn from the increased/emerged-only snapshot are not silently generalized. [src: webofmicrobes_explorer]

**Metadata availability versus operational reliability (5).**
- Benchmark Iceberg metadata counts against REST `/count` over the same table set and report success rate and latency per surface, rather than per resource. [src: nmdc_context_audit] [src: pitfalls]
- Characterize `/schema` timeout behaviour as a function of table size to establish where the failure boundary lies. [src: pitfalls]
- Add an interface-and-query-path field to discovery cards, as both reports prescribe, and verify that scale claims carry it. [src: nmdc_context_audit] [src: pitfalls]
- Re-test whether the audit's metadata-count success generalizes beyond the audited NMDC tables to the many-table loops where `/count` is reported unreliable. [src: nmdc_context_audit] [src: pitfalls]

**Completed analysis versus settled null (6).**
- Re-fit the clay-shield model families under spatial blocking and report whether negative out-of-sample R² persists. [src: soil_frontier_genomics]
- Run leverage diagnostics to identify high-leverage outliers and quantify their contribution to the negative R². [src: soil_frontier_genomics]
- Compare the three candidate causes — spatial distributional shift, high-leverage outliers, and genuine global-scale unpredictability — as competing explanations rather than reporting the aggregate fit alone. [src: soil_frontier_genomics]
- Withhold any biological interpretation of the result in downstream pages until the diagnostics above are complete, since the report explicitly contradicts treating the completed analysis as a settled null. [src: soil_frontier_genomics]
