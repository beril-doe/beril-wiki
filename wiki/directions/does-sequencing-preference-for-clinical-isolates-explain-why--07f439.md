---
type: "Research direction"
description: "Do clinical species really carry more antimicrobial resistance (AMR) gene clusters, or do clinical species simply get sequenced more deeply and because of their resistance?"
hypothesis: "After matching species for genome count and phylogeny and reweighting for sampling intensity, the clinical excess in AMR clusters shrinks sharply but does not vanish, because some of the excess is real selection and some is sampling preference."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "The catalog shows AMR gene calls, biome labels, environment metadata and species clades; the join and subsampling need new compute, and the catalog did not show per-genome clinical labels directly."
databases: ["kbase.ke_pangenome", "kescience.mgnify"]
tables: ["kescience.mgnify.gene_amr", "kescience.mgnify.biome", "kbase.ke_pangenome.ncbi_env", "kbase.ke_pangenome.gtdb_species_clade"]
findings: ["amr_environmental_resistome--3d24fba7", "amr_environmental_resistome--8ab4f4eb", "amr_environmental_resistome--58d57c36", "amr_pangenome_atlas--012985a7"]
conflicts: ["conflict--clinical-and-human-associated-sampling-bias-in-genome-collections--2e525286"]
papers: ["25003965", "22936781", "24847883", "32351993"]
builds_on: ["findings/amr_environmental_resistome--3d24fba7", "findings/amr_environmental_resistome--8ab4f4eb", "findings/amr_environmental_resistome--58d57c36", "findings/amr_pangenome_atlas--012985a7", "conflicts/conflict--clinical-and-human-associated-sampling-bias-in-genome-collections--2e525286"]
projects: ["amr_environmental_resistome", "amr_pangenome_atlas", "ecotype_env_reanalysis", "env_embedding_explorer", "genotype_to_phenotype_enigma", "pseudomonas_carbon_ecology"]
topics: ["sampling-coverage-and-statistical-confounding"]
---
# Does sequencing preference for clinical isolates explain why clinical species carry more AMR gene clusters?

Do clinical species really carry more antimicrobial resistance (AMR) gene clusters, or do clinical species simply get sequenced more deeply and because of their resistance?

## Hypothesis

After matching species for genome count and phylogeny and reweighting for sampling intensity, the clinical excess in AMR clusters shrinks sharply but does not vanish, because some of the excess is real selection and some is sampling preference.

## Why it matters

Resistome comparisons across habitats underpin risk assessments of environmental reservoirs. If the clinical excess is mostly sampling, environmental species are underrated as AMR carriers; if it persists, clinical selection is real.

## How to test it

Using AMR gene calls in the MGnify genome catalogue and the pangenome species table with NCBI environment metadata, compute per-species AMR cluster counts. Compare clinical and soil, aquatic or host species within the same genus, subsample every species to equal genome numbers, and repeat after excluding genomes from outbreak-style bioprojects. Also test whether clinical fraction still predicts accessory AMR share after this control.

## What would support or refute it

Support: the clinical excess falls but remains in matched, equal-depth comparisons. Refute: it disappears at equal depth within genus, meaning the original difference was sampling preference.

## Data

Approach: lakehouse analysis. Readiness: needs compute. The catalog shows AMR gene calls, biome labels, environment metadata and species clades; the join and subsampling need new compute, and the catalog did not show per-genome clinical labels directly.

## Builds on

- Finding: [[findings/amr_environmental_resistome--3d24fba7|Clinical species carry more AMR gene clusters than environmental species]] (Candidate novel)
- Finding: [[findings/amr_environmental_resistome--8ab4f4eb|Clinical genome fraction predicts species AMR cluster count]] (Candidate novel)
- Finding: [[findings/amr_environmental_resistome--58d57c36|Clinical fraction does not clearly predict accessory AMR share]] (Candidate novel)
- Finding: [[findings/amr_pangenome_atlas--012985a7|Pangenome openness does not correlate with AMR count overall]] (Candidate novel)
- Conflict: [[conflicts/conflict--clinical-and-human-associated-sampling-bias-in-genome-collections--2e525286|Clinical Sampling Bias: Explanation for a Weak Environment Signal, or Not?]]

## Closest published work

- [PMID 25003965](https://pubmed.ncbi.nlm.nih.gov/25003965/) Improved annotation of antibiotic resistance determinants reveals microbial resistomes cluster by ecology.
- [PMID 22936781](https://pubmed.ncbi.nlm.nih.gov/22936781/) The shared antibiotic resistome of soil bacteria and human pathogens.
- [PMID 24847883](https://pubmed.ncbi.nlm.nih.gov/24847883/) Bacterial phylogeny structures soil resistomes across habitats.
- [PMID 32351993](https://pubmed.ncbi.nlm.nih.gov/32351993/) Comparison of Antimicrobial Resistance Detected in Environmental and Clinical Isolates from Historical Data for the US.

25003965 and 22936781 show resistomes cluster by ecology and overlap between soil and pathogens; this direction asks whether the clinical excess in per-species counts survives equal-depth, within-genus comparison.
