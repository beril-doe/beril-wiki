---
type: "Finding"
description: "xoxF co-occurred in 49/62 lanmodulin genomes (79.0%), below the preregistered 80% threshold, with a one-sided p value of 0.65, so H3b was not formally supported."
finding_id: "lanthanide_methylotrophy_atlas--6543a6a6"
result: "null result"
source: "lanthanide_methylotrophy_atlas"
quantities: [{"value": "49 / 62 = 79.0 %", "what": "lanmodulin genomes also carrying xoxF (any source)", "unit": "%", "denominator": "62 lanmodulin genomes", "scope": "preregistered threshold 80 %"}, {"value": "0.65", "what": "one-sided binomial p value", "unit": "", "denominator": "", "scope": ""}]
caveat: "For xoxF, calls were 418 shared, 3,272 eggNOG-only, and 1,402 bakta-only, so the xoxF co-occurrence depends on which annotation source is used."
first_added: "2026-10-27"
source_hash: "4c006958be98f494be09edfff08176308c57490b4b48dc38c5753450c3d8e304"
---
# Lanmodulin–xoxF co-occurrence falls just short of preregistered threshold

xoxF co-occurred in 49/62 lanmodulin genomes (79.0%), below the preregistered 80% threshold, with a one-sided p value of 0.65, so H3b was not formally supported. [src: lanthanide_methylotrophy_atlas]

## Key figures

- **49 / 62 = 79.0 %**: lanmodulin genomes also carrying xoxF (any source) (denominator 62 lanmodulin genomes; scope preregistered threshold 80 %) [src: lanthanide_methylotrophy_atlas]
- **0.65**: one-sided binomial p value [src: lanthanide_methylotrophy_atlas]

## Evidence

> xoxF co-occurrence (any source) is **49 / 62 = 79.0 %**, just under the pre-registered 80 % threshold (one-sided binomial p = 0.65, **H3b not formally supported**). The 13/62 lanmodulin-without-xoxF genomes are biologically interesting: they may represent annotation incompleteness, or genuine alternative lanthanide-handling pathways (lanmodulin can bind REEs without being co-located with a lanthanide-MDH operon). [src: lanthanide_methylotrophy_atlas]

From the report [[summaries/lanthanide_methylotrophy_atlas__REPORT]].

## Caveat

For xoxF, calls were 418 shared, 3,272 eggNOG-only, and 1,402 bakta-only, so the xoxF co-occurrence depends on which annotation source is used. [src: lanthanide_methylotrophy_atlas]

> | xoxF | 418 | 3,272 | 1,402 | **eggNOG K00114 primary**; bakta as union | [src: lanthanide_methylotrophy_atlas]

## Other caveats in this report

- The initial per-phylum binomial framework did not formally control phylogenetic non-independence; the report describes three subsequent validation strategies. [src: lanthanide_methylotrophy_atlas]
- Environmental associations used per-class Fisher exact tests for any xoxF against a generic-environmental reference, with Benjamini–Hochberg correction. [src: lanthanide_methylotrophy_atlas]
- The REE-impacted class had only 37 genomes; its 10.81% xoxF rate and odds ratio 3.51 were descriptive, with adjusted p value 0.082. [src: lanthanide_methylotrophy_atlas]
- The report grades H2 as partially supported: soil/sediment and marine enrichment and host-associated depletion passed its correction, while the n=37 REE-impacted elevation did not pass the false-discovery-rate threshold (p_BH = 0.082). [src: lanthanide_methylotrophy_atlas]
- Of 2,185 genomes with no eggNOG pqq, 1,288 (59%) had at least one bakta PQQ product. The other 897 (24% of all xoxF carriers) lacked evidence in both sources; assembly incompleteness, pseudogenization, and community-acquired PQQ remain unresolved without sequence-level inspection. [src: lanthanide_methylotrophy_atlas]
