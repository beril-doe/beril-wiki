---
type: "Organism"
description: "The clinical pathogen Staphylococcus aureus, including strain NCTC 8325, covering its near-entirely accessory AMR repertoire and its role as a modeled Firmicute."
sources: ["summaries/amr_environmental_resistome__REPORT.md", "summaries/amr_strain_variation__REPORT.md", "summaries/functional_dark_matter__REPORT.md", "summaries/plant_microbiome_ecotypes__REPORT.md", "summaries/thermodynamic_impact__REPORT.md"]
aliases: ["S. aureus", "Staphylococcus aureus NCTC 8325"]
---
# Staphylococcus aureus

This page covers the clinical pathogen Staphylococcus aureus, including strain NCTC 8325. In the reports compiled here, its antimicrobial resistance (AMR) gene repertoire is almost entirely accessory [src: amr_environmental_resistome], and it is a modeled Firmicute [src: thermodynamic_impact] that was left out of a dark-gene organism covering set. [src: functional_dark_matter]

## Key facts

- In the AMR environmental resistome survey, S. aureus has 13,274 genomes and 642 AMR clusters. Of these, 9 are core and 633 (99%) are accessory. Its dominant environment is Clinical (85%). [src: amr_environmental_resistome] See [[concepts/environmental-and-clinical-distribution-of-antimicrobial-resistance]] and [[summaries/amr_environmental_resistome__REPORT]].
- The GTDB/NCBI genome collection is heavily biased toward clinical and human-associated isolates, particularly K. pneumoniae, S. aureus and E. coli. Environmental species are underrepresented. [src: amr_strain_variation] See [[concepts/sampling-bias-and-metadata-sparsity-in-amr-resistome-surveys]].

## AMR ecotypes

Case-study UMAP (uniform manifold approximation and projection) plots for K. pneumoniae, S. aureus and S. enterica show visible environmental structuring of AMR ecotypes. The report notes that the statistical test of this is underpowered with current metadata. [src: amr_strain_variation] See [[concepts/amr-ecotypes-and-environmental-association]], [[summaries/amr_strain_variation__REPORT]] and [[entities/salmonella-enterica]].

## Dark-gene organism selection

The covering-set algorithm did not select the Bacillota organisms B. subtilis and S. aureus. Their ortholog groups (OGs) are subsets of the coverage already provided by Pseudomonadota. [src: functional_dark_matter] The report adds that they remain valuable for studying genes in native Gram-positive genomic context. [src: functional_dark_matter] See [[concepts/organism-selection-and-taxonomic-coverage-bias-for-experimental-characterization-of-dark-genes]], [[entities/bacillus-subtilis-168]] and [[summaries/functional_dark_matter__REPORT]].

## Plant-marker negative control

In the plant microbiome project, Staphylococcus served as a non-plant negative control. Negative controls (NB08) classified it as 98% dual-nature. [src: plant_microbiome_ecotypes] With the refined plant marker panel, 18% of Staphylococcus was PGP-only. [src: plant_microbiome_ecotypes] See [[concepts/dual-nature-plant-associated-bacteria-and-the-validity-of-marker-based-cohorts]] and [[summaries/plant_microbiome_ecotypes__REPORT]].

## Metabolic model and thermodynamics

The S. aureus NCTC 8325 model is listed as Firmicutes with a GramPos template. It has 777 genes and 1,128 reactions, and its growth is 0.5000. [src: thermodynamic_impact] In the TMFA (thermodynamics-based metabolic flux analysis) impact table, 775 of the 1,128 reactions were constrained. None had changed flux (0, percentage 0.00), and none were newly blocked, newly active or reversed. There were 8 Marvin-versus-OPAM2 differences. [src: thermodynamic_impact] See [[concepts/effect-of-pka-source-on-flux-predictions-across-diverse-organisms]] and [[summaries/thermodynamic_impact__REPORT]].
