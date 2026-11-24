---
type: "Concept"
description: "Whether MAG incompleteness, isolate versus MAG composition, uneven biome sampling and limited power bias genome-resolved ecological comparisons."
sources: ["summaries/cazyme_pangenome_ecology__REPORT.md", "summaries/gene_copy_number_variation__REPORT.md", "summaries/neon_mag_functional_discovery__REPORT.md", "summaries/oak_ridge_cultivation_gap__REPORT.md"]
---
# Genome-type and sampling bias in metagenome-assembled genome surveys

This page covers whether MAG incompleteness, isolate versus MAG composition, uneven biome sampling and limited power bias genome-resolved ecological comparisons. One report found no significant difference in total CAZyme counts between isolate and MAG genomes within biomes. [src: cazyme_pangenome_ecology] Three others state caveats that bound their conclusions. [src: gene_copy_number_variation, neon_mag_functional_discovery, oak_ridge_cultivation_gap] See [[summaries/cazyme_pangenome_ecology__REPORT]], [[summaries/gene_copy_number_variation__REPORT]], [[summaries/neon_mag_functional_discovery__REPORT]] and [[summaries/oak_ridge_cultivation_gap__REPORT]].

## Literature Context

The one candidate paper is about a different kind of sampling bias from the ones in this hub. It does not study MAG completeness, isolate versus MAG composition, or biome coverage. It compares deep-seawater microbial communities collected with measures to limit pressure and temperature change against communities collected conventionally with Niskin bottles. Conventional collection lowered the total number of prokaryotic cells retrieved. It cut protein synthesis activity by more than 10%. It also shifted community composition [PMID 42391470](https://pubmed.ncbi.nlm.nih.gov/42391470/). The largest compositional change was a drop of more than 20% in metagenomic archaeal representation, in the TACK group (Thaumarchaeota, Nitrososphaerota) [PMID 42391470](https://pubmed.ncbi.nlm.nih.gov/42391470/). Bacterial groups responded in mixed ways. Pelagibacteraceae, Thioglobaceae and Chitinophagaceae were better represented when pressure was kept. Burkholderiaceae, Comamonadaceae and Oxalobacteraceae were better represented after decompression [PMID 42391470](https://pubmed.ncbi.nlm.nih.gov/42391470/). Incubations longer than 24 h also changed the original community composition [PMID 42391470](https://pubmed.ncbi.nlm.nih.gov/42391470/). This is an abstract-level result about deep-sea water, and it says nothing about soil, subsurface or host-associated genomes.

The corpus findings are consistent with this paper in one general respect. How a sample is obtained can change which taxa and functions appear in genome-resolved comparisons, and conclusions need to be bounded accordingly. The hub's biases arise at a different stage, after collection. They concern assembly and binning quality, the isolate or MAG origin of genomes, and uneven coverage of biomes or habitats. The paper does not test any of these, so it neither supports nor contradicts them.

The corpus claims are therefore novel relative to this candidate. The CAZyme report found no significant difference in total CAZyme counts between isolate and MAG genomes within biomes (all Cohen's d < 0.21) [src-free summary of hub]. The oak_ridge_cultivation_gap report warned that a mean completeness of 78.7% may hide KOs, so the 813 MAG-enriched KOs are probably conservative. The NEON H4b cohort of 73 MAGs is water-skewed. The deep-sea paper adds one point to these. A taxon-specific loss, such as the archaeal decline it reports, is a reason to check whether any sample-handling step also differs between genome types or habitats. In the corpus, that applies to the cultured collection, which comes mainly from ORFRC, and to the MAGs, which come from subsurface sites worldwide. The candidate does not show that such a handling difference exists there. That remains a hypothesis for future work. See [[concepts/metadata-and-annotation-coverage-gaps-biasing-environmental-genome-cohorts]].

## MAG incompleteness and genome type

In the bacterial CAZyme (carbohydrate-active enzyme) dataset, MAGs made up 96% of genomes. [src: cazyme_pangenome_ecology] Within-biome Mann-Whitney tests found no significant difference in total CAZyme counts between isolate and MAG genomes (all Cohen's d < 0.21). The report treats this as showing that MAG incompleteness does not drive its biome patterns. [src: cazyme_pangenome_ecology] It still warns that incomplete MAGs may undercount CAZymes in absolute terms. [src: cazyme_pangenome_ecology]

The oak_ridge_cultivation_gap report gives a limit in the other direction. Its QC-filtered MAG cohort has mean completeness 78.7%, so some KOs (KEGG orthologs) scored as absent may lie in the missing 20% of the genome. [src: oak_ridge_cultivation_gap] This would make the 813 MAG-enriched KOs a conservative estimate, with a true count likely higher. Some cultured-enriched KOs may be false positives. [src: oak_ridge_cultivation_gap] See also [[concepts/genome-size-and-taxonomic-composition-confounding-of-cultured-versus-mag-functional-comparisons]].

Fragmentation also affects copy-number work. Fragmented MAGs can split a paralog family across contigs and inflate multi-copy counts, or merge them and deflate counts. Because the metrics are per-cluster-per-genome counts, contig artifacts enter linearly. [src: gene_copy_number_variation] The report does not condition on checkm_completeness or contig N50, and it says a robustness pass on the tightest-quality genomes would strengthen the claim. [src: gene_copy_number_variation] It proposes restricting to checkm_completeness ≥ 95 and checkm_contamination ≤ 2 and rerunning NB03 to check whether the L effect is inflated by fragmented assemblies. [src: gene_copy_number_variation] See [[concepts/mechanisms-and-confounders-of-copy-number-variation-in-pangenomes]].

## Uneven sampling and power

Soil (34%) and marine (23%) genomes dominate the CAZyme dataset. [src: cazyme_pangenome_ecology] The rare biomes barley-rhizosphere (n=74) and zebrafish-fecal (n=67) have limited statistical power. [src: cazyme_pangenome_ecology] The same report controlled phylogeny by within-phylum stratification rather than PGLS (phylogenetic generalized least squares), which would need a resolved tree for 9,347 species. [src: cazyme_pangenome_ecology]

The NEON cohort shows a stronger form of the problem. The H4b cohort is 73 MAGs, a non-random 30% subset of a 246-MAG target. Its coverage is biased by NMDC per-gene-table coverage (water genera 100%, soil 0–30%), and 173 MAGs are missing. [src: neon_mag_functional_discovery] It over-represents water habitats, with cyanobacteria at 100% per-gene KO coverage. [src: neon_mag_functional_discovery] The report says the H4b result generalizes within a water-skewed sub-cohort. It attributes the photosystem-heavy enrichment list to that bias, not to a unique feature of field-only KOs across all NEON MAGs. [src: neon_mag_functional_discovery] The sample size also did not allow a clean cross-domain comparison, so archaea remain a soil-only side panel. [src: neon_mag_functional_discovery] See [[concepts/field-only-accessory-gene-content-absent-from-cultured-pangenomes]] and [[concepts/metadata-and-annotation-coverage-gaps-biasing-environmental-genome-cohorts]].

## Geography as a confounder of genome type

In the oak_ridge_cultivation_gap report, the cultured collection spans 20+ years of ENIGMA isolation, mainly at ORFRC (Oak Ridge Field Research Center). The MAGs come from subsurface sites worldwide. Composition differences may therefore reflect geography as much as cultivation bias. [src: oak_ridge_cultivation_gap]

## Tensions

- The CAZyme report finds no significant isolate-versus-MAG difference within biomes. [src: cazyme_pangenome_ecology] The oak_ridge_cultivation_gap report says MAG incompleteness may hide KOs. [src: oak_ridge_cultivation_gap] The two measure different things: total CAZyme counts versus presence or absence of individual KOs. The CAZyme report also concedes that absolute undercounting remains possible. [src: cazyme_pangenome_ecology]

## Open Directions

- Run the quality-restricted copy-number rerun described above, to close the gap that completeness and N50 are not conditioned on.
- Repeat the isolate-versus-MAG comparison on individual CAZyme families, not just totals, to test whether absolute undercounting exists.
- Fill the missing per-gene coverage for soil MAGs, or reweight by habitat, to test whether the NEON H4b enrichment list survives outside the water-skewed cohort.
- Compare ORFRC isolates with MAGs from the same site, to separate geography from cultivation bias.
- Sample the rare biomes more deeply, or use resampling, to find which biome contrasts have adequate power.
