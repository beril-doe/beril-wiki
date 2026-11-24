---
type: "Method"
description: "Fast protein sequence aligner (BLAST-like) used here to search gap-reaction candidates against Swiss-Prot exemplars."
sources: ["summaries/annotation_gap_discovery__REPORT.md", "summaries/conservation_vs_fitness__REPORT.md"]
aliases: ["DIAMOND BLAST", "DIAMOND blastp"]
---
# DIAMOND

DIAMOND is used here to search gap-reaction candidates against [[entities/swiss-prot|Swiss-Prot]] exemplars. [[summaries/annotation_gap_discovery__REPORT]] and [[summaries/conservation_vs_fitness__REPORT]] describe the two projects that use it. [src: annotation_gap_discovery, conservation_vs_fitness]

## Key facts

- In the conservation-versus-fitness project, DIAMOND blastp is the protein-similarity search method for gene-to-cluster mapping, attributed to Buchfink et al. (2015). [src: conservation_vs_fitness]
- In the annotation-gap project, DIAMOND BLAST was run against concatenated proteomes in the triangulation pipeline. [src: annotation_gap_discovery]

## Annotation-gap search

The search used DIAMOND v2.1.16 blastp with `--evalue 1e-5 --max-target-seqs 20 --id 25 --query-cover 50 --outfmt 6`. The targets were Swiss-Prot exemplar sequences: 328 reviewed bacterial sequences for 75/84 unique EC (Enzyme Commission) numbers, retrieved from the UniProt REST (representational state transfer) API (application programming interface). It identified 154 hits. [src: annotation_gap_discovery]

The analysis used medium-confidence thresholds of >=25% identity, >=50% coverage and e-value <=1e-5. [src: annotation_gap_discovery] Hits meeting high-confidence thresholds (>=30% identity, >=70% coverage, e-value <=1e-10) were concentrated in branched-chain amino acid biosynthesis and polyamine metabolism reactions. [src: annotation_gap_discovery]

The top reactions by hit count were rxn02185, rxn03436 and rxn15947. All three encode well-characterized enzymes with broad phylogenetic distribution. [src: annotation_gap_discovery] See [[concepts/multi-evidence-triangulation-of-metabolic-annotation-gaps]] for how this evidence is combined with other lines.

## Gene-to-cluster mapping

The mapping produced 177,863 gene-to-cluster links at 100.0% median protein identity and 94.2% median gene coverage. [src: conservation_vs_fitness] Of the mapped organisms, 34 have >=90% coverage. 33 were used downstream, and Dyella79 was excluded because of a locus tag mismatch. [src: conservation_vs_fitness] See [[concepts/linking-fitness-assay-genes-to-pangenome-clusters]] and [[entities/fitness-browser]].
