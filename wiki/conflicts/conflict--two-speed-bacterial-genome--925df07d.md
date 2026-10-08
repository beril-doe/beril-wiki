<!-- tension-hash: 925df07d7dbe2321 -->
# Do Pangenome Projects Share a Genome-Wide Singleton Baseline?

Two projects that compare gene-cluster cohorts against a genome-wide pangenome baseline report the same core baseline of 46.8% but different singleton baselines: 35.3% in one project and 37.9% across 132,531,501 gene clusters in another [src: plant_microbiome_ecotypes, phage_defense_arsenal]. A pangenome is the full set of gene clusters across the genomes of a species. A core cluster is one that its species pangenome classifies as core. A singleton cluster is found in only one genome. The tension is recorded on [[concepts/two-speed-bacterial-genome]]. Because neither report explains the gap, comparisons of singleton fractions across these projects should not assume a shared baseline [src: plant_microbiome_ecotypes, phage_defense_arsenal].

## Evidence Sides

**Side A: singleton baseline of 35.3%**
plant_microbiome_ecotypes reports a genome-wide baseline of 46.8% core and 35.3% singleton [src: plant_microbiome_ecotypes, phage_defense_arsenal]. The TENSION text gives no cluster denominator for this baseline.

**Side B: singleton baseline of 37.9%**
phage_defense_arsenal reports a genome-wide baseline of 46.8% core and 37.9% singleton across 132,531,501 gene clusters [src: plant_microbiome_ecotypes, phage_defense_arsenal].

**Shared caveat**
Neither report explains the difference between the singleton values. Comparisons of singleton fractions across these projects should therefore not assume a shared baseline [src: plant_microbiome_ecotypes, phage_defense_arsenal].

## Possible Reconciliations

- **Hypothesis 1 (different denominators):** The projects may have computed the singleton fraction over different sets of clusters or species. For example, one project may have filtered species or cluster types before computing it.
- **Hypothesis 2 (different classification rules):** The projects may define "singleton" differently, for instance by genome-count threshold or by how they treat species with very few genomes.
- **Hypothesis 3 (different data snapshots or aggregation):** The baselines may come from different releases of the pangenome tables in the KBase Data Lakehouse. They may also differ in aggregation, such as pooling clusters across all species versus averaging per species.

The evidence supplied here does not test any of these hypotheses. Each is a candidate to test, not an explanation.

## Resolving Work

- **Recompute both baselines from identified inputs.** First identify each project's actual pangenome input tables and versions in the KBase Data Lakehouse, then recompute the core and singleton fractions with each project's query logic. Does the singleton gap reproduce, and does it come from the data or from the query logic?
- **Audit the denominators.** Compare the species and cluster inclusion filters in each project's notebooks against the 132,531,501-cluster denominator. Does one baseline exclude species, cluster types or genomes that the other includes?
- **Tabulate the singleton definitions.** List the genome-count and species-size rules each project uses to call a cluster singleton, then reclassify clusters under both rules. How much of the singleton gap does the definition alone explain?
- **Compare cohorts against both baselines.** Compare each project's cohort singleton fractions against both reported baselines. Do any accessory-enrichment conclusions change direction or lose significance?
- **Pin a canonical baseline.** Publish a single versioned genome-wide core and singleton baseline, with an explicit denominator and definition, for use across [[concepts/two-speed-bacterial-genome]] analyses. Can future projects cite it, so that their singleton comparisons share a reference?
