---
type: "Dataset"
description: "Structural-protein dataset connecting AlphaFold models, MSA depth, and fitness data."
sources: ["summaries/alphafold_msa_annotation__REPORT.md", "summaries/berdl_data_atlas__REPORT.md"]
---
# KEScience AlphaFold

## What this entity is

**Canonical name:** KEScience AlphaFold. [src: alphafold_msa_annotation]

**Known aliases:** AlphaFold MSA-depth dataset; KBase Data Lakehouse AlphaFold snapshot. [src: alphafold_msa_annotation]

**Stable external identifier:** No stable external identifier was reported in the source document. [src: alphafold_msa_annotation]

KEScience AlphaFold is a dataset used to provide multiple-sequence-alignment (MSA) depths for gene-cluster representative sequences in the KBase Data Lakehouse analysis. [src: alphafold_msa_annotation] The analysis joined it with [[entities/kbase-ke-pangenome]], Bakta annotations, and [[entities/interproscan]] domain annotations. [src: alphafold_msa_annotation]

The BERDL Data Atlas inventories 241,070,489 AlphaFold predicted structures, establishing this dataset as a major structural reference layer in the data lakehouse. [src: berdl_data_atlas] This **supports** its use as a structural complement to pangenome and fitness data, while the atlas **refines** the earlier description by documenting a separate validated structural-fitness join through SwissProt best hits. [src: berdl_data_atlas]

## Key facts from alphafold_msa_annotation

The analysis contained 132,531,501 total gene clusters, of which 38,804,903 (29.3%) had a real UniProt accession and 38,051,842 (28.7%) bridged successfully to AlphaFold MSA depths. [src: alphafold_msa_annotation] The remaining 70.7% lacked UniRef100 identifiers or had UniParc-only identifiers without an AlphaFold entry. [src: alphafold_msa_annotation]

Among the bridged clusters, core genes had a median MSA depth of 15,308, compared with 5,299 for auxiliary+singleton clusters and 5,527 for auxiliary non-singleton clusters. [src: alphafold_msa_annotation] The core median was 2.89× higher than auxiliary+singleton and 2.77× higher than auxiliary non-singleton clusters. [src: alphafold_msa_annotation]

The 10th-percentile MSA depth was 334 for core genes versus 25–32 for accessory genes. [src: alphafold_msa_annotation] Core clusters included 415,733 (1.6%) with MSA depth below 10, while auxiliary non-singleton clusters included 245,002 (4.6%) and auxiliary+singleton clusters included 392,959 (5.5%) below that threshold. [src: alphafold_msa_annotation]

Across 38,051,842 gene cluster–UniProt pairs, MSA depth and domain-hit count had Spearman ρ = 0.7563. [src: alphafold_msa_annotation] Mean domain hits increased from 0.59 for MSA depth below 10 to 10.83 for MSA depth at least 10,000, while mean distinct InterPro families increased from 0.059 to 4.601. [src: alphafold_msa_annotation]

The report identified 415,603 distinct core clusters with MSA depth below 10 across 14,768 species clades. [src: alphafold_msa_annotation] Their mean and median MSA depths were 4.57 and 4.0, respectively, and 286,439 (68.9%) were hypothetical. [src: alphafold_msa_annotation] Only 137 (0.033%) were EC-annotated and 346 (0.083%) were KEGG-mapped. [src: alphafold_msa_annotation]

These low-MSA-depth core clusters were interpreted as candidates for experimental structural characterisation because they are conserved by pangenome classification yet structurally isolated from characterised sequence space; this is a prioritisation hypothesis rather than direct experimental validation. [src: alphafold_msa_annotation]

The dataset used a static version-6 KBase Data Lakehouse AlphaFold snapshot. [src: alphafold_msa_annotation] MSA depth was looked up for each cluster's representative sequence, so within-cluster sequence diversity was not represented. [src: alphafold_msa_annotation]

## Validated structural-fitness integration

The Data Atlas **refines** the presumed join path: FitnessBrowser does not expose `protein_id`; the validated path joins gene-fitness records to SwissProt best hits on the composite `orgId, locusId` key, then joins `sprotAccession` to `uniprot_accession` in AlphaFold entries. [src: berdl_data_atlas] Of 79,180 genes with a SwissProt best hit, 78,753 were represented in AlphaFold, and 55,454 genes across 48 organisms had both fitness data and an AlphaFold model; the joined cohort contained 22,303 distinct AlphaFold models. [src: berdl_data_atlas]

Within that cohort, 6,635 genes were essential, defined as `min_fit ≤ −4`; 8,271 were strong-defect, 10,950 moderate, 29,467 mild, and 131 had no defect, with genes tested under an average of 121–187 conditions per gene. [src: berdl_data_atlas] This **supports** the existing proposal to analyse low-MSA-depth core clusters alongside [[concepts/gene-essentiality]] and [[entities/tnseq]], but the cohort does not itself validate the structural-characterisation hypothesis. [src: berdl_data_atlas]

The validated AlphaFold entries lack per-residue pLDDT and structural-feature data, so downstream structure–function analysis requires those features to be ingested or computed from PDB files. [src: berdl_data_atlas]

## Relations to other wiki pages

KEScience AlphaFold supplies structural-representation evidence for [[concepts/pangenome-integration]], including the 2.9× core/accessory MSA-depth gradient and the low-MSA-depth core subset. [src: alphafold_msa_annotation] Its domain-depth relationship connects to [[concepts/multi-omics-integration]] and supports proposed joins with [[entities/kescience-fitnessbrowser]] measurements. [src: alphafold_msa_annotation] The atlas **supports** this adjacency by validating a 55,454-gene FitnessBrowser–AlphaFold cohort. [src: berdl_data_atlas] The low-MSA-depth core clusters are proposed candidates for analysis alongside [[concepts/gene-essentiality]] and [[entities/tnseq]] fitness measurements. [src: alphafold_msa_annotation]

## Source

- [[summaries/alphafold_msa_annotation__REPORT]] — report describing AlphaFold MSA depth as a lens on the bacterial annotation gap. [src: alphafold_msa_annotation]
- [[summaries/berdl_data_atlas__REPORT]] — atlas inventory and validation of the AlphaFold structural-fitness bridge. [src: berdl_data_atlas]
