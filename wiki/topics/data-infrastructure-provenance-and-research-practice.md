# Data Infrastructure, Provenance, and Research Practice

This topic covers how the data beneath the corpus's biology is organized, named, ingested, joined and audited, and how research practice catches the errors those steps introduce. One project inventoried the KBase Data Lakehouse itself. Another audited the provenance (record of origin) behind one overloaded resource name. Two central digests record pitfalls and review findings from many projects [src: berdl_data_atlas, nmdc_context_audit, pitfalls, discoveries]. Across them, a shared column, a matching name or an executable join is only a starting point for validation [src: berdl_data_atlas, nmdc_context_audit]. A successful exit status does not show that outputs were saved [src: pitfalls].

## Literature Context

The candidate literature is uneven: most papers address clinical or gut-microbiome biology, and only a few speak to data infrastructure. Those few establish that integrating sequence data with provenance and phenotype is an accepted design goal. PubMLST's BIGSdb platform curates sequence data with provenance and phenotype records for over 100 microbial species and genera. It exposes them through a RESTful application programming interface (API), a web-service interface for programmatic data access [PMID 30345391]. ERIC similarly combines genomic, proteomic, biochemical and microbiological information for a defined set of enteropathogens [PMID 17966403]. Reviews of microbiome practice stress that classic experimental-design and reproducibility issues persist alongside newer methods [PMID 29795328]. They also emphasize data variability and metadata collection [PMID 35362479]. Low-biomass work adds that contamination can confound interpretation unless minimal controls such as the 'RIDE' checklist are applied [PMID 30497919]. MaAsLin 2 was built to control false discovery in noisy, zero-inflated, high-dimensional meta-omics data, and its evaluation rests on simulations [PMID 34784344].

A second strand shows that labels and database matches are fallible. One study applied two programs, TB-Profiler and PhyResSE, to whole-genome data from 266 *Mycobacterium tuberculosis* isolates. Their average concordance with phenotypic testing was 91.96% vs. 91.4% for first-line drugs and 79.67% vs. 78.20% for second-line drugs. The authors attribute discordance partly to mutation-database limitations, especially for second-line drugs. They also cite the choice of critical concentration, variable reproducibility of phenotypic tests and the analysis program [PMID 30981926]. In 301 clinical yeast isolates, API 20C AUX misidentified 16.2%, and the authors call for better reference databases [PMID 30828570]. Named reference strains can also drift. Among 12 *Staphylococcus aureus* strains, whole-genome optical mapping showed a 19-kbp deletion in USA300_FPR3757 relative to its in silico map. Resequencing identified the deleted fragment as a 13 kbp-long integrative conjugative element, ICE6013 [PMID 25297888]. At cohort scale, obesity–microbiome signatures are often contradictory, which motivated a pooled meta-analysis of 3329 samples from 17 countries [PMID 38265338].

The corpus is **consistent** with this literature and **extends** it to joins across a multi-tenant platform, the KBase Data Lakehouse. It documents identity failures that arise when resources are joined. One example is the ENIGMA MT20 strain-name collision with an unrelated genome in GTDB (the Genome Taxonomy Database). Rename and prefix traps are others, all documented in [[concepts/taxonomic-nomenclature-reconciliation]]. The argument in [[concepts/provenance-aware-resource-discovery]] for exposing provenance at search time generalizes the provenance-plus-phenotype model that BIGSdb applies within one platform. The corpus's emphasis on null distributions and sample-size discipline in [[concepts/adversarial-research-quality-assurance]] fits the literature's focus on false-discovery control. However, that evidence comes from one project and is not a replication.

Several operational findings in the corpus are not described in the candidate abstracts:
- the 16,640 vs. 51,711,888 biosample "scale trap" behind an overloaded resource name;
- silent ingestion failures, covered in [[concepts/foreign-dump-ingestion-fidelity]];
- executors that exit successfully without saving outputs;
- schema bridges that remain potential rather than validated, as discussed in [[concepts/cross-tenant-data-bridging]].

All literature comparisons here rest on abstracts only.

## What the Corpus Shows

