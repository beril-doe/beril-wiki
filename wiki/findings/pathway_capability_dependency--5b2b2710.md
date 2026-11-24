---
type: "Finding"
description: "After controlling for genome count, the partial correlation between metabolic ecotype count and pangenome openness remains significant: rho=0.322 (p=8.0e-07)."
finding_id: "pathway_capability_dependency--5b2b2710"
result: "observation"
source: "pathway_capability_dependency"
quantities: [{"value": "rho=0.322", "what": "partial correlation of ecotype count with pangenome openness", "unit": "", "denominator": "", "scope": "controlling for genome count"}]
caveat: "The ecotype_analysis project found that phylogeny dominates gene content in 60.5% of species, and metabolic ecotypes may partially reflect intra-species phylogenetic structure."
first_added: "2026-11-24"
source_hash: "b48f1bebed72779629baaf7e71b9cffda8ab0298f49aa9c3460cc6d13bb7cf75"
---
# Metabolic ecotype count tracks pangenome openness beyond genome sampling

After controlling for genome count, the partial correlation between metabolic ecotype count and pangenome openness remains significant: rho=0.322 (p=8.0e-07). [src: pathway_capability_dependency]

## Key figures

- **rho=0.322**: partial correlation of ecotype count with pangenome openness (scope controlling for genome count) [src: pathway_capability_dependency]

## Evidence

> After controlling for genome count (to account for the sampling bias where more-sequenced species may yield more clusters), the partial correlation remains significant: rho=0.322 (p=8.0e-07). [src: pathway_capability_dependency]

From the report [[summaries/pathway_capability_dependency__REPORT]].

## Caveat

The ecotype_analysis project found that phylogeny dominates gene content in 60.5% of species, and metabolic ecotypes may partially reflect intra-species phylogenetic structure. [src: pathway_capability_dependency]

> The ecotype_analysis project found that phylogeny dominates gene content in 60.5% of species, and metabolic ecotypes may partially reflect intra-species phylogenetic structure. [src: pathway_capability_dependency]

## Other caveats in this report

- The report attributes the small conservation gap between pathway categories to its 7 Fitness Browser model organisms having near-complete, well-annotated core genomes. [src: pathway_capability_dependency]
- Genome count is a critical confounder because species with more sequenced genomes may appear to have more variable pathways solely from sampling depth. [src: pathway_capability_dependency]
- Smaller within-genus sample sizes limit statistical power for many groups in the pathway-variation analysis. [src: pathway_capability_dependency]
- Only 7 of the 48 Fitness Browser organisms have matching GapMind genome data. [src: pathway_capability_dependency]
- Full phylum-level stratification would require joining the KBase Data Lakehouse GTDB taxonomy table; the report instead uses genus-level grouping from GTDB species clade names as a conservative phylogenetic control. [src: pathway_capability_dependency]
