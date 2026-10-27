---
type: "Finding"
description: "33% of essential genes have COG assignments vs 5% of dispensable genes and 92% have KEGG KO assignments vs 53%, and the report suggests the ~8% of essential genes without KO are potential novel essential functions."
finding_id: "acinetobacter_adp1_explorer--4460d103"
result: "inference"
source: "acinetobacter_adp1_explorer"
quantities: [{"value": "33%", "what": "essential genes with COG assignments", "unit": "percent", "denominator": "essential genes", "scope": "vs 5% of dispensable genes"}, {"value": "92%", "what": "essential genes with KEGG KO assignments", "unit": "percent", "denominator": "essential genes", "scope": "vs 53% of dispensable genes"}, {"value": "~8%", "what": "essential genes without KO assignment", "unit": "percent", "denominator": "essential genes", "scope": ""}]
caveat: "The database covers only A. baylyi, so the essentiality-annotation pattern is not shown for other species without similar databases."
first_added: "2026-10-27"
source_hash: "ec7429b1cf2b99caae21a458ffae48609efc6384c9a4b7e3a9b1385d70024218"
---
# Unannotated essential genes are leads for novel essential functions

33% of essential genes have COG assignments vs 5% of dispensable genes and 92% have KEGG KO assignments vs 53%, and the report suggests the ~8% of essential genes without KO are potential novel essential functions. [src: acinetobacter_adp1_explorer]

## Key figures

- **33%**: essential genes with COG assignments (denominator essential genes; scope vs 5% of dispensable genes) [src: acinetobacter_adp1_explorer]
- **92%**: essential genes with KEGG KO assignments (denominator essential genes; scope vs 53% of dispensable genes) [src: acinetobacter_adp1_explorer]
- **~8%**: essential genes without KO assignment (denominator essential genes) [src: acinetobacter_adp1_explorer]

## Evidence

> Essential genes are dramatically more annotation-rich than dispensable genes: 33% of essential genes have COG assignments vs only 5% of dispensable genes. Similarly, 92% of essential genes have KEGG KO assignments vs 53% of dispensable genes. This pattern is expected — essential genes tend to encode well-characterized housekeeping functions — but it also means the functionally unannotated essential genes (~8% without KO) are particularly interesting as potential novel essential functions. [src: acinetobacter_adp1_explorer]

From the report [[summaries/acinetobacter_adp1_explorer__REPORT]].

## Caveat

The database covers only A. baylyi, so the essentiality-annotation pattern is not shown for other species without similar databases. [src: acinetobacter_adp1_explorer]

> - **Single species**: This database covers only *A. baylyi*. Cross-species comparisons would require similar databases for other organisms. [src: acinetobacter_adp1_explorer]

## Other caveats in this report

- Of 121,519 growth predictions across 14 genomes, 105,376 (87%) required at least one gapfilled reaction; false negatives had higher mean gap counts than correct predictions. Prediction reliability therefore depends on gapfilling quality. [src: acinetobacter_adp1_explorer]
- No gene has all six modalities; FBA coverage is 15%, restricting the FBA–TnSeq concordance analysis to 866 genes. [src: acinetobacter_adp1_explorer]
- Although reported as 100% complete, the three-table cluster mapping may have split-or-merge edge cases. [src: acinetobacter_adp1_explorer]
- The report cautions that 87% of growth predictions depend on gapfilled reactions and that 243 missing functions limit genomic support. [src: acinetobacter_adp1_explorer]
- A 37-table PhageFoundry Acinetobacter genome-browser collection was identified but not deeply queried. [src: acinetobacter_adp1_explorer]
