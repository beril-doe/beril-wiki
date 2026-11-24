---
type: "Organism"
description: "Enterobacterial genus with the highest AMR cluster count per species in the atlas."
sources: ["summaries/amr_pangenome_atlas__REPORT.md", "summaries/microbeatlas_metal_ecology__REPORT.md", "summaries/snipe_defense_system__REPORT.md"]
aliases: ["Klebsiella pneumoniae"]
---
# Klebsiella

Klebsiella (also known as Klebsiella pneumoniae) is an enterobacterial genus. It has the highest count of antimicrobial resistance (AMR) clusters per species in the atlas. [src: amr_pangenome_atlas] Other reports add evidence on metal resistance and on the phage defense system SNIPE. These come from single reports, and the SNIPE clinical relevance is a proposal.

## Key facts

- Klebsiella leads bacterial genera with 206 AMR clusters per species, followed by Salmonella (198), Citrobacter (134) and Enterobacter (93). [src: amr_pangenome_atlas] See [[summaries/amr_pangenome_atlas__REPORT]].
- The metal-ecology report names Klebsiella (Ag, As, Hg, Te) and Enterococcus (Ag, As, Cd, Cu, Hg, Te) as the broadest multi-metal resisters among its candidates. [src: microbeatlas_metal_ecology]
- That report ranks Klebsiella operational taxonomic unit (OTU) `97_56843` at priority 1 for microcosm experiments. Its Levins' B is 0.947, its metal types value is 3.5, and Ag or Te stress is recommended. [src: microbeatlas_metal_ecology] See [[summaries/microbeatlas_metal_ecology__REPORT]].

## SNIPE and phage defense

SNIPE was detected in Klebsiella, which the report calls a key phage therapy target. [src: snipe_defense_system] The report proposes that SNIPE could affect phage therapy efficacy in this pathogen. [src: snipe_defense_system] See [[entities/snipe]] and [[summaries/snipe_defense_system__REPORT]].

In [[entities/phagefoundry]], the Klebsiella search found DUF4041: 1, GIY-YIG: 1, nuclease: 98, restriction: 42 and abortive infection: 2. [src: snipe_defense_system] DUF4041 (SNIPE) is represented by 1 description and 3 proteins of 558 aa each. Acinetobacter, Pseudomonas aeruginosa and Pseudomonas viridiflava each have 0. [src: snipe_defense_system]

### Mannose PTS link

PhageFoundry Klebsiella has 28 proteins with mannose PTS IID (ManZ) eggNOG annotations. [src: snipe_defense_system] It has 1 protein with a mannose PTS IIA (ManX) eggNOG annotation. [src: snipe_defense_system] Klebsiella is the only PhageFoundry species with both SNIPE and the PF00358 ManX-family PTS domain by exact Pfam accession. [src: snipe_defense_system] See [[entities/manxyz-mannose-phosphotransferase-system]].

### Limits

No Klebsiella strain in the Fitness Browser carries ManXYZ by gene name. [src: snipe_defense_system] Klebsiella-specific SNIPE or ManYZ fitness data would need new mutant libraries in natural SNIPE-carrying strains such as K. pneumoniae NCTC9140 or HS11286. [src: snipe_defense_system] This is the kind of gap described in [[concepts/fitness-data-coverage-gaps-for-defense-genes]].
