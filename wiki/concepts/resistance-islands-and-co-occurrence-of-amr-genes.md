---
type: "Concept"
description: "Detection of tightly co-occurring AMR gene modules within species, their mechanism composition and mobile-element interpretation; stops short of proof of co-selection."
sources: ["summaries/amr_strain_variation__REPORT.md", "summaries/discoveries.md"]
---
# Resistance islands and co-occurrence of AMR genes

This page covers tightly co-occurring modules of antimicrobial resistance (AMR) genes within species, called resistance islands. The amr_strain_variation report found 1,517 of them, and most mix several resistance mechanisms. [src: amr_strain_variation] The mobile-element reading is an interpretation, and co-occurrence does not prove co-selection. [src: amr_strain_variation] See [[entities/resistance-island]] and [[summaries/amr_strain_variation__REPORT]].

## Literature Context

The candidate literature establishes that mobile genetic elements (MGEs) are central to how resistance genes are acquired and spread. A review of the major MGE classes names insertion sequences, transposons, gene cassettes/integrons, plasmids and integrative conjugative elements, and says they promote the acquisition and spread of resistance genes in both Gram-negative and Gram-positive bacteria [PMID 30068738](https://pubmed.ncbi.nlm.nih.gov/30068738/). A second review lists self-replicating plasmids, prophages, transposons, integrons and resistance islands as DNA elements that frequently carry resistance genes into sensitive organisms [PMID 12190884](https://pubmed.ncbi.nlm.nih.gov/12190884/). These reviews support the general idea that MGEs mobilize resistance determinants. Their abstracts do not themselves show that genes co-occur as tight modules across a species.

Several papers describe resistance islands or comparable structures in particular taxa. In Pseudomonas aeruginosa, the modular mobile elements that carry a carbapenemase gene are called resistance islands, and a review examines their structures [PMID 33679638](https://pubmed.ncbi.nlm.nih.gov/33679638/). A review of P. aeruginosa also places many horizontally acquired genes within integrons and MGEs [PMID 31492517](https://pubmed.ncbi.nlm.nih.gov/31492517/). A review of Acinetobacter baumannii covers integrons, transposons, resistance islands and insertion sequences linked to carbapenem resistance [PMID 27522927](https://pubmed.ncbi.nlm.nih.gov/27522927/). A single Spanish P. aeruginosa isolate carried blaDIM-1 in the class 1 integron In1592 together with aminoglycoside resistance genes. The element is a fragment of the PAGI-18 genomic island, and the authors suggest independent acquisition events [PMID 41251366](https://pubmed.ncbi.nlm.nih.gov/41251366/). In eight nontyphoidal Salmonella strains, three resistance islands, six composite transposons and two integrons were found on chromosomes, and plasmids carried further AMR genes. This is a very small sample [PMID 39158311](https://pubmed.ncbi.nlm.nih.gov/39158311/). Reviews of Salmonella and Enterobacteriaceae likewise cover integrons, resistance islands and the wider mobilome [PMID 35432284](https://pubmed.ncbi.nlm.nih.gov/35432284/), [PMID 29038087](https://pubmed.ncbi.nlm.nih.gov/29038087/). Integrons can also carry phage-defense cassettes that mix with resistance cassettes [PMID 40338999](https://pubmed.ncbi.nlm.nih.gov/40338999/).

A genome-scale analysis offers the closest parallel to the corpus. It examined 3303 dairy-isolate genomes from 52 countries and tested 29,299 gene pairs. It found 523 significant associations (FDR < 0.05), including linkage between arsenic resistance and tetracycline or multidrug efflux genes (Jaccard ≥ 0.98), and it concluded that metal exposure maintains whole resistance modules through genetic linkage [PMID 41923404](https://pubmed.ncbi.nlm.nih.gov/41923404/). That study is limited to dairy-isolated pathogens and to AMR–metal associations.

The corpus's claim that mobile elements co-mobilize resistance determinants is **consistent** with these reviews. The reviews show that integrons, transposons and resistance islands carry resistance genes. The corpus's finding of 1,517 islands across 705 species (54% of those analyzed) tests this at a different scale. It is a statistical detection of co-occurring modules, whereas the clinical and taxon-specific papers mostly describe individual elements. The dairy study is a partial precedent for genome-wide co-occurrence testing. It does not cover the corpus's 88% multi-mechanism composition, so that finding is **novel** within this candidate set. The corpus's mobile-element reading rests on phi values (mean 0.827) and has not been mapped to plasmid, integron or IS context. The literature here therefore **motivates** that reading but does not confirm it. The caution that co-occurrence does not prove co-selection stands unresolved, because the dairy study's "genetic linkage" is also an inference from co-occurrence statistics.

## Detection and size

The report detected 1,517 resistance islands across 705 species, 54% of those analyzed. [src: amr_strain_variation] The central digest gives the denominator as 705/1,305 species. [src: discoveries] Mean island size was 6.2 genes (median 4, max 43). [src: amr_strain_variation, discoveries] The mean phi coefficient was 0.827, which the report reads as very tight co-occurrence within each island. [src: amr_strain_variation, discoveries] The report concludes that AMR genes are frequently co-inherited as multi-gene modules. [src: amr_strain_variation] The [[summaries/discoveries]] digest repeats the 54% of species figure and the mean size of 6.2 genes. [src: discoveries]

## Mechanism composition

Most islands combine mechanisms: 88% (1,343/1,517) contain genes from multiple resistance mechanisms. [src: amr_strain_variation, discoveries] Efflux pumps (954 islands) and enzymatic inactivation (698) are the most common components. [src: amr_strain_variation] Other mechanism counts, in numbers of islands, are listed below.

| Mechanism | Islands |
|---|---|
| Other/Unclassified | 1,026 [src: amr_strain_variation] |
| Oxidoreductase | 694 [src: amr_strain_variation] |
| Regulatory | 502 [src: amr_strain_variation] |
| Beta-lactamase | 341 [src: amr_strain_variation] |
| Target modification | 293 [src: amr_strain_variation] |
| Cell wall modification | 137 [src: amr_strain_variation] |

## Interpretation

The report suggests that multi-mechanism islands give coordinated defense against several drug classes at once. [src: amr_strain_variation, discoveries] It also suggests that the 88% multi-mechanism share reflects selection for co-maintaining complementary strategies. One example is efflux combined with enzymatic inactivation, which acts at multiple stages of antibiotic action. [src: amr_strain_variation]

For mobility, the report calls the island structure consistent with the known role of transposons, integrons and genomic islands in co-mobilizing resistance determinants (Partridge et al. 2018). [src: amr_strain_variation] It reads the high phi values as inheritance of intact mobile elements rather than random assembly. [src: amr_strain_variation]

## Proposed follow-up in the report

The report proposes mapping islands to mobile genetic element context, including plasmid versus chromosome location, integron boundaries and IS elements. [src: amr_strain_variation] It also proposes a PanKA-style predictive approach that uses island co-occurrence structure to predict which AMR genes may be co-acquired in the future. [src: amr_strain_variation]

## Tensions

- The report proposes selection for complementary strategies. [src: amr_strain_variation] It also cautions that co-occurrence does not prove co-selection and may reflect linkage on one mobile element without functional synergy. [src: amr_strain_variation] The report does not settle which explanation holds.

## Open Directions

- Map islands to plasmid versus chromosome location, integron boundaries and IS elements. This would test the mobile-element reading, which is currently inferred only from phi values.
- Build a PanKA-style model on island co-occurrence to test whether it predicts future co-acquisition.
- Compare islands with and without shared mobile-element context against functional complementarity. This would separate linkage from co-selection.
