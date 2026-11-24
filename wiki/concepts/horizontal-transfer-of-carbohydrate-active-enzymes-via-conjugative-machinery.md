---
type: "Concept"
description: "Evidence that type IV secretion system (T4SS) and conjugative machinery co-localise with carbohydrate-active enzyme (CAZy) genes, especially GT2 glycosyltransferases, and that this reflects cross-phylum horizontal gene transfer; stops at mechanism, which is untested experimentally."
sources: ["summaries/t4ss_cazy_environmental_hgt__REPORT.md"]
---
# Horizontal transfer of carbohydrate-active enzymes via conjugative machinery

This page covers the evidence that type IV secretion system (T4SS) and conjugative machinery co-localise with carbohydrate-active enzyme (CAZy) genes, especially GT2 glycosyltransferases, and that this reflects cross-phylum horizontal gene transfer (HGT). The evidence comes from one preliminary environmental analysis. It is observational, and the mechanism is untested experimentally. [src: t4ss_cazy_environmental_hgt]

## Literature Context

The candidate papers give only indirect context for the hub's claim that T4SS and conjugative machinery sit next to CAZy genes and that this reflects cross-phylum transfer. None of them tests T4SS-mediated CAZy transfer. They do show that mobile genetic elements (MGEs), conjugative elements and carbohydrate-active enzymes can be linked in other settings.

