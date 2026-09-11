---
type: "Summary"
description: "Operational guide to the KBase Data Lakehouse querying, analysis, reproducibility, and interpretation pitfalls."
doc_type: "short"
full_text: "sources/pitfalls.md"
---
# KBase Data Lakehouse: Common Pitfalls & Gotchas

## Overview

This document is a practical reference for avoiding failures, silent misjoins, biased analyses, irreproducible workflows, and misleading interpretations when querying KBase Data Lakehouse databases. It emphasizes live, access-aware catalog discovery, direct Spark SQL for large workloads, explicit schema and type inspection, provenance-preserving joins, and independent validation of analysis designs. [src: pitfalls]

## Key Findings

### Namespace migration and access

KBase Data Lakehouse is migrating collections from Delta to Iceberg. Migrated tables use `catalog.namespace.table`, such as `kbase.ke_pangenome.genome`, whereas the former Delta form flattened the namespace, such as `kbase_ke_pangenome.genome`. Underscore-form references occur in hundreds of archived files, which are intentionally not rewritten. Migration remains incomplete, so code must discover the live address and prefer the dotted form when available, falling back to the underscore form when the dotted collection is absent. [src: pitfalls]

The `data_lakehouse_ingest` tenant is the MinIO governance-group name rather than the database prefix. The `kbase_ke_pangenome` database is under tenant `kbase`, with dataset `ke_pangenome`; using tenant `kbase_ke` causes access failure, while combining tenant `kbase` with dataset `kbase_ke_pangenome` incorrectly creates `kbase_kbase_ke_pangenome`. [src: pitfalls]

Access failures should be translated to a plain permissions explanation identifying the unreachable table and tenant and directing the user to the KBase Data Lakehouse Tenant Browser. User-facing messages must not expose internal strings such as “S3”, “token”, “403”, “access denied”, or internal service URLs. [src: pitfalls]

The REST API can return 504 Gateway Timeout, 524 Origin Timeout, 503 executor-restart errors, or empty responses. Direct Spark SQL is preferred for complex or large queries; the REST `/count` endpoint is particularly unreliable for loops over many tables, and `/schema` frequently times out on large tables. [src: pitfalls]

### Provenance, identifier, and join integrity

Short ENIGMA strain names are not globally unique. In one example, ENIGMA MT20 was *Rhodanobacter glycinis*, whereas GTDB’s MT20 was *Streptococcus pneumoniae*; the erroneous match involved 8,434 genomes, including 1,751 clinical genomes. Of 32 pangenome linkages through `ncbi_strain_identifiers`, 12 were incorrect genus matches. Genus consistency must be checked, and assembly accessions such as `GCF_*` should be used instead when possible. [src: pitfalls]

MetaPhlAn3 cross-cohort analyses require a synonymy layer rather than simple string normalization. Observed divergences included short names versus full lineage strings, GTDB-renamed *Bacteroides vulgatus* versus *Phocaeicola vulgatus*, *Eubacterium rectale* versus *Agathobacter rectalis*, *Ruminococcus gnavus* versus *Mediterraneibacter gnavus*, and multiple *Clostridium*, *Lactobacillus*, and related reclassifications. In the CrohnsPhage mart, failure to reconcile names produced log₂FC approximately 28, equivalent to approximately 2.68 × 10⁸ fold, because one cohort’s abundance collapsed to a pseudocount. A hand-curated 23-entry synonym map was used for a targeted battery, but full-taxonomy aggregation requires an NCBI-taxid-backed, GTDB-version-aware reconciliation layer. [src: pitfalls]

The pangenome taxonomy tables must be joined through `genome_id`, not `gtdb_taxonomy_id`, because the genome table stores a genus-level taxonomy string while `gtdb_taxonomy_r214v1` stores a species-level string. `gapmind_pathways.clade_name` uses the full `gtdb_species_clade_id`, including the representative accession, rather than the shorter `GTDB_species` value. [src: pitfalls]

Pangenome gene-cluster identifiers are species-specific and cannot be compared directly across species. Cross-species comparisons should use shared representations such as COG categories, KEGG orthologs, or Pfam domains. `eggnog_mapper_annotations.query_name` joins to `gene_cluster.gene_cluster_id`, not `gene.gene_id`; Bakta and InterProScan annotations similarly join at the gene-cluster level. [src: pitfalls]

