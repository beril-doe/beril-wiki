---
type: "Finding"
description: "The report concludes that for a substantial fraction of bacteria, amino acid biosynthesis pathway completeness depends on genes in the accessory pangenome."
finding_id: "pathway_capability_dependency--63330e78"
result: "inference"
source: "pathway_capability_dependency"
quantities: []
caveat: "Genes without KEGG annotations or with incorrect annotations are missed, which may underestimate the true number of genes per pathway."
first_added: "2026-11-24"
source_hash: "b48f1bebed72779629baaf7e71b9cffda8ab0298f49aa9c3460cc6d13bb7cf75"
---
# Amino acid biosynthesis completeness depends on accessory pangenome genes

The report concludes that for a substantial fraction of bacteria, amino acid biosynthesis pathway completeness depends on genes in the accessory pangenome. [src: pathway_capability_dependency]

## Evidence

> These gaps mean that for a substantial fraction of bacteria, amino acid biosynthesis pathway completeness depends on genes in the accessory pangenome. [src: pathway_capability_dependency]

From the report [[summaries/pathway_capability_dependency__REPORT]].

## Caveat

Genes without KEGG annotations or with incorrect annotations are missed, which may underestimate the true number of genes per pathway. [src: pathway_capability_dependency]

> Genes without KEGG annotations or with incorrect annotations are missed. This may underestimate the true number of genes per pathway. [src: pathway_capability_dependency]

## Other caveats in this report

- The report attributes the small conservation gap between pathway categories to its 7 Fitness Browser model organisms having near-complete, well-annotated core genomes. [src: pathway_capability_dependency]
- Genome count is a critical confounder because species with more sequenced genomes may appear to have more variable pathways solely from sampling depth. [src: pathway_capability_dependency]
- Smaller within-genus sample sizes limit statistical power for many groups in the pathway-variation analysis. [src: pathway_capability_dependency]
- Only 7 of the 48 Fitness Browser organisms have matching GapMind genome data. [src: pathway_capability_dependency]
- Full phylum-level stratification would require joining the KBase Data Lakehouse GTDB taxonomy table; the report instead uses genus-level grouping from GTDB species clade names as a conservative phylogenetic control. [src: pathway_capability_dependency]
