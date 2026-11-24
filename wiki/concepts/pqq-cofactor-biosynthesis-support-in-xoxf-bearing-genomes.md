---
type: "Concept"
description: "Whether xoxF-carrying genomes carry PQQ biosynthesis genes, annotation gaps versus true absence; stops at marker calibration."
sources: ["summaries/lanthanide_methylotrophy_atlas__REPORT.md"]
---
# PQQ cofactor biosynthesis support in xoxF-bearing genomes

Many xoxF-bearing genomes lack pyrroloquinoline quinone (PQQ) biosynthesis annotations, even though PQQ is described as an obligate XoxF cofactor. [src: lanthanide_methylotrophy_atlas] In the lanthanide methylotrophy atlas, most of this gap comes from annotation, not true absence: 59 % of xoxF-without-PQQ cases are eggNOG annotation gaps that bakta detects. [src: lanthanide_methylotrophy_atlas] About 24 % of xoxF carriers still show no PQQ evidence from either source, and the report treats them as unresolved candidates, not established absences. [src: lanthanide_methylotrophy_atlas] The evidence comes from one report and rests on gene-call annotations only. See also [[summaries/lanthanide_methylotrophy_atlas__REPORT]], [[entities/pyrroloquinoline-quinone-biosynthesis]] and [[concepts/annotation-source-disagreement-and-coverage]].

## The gap and how it was cross-checked

The pilot exploration found 2,320 xoxF-bearing genomes with no eggNOG PQQ-biosynthesis annotation. [src: lanthanide_methylotrophy_atlas] The report's NB07 cross-checks these genomes against PQQ matches in the bakta `product` field. [src: lanthanide_methylotrophy_atlas]

## Support categories among xoxF genomes

Complete eggNOG pqqA-E is rare, and bakta adds a large block of support that eggNOG misses. [src: lanthanide_methylotrophy_atlas] Values are counts of xoxF genomes and their share of the xoxF set.

| Category | Genomes | Share |
|---|---|---|
| Complete eggNOG pqqA-E | 33 [src: lanthanide_methylotrophy_atlas] | 0.9 % [src: lanthanide_methylotrophy_atlas] |
| Partial eggNOG pqq (1–4 of A-E) | 1,472 [src: lanthanide_methylotrophy_atlas] | 39.9 % [src: lanthanide_methylotrophy_atlas] |
| Bakta-only strong (≥3 PQQ products) | 899 [src: lanthanide_methylotrophy_atlas] | 24.4 % [src: lanthanide_methylotrophy_atlas] |
| Bakta-only partial (1–2 PQQ products) | 389 [src: lanthanide_methylotrophy_atlas] | 10.5 % [src: lanthanide_methylotrophy_atlas] |
| No PQQ detected by either source | 897 [src: lanthanide_methylotrophy_atlas] | 24.3 % [src: lanthanide_methylotrophy_atlas] |

Of the 2,185 genomes with no eggNOG pqq, 1,288 (59 %) have at least one bakta PQQ product. The report identifies these as pure annotation gaps. [src: lanthanide_methylotrophy_atlas]

## Marker calibration between sources

Bakta is not simply the better source. In the hit-bearing genome matrix, bakta-only calls for pqqA-E number 50–90K, and the report says bakta over-calls and uses eggNOG as primary. [src: lanthanide_methylotrophy_atlas] For future PQQ work in the KBase Data Lakehouse pangenome, it recommends the union of eggNOG and bakta sources. [src: lanthanide_methylotrophy_atlas] See also [[concepts/annotation-based-gene-detection-limits-in-pangenome-trait-surveys]].

## Limits on the unresolved 24 %

The 897 genomes with no PQQ evidence from either source are candidates for assembly incompleteness, pseudogenization or reliance on community-acquired PQQ. None of these explanations is established. [src: lanthanide_methylotrophy_atlas] The report assessed xoxF and PQQ presence at the gene-call level and did not screen for pseudogenes, truncated ORFs or assembly fragmentation. [src: lanthanide_methylotrophy_atlas] Telling the three explanations apart needs sequence-level inspection, which was outside the report's scope. [src: lanthanide_methylotrophy_atlas] The report proposes sequence-level genome-quality filtering for this purpose. [src: lanthanide_methylotrophy_atlas] It also proposes per-genome ORF integrity and CheckM2 completeness scoring of the ~897 genomes. [src: lanthanide_methylotrophy_atlas]

## Open Directions

- Score the 897 no-PQQ xoxF genomes for ORF integrity and CheckM2 completeness, to separate assembly fragmentation, pseudogenization and community-PQQ acquisition.
- Apply sequence-level genome-quality filtering to the remaining ~24 % of xoxF carriers.
- Check bakta-only PQQ calls against sequence evidence, such as gene synteny and homology, to see how much bakta over-calling affects the 899 bakta-only strong genomes.
- Re-run the xoxF–PQQ co-occurrence survey with the eggNOG and bakta union.