The closest match is a metagenomic survey of ruminant gut microbiomes. It identified 4,764,110 MGEs across 2,458 metagenomic samples from eight ruminant species. These included integrative and conjugative elements, integrons, insertion sequences, phages and plasmids, and the authors report that mobilisation patterns were largely confined to closely related microbial lineages [PMID 40652256](https://pubmed.ncbi.nlm.nih.gov/40652256/). In a validation cohort, GH1-carrying plasmids enriched in CAZymes predominated in the stomach and responded to forage-based diets [PMID 40652256](https://pubmed.ncbi.nlm.nih.gov/40652256/). This shows that MGEs can carry CAZyme cargo. It is a different setting from the hub's environmental MAGs, and it points to plasmids, whereas the hub's ICEfinder analysis found no plasmid-borne CAZy genes. The restriction to related lineages also sits uneasily with the hub's cross-phylum events, such as the 8-phylum Node_4915. The two studies differ in habitat and method, so this is a contrast and not a direct conflict.

A human gut study of 37 patients with Wilson's disease and 33 healthy controls links the same classes of features. CAZyme dysregulation, differentially abundant type IV secretion system genes (aec19, pilB) and 60 enriched functional MGEs, including conjugative transfer categories, were all reported, and the authors suggest heightened horizontal gene transfer potential [PMID 41623619](https://pubmed.ncbi.nlm.nih.gov/41623619/). These are co-occurrences in a disease cohort. They do not show that T4SS moves CAZymes. This is consistent with the hub's association of T4SS and MGEs with CAZy content, and it adds no mechanistic evidence.

Other papers show only that conjugative elements are present. A Brevibacterium comparative genomic study reports horizontal transfers of siderophore-related genes and a bacteriocin cluster in a probable conjugative transposon found only in cheese-associated strains. This is a genomic inference, and transfer was not demonstrated [PMID 29216827](https://pubmed.ncbi.nlm.nih.gov/29216827/). A study of bla NDM-1 in Enterobacter cloacae used conjugation experiments to show plasmid transfer of resistance into E. coli transconjugants [PMID 28830556](https://pubmed.ncbi.nlm.nih.gov/28830556/). That is the kind of experiment the hub lists as an open direction for a GT2 cassette. The Vibrio cholerae work shows that an ICE-encoded DNase, IdeA, inhibits natural transformation [PMID 26240317](https://pubmed.ncbi.nlm.nih.gov/26240317/). This shows ICEs can shape gene flow, but not that they transfer CAZy genes.

Overall, the hub's findings are consistent with the literature that MGEs, conjugative machinery and CAZymes co-occur. The cross-phylum GT2 signal and the T4SS-GT2 syntenic co-localisation are novel relative to these candidates. The integrative mechanism remains an untested hypothesis. See [[concepts/environmental-biome-enrichment-of-mobile-cazy-gene-content]].

## Prevalence of T4SS machinery and co-occurrence with CAZy genes

T4SS/conjugative machinery is common in environmental metagenome assembled genomes (MAGs), and GT2 is the CAZy family most often found near it. The report finds it in 21.8% of 30,497 high-quality environmental MAGs (6,652 MAGs), using a multi-marker definition. [src: t4ss_cazy_environmental_hgt] Ninety-two CAZy families show elevated co-occurrence with T4SS loci at ≤10 kb, but threshold validation is pending. [src: t4ss_cazy_environmental_hgt] GT2 glycosyltransferases ([[entities/glycosyl-transferases]]) are the top hit, at 767 genomes with an average of 5,041 bp. [src: t4ss_cazy_environmental_hgt] The report states that T4SS machinery is significantly co-localised with GT2 glycosyltransferase cassettes. [src: t4ss_cazy_environmental_hgt] See also [[entities/type-iv-secretion-system]].

In GT2 neighbourhoods, list-format parsing finds T4SS in 503 entries and GT2 in 495. The report reads this as confirming syntenic co-localisation at the contig level. [src: t4ss_cazy_environmental_hgt] GH23 (murein lytic transglycosylase) is the second most common CAZy family in these neighbourhoods, with 106 occurrences. [src: t4ss_cazy_environmental_hgt] The report suggests from this that cell wall remodelling genes cluster with GT2–T4SS syntenic loci. [src: t4ss_cazy_environmental_hgt]

## Cross-phylum transfer events in the GT2 gene tree

Phylogenetic incongruence in the GT2 gene tree gives positive evidence for cross-phylum transfer. The tree contains 77 detected HGT events, and 32 are high-confidence cross-phylum events (normalised). [src: t4ss_cazy_environmental_hgt] In the events file, 65 events span 2 phyla and 12 span ≥3 phyla (15.6%). [src: t4ss_cazy_environmental_hgt]

The strongest event is Node_4915, with max divergence 4.843. [src: t4ss_cazy_environmental_hgt] It contains 35 genes, 82.9% of them syntenic. [src: t4ss_cazy_environmental_hgt] It spans 8 phyla: WOR-3, Desulfobacterota, Patescibacteria, Bacteroidota, Firmicutes_A, Methanobacteriota, Bdellovibrionota and Acidobacteriota. [src: t4ss_cazy_environmental_hgt] BLAST validation of Node_4915 against NCBI nr is still pending. [src: t4ss_cazy_environmental_hgt]

The phyla most involved across events are Firmicutes_A (27), Pseudomonadota (22), Bacillota_A (19) and Actinomycetota (10). [src: t4ss_cazy_environmental_hgt]

Divergence and syntenic percentage are negatively correlated (Spearman ρ = −0.615, p<0.001). [src: t4ss_cazy_environmental_hgt] The report reads this as sequence divergence after transfer, which it calls the expected biological pattern. [src: t4ss_cazy_environmental_hgt]

## Mechanism: consistent with integrative transfer, not established

The data do not establish the transfer route. T4SS+ genomes have 10× higher mobile genetic element (MGE) density (p<0.001). [src: t4ss_cazy_environmental_hgt] ICEfinder found no plasmid-borne CAZy genes. [src: t4ss_cazy_environmental_hgt] The report reads this null result together with the MGE elevation as consistent with chromosomal or integrative transfer (IMEs/ICEs) rather than plasmid mobilisation. [src: t4ss_cazy_environmental_hgt] That is an interpretation. It does not prove integrative transfer or rule out plasmid mobilisation. The report concludes that the results support the hypothesis that T4SS machinery mediates environmental dissemination of CAZy diversity across phylogenetically distant bacteria. [src: t4ss_cazy_environmental_hgt] All associations are observational, and the analysis is preliminary: threshold validation (NB05) and manuscript figures (NB06) are pending. [src: t4ss_cazy_environmental_hgt] For the broader context, see [[concepts/environmental-biome-enrichment-of-mobile-cazy-gene-content]] and [[summaries/t4ss_cazy_environmental_hgt__REPORT]].

## Open Directions

- Run the pending BLAST of Node_4915 against NCBI nr to check the 8-phylum event independently of the gene tree.
- Complete the threshold validation, testing whether the 92 families at ≤10 kb hold at other distance cut-offs.
- Test whether T4SS-adjacent GT2 genes sit within IME/ICE boundaries. This would test the integrative interpretation against other mechanisms, including plasmid mobilisation.
- Check whether GH23 and other cell wall remodelling genes co-locate with GT2–T4SS loci more often than in matched control neighbourhoods.
- Test transfer experimentally, for example by conjugation assays with a candidate GT2 cassette, since all current evidence is observational.
