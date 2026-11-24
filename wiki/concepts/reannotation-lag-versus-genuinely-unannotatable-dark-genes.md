---
type: "Concept"
description: "How many genes labelled hypothetical are resolved by newer annotation pipelines versus remain unannotated, the properties of those that resist, and where archaeal and database-coverage bias enters; stops short of experimental function assignment."
sources: ["summaries/discoveries.md", "summaries/functional_dark_matter__REPORT.md", "summaries/truly_dark_genes__REPORT.md"]
---
# Reannotation lag versus genuinely unannotatable dark genes

Bakta reannotation resolves most Fitness Browser (FB) dark genes with pangenome links, and a smaller residue stays hypothetical. [src: discoveries] Of 39,532 such genes, Bakta v1.12.0 reclassifies 33,105 (83.7%) and leaves 6,427 called hypothetical by both pipelines. [src: truly_dark_genes] Another 17,479 dark genes lack pangenome links and could not be assessed. [src: truly_dark_genes] The residue is concentrated in archaea, which are underrepresented in annotation databases. [src: truly_dark_genes] Two projects, truly_dark_genes and functional_dark_matter, supply the evidence through the discoveries digest. The page stops short of experimental function assignment.

## Literature Context

The one candidate paper bears on the hub's subject, which is how much of the hypothetical fraction of genomes can be given a function. It reports that the function of about 35% of genes in a genome is currently unknown, and it calls this fraction "genomic dark matter" [PMID 24728961](https://pubmed.ncbi.nlm.nih.gov/24728961/). The authors screened the genomes of more than 5,500 microorganisms for hypothetical proteins located near known cellulases. They synthesized and expressed 17 putative cellulase genes. These genes had too little sequence similarity to known cellulases for traditional similarity-based annotation to identify them. Eleven of the 17 (65%) showed significant activity towards at least one cellulose or lignocellulosic substrate [PMID 24728961](https://pubmed.ncbi.nlm.nih.gov/24728961/). This is a small set of enzymes, tested in vitro, and the paper is an abstract-level source here. It still shows that gene context can assign function to genes that sequence similarity cannot [PMID 24728961](https://pubmed.ncbi.nlm.nih.gov/24728961/).

The corpus findings are consistent with that paper's framing and extend it in a different direction. The paper's roughly 35% unknown fraction is a general genome-level estimate. The corpus gives a measured decomposition for Fitness Browser dark genes. Bakta v1.12.0 reclassifies 33,105 (83.7%) of 39,532 dark genes that have pangenome links. 6,427 stay hypothetical in both pipelines, and 17,479 unlinked genes could not be assessed. This suggests that much of the dark fraction reflects reannotation lag in databases rather than a lack of any signal. The two sources do not conflict, because they measure different things. The paper's approach is a context-based, experimental route to function for genes that resist similarity annotation. The corpus counts what newer similarity-based pipelines resolve and stops short of experimental function assignment.

The residue that resists is where the paper's method is most relevant. The corpus reports that 41% of neighbors of truly dark genes are also hypothetical. It also reports that only 246 of 6,427 (3.8%) truly dark genes have zero annotation clues. Genomic neighborhood is therefore an available signal for these genes. The corpus's proposal to use high cofitness (r > 0.97) to map operonic structure in Methanococcus follows the same logic as the paper's neighborhood strategy. The paper did not test that proposal, and it did not test archaeal genes. The paper's 65% success rate comes from cellulase candidates only. It should not be assumed to carry over to the truly dark set, which is shorter and less conserved. The corpus's archaeal database-coverage bias claim, and its horizontal-gene-transfer interpretation of the residue, have no support or challenge in this candidate and remain novel relative to it.

See also [[concepts/annotation-source-disagreement-and-coverage]].

## Decomposition of the dark set

The truly_dark_genes report splits the 57,011 FB dark genes into three categories [src: truly_dark_genes]:

| Category | Genes | Meaning |
|---|---|---|
| Annotation-lag | 33,105 | Annotated by Bakta v1.12.0, read as a database vintage problem [src: truly_dark_genes] |
| Truly dark | 6,427 | Called hypothetical by both FB and Bakta [src: truly_dark_genes] |
| Unlinked | 17,479 | No pangenome link, Bakta status unknown [src: truly_dark_genes] |

The report says this 57,011 → 6,427 reduction separates annotation lag from genuine novelty and gives a tractable target set for experimental biology. [src: truly_dark_genes] The 6,427 genes fall into 5,870 unique truly dark gene clusters. [src: truly_dark_genes]

## Reannotation resolves most dark genes

