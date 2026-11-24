---
type: "Concept"
description: "Whether plant-growth-promoting (PGP) genes such as pqqC, acdS, hcnC, ipdC and nifH co-occur across species, forming modules or separate ecological guilds; stops at gene-level presence/absence, not physical linkage."
sources: ["summaries/discoveries.md", "summaries/pgp_pangenome_ecology__REPORT.md"]
---
# Co-occurrence of plant-growth-promoting genes and trait guilds

This page asks whether plant-growth-promoting (PGP) genes co-occur across bacterial species as modules or fall into separate ecological guilds. It stops at gene-level presence/absence and says nothing about physical linkage. The discoveries digest reports that pqqC and acdS co-occur strongly and that nifH sits in a separate guild. [src: discoveries] The pgp_pangenome_ecology report reports species-level associations across 11,272 species with at least one PGP gene. [src: pgp_pangenome_ecology]

## Literature Context

The candidate papers are mostly culture-based screens of rhizobacteria, and they give the field context for the hub's gene-level question. A review describes PGPR as using many mechanisms, including phosphate solubilization, siderophore production, biological nitrogen fixation, ACC deaminase production and phytohormone production [PMID 22805914](https://pubmed.ncbi.nlm.nih.gov/22805914/). Several isolate studies report these traits together in single strains. In one study, 13 nitrogen-fixing strains from 11 genera were all positive for ACC deaminase and IAA (indole-3-acetic acid) production. Each strain had at least four PGP properties besides nitrogen fixation [PMID 23553337](https://pubmed.ncbi.nlm.nih.gov/23553337/). Isolates from wheat, coffee, quinoa, durum wheat and barley rhizospheres likewise combined ACC deaminase with phosphate solubilization, IAA, siderophore production or nitrogen fixation [PMID 42924626](https://pubmed.ncbi.nlm.nih.gov/42924626/), [PMID 40219151](https://pubmed.ncbi.nlm.nih.gov/40219151/), [PMID 40197892](https://pubmed.ncbi.nlm.nih.gov/40197892/), [PMID 32574514](https://pubmed.ncbi.nlm.nih.gov/32574514/), [PMID 31396175](https://pubmed.ncbi.nlm.nih.gov/31396175/), [PMID 32849698](https://pubmed.ncbi.nlm.nih.gov/32849698/). Azospirillum brasilense EMCC1454 showed nitrogen fixation, phosphate solubilization, siderophore, ACC deaminase and IAA activities together [PMID 37299089](https://pubmed.ncbi.nlm.nih.gov/37299089/). A phytase screen of 73 isolates found that Pseudomonas had the most isolates (36) and the highest average phytase activity. It also showed multiple PGP traits [PMID 36687657](https://pubmed.ncbi.nlm.nih.gov/36687657/).

