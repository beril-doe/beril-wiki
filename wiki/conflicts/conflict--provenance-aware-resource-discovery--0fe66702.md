<!-- tension-hash: 0fe66702cb49c6cb -->
# Does "NMDC integrated" describe where ontology terms are hosted or whose authority they carry?

The BERDL Data Atlas and the NMDC context audit disagree about what a catalog provenance label should mean. NMDC is the National Microbiome Data Collaborative. The atlas uses "NMDC integrated" as a catalog tag for reference ontology terms. The audit reads the same tagging as provenance blur that hides the external authority behind those ontologies. The disagreement concerns label semantics rather than counts: whether a tag names the resource that hosts a dataset or the upstream body that defines it. This matters for [[concepts/provenance-aware-resource-discovery]], which holds that catalogs should expose authority and tenant placement together rather than treating a name as a sufficient dataset boundary. [src: berdl_data_atlas, nmdc_context_audit]

## Evidence Sides

**Side A: the atlas treats the catalog as provenance-bearing.** The atlas presents `table_topic_map.csv` as a machine-readable catalog, a comma-separated table that software can parse directly, with tenant, agency, program, and biological-topic provenance. Here a tenant is the namespace in the KBase Data Lakehouse where a resource is placed. [src: berdl_data_atlas, nmdc_context_audit]

Within this catalog, the atlas inventories 48,196 GO terms and 8,813 EC terms as "NMDC integrated". GO is the Gene Ontology, a controlled vocabulary of gene functions. EC is the Enzyme Commission classification of enzyme reactions. [src: berdl_data_atlas, nmdc_context_audit]

**Side B: the audit treats the label as blurring external authority.** The audit examines Rhea and GO reference ontologies held under the `nmdc_arkin` resource. Rhea is a curated database of biochemical reactions. The audit argues that tagging these ontologies "NMDC integrated" is provenance blur, because the label hides the external authority that defines the ontologies. Under this reading, the label is misleading even though the counts are not disputed. [src: berdl_data_atlas, nmdc_context_audit]

The tension stays unresolved until the catalog distinguishes the hosting resource from the upstream authority. [src: berdl_data_atlas, nmdc_context_audit]

## Possible Reconciliations

- *Hypothesis 1:* The two sides use "provenance" at different levels. The atlas may mean integration and hosting lineage, while the audit means definitional authority. If so, both readings could be correct for their own field, and the conflict would be a schema gap rather than a factual error.
- *Hypothesis 2:* The "NMDC integrated" tag may have been applied at the resource level, to `nmdc_arkin`, and inherited by every table in that resource. That would explain why external ontologies carry a program label they do not originate from.
- *Hypothesis 3:* A two-field label might satisfy both sides without changing any count. One field would name the hosting resource and tenant. The other would name the upstream authority, such as the GO or Rhea maintainers.

## Resolving Work

- **Catalog schema split.** Data: `table_topic_map.csv`. Method: add separate hosting-resource and upstream-authority columns and re-tag the ontology tables. Question: do any GO, EC or Rhea tables still carry "NMDC integrated" once authority is a separate field?
- **Label-inheritance trace.** Data: the catalog generation code and the `nmdc_arkin` table list. Method: trace how the "NMDC integrated" tag is assigned. Question: is the tag set per table or inherited per resource?
- **Upstream release matching.** Data: the Rhea and GO tables under `nmdc_arkin` and the public upstream releases. Method: match term identifiers and release versions. Question: are these unmodified external copies, or NMDC-processed derivatives that would justify the label?
- **Cross-label consistency audit.** Data: all catalog rows carrying a program label. Method: compare each label against the table's documented originating authority. Question: does any divergence between program label and originating authority occur only for ontologies, or also for other re-hosted reference data?