The `ncbi_env` table is entity-attribute-value data with columns including `accession`, `attribute_name`, `content`, `display_name`, `harmonized_name`, `id`, and `package_content`; it is not a flat genome-metadata table. Metadata extraction requires joining `genome.ncbi_biosample_id` to `ncbi_env.accession`, filtering attributes, and pivoting the long format. [src: pitfalls]

### Experimental and statistical design

The curatedMetagenomicData healthy and disease buckets contain disjoint sub-studies, making a pooled `log_abundance ~ diagnosis + (1 | substudy)` mixed model structurally unidentifiable for the CD-versus-HC contrast. In an ecotype-assigned set of 8,489 samples, 45 sub-studies had at least 10 HC samples, 5 had at least 10 CD samples, and 0 had at least 10 of both. Four IBD sub-studies had at least 10 CD and 10 nonIBD samples, comprising 242 CD and 369 nonIBD samples; a within-substudy contrast combined by inverse-variance meta-analysis is the design-consistent alternative. [src: pitfalls]

Clustering samples on a taxon-abundance matrix and then testing those same taxa within clusters creates selection-on-outcome leakage. In `ibd_phage_targeting`, K=4 LDA ecotypes produced a 33-species Tier-A list with CLR-Δ effect sizes from +0.5 to +3.0, but held-out-species sensitivity yielded Jaccard values of 0.230 for E1 and 0.064 for E3. Leave-one-species-out refitting changed *C. scindens* from a non-significant result to CD increases in both E1, with CI +0.68 to +0.87, and E3, with CI +1.13 to +1.71. Independent within-substudy evidence reduced the Tier-A list from 33 candidates to 3. [src: pitfalls]

When clusters and tests use related data, leakage should be assessed with held-out-feature clustering, leave-one-feature-out refitting, or clustering on a genuinely different functional matrix such as pathways or EC numbers. The document treats a Jaccard value above 0.5 as bounded leakage and below 0.3 as leakage dominating for the cited sensitivity procedure; these are project-specific decision thresholds, not universal statistical guarantees. [src: pitfalls]

In Web of Microbes, organism observations use action codes `I` for increased, `E` for emerged, and `N` for no change, with occasional `D` for decreased; the binary “produced” definition is `action IN ('I', 'E')`. For the “The Environment” control, `D` instead means detected and `N` means not detected, so actor context is required. The 2018 snapshot has no organism-level decreased or consumption action, and approximately 56% of compound names begin with `Unk_`. [src: pitfalls]

BacDive utilization is four-valued rather than binary: `+`, `-`, `produced`, and `+/-`. For *Pseudomonas fluorescens*, indole had 60 “produced” entries and 1 actual utilization test, illustrating why only explicit `+` and `-` observations should enter utilization percentages. [src: pitfalls]

### Coverage and sparsity

AlphaEarth environmental embeddings cover 83,227 of 293,059 genomes, or 28.4%. A separate quality check found 3,838 of 83,287 genomes, or 4.6%, with at least one NaN among 64 dimensions; filtering left 79,449 genomes. Coverage depends on valid latitude and longitude, which are especially sparse for clinical isolates. [src: pitfalls]

Per-genome NCBI environment classification yielded 52.7% unknown labels, or 94,957 of 180,025 genomes, because most BioSample records lack structured isolation metadata. Species-level majority-vote labels reached 91% coverage through keyword classification. [src: pitfalls]

AlphaEarth geographic analyses can be diluted by human-associated samples. The pooled geographic distance–embedding distance curve had a 2.0x near-versus-far ratio, while environmental samples had 3.4x and human-associated samples had 2.0x; analyses should therefore stratify by environment category or exclude human-associated samples when embeddings are used as environmental proxies. [src: pitfalls]

### Scale, typing, and Spark behavior

Many KBase Data Lakehouse numeric fields are strings, including all Fitness Browser columns and relevant pangenome and genome metadata fields. Values must be explicitly cast before comparisons, ordering, arithmetic, or aggregation. Spark `DECIMAL` values arrive in pandas as `decimal.Decimal`; `CAST(... AS DOUBLE)` in SQL or `.astype(float)` after collection prevents mixed-type arithmetic failures. [src: pitfalls]

`SELECT DISTINCT col, COUNT(*)` without `GROUP BY` fails in Spark strict mode with `MISSING_GROUP_BY`; `GROUP BY col` alone is the correct replacement. Spark Connect temporary views can disappear after a reconnect during a long-running query, so views should be re-registered immediately before use. [src: pitfalls]