These studies are phenotypic. Most select isolates for ACC deaminase or for several PGP traits, and they test few strains. One quinoa screen is a partial exception: only three of 51 strains (6%) showed PGP activities including IAA production, phosphate solubilization, growth in nitrogen-free medium and ACC deaminase production at 6 and 15 °C [PMID 32574514](https://pubmed.ncbi.nlm.nih.gov/32574514/). None of these papers tests co-occurrence statistically across species, and none measures gene presence or absence.

The corpus's pqqC–acdS module (OR = 7.24, n = 286 species, q = 1.2e-83) is consistent with the repeated finding that phosphate solubilization and ACC deaminase appear together in effective isolates. The candidate papers do not quantify that pairing, so the pangenome-scale estimate extends the literature rather than replicating it. The hcnC and ipdC links to pqqC are also not addressed by the candidates. One study found hydrocyanic acid production negative in all 13 nitrogen-fixing strains [PMID 23553337](https://pubmed.ncbi.nlm.nih.gov/23553337/). That fits the corpus's negative nifH–hcnC association (OR = 0.23), but it is a small phenotypic observation and does not confirm it.

The corpus's nifH guild is in some tension with the isolate literature. Several studies report nitrogen fixation alongside ACC deaminase and phosphate solubilization in the same strains [PMID 23553337](https://pubmed.ncbi.nlm.nih.gov/23553337/), [PMID 37299089](https://pubmed.ncbi.nlm.nih.gov/37299089/). The corpus reports nifH as negatively associated with pqqC (OR = 0.57), though nifH + pqqC is still the second most common multi-trait genotype (n = 225). These views can coexist if multi-trait diazotrophs are a minority of lineages. The candidate papers do not test that explanation. The physical linkage of pqqC and acdS remains untested in both the corpus and the literature.

## The pqqC–acdS module

Across 27K GTDB species, pqqC (phosphate solubilization) and acdS (ACC deaminase; ACC is 1-aminocyclopropane-1-carboxylate) co-occur at OR = 7.24 (OR is odds ratio). This is far stronger than any other PGP gene pair. [src: discoveries] The pgp_pangenome_ecology report gives the same estimate: n = 286 co-occurring species, q = 1.2e-83. It reads this as phosphate solubilization (PQQ, pyrroloquinoline quinone, cofactor biosynthesis) and ethylene reduction being nearly always found together when either is present. [src: pgp_pangenome_ecology]

The report calls the module tightly co-selected (OR = 7.24), strongly rhizosphere-enriched (acdS OR = 7.0) and vertically inherited as part of the core genome. [src: pgp_pangenome_ecology] It says the result matches trait co-occurrence seen in curated effective-inoculant collections (Glick 2014; Vejan et al. 2016). It calls this the first demonstration at pangenome scale. [src: pgp_pangenome_ecology] It concludes that the canonical PGPB phenotype selected in agricultural inoculants is built around pqqC + acdS, not around nitrogen fixation. [src: pgp_pangenome_ecology]

## Wider rhizosphere module: hcnC and ipdC

pqqC also co-occurred significantly with hcnC (OR = 1.91) and ipdC (OR = 1.55). The report describes these links as a coherent "rhizosphere effectiveness" module. [src: pgp_pangenome_ecology] The report also suggests the hcnA–hcnC operon is part of the rhizosphere niche toolkit, since hcnC is soil-enriched (OR = 1.85). [src: pgp_pangenome_ecology]

The trp→ipdC coupling (OR = 2.81) holds in non-soil species but reverses in soil species, likely because soil PGPB acquire tryptophan exogenously from root exudates. [src: discoveries] See [[concepts/aromatic-amino-acid-biosynthesis-and-auxin-pathway-gene-coupling]].

## nifH as a separate guild

nifH forms a separate ecological guild. It is negatively associated with pqqC and hcnC and depleted in soil relative to aquatic environments. [src: discoveries] In the PGP species analysis, nifH was negatively associated with hcnC (OR = 0.23, q = 5.8e-29) and with pqqC (OR = 0.57, q = 2.9e-19). [src: pgp_pangenome_ecology] It showed no significant association with ipdC (OR = 1.13, q = 0.54). [src: pgp_pangenome_ecology] The report concludes that nitrogen fixers have different co-occurrence partners and environmental distribution. [src: pgp_pangenome_ecology] It reads diazotrophs as a guild separate from pqqC/acdS-bearing rhizobacteria, and the classical PGPB suite as mostly non-diazotrophic. [src: pgp_pangenome_ecology] See bacterial nitrogen fixation nif genes.

## Overall extent

Across 11,272 species with at least one PGP gene, 8 of 10 focal-gene pairs were significantly associated after BH-FDR correction (Benjamini-Hochberg false discovery rate). [src: pgp_pangenome_ecology] Five pairs were positive and three were negative. [src: pgp_pangenome_ecology] Multi-trait genomes are rare: only 157 species (1.4%) carry ≥3 focal traits. [src: pgp_pangenome_ecology] The most common multi-trait genotype is pqqC + acdS (n = 153). [src: pgp_pangenome_ecology] nifH + pqqC follows (n = 225). Despite their negative overall association, these two co-occur in some generalist lineages. [src: pgp_pangenome_ecology]

## Follow-up the report proposes

The report proposes testing whether pqqC and acdS are physically co-located (same genomic island or operon) or at separate loci. This would separate operon linkage from independent co-selection. [src: pgp_pangenome_ecology] It calls for comparing marine/aquatic diazotrophs (cyanobacteria, Azotobacter) with legume-symbiotic rhizobia and free-living soil diazotrophs in genome structure and PGP trait co-occurrence. [src: pgp_pangenome_ecology] It proposes a focused study of hcnA-C phylogeny and co-occurrence with biocontrol phenotypes. [src: pgp_pangenome_ecology] It also proposes cross-referencing species carrying pqqC + acdS + hcnC with commercial inoculant strains, to see whether the genomic signature predicts inoculant efficacy. [src: pgp_pangenome_ecology]

## Tensions

- nifH and pqqC are negatively associated overall (OR = 0.57). [src: pgp_pangenome_ecology] Yet nifH + pqqC is the second most common multi-trait genotype (n = 225). [src: pgp_pangenome_ecology] The report reconciles this by pointing to generalist lineages. [src: pgp_pangenome_ecology]

## Open Directions

- Locate pqqC and acdS on assembled genomes to test operon linkage against independent co-selection, which gene-level presence/absence cannot do.
- Stratify nifH-bearing species by lifestyle (marine, symbiotic, free-living soil) and compare their PGP co-occurrence, to explain the aquatic depletion in soil.
- Examine the generalist lineages carrying both nifH and pqqC, to see what lets them escape the negative association.
- Link pqqC + acdS + hcnC species to inoculant strain lists to check the module against known effective inoculants.
