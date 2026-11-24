---
type: "Concept"
description: "Whether costly or fitness-neutral non-conserved genes and pathways show signatures of adaptive Black Queen gene loss, at gene, pathway-conservation and pangenome-openness levels; stops at the genes' identity as selfish elements."
sources: ["summaries/conservation_fitness_synthesis__REPORT.md", "summaries/core_gene_tradeoffs__REPORT.md", "summaries/costly_dispensable_genes__REPORT.md", "summaries/metabolic_capability_dependency__REPORT.md", "summaries/pathway_capability_dependency__REPORT.md"]
---
# Gene loss and Black Queen hypothesis tests

This page covers whether costly or fitness-neutral non-conserved genes and pathways show signatures of adaptive Black Queen gene loss. The evidence is mixed. Candidate genes exist [src: conservation_fitness_synthesis, core_gene_tradeoffs], and clade-level pangenome patterns fit the hypothesis. [src: metabolic_capability_dependency] Pathway-level conservation does not separate the predicted classes. [src: metabolic_capability_dependency] Most support is correlational and rests on suggestion, not direct observation of loss. The page stops at the question of what the candidate genes are.

## Literature Context

The one candidate paper bears on the adaptive-loss premise behind this page. It analysed 949 metabolic networks and concluded that auxotrophies are likely highly prevalent in both symbiotic and free-living bacteria [PMID 24910088](https://pubmed.ncbi.nlm.nih.gov/24910088/). It then tested whether selection can explain the loss of biosynthetic genes. It deleted conditionally essential biosynthetic genes from Escherichia coli and Acinetobacter baylyi, and it competed each of 20 auxotrophic mutants against the prototrophic wild type with the focal nutrient present. Virtually all mutants showed a concentration-dependent growth advantage of around 13% [PMID 24910088](https://pubmed.ncbi.nlm.nih.gov/24910088/). Different genes in the same pathway had gene-specific fitness consequences, and the same gene lost from the two species affected fitness differently. The authors suggest that adaptive benefits could drive the loss of conditionally essential biosynthetic genes [PMID 24910088](https://pubmed.ncbi.nlm.nih.gov/24910088/). These are laboratory competition experiments in two species, and only the abstract was available to me. They show that loss can be advantageous. They do not show that loss has occurred in natural communities, and they do not test whether neighbours supply the lost function.

The corpus's pangenome-level findings are consistent with this picture, but only loosely. The fraction of latent capabilities correlated positively with [[entities/pangenome-openness|pangenome openness]] (Spearman ρ = 0.69, p = 0.0004, n = 22 clades). The pan-bacterial result was a partial Spearman rho=0.530 across 2,810 species with 10+ genomes. Both are correlational. The pangenome result and the report's reading that amino acid biosynthesis depends on accessory genes fit a world where biosynthetic genes are often dispensable and lost. The candidate paper adds a mechanism that could explain such loss. That mechanism is a measured fitness gain when the nutrient is available. It is not a Black Queen mechanism in which community members provide a public good. The paper's selective advantage is also seen in monoculture-versus-wild-type competition, so it is an alternative or complementary explanation, not a confirmation of Black Queen dynamics.

The corpus's null pathway-conservation result (Mann-Whitney U p = 0.94, rank-biserial r = 0.052) is not contradicted by the paper. The paper found gene-specific fitness effects within a pathway, and the corpus measure is pathway-level. This agrees with the report's own caveat that it cannot see partial erosion. The corpus's gene-level finding concerns 5,526 costly and dispensable genes, which the report describes as predominantly selfish elements and not metabolic genes. That finding has no counterpart in the candidate paper, which studied biosynthetic genes. On that point the corpus is novel relative to this evidence. Per-gene tests of auxotroph loss across phylogenies, which the corpus proposes, would extend the paper's experimental results to natural populations.

## Gene level: costly and dispensable candidates

Several reports flag the same set of candidate genes. They count 5,526 costly and dispensable genes and call them candidates for ongoing gene loss. [src: conservation_fitness_synthesis, core_gene_tradeoffs] Whether these genes are mobile elements or recently acquired genes on their way out remains an open question. [src: conservation_fitness_synthesis]

The costly_dispensable_genes report proposes that these genes were acquired by horizontal gene transfer (HGT) and will likely be purged unless they give an environment-specific advantage. [src: costly_dispensable_genes] Condition-specific phenotypes occur in 14.1% of costly+dispensable genes, against 16.7% of costly+conserved genes. [src: costly_dispensable_genes] Neutral+dispensable genes show 2.7%. The report suggests that costly+dispensable genes keep some fitness effects, which may slow their loss. [src: costly_dispensable_genes] It also suggests that a subset may persist if the conditions that elicit their phenotypes are met often enough. [src: costly_dispensable_genes] It further suggests that these genes in free-living organisms may be early stages of genome degradation. [src: costly_dispensable_genes] Related literature cited includes strain-dependent essentiality in S. pneumoniae [src: costly_dispensable_genes] and extreme pseudogenization in symbiotic cyanobacteria under relaxed selection. [src: costly_dispensable_genes]

The report describes the [[entities/black-queen-hypothesis|Black Queen Hypothesis]] (Morris et al. 2012) as loss of costly genes when community members provide their functions as public goods. [src: costly_dispensable_genes] It proposes the costly+dispensable genes as candidates for this process. It notes that they are predominantly selfish elements rather than metabolic genes, and that they may represent a stage before actual loss. [src: costly_dispensable_genes] That caveat limits any Black Queen reading at the gene level. See mobile element origin of costly non conserved genes for the gene identities.

The strongest outlier is [[entities/pseudomonas-stutzeri-rch2]], with 21.5% costly+dispensable genes. The report suggests a recent mobile-element invasion or strain-specific genomic expansion. [src: costly_dispensable_genes] It cautions that this may reflect strain-specific features rather than a general pattern. [src: costly_dispensable_genes]

## Pathway conservation: no support for H2a

The pathway-level test did not support the Black Queen prediction. Conservation was the fraction of species genomes carrying a complete pathway. [src: metabolic_capability_dependency] Latent capabilities (n = 248) had mean conservation 0.869 and median 1.000. [src: metabolic_capability_dependency] Active dependencies (n = 755) had mean 0.829 and median 1.000. [src: metabolic_capability_dependency] Intermediate pathways (n = 508) had mean 0.907 and median 1.000. [src: metabolic_capability_dependency] Latent pathways had slightly higher mean conservation than active ones. The test for active > latent gave Mann-Whitney U p = 0.94 and rank-biserial r = 0.052, so H2a is not supported. [src: metabolic_capability_dependency]

The report offers several limits on this null result.
- The measure is pathway-level, so it cannot detect partial erosion or progressive gene loss within a complete pathway. [src: metabolic_capability_dependency]
- Fitness experiments cover only 48 organisms. Untested relatives in a clade may inflate apparent conservation. [src: metabolic_capability_dependency]
- Evolutionary lag may hide ongoing loss, leaving mid-loss capabilities that still look conserved at species level. [src: metabolic_capability_dependency]
- The species-level analysis across many taxa may miss a signal that is strongest within single lineages or communities. [src: metabolic_capability_dependency]

The report cites Schakel et al. (2025). That work showed that cross-feeding-based gene loss needs spatial structure and is not simply predicted by retention cost. The report treats this as consistent with the null result. [src: metabolic_capability_dependency]

## Pangenome openness: clade-level support

At the clade level the signal appears. The 41 Fitness Browser organisms were aggregated to 22 species clades, because strains in a clade share one pangenome openness value. [src: metabolic_capability_dependency] The fraction of latent capabilities correlated positively with [[entities/pangenome-openness|pangenome openness]] (Spearman ρ = 0.69, p = 0.0004, n = 22 clades). [src: metabolic_capability_dependency] The report reads this as consistent with the Black Queen framework at species level, and as clade-level support, with ongoing streamlining. [src: metabolic_capability_dependency] It aligns this result with Morris et al. (2012), who proposed selection-driven gene loss in Prochlorococcus and Pelagibacter. [src: metabolic_capability_dependency]

The pathway_capability_dependency report adds a pan-bacterial result. Across 2,810 species with 10+ genomes, species with more variable pathways had more open pangenomes (partial Spearman rho=0.530, p=2.83e-203, controlling for genome count). The report calls this consistent with ongoing pathway gene loss. [src: pathway_capability_dependency] It finds that amino acid biosynthesis completeness depends on accessory pangenome genes for a substantial fraction of bacteria. [src: pathway_capability_dependency] It calls this direct evidence for Black Queen dynamics, with synthesis capacity spread across strains. [src: pathway_capability_dependency] It also reads strain differences in biosynthetic capability as a precondition for public-goods dynamics. [src: pathway_capability_dependency] See [[concepts/black-queen-dynamics-in-amino-acid-biosynthesis]]. The report reframes the hypothesis as a continuum of dependency that varies with environment. [src: pathway_capability_dependency]

## Tensions

- The pangenome-openness correlation supports the Black Queen framework (ρ = 0.69, n = 22 clades), but pathway conservation does not distinguish latent from active pathways (p = 0.94). [src: metabolic_capability_dependency] The report suggests the signal lies in genome dynamics and community context, not in per-pathway conservation ratios. [src: metabolic_capability_dependency] This reading is a suggestion, not a tested result.
- The report cites Morris et al. (2012) and D'Souza et al. (2014) as showing gene loss in natural and experimental populations. It contrasts this with its own species-level result. [src: metabolic_capability_dependency]
- The costly+dispensable genes are called Black Queen candidates, yet they are mostly selfish elements and not metabolic genes. [src: costly_dispensable_genes]

## Tests the reports propose

- Per-gene dN/dS or gene presence/absence across a phylogeny could replace pathway-level conservation to test progressive gene loss directly. [src: metabolic_capability_dependency]
- Lineages with recent loss events (singletons or auxiliary genes) in latent pathways could be identified, and the deletions verified in the phylogeny. [src: metabolic_capability_dependency]
- Organisms with higher latent fractions could be tested for more public-goods pathways or co-occurrence with cross-feeding partners. [src: metabolic_capability_dependency]
- Costly+dispensable genes could be tracked across multiple sequenced strains and close relatives to see whether they are being lost. [src: costly_dispensable_genes]
- ENIGMA CORAL community data could test whether organisms with more costly+dispensable genes co-occur with organisms that could provide the lost functions. [src: costly_dispensable_genes]
- Phage invasion, IS element expansion or genomic island acquisition could be tested as explanations for the P. stutzeri RCH2 outlier. [src: costly_dispensable_genes]

## Open Directions

- Run a per-gene presence/absence analysis across a phylogeny for latent pathways. It would close the gap left by the pathway-level measure, which cannot see partial erosion.
- Compare costly+dispensable gene presence across strains of one species with close relatives. It would show whether these genes are being lost or only acquired.
- Join ENIGMA CORAL community composition to per-organism counts of costly+dispensable genes. It would test the public-goods premise directly.
- Repeat the latent-fraction versus openness test within single lineages. It would check whether the species-level null hides a within-lineage signal.
- Annotate the 5,526 genes for mobile-element features. It would settle whether they are selfish elements or metabolic genes.