The pangenome contains billion-row tables, including `gene` and `gene_genecluster_junction`, each approximately 1B rows; `genome_ani` is approximately 421M rows; `eggnog_mapper_annotations` approximately 93M rows; `interproscan_domains` approximately 833M rows; `bakta_db_xrefs` approximately 572M rows; and `gapmind_pathways` approximately 305M rows. These tables require key filters before joins, and results should remain in Spark until the final small output. [src: pitfalls]

A Spark Connect driver result-size cap of 1 GB serialized data makes large `.toPandas()` collections unsafe. For example, a filtered contig-feature result involving 218K Bacteroidota contigs produced more than 30M rows and approximately 1.5 GB serialized; MinIO parquet staging or server-side aggregation is required. Pandas spatial merges can also exceed 9 GB of working memory at approximately 24M intermediate rows, and `iterrows()` over 27K focal features took more than 30 minutes where a vectorized merge completed in approximately 10 seconds. [src: pitfalls]

Disabling `spark.sql.autoBroadcastJoinThreshold` with `-1` can harm performance: an NB10 job joining 13.7M rows with 18,989 species-taxonomy rows hung for 17+ minutes when automatic broadcasting was disabled. The optimizer should generally be trusted, with explicit broadcast hints only when needed. [src: pitfalls]

Long-running JupyterHub kernels can be silently killed after approximately 17–25 minutes without user activity. The recommended recovery pattern is to convert notebooks to scripts, run them with `nohup python3 -u`, write intermediate parquet checkpoints, and provide finalization scripts. `jupyter nbconvert --inplace` can also exit successfully while dropping all cell outputs; writing to a new executed notebook or logging a standalone script is safer. [src: pitfalls]

### Database-specific interpretation rules

GapMind `score_simplified` at `sequence_scope = 'core'` is binary, containing only 0.0 and 1.0, and should be aggregated with `MAX(score_simplified)` at species level. The broader GapMind table has multiple rows per genome-pathway pair, with categories `complete`, `likely_complete`, `steps_missing_low`, `steps_missing_medium`, and `not_present`; the best score must be selected before pathway-level aggregation. The stored metabolic categories are `aa` and `carbon`, not `amino_acid`. [src: pitfalls]

Pangenome core, auxiliary, and singleton flags are integer 0/1 values. Core and auxiliary counts sum to total gene clusters, while singletons are a subset of auxiliary clusters; the flags themselves are mutually exclusive. The `pangenome` identities are `no_core + no_aux_genome = no_gene_clusters`, with `no_singleton_gene_clusters` contained within `no_aux_genome`. [src: pitfalls]

Fitness Browser data requires exact case for `orgId`, filtering by organism because `genefitness` has approximately 27M rows, and casting string-valued `fit` and `t`. KO mapping is a two-hop join through `besthitkegg` and then `keggmember`; `kgroupdesc` uses `desc`, and the experiment grouping column is `expGroup`. Essential genes are absent from transposon fitness records: genefitness-only analyses miss approximately 14.3% of protein-coding genes, while genes absent from genefitness provide only an upper bound on essentiality. [src: pitfalls]

Phylogenetic tree distance tables use bare accessions such as `GCA_001038305.1`, while other pangenome tables use `GB_` or `RS_` prefixes; stripping the first three characters produced 100% overlap in tested species, including 399/399 for Koxy and 287/287 for Btheta. Large ANI analyses are quadratic: *Klebsiella pneumoniae* has 14,240 genomes and *Staphylococcus aureus* has 14,526, so analyses should cap samples at <=500 genomes or subsample. [src: pitfalls]

NMDC classifier and metabolomics tables use `file_id`, but their file-id namespaces do not overlap: classifiers use `nmdc:dobj-11-*` and metabolomics uses `nmdc:dobj-12-*`. They must be bridged through `sample_id` using `omics_files_table`, which contains 385,562 rows and includes `file_id`, `sample_id`, `study_id`, `workflow_type`, and `file_type`. The NMDC `taxonomy_features` table is a wide matrix with numeric taxon-ID columns rather than tidy sample identifiers. [src: pitfalls]

NMDC `abiotic_features` uses mostly `_has_numeric_value` column suffixes, has no `annotations_water_content` column, and stores unmeasured variables as 0.0 rather than NULL; zeros should be converted to NaN before analysis. `metabolomics_gold` compound identifiers include `kegg`, `chebi`, `name`, `inchi`, `inchikey`, and `smiles`, while `annotation_terms_unified` is a gene-annotation lookup rather than a metabolite lookup. [src: pitfalls]

### Reproducibility and workflow hygiene

