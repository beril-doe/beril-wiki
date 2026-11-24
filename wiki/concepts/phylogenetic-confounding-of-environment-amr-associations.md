---
type: "Concept"
description: "Whether environment–AMR associations survive control for taxonomy at phylum and family level, and what limits that control."
sources: ["summaries/amr_environmental_resistome__REPORT.md", "summaries/discoveries.md", "summaries/microbeatlas_metal_ecology__REPORT.md"]
---
# Phylogenetic confounding of environment-AMR associations

This page asks whether environment–antimicrobial resistance (AMR) associations survive control for taxonomy at phylum and family level, and what limits that control. They do survive in the amr_environmental_resistome report, but most families cannot be tested and effect sizes are modest. [src: amr_environmental_resistome] See [[concepts/environmental-structuring-of-antimicrobial-resistance-gene-content]] for the wider topic.

## Literature Context

Several candidate papers bear on whether resistomes track phylogeny or environment. A soil study using functional metagenomic selections for resistance to 18 antibiotics from 18 agricultural and grassland soils found that distinct soil types harbour distinct resistomes. Resistome composition also correlated with microbial phylogenetic and taxonomic structure, both across and within soil types, and the authors concluded that community composition is the primary determinant of soil ARG content [PMID 24847883](https://pubmed.ncbi.nlm.nih.gov/24847883/). An analysis of over 6000 sequenced genomes found significant enrichment of resistance functions by both ecology and phylogeny, and concluded that resistance functions are largely constrained by ecology [PMID 25003965](https://pubmed.ncbi.nlm.nih.gov/25003965/). Other habitats point the same way on phylogeny. In composting, microbial phylogeny was the key determinant of the transcriptional response of the resistome [PMID 28814344](https://pubmed.ncbi.nlm.nih.gov/28814344/). In the phyllosphere along an elevational gradient, bacterial community composition, rather than plant traits or abiotic factors, significantly affected ARG abundance [PMID 39572861](https://pubmed.ncbi.nlm.nih.gov/39572861/). Antarctic MAGs showed resistome composition that was site-specific and associated with geochemical variables such as cobalt and iron [PMID 42599548](https://pubmed.ncbi.nlm.nih.gov/42599548/). Wastewater work reports that shifts in bacterial community composition correlated with ARGs across 18 plants, and that bacterial phylogeny can shape the activated-sludge resistome [PMID 31133267](https://pubmed.ncbi.nlm.nih.gov/31133267/).

Some papers report decoupling. In Namib Desert soils, horizontally acquired ARGs co-occurring with mobile genetic elements were thought to decouple community composition from ARG profiles [PMID 37968548](https://pubmed.ncbi.nlm.nih.gov/37968548/). In migratory birds, Procrustes analysis showed that microbial community structure was not correlated with the resistome [PMID 32122398](https://pubmed.ncbi.nlm.nih.gov/32122398/). Host taxonomy can also matter for single genes. Burkholderiales, and Comamonadaceae in particular, were predicted as the original environmental hosts of dfrB [PMID 39658215](https://pubmed.ncbi.nlm.nih.gov/39658215/). Arsenic-related genes were common in 922 soil genomes and 38 metagenomes but not universal, and their types and proportions differed across soils [PMID 31146755](https://pubmed.ncbi.nlm.nih.gov/31146755/).

The amr_environmental_resistome corpus is consistent with the view that ecology and phylogeny both structure resistomes [PMID 25003965](https://pubmed.ncbi.nlm.nih.gov/25003965/). Its significant within-phylum effects in 5 of 6 major phyla, and within-family effects in 20 of 141 testable families (14%), agree with the soil finding that resistome differences persist within types and taxa [PMID 24847883](https://pubmed.ncbi.nlm.nih.gov/24847883/). Its explicit family-level test extends these mostly community-level studies. Its caveats stay in place. Most families cannot be tested, effect sizes are modest (η² = 0.02–0.13), and phylogeny likely explains more variance than environment. This is compatible with papers that emphasise phylogeny. It is in some tension with the bird and Namib reports of decoupling, though those studies are single-habitat and use different methods. The metal-ecology genus-level result, which finds that breadth of metal resistance relates to niche breadth beyond phylogenetic expectation, has no direct counterpart among these candidates. The arsenic survey concerns gene distribution rather than niche breadth [PMID 31146755](https://pubmed.ncbi.nlm.nih.gov/31146755/). That part of the corpus is therefore novel relative to this evidence.

## Phylum-level control

Significant within-phylum environment effects on AMR occur in 5 of 6 major phyla: Pseudomonadota, Bacillota_A, Actinomycetota, Bacteroidota and Bacillota. [src: amr_environmental_resistome] Chloroflexota is the only tested major phylum without a significant effect. [src: amr_environmental_resistome] Bacteroidota shows the largest within-phylum effect (η² = 0.130). [src: amr_environmental_resistome]

## Family-level control

Of 141 testable families, 20 (14%) show significant within-family environment effects after false discovery rate (FDR) correction. [src: amr_environmental_resistome] The top families are Enterobacteriaceae (q = 3×10⁻²¹) [src: amr_environmental_resistome], Bacteroidaceae (q = 1.3×10⁻¹⁷) [src: amr_environmental_resistome], Lachnospiraceae (q = 2.5×10⁻¹²) [src: amr_environmental_resistome] and Pseudomonadaceae (q = 3.9×10⁻¹²). [src: amr_environmental_resistome]

The report concludes that species in different environments carry different AMR profiles even within the same family, so the association is not simply a proxy for phylogeny. [src: amr_environmental_resistome] It states that the pattern holds within phyla and families and is not a phylogenetic artifact. [src: amr_environmental_resistome] The central discoveries digest repeats that all findings survive family-level control, with 20/141 families significant. [src: discoveries]

## Limits of the control

Environment and phylogeny stay deeply entangled despite family-level control. Some families are almost entirely clinical, for example many Enterobacteriaceae. [src: amr_environmental_resistome] The report calls the 14% of families with significant within-family effects its most convincing evidence, but most families do not span enough environments to test. [src: amr_environmental_resistome]

All tests are highly significant (p ~ 0), but the effect sizes are modest (η² = 0.02–0.13). Environment explains 2-13% of variance in AMR composition, and phylogeny likely explains much more. [src: amr_environmental_resistome]

## A related result for metals

The microbeatlas_metal_ecology report gives a parallel case at genus level. The raw ordinary least squares (OLS) correlation between mean metal type diversity and Levins' B_std is modest (r ≈ 0.21). The report says this reflects baseline phylogenetic structure in both variables. [src: microbeatlas_metal_ecology] It finds that genera with broader metal resistance repertoires have broader ecological ranges beyond what phylogenetic relatedness predicts. The association is robust to genome size, species richness, prevalence filtering, operational taxonomic unit (OTU) abundance filtering and all 13 environment categories. [src: microbeatlas_metal_ecology] See [[concepts/metal-resistance-repertoire-breadth-and-ecological-niche-breadth]].

## Open Directions

- Test family-level effects only in families that span several environments, and report how many families reach that threshold. This addresses the finding that most families cannot be tested.
- Partition AMR composition variance between phylogeny and environment, for example by variance partitioning. This would check the statement that phylogeny likely explains much more than the 2-13% attributed to environment.
- Repeat the within-family tests after excluding clinical isolates, to see whether the Enterobacteriaceae result depends on clinical sampling.
- Test finer taxonomic levels, such as genus, with the same approach used for metals, to see whether the effects persist.
