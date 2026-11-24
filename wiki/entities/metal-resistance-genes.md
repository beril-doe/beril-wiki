---
type: "Gene_Or_Pathway"
description: "AMR mechanism class that dominates soil and aquatic resistomes and is largely accessory."
sources: ["summaries/amr_cofitness_networks__REPORT.md", "summaries/amr_environmental_resistome__REPORT.md", "summaries/amr_fitness_cost__REPORT.md", "summaries/amr_pangenome_atlas__REPORT.md", "summaries/discoveries.md", "summaries/microbeatlas_metal_ecology__REPORT.md"]
aliases: ["metal resistance"]
---
# Metal resistance genes

Metal resistance genes are the antimicrobial resistance (AMR) mechanism class that dominates soil and aquatic resistomes, and they are largely accessory. [src: amr_environmental_resistome, amr_fitness_cost] The evidence comes from several projects. It is strongest for the environment pattern and the accessory fraction. The cause is interpretation by the reports, not a tested result. [src: amr_environmental_resistome]

## Key facts

- The assembled resistome in amr_environmental_resistome includes 22,223 metal-resistance gene clusters. Other mechanism classes are enzymatic inactivation (26,220), target modification (11,067) and efflux (5,224). [src: amr_environmental_resistome]
- Metal resistance is the AMR class with the largest environment effect. It makes up 45% of AMR in aquatic species, 44% in soil species and 6% in human gut species (η² = 0.107). [src: amr_environmental_resistome, discoveries]
- Metal resistance varies by environment across bacterial species (Kruskal-Wallis (KW) H=1498.4, p~0, η²=0.107). [src: amr_environmental_resistome] See [[entities/kruskal-wallis-test-with-eta-squared-effect-size]].

## Environment pattern

Metal resistance peaks in soil and aquatic environments and is low in the human gut. [src: amr_environmental_resistome] The fractions of AMR that is metal resistance are:

- Clinical: 19.7% [src: amr_environmental_resistome]
- Human gut: 6.1% [src: amr_environmental_resistome]
- Host-associated: 12.7% [src: amr_environmental_resistome]
- Soil: 44.0% [src: amr_environmental_resistome]
- Aquatic: 45.0% [src: amr_environmental_resistome]
- Other environmental: 24.9% [src: amr_environmental_resistome]

The report reads this as natural heavy-metal exposure in soil and aquatic habitats. It reads the clinical and gut preference for target modification and efflux as antibiotic selection pressure. [src: amr_environmental_resistome] It also suggests that these soil and aquatic genes are more often core, which it takes to indicate ancient adaptation. [src: amr_environmental_resistome] See [[concepts/environment-dependent-resistance-mechanism-composition]].

## Conservation and fitness cost

Mechanism predicts conservation. Metal resistance genes are 44% accessory, against 13% for efflux and 16% for enzymatic inactivation, which are overwhelmingly core. [src: amr_fitness_cost] amr_cofitness_networks cites this result from amr_fitness_cost. [src: amr_cofitness_networks]

Mechanism did not significantly predict fitness cost. The Kruskal-Wallis test across efflux (N=254), enzymatic inactivation (N=304), metal resistance (N=144) and unknown (N=74) groups was not significant (H = 0.65, p = 0.89). [src: amr_fitness_cost] Antibiotic-resistance and metal-resistance genes also showed no cost difference (Mann-Whitney U p = 0.87). [src: amr_fitness_cost] The report suggests that conservation reflects how and when genes were acquired rather than how much they cost. [src: amr_fitness_cost] It notes that metal-resistance operons are frequently carried on mobile elements and stay accessory, yet carry the same modest cost as efflux systems once established. [src: amr_fitness_cost] The report proposes cross-referencing the 144 metal resistance genes that have fitness data against metal_fitness_atlas. [src: amr_fitness_cost] See [[concepts/fitness-cost-of-antimicrobial-resistance-genes]] and [[concepts/intrinsic-versus-acquired-resistance-gene-conservation]].

## Gene families and annotation

Mercury genes (merA, merP, merC, merE, merF, merR, merD, merB, merT) account for ~15,000 hits, or 18% of all AMR annotations in amr_pangenome_atlas. [src: amr_pangenome_atlas] Arsenic genes (arsD, arsN1, arsN2, arsC) add ~6,000 hits. [src: amr_pangenome_atlas] The clusters of orthologous groups (COG) category P (inorganic ion transport) is 1.93x enriched in AMR genes (10.7% versus 5.6%), reflecting the mer and ars families. [src: amr_pangenome_atlas] The report reads this as heavy-metal and antibiotic resistance being genomically intertwined and often co-located on mobile elements. [src: amr_pangenome_atlas] See [[entities/mercury-resistance-mer-genes]] and [[entities/arsenic-resistance-ars-genes]].

microbeatlas_metal_ecology describes bacterial metal-resistance genes for mercury, arsenic, copper, zinc, cadmium, chromium and nickel. Many sit on mobile genetic elements and are frequently transferred among taxa by horizontal gene transfer (HGT). [src: microbeatlas_metal_ecology]

## Phylogenetic signal and networks

Across 606 bacterial genera, Pagel's λ is 0.441 for core AMR fraction (p = 1.8×10⁻⁸, likelihood ratio test (LRT)). It is 0.335 for metal type diversity (p = 1.1×10⁻²³, LRT). [src: microbeatlas_metal_ecology] See [[concepts/phylogenetic-signal-of-gene-content-and-traits]].

In amr_cofitness_networks, metal resistance genes show stronger chemotaxis enrichment in 4 organisms. [src: amr_cofitness_networks] See [[concepts/functional-composition-of-antimicrobial-resistance-cofitness-support-networks]].

## Open Directions

- Test whether genes costly under standard conditions protect against metal stress, using the 144 metal resistance genes with fitness data and metal_fitness_atlas.
