---
type: "Gene_Or_Pathway"
description: "The dissimilatory sulfate reduction module (sat, aprAB, dsrAB) and its KO markers (K11180, K11181, K00394, K00395, K00958) used to score sulfate-reduction potential; excludes the DsrEFH sulfite-handling family."
sources: ["summaries/bacillota_b_subsurface_accessory__REPORT.md", "summaries/clay_confined_subsurface__REPORT.md", "summaries/oak_ridge_cultivation_gap__REPORT.md"]
aliases: ["Dissimilatory sulfate reduction", "Dissimilatory sulfate reduction markers", "Dissimilatory sulfate reduction pathway (Sat–AprAB–DsrAB)", "SR", "SR markers", "dsrAB", "dsrAB-aprAB-sat", "sulfate reduction"]
---
# Dissimilatory sulfate reduction pathway

This page covers the dissimilatory sulfate reduction pathway (Sat–AprAB–DsrAB), also written SR, scored here with five KEGG ortholog (KO) markers: K11180, K11181, K00394, K00395 and K00958. [src: bacillota_b_subsurface_accessory] The module is strongly enriched in deep clay-confined genomes. [src: clay_confined_subsurface] Its dsrAB genes are underrepresented in ENIGMA's cultured collection. [src: oak_ridge_cultivation_gap]

## Key facts

- A later report states that the markers were correctly identified. [src: bacillota_b_subsurface_accessory]
- Bagnoud's Opalinus porewater food web included Desulfobulbaceae c16a expressing the complete Wood–Ljungdahl pathway, group 1 [NiFe]-hydrogenase and Sat–AprAB–DsrAB. Three MAGs (metagenome assembled genomes) recurred across seven independent boreholes. [src: clay_confined_subsurface] See [[entities/bagnoud-et-al-2016-opalinus-porewater-food-web]].
- The dissimilatory sulfite reductase subunits K11180 and K11181 serve terminal electron acceptor metabolism. [src: oak_ridge_cultivation_gap]

## Enrichment in deep clay-confined genomes

The deep clay-confined cohort is enriched for the module, and the enrichment is far above the rock-attached expectation. [src: clay_confined_subsurface] Within Bacillota_B the signal also survives phylogenetic control. [src: clay_confined_subsurface]

- Five of nine anchor_deep genomes in the KBase Data Lakehouse carry the module (Sat, AprAB, DsrAB). [src: clay_confined_subsurface] The cohort is enriched for SR markers (5/9 = 56%). [src: clay_confined_subsurface]
- Against the Mitzscherling et al. (2023) rock-attached null (SRB ~0.2% of community), the binomial p is 4.0×10⁻¹², with 5 observed versus 0.018 expected of 9. [src: clay_confined_subsurface] See [[entities/mitzscherling-et-al-2023-rock-attached-community-profile]].
- SR_complete occurred in 5 of 9 anchor_deep genomes versus 5 of 140 soil_baseline genomes, with Fisher OR (odds ratio) 33.8 and p_BH 2.5×10⁻⁴. [src: clay_confined_subsurface]
- Within [[entities/bacillota-b]], SR_complete occurred in 5 of 5 deep genomes versus 4 of 19 baseline genomes (OR=∞, p=0.003, BH-adjusted p=0.044). [src: clay_confined_subsurface] Only sulfate reduction survived the phylogenetic control. [src: clay_confined_subsurface]
- A later report kept this result: the deep-cohort 5/9 comparison against the null remains robust at p=4×10⁻¹². [src: bacillota_b_subsurface_accessory, clay_confined_subsurface]
- That report concludes the porewater-bias headline still holds via SR alone. The Mitzscherling rock-attached versus Bagnoud porewater framing is half-supported on the SR side and unsupported on the corrected iron-reduction (IR) side. [src: bacillota_b_subsurface_accessory]

## Cultured versus subsurface MAGs (ENIGMA)

The markers behave differently in the ENIGMA comparison of cultured isolates with subsurface MAGs. Sulfate reduction has 5 KOs and a mean log2 ratio of +0.79. Enrichment is mixed, and 4/5 KOs are significant. The report calls this a partial match to predictions, with heterogeneity within the category. [src: oak_ridge_cultivation_gap]

- K11180 and K11181 (dsrAB) are 3.0-3.1 log2 depleted in cultured genomes. [src: oak_ridge_cultivation_gap]
- aprAB (K00394) shows no significant difference. [src: oak_ridge_cultivation_gap]
- sat/PAPSS (K00395, K00958) are enriched in cultured genomes. [src: oak_ridge_cultivation_gap]
- The report suggests the two subsystems have different taxonomic distributions. [src: oak_ridge_cultivation_gap]
- Dissimilatory sulfite reduction is systematically underrepresented in ENIGMA's cultured collection for subsurface metabolic characterization. [src: oak_ridge_cultivation_gap]

## Related pages

[[concepts/iron-and-sulfate-reduction-signatures-in-clay-subsurface-porewater-versus-rock-attached-communities]], [[concepts/cultivation-bias-in-genome-collections-versus-uncultivated-lineages]], [[concepts/phylum-level-confounding-of-habitat-specific-anaerobic-gene-content]], [[summaries/clay_confined_subsurface__REPORT]], [[summaries/oak_ridge_cultivation_gap__REPORT]], [[summaries/bacillota_b_subsurface_accessory__REPORT]].
