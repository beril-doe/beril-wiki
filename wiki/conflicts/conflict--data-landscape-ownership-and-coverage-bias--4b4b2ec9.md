<!-- tension-hash: 4b4b2ec95b27af76 -->
# Atlas Provenance Labels vs. Audited Resource Origins: Are NMDC-Tagged Shares Correctly Attributed?

This tension concerns how the atlas attributes resources in the KBase Data Lakehouse to tenants and agencies. The atlas tags some reference ontologies as "NMDC integrated," where NMDC is the National Microbiome Data Collaborative, and an audit of NMDC-labelled resources describes that tag as provenance blur. Provenance is the record of where a resource came from. [src: nmdc_context_audit] The atlas also groups databases by name prefix into tenants, which are the namespace owners under which databases sit. [src: nmdc_context_audit, berdl_data_atlas] The concept page [[concepts/data-landscape-ownership-and-coverage-bias]] argues that ownership and tenant boundaries shape which biological data are available. [src: berdl_data_atlas] If the attribution underneath that argument is unreliable, tenant-level and agency-level shares may reflect naming conventions rather than origin. This remains a hypothesis. [src: nmdc_context_audit, berdl_data_atlas]

## Evidence Sides

**Atlas labelling and grouping (as described by the audit)**
- The atlas tags the Rhea and GO (Gene Ontology) reference ontologies that sit under `nmdc_arkin` as "NMDC integrated." [src: nmdc_context_audit]
- The atlas groups databases by prefix. Under that scheme, `nmdc_neon` and other NMDC-related databases are filed under the `kbase` tenant. [src: nmdc_context_audit, berdl_data_atlas]

**Audit's provenance reading**
- The audit **contradicts** part of the atlas's provenance labelling. It describes the "NMDC integrated" tag on the Rhea/GO reference ontologies as provenance blur, even where documentation of their origin exists. [src: nmdc_context_audit]
- Taken together with the prefix-based grouping, this suggests the hypothesis that some atlas tenant-level and agency-level shares misattribute externally sourced resources. [src: nmdc_context_audit, berdl_data_atlas]

The misattribution claim is a hypothesis, not a measured result. The evidence here does not quantify how large any misattribution is.

## Possible Reconciliations

- **Hypothesis: the labels answer different questions.** The atlas may use "NMDC integrated" to mean that a resource is integrated into an NMDC-associated database. The audit uses provenance to mean who originally produced the resource. Under this reading both descriptions could be accurate for their own purpose but misleading when read as the other.
- **Hypothesis: the grouping is correct but under-annotated.** Grouping by tenant prefix may correctly record where a database is hosted, while saying nothing about where its content came from. A second, source-of-origin attribute could sit alongside it without changing the tenant view.
- **Hypothesis: the share distortion is real but confined.** The misattribution may affect only a few NMDC-adjacent databases. Agency-level shares would then shift only for those resources. Whether this holds is untested.

## Resolving Work

- **Rhea/GO under `nmdc_arkin`:** Using the documentation for each ontology table, classify every table as either originally produced or re-hosted from an external source. Then check whether "NMDC integrated" is ever justified on an origin basis.
- **Databases containing "nmdc":** Cross-tabulate the atlas's prefix-based tenant assignment against the audit's provenance classes. This would show which assignments diverge, and in which direction.
- **Tenant and agency shares:** Recompute the atlas's tenant-level and agency-level table shares under an origin-based attribution. Compare them with the prefix-based shares to test whether the misattribution hypothesis changes any conclusion on the concept page.
- **`nmdc_neon`:** Trace its lineage through the source metadata to establish which program and agency produced it. This would settle whether filing it under `kbase` misstates ownership, hosting, or neither.
