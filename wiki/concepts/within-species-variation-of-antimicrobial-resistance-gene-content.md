---
type: "Concept"
description: "How AMR gene prevalence is distributed across strains within a species (fixed, variable, rare), how it relates to pangenome class and openness, and where it stops: not co-occurrence or phylogeny."
sources: ["summaries/amr_environmental_resistome__REPORT.md", "summaries/amr_pangenome_atlas__REPORT.md", "summaries/amr_strain_variation__REPORT.md", "summaries/discoveries.md"]
---
# Within-species variation of antimicrobial resistance gene content

Within a bacterial species, most antimicrobial resistance (AMR) genes are not shared by all strains. In the amr_strain_variation analysis of 1,305 species and 180,025 genomes, about half of AMR gene-species occurrences are rare, and few are fixed. [src: amr_strain_variation] The atlas conservation class predicts this within-species prevalence well, but the evidence here does not show which genes co-occur or how they follow phylogeny. The central figures come from one report, repeated in the discoveries digest. [src: discoveries]

## Literature Context

The candidate papers are single-species or small-cohort genomic studies. They broadly agree that resistance genes sit mostly in the accessory genome, with exceptions for intrinsic genes. In a culture-enriched gut microbiome study, *E. cloacae* contigs carried resistance genes that belonged to the core genome. *E. coli* had a large accessory resistome near mobile elements [PMID 30953542](https://pubmed.ncbi.nlm.nih.gov/30953542/). That fits the hub's split between intrinsic genes as core residents and acquired genes as accessory. In *Clostridium paraputrificum*, 15 antimicrobial resistance genes were identified among 42 global strains. The authors report that the majority of clinically relevant genes, especially drug-resistance genes, were accessory and likely acquired by horizontal transfer [PMID 41318693](https://pubmed.ncbi.nlm.nih.gov/41318693/). In *Elizabethkingia anophelis* (540 genomes), resistance factors were found in both the core and accessory genomes. The accessory ones were often tied to mobile elements within specific lineages [PMID 39472795](https://pubmed.ncbi.nlm.nih.gov/39472795/). Reports for *Morganella* (166 isolates) and *C. perfringens* describe acquired resistance genes carried on mobile elements or plasmids [PMID 35196820](https://pubmed.ncbi.nlm.nih.gov/35196820/), [PMID 32975504](https://pubmed.ncbi.nlm.nih.gov/32975504/).

Several papers also tie resistance variation to pangenome openness and lineage. *C. perfringens* has a very open pangenome, and its ARG number increased with isolation time in a correlation analysis [PMID 32975504](https://pubmed.ncbi.nlm.nih.gov/32975504/). Another *C. perfringens* study reported an open pangenome with 18.28% core genes and 81.72% accessory genes [PMID 41038457](https://pubmed.ncbi.nlm.nih.gov/41038457/). Among *Salmonella* serovars, the more closed typhoidal pangenomes carried fewer antimicrobial genes per genome in Paratyphi A than in Typhi. Resistance content therefore differs even between closely related lineages [PMID 40394957](https://pubmed.ncbi.nlm.nih.gov/40394957/). Similar accessory-gene dynamics are described for *S. aureus* [PMID 15276614](https://pubmed.ncbi.nlm.nih.gov/15276614/) and for multiresistant *P. paraeruginosa* (82 strains), where most differences lie in regions of genomic plasticity [PMID 40709931](https://pubmed.ncbi.nlm.nih.gov/40709931/).

The corpus's central findings are consistent with this literature. These are the 51.3% rare, 41.3% variable and 7.5% fixed split, the 99% accessory share in *K. pneumoniae* and *S. aureus*, and the match between conservation class and within-species prevalence. The corpus extends the literature by quantifying prevalence classes across 1,305 species and 180,025 genomes. The cited papers cover one species or a few at a time, and none gives fixed, variable and rare fractions. The corpus's weak negative correlation between AMR variability and pangenome openness (Spearman rho = -0.193) is not directly tested by these papers. The open-pangenome species above (*C. perfringens*, *E. anophelis*) are descriptive cases, not tests. The hub's rare-gene deflation explanation therefore remains a hypothesis. The candidates also do not address co-inherited resistance islands or ecotypes, so the hub's boundary on those topics stands.

The Salmonella and Morganella papers suggest that lineage or genospecies structure may shape resistance content. This supports the hub's caution that prevalence alone does not capture phylogeny or co-occurrence.

## Distribution of prevalence classes

Most AMR gene-species occurrences are rare or variable. 51.3% are rare (present in <=5% of strains), 41.3% are variable (5-95%), and only 7.5% are fixed (>=95%). [src: amr_strain_variation] The central digest repeats these figures. [src: discoveries] The report concludes that over 90% of occurrences are variable or rare. [src: amr_strain_variation] It also states that 51% of AMR genes are rare within any given species. [src: amr_strain_variation] The analysis covers 37,444 AMR gene-species records. [src: amr_strain_variation]

The median variability index is 0.526, which the report reads as over half of a species' AMR genes falling in the variable zone. [src: amr_strain_variation] The median pairwise Jaccard distance between strains is 0.435. The report reads this as strains of a species sharing less than 60% of their AMR repertoire. [src: amr_strain_variation, discoveries]

Median variability index differs modestly between phyla:

- Bacillota: 0.487 across 248 species. [src: amr_strain_variation]
- Bacillota_C: 0.500 across 21 species. [src: amr_strain_variation]
- Bacteroidota: 0.509 across 100 species. [src: amr_strain_variation]
- Pseudomonadota: 0.533 across 591 species. [src: amr_strain_variation]
- Actinomycetota: 0.533 across 133 species. [src: amr_strain_variation]
- Bacillota_A: 0.600 across 184 species. [src: amr_strain_variation]

## Relation to pangenome class

Atlas conservation class tracks within-species prevalence. This is the report's validation of the classification at strain resolution. [src: amr_strain_variation] See also [[concepts/core-versus-accessory-partitioning-of-gene-functions-and-trait-genes]].

- Core AMR genes: 77.3% fixed, 22.7% variable, 0.0% rare. [src: amr_strain_variation]
- Auxiliary genes: 0.0% fixed, 57.3% variable, 42.7% rare. [src: amr_strain_variation]
- Singleton genes: 0.0% fixed, 21.3% variable, 78.7% rare. [src: amr_strain_variation]

The digest summarises this as core genes 77% fixed and singletons 79% rare. [src: discoveries]

The species-level counts in amr_environmental_resistome show the same pattern. Almost all AMR clusters are accessory:

- K. pneumoniae: 13,637 genomes, 1,115 AMR clusters, 7 core, 1,108 accessory (99%). [src: amr_environmental_resistome]
- S. aureus: 13,274 genomes, 642 AMR clusters, 9 core, 633 accessory (99%). [src: amr_environmental_resistome]
- S. enterica: 10,097 genomes, 836 AMR clusters, 11 core, 825 accessory (99%). [src: amr_environmental_resistome]
- S. pneumoniae: 7,944 genomes, 59 AMR clusters, 1 core, 58 accessory (98%). [src: amr_environmental_resistome]
- M. tuberculosis: 6,673 genomes, 44 AMR clusters, 4 core, 40 accessory (91%). [src: amr_environmental_resistome]

The report says nearly the whole *K. pneumoniae* resistome is accessory. [src: amr_environmental_resistome] See [[entities/klebsiella-pneumoniae]]. The amr_pangenome_atlas report interprets intrinsic genes (ampC beta-lactamases, emhABC efflux, rox rifampin monooxygenases) as core residents present in >95% of genomes within a species. [src: amr_pangenome_atlas] It describes acquired genes (blaTEM, tet cassettes, ant(2'')-Ia) as fully accessory, often 0% core, appearing as singletons or in a minority of genomes. [src: amr_pangenome_atlas] See [[concepts/intrinsic-versus-acquired-resistance-gene-conservation]].

## Pangenome openness

AMR variability weakly anti-correlates with pangenome openness (Spearman rho = -0.193, p = 2.2e-12). The digest calls this unexpected. [src: amr_strain_variation, discoveries] The report proposes, as a hypothesis, that open-pangenome species accumulate more rare or singleton AMR genes below the 5% threshold. That would deflate an index that measures the 5-95% zone. [src: amr_strain_variation, discoveries] See [[concepts/pangenome-openness-and-its-correlates]].

## Where the picture stops

This page covers prevalence only. The report states that the variation is organised into co-inherited resistance islands, tracks phylogenetic structure, and in some species forms ecotypes. [src: amr_strain_variation] It finds distinct AMR subtypes in 19.5% of species. [src: amr_strain_variation] Those results are outside this page's scope. See [[concepts/amr-ecotypes-and-environmental-association]]. The report also claims the patterns are general bacterial features, not limited to well-studied clinical species. [src: amr_strain_variation] It claims to be the first systematic simultaneous quantification across >1,300 species. [src: amr_strain_variation]

Caveats limit these numbers:
- Some singleton AMR clusters may be annotation artifacts rather than true species-specific genes. [src: amr_pangenome_atlas]
- Sparsely annotated (1-source) clusters are enriched for singletons (55.4% vs 34.6%). [src: amr_pangenome_atlas]
- Identification relies on the AMRFinderPlus database, so novel mechanisms absent from it are missed. [src: amr_strain_variation] See [[entities/amrfinderplus]].
- Several species above are dominated by clinical isolates: K. pneumoniae Clinical (80%), S. aureus Clinical (85%), S. pneumoniae Clinical (99.6%), M. tuberculosis Clinical (98%). [src: amr_environmental_resistome]

## Open Directions

- Test the openness hypothesis by recomputing variability after removing genes below the 5% threshold, or by using a fixed-size genome subsample per species. This would show whether rare-gene accumulation causes the negative correlation.
- Re-estimate rare-class fractions after excluding singleton clusters supported by one annotation source. This would show how much of the 51.3% rare share is annotation artifact.
- Compare prevalence-class fractions within the clinically dominated species against less-sampled species. This would separate biology from sampling skew.
- Add a validation set of resistance mechanisms missing from AMRFinderPlus to estimate how much variation goes undetected.
