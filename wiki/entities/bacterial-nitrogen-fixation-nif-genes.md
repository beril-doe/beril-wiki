---
type: "Gene_Or_Pathway"
description: "The nitrogenase nifHDK operon (KEGG module M00175), including nifH as a marker, used as a plant-growth-promoting and nitrogen-fixation marker."
sources: ["summaries/discoveries.md", "summaries/oak_ridge_cultivation_gap__REPORT.md", "summaries/pgp_pangenome_ecology__REPORT.md", "summaries/plant_microbiome_ecotypes__REPORT.md"]
aliases: ["M00175", "nif operon", "nifH", "nitrogen fixation", "nitrogenase", "nitrogenase reductase"]
---
# Bacterial nitrogen fixation (nif genes)

This page covers the nitrogenase nifHDK operon (KEGG module M00175), including nifH as a marker used as a plant-growth-promoting (PGP) and nitrogen-fixation marker. Across the cited reports, nifH behaves as its own ecological guild: depleted in soil and negatively associated with other PGP markers. [src: discoveries, pgp_pangenome_ecology] It is still associated with some plant-associated species within genera. [src: plant_microbiome_ecotypes] See also [[summaries/pgp_pangenome_ecology__REPORT]] and [[summaries/plant_microbiome_ecotypes__REPORT]].

## Key facts

- nifH forms a separate ecological guild, negatively associated with pqqC and hcnC and depleted in soil relative to aquatic environments. [src: discoveries]
- The three species-level plant-association markers are the nif nitrogen-fixation operon, ACC (1-aminocyclopropane-1-carboxylate) deaminase and the hrp/hrc type III secretion system (T3SS) cluster. [src: plant_microbiome_ecotypes]
- The plant_microbiome_ecotypes report assigns high confidence to nitrogen fixation (nifHDK) as a mechanism hypothesis for the beneficial plant-microbiome cohort. [src: plant_microbiome_ecotypes]

## Environmental distribution

nifH is depleted in soil and rhizosphere species, with prevalence 12.9% versus 19.7% in other environments (odds ratio, OR, 0.60; q 5.5e-08). [src: pgp_pangenome_ecology] The report states that diazotrophs are depleted in soil-classified genomes relative to aquatic and host-associated environments. [src: pgp_pangenome_ecology] It attributes this to the database's nitrogen fixers being mostly aquatic/marine (cyanobacteria, Azotobacter) or host-associated (rhizobia). [src: pgp_pangenome_ecology] It also reads the pattern as consistent with nitrogen fixation being energetically expensive and most relevant in oligotrophic aquatic environments and specific symbioses, not bulk soil. [src: pgp_pangenome_ecology] The report relates the depletion to Wardell et al. (2022), who note that nif gene mobility on symbiosis islands is mainly relevant in legume-associated Rhizobiales, not free-living soil diazotrophs. [src: pgp_pangenome_ecology]

Bacillota_A is an exception in the phylum-stratified analysis. nifH is enriched in its soil species (OR = ∞, q = 2.5e-4), which the report attributes to soil-specific anaerobic diazotrophs such as clostridia. [src: pgp_pangenome_ecology]

In the ENIGMA cultured-isolate versus subsurface-MAG (metagenome-assembled genome) comparison, N-fixation had 3 KOs (KEGG orthologs), a mean log2 ratio of +1.56, mixed enrichment and 2/3 significant KOs. The report describes this as variable as predicted. [src: oak_ridge_cultivation_gap]

The report calls for comparing marine/aquatic diazotrophs (cyanobacteria, Azotobacter) with legume-symbiotic rhizobia and free-living soil diazotrophs in genome structure and PGP trait co-occurrence. [src: pgp_pangenome_ecology]

## Co-occurrence with other PGP traits

nifH was negatively associated with hcnC (OR = 0.23, q = 5.8e-29) and with pqqC (OR = 0.57, q = 2.9e-19). [src: pgp_pangenome_ecology] It showed no significant association with ipdC (OR = 1.13, q = 0.54). [src: pgp_pangenome_ecology] The report concludes that nifH-bearing nitrogen fixers form a separate guild with different co-occurrence partners and environmental distribution. [src: pgp_pangenome_ecology] It reads this as diazotrophs being ecologically separate from pqqC/acdS-bearing rhizobacteria, so the classical PGPB suite appears primarily non-diazotrophic. [src: pgp_pangenome_ecology] Despite the negative association, nifH + pqqC is the next most common multi-trait genotype (n = 225), co-occurring in some generalist lineages. [src: pgp_pangenome_ecology] See [[concepts/co-occurrence-of-plant-growth-promoting-genes-and-trait-guilds]], [[entities/hcnc]] and [[entities/pyrroloquinoline-quinone-biosynthesis]].

## Plant association

Nitrogen fixation is associated with plant-associated species in two separate tests that report different odds ratios. In the original NB04 Fisher-test framework, root species showed nitrogen fixation enrichment with OR = 14.5. [src: plant_microbiome_ecotypes] In the genus-cluster-robust generalized linear model (GLM), nitrogen fixation had OR=2.71. [src: plant_microbiome_ecotypes] The full row reads coef 1.00, OR 2.71, 95% confidence interval (CI) [1.54, 4.78] and Benjamini-Hochberg false discovery rate (BH-FDR) q 1.3×10⁻³. [src: plant_microbiome_ecotypes] It survived the within-genus plant-label shuffle with perm p < 0.001. It was one of only 3 of 15 testable markers to do so. [src: plant_microbiome_ecotypes]

## Pangenome structure and detection

- nifH clusters were 63.8% core, 15.1% auxiliary and 21.0% singleton (q vs baseline 4.3e-71). [src: pgp_pangenome_ecology]
- In the plant-associated architecture analysis, nitrogen fixation gene clusters had a 72.3% core fraction. [src: plant_microbiome_ecotypes]
- Nitrogen fixation was among the most common NB02 PGP functions, with 6,139 clusters. [src: plant_microbiome_ecotypes]
- Transposase co-occurrence for nitrogen-fixation markers gave OR=3.76 in the per-marker HGT (horizontal gene transfer) analysis. [src: plant_microbiome_ecotypes]
- The Phase 2b Pfam recovery found nitrogenase NifH PF00142 with 6,632 hits across 4,040 species and 32.4% core. [src: plant_microbiome_ecotypes]
- Pfam recovery added nitrogen-fixation markers to 2,872 species. [src: plant_microbiome_ecotypes]
- For M00175, requiring ≥2 module genes reduced nif-positive species by 346 (14% reduction). [src: plant_microbiome_ecotypes]

Related: [[concepts/domain-based-marker-detection-and-annotation-method-bias]], [[concepts/core-versus-accessory-partitioning-of-gene-functions-and-trait-genes]], [[concepts/mobile-elements-and-horizontal-transfer-of-plant-interaction-genes]].

## Caveats

The nifH cluster count was 2,756, against ~1,913 estimated in the research plan (43% higher). The report attributes this to incremental growth of the GTDB r214 pangenome. It states that the discrepancy does not affect any analysis. [src: pgp_pangenome_ecology] The soil depletion rests on the database composition, as the report itself explains. [src: pgp_pangenome_ecology]

## Open Directions

- Compare marine/aquatic diazotrophs with legume-symbiotic rhizobia and free-living soil diazotrophs in genome structure and PGP trait co-occurrence.
- Test whether the Bacillota_A soil enrichment holds after correcting for the database's taxonomic composition.
- Check which genera drive the difference between the root enrichment (OR = 14.5) and the genus-robust estimate (OR = 2.71).
