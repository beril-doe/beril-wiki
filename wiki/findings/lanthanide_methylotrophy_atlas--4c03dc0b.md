---
type: "Finding"
description: "Only 4/37 REE-acid-mine-drainage MAGs carried xoxF and 0/37 carried bakta-validated lanmodulin or xoxJ, and the functional signature instead read as an acid-mine-drainage stress profile."
finding_id: "lanthanide_methylotrophy_atlas--4c03dc0b"
result: "null result"
source: "lanthanide_methylotrophy_atlas"
quantities: [{"value": "4/37", "what": "REE-AMD MAGs carrying any xoxF", "unit": "MAGs", "denominator": "37 MAGs", "scope": ""}, {"value": "0/37", "what": "MAGs carrying bakta-validated lanmodulin or xoxJ", "unit": "MAGs", "denominator": "37 MAGs", "scope": ""}]
caveat: "The REE-AMD anchor is small (n=37) and from a single bioproject, so it is descriptive only and does not support inference about REE-impacted environments."
first_added: "2026-10-27"
source_hash: "4c006958be98f494be09edfff08176308c57490b4b48dc38c5753450c3d8e304"
---
# REE-acid-mine-drainage MAGs show little xoxF and no lanmodulin

Only 4/37 REE-acid-mine-drainage MAGs carried xoxF and 0/37 carried bakta-validated lanmodulin or xoxJ, and the functional signature instead read as an acid-mine-drainage stress profile. [src: lanthanide_methylotrophy_atlas]

## Key figures

- **4/37 MAGs**: REE-AMD MAGs carrying any xoxF (denominator 37 MAGs) [src: lanthanide_methylotrophy_atlas]
- **0/37 MAGs**: MAGs carrying bakta-validated lanmodulin or xoxJ (denominator 37 MAGs) [src: lanthanide_methylotrophy_atlas]

## Evidence

> Only **4/37** REE-AMD MAGs carry any xoxF; **0/37** carry bakta-validated lanmodulin or xoxJ. The functional signature instead reads as a textbook acid-mine-drainage stress profile: high prevalence of DNA-repair enzymes (RecN 33, RadA 32, RecO 31, RecA 28, RadC 24), acid-resistance machinery (FtsH zinc metalloprotease 31, proton-translocating NAD(P)+ transhydrogenase 27), MerR-family heavy-metal-responsive transcriptional regulators (30), and oxidative-stress defense (thioredoxin reductase 25, glutathione peroxidase 24). Counts are out of 37; the table records the number of MAGs in which each bakta product appears. [src: lanthanide_methylotrophy_atlas]

From the report [[summaries/lanthanide_methylotrophy_atlas__REPORT]].

## Caveat

The REE-AMD anchor is small (n=37) and from a single bioproject, so it is descriptive only and does not support inference about REE-impacted environments. [src: lanthanide_methylotrophy_atlas]

> **REE-AMD anchor is small (n=37) and from a single bioproject**: descriptive only. Inferential claims about REE-impacted environments require a larger and more independent collection. [src: lanthanide_methylotrophy_atlas]

## Other caveats in this report

- The initial per-phylum binomial framework did not formally control phylogenetic non-independence; the report describes three subsequent validation strategies. [src: lanthanide_methylotrophy_atlas]
- Environmental associations used per-class Fisher exact tests for any xoxF against a generic-environmental reference, with Benjamini–Hochberg correction. [src: lanthanide_methylotrophy_atlas]
- The REE-impacted class had only 37 genomes; its 10.81% xoxF rate and odds ratio 3.51 were descriptive, with adjusted p value 0.082. [src: lanthanide_methylotrophy_atlas]
- The report grades H2 as partially supported: soil/sediment and marine enrichment and host-associated depletion passed its correction, while the n=37 REE-impacted elevation did not pass the false-discovery-rate threshold (p_BH = 0.082). [src: lanthanide_methylotrophy_atlas]
- Of 2,185 genomes with no eggNOG pqq, 1,288 (59%) had at least one bakta PQQ product. The other 897 (24% of all xoxF carriers) lacked evidence in both sources; assembly incompleteness, pseudogenization, and community-acquired PQQ remain unresolved without sequence-level inspection. [src: lanthanide_methylotrophy_atlas]