Three ENIGMA analysis notebooks, NB08, NB09, and NB10, initially existed only as committed outputs rather than notebook history. Every analysis worth saving should have a committed notebook, and `git log --all --oneline -- projects/{project_id}/notebooks/NB*.ipynb` should be checked before submission. [src: pitfalls]

Concurrent agent sessions must use separate Git worktrees or verify `git branch --show-current` immediately before every commit. In the documented 2026-04-24 incident, a checkout by another process moved a commit from `ibd_phage_targeting` onto `plant_microbiome_ecotypes`; the files were recoverable from Git, but the working tree appeared to lose them. [src: pitfalls]

The observatory stores computed outputs flat in `data/`, not in a `data/results/` directory. Detailed synthesis belongs in `REPORT.md`, while `README.md` should remain a concise overview with status, links, metadata, reproduction information, and a link to the report. [src: pitfalls]

Notebook and environment failures include numpy `str_` values that PySpark cannot infer, invalid notebook cells missing `outputs`, non-UTF-8 SQLite text that requires a permissive `text_factory`, SQL schema parsers that mistake `/* ... */` comments for columns, broken symlinks to local Mac paths, Python 3.13 compatibility problems with `statsmodels.api`, and headless kaleido 1.x requiring Chrome. The stated remedies are native `str` conversion, notebook JSON validation, permissive decoding, comment stripping, broken-symlink removal, `statsmodels.formula.api`, and kaleido 0.2.1. [src: pitfalls]

## Caveats

The document repeatedly warns that table schemas, namespace availability, access permissions, API behavior, database contents, and naming conventions can change. Queries should therefore begin with live catalog and schema discovery rather than copied historical SQL, and archived reports and notebooks should be treated as historical records rather than automatically valid executable instructions. [src: pitfalls]

Several recommendations are project-specific safeguards rather than universal thresholds. Examples include the held-out-feature Jaccard boundaries of 0.5 and 0.3, bootstrap sizes of 250–400, the ICA limit of at most 40% of the number of experiments, the `|r| >= 0.3` module-membership rule, the ANI cap of <=500 genomes, and the 50–100 genome extraction batches for large species. These values should be reported with their analysis context rather than generalized without validation. [src: pitfalls]

The document records apparent method- or interface-specific inconsistencies that require care: direct Spark accepts a quoted species ID containing `--`, whereas the REST API rejects queries containing `--`; one section describes per-organism Fitness Browser convenience tables as long format while another database-specific note says they may be pre-pivoted and have non-standard schemas; and NMDC schema notes differ on whether abiotic numeric fields arrive as strings or doubles. The stated resolution is to inspect the live schema and query interface before relying on either description. [src: pitfalls]

Coverage limitations are not equivalent to biological absence. Missing AlphaEarth coordinates, sparse NCBI environment attributes, BacDive–GTDB naming differences, unmatched species concepts, orphan pangenomes, absent tables, and workflow-specific file identifiers can all produce zero or incomplete joins without indicating that the underlying biology is absent. [src: pitfalls]

## Slots Into

- [[concepts/provenance-aware-resource-discovery]] — live catalog discovery, schema inspection, tenant resolution, identifier reconciliation, and the requirement to preserve provenance across database joins.
- [[concepts/cross-tenant-data-bridging]] — tenant-versus-database naming, permissions, namespace migration, and bridges between NMDC, classifier, metabolomics, pangenome, and Fitness Browser resources.
- [[concepts/environment-embedding-geography]] — AlphaEarth coverage, NaN filtering, geographic signal dilution by human-associated samples, and coordinate sparsity.
- [[concepts/ecotype-environment-gene-content]] — cluster-stratified differential-abundance leakage, ecotype confounding, and the need for independent within-substudy validation.
- [[concepts/multi-omics-integration]] — NMDC `file_id` versus `sample_id` namespaces, bridge-table discovery, and tidy versus wide data representations.
- [[concepts/gene-essentiality]] — the absence of essential genes from Fitness Browser transposon records and the resulting upper-bound interpretation.
- [[concepts/pangenome-integration]] — pangenome identifiers, gene-cluster scope, taxonomy joins, GapMind aggregation, orphan records, and annotation join keys.
- [[concepts/condition-specific-fitness]] — Fitness Browser typing, experiment grouping, KO mapping, condition-specific thresholds, and unequal experiment-count effects.
- [[concepts/environmental-resistome]] — environmental metadata sparsity, NCBI EAV handling, and the danger of treating missing environment classifications as absence.
