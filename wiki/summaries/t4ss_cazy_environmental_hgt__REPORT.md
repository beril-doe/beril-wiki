---
type: "Summary"
description: "Summary of the project T4SS-CAZy Environmental HGT."
doc_type: "short"
full_text: "sources/t4ss_cazy_environmental_hgt__REPORT.md"
---
# T4SS-CAZy Environmental HGT

This page summarises the T4SS-CAZy Environmental HGT project. The report finds that type IV secretion system (T4SS) machinery in environmental metagenome assembled genomes (MAGs) is significantly co-localised with GT2 glycosyltransferase cassettes. It also finds GT2 gene-tree incongruence that gives positive evidence for 32 cross-phylum horizontal gene transfer (HGT) events. The evidence is observational and preliminary: core analyses are complete, and threshold validation and manuscript figures are pending. [src: t4ss_cazy_environmental_hgt]

## Key Findings

### T4SS prevalence and CAZy co-occurrence

T4SS/conjugative machinery is common in environmental MAGs, and many CAZy families co-occur with it. [src: t4ss_cazy_environmental_hgt] The report defines T4SS/conjugative machinery by multiple markers: VirB4/6/8/9/10/11, VirD4, TraI/D, TrwB and TraG. [src: t4ss_cazy_environmental_hgt] It finds this machinery in 21.8% of 30,497 high-quality environmental MAGs (6,652 MAGs). [src: t4ss_cazy_environmental_hgt] Separately, in environmental MAGs, 92 CAZy families show elevated co-occurrence with T4SS loci at ≤10 kb, and the threshold is not yet validated. [src: t4ss_cazy_environmental_hgt] GT2 glycosyltransferases are the top hit, with 767 genomes and avg 5,041 bp. [src: t4ss_cazy_environmental_hgt] See [[entities/glycosyl-transferases]] and [[entities/type-iv-secretion-system]].

### Biome enrichment

Enrichment is reported for several biomes: marine sediment (OR=5.5, q<10⁻⁹⁸), barley rhizosphere (OR=10.4) and maize rhizosphere (OR=4.1), where OR is the odds ratio. [src: t4ss_cazy_environmental_hgt] Enrichment patterns replicate across a 70/30 discovery/validation split, which the report reads as confirming robustness. [src: t4ss_cazy_environmental_hgt] See [[concepts/environmental-biome-enrichment-of-mobile-cazy-gene-content]].

### GT2 horizontal transfer events

The GT2 gene tree contains 77 detected HGT events, of which 32 are high-confidence cross-phylum events (normalised). [src: t4ss_cazy_environmental_hgt] The events are characterised in Detected_HGT_Events.csv (n=77). [src: t4ss_cazy_environmental_hgt] Of these, 65 events span 2 phyla and 12 span ≥3 phyla (15.6%). [src: t4ss_cazy_environmental_hgt]

The strongest event is Node_4915, with max divergence 4.843. [src: t4ss_cazy_environmental_hgt] It contains 35 genes, 82.9% syntenic. [src: t4ss_cazy_environmental_hgt] It spans 8 phyla: WOR-3, Desulfobacterota, Patescibacteria, Bacteroidota, Firmicutes_A, Methanobacteriota, Bdellovibrionota and Acidobacteriota. [src: t4ss_cazy_environmental_hgt]

Divergence and syntenic percentage are negatively correlated (Spearman ρ = −0.615, p<0.001). [src: t4ss_cazy_environmental_hgt] The report reads this as sequence divergence after transfer and calls it the expected biological pattern. [src: t4ss_cazy_environmental_hgt]

The most-involved phyla across events are Firmicutes_A (27), Pseudomonadota (22), Bacillota_A (19) and Actinomycetota (10). [src: t4ss_cazy_environmental_hgt]

### GT2 neighbourhoods

The GT2 neighbourhood analysis covers 376 genomes. [src: t4ss_cazy_environmental_hgt] Parsing the neighbourhoods as lists finds T4SS in 503 entries and GT2 in 495. The report takes this as confirming contig-level syntenic co-localisation. [src: t4ss_cazy_environmental_hgt] GH23 (murein lytic transglycosylase) is the second most common CAZy family in these neighbourhoods, with 106 occurrences. The report suggests that cell wall remodelling genes cluster with GT2–T4SS syntenic loci. [src: t4ss_cazy_environmental_hgt] See [[entities/glycoside-hydrolases]].

### Transfer mechanism

ICEfinder found no plasmid-borne CAZy genes, and detected 12 IMEs in the top 100 accumulators. [src: t4ss_cazy_environmental_hgt] T4SS+ genomes have 10× higher MGE (mobile genetic element) density (p<0.001). [src: t4ss_cazy_environmental_hgt] The report reads the two results together as consistent with chromosomal or integrative transfer (IMEs/ICEs) rather than plasmid mobilisation. [src: t4ss_cazy_environmental_hgt]

### Metal resistance

GT2-neighbourhood MAGs (n=376) have a mean of 0.045 metal resistance types, against 0.004 for non-GT2 MAGs (n=260,276); Mann-Whitney p=8.6e-27. [src: t4ss_cazy_environmental_hgt] The report states that genomes with GT2 in T4SS-proximal neighbourhoods carry 11× more metal resistance genes. [src: t4ss_cazy_environmental_hgt] It interprets this as an independent link between CAZy–T4SS synteny and the metal resistance niche breadth hypothesis. [src: t4ss_cazy_environmental_hgt] See [[concepts/metal-resistance-co-occurrence-with-mobile-gene-transfer-hubs]].

### Overall interpretation

The report concludes that its results support the hypothesis that T4SS machinery mediates environmental dissemination of carbohydrate-active enzyme diversity across phylogenetically distant bacteria. [src: t4ss_cazy_environmental_hgt] See [[concepts/horizontal-transfer-of-carbohydrate-active-enzymes-via-conjugative-machinery]].

## Caveats and Open Work

The analysis is preliminary: NB01–NB04 are complete, while NB05 threshold validation and NB06 manuscript figures are pending. [src: t4ss_cazy_environmental_hgt] All associations are observational, and mechanistic confirmation requires experimental validation. [src: t4ss_cazy_environmental_hgt] The ≤10 kb co-occurrence threshold is not yet validated. [src: t4ss_cazy_environmental_hgt]

Pending work:
- A synteny threshold permutation test, which requires Spark unfiltered data. [src: t4ss_cazy_environmental_hgt]
- BLAST validation of Node_4915, which requires BLAST against NCBI nr. [src: t4ss_cazy_environmental_hgt]
- A housekeeping gene null baseline. [src: t4ss_cazy_environmental_hgt]
- Biome enrichment factorisation, θ = OR(T4SS-CAZy) / [OR(T4SS) × OR(CAZy)]. [src: t4ss_cazy_environmental_hgt]

## Slots Into

- [[concepts/horizontal-transfer-of-carbohydrate-active-enzymes-via-conjugative-machinery]]: 32 high-confidence cross-phylum GT2 HGT events, with T4SS co-localisation, support the hypothesis of T4SS-mediated CAZy dissemination. [src: t4ss_cazy_environmental_hgt]
- [[concepts/environmental-biome-enrichment-of-mobile-cazy-gene-content]]: marine sediment, barley rhizosphere and maize rhizosphere enrichment. [src: t4ss_cazy_environmental_hgt]
- [[concepts/metal-resistance-co-occurrence-with-mobile-gene-transfer-hubs]]: GT2-neighbourhood MAGs are enriched for metal resistance. [src: t4ss_cazy_environmental_hgt]
