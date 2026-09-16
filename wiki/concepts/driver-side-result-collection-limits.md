---
type: "Concept"
description: "In several documented genome-scale analyses on the KBase Data Lakehouse, failures occurred when distributed Spark results were pulled into one driver process, either by hitting the driver-result size cap or by exhausting driver memory; the page also covers the reported staging, batching, push-down and algebraic remedies."
sources: ["summaries/pitfalls.md"]
---
# Single-Driver Result Collection as a Recurring Failure Point in Documented Genome-Scale Analyses

In several documented large cross-walk analyses on the KBase Data Lakehouse, failures happened when results computed across the Spark cluster were moved into a single driver process. The general warning is that `.toPandas()` pulls all data from the Spark cluster to the driver node. This is slow for large results and can cause out-of-memory errors, so filtering, joins and aggregations should be done in Spark first [src: pitfalls]. The evidence comes from pitfalls met in individual analyses, not from systematic benchmarks. It does not show that collection is the main or dominant scaling limit in general, only that it was the failure point in the cases below. These cases fall into two kinds: a hard cap on serialized result size, and driver memory used up by pandas work after collection [src: pitfalls].

## The hard ceiling on collected results

In one documented case, 1B-row tables were joined (`kbase.genomes.feature` × `contig_x_feature` × `pangenome.gene_genecluster_junction`) and filtered to >200K elements via broadcast. Calling `.toPandas()` on the Spark Connect result hit `spark.driver.maxResultSize = 1024 MB` and threw `Total size of serialized results bigger than spark.driver.maxResultSize` [src: pitfalls]. The source states that the cap cannot be raised with `SET spark.driver.maxResultSize` at runtime, because the property is read-only after session start [src: pitfalls].

The source gives an estimate, not a measurement, of the scale at which the cap matters. A filtered `contig_x_feature` table of 218K [[entities/bacteroidota]] contigs × ~140 features/contig gives 30M+ rows. At ~50 bytes serialized per row, that is ≈ 1.5 GB. The source calls this the standard pattern in any project doing genome-context cross-walks at >200 species [src: pitfalls].

The same ceiling appeared in a pangenome extraction. Gene-cluster memberships for *[[entities/klebsiella-pneumoniae]]* (250 genomes × ~5,500 genes per genome) were extracted via `gene` JOIN `gene_genecluster_junction` WHERE `genome_id IN (...)`, and the extraction exceeded Spark's `spark.driver.maxResultSize` (1GB default) [src: pitfalls]. The query succeeded in Spark and failed only when results were collected to the driver node. This **supports**, for this case, the observation that the failure happened at collection and not during distributed execution [src: pitfalls].

## Driver memory, not just result size

Staying under the result cap is not enough, because pandas operations after collection can use up driver memory. One example is a spatial-range merge done in pandas: focal_features × contig_features on contig_id, then a filter by `±NEIGHBOR_BP`. This builds a Cartesian product and then filters it. For 80K focal features × 21K contigs × ~105 features/contig on average, the merged DataFrame is ~24M rows × 9 columns. That is a ≈ 9 GB working set, and it ran out of memory on a 16 GB driver [src: pitfalls].

This failure came up in a [[entities/polysaccharide-utilization-loci]] (PUL, clustered polysaccharide-degradation genes) gene-neighborhood analysis in Bacteroidota. The full run at 723K focal × 210K contigs failed. A run sampled down to 309 species still ran out of memory at 80K × 21K [src: pitfalls]. By contrast, a [[entities/photosystem-ii]] (PSII) neighborhood at 27K focal × 16K contigs, with a 16M-row merge, fit in memory. The PUL and [[entities/mycolic-acid]] merges at full scale did not [src: pitfalls]. This **refines** the scaling picture: in these analyses, success depended on the size of the intermediate merge, not on the inputs alone. The boundary is documented only for these few analyses [src: pitfalls].

