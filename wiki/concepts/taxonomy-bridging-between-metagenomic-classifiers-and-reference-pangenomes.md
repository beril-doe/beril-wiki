---
type: "Concept"
description: "How well community taxonomy calls map onto GTDB pangenome species and how ambiguity in the bridge affects community-weighted scores."
sources: ["summaries/enigma_carbon_census_1__REPORT.md", "summaries/enigma_contamination_functional_potential__REPORT.md", "summaries/functional_dark_matter__REPORT.md", "summaries/microbeatlas_metal_ecology__REPORT.md", "summaries/nmdc_community_metabolic_ecology__REPORT.md", "summaries/phb_granule_ecology__REPORT.md"]
---
# Taxonomy bridging between metagenomic classifiers and reference pangenomes

ENIGMA reports 530 mapped and 862 unmapped genera. [src: enigma_contamination_functional_potential] Ambiguity in the bridge is bounded in one NMDC analysis at ~6.5% of mapped abundance. [src: nmdc_community_metabolic_ecology] The ENIGMA analysis reports the ambiguity but does not bound its effect. [src: enigma_contamination_functional_potential] See [[entities/gtdb]] and [[entities/genus-to-species-clade-taxonomy-bridge]] for background.

## Coverage of the bridge

**NMDC Centrifuge calls map well to GTDB species in one project.** Mean bridge coverage was 94.6%, and all 220 samples passed the 30% QC (quality control) threshold. [src: nmdc_community_metabolic_ecology] In 92% of samples, at least 85% of community abundance mapped to GTDB pangenome species. [src: nmdc_community_metabolic_ecology] Per-sample coverage is stored in a 220-row table. [src: nmdc_community_metabolic_ecology]

**Genus-level mapping of NMDC taxon columns in the PHB project.** The PHB (polyhydroxybutyrate) analysis mapped 3,014/3,492 (86.3%) NMDC taxon columns to GTDB genera with known PHB status. [src: phb_granule_ecology] Its per-sample scores were abundance-weighted sums of genus-level phaC prevalence over 6,365 samples, with a median 87.2% of taxonomic abundance matched to pangenome genera. [src: phb_granule_ecology] These figures are stated on their own, because the claims do not give a common sample set or unit for comparing them with the other NMDC project.

**Microbeatlas.** The CWM (community weighted mean) for PRJNA1084851 excludes the ~83% of reads from genera whose SILVA taxonomy has no match to GTDB AMR (antimicrobial resistance) annotations. [src: microbeatlas_metal_ecology]

**ENIGMA.** There were 530 mapped genera and 862 unmapped genera. [src: enigma_contamination_functional_potential] The unmapped share is 862/1,392 observed genera. [src: enigma_contamination_functional_potential] Mean mapped abundance fraction was 0.343 in strict/relaxed modes (range 0.031 to 0.854) and 0.031 in species-proxy mode (range 0.0002 to 0.543). [src: enigma_contamination_functional_potential]

## Ambiguity in the bridge

Genus matches often hit several species clades, and the choice affects community scores.

In ENIGMA, 150 genera mapped to a unique clade, against 530 mapped genera in total. [src: enigma_contamination_functional_potential] Another 380 genera were ambiguous across several clades. [src: enigma_contamination_functional_potential] The most ambiguous genera include prevotella (358 clades), streptococcus (214) and mycobacterium (186). [src: enigma_contamination_functional_potential]

In NMDC, about 1,352 Centrifuge taxa matched several GTDB clades within a genus. The report picked one representative clade by alphabetical tiebreaking on gtdb_species_clade_id. [src: nmdc_community_metabolic_ecology] Genus-proxy-ambiguous taxa make up ~6.5% of mapped abundance, which bounds how far this choice can move community completeness scores. [src: nmdc_community_metabolic_ecology] See [[concepts/genome-predicted-pathway-completeness-and-community-metabolite-chemistry]].

## Limits on resolution and inference

- The ENIGMA bridge is genus-level at best. One ENIGMA project therefore avoids isolate-specific transfer of pangenome Tier-2 reconstructions and uses direct genome_depot annotation instead. [src: enigma_carbon_census_1] See [[entities/enigma]].
- In ENIGMA species-proxy mode, no high-coverage subset test was feasible at mapped_abundance_fraction >= 0.25, because retained coverage was low. [src: enigma_contamination_functional_potential] The report suggests that, at current taxonomy granularity, stricter resolution sharply reduces analyzable signal without yet strengthening inference. [src: enigma_contamination_functional_potential]
- The NMDC validation in functional_dark_matter maps taxon columns to pangenome genera via ncbi_taxid at genus resolution, so it may miss species-specific dark-gene signals. [src: functional_dark_matter] Only 5 of 6 carrier genera matched. The high significance rate (76/105) likely reflects common genera such as Pseudomonas and Klebsiella dominating both datasets. [src: functional_dark_matter] See [[concepts/compositional-coupling-in-metagenomic-validation-of-carrier-abundance]].
- If the uncovered genera in PRJNA1084851 are systematically more metal-sensitive than the covered ones, CWM would be biased upward. [src: microbeatlas_metal_ecology]

## Open Directions

- Rerun the ENIGMA community-weighted scores with each ambiguous genus (such as prevotella) resampled across its candidate clades. This would show whether the 380 ambiguous genera change results, as the ~6.5% bound does for NMDC.
- Estimate the PRJNA1084851 bias by comparing the metal resistance of matched genera with a sample of unmatched ones. This would test the upward-bias hypothesis.
- Obtain ENIGMA labels below genus, such as isolate genomes, so species-level bridge testing becomes possible.
- Compare the two NMDC bridge coverage figures on one common sample set and one common unit.
