---
type: "Finding"
description: "Across 161 classified organism-pathway pairs (7 Fitness Browser organisms, 23 GapMind pathways), only 35.4% (57/161) are Active Dependencies, while Latent Capability is the largest category at 41.0% (66/161), 14.9% (24/161) are Incomplete but Important (suggesting annotation gaps or salvage routes), and 8.7% (14/161) are Missing."
finding_id: "pathway_capability_dependency--250e9510"
result: "observation"
source: "pathway_capability_dependency"
quantities: [{"value": "35.4%", "what": "Active Dependencies, where a complete pathway contains fitness-important genes", "unit": "percent", "denominator": "57/161 organism-pathway pairs", "scope": "7 Fitness Browser organisms, 23 GapMind pathways"}, {"value": "41.0%", "what": "Latent Capability: genomically complete pathways with no significant fitness defects under standard conditions", "unit": "percent", "denominator": "66/161 organism-pathway pairs", "scope": "7 Fitness Browser organisms, 23 GapMind pathways"}, {"value": "14.9%", "what": "Incomplete but Important pathways", "unit": "percent", "denominator": "24/161 organism-pathway pairs", "scope": "7 Fitness Browser organisms, 23 GapMind pathways"}, {"value": "8.7%", "what": "Missing pathways (neither complete nor important)", "unit": "percent", "denominator": "14/161 organism-pathway pairs", "scope": "7 Fitness Browser organisms, 23 GapMind pathways"}]
caveat: "Only 7 of the 48 Fitness Browser organisms have matching GapMind genome data, and 23 GapMind pathways had sufficient annotation, limiting classification to 161 organism-pathway pairs."
first_added: "2026-10-27"
source_hash: "b48f1bebed72779629baaf7e71b9cffda8ab0298f49aa9c3460cc6d13bb7cf75"
---
# Latent capability outnumbers active dependency among model-bacteria pathways

Across 161 classified organism-pathway pairs (7 Fitness Browser organisms, 23 GapMind pathways), only 35.4% (57/161) are Active Dependencies, while Latent Capability is the largest category at 41.0% (66/161), 14.9% (24/161) are Incomplete but Important (suggesting annotation gaps or salvage routes), and 8.7% (14/161) are Missing. [src: pathway_capability_dependency]

## Key figures

- **35.4%**: Active Dependencies, where a complete pathway contains fitness-important genes (denominator 57/161 organism-pathway pairs; scope 7 Fitness Browser organisms, 23 GapMind pathways) [src: pathway_capability_dependency]
- **41.0%**: Latent Capability: genomically complete pathways with no significant fitness defects under standard conditions (denominator 66/161 organism-pathway pairs; scope 7 Fitness Browser organisms, 23 GapMind pathways) [src: pathway_capability_dependency]
- **14.9%**: Incomplete but Important pathways (denominator 24/161 organism-pathway pairs; scope 7 Fitness Browser organisms, 23 GapMind pathways) [src: pathway_capability_dependency]
- **8.7%**: Missing pathways (neither complete nor important) (denominator 14/161 organism-pathway pairs; scope 7 Fitness Browser organisms, 23 GapMind pathways) [src: pathway_capability_dependency]

## Evidence

> Of 161 classified organism-pathway pairs (7 Fitness Browser organisms, 23 GapMind pathways), only 35.4% (57/161) are Active Dependencies where a complete pathway contains fitness-important genes. The largest single category is Latent Capability at 41.0% (66/161): pathways that are genomically complete but whose constituent genes show no significant fitness defects under standard conditions. An additional 14.9% (24/161) are Incomplete but Important -- pathways that GapMind scores as incomplete yet whose mapped genes are fitness-important, suggesting annotation gaps or salvage routes. Only 8.7% (14/161) are Missing (neither complete nor important). [src: pathway_capability_dependency]

From the report [[summaries/pathway_capability_dependency__REPORT]].

## Caveat

Only 7 of the 48 Fitness Browser organisms have matching GapMind genome data, and 23 GapMind pathways had sufficient annotation, limiting classification to 161 organism-pathway pairs. [src: pathway_capability_dependency]

> Of the 48 organisms in the Fitness Browser, only these 7 have matching GapMind genome data. Across these organisms, 23 GapMind pathways had sufficient gene-level annotation to classify, yielding 161 organism-pathway pairs. [src: pathway_capability_dependency]

## Other caveats in this report

- The report cites a separate finding of 28,017 Fitness Browser genes costly in lab but conserved in nature, underscoring lab-versus-nature limitations. [src: pathway_capability_dependency]
- The report proposes the hypothesis that environmental-condition breadth, rather than mean fitness under one condition, may constrain pathway gene loss. [src: pathway_capability_dependency]
- The core-completeness comparison is compressed by 7 well-studied model organisms; this passage names all 7. [src: pathway_capability_dependency]
- The pathway-openness signal was positive in 13 of 18 genera and significant in 5 of 18; small genus-level samples limit power. [src: pathway_capability_dependency]
- Carbon-utilization pathways showed smaller core-versus-all completeness gaps; the proposed mechanism is explicitly speculative. [src: pathway_capability_dependency]
