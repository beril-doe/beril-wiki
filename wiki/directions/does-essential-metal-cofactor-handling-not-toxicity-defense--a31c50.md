---
type: "Research direction"
description: "Removing genes also important under salt stress left core-genome enrichment of metal-important genes intact, and strengthened it for essential metals; cadmium and iron, each in one organism, moved the other way. Do essential-metal use and acquisition genes carry the enrichment, while toxic-metal defense genes are as variable as other accessory genes?"
hypothesis: "Metal-important genes involved in uptake, cofactor biosynthesis or metal-dependent enzymes are strongly core, while detoxification and efflux genes for metals with no biological role are much less core, so the pooled enrichment is a mixture of the two."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Fitness data and core status already exist, but gene function labels must be assigned and the cadmium and iron results rest on one organism each."
collections: ["kescience-fitnessbrowser", "kbase-ke-pangenome"]
findings: ["counter_ion_effects--e835d451"]
conflicts: ["conflict--laboratory-fitness-versus-natural-selection--a172813c"]
papers: ["34432491", "34765088", "12829273", "40302248", "29769716"]
builds_on: ["findings/counter_ion_effects--e835d451", "conflicts/conflict--laboratory-fitness-versus-natural-selection--a172813c"]
projects: ["counter_ion_effects", "field_vs_lab_fitness"]
topics: ["laboratory-fitness-versus-natural-selection-and-gene-conservation"]
---
# Does essential-metal cofactor handling, not toxicity defense, drive core enrichment of metal-fitness genes?

Removing genes also important under salt stress left core-genome enrichment of metal-important genes intact, and strengthened it for essential metals; cadmium and iron, each in one organism, moved the other way. Do essential-metal use and acquisition genes carry the enrichment, while toxic-metal defense genes are as variable as other accessory genes?

## Hypothesis

Metal-important genes involved in uptake, cofactor biosynthesis or metal-dependent enzymes are strongly core, while detoxification and efflux genes for metals with no biological role are much less core, so the pooled enrichment is a mixture of the two.

## Why it matters

It would explain why different analyses disagree about whether metal genes are core or accessory, and show that conservation of metal fitness genes reflects ordinary physiology rather than adaptation to contaminated sites.

## How to test it

In Fitness Browser organisms with metal experiments, label each metal-important gene by annotation as uptake or cofactor use versus detoxification or efflux. Compare core fractions from the Pangenome Collection for each label, for essential metals (molybdenum, tungsten, selenium, nickel) versus toxic-only metals (mercury, cadmium, uranium), after removing genes also important under salt stress. Repeat with organisms contributing more than one metal to see whether the split holds within a genome.

## What would support or refute it

Support: uptake and cofactor genes are clearly more core than detoxification genes, and the difference between metal classes shrinks after the split. Refute: both gene types are similarly core, or toxic-only metals are as core-enriched as essential metals.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Fitness data and core status already exist, but gene function labels must be assigned and the cadmium and iron results rest on one organism each.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/counter_ion_effects--e835d451|Core-genome enrichment not weakened by removing shared-stress genes]] (Candidate novel)
- Conflict: [[conflicts/conflict--laboratory-fitness-versus-natural-selection--a172813c|Are Metal-Important Genes Core or Accessory?]]

## Closest published work

- [PMID 34432491](https://pubmed.ncbi.nlm.nih.gov/34432491/) Deciphering Microbial Metal Toxicity Responses via Random Bar Code Transposon Site Sequencing and Activity-Based Metabolomics.
- [PMID 34765088](https://pubmed.ncbi.nlm.nih.gov/34765088/) Cadmium stress triggers significant metabolic reprogramming in Enterococcus faecium CX 2-6.
- [PMID 12829273](https://pubmed.ncbi.nlm.nih.gov/12829273/) Efflux-mediated heavy metal resistance in prokaryotes.
- [PMID 40302248](https://pubmed.ncbi.nlm.nih.gov/40302248/) High-Throughput Tn-Seq Screens Identify Both Known and Novel Pseudomonas putida KT2440 Genes Involved in Metal Tolerance.
- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.

PMID 34765088 reports that most cadmium-responsive genes in one Enterococcus faecium strain are core, and PMID 34432491 and PMID 40302248 map metal-tolerance genes, but none separates essential-metal handling from toxicity defense when asking about conservation.
