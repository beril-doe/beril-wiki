---
type: "Concept"
description: "How physical table layout (partitioning) and join strategy (broadcast vs. shuffle, partition-aligned filters vs. pagination) affect the cost of billion-row genomic joins in Spark queries over the KBase Data Lakehouse."
sources: ["summaries/pitfalls.md"]
---
# Join Strategy and Table Partitioning, Not Query Logic, Set the Cost of Billion-Row Genomic Joins

The operational pitfalls recorded by the observatory point to a working hypothesis about large genomic queries on [[entities/spark-sql]]. Their cost appears to depend heavily on how the underlying tables are physically laid out and on which join strategy the engine uses. The evidence comes from practitioner observations and one small profiling run in the central pitfalls digest, not from a controlled benchmark. It suggests the hypothesis that physical layout is a major cost driver. It does not establish that query logic or join strategy cannot materially change the cost of other queries [src: pitfalls].

## Unpartitioned billion-row tables force full scans

Most genome junction tables have ~1 billion rows, and the source advises never querying them without filters [src: pitfalls].

Joining `gene_genecluster_junction` (~1B rows) with `gene` (~1B rows) to build genome × cluster presence matrices takes 3-5 minutes per species, even on Spark. Neither table is partitioned by `gene_cluster_id` or `genome_id`, so every query requires a full table scan [src: pitfalls].

Annotation lookups show the same pattern. The four-table chain gene → gene_genecluster_junction → gene_cluster → eggnog_mapper_annotations can be slow for species with >500 genomes [src: pitfalls].

The source attributes the slowness to `gene` and `gene_genecluster_junction` being stored as unpartitioned parquet. It proposes that partitioning `gene` by `genome_id` and the junction by `gene_cluster_id` would dramatically reduce scan time, but this requires rebuilding the lakehouse tables. No measurement of a rebuilt layout is reported, so the remedy is untested [src: pitfalls].

## Broadcast hints gave a modest gain in one profiling run

Profiling on Smeli (241 genomes, 6K target clusters) gave these per-organism times [src: pitfalls]:

- Without BROADCAST: ~300s [src: pitfalls].
- With `/*+ BROADCAST(tc), BROADCAST(tg) */` on the filter tables: ~274s, an 8% improvement [src: pitfalls].
- With a two-stage approach that filtered the junction first and then looked up genome_ids: ~310s, no improvement [src: pitfalls].
- `.toPandas()` on 1-2M result rows took <2s, so it was not the bottleneck [src: pitfalls].

This result is **consistent with** the full-scan explanation above: in this one case, neither the broadcast hints on the small filter tables nor the two-stage restructuring changed runtime much. It covers a single organism, though, and the partitioning remedy has not been measured. It therefore does not show that join logic cannot matter for other scan-bound queries [src: pitfalls].

## Disabling automatic broadcast preceded a hang

A defensive setting carried over from prior projects, `spark.sql.autoBroadcastJoinThreshold = -1` to "force shuffle joins", caused an NB10 KO atlas job to hang for 17+ minutes on a 13.7M × 18K join. The job was waiting for a shuffle that never materialized. The small-side table (18,989 species_tax rows) was well below the default 10MB broadcast threshold and would have been auto-broadcast at the default setting [src: pitfalls].

The recommended workaround is to remove the autoBroadcast disable and trust the optimizer for small-table joins. Explicit `F.broadcast(small_df)` hints should be used when the optimizer does not auto-detect a small side. The source gives this as a recommendation and does not report a measured rerun after the change [src: pitfalls].

This **adds a different failure mode** to the profiling result rather than refining it. In the hang, the engine-wide broadcast setting was the reported cause. In the Smeli profiling, adding explicit broadcast hints for small filter tables gave a modest gain. Both cases involve small tables that could be broadcast, so whether a small side is present does not by itself explain the difference. The evidence does not show how large the benefits of join strategy are in general [src: pitfalls].

## Partition-aligned filters beat pagination

In the conservation_vs_fitness work, `LIMIT N OFFSET M` pagination made Spark re-scan all rows up to the offset on each query. For extracting cluster representative FASTAs across 154 clades, paginated queries (5000 rows per batch) were orders of magnitude slower than single queries per clade. Because `gene_cluster` is partitioned by `gtdb_species_clade_id`, a single `WHERE gtdb_species_clade_id = 'X'` query per clade is fast. The source advises paginating only when the result set would exceed memory [src: pitfalls].

This case **supports** the layout hypothesis from the other direction. When a table is partitioned and the filter matches the partition key, the extraction becomes fast. Filtering to the natural unit also applies to large non-junction tables: the [[entities/kescience-fitnessbrowser]] `genefitness` table has 27M rows, which motivates filtering by organism [src: pitfalls].

## Tensions

The pitfalls digest gives two different pictures of broadcast handling. The disabled auto-broadcast setting was blamed for a 17+ minute hang, and the recommended fix is to restore the default, though no successful rerun is reported. Explicit broadcast hints on filter tables, by contrast, gave only an 8% improvement for Smeli. The source does not reconcile these cases, and no side-by-side measurement explains why the setting and the hints had such different reported effects [src: pitfalls].

## Open Directions

- Rebuild a test copy of `gene` partitioned by `genome_id` and `gene_genecluster_junction` partitioned by `gene_cluster_id`. Then rerun the Smeli genome × cluster extraction to measure whether the predicted dramatic scan reduction happens, compared with the ~300s baseline [src: pitfalls].
- Rerun the NB10 KO atlas join with default auto-broadcast restored, to confirm that the recommended workaround removes the 17+ minute hang [src: pitfalls].
- Repeat the broadcast-hint profiling on species with more and fewer than 500 genomes, varying the auto-broadcast setting and the hint targets, to find when join strategy changes cost materially [src: pitfalls].
- Benchmark per-organism filtered queries against the 27M-row `genefitness` table versus unfiltered joins, to measure the benefit of organism-level filtering [src: pitfalls].
- Compare these cost patterns with [[concepts/silent-failure-modes-in-distributed-queries]] and [[concepts/driver-side-result-collection-limits]] to separate scan-bound slowness from hangs and collection failures [src: pitfalls].