**Ownership structures observed availability.** The atlas inventories 1,740 deduplicated tables across 119 databases, 17 tenants (governance groups that own namespaces) and 10 funding agencies or programs [src: berdl_data_atlas]. DOE accounts for approximately 78% of tables, with DOE-BER contributing 63% [src: berdl_data_atlas]. Volume is not reuse: ENIGMA holds 36% of tables but appears in only 6 projects, whereas KBase appears in 53/66 projects [src: berdl_data_atlas]. Of 66 audited projects, 51, or 77%, span multiple tenants [src: berdl_data_atlas].

Table breadth also does not guarantee coverage of a given organism:
- *Acinetobacter baylyi* ADP1 is not present in the Fitness Browser, a collection of genome-wide mutant fitness assays [src: acinetobacter_adp1_explorer].
- *E. coli* K-12 (Keio, GCF_000005845.2) had 0 GapMind (pathway-completeness predictor) predictions in a coverage check of the KBase pangenome collection [src: essential_metabolome].
- ENIGMA CORAL contains no *Desulfovibrio vulgaris* Hildenborough records [src: field_vs_lab_fitness].

Metadata gaps behave the same way. Only 83,227 of 293,059 genomes, or 28.4%, have AlphaEarth environmental embeddings (vector descriptors of a genome's environment), and such gaps can reflect missing coordinates rather than biological absence [src: pitfalls]. [[concepts/data-landscape-ownership-and-coverage-bias]] develops this argument.

**A name, a tenant or a shared column is an entry point, not evidence.** The 20 database names containing "nmdc" resolve to 7 real, maintained resources in six provenance classes. One, `kbase.nmdc_neon`, is NEON (the NSF National Ecological Observatory Network) rather than NMDC (the National Microbiome Data Collaborative) [src: nmdc_context_audit]. The genuine NMDC biosample set holds 16,640 samples, while the co-hosted mirror from NCBI (the National Center for Biotechnology Information) holds 51,711,888, which the audit calls a ~3,000× scale trap [src: nmdc_context_audit]. [[concepts/provenance-aware-resource-discovery]] argues that provenance, scale, currency and access conditions should be shown at the point of search [src: nmdc_context_audit, pitfalls, webofmicrobes_explorer].

Schema compatibility is weaker still. The atlas finds 536 unordered cross-tenant bridges, counted at tenant-by-topic-cell granularity through 29 canonical join keys. These describe potential connectivity, not validated joins, and only UC1 of five use cases was sample-validated [src: berdl_data_atlas]. [[concepts/cross-tenant-data-bridging]] separates four evidence states: shared keys, overlapping values, an executable join and an interpretable result [src: berdl_data_atlas].

[[concepts/taxonomic-nomenclature-reconciliation]] shows what goes wrong when identities are assumed:
- **Strain-name collisions.** ENIGMA MT20 (*Rhodanobacter glycinis*) matched MT20 in GTDB (the Genome Taxonomy Database), which is *Streptococcus pneumoniae*; 12 of 32 strain-name linkages were incorrect genus matches [src: pitfalls, genotype_to_phenotype_enigma]. The repair reduced verified linkages from 32 to 20 but eliminated all false matches [src: genotype_to_phenotype_enigma].
- **Taxonomic renames.** Unreconciled renames produced log₂FC (log-base-two fold change) ≈ 28 artifacts. The inflammatory bowel disease (IBD) project built a synonymy layer mapping 2,417 aliases to 1,848 canonical species [src: pitfalls, ibd_phage_targeting].
- **Identifier prefixes.** Mismatched `GB_`/`RS_` prefixes produce zero-row joins; stripping them gave 100% overlap for all tested species [src: pitfalls].
- **Address changes.** The incomplete Delta-to-Iceberg migration changes live addresses to `catalog.namespace.table`, so addresses must be resolved through live catalog discovery [src: pitfalls].

**Validated integration often yields smaller bridges, nulls or mapped gaps.** For *Pseudomonas* FW300-N2E3, a four-resource join found 17/21 (81%) testable metabolites fully concordant and none fully discordant, but 37/58 (64%) metabolites occurred only in Web of Microbes (WoM, an exometabolomics resource) [src: fw300_metabolic_consistency]. The analyzed 2018 WoM snapshot records no organism consumption action, so production cannot be read as utilization [src: webofmicrobes_explorer].

Other validated joins narrowed or returned nulls:
- The ENIGMA growth-curve corpus aligns with RB-TnSeq (random barcode transposon sequencing) fitness data through only 486 strain × condition anchor pairs [src: genotype_to_phenotype_enigma].
- Environmental species did not have stronger partial correlations than human-associated species (U=1536, p=0.83) [src: ecotype_env_reanalysis].
- 74/83 (89%) enrichment compounds remained organism-dark, meaning no ENIGMA-isolate prediction or measured fitness could call them [src: enigma_carbon_census_1].
- In [[concepts/multi-omics-integration]], a 1,286-KO (KEGG ortholog) repertoire score did not predict metal fitness [src: metal_fitness_atlas].

An integration can therefore establish a knowledge gap rather than a biological conclusion [src: enigma_carbon_census_1].

**Pipelines and executors can fail silently.** [[concepts/foreign-dump-ingestion-fidelity]] documents several ingestion problems:
- MySQL dumps encode NULL as a literal `\N` [src: pitfalls].
- A data definition language (DDL) trailer defeats the schema regular expression [src: pitfalls].
- An inline comment causes the ingest pipeline to skip a whole table with no error message or quarantine entry [src: pitfalls].
- The UTF-8 workaround completes the export but replaces invalid bytes with U+FFFD characters [src: pitfalls].

[[concepts/analysis-provenance-and-reproducible-outputs]] records two further failures. `nbconvert --inplace` exited with code 0 while saving zero cell outputs. Separately, notebooks NB08/NB09/NB10 existed only as outputs, with no committed code [src: pitfalls]. Each of these failures is documented once, so how often they occur across projects is not established [src: pitfalls].

**Adversarial review is a distinct quality-assurance layer that itself needs auditing.** [[concepts/adversarial-research-quality-assurance]] reports that standard review found no critical issues, while adversarial review of the same files found 5 critical and 6 important issues [src: discoveries, ibd_phage_targeting]. Both accounts describe one project, so this is a single case rather than a replication [src: discoveries, ibd_phage_targeting]. Recurring failure classes were:
- thresholds reported without null distributions [src: discoveries];
- sample-size overclaims [src: discoveries];
- hypothesis labels that did not match the test [src: discoveries];
- falsifiability rules loose enough to pass on random data [src: discoveries].

Repair did not always overturn the biology. An observed Jaccard (set-overlap) index of 0.104 against a null mean of 0.785 ± 0.054, with an empirical permutation p = 0.000 over 200 permutations of randomized ecotype labels, showed the original statistic was wrong but the conclusion survived [src: discoveries, ibd_phage_targeting].

Reviewers fabricate too. The functional-atlas project found a Mendoza 2020 PMID (PubMed identifier) hijack, in which a real PMID was attached to an unrelated purported citation; a later round, REVIEW_8, had 0 fabrications, with 7/7 DOIs (digital object identifiers) auto-verified [src: gene_function_ecological_agora]. The same class of repair took 7 notebooks when caught at notebook scope and a single plan-edit pass when caught at plan scope [src: discoveries].

## Tensions and Caveats

**Self-contradicting reports.** Several reports state figures in prose that disagree with their own tables, so any single number carried forward takes a side [[conflicts/conflict--adversarial-research-quality-assurance--a6ef7613]] [src: bacdive_phenotype_metal_tolerance, cf_formulation_design, ibd_phage_targeting, pitfalls, snipe_defense_system, truly_dark_genes]. In one specific case, a screen is stated as 188 strains × 96 phages = 17,672 pairs, which is internally inconsistent, while a 94-phage denominator appears elsewhere [[conflicts/conflict--adversarial-research-quality-assurance--eca086c5]] [src: snipe_defense_system, ibd_phage_targeting].

**Attribution reliability.** The atlas tags some ontologies "NMDC integrated", which the audit reads as provenance blur. Agency shares may therefore reflect naming rather than origin; this remains a hypothesis [[conflicts/conflict--provenance-aware-resource-discovery--0fe66702]] [[conflicts/conflict--data-landscape-ownership-and-coverage-bias--4b4b2ec9]] [src: berdl_data_atlas, nmdc_context_audit]. The atlas also attributes PhageFoundry to Defense / HHS in one place, against a confirmed DOE BRaVE mapping in its caveats [src: berdl_data_atlas]. The audit's provenance classes are themselves inferred, because no ingestion manifest is exposed in the catalog [src: nmdc_context_audit].

**Access surfaces.** Metadata counts succeeded in the audit but are unreliable through REST, a web-service interface. These findings concern different access surfaces, so discovery cards should record the query path used [[conflicts/conflict--provenance-aware-resource-discovery--f0c8f1e3]] [src: nmdc_context_audit, pitfalls].

**Collection identity.** "UniRef" names both partial `kbase_uniref*` samples and dated `refdata_uniref*_2026_01` collections [[conflicts/conflict--provenance-aware-resource-discovery--f19db99c]] [src: pitfalls, berdl_data_atlas].

**Bridging disputes.** Four unresolved questions remain:
- Whether module-level aggregation rescues weak fitness bridges: modules gave delta phi=+0.053 in one project, while another found no significant link between module conservation and field activity [[conflicts/conflict--cross-tenant-data-bridging--8325c1f4]] [src: cofitness_coinheritance, field_vs_lab_fitness].
- Whether tryptophan concordance implies growth: 0/50 *P. fluorescens* strains used it as a carbon source, while binary growth on it was predicted with AUC (area under the receiver operating characteristic curve) 0.933; the projects measure different endpoints, so whether they truly conflict is open [[conflicts/conflict--cross-tenant-data-bridging--d89b8efa]] [src: fw300_metabolic_consistency, genotype_to_phenotype_enigma].
- Whether IBD bridges face a validation-stage gap or a structurally unidentifiable contrast [[conflicts/conflict--cross-tenant-data-bridging--34478c5a]] [src: ibd_phage_targeting, pitfalls].
- Whether summary measures are comparable across tenants when literature attention and sampling are uneven [[conflicts/conflict--cross-tenant-data-bridging--dd5b9877]] [src: paperblast_explorer, ecotype_env_reanalysis].

**BacDive bridges.** Two bridges from BacDive (a curated bacterial strain-phenotype database) to pangenomes (gene collections pooled across genomes) report 43.4% versus 38.4% strain coverage [[conflicts/conflict--taxonomic-nomenclature-reconciliation--2208cd83]] [src: bacdive_metal_validation, bacdive_phenotype_metal_tolerance]. Separately, GTDB suffix stripping may merge clades that GTDB keeps distinct [[conflicts/conflict--taxonomic-nomenclature-reconciliation--a209158c]] [src: bacdive_metal_validation, cf_formulation_design].

## Where to Go Deeper

- [[concepts/cross-tenant-data-bridging]] — the four evidence states and worked bridges; read first.
- [[concepts/taxonomic-nomenclature-reconciliation]] — identifier, rename and prefix traps behind zero-row and false joins.
- [[concepts/provenance-aware-resource-discovery]] — what a resource card must expose.
- [[concepts/data-landscape-ownership-and-coverage-bias]] — how ownership skews coverage and reuse.
- [[concepts/multi-omics-integration]] — project-level integrations built on these bridges.
- [[concepts/adversarial-research-quality-assurance]] — failure classes and review protocols.
- [[concepts/analysis-provenance-and-reproducible-outputs]] — what a reproducible record needs.
- [[concepts/foreign-dump-ingestion-fidelity]] — silent ingestion failures and remedies.

Key entities: [[entities/kescience-fitnessbrowser]], [[entities/gtdb]], [[entities/kbase-ke-pangenome]], [[entities/gapmind]], [[entities/bacdive]], [[entities/alph-aearth]].

Reports: [[summaries/berdl_data_atlas__REPORT]], [[summaries/nmdc_context_audit__REPORT]], [[summaries/genotype_to_phenotype_enigma__REPORT]], [[summaries/fw300_metabolic_consistency__REPORT]], [[summaries/ibd_phage_targeting__REPORT]], [[summaries/gene_function_ecological_agora__REPORT]].
