---
type: "Concept"
description: "Whether exometabolite-derived phenotypes such as de novo production fraction can be cross-referenced to pangenome size, openness and gene clusters; covers genus-level availability and the strain-to-genome mapping gap."
sources: ["summaries/webofmicrobes_explorer__REPORT.md"]
---
# Linking exometabolic phenotypes to pangenome gene content

This page covers whether exometabolite phenotypes such as de novo production fraction can be cross-referenced to pangenome size, openness and gene clusters. Pangenome context exists for every Web of Microbes (WoM) genus. [src: webofmicrobes_explorer] The report proposes the analysis but does not run it, and species-level matching is blocked by a strain-to-genome mapping gap. [src: webofmicrobes_explorer] See [[summaries/webofmicrobes_explorer__REPORT]].

## Literature Context

The candidate papers show that pairing gene content with metabolic phenotypes is an established approach, usually at strain or species level. None of them tests the hub's specific question, whether a de novo production fraction tracks pangenome openness or accessory gene content. In coastal Vibrio cholerae, 41 non-O1/O139 environmental isolates and four clinical strains were profiled. Comparative genome hybridization identified 2,787 core genes, and dispensable genes and metabolic capabilities were correlated with measured environmental parameters [PMID 17449702](https://pubmed.ncbi.nlm.nih.gov/17449702/). In mulberry-associated Pantoea ananatis, two strains shared approximately 98.9% average nucleotide identity but differed in accessory-gene content, plasmid composition and strain-specific clusters. Their host-contact extracellular metabolomes also differed, though the authors state that the contributions of individual loci and phylogenetic background remain unresolved [PMID 42998248](https://pubmed.ncbi.nlm.nih.gov/42998248/).

Other papers link genes to metabolic output more loosely. A Paracoccus niotae genome showed an open pan-genome of 19,613 gene clusters, including 1,288 strain-specific genes. It also carried carotenoid biosynthesis genes, and the strain produced carotenoids. The abstract reports these findings side by side and does not show that the genes caused the measured production [PMID 42801408](https://pubmed.ncbi.nlm.nih.gov/42801408/). A qPCR assay for the but gene found higher but gene copy number in lean vegans than in healthy obese omnivores, in line with higher fecal butyrate in the vegan group. The abstract reports this groupwise correspondence and no formal correlation [PMID 34572516](https://pubmed.ncbi.nlm.nih.gov/34572516/). In Sinorhizobium meliloti, moving the pSymA replicon, about 20% of the genome, between strains gave a cis-hybrid whose phenotypes, including intra- and extracellular metabolomes, agreed well with both parents. This is direct experimental evidence that accessory replicon content shapes phenotype within a species' pangenome [PMID 30223644](https://pubmed.ncbi.nlm.nih.gov/30223644/). Genome-scale reconstruction of Bacteroides thetaiotaomicron (iAH991, 991 genes) also predicted exchanged metabolites that were compared with published metabolomics data. This is a model-based route from gene content to exometabolite exchange, similar in spirit to the hub's proposed use of `gapmind_pathways` [PMID 23022739](https://pubmed.ncbi.nlm.nih.gov/23022739/).

The corpus's claims sit mostly as an extension of this literature and are consistent with it. Pangenome context exists for every Web of Microbes genus, and the page proposes that organisms with higher E/(E+I) ratios may have more open pangenomes or more accessory genes. The cited studies make that hypothesis plausible but do not confirm it. They support the premise that accessory content relates to metabolic phenotype, but they are single-species or few-strain studies, and none uses a production fraction across genera. The hub's genus-level design, with entries ranging from 2 to 2,557 genomes, and its strain-to-genome mapping gap are not addressed by any candidate. The hub reports no result, so the test remains novel and untested. The candidates also warn that apparent gene-phenotype links can be confounded by phylogenetic background [PMID 42998248](https://pubmed.ncbi.nlm.nih.gov/42998248/), which bears on the proposed comparison. The remaining candidates, on rice OsCSLD4, Paraburkholderia dioscoreae, Bacillus altitudinis and Bifidobacterium kimbladii, do not bear on this question.

## Genus-level availability

Pangenome context (gene clusters, conservation, functional annotations) is available for all WoM organism genera, and every WoM genus has pangenome representation. [src: webofmicrobes_explorer] The report drew on the [[entities/kbase-data-lakehouse]] collection `kbase_ke_pangenome`, tables `pangenome` and `gapmind_pathways`, for species clade counts and pathway predictions. [src: webofmicrobes_explorer] For pathway predictions, see [[entities/gapmind]].

The table below lists entries from the report's pangenome context table, with pangenome species in the top-species listing and total genomes. [src: webofmicrobes_explorer] Pseudomonas fluorescens, Zymomonas mobilis and Escherichia coli are named at species level; the others are genera.

| Entry | Pangenome species | Total genomes |
|---|---|---|
| Bacillus | 5 [src: webofmicrobes_explorer] | 2,557 [src: webofmicrobes_explorer] |
| Rhizobium | 5 [src: webofmicrobes_explorer] | 449 [src: webofmicrobes_explorer] |
| Pseudomonas fluorescens | 5 [src: webofmicrobes_explorer] | 139 [src: webofmicrobes_explorer] |
| Synechococcus | 5 [src: webofmicrobes_explorer] | 88 [src: webofmicrobes_explorer] |
| Phenylobacterium | 5 [src: webofmicrobes_explorer] | 80 [src: webofmicrobes_explorer] |
| Acidovorax | 5 [src: webofmicrobes_explorer] | 79 [src: webofmicrobes_explorer] |
| Zymomonas mobilis | 1 [src: webofmicrobes_explorer] | 26 [src: webofmicrobes_explorer] |
| Escherichia coli | 1 [src: webofmicrobes_explorer] | 2 [src: webofmicrobes_explorer] |

Genome counts vary widely across these entries, from 2,557 for Bacillus to 2 for Escherichia coli. [src: webofmicrobes_explorer]

## The strain-to-genome mapping gap

Species-level matching of WoM to the pangenome requires strain-to-genome mapping, which the project did not attempt. [src: webofmicrobes_explorer] The general problem is discussed in [[concepts/linking-isolate-and-strain-records-to-reference-genome-databases]].

## Proposed phenotype

The report proposes a "metabolic novelty rate" as a potential phenotype for cross-referencing with pangenome gene content. [src: webofmicrobes_explorer] Specifically, it proposes testing whether organisms with higher E/(E+I) ratios (more de novo production) have more open pangenomes or more accessory genes. [src: webofmicrobes_explorer] This is a hypothesis; the report gives no result. [src: webofmicrobes_explorer]

## Open Directions

- Run the proposed test at genus level: correlate the E/(E+I) de novo production ratio with pangenome openness and accessory gene counts. This tests the hypothesis in the report.
- Build a strain-to-genome mapping for WoM organisms. This would allow species-level comparisons and close the mapping gap.
- Account for genome depth, since the listed entries range from 2 to 2,557 genomes. Restrict to well-sampled entries before comparing openness.
- Compare WoM-observed production with pathway predictions from `gapmind_pathways` to link gene content to metabolite output.
