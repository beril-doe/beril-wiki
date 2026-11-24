---
type: "Concept"
description: "Species-level association between prophage marker density and the number of distinct AMR genes, its robustness to genome count and phylogeny, and candidate mechanisms; stops short of proof of phage-mediated transfer."
sources: ["summaries/prophage_amr_comobilization__REPORT.md"]
---
# Prophage density and AMR repertoire breadth across species

Species-level association between prophage marker density and the number of distinct AMR genes, its robustness to genome count and phylogeny, and candidate mechanisms; stops short of proof of phage-mediated transfer.

## Literature Context

The candidate papers show that phage-mediated movement of resistance genes is experimentally documented in several taxa, mostly by generalized transduction. In Staphylococcus aureus USA300, phages φ80α and φJB transduced penicillinase and tetracycline resistance plasmids between clinical isolates at 10^-5 to 10^-6 CFU/PFU [PMID 22553940](https://pubmed.ncbi.nlm.nih.gov/22553940/). In Acinetobacter baumannii, phage-enveloped DNA carried chromosomal ARGs between strains without cell contact, which the authors attribute to generalized transduction [PMID 31138576](https://pubmed.ncbi.nlm.nih.gov/31138576/). In Salmonella Typhimurium, carbadox and fluoroquinolones induced prophages that transferred plasmid and chromosomal DNA, including resistance genes, in vitro [PMID 24575089](https://pubmed.ncbi.nlm.nih.gov/24575089/) [PMID 26078016](https://pubmed.ncbi.nlm.nih.gov/26078016/). A study of nasal MRSA carriers (38 patients) found free phages in nearly half of them. Those phages transduced resistance genes in vitro, and the mobile-element profiles varied while the core genomes stayed stable [PMID 25957384](https://pubmed.ncbi.nlm.nih.gov/25957384/). A review of Streptococcus pyogenes phages likewise describes generalized transduction of antibiotic resistance [PMID 31111820](https://pubmed.ncbi.nlm.nih.gov/31111820/). A large streptococcal prophage family, SMphages, carries twenty-five ARGs and transfers by conjugation. The authors note that whether prophages harbor and transmit ARGs is still debated [PMID 37369704](https://pubmed.ncbi.nlm.nih.gov/37369704/).

Some papers support the second mechanism the hub proposes, in which prophage-rich genomes gain genes through wider recombination and mobile-element activity. In Vibrio cholerae, prophage-dependent predation of neighbors enhanced horizontal gene transfer by natural transformation in chitin microcosms. That route is not transduction [PMID 33177216](https://pubmed.ncbi.nlm.nih.gov/33177216/). Genome surveys also find prophages beside ARGs and other mobile elements. Examples are 379 prophage-like elements in 120 Ralstonia genomes, some encoding antibiotic resistance genes [PMID 33626339](https://pubmed.ncbi.nlm.nih.gov/33626339/), and two multidrug-resistant bovine mastitis E. coli genomes with an open pangenome [PMID 41326987](https://pubmed.ncbi.nlm.nih.gov/41326987/). Those two genome studies are descriptive and do not test an association across species. One food metagenome study found no ARGs in prophages, insertion sequences or transposons within its 76 recovered MAGs [PMID 40436596](https://pubmed.ncbi.nlm.nih.gov/40436596/). That result concerns ARG placement within MAGs from fermented foods. It does not test a species-level association, so it neither supports nor contradicts the corpus.

The corpus reports a positive correlation between prophage marker density and AMR repertoire breadth across 4,770 species (Spearman rho=0.572). It holds after controlling for genome count (partial rho=0.464) and within five phyla (rho from 0.29 to 0.59). This is consistent with the literature, because the experimental papers show that prophages can move resistance genes. It extends that literature to a pangenome-wide scale. None of the candidate papers measures a species-level correlation, so the scale of the corpus result is novel relative to this evidence. The experimental work covers single species, often in vitro, with named taxa such as Staphylococcus, Salmonella and Acinetobacter. It cannot show that transduction explains the corpus pattern. The corpus's own caveat stands: open pangenomes may accumulate both prophages and AMR genes independently. The open pangenome reported in the mastitis E. coli genomes shows that such pangenomes carry both element types [PMID 41326987](https://pubmed.ncbi.nlm.nih.gov/41326987/). It does not separate the explanations. The corpus is therefore consistent with the transfer literature but does not prove phage-mediated transfer.

## The species-level association

Prophage marker density correlates positively with AMR repertoire breadth (Spearman rho=0.572, p<10^-300, n=4,770 species). [src: prophage_amr_comobilization] See [[entities/spearman-rank-correlation]]. The report also gives rho=0.608 (p<10^-300) for prophage/genome versus AMR/genome. [src: prophage_amr_comobilization] These are two different measures, so each is stated on its own.

A log-log regression gives a slope of 0.823 (SE=0.018, standard error), p<10^-300. [src: prophage_amr_comobilization] A 10-fold increase in prophage density predicts a ~6.6-fold increase in AMR breadth (slope=0.823, R²=0.30). [src: prophage_amr_comobilization] The report says prophage density explains 30% of the variance in AMR breadth, and calls it a stronger predictor than previously documented. [src: prophage_amr_comobilization]

For context, of 27,702 species in the pangenome, 14,669 (52.9%) carry both AMR and prophage markers. [src: prophage_amr_comobilization]

## Robustness

After controlling for genome count, the association persists (partial Spearman rho=0.464, p=1.0×10^-253). [src: prophage_amr_comobilization] The report says this extends earlier work from ~100 species to 4,770 species, and that it controls genome count rather than capsule presence. [src: prophage_amr_comobilization]

The correlation is significant in each of five major phyla. The values are:

| Phylum | rho |
|---|---|
| Pseudomonadota | 0.54 [src: prophage_amr_comobilization] |
| Bacillota_A | 0.55 [src: prophage_amr_comobilization] |
| Bacillota | 0.40 [src: prophage_amr_comobilization] |
| Bacteroidota | 0.59 [src: prophage_amr_comobilization] |
| Actinomycetota | 0.29 [src: prophage_amr_comobilization] |

The report reads this pan-phylogenetic consistency as arguing against phylogenetic confounding. [src: prophage_amr_comobilization]

## Candidate mechanisms

The report names two non-exclusive mechanisms. First, prophages may directly mobilize resistance genes by specialized or generalized transduction. [src: prophage_amr_comobilization] Second, species with many prophages may have high recombination potential and so acquire genes more readily from other mobile elements. [src: prophage_amr_comobilization] The report offers both as consistent with the association. [src: prophage_amr_comobilization]

The report's caveat is that species with open pangenomes may independently accumulate both prophages and AMR genes. [src: prophage_amr_comobilization] This alternative would produce the same species-level correlation without any phage-mediated transfer.

## Open Directions

- Test whether AMR genes sit on or next to prophage regions within genomes. This would separate direct transduction from shared accumulation.
- Add pangenome openness as a covariate, or stratify by it, to test the open-pangenome explanation.
- Repeat the analysis with a phylogenetic comparative method, such as phylogenetic generalized least squares, to test the phylogenetic-confounding argument directly.
- Explain why Actinomycetota (rho=0.29) is weaker than Bacteroidota (rho=0.59). Check whether the cause is marker detection or biology.
