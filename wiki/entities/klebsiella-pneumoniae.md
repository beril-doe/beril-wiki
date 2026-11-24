---
type: "Organism"
description: "The species Klebsiella pneumoniae, including the reference strain HS11286, covering its accessory-dominated resistome and its use as a modeled organism; genus-wide Klebsiella statistics belong to the Klebsiella page."
sources: ["summaries/amr_environmental_resistome__REPORT.md", "summaries/amr_strain_variation__REPORT.md", "summaries/discoveries.md", "summaries/ecotype_env_reanalysis__REPORT.md", "summaries/metabolic_capability_dependency__REPORT.md", "summaries/thermodynamic_impact__REPORT.md"]
aliases: ["K. pneumoniae", "Klebsiella", "Klebsiella pneumoniae HS11286"]
---
# Klebsiella pneumoniae

This page covers the species Klebsiella pneumoniae, including the reference strain HS11286. Its antimicrobial resistance (AMR) gene content is almost entirely accessory: 1,115 AMR clusters, only 7 of them core. [src: amr_environmental_resistome, discoveries] The evidence is pangenome-scale counts in one dataset, a metabolic model of strain HS11286, and a few literature-based or proposed interpretations. Genus-wide statistics belong to the Klebsiella page.

## Key facts

- The species has 13,637 genomes, 1,115 AMR clusters, 7 core clusters and 1,108 accessory clusters (99%). Its dominant environment is Clinical (80%). [src: amr_environmental_resistome]
- 80% of its genomes in that dataset come from clinical sources. [src: amr_environmental_resistome]
- Among well-sampled pathogens (>2,500 genomes), it was the most open pangenome: 99.05% open, 0.95% core genes. [src: metabolic_capability_dependency] See [[entities/pangenome-openness]].

## Accessory-dominated resistome

The report interprets the nearly entirely accessory resistome as massive within-species AMR variation driven by horizontal gene transfer (HGT) in clinical settings. That is an interpretation, not a tested mechanism. [src: amr_environmental_resistome] The amr_strain_variation report cites Holt et al. 2015 for distinct lineages with different AMR and virulence profiles tied to different ecological niches. [src: amr_strain_variation] Related pages: [[concepts/within-species-variation-of-antimicrobial-resistance-gene-content]], [[concepts/amr-ecotypes-and-environmental-association]].

The environment reanalysis report states that Klebsiella and Enterococcus have global epidemiological patterns, with different lineages dominating different regions. [src: ecotype_env_reanalysis]

## Phage defense context

The PhageFoundry Klebsiella genome browser contains 1 DUF4041 annotation, representing 3 proteins at 558 aa, the same length as Escherichia coli [[entities/snipe]]. It also contains 4,619 PTS_EIIC (PF02378/ManY family) annotations. [src: discoveries] Klebsiella is the only PhageFoundry species with both SNIPE and the ManX-family PTS domain PF00358. [src: discoveries] The report proposes that SNIPE could affect phage therapy efficacy in this pathogen. [src: discoveries]

## Metabolic model

The HS11286 model is listed as Proteobacteria with a GramNeg template, 1,601 genes, 1,793 reactions and growth 0.5000. [src: thermodynamic_impact] In the thermodynamics-based metabolic flux analysis (TMFA) impact table, 1,243 of the 1,793 reactions were constrained. Six reactions changed flux (percentage column 0.33), with 0 newly blocked, 5 newly active and 1 reversed. Marvin and OPAM2 differed in 6 reactions. [src: thermodynamic_impact]

## Caveats

- The phylogenetic signal analysis in amr_strain_variation used average nucleotide identity (ANI) only for species with ≤500 genomes. It therefore excluded K. pneumoniae (14,240 genomes in that report) and Escherichia coli (15,388 genomes). [src: amr_strain_variation]
- K. pneumoniae was excluded from the environment reanalysis correlation data because gene cluster extraction exceeded Spark's maxResultSize. [src: ecotype_env_reanalysis]
- The genome count is 13,637 in one report and 14,240 in another. The claims do not explain the difference. [src: amr_environmental_resistome, amr_strain_variation]
