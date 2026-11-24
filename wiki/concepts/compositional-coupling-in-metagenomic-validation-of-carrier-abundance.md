---
type: "Concept"
description: "Independent metagenome-based validation of lab-derived predictions using genus-level taxon bridges, and how abundant ubiquitous genera inflate correlations; stops at the NMDC-based tests in this report."
sources: ["summaries/functional_dark_matter__REPORT.md", "summaries/phb_granule_ecology__REPORT.md"]
---
# Compositional coupling in metagenomic validation of carrier abundance

This page covers independent metagenome-based validation of lab-derived predictions through genus-level taxon bridges, and how abundant, ubiquitous genera inflate the resulting correlations. It stops at the NMDC-based tests in the functional_dark_matter report, with one cross-check from phb_granule_ecology. The directional predictions held up in every pre-registered test. The report itself says the strength of the signal is inflated by compositional coupling, so the correlations show ecological co-occurrence and not causal gene-phenotype links. [src: functional_dark_matter]

## Literature Context

The candidate papers say little about the central issue here, which is compositional coupling between genus-level carrier abundance and community trait or abiotic correlations. One paper is indirectly relevant. Readsynth is a simulation tool for reduced metagenomic sequencing, a middle ground between amplicon and whole-metagenome sequencing. It was built to examine composition biases in that approach [PMID 38750423](https://pubmed.ncbi.nlm.nih.gov/38750423/). The authors report that restriction enzyme choice and size selection in library preparation are non-trivial decisions that bias downstream profiling and quantification [PMID 38750423](https://pubmed.ncbi.nlm.nih.gov/38750423/). Their fixed length taxonomic ratios improved quantification accuracy of simulated human gut communities compared with mean or median coverage [PMID 38750423](https://pubmed.ncbi.nlm.nih.gov/38750423/). The study is a simulation and covers only reduced-representation libraries, so it does not describe the NMDC samples used in the functional_dark_matter report.

The general lesson is that relative-abundance estimates from metagenomes carry method-dependent biases. This is consistent with the report's caution that genus abundance scores are not clean measurements of independent gene-phenotype links. It is only loosely related, though. Readsynth concerns bias introduced by library preparation and read assignment. The report's concern is different: abundant, ubiquitous genera such as Pseudomonas, Klebsiella and Bacteroides contribute to both the carrier abundance score and the community trait score. Readsynth neither tests nor contradicts that mechanism.

The tobacco bacterial wilt metagenome study is not relevant to the hub's claims. It compares rhizosphere communities of symptomatic and asymptomatic plants and does not examine genus bridges, trait-score correlations or compositional coupling. It does report enrichment of Pseudomonas among opportunistic taxa in symptomatic rhizospheres [PMID 42063498](https://pubmed.ncbi.nlm.nih.gov/42063498/). That finding is a different setting and says nothing about the NMDC correlations, so I draw no inference from it.

The corpus findings therefore sit largely outside what these candidates cover. The pre-registered directional confirmations are not tested against any candidate paper: 4 of 4 abiotic predictions and 7 of 7 trait predictions. The same holds for the ~20× inflation estimate for exploratory tests (441/449 significant vs. 22.5 expected), the partial null approximations, and the PHB-high versus PHB-low genus comparison (Mann-Whitney p = 8.41 x 10^-22). The retrieved literature does not support or challenge these figures. The report's own caveat stands: the correlations show ecological co-occurrence, not causal gene-phenotype validation. A permutation null on the raw NMDC per-sample matrices, as listed in the open directions, remains the way to settle how much signal survives coupling. See [[concepts/metagenome-based-cross-validation-of-genomic-trait-predictions]] for related framing.

## The genus bridge

The validation used a two-tier taxonomy bridge (gtdb_metadata ncbi_taxid plus taxonomy_dim fallback). It mapped 5 of 6 carrier genera to 47 NMDC taxon columns across 6,365 metagenomic samples. [src: functional_dark_matter] The bridge works at genus resolution and may miss species-specific dark-gene signals. [src: functional_dark_matter] See [[concepts/genus-level-taxonomy-bridging-to-pangenome-clades-and-its-coverage-limits]] and [[entities/nmdc-integrated-collections]] for background.

## Abiotic validation

The report calls the NMDC abiotic confirmations independent, because the metagenomic samples are entirely separate from the pangenome-based carrier analysis. [src: functional_dark_matter] All 4 testable pre-registered predictions were confirmed. [src: functional_dark_matter] The four are listed below.

- Nitrogen-source carriers with total nitrogen content: rho +0.109, n 1,231, FDR 2.3e-4, positive as expected. [src: functional_dark_matter]
- Nitrogen-source carriers with ammonium nitrogen: rho +0.231, n 1,230, FDR 8.0e-16, positive as expected. [src: functional_dark_matter]
- pH carriers with pH: rho +0.157, n 4,366, FDR 7.4e-25, positive as expected. [src: functional_dark_matter]
- Anaerobic carriers with dissolved oxygen: rho -0.298, n 272, FDR 1.5e-6, negative as expected. [src: functional_dark_matter]

Beyond these, 76 of 105 total Spearman correlation tests reached FDR < 0.05 (72.4%). [src: functional_dark_matter] The report attributes this high rate likely to confounding. Pseudomonas, Klebsiella and Bacteroides are among the most abundant and ubiquitous taxa in NMDC samples, so their abundance correlates with many abiotic variables whatever the condition class. [src: functional_dark_matter] Only 5 of 6 carrier genera matched, and common genera such as Pseudomonas and Klebsiella likely dominate both datasets. [src: functional_dark_matter] The report therefore treats the 4/4 pre-registered rate as the more meaningful metric, since it tests specific directional hypotheses. [src: functional_dark_matter]

## Trait-condition validation and compositional coupling

The same genus bridge was used to correlate carrier-genera abundance with community functional trait scores. These came from NMDC trait_features, which has 76 functional_group columns across 6,365 samples. [src: functional_dark_matter] All 7 pre-registered predictions were confirmed at FDR < 10⁻²¹. [src: functional_dark_matter] The reported correlations were:

- Nitrogen-source carriers with nitrogen_fixation: ρ=0.60. [src: functional_dark_matter]
- Nitrogen-source carriers with nitrate_denitrification: ρ=0.52. [src: functional_dark_matter]
- Carbon-source carriers with aerobic_chemoheterotrophy: ρ=0.73. [src: functional_dark_matter]
- Carbon-source carriers with fermentation: ρ=0.59. [src: functional_dark_matter]
- Anaerobic carriers with fermentation: ρ=0.59. [src: functional_dark_matter]
- Anaerobic carriers with iron_respiration: ρ=0.45. [src: functional_dark_matter]

An additional 441/449 exploratory tests reached FDR < 0.05. [src: functional_dark_matter]

This near-universal significance likely reflects compositional coupling. Genera abundant in a sample contribute to both the carrier abundance score and the community trait score. The high correlations are therefore not independent gene-phenotype validation. [src: functional_dark_matter] The report's NB10 puts a number on this: an inflation factor of ~20× for exploratory tests (441/449 significant vs. 22.5 expected). [src: functional_dark_matter]

### Partial null approximations

NB10 gives partial null approximations. A sign test on the 7/7 pre-registered trait directions gives p = 0.0078. [src: functional_dark_matter] A sign test on the 4/4 pre-registered abiotic directions gives p = 0.0625, which is above 0.05 in itself. [src: functional_dark_matter] Fisher's combined probability across all 11 pre-registered tests gives p ≈ 0. [src: functional_dark_matter] A full permutation test that shuffles sample labels remains future work. It needs Spark access to raw per-sample matrices. [src: functional_dark_matter]

The report still draws a positive inference. It says directional concordance across independent datasets supports the idea that lab fitness phenotypes reflect real ecological function. [src: functional_dark_matter] It describes the NMDC correlations as community-level corroboration across 6,365 metagenomic samples. [src: functional_dark_matter] For the wider framing, see [[concepts/concordance-between-laboratory-fitness-phenotypes-and-field-environments-of-gene-carriers]], [[concepts/metagenome-based-cross-validation-of-genomic-trait-predictions]] and [[concepts/adversarial-review-pre-registration-and-multiple-testing-discipline]].

## Data not yet used

The NMDC dataset includes proteomics (346K observations) and metabolomics (3.1M observations) that the report did not use. [src: functional_dark_matter] The report proposes that correlating dark gene carrier abundance with metabolite or protein profiles could provide more direct functional evidence than abiotic correlations alone. [src: functional_dark_matter]

## A separate genus-level cross-check

The phb_granule_ecology report used a similar genus bridge for a different trait. It matched 693 genera between pangenomes and NMDC metagenomes. PHB-high genera (>=50% phaC prevalence) had higher NMDC abundance than PHB-low genera (Mann-Whitney p = 8.41 x 10^-22). [src: phb_granule_ecology] This is an abundance comparison between genus groups. The cited claim does not say whether it was tested for the coupling described above.

## Open Directions

- Run the full NMDC permutation test, shuffling sample labels on the raw per-sample matrices. This would replace the partial nulls, the sign test and Fisher combination, with a proper null for the coupling.
- Re-test the carrier-trait correlations after removing or adjusting for the abundant ubiquitous genera (Pseudomonas, Klebsiella, Bacteroides). This would show how much signal remains beyond coupling.
- Correlate carrier abundance with NMDC metabolite and protein profiles. This would give more direct functional evidence.
- Check whether the abundance advantage of PHB-high genera in NMDC survives the same abundance adjustment.
- Test at species resolution where the bridge allows. This would address the genus-level blind spot.
