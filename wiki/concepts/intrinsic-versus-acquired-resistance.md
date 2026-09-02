---
type: "Concept"
description: "Intrinsic resistance is usually core; acquired resistance is often accessory and mobile."
sources: ["summaries/amr_pangenome_atlas__REPORT.md"]
---
# Intrinsic and Acquired Resistance Occupy Different Genomic Compartments

## Core distinction

The [[summaries/amr_pangenome_atlas__REPORT]] supports a genomic distinction between intrinsic resistance—resistance functions maintained as part of a lineage's conserved genome—and acquired resistance—resistance genes found in accessory, minority, or singleton compartments. [src: amr_pangenome_atlas] This distinction refines [[concepts/intrinsic-versus-acquired-resistance]] by tying resistance mode to pangenome conservation rather than to gene name alone. [src: amr_pangenome_atlas]

## Evidence from pan-bacterial conservation

Across 27,690 pangenome species, the analysis identified 83,008 AMRFinderPlus hits spanning 82,908 distinct gene clusters, 1,939 AMR gene families, 2,079 AMR products, and 14,723 species. [src: amr_pangenome_atlas] Only 30.3% of AMR genes were core, compared with 46.8% for the pangenome baseline, corresponding to an odds ratio of 0.49, chi-squared=23,117, and p≈0. [src: amr_pangenome_atlas] The auxiliary genome was 2.2x enriched for AMR, with 33.6% of AMR genes classified as auxiliary compared with 15.3% for the baseline. [src: amr_pangenome_atlas]

A paired comparison of 4,252 species containing at least 5 AMR clusters found that 63.7% had AMR less core than their species baseline, with Wilcoxon p=1.1e-130 and a mean difference of -0.102. [src: amr_pangenome_atlas] This directly supports the claim that AMR is disproportionately allocated to accessory genomic compartments across species, rather than simply reflecting each species' general pangenome structure. [src: amr_pangenome_atlas]

## Gene-class contrasts

The conservation pattern differed sharply among AMR gene classes. [src: amr_pangenome_atlas] Beta-lactamases were 54.9% core and significantly enriched relative to the species baseline, with p=7.7e-74, whereas regulatory genes were only 6.5% core. [src: amr_pangenome_atlas] The acquired-resistance examples blaTEM, tet(C), and ant(2'')-Ia were each 0% core in the analyzed pangenomes. [src: amr_pangenome_atlas] Intrinsic efflux pumps such as emhABC were >95% core, while acquired efflux genes were accessory. [src: amr_pangenome_atlas]

These results support an intrinsic-acquired dichotomy: vertically inherited intrinsic resistance genes can be stable core residents, whereas acquired resistance genes are often present in a minority of genomes, accessory clusters, or singleton clusters. [src: amr_pangenome_atlas] The dichotomy is a population-genomic pattern, not an absolute classification rule, because the same broad mechanism category can contain both highly conserved and accessory genes. [src: amr_pangenome_atlas]

## Environmental context

Clinical species carried 10.6 AMR clusters per species, compared with 4.6 for Soil/Terrestrial species, 3.9 for Aquatic species, and 3.0 for Animal species; the difference was significant with Kruskal-Wallis H=440 and p=7.0e-93. [src: amr_pangenome_atlas] Clinical AMR was less core at 30.8% than soil AMR at 58.1% or plant AMR at 63.1%. [src: amr_pangenome_atlas] This pattern supports the interpretation that clinical environments contain more acquired or mobile resistance, while environmental AMR in the analyzed data is more predominantly intrinsic. [src: amr_pangenome_atlas]

The environmental comparison was restricted to 7,838 of the 14,723 AMR-carrying species that received a non-Other/Unknown classification, because 46.8% of species remained in the Other/Unknown bin owing to sparse and inconsistent free-text isolation_source metadata. [src: amr_pangenome_atlas] Therefore, the clinical-environmental contrast supports a genomic-compartment hypothesis but does not establish that every environmental resistance gene is intrinsic or that every clinical resistance gene is acquired. [src: amr_pangenome_atlas]

Environmental diversity also predicted AMR count among 2,684 species with at least 3 genomes and AlphaEarth embeddings, with Spearman rho=0.466 and p=1.6e-144, while environmental diversity and AMR core fraction were negatively correlated with rho=-0.173 and p=1.8e-19. [src: amr_pangenome_atlas] Because AlphaEarth embeddings covered only 28% of genomes and were biased toward genomes with geographic metadata, these associations suggest a hypothesis about niche breadth and resistance accumulation rather than proving a causal route from environmental diversity to acquired resistance. [src: amr_pangenome_atlas]

## Functional and annotation implications

