---
type: "Organism"
description: "The species Salmonella enterica, including serovar Typhimurium LT2, covering its large almost entirely accessory AMR repertoire and its role as a modeled Proteobacterium."
sources: ["summaries/amr_environmental_resistome__REPORT.md", "summaries/amr_pangenome_atlas__REPORT.md", "summaries/amr_strain_variation__REPORT.md", "summaries/metabolic_capability_dependency__REPORT.md", "summaries/plant_microbiome_ecotypes__REPORT.md", "summaries/thermodynamic_impact__REPORT.md"]
aliases: ["Salmonella enterica LT2", "Salmonella enterica serovar Typhimurium LT2"]
---
# Salmonella enterica

Salmonella enterica has 836 AMR (antimicrobial resistance) clusters across 10,097 genomes, and 825 of them (99%) are accessory. [src: amr_environmental_resistome] Its LT2 model is listed as a Proteobacterium with a GramNeg template. [src: thermodynamic_impact]

## Key facts

- The AMR environmental resistome report counts 11 core clusters and 825 (99%) accessory clusters. Host-associated (31%) is the dominant environment. [src: amr_environmental_resistome]
- In the bacterial atlas, Salmonella has 198 AMR clusters per species, second among genera after Klebsiella (206). [src: amr_pangenome_atlas]
- The LT2 model is listed with 1,306 genes, 1,683 reactions, and growth 0.5625. [src: thermodynamic_impact]

## AMR and environment

Case-study UMAP (uniform manifold approximation and projection) plots for Klebsiella pneumoniae, Staphylococcus aureus and S. enterica show visible environmental structuring of AMR ecotypes. The report notes that its statistical test is underpowered with current metadata. [src: amr_strain_variation] See [[concepts/amr-ecotypes-and-environmental-association]] and [[concepts/environmental-and-clinical-distribution-of-antimicrobial-resistance]].

## Metabolic ecotypes

Metabolic clustering of 11,396 S. enterica genomes gave 6 clusters with silhouette 0.894. [src: metabolic_capability_dependency] The report calls this its strongest ecotype structure. [src: metabolic_capability_dependency] Clusters correlated significantly with isolation environment (χ²=1570.2, df=25, p<0.0001). [src: metabolic_capability_dependency] They correlated strongly with clinical, food and environmental isolation sources. [src: metabolic_capability_dependency] The report relates this to the established epidemiological serovars of Salmonella. It also calls it consistent with Van Rossum et al. (2020), who highlighted strain-level metabolic differentiation in human microbiome species. [src: metabolic_capability_dependency] See [[concepts/within-species-metabolic-ecotypes-from-pathway-variation]].

## Negative control for plant association

In the plant microbiome report, negative controls (NB08) classified non-plant Escherichia, Salmonella and Clostridioides as 100% dual-nature. [src: plant_microbiome_ecotypes] The Phase 1 91-marker panel caused this. It included ubiquitous bacterial functions (flagella, chemotaxis, T6SS (type VI secretion system), biofilm, quorum sensing, T2SS) that classified even Escherichia and Salmonella as 100% dual-nature. [src: plant_microbiome_ecotypes] With the refined marker panel, Salmonella negative controls were 0% PGP-only. [src: plant_microbiome_ecotypes] See [[concepts/dual-nature-plant-associated-bacteria-and-the-validity-of-marker-based-cohorts]].

## Thermodynamic flux modelling

The TMFA (thermodynamics-based metabolic flux analysis) impact table reports for S. enterica 1,683 reactions, of which 1,153 were constrained. It lists 20 flux-changed reactions (percentage column: 1.19), 3 newly blocked, 13 newly active and 4 reversed, with 10 Marvin-versus-OPAM2 differences. [src: thermodynamic_impact] See [[concepts/effect-of-pka-source-on-flux-predictions-across-diverse-organisms]].
