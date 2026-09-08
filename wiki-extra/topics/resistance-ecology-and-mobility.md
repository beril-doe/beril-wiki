---
title: Resistance Ecology and Mobility
type: Topic
sources:
- id: amr_environmental_resistome
  resource: ../../wiki/summaries/amr_environmental_resistome__REPORT.md
  title: amr environmental resistome
- id: amr_pangenome_atlas
  resource: ../../wiki/summaries/amr_pangenome_atlas__REPORT.md
  title: amr pangenome atlas
- id: amr_strain_variation
  resource: ../../wiki/summaries/amr_strain_variation__REPORT.md
  title: amr strain variation
- id: metal_resistance_global_biogeography
  resource: ../../wiki/summaries/metal_resistance_global_biogeography__REPORT.md
  title: metal resistance global biogeography
- id: prophage_amr_comobilization
  resource: ../../wiki/summaries/prophage_amr_comobilization__REPORT.md
  title: prophage amr comobilization
- id: t4ss_cazy_environmental_hgt
  resource: ../../wiki/summaries/t4ss_cazy_environmental_hgt__REPORT.md
  title: t4ss cazy environmental hgt
- id: amr_fitness_cost
  resource: ../../wiki/summaries/amr_fitness_cost__REPORT.md
  title: amr fitness cost
- id: metal_cross_resistance
  resource: ../../wiki/summaries/metal_cross_resistance__REPORT.md
  title: metal cross resistance
- id: counter_ion_effects
  resource: ../../wiki/summaries/counter_ion_effects__REPORT.md
  title: counter ion effects
- id: metal_specificity
  resource: ../../wiki/summaries/metal_specificity__REPORT.md
  title: metal specificity
- id: phage_defense_arsenal
  resource: ../../wiki/summaries/phage_defense_arsenal__REPORT.md
  title: phage defense arsenal
- id: snipe_defense_system
  resource: ../../wiki/summaries/snipe_defense_system__REPORT.md
  title: snipe defense system
- id: fitness_effects_conservation
  resource: ../../wiki/summaries/fitness_effects_conservation__REPORT.md
  title: fitness effects conservation
- id: prophage_ecology
  resource: ../../wiki/summaries/prophage_ecology__REPORT.md
  title: prophage ecology
---
# Resistance Ecology and Mobility

Resistance ecology and mobility concerns how resistance traits are distributed across environments, lineages, strains, and genomic compartments—and how they move, persist, or become conditionally valuable. The corpus speaks to this topic through complementary evidence: pangenome surveys describe where resistance genes occur, fitness experiments show when they matter, and genomic-context analyses test whether co-occurrence is consistent with transfer. Together, the projects support a model in which resistance is shaped by ecology and selection, but in which “mobile,” “acquired,” “co-inherited,” and “mechanistically transferred” remain distinct claims.

## Literature Context

