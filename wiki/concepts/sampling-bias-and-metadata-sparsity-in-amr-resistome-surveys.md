---
type: "Concept"
description: "How clinical and isolate sampling skew, environment classification, annotation-tool coverage and sparse or noisy collection-date and isolation-source metadata bias inference of environmental and temporal AMR patterns."
sources: ["summaries/amr_environmental_resistome__REPORT.md", "summaries/amr_pangenome_atlas__REPORT.md", "summaries/amr_strain_variation__REPORT.md"]
---
# Sampling bias and metadata sparsity in AMR resistome surveys

Inference about environmental and temporal antimicrobial resistance (AMR) patterns from public genome collections is limited by who gets sequenced, how environments are labelled, what the annotation tool can detect, and how sparse the collection metadata are. [src: amr_environmental_resistome, amr_pangenome_atlas, amr_strain_variation]

## Clinical and isolate sampling skew

Genome databases over-represent clinical pathogens, which inflates AMR counts for human-associated species. [src: amr_pangenome_atlas] One report adds that clinical isolates are massively overrepresented in NCBI and soil and aquatic species are undersampled. It says the "clinical species carry more AMR" finding partly reflects that clinical species are sequenced because they have AMR. [src: amr_environmental_resistome] A third report finds the GTDB/NCBI collection heavily biased toward clinical and human-associated isolates, especially *K. pneumoniae*, *S. aureus* and *E. coli*, with environmental species underrepresented. [src: amr_strain_variation] These three statements agree. See also [[concepts/clinical-and-human-associated-sampling-bias-in-genome-collections]].

## Environment classification

Environment labels are coarse, and many genomes cannot be labelled at all.

- Of 14,723 AMR-carrying species, 7,838 (53.2%) received a non-"Other/Unknown" environment classification. The Kruskal-Wallis test used only these species, across 6 categories. [src: amr_pangenome_atlas]
- The "Other/Unknown" bin holds 46.8% of species. The report attributes this to sparse and inconsistent free-text isolation_source metadata in NCBI BioSample. [src: amr_pangenome_atlas]
- In the strain-variation report, 52.7% of genomes had no classifiable isolation_source. Only 2 species had enough within-species environmental diversity for chi-squared testing under strict expected-frequency criteria. [src: amr_strain_variation]
- Majority-vote species classification collapses within-species variation, so a "clinical" species may include environmental strains. A sensitivity analysis at 60-90% thresholds mitigates this. [src: amr_environmental_resistome]
- BacDive and NCBI keyword classifiers are approximate, and the report says dedicated metadata curation would improve ecotype analyses. [src: amr_strain_variation]
- The clinical-exposure analysis is a species-level proxy, not a true per-genome within-species comparison. The report says the latter would require billion-row joins. [src: amr_environmental_resistome]

## Annotation-tool and classification coverage

[[entities/amrfinderplus]] focuses on known resistance genes. It may underestimate novel resistance in environmental bacteria, which would bias results toward more AMR in clinical species, where resistance genes are well characterized. [src: amr_environmental_resistome] The strain-variation report likewise notes that novel mechanisms absent from the database are missed. [src: amr_strain_variation]

Other coverage limits:
- 18.7% of AMR clusters (15,550) could not be assigned a mechanism. They were excluded from mechanism fractions, which could bias results if they are non-randomly distributed across environments. [src: amr_environmental_resistome]
- The 95% prevalence threshold for "core" depends on species genome count. Many species have few genomes, so core/accessory labels are imprecise. [src: amr_environmental_resistome]
- The continuous AlphaEarth analysis confirms the discrete environment findings. It adds limited interpretability because the embedding dimensions are opaque and genome coverage is 28%. [src: amr_environmental_resistome]

## Temporal inference and collection dates

Of 513 species with at least 20 genomes spanning at least 3 years (post-1990), none show significant temporal trends in AMR gene count after Benjamini-Hochberg false discovery rate (FDR) correction. [src: amr_strain_variation] Slopes are roughly symmetric around zero, with 251 positive and 262 negative. [src: amr_strain_variation] The report suggests this null likely reflects sparse and noisy BioSample collection dates, not a true absence of trends. It cites well-documented AMR expansions in *S. aureus* and *K. pneumoniae*. [src: amr_strain_variation] It also notes that only 70% of genomes had parseable dates. [src: amr_strain_variation] It proposes partnering with NCBI metadata curation to obtain higher-quality collection dates. [src: amr_strain_variation]

## Open Directions

- Re-run the environment comparison with clinical species down-sampled or weighted to match soil and aquatic genome counts. This would test how much of the "clinical species carry more AMR" signal comes from sampling.
- Compare AMRFinderPlus calls with a database-independent homology or novelty screen on environmental genomes. This would estimate how much novel resistance is missed.
- Rerun the species-level environment tests with within-species per-genome labels for a few well-sampled species. This would show whether majority-vote collapse changes the results.
- Redo the temporal trend test on the subset of genomes with curated collection dates, and add power calculations. This would separate a true null from date noise.
- Improve isolation_source classification, for example by curation or text mining, and report how many more species reach the chi-squared criteria.
