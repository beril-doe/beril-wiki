<!-- tension-hash: f0c8f1e3efe3039f -->
# Reliable enough to quote? Iceberg metadata counts succeeded where REST `/count` and `/schema` are reported unreliable

Two sources in this corpus report different operational experiences with what looks like one task — establishing how many rows a table holds and what columns it has — but they reach it over different access surfaces. The [[concepts/provenance-aware-resource-discovery]] page treats scale and schema as things discovery must expose, which only works if they can be read reliably. One project read counts successfully via Iceberg metadata, the row counts carried in the table format's own manifests; the other, a cross-project pitfalls report, records a conditional unreliability for a REST (HTTP) endpoint — `/count` over loops of many tables, `/schema` on large tables. Whether the difference tracks the interface, the query pattern, or the table decides whether a discovery card may quote a row count at face value or must also record how that count was obtained.

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
