---
type: "Concept"
description: "How the genomic capacity for lanthanide-dependent methylotrophy, marked by xoxF, is distributed across habitats, and how weakly that distribution lines up with rare-earth-element-rich environments such as REE acid mine drainage."
sources: ["summaries/lanthanide_methylotrophy_atlas__REPORT.md"]
---
# Habitat Enrichment of Lanthanide Methylotrophy Does Not Track Rare-Earth-Rich Environments

One natural expectation is that lanthanide-dependent methylotrophy would be most common where rare-earth elements (REEs) are abundant. Lanthanide-dependent methylotrophy is the use of REEs as cofactors for methanol oxidation. The [[summaries/lanthanide_methylotrophy_atlas__REPORT|lanthanide methylotrophy atlas]] tests this expectation by tracking [[entities/xoxf|xoxF]], the marker for lanthanide-dependent methanol dehydrogenase, across habitat categories. It uses per-class Fisher's exact tests against a generic environmental reference with BH-FDR correction (Benjamini-Hochberg false discovery rate control for multiple tests). Within this single project, the habitat-level statistics and the gene content of one REE-rich sample collection give only partial and uneven support to that expectation. [src: lanthanide_methylotrophy_atlas]

## Habitat-level enrichment and depletion

Two broad habitat categories are significantly enriched for xoxF. Soil/sediment had 13,779 genomes, a 6.84% xoxF rate, an odds ratio of 1.92 against the generic environmental category, and an adjusted p value of 6.1 × 10⁻³⁹. Marine samples had 15,554 genomes, a 4.76% xoxF rate, an odds ratio of 1.31 and an adjusted p value of 7.8 × 10⁻⁷. Both results rest on large genome counts with strong statistics. [src: lanthanide_methylotrophy_atlas]

Two habitat categories that might plausibly be linked to metal exposure show no significant enrichment. These are null results. Volcanic/geothermal samples had 3,450 genomes, a 3.19% xoxF rate, an odds ratio of 0.86 and an adjusted p value of 0.20. Mining samples had 1,636 genomes, a 4.10% xoxF rate, an odds ratio of 1.12 and an adjusted p value of 0.38. [src: lanthanide_methylotrophy_atlas]

The one explicitly REE-impacted category points the other way, but only descriptively. Its 37 genomes have a 10.81% xoxF rate and an odds ratio of 3.51 against the generic environmental category. However, the adjusted p value is 0.082, and the atlas states that n=37 is too small to clear the FDR threshold, which was a pre-registered caveat. The atlas rates its habitat hypothesis as only "partially supported." [src: lanthanide_methylotrophy_atlas]

Host-associated samples are strongly depleted. They had 107,600 genomes, a 0.22% xoxF rate and an odds ratio of 0.058. The table reports the adjusted p value as 0.0. The atlas reads this result as consistent with the absence of methylotrophy in the gut/host niche. [src: lanthanide_methylotrophy_atlas]

The soil/sediment enrichment also holds within Acidobacteriota, the phylum with the highest per-genome xoxF carriage (within-phylum OR=2.16, p_BH=2.2 × 10⁻⁵). The atlas takes this as a sign that at least part of the soil signal is not purely phylogenetic confounding. This check covers a single phylum. [src: lanthanide_methylotrophy_atlas]

## REE acid-mine-drainage MAGs: low carriage of known lanthanide markers

A MAG (metagenome-assembled genome) is a genome reconstructed from community sequencing data. The atlas examined 37 MAGs from samples explicitly tagged as "rare earth elements-acid mine drainage (REEs-AMD) contaminated river water". These MAGs are taxonomically diverse and **not dominated by canonical methylotrophs**. Acidophilic and metal-tolerant lineages lead the community, namely *Acidocella*, *Acidiphilium*, *Thiomonas* and *Metallibacterium*. The collection also includes multiple Burkholderiaceae_A/_B genera (*Limnohabitans*, *Rhodoferax_A*, *Trinickia*, others), Bacteroidota *Chitinophagaceae*, Actinomycetota *Acidimicrobiia*, Chloroflexota and Cyanobacteriota. A further member is the previously uncharacterised clade [[entities/reeb76|f__REEB76 / g__REEB76]], which was discovered from these samples and named after them. [src: lanthanide_methylotrophy_atlas]

