<!-- tension-hash: ecd3bef777340e7b -->
# Ecological Association Versus Within-Species and Causal Evidence

The corpus contains a broad environmental association with AMR, but its interpretation is contested by weak within-species effects, incomplete exposure data, competing explanations for metal associations, and non-equivalent definitions of resistance. The disagreement matters because an ecological pattern may reflect environmental selection, lineage structure, host-associated traits, sampling, or annotation choices rather than direct exposure-to-selection or demonstrated gene transfer.

## Evidence Sides

**Broad ecological signal beyond simple species-label artifacts.**  
Environment effects explain 2–13% of AMR-composition variance (η² = 0.02–0.13), and the association persisted after majority-vote thresholds and phylum- and family-level controls, supporting an ecological signal beyond a simple species-label artifact. [src: amr_environmental_resistome] The global MAG result also reports soil prevalence of 5.8% with OR=5.05, versus 1.2% and OR=0.20 in marine samples. [src: metal_resistance_global_biogeography] BacDive reports higher metal-tolerance scores among contamination-associated isolates, including Cohen’s d = +1.00 for heavy-metal contamination (n = 10). [src: bacdive_metal_validation]

**Weak or unresolved within-species structure and no direct causal test.**  
Only 20 of 141 testable families (14%) showed significant within-family effects after FDR correction; whole-genome ecotype analysis found environmental effects significant and positive in 12 species (7.0%), significant and negative in 4 species (2.3%), and absent in 156 species (90.7%). [src: amr_environmental_resistome, ecotype_analysis] The strain analysis found AMR ecotypes in 19.5% of eligible species, but metadata were sparse and only 2 species passed strict testing criteria. [src: amr_strain_variation] Clinical exposure could increase AMR, AMR could contribute to clinical isolation, or both could reflect correlated host-associated traits. [src: amr_environmental_resistome]

**Metal-specific interpretation is contradicted by cross-resistance and confounding.**  
Cross-resistance found no species-scale correlation between multi-metal tolerance and metal-associated isolation (Spearman rho approximately −0.02, p > 0.8), leaving only 20 independent species. [src: metal_cross_resistance] MicrobeAtlas found metal-type diversity associated with groundwater prevalence (ρ = +0.112, p = 0.0019) but not groundwater-specific fold enrichment (ρ = +0.042, p = 0.242). [src: microbeatlas_metal_ecology] Chromium, copper, lead, and zinc co-vary in many industrial soils, leaving soil COG associations versus metal-specific interpretation unresolved. [src: soil_metal_functional_genomics]

**Catalog, mobility, and fitness claims are definition- and scale-dependent.**  
The catalog detects metal and stress systems, while the narrow interpretation is weakened by mercury- and arsenic-resistance families and the 22.2% Other/Unclassified category; the environmental-resistome analysis reports 15,550 unassigned clusters (18.7%), not 18,448 (22.2%). [src: amr_pangenome_atlas, amr_environmental_resistome] Prophage density was strongly associated with AMR breadth (rho=0.572; partial rho=0.464 after controlling for genome count), whereas local proximity had median species-level OR=0.85. [src: prophage_amr_comobilization] T4SS–CAZy evidence reports 92 elevated co-occurrences, 77 GT2 HGT events, 32 normalized high-confidence cross-phylum events, and 10× higher MGE density in T4SS-positive genomes, but no CAZy genes on plasmids by ICEfinder and only 12 IMEs among the top 100 accumulators. [src: t4ss_cazy_environmental_hgt]

## Possible Reconciliations

- **Hypothesis—scale:** Broad between-species environmental structure may coexist with weak within-species adaptation because lineage composition differs across environments.
- **Hypothesis—measurement:** Missing or imprecise geographic coordinates and sparse metadata may attenuate true environmental effects; partial correlations also assume linear relationships between distance matrices. [src: amr_strain_variation, ecotype_analysis]
- **Hypothesis—definition:** The 21% versus 7.0% efflux estimates, and 13% versus 44% core/accessory values, may reflect different entity sets, filters, annotations, and denominators. [src: discoveries, amr_environmental_resistome, amr_fitness_cost]
- **Hypothesis—co-exposure:** Correlated metals may generate a general stress or efflux signal without supporting a specific metal-selection claim.
- **Hypothesis—association versus transfer:** Prophage density and T4SS co-occurrence may indicate shared ecological conditions or capacity, not demonstrated local gene transfer.

## Resolving Work

- Assemble geographically precise, repeated environmental and clinical samples, then fit hierarchical within-species models to test whether exposure predicts AMR after lineage and host adjustment.
- Reanalyze all effect sizes using harmonized entity sets, annotation versions, filters, and denominators; determine whether the 21% versus 7.0% and 13% versus 44% discrepancies persist.
- Measure chromium, copper, lead, and zinc independently in the same soils and use multivariable or experimental exposure designs to separate metal-specific selection from co-variation.
- Compare matched isolates and genomes across exposure gradients, testing whether local prophage, plasmid, ICE, and IME proximity predicts newly acquired resistance rather than only density.
- Combine field fitness, laboratory competition, gene-essentiality, and transposon data to test whether core-gene enrichment predicts environmental activity or merely reflects fitness importance.
