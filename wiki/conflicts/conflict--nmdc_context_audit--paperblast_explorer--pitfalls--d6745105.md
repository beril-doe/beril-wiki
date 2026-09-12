<!-- tension-hash: 14ff5da037852c4f -->
# Discovery Signals Versus Unambiguous, Reliable Interpretation

The tensions recorded on [[concepts/provenance-aware-resource-discovery]] concern whether convenient discovery signals—shared naming, compact catalogs, literature links, metabolite records, successful metadata queries, or completed models—can be treated as evidence of clear provenance, biological coverage, operational reliability, or settled interpretation. These disagreements matter because the same interface or dataset can support useful discovery while still encouraging attribution errors, overstating functional evidence, or masking unresolved methodological limitations.

## Evidence Sides

**Intentional co-hosting and compact grouping support discovery.** Co-hosting can provide useful re-hosted and value-added resources, and prefix-based grouping is simple. [src: nmdc_context_audit]

**Naming and prefix grouping can obscure attribution and cross-tenant discovery.** The same naming pattern can cause users to confuse NMDC, NCBI, Pfam/InterPro, Arkin-derived, and NEON resources. Prefix-based grouping can hide `kbase.nmdc_mags`, `kbase.nmdc_arkin`, and `kbase.nmdc_neon` from searches focused on the `nmdc` tenant. [src: nmdc_context_audit]

**Literature links indicate apparent coverage.** PaperBLAST provides genes with paper links and a large or well-linked resource may appear to offer broad functional coverage. [src: paperblast_explorer]

**Literature links do not guarantee authoritative or even coverage.** Text-mined mentions may be incidental; 65.6% of genes with a paper link have exactly one paper, while 25.6% of genes in its gene table have no text-mined paper link. [src: paperblast_explorer]

**Metabolite integration can appear biologically informative.** The WoM snapshot records increased or newly emerged metabolites, and “decrease” is described as a valid WoM action elsewhere. [src: webofmicrobes_explorer]

**The snapshot cannot establish consumption-based interpretation.** It records no organism consumption actions, so the absence of consumption data in this export prevents testing whether consumed metabolites predict gene essentiality. Newer GNPS2 data may contain such records, but this remains a version-dependent possibility rather than an established property of the snapshot. [src: webofmicrobes_explorer]

**Audited metadata queries can succeed.** Iceberg metadata counts succeeded for the audited NMDC tables. [src: nmdc_context_audit]

**Other access paths can be operationally unreliable.** REST `/count` is particularly unreliable for loops over many tables, and `/schema` is prone to timeout on large tables. [src: pitfalls]

**A completed soil-frontier analysis can look like a biological null.** All clay-shield model families had negative out-of-sample R². [src: soil_frontier_genomics]

**The result does not yet identify the cause or settle the biology.** Spatial distributional shift, high-leverage outliers, and genuine global-scale unpredictability remain distinct possibilities; spatial blocking and leverage diagnostics are required before the result can be used as evidence about soil function. [src: soil_frontier_genomics]

## Possible Reconciliations

- **Hypothesis — scope difference:** Co-hosting and prefix grouping may be appropriate for catalog organization, while provenance-aware labels and tenant-aware search are needed for attribution.
- **Hypothesis — evidence-strength difference:** Paper links and metabolite records may support exploratory discovery without constituting authoritative functional characterization or demonstrated consumption.
- **Hypothesis — interface difference:** Successful Iceberg metadata queries and unreliable REST endpoints may both be accurate because they use different access surfaces and query paths.
- **Hypothesis — diagnostic difference:** Negative out-of-sample R² may reflect spatial shift or leverage rather than a global biological null.

## Resolving Work

- Compare user search and selection behavior under shared versus provenance-explicit labels; test whether label overload causes sub-optimal selection.
- Reconcile tenant-aware and prefix-based catalog indexes, verifying whether `kbase.nmdc_mags`, `kbase.nmdc_arkin`, and `kbase.nmdc_neon` appear in `nmdc`-focused searches.
- Audit PaperBLAST links for incidental mentions, independent functional evidence, and coverage across genes with zero, one, or multiple papers.
- Obtain a WoM/GNPS2 export containing organism consumption actions and test whether consumed metabolites predict gene essentiality.
- Repeat soil-frontier evaluation with spatial blocking and leverage diagnostics, then compare model performance under each condition.
