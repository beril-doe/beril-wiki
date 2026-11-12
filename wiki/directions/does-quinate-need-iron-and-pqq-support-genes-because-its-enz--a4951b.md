---
type: "Research direction"
description: "Most genes with quinate-specific defects in ADP1 fall into four groups: the aromatic degradation pathway, Complex I, iron acquisition and PQQ biosynthesis. Do the iron and PQQ genes matter because quinate catabolism depends on an iron-containing enzyme and a PQQ-dependent dehydrogenase?"
hypothesis: "Iron acquisition and PQQ mutants fail on quinate because quinate dehydrogenase needs PQQ and ring cleavage needs iron. Added iron or PQQ should relieve the defects."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "The co-occurrence step uses pangenome data. The rescue test needs ADP1 deletion mutants and new growth measurements."
collections: ["kbase-ke-pangenome"]
findings: ["aromatic_catabolism_network--8650ba38", "adp1_deletion_phenotypes--ec39f324"]
conflicts: []
papers: ["8002591", "3044290", "2855587", "15691962", "25374488"]
builds_on: ["findings/aromatic_catabolism_network--8650ba38", "findings/adp1_deletion_phenotypes--ec39f324"]
projects: ["adp1_deletion_phenotypes", "aromatic_catabolism_network"]
topics: ["gene-fitness-landscapes-and-cofitness-modules"]
---
# Does quinate need iron and PQQ support genes because its enzymes are iron- and cofactor-limited?

Most genes with quinate-specific defects in ADP1 fall into four groups: the aromatic degradation pathway, Complex I, iron acquisition and PQQ biosynthesis. Do the iron and PQQ genes matter because quinate catabolism depends on an iron-containing enzyme and a PQQ-dependent dehydrogenase?

## Hypothesis

Iron acquisition and PQQ mutants fail on quinate because quinate dehydrogenase needs PQQ and ring cleavage needs iron. Added iron or PQQ should relieve the defects.

## Why it matters

It would explain why the aromatic module has dispersed support genes. It would also show which co-factor supply limits growth on aromatics.

## How to test it

Grow deletions of the 7 iron acquisition genes and 2 PQQ biosynthesis genes in ADP1 on quinate with and without surplus iron or PQQ. Include growth on a non-aromatic carbon source as a control. Across the Pangenome Collection, ask whether species carrying the quinate pathway also keep iron-acquisition and PQQ genes more often than those without it.

## What would support or refute it

Support: iron or PQQ restores quinate growth in the matching mutants and the genes co-occur with the pathway. Refute: supplementation does not rescue, or the mutants are equally impaired on non-aromatic carbon.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. The co-occurrence step uses pangenome data. The rescue test needs ADP1 deletion mutants and new growth measurements.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/aromatic_catabolism_network--8650ba38|Co-fitness assigns most quinate-specific genes to four support subsystems]] (Insufficient literature evidence)
- Finding: [[findings/adp1_deletion_phenotypes--ec39f324|Aromatic degradation genes form the only discrete phenotypic module]] (Extends retrieved work)

## Closest published work

- [PMID 8002591](https://pubmed.ncbi.nlm.nih.gov/8002591/) The pca-pob supraoperonic cluster of Acinetobacter calcoaceticus contains quiA, the structural gene for quinate-shikimate dehydrogenase.
- [PMID 3044290](https://pubmed.ncbi.nlm.nih.gov/3044290/) Bacterial NAD(P)-independent quinate dehydrogenase is a quinoprotein.
- [PMID 2855587](https://pubmed.ncbi.nlm.nih.gov/2855587/) A search for intermediates in the bacterial biosynthesis of PQQ.
- [PMID 15691962](https://pubmed.ncbi.nlm.nih.gov/15691962/) Transcriptional organization of genes for protocatechuate and quinate degradation from Acinetobacter sp. strain ADP1.
- [PMID 25374488](https://pubmed.ncbi.nlm.nih.gov/25374488/) Novel metabolic features in Acinetobacter baylyi ADP1 revealed by a multiomics approach.

PMID 3044290 and PMID 2855587 describe the PQQ-dependent quinate dehydrogenase, and PMID 8002591 and PMID 15691962 map the pathway genes. None addresses the iron and PQQ support set found by cofitness.
