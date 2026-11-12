---
type: "Research direction"
description: "Genomes with glycosyltransferase family 2 (GT2) genes near type IV secretion (T4SS, conjugation) machinery carry far more metal-resistance types than other genomes. Is GT2 a marker of a distinct kind of conjugative element that carries metal cargo, or is the metal signal a property of T4SS-bearing genomes in general, with GT2 a bystander?"
hypothesis: "Genomes with T4SS but no nearby GT2 carry metal resistance no more often than the genome background, and only GT2-adjacent T4SS neighbourhoods are enriched for metal cargo."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Annotations and genomes are in the lakehouse, but neighbourhood grouping at several cut-offs and the matched comparison have not been run."
collections: ["kbase-ke-pangenome", "kbase-genomes", "nmdc-ncbi-biosamples"]
findings: ["t4ss_cazy_environmental_hgt--44ad24db", "t4ss_cazy_environmental_hgt--5d73bfde", "t4ss_cazy_environmental_hgt--a2b33180", "t4ss_cazy_environmental_hgt--91e33b0b"]
conflicts: ["conflict--horizontal-gene-transfer-driven-innovation--60dc31ce"]
papers: ["41708296", "35230132", "29572102"]
builds_on: ["findings/t4ss_cazy_environmental_hgt--44ad24db", "findings/t4ss_cazy_environmental_hgt--5d73bfde", "findings/t4ss_cazy_environmental_hgt--a2b33180", "findings/t4ss_cazy_environmental_hgt--91e33b0b", "conflicts/conflict--horizontal-gene-transfer-driven-innovation--60dc31ce"]
projects: ["cog_analysis", "costly_dispensable_genes", "gene_function_ecological_agora", "t4ss_cazy_environmental_hgt"]
topics: ["pangenome-structure-and-genome-evolution"]
---
# Do GT2 sugar-polymer genes mark a distinct class of metal-carrying conjugative elements?

Genomes with glycosyltransferase family 2 (GT2) genes near type IV secretion (T4SS, conjugation) machinery carry far more metal-resistance types than other genomes. Is GT2 a marker of a distinct kind of conjugative element that carries metal cargo, or is the metal signal a property of T4SS-bearing genomes in general, with GT2 a bystander?

## Hypothesis

Genomes with T4SS but no nearby GT2 carry metal resistance no more often than the genome background, and only GT2-adjacent T4SS neighbourhoods are enriched for metal cargo.

## Why it matters

If GT2-adjacent elements are a distinct class, cell-surface polysaccharide traits and metal resistance may be transferred together under shared selection in metal-rich habitats. If T4SS genomes in general carry the metal signal, the GT2 link is only incidental. The source also states that no plasmid-borne CAZy genes were found, so any route would be chromosomal or integrative.

## How to test it

In the Pangenome Collection and KBase Genomes, define three genome groups: T4SS genomes with GT2 in the T4SS-proximal neighbourhood (376 GT2-neighbourhood genomes, mean 0.045 metal-resistance types), T4SS genomes without nearby GT2, and genomes with GT2 but no T4SS (against 0.004 in 260,276 other genomes). Match groups on genome quality and taxonomy and compare metal-resistance types per genome. Then see whether the 32 high-confidence cross-phylum GT2 transfer events sit in lineages that also gained metal-resistance genes. Use NMDC BioSamples habitat labels to ask whether the enrichment is concentrated in metal-contaminated habitats. The proximity cut-off of 10 kb is not yet validated in the source, so repeat the group comparison at several cut-offs.

## What would support or refute it

Support: metal resistance is elevated only in the GT2-adjacent group and holds across cut-offs and habitats. Refutation: T4SS genomes without nearby GT2 are equally enriched, or the enrichment disappears once genome quality and taxonomy are matched.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Annotations and genomes are in the lakehouse, but neighbourhood grouping at several cut-offs and the matched comparison have not been run.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/kbase-genomes|KBase Genomes]]
- Collection: [[data/nmdc-ncbi-biosamples|NMDC BioSamples]]

## Builds on

- Finding: [[findings/t4ss_cazy_environmental_hgt--44ad24db|GT2-neighbourhood genomes carry more metal resistance genes]] (Insufficient literature evidence)
- Finding: [[findings/t4ss_cazy_environmental_hgt--5d73bfde|No plasmid-borne CAZy genes found; transfer appears chromosomal or integrative]] (Insufficient literature evidence)
- Finding: [[findings/t4ss_cazy_environmental_hgt--a2b33180|GT2 gene tree shows many cross-phylum horizontal transfer events]] (Insufficient literature evidence)
- Finding: [[findings/t4ss_cazy_environmental_hgt--91e33b0b|Many CAZy families co-occur near T4SS loci, led by GT2]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--horizontal-gene-transfer-driven-innovation--60dc31ce|Do Mobile Elements Carry Most Bacterial Gene Novelty, or Do Focal Innovations Arrive Without an MGE-Cargo Signal?]]

## Closest published work

- [PMID 41708296](https://pubmed.ncbi.nlm.nih.gov/41708296/) Antibiotics or Heavy Metals in Livestock Wastewater: Which One Is the Main Driver for the Development and Spread of Antibiotic Resistance under Coexposure?
- [PMID 35230132](https://pubmed.ncbi.nlm.nih.gov/35230132/) Pan-Genome Analysis of Delftia tsuruhatensis Reveals Important Traits Concerning the Genetic Diversity, Pathogenicity, and Biotechnological Properties of the Species.
- [PMID 29572102](https://pubmed.ncbi.nlm.nih.gov/29572102/) Biochemical characterization of the Helicobacter pylori Cag Type 4 Secretion System protein CagN and its interaction partner CagM.

PMID 41708296 asks whether antibiotics or heavy metals drive resistance spread in livestock wastewater, PMID 35230132 describes a Delftia pangenome, and PMID 29572102 characterizes a T4SS protein pair in Helicobacter. None asks whether a carbohydrate-synthesis family marks a separate class of secretion-linked elements that carry metal cargo.
