---
type: "Research direction"
description: "Why do genomes with glycosyltransferase family 2 genes next to type IV secretion machinery carry far more metal-resistance genes, and does one mobile element carry both?"
hypothesis: "The glycosyltransferase and the metal-resistance genes sit on the same chromosomal integrative element. If so, metal resistance should also be elevated beside other carbohydrate-enzyme families near secretion loci, and the signal should disappear in genomes lacking the element."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "Genome annotations are in the lakehouse, but the synteny-threshold test and mobile-element calls on unfiltered data are pending, and closed-genome confirmation needs new long-read sequencing."
collections: ["kbase-ke-pangenome"]
findings: ["t4ss_cazy_environmental_hgt--44ad24db", "t4ss_cazy_environmental_hgt--5d73bfde", "t4ss_cazy_environmental_hgt--91e33b0b", "t4ss_cazy_environmental_hgt--a2b33180"]
conflicts: []
papers: ["29572102", "35230132", "41708296", "33096255"]
builds_on: ["findings/t4ss_cazy_environmental_hgt--44ad24db", "findings/t4ss_cazy_environmental_hgt--5d73bfde", "findings/t4ss_cazy_environmental_hgt--91e33b0b", "findings/t4ss_cazy_environmental_hgt--a2b33180"]
projects: ["t4ss_cazy_environmental_hgt"]
topics: ["pangenome-structure-and-genome-evolution"]
---
# Do glycosyltransferase genes near secretion loci travel on integrative elements carrying metal resistance?

Why do genomes with glycosyltransferase family 2 genes next to type IV secretion machinery carry far more metal-resistance genes, and does one mobile element carry both?

## Hypothesis

The glycosyltransferase and the metal-resistance genes sit on the same chromosomal integrative element. If so, metal resistance should also be elevated beside other carbohydrate-enzyme families near secretion loci, and the signal should disappear in genomes lacking the element.

## Why it matters

It would show whether secretion-linked integrative elements move cell-surface carbohydrate enzymes between phyla together with metal tolerance. That would tie horizontal transfer of surface chemistry to adaptation in contaminated habitats. Otherwise the association is a by-product of genome quality or habitat.

## How to test it

In Pangenome Collection genomes, take those with glycosyltransferase family 2 within 10 kb of secretion-machinery genes. Compare their metal-resistance content with genomes holding other carbohydrate-enzyme families near secretion loci and with genomes holding housekeeping-gene neighbourhoods as a matched background. Use integrative-element and mobile-element calls on the same contigs, and the 8-phylum tree branch flagged as the strongest transfer event, to test whether metal-resistance genes share the element. Then sequence selected strains with long reads to obtain closed genomes and confirm the arrangement.

## What would support or refute it

Support: metal-resistance genes lie on the same integrative element as the glycosyltransferase, and the enrichment is specific to this family. Refutation: the enrichment appears equally for other carbohydrate-enzyme families or housekeeping neighbourhoods, or the two gene sets lie on separate elements.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. Genome annotations are in the lakehouse, but the synteny-threshold test and mobile-element calls on unfiltered data are pending, and closed-genome confirmation needs new long-read sequencing.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/t4ss_cazy_environmental_hgt--44ad24db|GT2-neighbourhood genomes carry more metal resistance genes]] (Insufficient literature evidence)
- Finding: [[findings/t4ss_cazy_environmental_hgt--5d73bfde|No plasmid-borne CAZy genes found; transfer appears chromosomal or integrative]] (Insufficient literature evidence)
- Finding: [[findings/t4ss_cazy_environmental_hgt--91e33b0b|Many CAZy families co-occur near T4SS loci, led by GT2]] (Insufficient literature evidence)
- Finding: [[findings/t4ss_cazy_environmental_hgt--a2b33180|GT2 gene tree shows many cross-phylum horizontal transfer events]] (Insufficient literature evidence)

## Closest published work

- [PMID 29572102](https://pubmed.ncbi.nlm.nih.gov/29572102/) Biochemical characterization of the Helicobacter pylori Cag Type 4 Secretion System protein CagN and its interaction partner CagM.
- [PMID 35230132](https://pubmed.ncbi.nlm.nih.gov/35230132/) Pan-Genome Analysis of Delftia tsuruhatensis Reveals Important Traits Concerning the Genetic Diversity, Pathogenicity, and Biotechnological Properties of the Species.
- [PMID 41708296](https://pubmed.ncbi.nlm.nih.gov/41708296/) Antibiotics or Heavy Metals in Livestock Wastewater: Which One Is the Main Driver for the Development and Spread of Antibiotic Resistance under Coexposure?
- [PMID 33096255](https://pubmed.ncbi.nlm.nih.gov/33096255/) Complete genome sequence and comparative genome analysis of Alcanivorax sp. IO_7, a marine alkane-degrading bacterium isolated from hydrothermally-influenced deep seawater of southwest Indian ridge.

PMIDs 29572102 and 35230132 describe secretion-system proteins and pan-genomes in single organisms, and 41708296 describes metal-driven resistance spread in wastewater. None tests whether glycosyltransferase neighbourhoods and metal resistance share a mobile element.
