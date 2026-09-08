---
type: Organism
description: Cystic-fibrosis pathogen and intensively studied Pseudomonas model.
sources:
- id: cf_formulation_design
  resource: ../summaries/cf_formulation_design__REPORT.md
  title: cf formulation design
- id: essential_metabolome
  resource: ../summaries/essential_metabolome__REPORT.md
  title: essential metabolome
- id: lignin_community_enrichment
  resource: ../summaries/lignin_community_enrichment__REPORT.md
  title: lignin community enrichment
- id: paperblast_explorer
  resource: ../summaries/paperblast_explorer__REPORT.md
  title: paperblast explorer
- id: pseudomonas_carbon_ecology
  resource: ../summaries/pseudomonas_carbon_ecology__REPORT.md
  title: pseudomonas carbon ecology
title: Pseudomonas aeruginosa
---
# Pseudomonas aeruginosa

## What this entity is

**Pseudomonas aeruginosa** is the canonical organism name for the cystic-fibrosis airway pathogen targeted by protective commensal formulations designed to achieve competitive exclusion. [^cf_formulation_design]

Known aliases include **PA** and **P. aeruginosa**. [^cf_formulation_design]

A stable external identifier was not provided in the source report. [^cf_formulation_design]

## Key facts from the formulation-design study

- The study targeted *P. aeruginosa* using planktonic inhibition assays, carbon-utilization profiling, growth kinetics, patient metagenomics and metatranscriptomics, pairwise interaction data, and pangenome analysis. [^cf_formulation_design]
- The experiments primarily used the PA14 strain under synthetic cystic-fibrosis sputum conditions. [^cf_formulation_design]
- PA14 preferentially used amino acids, with endpoint optical-density values of 0.60 for proline, 0.56 for histidine, 0.46 for ornithine, 0.40 for glutamate, 0.36 for aspartate, 0.36 for isoleucine, and 0.35 for arginine. [^cf_formulation_design]
- Glucose supported an endpoint optical density of 0.22, while threonine, methionine, cysteine, serine, and glycine each supported essentially no growth at less than 0.07. [^cf_formulation_design]
- Across 1,796 lung or respiratory *P. aeruginosa* genomes, amino-acid catabolic pathways were 97.4% conserved, and proline utilization was complete in 97% of lung isolates. [^cf_formulation_design]
- Lung *P. aeruginosa* showed pathway losses for sorbitol (-0.165), mannitol (-0.204), and gluconate (-0.185), consistent with metabolic streamlining toward amino-acid dependence. [^cf_formulation_design]
- The amino-acid target set was invariant across virulence backgrounds: GapMind score differences between ExoU+ and ExoS+ isolates were less than 0.03, with zero FDR-significant pathways. [^cf_formulation_design]
- Among 291 cystic-fibrosis genomes, 94% were ExoS+ and 5% were ExoU+. [^cf_formulation_design]
- Among 643 annotated PROTECT genomes, 304 (47%) were PAO1-like, 48 (7%) were PA14-like, and 291 (45%) were intermediate; among classifiable isolates, 86% were PAO1-like. [^cf_formulation_design]
- The PROTECT isolates were distributed across broader lung-*P. aeruginosa* diversity in a Pfam-based tree of 165 genomes rather than clustering in one lineage. [^cf_formulation_design]
- The study identified metabolic competition as a real but incomplete mechanism for inhibiting PA14: metabolic overlap with PA14 predicted planktonic inhibition across 142 isolates with correlation r = 0.384 and p = 2.3×10⁻⁶, while approximately 73% of inhibition variance remained unexplained by metabolism alone. [^cf_formulation_design]
- Adding genus-level taxonomy increased the metabolic model from R² = 0.274 to R² = 0.360, while five-fold cross-validation yielded CV R² = 0.145 ± 0.142. [^cf_formulation_design]
- PA14 outgrew the average commensal on every one of the 22 tested substrates, and no tested amino acid or simple sugar provided a clear commensal growth advantage; the most selective substrates had commensal-to-PA14 ratios of only 0.77–0.96. [^cf_formulation_design]
- Genomic comparisons identified myoinositol, xylitol, xylose, arabinose, fucose, and rhamnose as pathways complete in at least one core commensal species but absent or nearly absent in PA14; PA pathway completeness was 0% for myoinositol, xylitol, xylose, and arabinose, and 1% for fucose and rhamnose. [^cf_formulation_design]
- The source report proposed testing PAO1 and 3–5 mucoid clinical *P. aeruginosa* isolates because PA14-based inhibition measurements had not been validated against PAO1 or ExoS+ clinical strains. [^cf_formulation_design]
- The report notes that the inhibition assays were planktonic, whereas *P. aeruginosa* in cystic-fibrosis lungs primarily occupies structured biofilms. [^cf_formulation_design]

## Cross-study metabolic, ecological, and literature evidence

A separate seven-organism GapMind pilot found that *P. aeruginosa* strain PS had 18/18 amino-acid biosynthesis pathways complete (100%), with 745 GapMind predictions. This **supports** the broader evidence for substantial amino-acid metabolic capacity, while **refining** it by distinguishing biosynthetic completeness from the lung-isolate study’s amino-acid catabolic conservation. [^essential_metabolome]

The result is computational and limited to a seven-organism pilot, so it does not establish that these pathways are essential for viability or that all *P. aeruginosa* strains share the result. [^essential_metabolome]