The truly_dark_genes report states that only 16.3% of dark matter resists modern annotation. [src: discoveries] Bakta v1.12.0 reclassifies 33,105 (83.7%) of 39,532 FB dark genes with pangenome links. [src: discoveries] This is the same cross-reference of Bakta v1.12.0 (DB v6.0) annotations for 132.5M pangenome cluster representatives against the 57,011 dark-gene catalog. [src: functional_dark_matter] The reclassified genes represent 58.1% of all dark genes. [src: functional_dark_matter] The 83.7% applies only to genes with pangenome links; the 58.1% is the share of the whole catalog.

Adding has_bakta_annotation as a 7th evidence flag changes darkness tiers for 18,019 genes. The largest shifts go from T4 Penumbra to T5 Dawn, as genes gain their final missing evidence line. [src: functional_dark_matter]

All 100 top prioritized candidates gain Bakta product descriptions. [src: functional_dark_matter] Examples include Homogentisate 1,2-dioxygenase HmgA (MR-1 rank 8) [src: functional_dark_matter], cell division proteins ZapE/ZapC (MR-1 ranks 13/16) [src: functional_dark_matter], N-acetylglucosamine kinase (MR-1 rank 26) [src: functional_dark_matter] and BolA family iron metabolism protein IbaG (Keio rank 31). [src: functional_dark_matter] The report reads this as independent validation of the experimental prioritization. In its view, dark genes with the strongest fitness effects tend to be annotated in UniProt but absent from the FB annotation vintage. [src: functional_dark_matter] That is an interpretation, not a measured test.

Bakta's AMRFinderPlus (AMR, antimicrobial resistance) also assigns AMR annotations to 5 dark genes. [src: functional_dark_matter] They include MerF mercury resistance transport in Marinobacter [src: functional_dark_matter], YbtP yersiniabactin transporter in K. oxytoca [src: functional_dark_matter], Asr acid resistance protein in K. oxytoca [src: functional_dark_matter], HdeD-GI heat resistance membrane protein in P. stutzeri [src: functional_dark_matter] and an S8 family peptidase in PV4. [src: functional_dark_matter] See [[entities/bakta]] and [[concepts/annotation-source-disagreement-and-coverage]].

## The residue that resists

6,427 genes remain truly dark, with both FB and Bakta calling them hypothetical proteins. [src: discoveries] They differ from the comparison genes in several ways:

- They are shorter (121 vs 194 aa). [src: discoveries]
- They are less conserved (43% vs 73% core). [src: discoveries]
- They have fewer orthologs (29% vs 64%). [src: discoveries]
- They show higher GC deviation (d=0.247). [src: discoveries]

The report calls these properties consistent with recent horizontal gene transfer (HGT) outpacing annotation databases. [src: discoveries] This is an interpretation. In support, 41% of neighbors of truly dark genes are also hypothetical. [src: discoveries] 12% are within 2 genes of mobile elements such as transposases, integrases and phage proteins. [src: discoveries] The report suggests these genes concentrate in recently acquired genomic islands rather than being randomly distributed. [src: discoveries] The 16.3% truly-dark rate (6,427/39,532) aligns with bacterial ORFan prevalence estimates (10-30%; Siew & Fischer 2003). The report takes this to confirm that a hard core of genuinely novel proteins persists despite database growth. [src: truly_dark_genes] See [[concepts/horizontal-gene-transfer-and-mobile-elements-as-a-source-of-novel-and-dark-genes]] and [[concepts/sequence-composition-and-conservation-of-unannotatable-genes]].

"Truly dark" does not mean "no clues". Only 246/6,427 (3.8%) have zero annotation clues. [src: discoveries] 84.7% have database cross-references. [src: discoveries] 43.5% have eggNOG hits, though 55% of COG (clusters of orthologous groups) assignments are "S"/unknown. [src: discoveries] 29.3% have cross-organism orthologs. [src: discoveries] 9.5% are in ICA (independent component analysis) fitness modules. [src: discoveries] Even among the 6,427 genes that remain hypothetical in both FB and Bakta, 79.4% gain UniRef50 links [src: functional_dark_matter], 69.1% gain UniParc/UniRef100 links [src: functional_dark_matter] and 62.4% gain RefSeq links. [src: functional_dark_matter] The report describes these as cross-reference paths for literature mining even without a product description. [src: functional_dark_matter]

Those with strong fitness phenotypes are depleted in stress conditions (OR=0.53, p<0.001), contrary to expectation (OR = odds ratio). [src: discoveries] They are enriched in nutrient, mixed community and iron conditions. [src: discoveries] The report suggests novel metabolic or inter-species interaction functions rather than stress responses. [src: discoveries]

## Archaeal and database-coverage bias