AMR clusters were enriched in defense and inorganic-ion transport functions: COG V (Defense mechanisms) was 7.05x enriched, representing 14.9% of AMR clusters versus 2.1% of the baseline, and COG P (Inorganic ion transport) was 1.93x enriched, representing 10.7% versus 5.6%. [src: amr_pangenome_atlas] COG means the Cluster of Orthologous Groups functional classification. [src: amr_pangenome_atlas] The five most abundant AMR gene families were bla with 6,115 hits, merA with 4,506, arsD with 2,611, merP with 2,222, and vanR with 1,929. [src: amr_pangenome_atlas]

The broad AMRFinderPlus Reference Gene Catalog included stress-response genes alongside classical antibiotic-resistance genes, with mercury-resistance families accounting for approximately 15,000 hits and 18% of all AMR annotations and arsenic-resistance families adding another approximately 6,000 hits. [src: amr_pangenome_atlas] Consequently, the core-versus-accessory distinction applies to the report's operational AMR catalog and should not be read as a measurement of antibiotic resistance alone. [src: amr_pangenome_atlas] This limitation connects the concept to [[concepts/environmental-resistome]] and [[concepts/environmental-resistome]]. [src: amr_pangenome_atlas]

Mechanism labels also remain partly uncertain because keyword matching against AMRFinderPlus product descriptions, rather than CARD Antibiotic Resistance Ontology terms, left 18,448 hits—22.2%—in the Other/Unclassified category; 24.0% of those hits were core. [src: amr_pangenome_atlas] A more systematic ontology mapping could change the assignment of particular genes to intrinsic or acquired mechanism classes without necessarily changing the observed genome-compartment pattern. [src: amr_pangenome_atlas]

## Fitness interpretation

The Fitness Browser cross-reference identified 178 AMR genes across 37 Fitness Browser organisms and 29,386 fitness measurements using a DIAMOND-based pangenome link table at 100% sequence identity. [src: amr_pangenome_atlas] AMR genes had a median fitness of -0.007 versus -0.012 for the non-AMR baseline, with Mann-Whitney p=3.7e-6; beta-lactamases had a median fitness of -0.001, while singleton AMR genes had a median of -0.019. [src: amr_pangenome_atlas] These measurements are consistent with well-integrated intrinsic resistance genes being less burdensome under the tested laboratory conditions, but they do not establish that recently acquired mobile resistance is cost-free in clinical pathogens. [src: amr_pangenome_atlas]

The source separately reports fitness data for 162 AMR genes in 36 Fitness Browser organisms and does not reconcile that count with the 178-gene, 37-organism analysis. [src: amr_pangenome_atlas] The 100% DIAMOND identity threshold is conservative and may miss closely related resistance variants, including alleles differing by a single synonymous substitution. [src: amr_pangenome_atlas] This limitation links the concept to [[concepts/antimicrobial-resistance-fitness-cost]] and [[concepts/condition-specific-fitness]]. [src: amr_pangenome_atlas]

## Relationship to broader pangenome interpretation

The evidence supports [[concepts/pangenome-integration]] by showing that AMR conservation classes, taxonomy, environmental metadata, functional annotations, and fitness measurements can be compared across a single pangenome collection. [src: amr_pangenome_atlas] It also qualifies interpretations of [[concepts/pangenome-conservation-fitness-decoupling]] because a gene's accessory status and its measured laboratory fitness effect are related dimensions, not interchangeable measures of evolutionary cost. [src: amr_pangenome_atlas]

## Open Directions

- Map AMR proteins to CARD ARO terms and re-estimate core, auxiliary, and singleton fractions by resistance mechanism; question: does ontology-based classification preserve the intrinsic-acquired compartment contrast after reducing the 22.2% Other/Unclassified category? [src: amr_pangenome_atlas]
- Infer AMR gene gain and loss rates from species phylogenies and gene-family distributions; question: do low-core AMR families show turnover rates consistent with repeated acquisition and loss? [src: amr_pangenome_atlas]
- Test co-localization of accessory AMR genes with genomic islands, insertion sequences, and integrons; question: are the least-conserved AMR genes physically associated with mobility features? [src: amr_pangenome_atlas]
- Extend Fitness Browser linking beyond 100% DIAMOND identity and measure fitness under antibiotic stress; question: do closely related acquired variants and mobile clinical resistance genes incur costs that are missed under the current laboratory and sequence-matching filters? [src: amr_pangenome_atlas]
- Use NMDC and MGnify environmental metagenomes with resolved isolation metadata; question: does the intrinsic-acquired genomic-compartment pattern persist in community-level environmental resistomes rather than genome databases alone? [src: amr_pangenome_atlas]
