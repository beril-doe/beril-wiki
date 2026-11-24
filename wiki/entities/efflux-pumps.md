---
type: "Gene_Or_Pathway"
description: "Efflux-type AMR genes (including the multidrug pump emrB, KO K03446), their support-network enrichments, fitness costs and association with environmental metal responses."
sources: ["summaries/amr_cofitness_networks__REPORT.md", "summaries/amr_environmental_resistome__REPORT.md", "summaries/amr_fitness_cost__REPORT.md", "summaries/amr_pangenome_atlas__REPORT.md", "summaries/comprehensive_metal_ecology__REPORT.md", "summaries/discoveries.md"]
aliases: ["K03446", "efflux", "efflux AMR genes", "efflux genes", "emrB"]
---
# Efflux pumps

This page covers efflux-type AMR genes, including the multidrug pump emrB (KO K03446), their support-network enrichments, fitness costs and association with environmental metal responses. Efflux genes are enriched in clinical and gut bacteria, and they show a broad-spectrum fitness profile. [src: amr_environmental_resistome, amr_fitness_cost]

## Distribution across environments

Efflux makes up a larger share of AMR in host-associated and clinical species than in soil or aquatic species. The fractions are 6.1% in clinical, 7.0% in human gut, 3.7% in host-associated, 2.0% in soil, 1.1% in aquatic and 2.7% in other environmental species (η² = 0.055). [src: amr_environmental_resistome] The difference by environment is significant for bacterial species (Kruskal-Wallis, KW, H=768.0, p=9.8×10⁻¹⁶⁴, η²=0.055). [src: amr_environmental_resistome] The assembled resistome holds 5,224 efflux gene clusters. [src: amr_environmental_resistome] A separate summary states that efflux is 21% of AMR in human gut species but 1% in aquatic species (η²=0.127). [src: discoveries] These figures differ between claims (7.0% versus 21% for gut). The claims do not explain the gap, so I report each as given. See [[concepts/environment-dependent-resistance-mechanism-composition]].

## Conservation

In the pangenome AMR census, efflux accounts for 14,338 hits (17.3%), of which 30.9% are core. [src: amr_pangenome_atlas] Intrinsic pumps such as emhABC are >95% core, while acquired efflux genes are accessory. [src: amr_pangenome_atlas] The fitness-cost report separately states that efflux genes are 13% accessory in its AMR conservation analysis. [src: amr_fitness_cost] The claims do not say how this figure relates to the 30.9% core figure from the census, so I state each on its own. The fitness-cost report proposes that efflux systems, often chromosomally encoded as part of the general stress response, are maintained as core genes. [src: amr_fitness_cost] See [[concepts/intrinsic-versus-acquired-resistance-gene-conservation]].

## Fitness behaviour

Efflux genes show a stronger antibiotic-dependent fitness flip than enzymatic inactivation genes: +0.094 versus −0.001 (Mann-Whitney U, MWU, p = 0.007). [src: amr_fitness_cost, discoveries] The report reads this as broad-spectrum pumps becoming important under any antibiotic. Narrow-spectrum enzymes flip only under their matching antibiotic. [src: amr_fitness_cost] The report describes beta-lactamases as examples of such narrow-spectrum enzymes. [src: amr_fitness_cost] It proposes separating narrow-spectrum drug pumps from general RND systems such as AcrAB-TolC. It also proposes testing whether constitutively expressed efflux systems cost less. [src: amr_fitness_cost] Both reports cite work in *P. aeruginosa* showing that efflux-pump costs are metabolic, from proton motive force drain, and are compensated by metabolic rewiring. [src: amr_cofitness_networks, amr_fitness_cost] See [[concepts/antibiotic-dependent-fitness-flip-of-resistance-genes]], [[concepts/fitness-cost-of-antimicrobial-resistance-genes]], [[entities/proton-motive-force]] and [[entities/pseudomonas-aeruginosa]].

## Cofitness support networks

Efflux AMR genes show the strongest amino acid biosynthesis enrichment among mechanisms, with histidine in 6 organisms and tryptophan in 5. [src: amr_cofitness_networks] In the mechanism-specific Gene Ontology (GO) analysis, 212 of 9,244 tests are significant at a false discovery rate (FDR) below 0.05. The top signal is efflux histidine biosynthesis in 6 organisms. [src: amr_cofitness_networks] Null result: module size does not differ between efflux and enzymatic mechanisms (efflux = enzymatic = 48, MWU p = 0.91). [src: amr_cofitness_networks] See [[entities/histidine-and-tryptophan-biosynthesis]] and [[concepts/functional-composition-of-antimicrobial-resistance-cofitness-support-networks]].

## Metal associations

In an exploratory per-KO driver analysis, emrB (K03446) has 11 significant responses (p < 0.05). Its strongest is Ni (GeoROC), β = 8.45, t = 5.01, p = 6.0×10⁻⁷. [src: comprehensive_metal_ecology] The report calls emrB a Cu/Tl transporter encoding a multi-drug efflux pump with broad substrate range. [src: comprehensive_metal_ecology] It suggests the diverse metal associations likely reflect broad RND/MFS efflux chemical selectivity rather than primary metal resistance. It adds that emrB prevalence may track metal-stress environments non-specifically. [src: comprehensive_metal_ecology] In the global MGnify metagenome assembled genome (MAG) niche-breadth analysis, efflux pumps show a significant positive association (β = +0.018, q = 0.016). This is exploratory. [src: comprehensive_metal_ecology] See [[concepts/environmental-drivers-of-genus-niche-breadth-and-metal-gene-density]].

## Open Directions

- Separate narrow-spectrum drug pumps from general RND systems and compare their fitness flips.
- Test whether constitutive efflux systems cost less than inducible ones.
- Reconcile the gut efflux fractions (7.0% versus 21%) by checking the denominators of each analysis.
- Reconcile the 30.9% core figure with the 13% accessory figure by comparing populations and definitions.
- Test emrB metal associations against non-metal stress variables to check for non-specific tracking.
