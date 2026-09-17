<!-- tension-hash: f0c8f1e3efe3039f -->
# Do scale and schema read reliably? Iceberg metadata counts beside REST `/count` and `/schema`

Two projects in this corpus report different operational experiences with what looks like one task — establishing how many rows a table holds and what columns it has. The [[concepts/provenance-aware-resource-discovery]] page treats scale and schema as things discovery must expose, which only works if they can be read reliably. One project read scale successfully through the table format's own metadata for the audited NMDC tables [src: nmdc_context_audit]; the other reports conditional unreliability on a different access surface — REST (Representational State Transfer, an HTTP endpoint interface) `/count` for loops over many tables, and `/schema` prone to timeout on large tables [src: pitfalls]. The corpus reads these findings as not contradictory, because they concern different access surfaces, and requires that discovery cards record the interface and query path used to establish each claim [src: nmdc_context_audit] [src: pitfalls]. What stays open is which condition — interface, workload shape, or table size — carries the failure, and therefore what a quoted row count means without its query path attached.

## Evidence Sides

**Metadata counts were reliable (nmdc_context_audit).** Iceberg metadata counts — row counts read from the table format's own manifest metadata rather than by scanning data — succeeded for the audited NMDC tables [src: nmdc_context_audit]. This is a positive, direct operational result over a specific audited set, not a general claim about all tables or all interfaces.

**REST `/count` and `/schema` were unreliable (pitfalls).** The pitfalls report finds the REST (HTTP endpoint) `/count` particularly unreliable for loops over many tables, and `/schema` prone to timeout on large tables [src: pitfalls]. The direction here is conditional rather than absolute: the stated failure conditions are the loop over many tables for `/count`, and large table size for `/schema`.

## Possible Reconciliations

- *Access-surface hypothesis.* The corpus's own reading is that these findings are not contradictory because they concern different access surfaces — table-format metadata versus a REST endpoint — so both can hold simultaneously [src: nmdc_context_audit] [src: pitfalls]. This is offered as an explanation, not a demonstrated cause.
- *Workload-shape hypothesis.* The unreliability may attach to the query pattern rather than the interface: a single audit of a bounded table set is not a loop over many tables, which is the condition under which `/count` is reported unreliable [src: pitfalls].
- *Table-size hypothesis.* `/schema` timeouts are reported specifically on large tables [src: pitfalls]; the audited NMDC tables may fall below whatever size the timeout tracks [src: nmdc_context_audit]. No threshold is given in either report, so this remains untested.

## Resolving Work

- Run both surfaces over one shared table list spanning the audited NMDC tables and larger tables: compare Iceberg metadata counts against REST `/count` per table, and ask whether disagreement or failure tracks the interface or the table.
- Sweep table size against `/schema` latency and timeout outcome on the same catalog, to ask whether a size threshold exists and where it sits — a number neither report supplies.
- Repeat `/count` as a single call and as a loop over many tables on identical targets, asking whether loop context alone reproduces the reported unreliability.
- Record interface and query path alongside every scale and schema claim in discovery cards, then re-audit stored claims to ask how many are reproducible on the surface that produced them [src: nmdc_context_audit] [src: pitfalls].
