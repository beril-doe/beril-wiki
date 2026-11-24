---
type: "Concept"
description: "Covers how a shared name (such as NMDC) is attached to resources of different origin, tenant, scale and authority, and how that misleads resource choice; stops at general documentation practice."
sources: ["summaries/nmdc_context_audit__REPORT.md"]
---
# Provenance overloading of dataset labels in the data lakehouse

A shared name such as "nmdc" is attached in the [[entities/kbase-data-lakehouse]] to resources of different origin, tenant, scale and authority. The NMDC Context Audit found that 20 database names containing "nmdc" resolve to 7 real, maintained resources across three tenants and six provenance classes. [src: nmdc_context_audit] The audit supports its hypothesis (H1) that the label is systematically overloaded. [src: nmdc_context_audit] Its claim that the overloading drives poor resource choice is an inference, not an observed wrong choice. [src: nmdc_context_audit] See also [[summaries/nmdc_context_audit__REPORT]].

## Literature Context

The candidate papers do not study dataset-label overloading directly. They do show that provenance and descriptive metadata are widely treated as prerequisites for finding, understanding and reusing data. The W3C health care and life sciences community profile sets out a guideline for dataset descriptions. It covers elements of description, identification, attribution, versioning, provenance and content summarization, with the aim of supporting indexing, discovery, exchange, query and retrieval, and so FAIR data [PMID 27602295](https://pubmed.ncbi.nlm.nih.gov/27602295/). A virology review likewise notes that viral databases have had an anthropocentric focus on human and clinical pathogens. That focus created inconsistencies in metadata for non-human viruses. The same review says reproducible, scalable tools depend on curated datasets, standardized pipelines and transparent provenance [PMID 43039614](https://pubmed.ncbi.nlm.nih.gov/43039614/).

Two further papers show what happens when provenance is incomplete. A Helsinki course reanalyzed six public proteomics projects. The teams hit recurring barriers, including missing metadata formats, vague parameters and proprietary-only outputs, and they got large discrepancies, for example 13,068 vs. 4,923 proteins. This was a small educational exercise, but its authors conclude that reproducibility hinges on transparent metadata, open formats and executable analysis provenance [PMID 41571719](https://pubmed.ncbi.nlm.nih.gov/41571719/). A narrative review of public-omics reuse in gastric cancer describes "evidentiary dilution", where many studies reuse similar cohorts. It proposes an appraisal framework with resource provenance as one of five domains. The review calls its PubMed scans descriptive signals, not formal quality appraisals [PMID 43005429](https://pubmed.ncbi.nlm.nih.gov/43005429/). Infrastructure papers make a related point. One proposes research objects and distributed ledgers to record chains of provenance across scholarly assets [PMID 28423841](https://pubmed.ncbi.nlm.nih.gov/28423841/). Another describes provenance management and semantically rich metadata as services for selecting resources in bioinformatics workflows [PMID 12855473](https://pubmed.ncbi.nlm.nih.gov/12855473/).

The corpus finding is consistent with this literature in its main thrust. The NMDC Context Audit found that 20 database names containing "nmdc" resolve to 7 resources across three tenants and six provenance classes. The label therefore does not signal origin, tenant, scale or authority. For example, the genuine NMDC biosample set holds 16,640 samples and the co-hosted NCBI mirror holds 51.7M. This matches the literature's view that attribution and provenance must be explicit for correct reuse. In the audit, the specific catalog gap is that no ingestion manifest is exposed, so the classes had to be inferred from schema, table properties, tenant metadata and prior usage. That is narrower than a general absence of provenance metadata.

The corpus extends the literature in one respect. The cited work concerns study-level or repository-level metadata. The audit looks at a single shared name attached to resources of different authority within one platform, the [[entities/kbase-data-lakehouse]]. It also argues for surfacing provenance together with value instead of relabeling. This framing appears to be novel relative to these candidates. The candidates do not test it, and the audit's link from overloading to poor resource choice is an inference, not an observed wrong choice. The papers above likewise show consequences of weak provenance only in other domains. They give no evidence about this platform.

## Provenance classes behind one label

Only some resources carrying the label are genuine NMDC output. The audit classifies nmdc.metadata and nmdc.results as genuine NMDC resources from the NMDC program (DOE-BER). [src: nmdc_context_audit] Two of the four databases in the nmdc tenant are external data re-hosted, not NMDC output. [src: nmdc_context_audit] The other classes are:

- nmdc.ncbi_biosamples is an external re-host of NCBI data, and NCBI BioSample is its true authority. [src: nmdc_context_audit]
- nmdc.ref_data is an external re-host from the Pfam consortium, and Pfam/InterPro is its true authority. [src: nmdc_context_audit] See [[entities/pfam-domain-annotations]].
- kbase.nmdc_arkin is an other-group derivation from LBNL Arkin Lab. [src: nmdc_context_audit]
- kbase.nmdc_mags is NMDC-derived data in the kbase tenant, from KBase / NMDC. [src: nmdc_context_audit]
- kbase.nmdc_neon is a namesake collision. It belongs to NEON (NSF), not NMDC. [src: nmdc_context_audit]

The report asserts that this six-class framework generalizes to other overloaded labels, such as any tenant co-hosting external mirrors. [src: nmdc_context_audit]

## Tenant, scale and acronym traps

Tenant placement misleads. Three NMDC-related databases (nmdc_arkin, nmdc_mags, nmdc_neon) sit in kbase. Inventory grouping uses catalog prefixes, so they are invisible to anyone browsing the nmdc tenant. [src: nmdc_context_audit]

Scale is a second trap. The genuine NMDC biosample universe in nmdc.metadata.biosample_set is 16,640 samples. The co-hosted NCBI mirror holds 51.7M, a ~3,000× difference that the names do not signal. [src: nmdc_context_audit]

The acronym is a third trap. NEON is the National Science Foundation (NSF) National Ecological Observatory Network, a different program from NMDC, with a distinct agency and sampling design. [src: nmdc_context_audit] Reading it as NMDC would corrupt agency attribution. [src: nmdc_context_audit] Related pages: [[entities/nmdc-neon-metagenome-studies]], [[entities/nmdc-integrated-collections]], [[entities/ncbi-env-environmental-metadata]].

The report's warning is that treating the nmdc tenant as one coherent NMDC dataset will mis-scope or mis-attribute data. [src: nmdc_context_audit]

## Co-hosting can be valuable

Some of the co-hosted resources add value. The NCBI mirror adds an attribute-harmonization layer that makes 51.7M raw NCBI samples analytically usable. [src: nmdc_context_audit] The Arkin derivative adds embeddings and traits that do not exist upstream. [src: nmdc_context_audit] The report therefore argues against relabeling or removing resources. It argues for surfacing provenance and value together. [src: nmdc_context_audit]

## Caveats

The link to bad resource choices is inferred from gap analysis and prior-project usage skew. [src: nmdc_context_audit] Wasted time and compute and weakened conclusions are plausible consequences, not observed outcomes. [src: nmdc_context_audit] The provenance classes are inferred from schema, table properties, tenant metadata and prior project usage. No ingestion manifest is exposed in the catalog. [src: nmdc_context_audit]

## Open Directions

- Extend the provenance-audit method to other overloaded labels, to test whether the six-class framework generalizes.
- Trace actual queries or notebooks to see whether users picked the wrong NMDC-named resource. This would replace the inferred link with a direct observation.
- Obtain or build an ingestion manifest and compare it with the inferred classes.
- Group the inventory by provenance class rather than catalog prefix. Then test whether the kbase-tenant NMDC-related databases become findable.
- See [[concepts/audit-blind-spots-in-inventories-of-data-and-its-use]] and [[concepts/documentation-discovery-and-currency-gaps-in-lakehouse-catalogs-and-tooling]] for related gaps.
