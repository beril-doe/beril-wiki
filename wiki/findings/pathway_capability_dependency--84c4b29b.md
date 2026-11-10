---
type: "Finding"
description: "Across 2,810 species with at least 10 genomes, the number of variable pathways (present in 10-90% of genomes) correlates with pangenome openness, with raw Spearman rho=0.327 (p=7.2e-71) strengthening to partial rho=0.530 (p=2.83e-203) after controlling for genome count."
finding_id: "pathway_capability_dependency--84c4b29b"
result: "observation"
source: "pathway_capability_dependency"
quantities: [{"value": "0.327", "what": "raw Spearman correlation between variable pathways and pangenome openness", "unit": "rho", "denominator": "", "scope": "2,810 species with at least 10 genomes; p=7.2e-71"}, {"value": "0.530", "what": "partial Spearman correlation after controlling for genome count", "unit": "rho", "denominator": "", "scope": "2,810 species with at least 10 genomes; p=2.83e-203"}, {"value": "2,810", "what": "species with at least 10 genomes analysed", "unit": "species", "denominator": "", "scope": "GTDB species"}]
caveat: "Correlations were controlled for genome count and checked within taxonomic groups, but full phylogenetic independent contrasts were not computed, and the ecotype_analysis project found phylogeny dominates gene content in 60.5% of species."
first_added: "2026-10-27"
source_hash: "b48f1bebed72779629baaf7e71b9cffda8ab0298f49aa9c3460cc6d13bb7cf75"
---
# Pathway variability tracks pangenome openness, strengthening after genome-count control

Across 2,810 species with at least 10 genomes, the number of variable pathways (present in 10-90% of genomes) correlates with pangenome openness, with raw Spearman rho=0.327 (p=7.2e-71) strengthening to partial rho=0.530 (p=2.83e-203) after controlling for genome count. [src: pathway_capability_dependency]

## Key figures

- **0.327 rho**: raw Spearman correlation between variable pathways and pangenome openness (scope 2,810 species with at least 10 genomes; p=7.2e-71) [src: pathway_capability_dependency]
- **0.530 rho**: partial Spearman correlation after controlling for genome count (scope 2,810 species with at least 10 genomes; p=2.83e-203) [src: pathway_capability_dependency]
- **2,810 species**: species with at least 10 genomes analysed (scope GTDB species) [src: pathway_capability_dependency]

## Evidence

> Across 2,810 species with at least 10 genomes, the number of variable pathways (present in 10-90% of genomes) correlates with pangenome openness (fraction of accessory gene clusters). The raw Spearman correlation is rho=0.327 (p=7.2e-71). After controlling for genome count -- a critical confounder since species with more sequenced genomes may appear to have more variable pathways simply from sampling depth -- the partial Spearman correlation strengthens to rho=0.530 (p=2.83e-203). [src: pathway_capability_dependency]

From the report [[summaries/pathway_capability_dependency__REPORT]].

## Caveat

Correlations were controlled for genome count and checked within taxonomic groups, but full phylogenetic independent contrasts were not computed, and the ecotype_analysis project found phylogeny dominates gene content in 60.5% of species. [src: pathway_capability_dependency]

> While correlations were controlled for genome count and checked within taxonomic groups, full phylogenetic independent contrasts were not computed. The ecotype_analysis project found that phylogeny dominates gene content in 60.5% of species, and metabolic ecotypes may partially reflect intra-species phylogenetic structure. [src: pathway_capability_dependency]

## Other caveats in this report

- The report cites a separate finding of 28,017 Fitness Browser genes costly in lab but conserved in nature, underscoring lab-versus-nature limitations. [src: pathway_capability_dependency]
- The report proposes the hypothesis that environmental-condition breadth, rather than mean fitness under one condition, may constrain pathway gene loss. [src: pathway_capability_dependency]
- The core-completeness comparison is compressed by 7 well-studied model organisms; this passage names all 7. [src: pathway_capability_dependency]
- The pathway-openness signal was positive in 13 of 18 genera and significant in 5 of 18; small genus-level samples limit power. [src: pathway_capability_dependency]
- Only 7 of 48 Fitness Browser organisms matched GapMind genome data, and 23 pathways had sufficient annotation, limiting classification to 161 pairs. [src: pathway_capability_dependency]
