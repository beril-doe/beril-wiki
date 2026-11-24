---
type: "Method"
description: "The fraction of species in a clade carrying a given KO, used as a per-event uncertainty proxy and signature of within-clade structure."
sources: ["summaries/discoveries.md", "summaries/gene_function_ecological_agora__REPORT.md"]
aliases: ["LC"]
---
# leaf_consistency

leaf_consistency (LC, leaf consistency) is the fraction of species in a clade that carry a given KO (KEGG ortholog). The gene_function_ecological_agora project uses it as a per-event uncertainty proxy and as a signature of within-clade structure. [src: gene_function_ecological_agora] It is a descriptive statistic, not a hypothesis test. [src: gene_function_ecological_agora] See [[summaries/gene_function_ecological_agora__REPORT]] and [[summaries/discoveries]].

## Key facts

- Definition: per-(rank × clade × KO) leaf_consistency is the fraction of clade species carrying that KO. [src: gene_function_ecological_agora]
- Computation: NB28e read the data via Spark, divided species-with-KO by total species in each rank × clade × KO grouping, and merged the result to 16.7M gain events with 97.8% coverage. [src: gene_function_ecological_agora]
- It was computed once per (rank × clade × KO) tuple, so the report says there is nothing to correct. [src: gene_function_ecological_agora]
- Uses: per-event uncertainty and within-clade structure characterization. [src: gene_function_ecological_agora]
- The report calls it a reusable substrate for separating "near-fixed in clade" (high LC) signals from "patchy in clade" (low LC) signals. It can also detect within-clade heterogeneity that deep-rank averaging would obscure. [src: gene_function_ecological_agora]

## Pattern across gain depth

Leaf_consistency falls as gains get older. Recent gains have a long right tail toward 1.0, meaning clades where the KO is fully fixed. Ancient gains compress toward 0, meaning the KO is retained in a small fraction of phylum members after diversification and loss. [src: gene_function_ecological_agora]

Median values fall monotonically across depth bins: recent 0.34, older_recent 0.30, mid 0.26, older 0.23, ancient 0.20. The report reads this as validating its M22 expectation. [src: gene_function_ecological_agora] The discoveries digest describes the same decrease, from 0.34 to 0.20, as independent validation. [src: discoveries]

One figure in the same report differs. It states per-depth_bin medians ranging from 0.05 ancient to 0.26 recent across n=16.7M gain events. [src: gene_function_ecological_agora] The claims do not explain the difference from the 0.20–0.34 range. Both are reported here as written.

## Interpretation as signal confidence

The report treats recent-gain attribution as cleaner. For ancient gains, subsequent within-clade losses dilute the signal. The depth-wise leaf_consistency figure is described as the project's atlas-wide signal-confidence map. [src: gene_function_ecological_agora] Bootstrap-based per-event uncertainty remains future work. [src: gene_function_ecological_agora]

## Example: mycolic-acid KOs

Mycolic-acid KOs in Mycobacteriaceae had median LC=0.15, below the atlas reference of 0.20. [src: discoveries] The report reads this to mean that mycolic gain events land in clades where only ~15% of family members carry the KO panel. [src: discoveries]

## Related concepts

- [[concepts/clade-level-innovation-signals-and-their-rank-dependence]]
- [[concepts/horizontal-gene-transfer-inference-metrics-and-control-class-calibration]]
- [[concepts/core-versus-accessory-partitioning-of-gene-functions-and-trait-genes]]
