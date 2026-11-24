---
type: "Finding"
description: "Across 293,059 GTDB-r214 genomes, eggNOG KEGG_ko K00114 (xoxF) is annotated in 3,690 genomes and K14028 (mxaF) in 195 genomes, a global xoxF:mxaF ratio of 18.92 : 1 with a Clopper-Pearson 95% CI of [13.07, 27.69]."
finding_id: "lanthanide_methylotrophy_atlas--e22bc5ab"
result: "observation"
source: "lanthanide_methylotrophy_atlas"
quantities: [{"value": "18.92 : 1", "what": "global xoxF:mxaF ratio", "unit": "", "denominator": "", "scope": "293,059 GTDB-r214 genomes"}, {"value": "3,690", "what": "genomes annotated with xoxF (K00114)", "unit": "genomes", "denominator": "", "scope": ""}, {"value": "195", "what": "genomes annotated with mxaF (K14028)", "unit": "genomes", "denominator": "", "scope": ""}, {"value": "[13.07, 27.69]", "what": "Clopper-Pearson 95% CI of the ratio", "unit": "", "denominator": "", "scope": ""}]
caveat: "The reviewer noted that the per-phylum binomial framework does not formally control for phylogenetic non-independence."
first_added: "2026-11-24"
source_hash: "4c006958be98f494be09edfff08176308c57490b4b48dc38c5753450c3d8e304"
---
# xoxF outnumbers mxaF roughly nineteen to one across the pangenome

Across 293,059 GTDB-r214 genomes, eggNOG KEGG_ko K00114 (xoxF) is annotated in 3,690 genomes and K14028 (mxaF) in 195 genomes, a global xoxF:mxaF ratio of 18.92 : 1 with a Clopper-Pearson 95% CI of [13.07, 27.69]. [src: lanthanide_methylotrophy_atlas]

## Key figures

- **18.92 : 1**: global xoxF:mxaF ratio (scope 293,059 GTDB-r214 genomes) [src: lanthanide_methylotrophy_atlas]
- **3,690 genomes**: genomes annotated with xoxF (K00114) [src: lanthanide_methylotrophy_atlas]
- **195 genomes**: genomes annotated with mxaF (K14028) [src: lanthanide_methylotrophy_atlas]
- **[13.07, 27.69]**: Clopper-Pearson 95% CI of the ratio [src: lanthanide_methylotrophy_atlas]

## Evidence

> Across 293,059 GTDB-r214 genomes, eggNOG `KEGG_ko = K00114` (xoxF, lanthanide-dependent methanol dehydrogenase, EC 1.1.2.8) is annotated in **3,690 genomes**, while `K14028` (mxaF, Ca-dependent methanol dehydrogenase, EC 1.1.2.7) is annotated in **195 genomes** — a global xoxF:mxaF ratio of **18.92 : 1**, with a Clopper-Pearson 95% CI of [13.07, 27.69]. [src: lanthanide_methylotrophy_atlas]

From the report [[summaries/lanthanide_methylotrophy_atlas__REPORT]].

## Caveat

The reviewer noted that the per-phylum binomial framework does not formally control for phylogenetic non-independence. [src: lanthanide_methylotrophy_atlas]

> The reviewer (PLAN_REVIEW_1.md, REVIEW_1.md) noted that the per-phylum binomial framework does not formally control for phylogenetic non-independence. [src: lanthanide_methylotrophy_atlas]

## Other caveats in this report

- The report suggests that the 13/62 lanmodulin-without-xoxF genomes may reflect annotation incompleteness or genuine alternative lanthanide-handling pathways, since lanmodulin can bind REEs without co-location with a lanthanide-MDH operon. [src: lanthanide_methylotrophy_atlas]
- The report says REE-impacted samples show a 3.5-fold descriptive xoxF elevation (10.8 % vs 3.7 % baseline), but n=37 is too small to clear the FDR threshold (p_BH = 0.082). [src: lanthanide_methylotrophy_atlas]
- The 897 genomes (24 % of all xoxF carriers) lacking PQQ evidence from either source are candidates for assembly incompleteness, pseudogenization or community-acquired PQQ dependence, not established cases of any one explanation. [src: lanthanide_methylotrophy_atlas]
- Discriminating assembly incompleteness, pseudogenization and community-acquired PQQ dependence requires sequence-level inspection outside the report's scope. [src: lanthanide_methylotrophy_atlas]
- REE-AMD enrichment is descriptive-only at n=37, OR=3.51, p_BH=0.082, and a larger explicitly REE-impacted metagenome collection would test whether REE supply per se selects for the cassette. [src: lanthanide_methylotrophy_atlas]