A larger GapMind analysis of 12,732 genomes across 433 *Pseudomonas* species clades **supports** the formulation study’s evidence for carbon-use streamlining: the *P. aeruginosa* group had substantially less complete xylose, arabinose, myo-inositol, mannitol, and sorbitol pathways than the *P. fluorescens/putida* group, while amino-acid and core organic-acid pathways remained near-universal. [^pseudomonas_carbon_ecology] The same analysis **refines** the host-associated interpretation by showing that the dominant carbon-profile separation is between *Pseudomonas* s.s. and *Pseudomonas_E*, rather than a clean lifestyle separation within *Pseudomonas_E*. [^pseudomonas_carbon_ecology] Carbon profiles nevertheless retained a modest ecological signal among free-living and plant-associated species: a 999-permutation test gave p = 0.006, but a four-class Random Forest reached balanced accuracy of 0.408 +/- 0.169 versus a 0.250 chance baseline. [^pseudomonas_carbon_ecology]

The lignin-enrichment experiment **supports** the condition-specific-fitness evidence: *Pseudomonas* increased from less than 0.1% in the base community to 39.3% after one lignin-enrichment round and reached 23–53% across enriched conditions, but fell from 39.3% to 23.0% when labile carbon was added. [^lignin_community_enrichment] This community-level response **refines** the metabolic-competition claims by showing that *Pseudomonas* enrichment depends on the carbon regime; the study inferred lignin association from taxonomy rather than directly measuring pathway genes. [^lignin_community_enrichment]

PaperBLAST lists *P. aeruginosa* PAO1 as the third-leading bacterium by literature coverage, with **5,928** papers. This **supports** its status as a model organism and **refines** the formulation study’s recommendation to test PAO1 by showing that PAO1 is prominent in the literature, while not establishing that it represents cystic-fibrosis clinical diversity. [^paperblast_explorer]

## Related pages

This organism is the target of the protective-community strategy described in [cf_formulation_design__REPORT](../summaries/cf_formulation_design__REPORT.md). [^cf_formulation_design]

The seven-organism pathway analysis is summarized in [essential_metabolome__REPORT](../summaries/essential_metabolome__REPORT.md). [^essential_metabolome]

The comparative *Pseudomonas* carbon-ecology analysis is summarized in [pseudomonas_carbon_ecology__REPORT](../summaries/pseudomonas_carbon_ecology__REPORT.md). [^pseudomonas_carbon_ecology]

The lignin-community experiment is summarized in [lignin_community_enrichment__REPORT](../summaries/lignin_community_enrichment__REPORT.md). [^lignin_community_enrichment]

The PaperBLAST literature-coverage analysis is summarized in [paperblast_explorer__REPORT](../summaries/paperblast_explorer__REPORT.md). [^paperblast_explorer]

The findings relate to [condition-specific-fitness](../concepts/condition-specific-fitness.md) through substrate-specific growth, inhibition, lung adaptation, and carbon-regime-dependent community enrichment. [^cf_formulation_design][^lignin_community_enrichment]

They relate to [ecotype-environment-gene-content](../concepts/ecotype-environment-gene-content.md) through subgenus-associated carbon pathway profiles and the limited environment signal among free-living species. [^pseudomonas_carbon_ecology]

They relate to [environment-embedding-geography](../concepts/environment-embedding-geography.md) through PCA, permutation testing, and classification of isolation environments from carbon-pathway profiles. [^pseudomonas_carbon_ecology]

They relate to [multi-omics-integration](../concepts/multi-omics-integration.md) through combined inhibition, utilization, kinetics, metagenomics, metatranscriptomics, pangenome evidence, and paired bacterial 16S and fungal ITS community profiling. [^cf_formulation_design][^lignin_community_enrichment]

They relate to [pangenome-integration](../concepts/pangenome-integration.md) through comparisons of 1,796 lung or respiratory genomes and commensal pangenomes, and the 12,732-genome *Pseudomonas* carbon-pathway matrix; the lignin study proposes mapping enriched *Pseudomonas* and other genera to gene annotations in [kbase_ke_pangenome](kbase-ke-pangenome.md). [^cf_formulation_design][^pseudomonas_carbon_ecology][^lignin_community_enrichment]

They relate to [metabolic-model-gapfilling](../concepts/metabolic-model-gapfilling.md) through GapMind comparisons of pathway completeness between PA14 and candidate commensals, the PS pilot result, and standardized carbon-pathway predictions. [^cf_formulation_design][^essential_metabolome][^pseudomonas_carbon_ecology]

They relate to [gene-function-acquisition-depth](../concepts/gene-function-acquisition-depth.md) because PaperBLAST quantifies the concentration of functional literature on organisms and protein families, including the prominent but potentially nonrepresentative coverage of PAO1. [^paperblast_explorer]

[^cf_formulation_design]: [cf formulation design](../summaries/cf_formulation_design__REPORT.md)
[^essential_metabolome]: [essential metabolome](../summaries/essential_metabolome__REPORT.md)
[^pseudomonas_carbon_ecology]: [pseudomonas carbon ecology](../summaries/pseudomonas_carbon_ecology__REPORT.md)
[^lignin_community_enrichment]: [lignin community enrichment](../summaries/lignin_community_enrichment__REPORT.md)
[^paperblast_explorer]: [paperblast explorer](../summaries/paperblast_explorer__REPORT.md)
