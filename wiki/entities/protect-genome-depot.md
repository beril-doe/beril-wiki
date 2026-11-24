---
type: "Dataset"
description: "ARPA-H PROTECT MIND pathogen genome depot (protect_genomedepot)."
sources: ["summaries/berdl_data_atlas__REPORT.md", "summaries/cf_formulation_design__REPORT.md", "summaries/discoveries.md", "summaries/pitfalls.md"]
aliases: ["PROTECT", "PROTECT Gold", "PROTECT MIND", "protect_genomedepot"]
---
# PROTECT genome depot

PROTECT genome depot (`protect_genomedepot`; also PROTECT, PROTECT Gold, PROTECT MIND) is the ARPA-H PROTECT pathogen genome collection hosted in the [[entities/kbase-data-lakehouse|KBase Data Lakehouse]]. Its browser tables make up the PROTECT MIND pathogen genome depot. [src: berdl_data_atlas] The evidence comes from two reports: the platform audit [[summaries/berdl_data_atlas__REPORT]] and the cystic fibrosis formulation project [[summaries/cf_formulation_design__REPORT]]. Pitfalls notes from other projects add query caveats.

## Key facts

- The inventory lists 4,923 PROTECT MIND genomes. [src: berdl_data_atlas]
- The depot tables are `browser_genome`, `browser_gene` and `browser_protein`. [src: berdl_data_atlas]
- The cf_formulation_design project used `browser_genome` and `browser_gene_sampled` for isolate genome annotations and reference-genome linkage. [src: cf_formulation_design]
- A second Protect-tenant database, `protect_integration`, exists beyond `protect_genomedepot`. [src: discoveries]
- The cf_formulation_design project also used "PROTECT Gold" (`~/protect/gold/`). It has 23 tables (30.5M rows) covering the isolate catalog, inhibition assays, carbon utilization, growth kinetics, patient metagenomics and pairwise interactions. [src: cf_formulation_design]

## Place in the platform

ARPA-H (PROTECT) contributes 4% of the KBase Data Lakehouse tables [src: berdl_data_atlas] and spans 6 topics. [src: berdl_data_atlas] The tenant has topic entropy 2.37 and is described as punching above its size. [src: berdl_data_atlas] See [[concepts/funding-agency-and-topic-coverage-of-a-shared-data-platform]].

Use of PROTECT is limited. It appears in 2 audited BERIL projects. [src: berdl_data_atlas] The report calls PROTECT under-leveraged for cross-program work, with fewer than 8 projects despite relevant topics. [src: berdl_data_atlas] The nmdc ↔ protect bridge has 10 shared keys but had zero realized use at audit time. [src: berdl_data_atlas] See [[concepts/realized-versus-theoretical-cross-collection-data-reuse]].

For pathogens, the report recommends `protect_genomedepot` for MIND classification. It suggests joining to environmental abundance via `ncbi_taxon_id`. [src: berdl_data_atlas] Use case UC4 would use that bridge to ask where clinically relevant pathogens live in the environment and what biogeochemistry tracks them. [src: berdl_data_atlas] See [[concepts/untapped-cross-program-synergy-use-cases-for-environmental-and-clinical-microbiology]].

## The PROTECT cystic fibrosis isolate collection

The cf_formulation_design report combined the PROTECT CF Synbiotic Cocktail Study (4,949 isolates from 175 CF/NCFB patient samples) with the pangenome of 293,000 genomes and GapMind pathway predictions. [src: cf_formulation_design] The study produced 23 structured tables with 30.5M total rows. They cover 4,949 isolates from 211 species across 175 patient samples (133 CF, 41 NCFB, 43 subjects, 4 clinical states). [src: cf_formulation_design] Patient metagenomics covers 175 samples. [src: cf_formulation_design]

The collection is dominated by three species [src: cf_formulation_design]:

| Species | Isolates |
|---|---|
| [[entities/pseudomonas-aeruginosa]] | 655 |
| Staphylococcus aureus | 379 |
| [[entities/rothia-dentocariosa]] | 318 |

Genome quality is high, with mean completeness 99.8% and median contamination 0.08%. [src: cf_formulation_design]

Three assays were run [src: cf_formulation_design]:
- Planktonic inhibition of PA14, tested with 220 isolates.
- Carbon source utilization, with 430 isolates on 21 substrates.
- Growth kinetics, with 32 isolates and full time-series curves.

The core cohort with both inhibition and carbon utilization data has 142 isolates from 62 species. [src: cf_formulation_design]

## Annotation and query caveats

- Of 643 profiled PROTECT P. aeruginosa genomes, 291 (45%) are intermediate because they lack clear T3SS (type III secretion system) annotation in GenomeDepot. [src: cf_formulation_design] Another statement of the same gap gives a collection of 651 genomes with 45% unannotated for T3SS effectors. [src: cf_formulation_design] The two reports give different genome counts (643 and 651). See [[concepts/annotation-based-gene-detection-limits-in-pangenome-trait-surveys]] and [[concepts/pseudomonas-aeruginosa-strain-diversity-and-representativeness-of-reference-strains]].
- GenomeDepot and the pangenome use different annotation pipelines (bakta/eggNOG for the pangenome). Gene names are therefore unreliable for cross-database comparison. [src: cf_formulation_design] See [[entities/kbase-ke-pangenome]].
- GenomeDepot databases rarely annotate pslA–pslO with canonical gene names. Only the PAO1 reference genome has them. This applies to `protect_genomedepot` and `phagefoundry_paeruginosa_genome_browser`. [src: pitfalls] See [[entities/phagefoundry]].
- `browser_genome` has no species column, so species filtering needs a join through `browser_taxon`. [src: pitfalls] The documented query joins `browser_gene.genome_id` to `browser_genome.id` and `browser_genome.taxon_id` to `browser_taxon.id`. [src: pitfalls]
- The database uses sampled table variants (`browser_gene_sampled`, `browser_annotation_sampled`). Query these instead of the unsuffixed names. [src: pitfalls]
