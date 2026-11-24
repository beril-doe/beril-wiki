---
type: "Concept"
description: "What the orthologous groups enriched in plant-associated species do, whether they are dark or characterized, and which mechanistic hypotheses they suggest."
sources: ["summaries/discoveries.md", "summaries/plant_microbiome_ecotypes__REPORT.md"]
---
# Functional characterization of plant-enriched gene families

After phylogenetic control, 50 eggNOG ortholog groups (OGs) distinguish plant-associated species from non-plant species. [src: discoveries] Annotation shows they are well-characterized proteins, not dark genes, but their plant-interaction mechanisms are mostly unproposed. [src: plant_microbiome_ecotypes]

## Literature Context

The candidate papers show that bacterial and fungal genes linked to plant association are often individually characterized in function but not in their plant-specific role. A transcriptome-guided study of a rhizosphere Pseudomonas found genes upregulated during root colonization and more abundant in rhizosphere communities than in bulk soils. Many had not previously been linked to plant–bacteria interactions, and some were more prevalent in plant-associated Pseudomonas genomes than in genomes from other environments [PMID 41345977](https://pubmed.ncbi.nlm.nih.gov/41345977/). A knockout of one of them, a yafL homolog encoding an NlpC/P60 family cysteine peptidase, affected root architecture and plant growth, which is functional validation for a gene of known biochemical class [PMID 41345977](https://pubmed.ncbi.nlm.nih.gov/41345977/). In the Arabidopsis root mycobiome, comparative genomics of 41 fungal isolates against 79 other plant-associated fungi identified 84 gene families associated with endophytism, including plant cell wall-degrading enzyme families (GH10, AA9) [PMID 34893598](https://pubmed.ncbi.nlm.nih.gov/34893598/). Metagenomic work on Brazilian campos rupestres plant microbiomes reported enrichment of genes for organic compound intake and for phosphorus and nitrogen turnover [PMID 36536072](https://pubmed.ncbi.nlm.nih.gov/36536072/). Other genomic studies emphasize colonization and competition traits: motility and biofilm genes in Allorhizobium vitis [PMID 41825396](https://pubmed.ncbi.nlm.nih.gov/41825396/), and biofilm regulators (wspC, rpoE, fliD) in Pseudomonas argentinensis SA190, whose mutants were differentially compromised in colonization [PMID 41310433](https://pubmed.ncbi.nlm.nih.gov/41310433/).

The corpus's central finding is that the 50 phylogenetically controlled ortholog groups are well characterized, not dark, with 50/50 eggNOG and InterProScan coverage. This is consistent with the Pseudomonas and fungal studies, where plant-associated enrichment fell on genes with recognizable biochemical classes such as peptidases, glycoside hydrolases and metabolic enzymes. It sits in partial tension with the framing of uncharacterized genes in [PMID 41345977](https://pubmed.ncbi.nlm.nih.gov/41345977/). The corpus does cite that line of work, but its own set is mostly annotated, although 19/50 OGs fall in COG category S (unknown function). The tension is partial because the Pseudomonas study used expression during colonization, while the corpus used phylum-level logistic regression across species.

The corpus's interpretation is metabolic competitiveness in the rhizosphere, with high-affinity oxidases, Fe-S biogenesis and ion transport. This is a hypothesis, and it is broadly compatible with nutrient-turnover enrichment in [PMID 36536072](https://pubmed.ncbi.nlm.nih.gov/36536072/) and with siderophore and iron-sequestration traits in [PMID 41825396](https://pubmed.ncbi.nlm.nih.gov/41825396/). None of the candidates directly tests the cbb3-oxidase or microaerobic-adaptation proposal, so that part is novel and untested here. The corpus extends the literature by providing a cross-species, phylogeny-aware enrichment list. Unlike the knockout validation in [PMID 41345977](https://pubmed.ncbi.nlm.nih.gov/41345977/), it offers no mutant evidence, and its mechanisms remain unproposed pending structural prediction or experimental work.

## The enriched set

After phylogenetic control, 50 novel eggNOG ortholog groups distinguish plant-associated species from non-plant species. [src: discoveries] The project used phylum-level logistic regression, and all 50 kept p<0.05 with OR (odds ratio) >1. [src: plant_microbiome_ecotypes] The report presents them as candidate plant–microbe interaction gene families not confounded by shared evolutionary history. [src: discoveries, plant_microbiome_ecotypes] The top hit is COG3569 (clusters of orthologous groups), with OR=6.01 phylo-controlled. [src: discoveries] See [[entities/cog3569]]. In the earlier NB03 analysis, the top OGs had these ORs:

| OG | OR |
|---|---|
| COG3569 | 8.92 [src: plant_microbiome_ecotypes] |
| COG1764 | 9.29 [src: plant_microbiome_ecotypes] |
| COG5343 | 7.74 [src: plant_microbiome_ecotypes] |
| COG0654 | 12.66 [src: plant_microbiome_ecotypes] |
| COG1845 | 14.47 [src: plant_microbiome_ecotypes] |

The report later reframed its "novel OGs" wording as "enriched gene families", because it judged "novel" an overstatement. [src: plant_microbiome_ecotypes] The 1,206,652 gene clusters carrying these OGs span 14,329–16,166 species per OG. [src: plant_microbiome_ecotypes] Phylogenetic confounding is treated more broadly in [[concepts/genome-sampling-depth-genome-size-and-phylogeny-as-confounders-of-gene-content-and-pangenome-associations]].

## Are they dark?

They are not. Phase 2 annotation (NB09) found all 50 OGs to be well-characterized proteins, none hypothetical. [src: plant_microbiome_ecotypes] Coverage was 50/50 for eggNOG descriptions and 50/50 for InterProScan domains. It was 48/50 for GO (Gene Ontology) terms, with 699 unique terms, and 39/50 for MetaCyc pathways. [src: plant_microbiome_ecotypes]

The report cites Saati-Santamaria et al. (2025), who found numerous uncharacterized genes upregulated during root colonization. It also cites Zhou et al. (2025), who reported that >99% of phyllosphere antimicrobial peptides were previously uncharacterized. [src: plant_microbiome_ecotypes]

By COG category, the unknown-function category S is the largest group of the 50 OGs:

| COG category | OGs |
|---|---|
| S, unknown function | 19/50 (38%) [src: plant_microbiome_ecotypes] |
| C, energy production | 7/50 (14%) [src: plant_microbiome_ecotypes] |
| P, inorganic ion transport | 6/50 (12%) [src: plant_microbiome_ecotypes] |
| G, carbohydrate metabolism | 4/50 (8%) [src: plant_microbiome_ecotypes] |
| Q, secondary metabolite biosynthesis | 3/50 (6%) [src: plant_microbiome_ecotypes] |

The 19 category-S OGs have characterized domains but no clear plant-interaction mechanism. The report treats them as candidates for experimental characterization. [src: plant_microbiome_ecotypes]

## Functional themes and mechanistic hypotheses

The report reads the themes as pointing to metabolic competitiveness in the rhizosphere rather than plant-specific signaling. This is an interpretation, not a tested result. [src: plant_microbiome_ecotypes]

### Electron transport and high-affinity oxidases

Electron transport and energy metabolism account for 7/50 OGs (14%). They include cytochrome c oxidase subunits, NADH (reduced nicotinamide adenine dinucleotide) dehydrogenase COG0649 and ubiquinol-cytochrome c reductase COG0723. [src: plant_microbiome_ecotypes] COG1845/ctaE has OR=14.5 and occurs in 93.2% of plant species versus 48.7% of non-plant species. [src: plant_microbiome_ecotypes] COG0843/ctaD has OR=13.7. [src: plant_microbiome_ecotypes] The report notes that cbb3-type terminal oxidases enable respiration in microaerobic root nodules and xylem. [src: plant_microbiome_ecotypes] It cites Preisig et al. (1996), who characterized the high-affinity cbb3 oxidase as essential for symbiotic nitrogen fixation in microaerobic root nodules. [src: plant_microbiome_ecotypes] From this it suggests the hypothesis that microaerobic adaptation is a key niche axis. [src: plant_microbiome_ecotypes] The report proposes measuring oxygen tolerance ranges in plant-associated versus non-plant strains to test it. [src: plant_microbiome_ecotypes]

### Iron-sulfur clusters and ion transport

The iron-sulfur biosynthesis OG COG0316/iscA occurs in 94.3% of plant species. [src: plant_microbiome_ecotypes] The report calls Fe-S clusters essential cofactors for nitrogenase, respiratory chain complexes and oxidative stress defense. [src: plant_microbiome_ecotypes] It also cites Fuangthong et al. (2015), who link IscR-mediated Fe-S regulation to pathogenicity and oxidative stress resistance in plant-associated bacteria. [src: plant_microbiome_ecotypes] See [[entities/iron-sulfur-cluster-biogenesis]]. Inorganic ion transport (6/50, 12%) fits the nutrient-acquisition demands of rhizosphere colonization. [src: plant_microbiome_ecotypes]

### Cross-reference

Cross-referencing with MGnify rhizosphere KEGG modules confirmed that 8 modules from the novel OGs are present in rhizosphere species. [src: plant_microbiome_ecotypes]

## Limits

All 50 OGs have an annotated function from NB09 but lack mechanism-level proposals. [src: plant_microbiome_ecotypes] For COG3569, COG1845, COG0843 and COG0316, the report proposes AlphaFold structural prediction or cross-referencing with biochemical pathway databases to generate testable mechanisms. [src: plant_microbiome_ecotypes]

## Open Directions

- Measure oxygen tolerance ranges in plant-associated versus non-plant strains. This would test the microaerobic-adaptation hypothesis for COG1845 and COG0843.
- Run AlphaFold structural prediction, or cross-reference pathway databases, for COG3569, COG1845, COG0843 and COG0316. This would turn their broad classifications into testable plant-interaction mechanisms.
- Test the 19 category-S OGs experimentally, for example with mutants in root colonization assays. This would address the missing mechanism for characterized domains.
- Compare enrichment of the cbb3 oxidase OGs between nodule-forming and other plant-associated species. This would show whether the signal tracks microaerobic niches.
