---
type: "Method"
description: "A fast sequence clustering tool used to cluster 815,571 PaperBLAST sequences at 90, 50 and 30% identity."
sources: ["summaries/paperblast_explorer__REPORT.md", "summaries/prophage_ecology__REPORT.md"]
aliases: ["MMseqs"]
---
# MMseqs2

This page covers MMseqs2 (also written MMseqs), a sequence clustering tool used to cluster 815,571 PaperBLAST sequences at 90, 50 and 30% identity. It was also used on prophage terminase large subunit (TerL) sequences. [src: paperblast_explorer, prophage_ecology]

## Key facts

- Use 1: clustering of 815,571 PaperBLAST protein sequences at three identity thresholds. [src: paperblast_explorer]
- Use 2: clustering of 38,085 bacterial prophage TerL sequences at 70% amino acid identity (AAI). [src: prophage_ecology]

## PaperBLAST clustering

The three thresholds give progressively coarser groupings. At 90% identity there were 628K clusters (77%), which the report reads as low strain-level redundancy. [src: paperblast_explorer] At 50% identity there were 345K clusters, read as the protein family level. [src: paperblast_explorer] At 30% identity there were 215K clusters, read as the superfamily level. [src: paperblast_explorer] See [[concepts/sequence-clustering-resolution-and-protein-family-definition]] and [[summaries/paperblast_explorer__REPORT]].

The report lists a CTS job, c10c4a0f-3d57-4219-9329-501b74c8f29a, for this clustering of 815K sequences at 90/50/30% identity. [src: paperblast_explorer] It also lists a generated summary file, data/clustering_summary.txt. [src: paperblast_explorer]

## Prophage TerL clustering

Clustering 38,085 TerL protein sequences at 70% AAI gave 10,991 lineages. [src: prophage_ecology] The size distribution was highly skewed, with median=1 and max=1,094. [src: prophage_ecology] The two source claims give different species counts. One says the sequences came from 11,789 species. [src: prophage_ecology] The other attaches "across 869 species" to the maximum lineage size of 1,094. [src: prophage_ecology] The claims do not explain the difference. It may reflect different scopes, but that is not stated. A threshold sensitivity analysis gave lineage counts from 4,001 at 50% AAI to 16,283 at 80% AAI. [src: prophage_ecology] The work was done in the notebook 02_terL_lineage_clustering.ipynb. [src: prophage_ecology] See [[concepts/environmental-specificity-of-prophage-terminase-lineages]] and [[summaries/prophage_ecology__REPORT]].
