---
type: "Finding"
description: "Comparing AlphaEarth 64-dimensional environmental embeddings between SNIPE-bearing (n=1,069) and non-SNIPE species (n=13,977), 22 of 64 dimensions were significantly different (Bonferroni-corrected p < 0.05)."
finding_id: "snipe_defense_system--b2833f06"
result: "observation"
source: "snipe_defense_system"
quantities: [{"value": "22 of 64", "what": "AlphaEarth dimensions significantly different", "unit": "dimensions", "denominator": "64 dimensions", "scope": "Bonferroni-corrected p < 0.05"}, {"value": "n=1,069", "what": "SNIPE-bearing species compared", "unit": "species", "denominator": "", "scope": "versus non-SNIPE species"}, {"value": "n=13,977", "what": "non-SNIPE species compared", "unit": "species", "denominator": "", "scope": ""}]
caveat: "AlphaEarth coverage is 28.4% of genomes and is biased toward environmental isolates with lat/lon data."
first_added: "2026-11-09"
source_hash: "f7d78af3b2d5fc355bdd55bc72ce728519a3dc854968793d401b959f1e9ae555"
---
# SNIPE-bearing species differ from others in environmental embeddings

Comparing AlphaEarth 64-dimensional environmental embeddings between SNIPE-bearing (n=1,069) and non-SNIPE species (n=13,977), 22 of 64 dimensions were significantly different (Bonferroni-corrected p < 0.05). [src: snipe_defense_system]

## Key figures

- **22 of 64 dimensions**: AlphaEarth dimensions significantly different (denominator 64 dimensions; scope Bonferroni-corrected p < 0.05) [src: snipe_defense_system]
- **n=1,069 species**: SNIPE-bearing species compared (scope versus non-SNIPE species) [src: snipe_defense_system]
- **n=13,977 species**: non-SNIPE species compared [src: snipe_defense_system]

## Evidence

> Comparison of AlphaEarth 64-dimensional environmental embeddings between SNIPE-bearing (n=1,069) and non-SNIPE species (n=13,977): - **22 of 64 dimensions** are significantly different (Bonferroni-corrected p < 0.05) [src: snipe_defense_system]

From the report [[summaries/snipe_defense_system__REPORT]].

## Caveat

AlphaEarth coverage is 28.4% of genomes and is biased toward environmental isolates with lat/lon data. [src: snipe_defense_system]

> **Caveat**: AlphaEarth coverage is 28.4% of genomes, biased toward environmental isolates with lat/lon data. [src: snipe_defense_system]

## Other caveats in this report

- UniProt's fructose-specific ManX annotation conflicts with the reported Fitness Browser phenotypes. [src: snipe_defense_system]
- Fitness scores are log2 RB-TnSeq ratios; carbon-source conditions were selected by condition_1 and expGroup='carbon source'. [src: snipe_defense_system]
- The report proposes that SNIPE avoids the metabolic cost of man knockouts while blocking phage DNA; this passage does not present a direct comparative fitness measurement. [src: snipe_defense_system]
- Three Klebsiella DUF4041 proteins are 558 aa, matching E. coli SNIPE; their full two-domain architecture is inferred rather than directly confirmed here. [src: snipe_defense_system]
- The query footnote labels PF00358 as PTS_EIIC and PF02378 as PTS_EIID, conflicting with the report's table labels PF00358/PTS_EIIA_1 and PF02378/PTS_EIIC. [src: snipe_defense_system]
