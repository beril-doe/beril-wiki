---
type: "Concept"
description: "Whether genes that jointly support a pathway are co-located or co-regulated in operons, or coupled only by biochemistry; stops at ADP1 aromatic catabolism."
sources: ["summaries/aromatic_catabolism_network__REPORT.md"]
---
# Operon organization versus functional coupling of pathway support genes

In *Acinetobacter baylyi* ADP1, the report finds no cross-category operons linking the support subsystems of aromatic catabolism, except one within the aromatic pathway itself. It attributes their coupling to ring-cleavage biochemistry. [src: aromatic_catabolism_network] This evidence comes from one organism and one report, [[summaries/aromatic_catabolism_network__REPORT]], so it is not a general rule. See also [[concepts/support-gene-networks-around-catabolic-pathways]] and [[entities/acinetobacter-baylyi-adp1]].

## Literature Context

The candidate papers show that operon organization of aromatic catabolic genes is well documented, but that it varies between species and mostly concerns the pathway's own genes. In *Acinetobacter* sp. ADP1, the adjacent pca and qui clusters share a direction of transcription and are both induced by protocatechuate. Data suggest a large 14-kb primary transcript covering the pca and qui genes, and Northern blots identified a 12-kb transcript spanning pcaI to quiX. The authors conclude that the genes form a pca-qui operon governed by PcaU [PMID 15691962](https://pubmed.ncbi.nlm.nih.gov/15691962/). ADP1 catabolic genes also form a larger supraoperonic cluster of 30 kbp, which includes the are-ben-cat genes and the sal genes. The sal genes are organized into two convergent transcription units, salAR and salDE, according to reverse transcription-PCR [PMID 10715011](https://pubmed.ncbi.nlm.nih.gov/10715011/). That work also showed that salicylate and ethyl salicylate are channeled into the beta-ketoadipate pathway at the level of catechol.

Other taxa show different layouts. In *Sinorhizobium meliloti*, protocatechuate genes sit on the pSymB megaplasmid in two transcriptional units, pcaDCHGB and pcaIJF. These are regulated by different proteins, the LysR-type PcaQ and the IclR-type PcaR [PMID 16885292](https://pubmed.ncbi.nlm.nih.gov/16885292/). In *Pseudomonas putida*, six pca genes fall into at least three separate transcriptional units, and pcaIJ is an operon induced via pcaR [PMID 8376330](https://pubmed.ncbi.nlm.nih.gov/8376330/). In *Pseudomonas stutzeri* A1501, pathway expression is modulated by both pathway-specific and catabolite repression controls [PMID 20137101](https://pubmed.ncbi.nlm.nih.gov/20137101/). In *Acinetobacter radioresistens* S13, benzoate induces both the benzoate and the phenol catabolic operons [PMID 17483933](https://pubmed.ncbi.nlm.nih.gov/17483933/). These papers describe regulation and organization within the aromatic pathway and its peripheral branches. None of them tests whether support subsystems such as Complex I, pyrroloquinoline quinone (PQQ) biosynthesis or iron acquisition are co-located with the pathway.

The hub's within-pathway claim is consistent with this literature. The report's 12-gene pca/qui operon, pcaIJFBDCHG-quiABC plus transport genes, matches the experimentally mapped transcriptional organization in ADP1 [PMID 15691962](https://pubmed.ncbi.nlm.nih.gov/15691962/). Its finding that the only cross-category operon lies within the aromatic pathway fits the picture of catabolic genes clustering by pathway. The hub's statement that no cross-category operons link the support subsystems is not tested by these papers. It extends the literature, and it comes from one organism and one report. The Complex I operon (13 subunits, nuoA–N), the PQQ locus and the four iron loci have no counterpart in the candidate papers. The same holds for the attribution of coupling to ring-cleavage biochemistry rather than genomic co-localization, so that attribution remains an untested hypothesis here. The species differences above, such as the split pca units in *S. meliloti* and *P. putida*, also caution against generalizing from ADP1 to other aromatic degraders.

## Genomic separation of support subsystems

The four support subsystems sit at distinct places on the chromosome. The Complex I operon is at 714–729 kb, the pca/qui pathway at 1,709–1,724 kb, and pyrroloquinoline quinone (PQQ) biosynthesis at 2,461 kb. Iron acquisition genes are scattered across 4 loci. [src: aromatic_catabolism_network] The report states that no cross-category operons exist, except one within the aromatic pathway itself. [src: aromatic_catabolism_network] It concludes that the metabolic dependency is not encoded by genomic co-localization. It says the dependency emerges from the biochemistry of aromatic ring cleavage. [src: aromatic_catabolism_network]

## Co-regulation inside operons

Operon structure matters within each subsystem. The Complex I operon (see [[entities/respiratory-complex-i-nadh-ubiquinone-oxidoreductase]]) has 13 subunits (nuoA–N), all on the same strand with <100 bp intergenic distances. [src: aromatic_catabolism_network] The report describes genes within operons as tightly co-regulated, naming the 13-gene Complex I operon and the 12-gene pca/qui operon. [src: aromatic_catabolism_network] It reads the Complex I co-fitness correlation of r = 0.992 as essentially identical phenotypic profiles, consistent with single-operon co-regulation. [src: aromatic_catabolism_network] The report states that disrupting any single subunit eliminates the entire complex. It uses this to explain why 10/13 subunits independently produce quinate-specific growth defects. [src: aromatic_catabolism_network]

The operon predictions match the experimental transcriptional organization mapped by Dal et al. (2005). That work includes a 12-gene pca/qui operon spanning pcaIJFBDCHG-quiABC plus transport genes. [src: aromatic_catabolism_network] Related pathway context is in [[entities/ketoadipate-pathway]].

## Weak clustering among quinate-specific genes

The support network has 9 genomic clusters of ≥2 quinate-specific genes. Overall clustering is mild, with an observed/expected nearest-neighbour distance ratio of 0.89. [src: aromatic_catabolism_network] See [[concepts/substrate-dependent-complex-i-requirement-and-ndh-2-compensation]] for the Complex I dependence.

## Open Directions

- Repeat the cross-category operon and clustering test in other aromatic degraders. This would show whether the lack of co-localization is specific to ADP1.
- Compare transcript data for PQQ, iron and Complex I genes under quinate and non-aromatic substrates. This would test whether separate loci share regulation despite their distance.
- Test whether the 0.89 nearest-neighbour ratio differs from a permutation null that accounts for operon structure. This would show whether the 9 clusters are more than chance.