Published work has long treated resistance as an ecological and evolutionary phenotype rather than a property determined by antibiotic exposure alone. Environmental conditions—including pollution, resource availability, population density, and microbial community structure—can alter selection for resistance and the opportunities for its spread, while genomic evolution combines mutation, gene acquisition, recombination, and lineage-specific adaptation.[PMID 29069382](https://pubmed.ncbi.nlm.nih.gov/29069382/) Reviews of resistance evolution likewise emphasize that resistance determinants can be ancient, repeatedly recruited into new genomic backgrounds, and shaped by both vertical inheritance and horizontal gene transfer (HGT).[PMID 27768822](https://pubmed.ncbi.nlm.nih.gov/27768822/) HGT is especially important in host-associated communities, where plasmids, phages, mobile elements, and dense microbial interactions create multiple routes for gene exchange.[PMID 37054673](https://pubmed.ncbi.nlm.nih.gov/37054673/) Work on urban rivers and plant-pathogenic bacteria similarly shows that resistance distributions reflect environmental reservoirs, anthropogenic inputs, host-associated selection, and organism-specific histories rather than a single universal driver.[PMID 35926259](https://pubmed.ncbi.nlm.nih.gov/35926259/)[PMID 29856934](https://pubmed.ncbi.nlm.nih.gov/29856934/)

The corpus is consistent with this literature in finding strong environmental and genomic structure, a large accessory component, and conditional fitness effects. Its environmental differences in AMR burden and mechanism composition extend prior ecological frameworks by quantifying their explanatory limits: environment-associated effects account for only approximately 2–13% of AMR-composition variance, leaving phylogeny, sampling, and annotation as substantial alternatives. Its distinction between co-occurrence and demonstrated transfer also aligns with genomic studies showing that resistance mobility depends on specific vehicles and contexts. Plasmid research documents broad but uneven transfer potential and emphasizes that mobility is a property of interacting plasmid, host, and genomic contexts, not merely of a resistance gene.[PMID 20805406](https://pubmed.ncbi.nlm.nih.gov/20805406/)[PMID 40694848](https://pubmed.ncbi.nlm.nih.gov/40694848/) Examples such as plasmid-borne *tet(X)* and insertion-sequence-mediated *mcr-2* mobilization demonstrate that particular resistance genes can acquire clinically consequential mobility through identifiable mechanisms.[PMID 31235960](https://pubmed.ncbi.nlm.nih.gov/31235960/)[PMID 33510713](https://pubmed.ncbi.nlm.nih.gov/33510713/)

The corpus extends this literature most clearly through its cross-scale comparison of resistance islands, prophage proximity, species-level prophage density, integrative machinery, and fitness conditionality. The 1,517 resistance islands and high co-occurrence values provide evidence for tight co-inheritance, but the weak and window-dependent prophage-proximity signal argues against treating every prophage-associated contig as proof of mobilization. This is a refinement of HGT-centered interpretations, not a rejection of them. Likewise, the metal-resistance results are compatible with literature linking metal exposure, oxidative stress, and co-selection, but the corpus separates shared stress tolerance from metal-specific fitness and identifies geographic hotspots without yet establishing regional selection.[PMID 34298350](https://pubmed.ncbi.nlm.nih.gov/34298350/) Its near-zero pooled openness–AMR correlation is therefore in tension with simple community-level expectations that more open genomes should uniformly carry more resistance. Finally, the corpus’s defense-system co-occurrence landscape and SNIPE case study add a comparatively novel defense–metabolism dimension: they suggest that resistance ecology should include phage defense and conditional cellular trade-offs, while remaining hypotheses until physical linkage, transfer, expression, and ecological selection are directly validated.

## What the Corpus Shows

**Resistance is environmentally structured, but not simply environmentally caused.** The broadest AMR catalog analyses identify environment-associated differences in resistance burden, mechanism composition, and core/accessory allocation. Across 14,723 bacterial species and 293K genomes, environment was associated with AMR burden and composition, with reported effects explaining approximately 2–13% of AMR-composition variance; however, phylogeny, sampling, isolation practices, annotation, and host-associated traits remain alternative explanations. [^amr_environmental_resistome] The catalog itself includes stress-response genes alongside classical antibiotic-resistance genes, so its “AMR” landscape is broader than clinically defined antibiotic resistance. [^amr_pangenome_atlas]

The pangenome atlas found that only 30.3% of AMR genes were core, compared with 46.8% for the pangenome baseline, while the auxiliary genome was 2.2x enriched for AMR. [^amr_pangenome_atlas] Clinical species had 68% accessory AMR in one environmental comparison, versus 43% in soil; related atlas estimates reported 30.8% core AMR in clinical species, compared with 58.1% in soil and 63.1% in plant species. [^amr_environmental_resistome][^amr_pangenome_atlas] These results support a connection between human-associated sampling and acquired or mobile resistance, but they do not imply that environmental resistance is uniformly intrinsic or clinical resistance uniformly acquired. The intrinsic/acquired distinction is graded: in a within-species atlas, 51.3% of AMR records were rare, 41.3% variable, and 7.5% fixed. [^amr_strain_variation] [environmental-resistome](../../wiki/concepts/environmental-resistome.md)

This pattern extends beyond antibiotics. Coordinate-filtered environmental MAGs showed 2.8% prevalence of at least one metal-resistance type; a 5° grid yielded 11 significant hotspots and 3 coldspots after multiple-testing correction. [^metal_resistance_global_biogeography] Soil had 5.8% prevalence, compared with 1.2% in marine samples, but the geographic analysis remains preliminary because study origin, biome composition, and sampling effort were not yet fully corrected. [^metal_resistance_global_biogeography] Thus, geography is a useful organizing axis, not evidence by itself for regional selection. [spatial-sampling-effort-confounding](../../wiki/concepts/spatial-sampling-effort-confounding.md)

**Mobility is visible at several genomic scales, with different evidentiary strength.** The most direct population-level evidence for modular inheritance comes from resistance islands—sets of AMR genes that co-occur across strains. The corpus detected 1,517 islands across 705 species, with mean size 6.2 genes, median size 4 genes, maximum size 43 genes, and mean pairwise phi coefficient 0.827. [^amr_strain_variation] Here, phi measures co-occurrence; the high value supports tight co-inheritance, but does not establish physical location, co-selection, functional synergy, or a particular mobile carrier. Of the islands, 1,343 (88%) contained genes from multiple resistance mechanisms. [^amr_strain_variation] [resistance-island-coinheritance](../../wiki/concepts/resistance-island-coinheritance.md)

Prophage analyses show why scale matters. Among 36,041 AMR gene instances, 20,073 (55.7%) occurred on contigs carrying strict prophage markers, but only 1,991 (5.5%) were within 5 genes of a marker and 3,731 (10.4%) within 10 genes; the median nearest-marker distance was 34 genes. [^prophage_amr_comobilization] At a 10-gene threshold, nearby genes were 67.6% accessory versus 65.5% for distal genes, with odds ratio 1.10 and bootstrap 95% confidence interval [1.024, 1.185]. [^prophage_amr_comobilization] The association changed with the window—odds ratio 0.78 at 3 genes, 0.92 at 5, 1.10 at 10, 1.19 at 15, and 1.28 at 50—and the median species-level odds ratio was 0.85. [^prophage_amr_comobilization] These results support a heterogeneous relationship between prophage-associated sequence and AMR, rather than uniform phage-mediated transfer. [scale-dependent-mobile-element-associations](../../wiki/concepts/scale-dependent-mobile-element-associations.md)

At a broader scale, prophage-marker density was positively associated with AMR repertoire breadth across 4,770 species, with Spearman rho=0.572; after controlling for genome count, the partial correlation remained rho=0.464. [^prophage_amr_comobilization] The association was reported across five major phyla, but its persistence across species does not demonstrate local physical linkage or mobilization. [^prophage_amr_comobilization] This distinction is central: species-level covariance can arise through shared ecological history, co-acquisition, or lineage structure even when local proximity is weak.

Chromosomal and integrative routes provide a parallel mobility model. Among 30,497 high-quality environmental MAGs, 6,652 (21.8%) carried T4SS or conjugative machinery, and T4SS-positive genomes had 10× higher MGE density than other genomes. [^t4ss_cazy_environmental_hgt] CAZy genes were not detected on plasmids by ICEfinder, while 12 IMEs occurred among the top 100 accumulators. [^t4ss_cazy_environmental_hgt] T4SS-proximal CAZy neighborhoods were enriched in marine sediment, barley rhizosphere, and maize rhizosphere, and the GT2 gene tree contained 77 detected HGT events, including 32 normalized high-confidence cross-phylum events. [^t4ss_cazy_environmental_hgt] These observations support chromosomal or integrative transfer as a hypothesis, but synteny, neighborhood structure, and phylogenetic incongruence do not establish the causal transfer mechanism. [chromosomal-and-integrative-gene-transfer](../../wiki/concepts/chromosomal-and-integrative-gene-transfer.md)

**Mobility is filtered by fitness and condition.** Resistance genes are not simply costly cargo. Under non-antibiotic conditions, AMR-gene knockouts had a pooled relative shift of +0.086 [95% CI: +0.074, +0.098], but the AMR knockout mean was −0.024 and the comparison non-AMR knockout background was approximately −0.11. [^amr_fitness_cost] Because RB-TnSeq measures competitive fitness of insertion mutants relative to a pool, this is a relative perturbation contrast, not an absolute selection coefficient for an intact resistance gene. [^amr_fitness_cost]

Under any-antibiotic conditions, 57.0% of AMR genes showed a fitness flip toward greater importance, with N = 797, mean flip +0.045, and Wilcoxon p = 0.0001. [^amr_fitness_cost] The effect depended on mechanism: broad-spectrum efflux genes had mean flip +0.094, compared with −0.001 for enzymatic-inactivation genes, with Mann-Whitney p = 0.007. [^amr_fitness_cost] This supports a conditional-mobility model: a resistance gene can be burdensome or relatively dispensable in one environment yet retained when antibiotic or chemical stress changes the fitness landscape.

The same logic applies to metals, but metal fitness contains both shared stress and stressor-specific components. Across 317 organism–metal-pair observations, 98.1% of gene-level correlations were positive, yet the study lacked non-metal stress controls. [^metal_cross_resistance] A direct NaCl comparison classified 4,304 of 10,821 metal-important records (39.8%) as also NaCl-important, leaving 6,517 records (60.2%) outside that shared-stress overlap. [^counter_ion_effects] A separate specificity analysis classified 4,177 of 7,609 records (54.9%) as metal-specific, 2,888 (38.0%) as generally sick, and 544 (7.2%) as metal+stress. [^metal_specificity] Resistance ecology therefore includes broad cellular robustness as well as chemistry-specific mechanisms. [shared-stress-versus-stressor-specific-fitness](../../wiki/concepts/shared-stress-versus-stressor-specific-fitness.md) [metal-cross-resistance](../../wiki/concepts/metal-cross-resistance.md)

**Defense systems create a second mobility and arms-race layer.** Markers for at least one anti-phage defense system occurred in 27,626 of 27,690 species-level pangenomes (99.8%), although prevalence depended strongly on marker definition. [^phage_defense_arsenal] Using permutation-based nulls and false-discovery-rate correction, 27 of 28 defense-system pairs showed significant positive co-occurrence; the strongest was R-M Type II × Gabija, with 2,429 observed co-occurrences, null mean 1,555, z = 46.1, and OR = 24.0. [^phage_defense_arsenal]

SNIPE adds a mechanistic example linking defense to a host-entry route: its DUF4041/PF13250 marker occurred in 4,572 gene clusters across 1,696 species and 33 bacterial and archaeal phyla, with 86.7% of clusters accessory or singleton. [^snipe_defense_system] In *E. coli* K-12, ManXYZ fitness data from 168 experiments per gene supported operation as a single operon, with cofitness correlations of 0.851 for *manX*↔*manZ*, 0.705 for *manX*↔*manY*, and 0.725 for *manY*↔*manZ*. [^snipe_defense_system] These data support a defense–metabolism trade-off for this system, not a general mechanism for all defense syndromes. [phage-defense-syndromes-and-arms-race](../../wiki/concepts/phage-defense-syndromes-and-arms-race.md)

## Tensions and Caveats

The central tension is whether broad conservation and fitness patterns predict resistance burden. Genome-wide analyses associate essentiality or strong fitness effects with higher core representation, but AMR-specific analyses found indistinguishable baseline distributions for core and accessory AMR genes, with d = 0.002 and p = 0.33. [^fitness_effects_conservation][^amr_fitness_cost] The conflict [conflict--acinetobacter_adp1_explorer--adp1_triple_essentiality--alphafold_msa_annotation--8af84dcc](../conflicts/conflict--acinetobacter_adp1_explorer--adp1_triple_essentiality--alphafold_msa_annotation--8af84dcc.md) frames this correctly: conservation, essentiality, and laboratory deletion cost are related observables, not interchangeable biological quantities. The AMR-specific version, conflict  amr_cofitness_networks  amr_fitness_cost  90a27ef2, further shows that pooled antibiotic flips and class-matched validation differ: the latter had a 54.8% flip rate for 157 pairs with p = 0.14. [^amr_fitness_cost]

A second tension concerns ecology versus lineage. The pooled openness–AMR correlation was near zero, rho=0.006, while openness correlated positively with AMR count in 8/10 tested phyla. [^amr_pangenome_atlas] Within species, 55.6% of 1,261 tested species had significant ANI–AMR repertoire associations at FDR < 0.05, but sparse metadata limited strict ecotype testing to 2 species. [^amr_strain_variation] The conflict [conflict--amr_environmental_resistome--amr_fitness_cost--amr_pangenome_atlas--76f2bfcc](../conflicts/conflict--amr_environmental_resistome--amr_fitness_cost--amr_pangenome_atlas--76f2bfcc.md) therefore cautions against reading community-level environmental differences as direct evidence of exposure-driven selection within populations.

Finally, marker-based mobility evidence remains incomplete. Prophage annotations may include domesticated remnants or bacterial homologs, and CRISPR-Cas prevalence ranged from 96% by EggNOG description matching to approximately 55% using Cas1 PF01867. [^prophage_ecology][^phage_defense_arsenal] The conflict [conflict--phage_defense_arsenal--prophage_amr_comobilization--prophage_ecology--9f1135e8](../conflicts/conflict--phage_defense_arsenal--prophage_amr_comobilization--prophage_ecology--9f1135e8.md) captures the load-bearing limitation: system-level associations are useful for generating hypotheses, but intact elements, physical linkage, transfer events, and expression require dedicated validation.

## Where to Go Deeper

- [environmental-resistome](../../wiki/concepts/environmental-resistome.md) — Start here for the broad ecological, phylogenetic, and genomic-compartment distribution of resistance.
- [scale-dependent-mobile-element-associations](../../wiki/concepts/scale-dependent-mobile-element-associations.md) — Compare local proximity, contig co-occurrence, and species-level association without conflating their evidentiary strength.
- [resistance-island-coinheritance](../../wiki/concepts/resistance-island-coinheritance.md) — Examine strain-level modules and the distinction between co-inheritance and demonstrated transfer.
- [chromosomal-and-integrative-gene-transfer](../../wiki/concepts/chromosomal-and-integrative-gene-transfer.md) — Follow the evidence for T4SS, IME, chromosomal neighborhoods, and cross-phylum HGT.
- [antimicrobial-resistance-fitness-cost](../../wiki/concepts/antimicrobial-resistance-fitness-cost.md) — Assess when resistance is burdensome, conditionally beneficial, or only relatively costly.
- [metal-cross-resistance](../../wiki/concepts/metal-cross-resistance.md) — Extend the framework from antibiotics to shared and chemistry-specific metal fitness.
- [phage-defense-syndromes-and-arms-race](../../wiki/concepts/phage-defense-syndromes-and-arms-race.md) — Explore defense-system co-occurrence, prophage ecology, and arms-race interpretations.

Key entities: [kescience-fitnessbrowser](../../wiki/entities/kescience-fitnessbrowser.md), [kbase-ke-pangenome](../../wiki/entities/kbase-ke-pangenome.md), [gtdb](../../wiki/entities/gtdb.md), [metal-fitness-atlas](../../wiki/entities/metal-fitness-atlas.md), [bacdive](../../wiki/entities/bacdive.md), [tnseq](../../wiki/entities/tnseq.md)

Project reports:

- [amr_environmental_resistome__REPORT](../../wiki/summaries/amr_environmental_resistome__REPORT.md)
- [amr_strain_variation__REPORT](../../wiki/summaries/amr_strain_variation__REPORT.md)
- [prophage_amr_comobilization__REPORT](../../wiki/summaries/prophage_amr_comobilization__REPORT.md)
- [t4ss_cazy_environmental_hgt__REPORT](../../wiki/summaries/t4ss_cazy_environmental_hgt__REPORT.md)
- [amr_fitness_cost__REPORT](../../wiki/summaries/amr_fitness_cost__REPORT.md)
- [metal_cross_resistance__REPORT](../../wiki/summaries/metal_cross_resistance__REPORT.md)
- [phage_defense_arsenal__REPORT](../../wiki/summaries/phage_defense_arsenal__REPORT.md)

[^amr_environmental_resistome]: [amr environmental resistome](../../wiki/summaries/amr_environmental_resistome__REPORT.md)
[^amr_pangenome_atlas]: [amr pangenome atlas](../../wiki/summaries/amr_pangenome_atlas__REPORT.md)
[^amr_strain_variation]: [amr strain variation](../../wiki/summaries/amr_strain_variation__REPORT.md)
[^metal_resistance_global_biogeography]: [metal resistance global biogeography](../../wiki/summaries/metal_resistance_global_biogeography__REPORT.md)
[^prophage_amr_comobilization]: [prophage amr comobilization](../../wiki/summaries/prophage_amr_comobilization__REPORT.md)
[^t4ss_cazy_environmental_hgt]: [t4ss cazy environmental hgt](../../wiki/summaries/t4ss_cazy_environmental_hgt__REPORT.md)
[^amr_fitness_cost]: [amr fitness cost](../../wiki/summaries/amr_fitness_cost__REPORT.md)
[^metal_cross_resistance]: [metal cross resistance](../../wiki/summaries/metal_cross_resistance__REPORT.md)
[^counter_ion_effects]: [counter ion effects](../../wiki/summaries/counter_ion_effects__REPORT.md)
[^metal_specificity]: [metal specificity](../../wiki/summaries/metal_specificity__REPORT.md)
[^phage_defense_arsenal]: [phage defense arsenal](../../wiki/summaries/phage_defense_arsenal__REPORT.md)
[^snipe_defense_system]: [snipe defense system](../../wiki/summaries/snipe_defense_system__REPORT.md)
[^fitness_effects_conservation]: [fitness effects conservation](../../wiki/summaries/fitness_effects_conservation__REPORT.md)
[^prophage_ecology]: [prophage ecology](../../wiki/summaries/prophage_ecology__REPORT.md)
