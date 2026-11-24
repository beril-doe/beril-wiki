---
type: "Finding"
description: "Latent Capability, pathways genomically complete but with no significant fitness defects under standard conditions, is the largest category at 41.0% (66/161) of classified organism-pathway pairs."
finding_id: "pathway_capability_dependency--256374bc"
result: "null result"
source: "pathway_capability_dependency"
quantities: [{"value": "41.0%", "what": "share of pairs that are Latent Capability", "unit": "", "denominator": "161 classified organism-pathway pairs", "scope": ""}]
caveat: "Only 7 of 48 FB organisms have GapMind data, limiting Tier 1 to a small set of model organisms with near-complete core genomes that compress the conservation validation signal."
first_added: "2026-11-24"
source_hash: "b48f1bebed72779629baaf7e71b9cffda8ab0298f49aa9c3460cc6d13bb7cf75"
---
# Many complete pathways show no fitness defect under standard conditions

Latent Capability, pathways genomically complete but with no significant fitness defects under standard conditions, is the largest category at 41.0% (66/161) of classified organism-pathway pairs. [src: pathway_capability_dependency]

## Key figures

- **41.0%**: share of pairs that are Latent Capability (denominator 161 classified organism-pathway pairs) [src: pathway_capability_dependency]

## Evidence

> The largest single category is Latent Capability at 41.0% (66/161): pathways that are genomically complete but whose constituent genes show no significant fitness defects under standard conditions. [src: pathway_capability_dependency]

From the report [[summaries/pathway_capability_dependency__REPORT]].

## Caveat

Only 7 of 48 FB organisms have GapMind data, limiting Tier 1 to a small set of model organisms with near-complete core genomes that compress the conservation validation signal. [src: pathway_capability_dependency]

> Only 7 of 48 FB organisms have GapMind data, limiting Tier 1 to a small set of model organisms. These organisms have near-complete core genomes, which compresses the conservation validation signal. [src: pathway_capability_dependency]

## Other caveats in this report

- The report attributes the small conservation gap between pathway categories to its 7 Fitness Browser model organisms having near-complete, well-annotated core genomes. [src: pathway_capability_dependency]
- Genome count is a critical confounder because species with more sequenced genomes may appear to have more variable pathways solely from sampling depth. [src: pathway_capability_dependency]
- Smaller within-genus sample sizes limit statistical power for many groups in the pathway-variation analysis. [src: pathway_capability_dependency]
- Only 7 of the 48 Fitness Browser organisms have matching GapMind genome data. [src: pathway_capability_dependency]
- Full phylum-level stratification would require joining the KBase Data Lakehouse GTDB taxonomy table; the report instead uses genus-level grouping from GTDB species clade names as a conservative phylogenetic control. [src: pathway_capability_dependency]
