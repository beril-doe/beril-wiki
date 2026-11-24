---
type: "Concept"
description: "Whether and how a species' isolation environment (clinical, gut, soil, aquatic, host-associated) predicts the number of AMR gene clusters it carries; stops at mechanism composition and within-species effects."
sources: ["summaries/amr_environmental_resistome__REPORT.md", "summaries/amr_pangenome_atlas__REPORT.md", "summaries/amr_strain_variation__REPORT.md", "summaries/discoveries.md"]
---
# Environmental structuring of antimicrobial-resistance gene content

Whether and how a species' isolation environment (clinical, gut, soil, aquatic, host-associated) predicts the number of AMR gene clusters it carries; stops at mechanism composition and within-species effects.

## Scale and main result

The amr_environmental_resistome report analysed 82,908 AMR gene clusters across 14,723 species, out of 27,700 total species. [src: amr_environmental_resistome] It used 280,337 genomes with ncbi_env data, of which 93.5% were classified per genome. [src: amr_environmental_resistome] Majority-vote species-level environment assignments cover 95% of species (13,981 species). [src: amr_environmental_resistome] The report describes this as the largest genomic analysis of environmental AMR distribution, extending Gibson et al. (2015) from ~6K genomes to 293K genomes across 14,723 species. [src: amr_environmental_resistome]

Clinical species have a median of 5 AMR gene clusters, against 2 for soil, aquatic and host-associated species (Kruskal-Wallis H = 781.9, p = 9.4×10⁻¹⁶⁷, η² = 0.056). [src: amr_environmental_resistome] Human gut species are similar to clinical, with a median of 5. [src: amr_environmental_resistome] Clinical and gut species carry 2.5× more AMR clusters than soil or aquatic species, and the excess is almost entirely in the accessory (acquired) gene pool. [src: amr_environmental_resistome]

Of 15 pairwise environment comparisons, 13 are significant after false discovery rate (FDR) correction. [src: amr_environmental_resistome] The largest effect is clinical versus aquatic (rank-biserial r = −0.49). [src: amr_environmental_resistome] The Kruskal-Wallis effect holds at 50%, 60%, 75% and 90% majority-vote thresholds (η² = 0.044–0.056). [src: amr_environmental_resistome]

## Independent support from other reports

The amr_pangenome_atlas report **supports** the gradient. Human/Clinical species carry 10.6 AMR clusters per species (n=2,248). [src: amr_pangenome_atlas] Soil/Terrestrial species carry 4.6 (n=2,469). [src: amr_pangenome_atlas] Aquatic species carry 3.9 (n=1,827). [src: amr_pangenome_atlas] Animal species carry 3.0 (n=959). [src: amr_pangenome_atlas] The difference is significant (Kruskal-Wallis H=440, p=7.0e-93). [src: amr_pangenome_atlas] That report describes clinical species as carrying 2.7x more AMR, and more of it acquired. [src: amr_pangenome_atlas] Clinical species have a lower AMR core fraction than environmental species (30.8% vs 58.1%). The report reads this as antibiotic-exposed environments selecting acquired resistance, while environmental species keep mainly intrinsic defenses. [src: amr_pangenome_atlas]

The amr_strain_variation report **supports** the direction. Host-associated species consistently carry more AMR genes per genome than terrestrial or aquatic species under both a rule-based classification approximating BacDive categories and NCBI keyword-based annotation (Kruskal-Wallis, p < 0.05). [src: amr_strain_variation] Both methods agree that human-clinical isolates show the highest burden. [src: amr_strain_variation]

Environmental diversity also tracks AMR load. Across 2,684 species with ≥3 genomes and embeddings, AlphaEarth embedding diversity predicts AMR count (Spearman rho=0.466, p=1.6e-144). [src: amr_pangenome_atlas] Species sampled from more diverse environments carry AMR genes that are less core (rho=-0.173, p=1.8e-19). [src: amr_pangenome_atlas] Within 823 multi-environment species, clinical strain fraction predicts total AMR (rho=0.465, p=2.2e-45). [src: discoveries]

## Limits on the result

- **Effect size.** All tests are highly significant, but effects are modest (η² = 0.02–0.13). Environment explains 2-13% of variance in AMR composition, and phylogeny likely explains much more. [src: amr_environmental_resistome]
- **Phylogeny.** The discoveries digest says all amr_environmental_resistome findings survive family-level phylogenetic control, with 20/141 families significant. [src: discoveries]
- **Causation.** The data show correlation. Clinical species may carry more AMR because of antibiotic exposure, or may be clinical because they carry more AMR (virulence-resistance co-selection). [src: amr_environmental_resistome]
- **Metadata coverage.** In the amr_pangenome_atlas analysis, only 7,838 of 14,723 AMR-carrying species (53.2%) had a non-Other/Unknown environment. The Kruskal-Wallis test used only these, across 6 categories. [src: amr_pangenome_atlas] The Other/Unknown bin holds 46.8% of species, reflecting sparse and inconsistent free-text isolation_source metadata in NCBI BioSample. [src: amr_pangenome_atlas]
- **Unexecuted analyses.** PCoA (principal coordinates analysis) ordination, PERMANOVA (permutational multivariate analysis of variance), environment-specific gene identification, MAG (metagenome assembled genomes) versus isolate assessment, and archaea-specific analysis were planned but not executed. [src: amr_environmental_resistome]

## Tensions

- Absolute levels differ between reports. amr_environmental_resistome gives medians of 5 (clinical) versus 2 (soil, aquatic and host-associated). [src: amr_environmental_resistome] amr_pangenome_atlas gives 10.6 clusters per species for Human/Clinical versus 3.0–4.6 for the other classes. [src: amr_pangenome_atlas] These are a median and per-species figures, so each is stated on its own. The ratios reported are 2.5× [src: amr_environmental_resistome] and 2.7×. [src: amr_pangenome_atlas]

## Open Directions

- Fit models with phylogeny and environment together, for example within-genus contrasts, to measure how much of the 2–13% environment effect survives. This addresses the modest η² and the phylogeny caveat.
- Rerun the planned PCoA and PERMANOVA on AMR mechanism composition. These were planned but not executed.
- Reclassify the Other/Unknown species, using AlphaEarth embeddings where available, to test whether the gradient holds beyond the well-classified half.
- Run the MAG versus isolate comparison and an archaea-specific analysis, to check for sampling-source bias.
- Use longitudinal or within-species strain data to test whether exposure or co-selection explains the clinical excess.
