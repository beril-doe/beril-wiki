---
type: "Concept"
description: "Evidence from transposase proxies, contig co-location and mobilome data on whether plant-interaction genes are mobile, including the genus-versus-genome scale discrepancy."
sources: ["summaries/discoveries.md", "summaries/plant_microbiome_ecotypes__REPORT.md"]
---
# Mobile elements and horizontal transfer of plant-interaction genes

In the plant_microbiome_ecotypes project, plant-interaction marker genes co-occur with transposase/integrase singletons across species, and plant-associated genera carry more mobile elements per genome in MGnify. Marker singleton enrichment is below the genomic average, and genome-level literature reports fewer mobile elements in plant-associated bacteria. [src: plant_microbiome_ecotypes] The horizontal gene transfer (HGT) evidence is partly proxy-based, through transposase/integrase singletons and MGnify mobilome aggregates. [src: plant_microbiome_ecotypes] The MGnify mobilome counts are described by the report as direct mobile-element quantification, but only for soil-biome genera. [src: plant_microbiome_ecotypes]

## Literature Context

The candidate literature establishes that mobile genetic elements (MGEs) are widespread in soil and plant-associated bacteria and are treated as a major route of adaptation. Reviews describe MGEs in soil and plant-associated bacteria and the factors affecting gene transfer [PMID 17961477](https://pubmed.ncbi.nlm.nih.gov/17961477/). They also describe plasmids as supplying metabolic, resistance and pathogenicity-related genes in the plant environment, while noting that the role of mobile elements for plant-associated bacteria is only beginning to be understood [PMID 30070649](https://pubmed.ncbi.nlm.nih.gov/30070649/). Another review argues that gain and loss of genomic islands and other MGEs frequently mediate lifestyle transitions in agroecosystem bacteria, while core genome stability is preserved [PMID 42283811](https://pubmed.ncbi.nlm.nih.gov/42283811/). A phytosphere review cautions that the selective forces driving gene transfer and persistence in situ are not well understood [PMID 33873398](https://pubmed.ncbi.nlm.nih.gov/33873398/).

More specific evidence comes from genomes. An analysis of 5,565 plant-associated bacterial genomes found integrons abundant in Pseudomonadales, Burkholderiales and Xanthomonadales. It detected nearly 9,000 gene cassettes and reported that integrons facilitate cross-species HGT, particularly in the phyllosphere [PMID 38741746](https://pubmed.ncbi.nlm.nih.gov/38741746/). In four Pseudomonas amygdali pv. aesculi genomes, effector genes were mostly associated with insertion sequence elements, and the coronatine cluster moved from a chromosomal location to a mobilizable plasmid [PMID 37541538](https://pubmed.ncbi.nlm.nih.gov/37541538/). A survey of 9,725 unique plasmid sequences found that plasmid traits varied with environment, including plant, and with host taxonomy. Environment differences in broad COG categories were not fully explained by host taxonomy, which suggests selection on plasmid traits [PMID 36629415](https://pubmed.ncbi.nlm.nih.gov/36629415/).

The corpus's transposase and integrase co-occurrence result (OR=15.95 among 1,136 plant-associated species) is consistent with this picture of mobile-element-linked plant-interaction genes. It is a proxy, though, and does not show transfer. The corpus's adjacent marker–transposase pairs involve effectors, T6SS, type III secretion, quorum sensing, cellulase and T4SS. Those pairs are compatible with the plasmid and effector mobilization reported in P. amygdali [PMID 37541538](https://pubmed.ncbi.nlm.nih.gov/37541538/). The hub does not identify the transposases as insertion sequences, so this is only a loose parallel. Its partial H4 proxy results align with the integron work [PMID 38741746](https://pubmed.ncbi.nlm.nih.gov/38741746/).

The MGnify finding of 3.7 vs 2.8 mobile elements per genome in plant-associated genera is direct mobile-element quantification, but only for soil-biome genera. It shows MGE presence and is not a measure of HGT activity. It is compatible with the reviews' view of MGEs as common in soil and plant-associated bacteria [PMID 42283811](https://pubmed.ncbi.nlm.nih.gov/42283811/), but it does not by itself demonstrate active transfer. The candidate papers do not address the corpus's genus-versus-genome discrepancy with Levy et al. (2018) and Bograd et al. (2025). The corpus's hypothesis that adaptation involves accessory acquisition followed by core stabilization echoes the review's emphasis on dynamic MGEs with preserved core genome stability [PMID 42283811](https://pubmed.ncbi.nlm.nih.gov/42283811/). It remains untested here. The singleton enrichment of 0.78, below the genomic average, has no direct counterpart in these papers and is novel relative to them.

## Transposase co-occurrence

Species that carry singleton marker gene clusters are far more likely to also carry transposase/integrase singletons. Among 1,136 plant-associated species the odds ratio (OR) was 15.95 (Fisher's exact, p=8.8e-20). [src: plant_microbiome_ecotypes, discoveries] The proxy was 986,464 transposase/integrase singleton clusters, made up of 722,674 transposase and 263,790 integrase clusters. [src: plant_microbiome_ecotypes] The report suggests this co-localization reflects recent HGT on mobile genetic elements. [src: discoveries]

Per-marker analysis found the strongest signal in plant growth promoting (PGP) markers [src: plant_microbiome_ecotypes]:
- DAPG biocontrol, OR=8.75 [src: plant_microbiome_ecotypes]
- ACC (1-aminocyclopropane-1-carboxylate) deaminase, OR=6.43 [src: plant_microbiome_ecotypes]
- Nitrogen fixation, OR=3.76 [src: plant_microbiome_ecotypes]

Among pathogenic markers, type IV secretion system (T4SS) had OR=3.23. [src: plant_microbiome_ecotypes] Type VI secretion system (T6SS) had OR=2.66. [src: plant_microbiome_ecotypes] Effectors had OR=2.67. [src: plant_microbiome_ecotypes] See also [[entities/acc-deaminase-acds]] and bacterial nitrogen fixation nif genes.

## Contig co-location

Contig co-location analysis found 498,677 marker-transposase pairs on shared contigs across 18,569 species. [src: plant_microbiome_ecotypes] The report gives no baseline for this count in the cited claim. T4SS had the most co-located pairs (84,411) and the closest median distance (238 genes). [src: plant_microbiome_ecotypes] Fifteen pairs were immediately adjacent at gene-number distance 1. They spanned effectors, T6SS, type III secretion system, quorum sensing, cellulase and T4SS, in species including Rhizobium ecuadorense, Phytobacter ursingii and Burkholderia puraquae. [src: plant_microbiome_ecotypes]

## A counter-signal: singleton enrichment

Markers had an overall singleton enrichment ratio of 0.78. That is less mobile than the genomic average (Wilcoxon p<1e-300). [src: plant_microbiome_ecotypes] The report reads the mixed signal as follows. Individual HGT events are common, but markers as a class appear under stronger purifying selection, likely because they are functionally important once acquired. [src: plant_microbiome_ecotypes] The report also says this mixed signal shows the limits of proxy approaches. [src: plant_microbiome_ecotypes] For the core-versus-accessory side of this, see [[concepts/core-versus-accessory-partitioning-of-gene-functions-and-trait-genes]].

## Mobilome burden and the genus-versus-genome discrepancy

In the MGnify cross-validation, plant-associated genera carried more mobile elements per genome than non-plant genera, with medians of 3.7 vs 2.8 (Mann-Whitney U p=1.49×10⁻⁵). [src: plant_microbiome_ecotypes] The soil biome analysis detected 17,323 mobilome entries across 563 pangenome genera, using ISEScan, ICEfinder and geNomad. [src: plant_microbiome_ecotypes] Element types included IS110, IS701, IS1634, IS256 and IS3 elements, plasmids, prophages, terminal inverted repeats and viral sequences. [src: plant_microbiome_ecotypes] See [[entities/kescience-mgnify]].

This genus-level result appears to contradict genome-level findings by Levy et al. (2018) and Bograd et al. (2025), who report fewer mobile elements in plant-associated genomes. [src: plant_microbiome_ecotypes] The report says the difference likely reflects rhizosphere/soil genera, where HGT is frequent, versus endosphere-focused genome-level comparisons. [src: plant_microbiome_ecotypes] It treats the enrichment as consistent with Rajabal et al. (2024), who describe the rhizosphere as an HGT hotspot. [src: plant_microbiome_ecotypes] It documents the scale dependence as an item of its own. [src: plant_microbiome_ecotypes]

The report offers a hypothesis, not a demonstrated result. At the genome level, plant-adapted strains may shed mobile elements as beneficial functions stabilize into the core genome, consistent with a 64.6% core fraction for PGP genes. At the genus level, diversity of accessory elements across strains inflates the aggregate count. [src: plant_microbiome_ecotypes] It frames this as plant adaptation involving HGT-mediated accessory gene acquisition followed by core genome stabilization. [src: plant_microbiome_ecotypes]

The partial H4 HGT proxy results align with Ghaly et al. (2024), who found integrons as HGT hotspots in plant-associated bacteria. [src: plant_microbiome_ecotypes] They also align with Pinto-Carbo et al. (2016), who demonstrated HGT between obligate plant symbionts. [src: plant_microbiome_ecotypes]

## Caveats

MGnify BGC (biosynthetic gene cluster), mobilome and defense annotations exist only for the soil biome. They are not available for the tomato, maize or barley rhizosphere biomes. [src: plant_microbiome_ecotypes] The mobilome comparison is therefore soil-dwelling plant-associated genera against soil-dwelling non-plant genera, not rhizosphere against bulk soil. [src: plant_microbiome_ecotypes] The HGT analysis uses transposase/integrase singletons and MGnify mobilome aggregates as proxies. [src: plant_microbiome_ecotypes] Without geNomad annotations, HGT was assessed indirectly. [src: plant_microbiome_ecotypes] The report proposes replacing the proxies with geNomad mobile-element predictions once these are available in the KBase Data Lakehouse, to strengthen H4 conclusions and resolve the genus-versus-genome signal. [src: plant_microbiome_ecotypes] See also [[concepts/isolation-metadata-versus-metagenomic-cross-validation-of-plant-associated-taxa]] and [[summaries/plant_microbiome_ecotypes__REPORT]].

## Tensions

- Transposase co-occurrence is strongly positive (OR=15.95) [src: plant_microbiome_ecotypes], but marker singleton enrichment is 0.78, below the genomic average. [src: plant_microbiome_ecotypes]
- Genus-level mobilome enrichment (3.7 vs 2.8 per genome) [src: plant_microbiome_ecotypes] contrasts with literature showing fewer mobile elements in plant-associated genomes. [src: plant_microbiome_ecotypes]

## Open Directions

- Replace the proxies with direct geNomad mobile-element predictions, once available. This would test H4 and the genus-versus-genome signal.
- Run a genome-level mobilome comparison inside the same MGnify genera. This would test whether strains shed elements while genus totals stay high.
- Test whether the 15 adjacent marker-transposase pairs sit within annotated mobile elements, and compare the 498,677 shared-contig pairs with a baseline. This would separate real mobility from chance proximity.
- Obtain mobilome annotations for rhizosphere biomes. This would remove the soil-only limitation.
