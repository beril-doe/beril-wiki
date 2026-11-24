---
type: "Finding"
description: "After controlling for genome count, the partial Spearman correlation between variable pathways and pangenome openness strengthens to rho=0.530 (p=2.83e-203)."
finding_id: "pathway_capability_dependency--342cfb41"
result: "observation"
source: "pathway_capability_dependency"
quantities: [{"value": "rho=0.530", "what": "partial Spearman correlation of pathway variability with pangenome openness", "unit": "", "denominator": "", "scope": "controlling for genome count"}]
caveat: "Species with more sequenced genomes are more likely to show pathway variation and more ecotypes, and partial correlations controlling for genome count mitigate but do not fully eliminate this bias."
first_added: "2026-11-24"
source_hash: "b48f1bebed72779629baaf7e71b9cffda8ab0298f49aa9c3460cc6d13bb7cf75"
---
# Pathway variability strongly predicts pangenome openness across bacterial species

After controlling for genome count, the partial Spearman correlation between variable pathways and pangenome openness strengthens to rho=0.530 (p=2.83e-203). [src: pathway_capability_dependency]

## Key figures

- **rho=0.530**: partial Spearman correlation of pathway variability with pangenome openness (scope controlling for genome count) [src: pathway_capability_dependency]

## Evidence

> After controlling for genome count -- a critical confounder since species with more sequenced genomes may appear to have more variable pathways simply from sampling depth -- the partial Spearman correlation strengthens to rho=0.530 (p=2.83e-203). [src: pathway_capability_dependency]

From the report [[summaries/pathway_capability_dependency__REPORT]].

## Caveat

Species with more sequenced genomes are more likely to show pathway variation and more ecotypes, and partial correlations controlling for genome count mitigate but do not fully eliminate this bias. [src: pathway_capability_dependency]

> Species with more sequenced genomes are more likely to show pathway variation and more ecotypes. Partial correlations controlling for genome count mitigate but do not fully eliminate this bias. [src: pathway_capability_dependency]

## Other caveats in this report

- The report attributes the small conservation gap between pathway categories to its 7 Fitness Browser model organisms having near-complete, well-annotated core genomes. [src: pathway_capability_dependency]
- Genome count is a critical confounder because species with more sequenced genomes may appear to have more variable pathways solely from sampling depth. [src: pathway_capability_dependency]
- Smaller within-genus sample sizes limit statistical power for many groups in the pathway-variation analysis. [src: pathway_capability_dependency]
- Only 7 of the 48 Fitness Browser organisms have matching GapMind genome data. [src: pathway_capability_dependency]
- Full phylum-level stratification would require joining the KBase Data Lakehouse GTDB taxonomy table; the report instead uses genus-level grouping from GTDB species clade names as a conservative phylogenetic control. [src: pathway_capability_dependency]
