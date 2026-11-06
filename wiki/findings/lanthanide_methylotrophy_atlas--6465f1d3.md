---
type: "Finding"
description: "In 293,059 GTDB-r214 genomes, eggNOG annotated xoxF/K00114 in 3,690 and mxaF/K14028 in 195 (ratio 18.92:1, Clopper\u2013Pearson 95% CI [13.07, 27.69]; xoxF fraction 0.9498, 95% CI [0.9425, 0.9558]), and the preregistered one-sided binomial test against the H1 threshold of xoxF fraction > 10/11 \u2248 0.909 gave p = 7.6 \u00d7 10\u207b\u00b2\u00b2."
finding_id: "lanthanide_methylotrophy_atlas--6465f1d3"
result: "observation"
source: "lanthanide_methylotrophy_atlas"
quantities: [{"value": "18.92 : 1", "what": "global xoxF:mxaF ratio of genome annotations", "unit": "ratio", "denominator": "", "scope": "293,059 GTDB-r214 genomes, eggNOG K00114 vs K14028"}, {"value": "3,690", "what": "genomes annotated with xoxF/K00114", "unit": "genomes", "denominator": "293,059 GTDB-r214 genomes", "scope": ""}, {"value": "0.9498", "what": "xoxF fraction of joint MDH calls (xoxF + mxaF)", "unit": "fraction", "denominator": "xoxF + mxaF calls", "scope": "95% CI [0.9425, 0.9558]; tested against preregistered H1 threshold xoxF fraction > 10/11 \u2248 0.909"}, {"value": "7.6 \u00d7 10\u207b\u00b2\u00b2", "what": "one-sided binomial p value against the preregistered H1 threshold (xoxF fraction > 10/11 \u2248 0.909)", "unit": "", "denominator": "", "scope": ""}]
caveat: "The initial per-phylum binomial framework did not formally control phylogenetic non-independence; the report describes three subsequent validation strategies."
first_added: "2026-10-27"
source_hash: "4c006958be98f494be09edfff08176308c57490b4b48dc38c5753450c3d8e304"
---
# Lanthanide-dependent xoxF vastly outnumbers calcium-dependent mxaF across a large genome collection

In 293,059 GTDB-r214 genomes, eggNOG annotated xoxF/K00114 in 3,690 and mxaF/K14028 in 195 (ratio 18.92:1, Clopper–Pearson 95% CI [13.07, 27.69]; xoxF fraction 0.9498, 95% CI [0.9425, 0.9558]), and the preregistered one-sided binomial test against the H1 threshold of xoxF fraction > 10/11 ≈ 0.909 gave p = 7.6 × 10⁻²². [src: lanthanide_methylotrophy_atlas]

## Key figures

- **18.92 : 1 ratio**: global xoxF:mxaF ratio of genome annotations (scope 293,059 GTDB-r214 genomes, eggNOG K00114 vs K14028) [src: lanthanide_methylotrophy_atlas]
- **3,690 genomes**: genomes annotated with xoxF/K00114 (denominator 293,059 GTDB-r214 genomes) [src: lanthanide_methylotrophy_atlas]
- **0.9498 fraction**: xoxF fraction of joint MDH calls (xoxF + mxaF) (denominator xoxF + mxaF calls; scope 95% CI [0.9425, 0.9558]; tested against preregistered H1 threshold xoxF fraction > 10/11 ≈ 0.909) [src: lanthanide_methylotrophy_atlas]
- **7.6 × 10⁻²²**: one-sided binomial p value against the preregistered H1 threshold (xoxF fraction > 10/11 ≈ 0.909) [src: lanthanide_methylotrophy_atlas]

## Evidence

> Across 293,059 GTDB-r214 genomes, eggNOG `KEGG_ko = K00114` (xoxF, lanthanide-dependent methanol dehydrogenase, EC 1.1.2.8) is annotated in **3,690 genomes**, while `K14028` (mxaF, Ca-dependent methanol dehydrogenase, EC 1.1.2.7) is annotated in **195 genomes** — a global xoxF:mxaF ratio of **18.92 : 1**, with a Clopper-Pearson 95% CI of [13.07, 27.69]. The xoxF fraction of joint MDH calls (xoxF + mxaF) is **0.9498** [95% CI 0.9425, 0.9558]. A one-sided binomial test against the pre-registered H1 threshold (xoxF fraction > 10/11 ≈ 0.909) gives **p = 7.6 × 10⁻²²**. **H1 is strongly supported.** [src: lanthanide_methylotrophy_atlas]

From the report [[summaries/lanthanide_methylotrophy_atlas__REPORT]].

## Caveat

The initial per-phylum binomial framework did not formally control phylogenetic non-independence; the report describes three subsequent validation strategies. [src: lanthanide_methylotrophy_atlas]

> The reviewer (PLAN_REVIEW_1.md, REVIEW_1.md) noted that the per-phylum binomial framework does not formally control for phylogenetic non-independence. NB08 implements three orthogonal validation strategies, all of which support H1: [src: lanthanide_methylotrophy_atlas]

## Other caveats in this report

- Environmental associations used per-class Fisher exact tests for any xoxF against a generic-environmental reference, with Benjamini–Hochberg correction. [src: lanthanide_methylotrophy_atlas]
- The REE-impacted class had only 37 genomes; its 10.81% xoxF rate and odds ratio 3.51 were descriptive, with adjusted p value 0.082. [src: lanthanide_methylotrophy_atlas]
- The report grades H2 as partially supported: soil/sediment and marine enrichment and host-associated depletion passed its correction, while the n=37 REE-impacted elevation did not pass the false-discovery-rate threshold (p_BH = 0.082). [src: lanthanide_methylotrophy_atlas]
- Of 2,185 genomes with no eggNOG pqq, 1,288 (59%) had at least one bakta PQQ product. The other 897 (24% of all xoxF carriers) lacked evidence in both sources; assembly incompleteness, pseudogenization, and community-acquired PQQ remain unresolved without sequence-level inspection. [src: lanthanide_methylotrophy_atlas]
- The marker-calibration comparison is based on a 134,578-row hit-bearing genome matrix. [src: lanthanide_methylotrophy_atlas]