Truly dark genes are concentrated in specific organisms. Methanococcus strains S2 and JJ account for 55% of all truly dark genes, which the report attributes to archaea being underrepresented in annotation databases. [src: truly_dark_genes] It describes this as a well-known bias: archaeal proteins are systematically underrepresented in reference databases compared to bacteria. [src: truly_dark_genes] Across organisms, 4–96% of dark genes resist Bakta annotation, with archaeal organisms at the high end. [src: truly_dark_genes] The report argues that for archaea even the annotation-lag category underestimates true novelty, citing Makarova et al. (2019) on disproportionately large and functionally unexplored archaeal genomic dark matter. [src: truly_dark_genes] This is an argument from the literature, not a measured archaeal reannotation rate. The report suggests that a focused Methanococcus analysis could use high cofitness signals (r > 0.97) to map operonic structure and generate functional predictions for archaeal-specific hypothetical proteins. [src: truly_dark_genes]

## Evidence depth and conservation of the dark set

The functional_dark_matter classification gives a similar picture. Only 4,273 of 57,011 dark genes (7.5%) are T1 Void, with zero evidence. [src: discoveries] These T1 Void genes lack all evidence, so structure-based function prediction is the only remaining computational inference strategy for them. [src: functional_dark_matter] T4 Penumbra holds 22,500 genes (39.5%) with 3-4 converging lines of evidence. [src: discoveries] The report concludes that the bottleneck for most dark genes is targeted experimental validation, not computational inference. [src: discoveries] For the top 100 candidates, and especially the 1,853 T5 Dawn genes (nearly characterized), the report proposes AlphaFold2 structure predictions to confirm functional hypotheses and distinguish DUF families. [src: functional_dark_matter] See [[concepts/census-and-evidence-depth-classification-of-functionally-dark-genes]].

Many dark ortholog groups (OGs) are widespread. 55.9% of dark gene OGs are kingdom-level, present across multiple phyla. [src: discoveries] Across 27,690 species, species counts per OG range from 1 to 27,482 (median 135). [src: discoveries] COG0468, COG0443 and COG0491 are present in virtually all sequenced bacterial genomes yet have zero functional evidence. [src: discoveries] See [[concepts/phylogenetic-breadth-and-pangenome-conservation-of-dark-genes]].

## Database coverage and taxonomic bias in organism choice

Taxon choice shapes which dark genes get attention. Adding 25 non-FB organisms from Bacillota, Actinomycetota and Campylobacterota yields 50 selected organisms spanning 6 phyla, versus 4 for FB-only selection. [src: discoveries] P. aeruginosa PAO1 ranks #1 with 3,713 OGs. [src: discoveries] M. tuberculosis ranks #6 as the first Actinomycetota. [src: discoveries] B. subtilis and S. aureus are not selected, because their kingdom-level OGs are already covered by selected Pseudomonadota. [src: discoveries] They stay valuable for studying dark genes in a native Gram-positive context. [src: discoveries] Shewanella MR-1 contributes 25/100 top fitness-active candidates [src: discoveries], with 587 scored dark genes. [src: discoveries] It covers 20.8% of the top-500 in just 3 experiments. [src: discoveries] The report attributes this to 121 conditions, a large dark gene complement and 142 genes with |fit| >= 4. [src: discoveries] See [[concepts/reference-database-coverage-and-phylogenetic-bias-in-annotation-gap-estimates]] and [[concepts/organism-selection-and-taxonomic-coverage-bias-for-experimental-characterization-of-dark-genes]].

## Caveats on the counts

- The dark-gene count (57,011) likely overestimates functionally uncharacterized genes, because databases not checked (UniProt, InterPro, recent NCBI updates) may annotate some hypothetical genes. [src: functional_dark_matter]
- Some Bakta "hypothetical protein" calls may be false negatives: genes with known functions that failed to match the PSC database version tested (v6.0). [src: truly_dark_genes]
- The 17,479 unlinked dark genes (31%) could not be assessed. An estimated ~2,841 of them may be truly dark, a 31% coverage gap in the prioritized list. [src: truly_dark_genes]
- The report itself proposes extending pangenome linkage to the 17,479 unlinked dark genes, then running Bakta to identify additional truly dark candidates and expand the priority list. [src: truly_dark_genes]

## Tensions

- The report treats Bakta annotations as validating the experimental prioritization. [src: functional_dark_matter] Yet two caveats point the same way: Bakta hypothetical calls may be false negatives for genes with known functions [src: truly_dark_genes], and unchecked databases may annotate some genes counted as dark, so the dark-gene count likely overestimates uncharacterized genes. [src: functional_dark_matter]

## Open Directions

- Extend pangenome linkage to the unlinked dark genes, then run Bakta on them, to close the coverage gap in the truly dark list.
- Break the reclassification rate down by phylum, including archaeal genomes such as [[entities/methanococcus-maripaludis]], to test database-coverage bias.
- Check whether Bakta product names for the 33,105 reclassified genes are specific or generic, for example by the share of "S"/unknown COGs.
- Test whether the 6,427 truly dark genes sit in genomic islands by comparing island and mobile-element proximity against a background gene set.
- Re-annotate the truly dark set with newer database versions to measure how fast the residue shrinks.
