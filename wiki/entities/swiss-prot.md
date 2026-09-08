---
type: Dataset
description: Reviewed protein-sequence dataset used for homology and integrated annotation
  evidence.
sources:
- id: annotation_gap_discovery
  resource: ../summaries/annotation_gap_discovery__REPORT.md
  title: annotation gap discovery
- id: berdl_data_atlas
  resource: ../summaries/berdl_data_atlas__REPORT.md
  title: berdl data atlas
- id: paperblast_explorer
  resource: ../summaries/paperblast_explorer__REPORT.md
  title: paperblast explorer
title: Swiss-Prot
---
# Swiss-Prot

## What this entity is

**Canonical name:** Swiss-Prot. [^annotation_gap_discovery]

**Known aliases:** Swiss-Prot; reviewed UniProt protein sequences. [^annotation_gap_discovery]

**Stable external identifier:** No stable external identifier was reported in this document. [^annotation_gap_discovery]

Swiss-Prot is the reviewed protein-sequence dataset used to provide enzyme-homology exemplar sequences for the annotation-gap discovery pipeline. [^annotation_gap_discovery]

## Key facts

### Annotation-gap discovery

The study retrieved 328 reviewed bacterial sequences for 75 of 84 unique EC numbers through the UniProt REST API. [^annotation_gap_discovery]

The sequences served as exemplars for DIAMOND blastp homology searches against candidate proteins from 14 Fitness Browser organisms. [^annotation_gap_discovery]

The DIAMOND v2.1.16 search used `--evalue 1e-5`, `--max-target-seqs 20`, `--id 25`, `--query-cover 50`, and `--outfmt 6`. [^annotation_gap_discovery]

The search identified 154 BLAST hits. [^annotation_gap_discovery]

High-confidence homology required at least 30% identity, at least 70% coverage, and an e-value at most 1e-10, while medium-confidence homology required at least 25% identity, at least 50% coverage, and an e-value at most 1e-5. [^annotation_gap_discovery]

BLAST was the strongest single evidence stream: it resolved 70 of 201 gapfilled enzymatic reaction-organism pairs, or 34.8%, whereas the complete evidence pipeline resolved 96 of 201 pairs, or 47.8%. [^annotation_gap_discovery]

The complete pipeline combined Swiss-Prot homology with fitness evidence, pangenome conservation, pathway evidence, and metabolic-model gapfilling; this integration added 13 percentage points over BLAST alone. [^annotation_gap_discovery]

The reactions with the most BLAST hits were rxn02185, rxn03436, and rxn15947, which the study characterized as well-described enzymes with broad phylogenetic distribution. [^annotation_gap_discovery]

### Collection-scale literature coverage

The [PaperBLAST](kescience-paperblast.md) analysis **refines** Swiss-Prot’s role from a homology reference to a partially literature-linked protein resource: it contains 110,171 Swiss-Prot proteins associated with 181,916 unique papers, with 1.7 reported papers per protein. [^paperblast_explorer]

PaperBLAST includes approximately 19% of the full SwissProt database, estimated there as approximately 570K reviewed entries as of 2024; this **qualifies** rather than contradicts the use of Swiss-Prot as a reference, because curated knowledge exists for proteins that PaperBLAST cannot connect to PMC full text. [^paperblast_explorer]

The PaperBLAST coverage analysis **supports** the importance of provenance when interpreting Swiss-Prot-linked literature: its links are based on PubMed Central full-text mining, so papers behind paywalls may be missed, and a gene mention is not necessarily a functional characterization. [^paperblast_explorer]

### Structural fitness integration

The BERDL Data Atlas **refines** Swiss-Prot’s role as a homology reference by documenting a validated structural-fitness join: FitnessBrowser gene-fitness records were joined to Swiss-Prot best hits using the composite `orgId`, `locusId` key, then to AlphaFold entries through `sprotAccession` and `uniprot_accession`. [^berdl_data_atlas]

That validation found 79,180 genes with a Swiss-Prot best hit, of which 78,753 were represented in AlphaFold; 55,454 genes across 48 organisms had both fitness data and an AlphaFold model. [^berdl_data_atlas] The joined cohort contained 22,303 distinct AlphaFold models. [^berdl_data_atlas]

## Related pages

Swiss-Prot evidence is connected to the [diamond](diamond.md) homology-search method and the [uniprot](uniprot.md) protein resource. [^annotation_gap_discovery]

The dataset contributes to [metabolic-model-gapfilling](../concepts/metabolic-model-gapfilling.md) by supplying sequence evidence for candidate genes underlying gapfilled reactions. [^annotation_gap_discovery]

It also contributes to [multi-omics-integration](../concepts/multi-omics-integration.md) through integration of protein homology with fitness, pangenome, pathway, and metabolic-model evidence. [^annotation_gap_discovery]

The validated structural-fitness use further connects Swiss-Prot to [kescience-alphafold](kescience-alphafold.md) and [condition-specific-fitness](../concepts/condition-specific-fitness.md). [^berdl_data_atlas]

See the source summaries: [annotation_gap_discovery__REPORT](../summaries/annotation_gap_discovery__REPORT.md), [berdl_data_atlas__REPORT](../summaries/berdl_data_atlas__REPORT.md), and [paperblast_explorer__REPORT](../summaries/paperblast_explorer__REPORT.md). [^annotation_gap_discovery][^berdl_data_atlas][^paperblast_explorer]

[^annotation_gap_discovery]: [annotation gap discovery](../summaries/annotation_gap_discovery__REPORT.md)
[^paperblast_explorer]: [paperblast explorer](../summaries/paperblast_explorer__REPORT.md)
[^berdl_data_atlas]: [berdl data atlas](../summaries/berdl_data_atlas__REPORT.md)
