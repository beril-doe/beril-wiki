---
type: "Method"
description: "Sequence-search and clustering method used for protein-family and TerL lineage analysis"
sources: ["summaries/paperblast_explorer__REPORT.md", "summaries/prophage_ecology__REPORT.md"]
---
# MMseqs2

## What it is

**MMseqs2** is the canonical name of a sequence-search and clustering method used in the [[summaries/paperblast_explorer__REPORT]] analysis; no additional alias or stable external identifier is reported in that document. [src: paperblast_explorer]

## Key facts in PaperBLAST analysis

MMseqs2 clustered **815,571** protein sequences from the [[entities/kescience-paperblast]] collection at **90%**, **50%**, and **30%** sequence-identity thresholds. [src: paperblast_explorer]

The clustering produced **628K** clusters at 90% identity, **345K** clusters at 50% identity, and **215K** clusters at 30% identity. [src: paperblast_explorer]

The report interprets these thresholds as representing low strain-level redundancy at 90% identity, a protein-family scale at 50% identity, and a superfamily scale at 30% identity; the 50% cutoff is conventional rather than a universal biological boundary. [src: paperblast_explorer]

At 90% identity, **83.3%** of clusters were singletons; at 50% identity, **67.5%** were singletons; and at 30% identity, **62.8%** were singletons. [src: paperblast_explorer]

The largest 90%-identity cluster contained **212** members and was identified as actin. [src: paperblast_explorer]

At 50% identity, the largest reported protein families included HSP70/BiP with **650** members, GAPDH with **609**, enolase with **552**, and GroEL with **443**. [src: paperblast_explorer]

The 50%-identity clustering supported the identification of poorly studied protein families relevant to [[concepts/gene-function-acquisition-depth]]: **9.2%** of families (**31,653**) had zero papers across all members, **46.1%** (**159,046**) had exactly one paper, and **4.3%** (**14,904**) had **20 or more** papers. [src: paperblast_explorer]

The analysis found **5,218** multi-member 50%-identity families, representing **14,534** sequences, with no literature whatsoever. [src: paperblast_explorer]

Family size was positively associated with literature coverage: **95.4%** of multi-member 50%-identity clusters had at least one member with a paper, while **4.6%**—**5,218** families—had none. [src: paperblast_explorer]

The report describes the dark families as dominated by REBASE methyltransferases and biolip structural entries, while cautioning that the 50% identity threshold is an analytical convention and that missing literature may reflect incomplete text mining rather than genuine absence of study. [src: paperblast_explorer]

## Prophage ecology application

The [[summaries/prophage_ecology__REPORT]] analysis **extends** MMseqs2’s demonstrated protein-family use to prophage lineage analysis: it clustered **38,085** TerL sequences from **11,789** species into **10,991** lineages at **70% AAI**, where AAI means amino-acid identity. [src: prophage_ecology]

Threshold sensitivity produced **4,001** lineages at **50% AAI** and **16,283** at **80% AAI**; the largest 70%-AAI lineage contained **1,094** members across **869** species, while **6,921** lineages (**63%**) were singletons. [src: prophage_ecology]

This application **refines** the existing interpretation of identity thresholds: MMseqs2 supported both broad protein-family characterization and finer TerL lineage partitioning, but the prophage analysis found no significant environment-specific enrichment for individual TerL lineages in **0/500** tests after FDR correction. [src: prophage_ecology]

## Relation to the source resource

MMseqs2 provided the sequence-family layer for the collection-level characterization of [[entities/kescience-paperblast]], allowing literature coverage to be evaluated across protein families rather than only individual genes. [src: paperblast_explorer]

In the prophage study, it provided the lineage-clustering layer for comparing TerL-associated prophage variation across hosts and environments, complementing module-level ecological analyses. [src: prophage_ecology]