A third case involved an exploded intermediate. Tree-based donor inference computed a per-(donor genus × KO) "donor candidate event" count by exploding 6.3M gain events × ~20 candidate-donor genera per event. The source puts this at about a 126M-row exploded DataFrame of ~19 GB. These sizes are the source's approximate figures, not reported measurements. The step ran out of memory [src: pitfalls].

## Remedies

The reported workaround for the result-size cap is staging. Write the Spark result to MinIO with `df.coalesce(N).write.mode("overwrite").parquet("s3a://cdm-lake/...")`, then read it back with `spark.read.parquet(path).toPandas()`. According to the source, the read-back uses Spark Connect's parquet streaming path, which does not hit the result-size cap [src: pitfalls]. The stated alternative is to read the staged data directly with `pyarrow.parquet.read_table(path)` via s3fs, provided PyArrow is configured. The source gives no timings for either route [src: pitfalls].

The source proposes two workarounds for the spatial-merge memory failure. The first is to process focal features in batches of ~10K, merge each batch and accumulate an aggregate result. The second is to do the spatial-range filter in Spark by pushing the BETWEEN clause through, so that only the per-feature aggregate is collected to the driver [src: pitfalls]. Both are presented as proposals, and the source reports no outcome for either on the failed PUL run [src: pitfalls].

The donor-inference explode was replaced with an algebraic identity. Take each (family F × KO K) with R_FK total recipient events. Every genus G in F that has K present is a candidate donor for (R_FK − recipient_events_for_G). This can be computed as a single join plus a subtraction, with no explode. Stage 2b ran in 142s instead of running out of memory [src: pitfalls]. This is the only remedy here with a reported execution time. The source does not compare it against running the original explode on a larger driver [src: pitfalls].

For pangenome extractions involving species with >200 genomes, the source recommends splitting the genome list into batches of 50-100 and concatenating the results. Its alternative is to increase `spark.driver.maxResultSize` in the Spark session config. It also notes that the per-species extraction script catches this error with try/except and continues to the next species [src: pitfalls].

## Unresolved configuration question

The two entries on `spark.driver.maxResultSize` refer to different configuration stages, so they do not necessarily contradict each other. One says the property cannot be raised via `SET` at runtime because it is read-only after session start, and recommends Parquet staging [src: pitfalls]. The other suggests raising it in the Spark session config as an alternative to batching [src: pitfalls]. Neither entry says whether users of Spark Connect sessions on the Lakehouse can set the property when the session is created. That question remains open [src: pitfalls].

## Open Directions

- Test whether `spark.driver.maxResultSize` can be set at Spark Connect session creation on the KBase Data Lakehouse. This would settle the configuration question above and show whether batching or staging is the only way past the cap [src: pitfalls].
- Rerun the Bacteroidota PUL neighborhood with the BETWEEN filter pushed into Spark, collecting only per-feature aggregates. This would show whether push-down removes the driver-memory failure at full scale, where the source reports only the failure [src: pitfalls].
- Benchmark Parquet staging against direct `pyarrow.parquet.read_table` reads on the same 1B-row join cross-walk. This would measure wall-time and memory for both reported cap workarounds, which have no timings in the source [src: pitfalls].
- Apply join-and-aggregate reformulations like the donor-inference identity to other explode-heavy steps, and compare them with larger-driver runs. This would test whether algebraic rewriting generalizes beyond the single Stage 2b case [src: pitfalls].
- Profile where wall-time and failures occur across a set of large analyses, covering distributed execution as well as driver collection. This would test whether driver collection is in fact the most common scaling limit, which the current single-case pitfalls cannot establish [src: pitfalls].

Related: [[concepts/join-strategy-and-table-partitioning-cost]], [[concepts/vectorization-versus-row-wise-iteration]], [[concepts/silent-failure-modes-in-distributed-queries]], [[entities/spark-sql]], [[summaries/pitfalls]].
