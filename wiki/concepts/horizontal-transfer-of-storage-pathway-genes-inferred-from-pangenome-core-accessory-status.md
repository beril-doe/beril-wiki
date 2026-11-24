---
type: "Concept"
description: "Using discordance between gene presence and family-level prevalence, plus core versus accessory placement, to infer horizontal gene transfer; limited by the proxy nature of the evidence."
sources: ["summaries/phb_granule_ecology__REPORT.md"]
---
# Horizontal transfer of storage-pathway genes inferred from pangenome core/accessory status

This page covers horizontal transfer of storage-pathway genes inferred from pangenome core/accessory status. The phb_granule_ecology report infers HGT of phaC from two proxies: discordance between a species' phaC status and its family's prevalence, and accessory placement of the gene. [src: phb_granule_ecology] The evidence is indirect and comes from one report, which itself proposes a direct phylogenetic test. [src: phb_granule_ecology] See also [[summaries/phb_granule_ecology__REPORT]] and [[concepts/core-versus-accessory-partitioning-of-gene-functions-and-trait-genes]].

## Literature Context

The candidate papers show that horizontal gene transfer (HGT) of polyhydroxyalkanoate (PHA) genes has been inferred many times, mostly by phylogenetic methods rather than by core/accessory placement. A comparison of 253 sequenced genomes found discrepancies between the phaA, phaB and phaC trees, which suggested that HGT may be a major contributor to PHA pathway evolution. Twenty four organisms were found to be involved in HGT [PMID 17113245](https://pubmed.ncbi.nlm.nih.gov/17113245/). A Halomonas sp. TD01 comparative genomics study found that PHA synthase, depolymerase, regulator and phasin showed different HGT events between strains. This was an in silico analysis of one draft genome and its relatives [PMID 22040376](https://pubmed.ncbi.nlm.nih.gov/22040376/). In Betaproteobacteria (66 genomes), the organization of PHA gene clusters pointed to an influence of HGT [PMID 30062554](https://pubmed.ncbi.nlm.nih.gov/30062554/).

Several papers give more direct or lineage-specific evidence. In 859 Pseudomonas genomes, several phaC genes lay inside putative genomic islands, phages and plasmids, which supports acquisition by multiple horizontal routes [PMID 40674104](https://pubmed.ncbi.nlm.nih.gov/40674104/). In SAR11, Pha proteins sat on a long branch. The authors reported an origin at the common ancestor of the brackish IIIa and freshwater LD12 subclades, followed by horizontal transfer within SAR11 [PMID 40305681](https://pubmed.ncbi.nlm.nih.gov/40305681/). A Halovibrio sp. HP20-59 genome showed a phaC with 91% similarity to Halovibrio variabilis and 89% similarity to the Vreelandella genus, which the authors say suggests possible HGT of the cluster [PMID 41520089](https://pubmed.ncbi.nlm.nih.gov/41520089/). An extracellular depolymerase (PhaZ) gene in Alteromonas was present in 4/20 strains examined. Its differing genomic context suggested transfer after a certain degree of species division [PMID 40500476](https://pubmed.ncbi.nlm.nih.gov/40500476/). In Accumulibacter, ancestral genome reconstruction identified 135 laterally derived genes, including some in glycogen and PHA metabolism [PMID 27128993](https://pubmed.ncbi.nlm.nih.gov/27128993/). A Himalayan isolate survey suggested possible HGT of phaC among distant taxa from partial phaC phylogenies [PMID 29912320](https://pubmed.ncbi.nlm.nih.gov/29912320/).

The hub's inference of phaC transfer is consistent with this literature in direction. The hub reports 311 putative acquisitions, and 60.1% of those species carry accessory phaC, against 32.3% across all phaC-carrying species. The hub also names Pelagibacteraceae, with 13 putative acquisitions, as a recipient lineage. That fits the SAR11 phylogenetic evidence for within-clade transfer [PMID 40305681](https://pubmed.ncbi.nlm.nih.gov/40305681/). Likewise, the wider Pseudomonas and Halomonas results agree that PHA genes move between lineages [PMID 40674104](https://pubmed.ncbi.nlm.nih.gov/40674104/), [PMID 22040376](https://pubmed.ncbi.nlm.nih.gov/22040376/). The hub's contribution is new in scale. It uses pangenome-wide family prevalence and core/accessory status as proxies across many families, where the candidate papers use trees or mobile-element context in selected genomes.

The candidates also show why the proxy is only indirect. The tree-based and mobile-element studies used evidence the hub lacks: incongruent gene trees and islands, phages or plasmids [PMID 17113245](https://pubmed.ncbi.nlm.nih.gov/17113245/), [PMID 40674104](https://pubmed.ncbi.nlm.nih.gov/40674104/). A Paracoccaceae study found PHA genes in the soft-core genome of a family with extensive mobile-element evidence of HGT. That study did not test whether the PHA genes themselves were transferred [PMID 41276040](https://pubmed.ncbi.nlm.nih.gov/41276040/). It therefore does not contradict the hub, but it shows that gene placement and lineage-level HGT are separate questions. The hub's own proposed phaC gene tree against species tree test follows the approach of these phylogenetic studies and would settle the question directly.

## How the inference works

The pangenome analysis calls a gene cluster core if it is present in >90% of genomes within a species, and accessory otherwise. [src: phb_granule_ecology] The report counts 311 potential acquisition events: species that carry phaC although they sit in families with <20% phaC prevalence. [src: phb_granule_ecology] It also counts 278 potential loss events: species that lack phaC in families with >80% prevalence. [src: phb_granule_ecology] Overall, 5,371 species carry core phaC and 1,959 carry accessory phaC, and some species carry both types of copies. [src: phb_granule_ecology]

## Evidence for transfer

Discordant species carry phaC as an accessory gene more often than phaC-carrying species overall. Among the 311 discordant phaC-positive species, 60.1% carry accessory phaC, against 32.3% across all phaC-carrying species. [src: phb_granule_ecology] The report reads this as strong support for horizontal acquisition. Its reasoning is that recently transferred genes have not yet been fixed in the core genome. [src: phb_granule_ecology] It calls this pangenome-scale evidence for ongoing transfer, consistent with earlier single-species case studies. [src: phb_granule_ecology] It also calls it the first systematic quantification of phaC HGT frequency. [src: phb_granule_ecology]

The report cites Kalia et al. (2007) and Catone et al. (2014) as documenting phaC HGT in individual species. [src: phb_granule_ecology] It cites Cai et al. (2011) as showing distinct HGT patterns for different PHA pathway genes in *Halomonas*. [src: phb_granule_ecology]

### Families and lineages

The report finds extensive HGT across Lachnospiraceae, Chitinophagaceae, Pelagibacteraceae and Enterobacteriaceae, and interprets it as widespread. [src: phb_granule_ecology] Putative acquisitions and family phaC prevalence are listed below.

| Family | Putative acquisitions | Family phaC prevalence |
|---|---|---|
| Lachnospiraceae | 38 [src: phb_granule_ecology] | 3.1% [src: phb_granule_ecology] |
| Chitinophagaceae | 22 [src: phb_granule_ecology] | 12.4% [src: phb_granule_ecology] |
| Pelagibacteraceae | 13 [src: phb_granule_ecology] | 5.3% [src: phb_granule_ecology] |
| Enterobacteriaceae | 11 [src: phb_granule_ecology] | 2.3% [src: phb_granule_ecology] |
| Planococcaceae | 10 [src: phb_granule_ecology] | 12.8% [src: phb_granule_ecology] |

The report also says the high accessory fractions in SAR324, Bacillota_A and Eremiobacterota suggest these lineages are active recipients of phaC via HGT. [src: phb_granule_ecology] For the group, see [[entities/bacillota-a]].

## Limits

Both proxies are indirect. Family-level discordance and accessory status do not show transfer directly. The report itself proposes reconstructing a phaC gene tree and comparing it with the species tree. That would identify incongruent HGT branches directly, instead of relying on the core/accessory proxy. [src: phb_granule_ecology] The acquisition and loss counts are labelled "potential" or "putative". [src: phb_granule_ecology]

## Open Directions

- Build a phaC gene tree and test it for incongruence with the species tree. This replaces the core/accessory proxy with direct evidence.
- Test whether accessory phaC in discordant species sits on mobile elements or in genomic islands. This would separate recent transfer from other causes of accessory status.
- Check whether the 278 putative loss events in high-prevalence families are real losses or annotation gaps.
- Compare accessory rates for other PHA pathway genes, following the gene-specific patterns Cai et al. reported in *Halomonas*.
