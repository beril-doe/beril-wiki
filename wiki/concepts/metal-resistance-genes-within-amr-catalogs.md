---
type: "Concept"
description: "The contribution of mercury and arsenic resistance and other stress-response genes to AMR catalogs and the implications for interpreting AMR counts."
sources: ["summaries/amr_environmental_resistome__REPORT.md", "summaries/amr_fitness_cost__REPORT.md", "summaries/amr_pangenome_atlas__REPORT.md", "summaries/microbeatlas_metal_ecology__REPORT.md"]
---
# Metal resistance genes within AMR catalogs

The contribution of mercury and arsenic resistance and other stress-response genes to AMR catalogs and the implications for interpreting AMR counts.

## Literature Context

The candidate papers mostly address co-selection: the idea that metals maintain antibiotic resistance genes in the environment. A review of environmental co-selection says metal resistance genes are known to be genetically linked to antibiotic resistance genes, with plasmids, transposons and integrons involved in their assembly and transfer [PMID 38897736](https://pubmed.ncbi.nlm.nih.gov/38897736/). The same review warns that co-resistance is often suggested as the dominant mechanism but that interpretations are beset with correlational bias. It also says the molecular aspects are often not defined or quantified. Other reviews describe co-localization of antibiotic and metal resistance genes on shared mobile genetic elements in wastewater and aquatic settings [PMID 36805463](https://pubmed.ncbi.nlm.nih.gov/36805463/) [PMID 42162448](https://pubmed.ncbi.nlm.nih.gov/42162448/).

Empirical studies point the same way, but they are correlational or system-specific. In terrestrial subsurface soils, metagenomics showed widespread co-occurrence of ARGs and MRGs. Heavy metals shaped ARG profiles in soils with high metal contents but had no significant effect in soils with low contents [PMID 33858075](https://pubmed.ncbi.nlm.nih.gov/33858075/). In urban rivers in the UK and India, MRG, ARG and integron abundances tended to rise in high-metal environments, and network analysis linked MRGs and ARGs (r > 0.80, p < 0.05) [PMID 35491000](https://pubmed.ncbi.nlm.nih.gov/35491000/). In poultry farms, metals had a bigger effect on the ARG profile than detected antibiotics. Even so, bacterial composition and mobile elements explained more variance (21.9% and 12.4%) than metals (5.7%) [PMID 33049532](https://pubmed.ncbi.nlm.nih.gov/33049532/). A copper shock-loading experiment on drinking-water biofilter bacteria showed rapid co-selection within 6 h [PMID 29059628](https://pubmed.ncbi.nlm.nih.gov/29059628/). In manure composting, reducing metal bioavailability lowered ARGs and MGEs [PMID 41297266](https://pubmed.ncbi.nlm.nih.gov/41297266/). A review of biochar reaches a similar conclusion [PMID 35663734](https://pubmed.ncbi.nlm.nih.gov/35663734/). Not every selective pressure co-selects. Chlorination of wastewater effluent reduced ARGs and MGEs, and only six ARGs were potentially enriched [PMID 27192478](https://pubmed.ncbi.nlm.nih.gov/27192478/).

The corpus findings are consistent with this literature but differ in kind. The pangenome atlas reports that mercury genes account for about 15,000 hits (18% of AMR annotations) and arsenic genes add about 6,000. It also reports a 1.93x enrichment of COG category P. Those counts reflect the broad AMRFinderPlus definition of AMR, which includes stress-response genes. The environmental resistome project finds the metal share is 45% of aquatic AMR, 44% of soil AMR and 6% of human gut AMR. This fits the soil and river studies, where metal pressure is tied to resistance profiles [PMID 33858075](https://pubmed.ncbi.nlm.nih.gov/33858075/) [PMID 35491000](https://pubmed.ncbi.nlm.nih.gov/35491000/). The corpus measures catalog composition across genomes. It does not measure selection, so it extends the field by quantifying how much of an AMR count is metal-related. Its reading that metal and antibiotic resistance are co-located on mobile elements is a hypothesis, not an established result. The literature suggests caution about that reading [PMID 38897736](https://pubmed.ncbi.nlm.nih.gov/38897736/). The proposed co-localization analysis with IS elements and integrons would test it directly. The corpus has no counterpart to the experimental cross-resistance and co-regulation work, so that link remains untested here.

## Why catalogs contain metal genes

The AMRFinderPlus Reference Gene Catalog includes stress response genes, so the 83K hits in the pangenome atlas are not all antibiotic resistance. [src: amr_pangenome_atlas] The report ties the prominence of mer and ars families to this broad definition of AMR. [src: amr_pangenome_atlas] See [[entities/amrfinderplus]].

## Size of the contribution

Among the top five AMR gene families, merA (mercury reductase) has 4,506 hits, arsD (arsenic metallochaperone) has 2,611 and merP (mercury binding protein) has 2,222. [src: amr_pangenome_atlas] Mercury genes (merA, merP, merC, merE, merF, merR, merD, merB, merT) together account for ~15,000 hits, or 18% of all AMR annotations. [src: amr_pangenome_atlas] Arsenic genes (arsD, arsN1, arsN2, arsC) add ~6,000. [src: amr_pangenome_atlas] COG (clusters of orthologous groups) category P, inorganic ion transport, is 1.93x enriched in AMR genes (10.7% versus 5.6%). The report attributes this to the mercury and arsenic gene families. [src: amr_pangenome_atlas] A separate project's assembled AMR class distribution also lists mercury (27) and arsenic (22). [src: amr_fitness_cost] See [[entities/mercury-resistance-mer-genes]] and [[entities/arsenic-resistance-ars-genes]].

## Dependence on environment

The metal share varies strongly by environment. It is 45% of aquatic AMR, 44% of soil AMR and 6% of human gut AMR, the largest environment effect (η² = 0.107). [src: amr_environmental_resistome] By group, the fractions are 19.7% clinical, 6.1% human gut, 12.7% host-associated, 44.0% soil, 45.0% aquatic and 24.9% other environmental. [src: amr_environmental_resistome] The report interprets the soil and aquatic values as a response to natural heavy-metal exposure. [src: amr_environmental_resistome] See [[concepts/environment-dependent-resistance-mechanism-composition]].

## Interpretation

The pangenome atlas report reads the COG P enrichment as showing that heavy-metal and antibiotic resistance are genomically intertwined and often co-located on mobile elements. [src: amr_pangenome_atlas] The report proposes a co-localization analysis to test whether AMR genes cluster in genomic islands or co-localize with mobile element markers such as IS elements and integrons. [src: amr_pangenome_atlas] A separate metal-ecology project notes that its "other" metal category (17% of annotated clusters) holds metal-associated genes outside the 7 primary types and may include weaker hits. [src: microbeatlas_metal_ecology] See [[concepts/validity-of-curated-metal-gene-annotation]].

## Open Directions

- Recompute AMR prevalence per environment with metal and stress-response classes excluded, to show how much of the environment contrast is due to metal genes.
- Run the proposed co-localization analysis to test whether metal and antibiotic resistance genes really co-occur on mobile elements.
- Check whether removing the weaker hits in the "other" metal category changes the metal share.