Only 4/37 REE-AMD MAGs carry any xoxF, and 0/37 carry [[entities/bakta|bakta]]-validated [[entities/lanmodulin|lanmodulin]] or [[entities/xoxj|xoxJ]]. The atlas reads the functional signature as an acid-mine-drainage stress profile. It includes DNA-repair enzymes (RecN 33, RadA 32, RecO 31, RecA 28, RadC 24) and acid-resistance machinery (FtsH zinc metalloprotease 31, proton-translocating NAD(P)+ transhydrogenase 27). It also includes MerR-family heavy-metal-responsive transcriptional regulators (30) and oxidative-stress defense (thioredoxin reductase 25, glutathione peroxidase 24). Every count is out of 37 and gives the number of MAGs in which each bakta product appears. This is a descriptive analysis of a single sample collection, not a comparative test. [src: lanthanide_methylotrophy_atlas]

The negative findings cover only known, annotatable markers. The analysis is bounded by what eggNOG and bakta call, and genuinely novel REE-handling enzymes without KEGG/RefSeq homologs would not be detected. The REE-AMD MAGs therefore show low carriage of recognised lanthanide genes. They do not show an absence of all lanthanide-handling capability. [src: lanthanide_methylotrophy_atlas]

## Interpretation

Taken together, these results **weaken**, but do not refute, a simple model in which REE availability drives lanthanide-dependent methylotrophy. The statistically robust enrichments are in the broad soil/sediment and marine categories. The mining and volcanic/geothermal categories are null. In the REE-impacted genomes, xoxF is elevated relative to the baseline but not significantly. Most of these genomes lack known lanthanide markers, and their gene content is dominated by acid and metal stress functions. [src: lanthanide_methylotrophy_atlas]

The atlas suggests that the soil enrichment fits two things: methanol oxidation as a known soil process, and soil as a reservoir of lanthanide minerals. Habitat-level REE availability and methylotrophic niche therefore cannot be separated with these data. Any claim that methanol supply rather than lanthanide abundance governs where xoxF occurs remains a hypothesis. This connects to the general predominance of xoxF over mxaF discussed in [[concepts/lanthanide-dependent-methanol-dehydrogenase-predominance]]. It also connects to the narrow phylogenetic range of lanmodulin discussed in [[concepts/lanmodulin-narrow-distribution]]. [src: lanthanide_methylotrophy_atlas]

## Tensions

The habitat-scale and sample-scale views of the REE-impacted genomes pull in different directions. The 37 REE-impacted genomes show a descriptive 3.51 odds ratio for xoxF (p_BH = 0.082), yet only 4/37 REE-AMD MAGs carry any xoxF, and the collection is dominated by acidophiles rather than methylotrophs. Low absolute carriage does not rule out relative enrichment. A non-significant elevation in 37 genomes does not establish enrichment either. The mining category (OR 1.12, p 0.38) is null rather than depleted. None of these results establishes that REE-rich habitats select for or against lanthanide methylotrophy. [src: lanthanide_methylotrophy_atlas]

## Open Directions

- Gather more REE-impacted genomes or MAGs and re-run the Fisher test. This would show whether the descriptive 3.51 odds ratio, now based on n=37, clears the FDR threshold. [src: lanthanide_methylotrophy_atlas]
- Re-run the habitat enrichment with "mining" split into REE-bearing and other ore types, using BioSample isolation-source text. This tests whether pooling diverse mine environments masks an REE-specific signal. [src: lanthanide_methylotrophy_atlas]
- Compare the REE-AMD MAGs with non-REE acid-mine-drainage MAGs for xoxF, lanmodulin and the stress-gene profile. This would separate an acid/metal-stress effect from an REE effect. [src: lanthanide_methylotrophy_atlas]
- Extend the within-phylum check beyond Acidobacteriota to other xoxF-carrying phyla. This tests whether the soil/sediment and marine enrichments reflect habitat or the taxonomic makeup of methylotroph-rich lineages. [src: lanthanide_methylotrophy_atlas]
- Search the REE-AMD MAGs with structure- or motif-based methods for lanthanide-binding proteins that lack KEGG/RefSeq homologs. This would address the annotation-bounded detection limit. [src: lanthanide_methylotrophy_atlas]
