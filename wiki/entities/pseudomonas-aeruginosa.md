---
type: "Organism"
description: "Opportunistic pathogen in which efflux-pump costs from PMF drain are compensated by metabolic rewiring."
sources: ["summaries/amr_cofitness_networks__REPORT.md", "summaries/amr_fitness_cost__REPORT.md", "summaries/cf_formulation_design__REPORT.md", "summaries/essential_metabolome__REPORT.md", "summaries/pseudomonas_carbon_ecology__REPORT.md"]
aliases: ["P. aeruginosa", "PA", "PS"]
---
# Pseudomonas aeruginosa

Pseudomonas aeruginosa (also P. aeruginosa, PA, PS) is an opportunistic pathogen. Across the cited reports, its efflux-pump costs come from proton motive force (PMF) drain and are compensated by metabolic rewiring. [src: amr_fitness_cost] In cystic fibrosis (CF) lungs it keeps amino acid catabolism and loses sugar pathways. [src: cf_formulation_design, pseudomonas_carbon_ecology]

## Key facts

- Efflux-pump costs in P. aeruginosa are metabolic (proton motive force drain) and rapidly compensated through metabolic rewiring, per Olivares Pacheco & Alvarez (2017) as cited by the report. [src: amr_fitness_cost] See [[entities/efflux-pumps]] and [[concepts/fitness-cost-of-antimicrobial-resistance-genes]].
- In the GapMind analysis, strain PS (genome GCF_000006765.1) has 745 predictions and is present in the collection. [src: essential_metabolome] It has 18/18 amino acid pathways complete (100%). [src: essential_metabolome]
- The genome is 6.58 Mb with 6,177 CDS. This is 2.5–3× larger than the formulation commensal genomes of 2.1–2.7 Mb and 2,200–3,000 CDS. [src: cf_formulation_design]
- An efflux pump in Pseudomonas shares more cofitness partners with a beta-lactamase in the same Pseudomonas than with an efflux pump in Shewanella. [src: amr_cofitness_networks] See [[concepts/organism-specific-versus-mechanism-specific-wiring-of-amr-support-networks]].

## Role in cystic fibrosis

Chronic P. aeruginosa infection is described as the primary driver of lung function decline in CF. [src: cf_formulation_design] It chronically colonizes the airways of most CF patients by early adulthood. [src: cf_formulation_design] Once established, it switches to amino acid catabolism as its primary carbon source, forms biofilms and becomes increasingly antibiotic-resistant. [src: cf_formulation_design] See [[entities/cystic-fibrosis-sputum]].

Patient metatranscriptomics showed PA downregulating 170 of 207 measured pathways during acute exacerbation. [src: cf_formulation_design]

## Metabolic streamlining in the lung

Lung genomes lose sugar utilization pathways (sorbitol, mannitol, gluconate). Amino acid catabolism stays invariant, so the report calls the competitive-exclusion targets evolutionarily stable. [src: cf_formulation_design] Across 1,796 lung PA genomes, amino acid catabolic pathways are 97.4% conserved in mean completeness. [src: cf_formulation_design] See [[concepts/pathogen-metabolic-adaptation-in-the-lung-and-stability-of-competition-targets]].

The species-level comparison with the P. fluorescens group points the same way:

- The P. aeruginosa group shows near-complete loss of xylose, arabinose and myo-inositol catabolism (0% vs. 59-74% in the P. fluorescens group). [src: pseudomonas_carbon_ecology]
- It also has dramatic reductions in ribose, galacturonate, mannitol and sorbitol pathways. [src: pseudomonas_carbon_ecology]
- Arginine, histidine, serine and glutamate pathways remain >99.5% complete. [src: pseudomonas_carbon_ecology]
- The report finds these sugar losses conserved at the species level, not strain-specific. It contrasts this with the mosaic genome with strain-specific regions of genomic plasticity described by Mathee et al. (2008). [src: pseudomonas_carbon_ecology]

The report cites several studies as context:

- La Rosa et al. (2018) found convergent loss of carbon catabolism with retained amino acid utilization in CF lungs. [src: pseudomonas_carbon_ecology]
- Palmer et al. (2007) showed CF sputum is dominated by amino acids, especially aromatic amino acids, as carbon sources. [src: pseudomonas_carbon_ecology]
- Flynn et al. (2016) showed reliance on amino acids and short-chain fatty acids from anaerobic mucin-fermenting bacteria. [src: pseudomonas_carbon_ecology]
- Rossi et al. (2021) documented progressive loss of metabolic versatility in chronic infection. [src: pseudomonas_carbon_ecology]

See [[concepts/host-adaptation-pathway-loss-in-pseudomonas-carbon-catabolism]].

## Genome collections and virulence

The PA pangenome analysis included 6,760 genomes, 5,199 with metadata, of which 1,796 were from lung/respiratory or CF sources. [src: cf_formulation_design] The virulence-distribution analysis covers the same 6,760 genomes, with environmental metadata for 4,769. [src: cf_formulation_design] The PROTECT collection includes 655 P. aeruginosa isolates. [src: cf_formulation_design] See [[entities/protect-genome-depot]].

## Caveats

- P. aeruginosa makes up 53% of all genomes (6,760/12,732) because of its clinical importance. Many environmental species have <10 sequenced genomes, which affects the power of species-level comparisons. [src: pseudomonas_carbon_ecology] See [[concepts/clinical-and-human-associated-sampling-bias-in-genome-collections]].
- The 28 Fitness Browser organisms are lab-adapted, phylogenetically biased (many Pseudomonas) and limited in ecological diversity. [src: amr_cofitness_networks] See [[entities/fitness-browser]].
