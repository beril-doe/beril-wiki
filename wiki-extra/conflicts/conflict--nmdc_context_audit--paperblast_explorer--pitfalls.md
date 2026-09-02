<!-- tension-hash: 14ff5da037852c4f -->
# Apparent Integration vs Unambiguous, Actionable Evidence

Across [[concepts/provenance-aware-resource-discovery]] and related project reports, the disagreement is whether a resource’s apparent integration, coverage, or analytical completion can be treated as reliable evidence for discovery and interpretation. Shared naming can improve access while obscuring provenance; links and metabolite records can suggest biological value without establishing functional or causal evidence; and successful queries or completed models can conceal interface-specific failures or unresolved statistical explanations.

## Evidence Sides

**Intentional integration improves discovery, but naming and grouping can obscure provenance.** Co-hosting can provide useful re-hosted and value-added resources, but the same naming pattern can cause users to confuse NMDC, NCBI, Pfam/InterPro, Arkin-derived, and NEON resources. Prefix-based grouping is simple, but it can hide `kbase.nmdc_mags`, `kbase.nmdc_arkin`, and `kbase.nmdc_neon` from searches focused on the `nmdc` tenant. [src: nmdc_context_audit]

**The selection-risk claim remains inferential.** The report does not directly observe users choosing the wrong resource; the hypothesis that label overload causes sub-optimal selection is based on gap analysis and prior-project usage skew. [src: nmdc_context_audit]

**Literature links indicate coverage but not necessarily functional authority.** Text-mined mentions may be incidental, and 65.6% of genes with a paper link have exactly one paper, while 25.6% of genes in its gene table have no text-mined paper link. Thus a large or well-linked resource may still provide uneven functional coverage rather than authoritative characterization. [src: paperblast_explorer]

**Metabolite integration does not establish biological interpretability.** The snapshot records increased or newly emerged metabolites but no organism consumption actions; although “decrease” is described as a valid WoM action elsewhere, the absence of consumption data in this export prevents testing whether consumed metabolites predict gene essentiality. Newer GNPS2 data may contain such records, but this remains a version-dependent possibility rather than an established property of the snapshot. [src: webofmicrobes_explorer]

**Successful metadata queries and unreliable operational surfaces can coexist.** Iceberg metadata counts succeeded for the audited NMDC tables, whereas REST `/count` is particularly unreliable for loops over many tables and `/schema` is prone to timeout on large tables. These findings concern different access surfaces. [src: nmdc_context_audit] [src: pitfalls]

**A completed model is not necessarily a settled biological null.** All clay-shield model families had negative out-of-sample R², but this does not distinguish spatial distributional shift, high-leverage outliers, and genuine global-scale unpredictability. [src: soil_frontier_genomics]

## Possible Reconciliations

- **Hypothesis — scope difference:** co-hosting and prefix grouping may be useful for broad catalog navigation while requiring provenance-aware views for precise selection.
- **Hypothesis — evidence-type difference:** text-mined links and metabolite changes may be discovery signals, not claims of validated function or consumption.
- **Hypothesis — interface difference:** Iceberg metadata paths may be dependable even when REST endpoints fail under looping or large-table workloads.
- **Hypothesis — model-diagnosis difference:** negative out-of-sample R² may reflect spatial shift or leverage rather than global biological unpredictability.

## Resolving Work

- Measure resource-selection errors in a user study comparing prefix-based and provenance-aware catalog views; test whether label overload changes choices.
- Compare PaperBLAST text-mined links with independently curated functional evidence; determine whether link count or link presence predicts validated characterization.
- Obtain a GNPS2 export containing organism consumption actions and test whether consumed metabolites predict gene essentiality.
- Benchmark Iceberg metadata, REST `/count`, and `/schema` over the same tables; determine which query path supports reproducible discovery claims.
- Refit soil-frontier models with spatial blocking and leverage diagnostics; determine whether negative out-of-sample R² persists after separating distributional shift, outliers, and global unpredictability.
