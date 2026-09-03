---
type: "Concept"
description: "Classifier database compatibility constrains cross-study taxonomic comparison"
sources: ["summaries/euk_in_prok_correlates__REPORT.md", "summaries/ecotype_analysis__REPORT.md"]
---
# Classifier database compatibility limits cross-study taxonomic quantification

Cross-study taxonomic quantification is only comparable when classifiers have sufficiently compatible reference databases, taxonomic scopes, and reporting behavior. The same biological reads can produce very different apparent taxonomic abundances when one database represents eukaryotes or plastids and another is restricted primarily to prokaryotes. [src: euk_in_prok_correlates]

This issue is distinct from ordinary classifier disagreement: a database that cannot represent a taxon cannot provide evidence that the taxon is absent. Consequently, cross-study comparisons should treat classifier identity and database composition as analytical variables, not merely software metadata. [src: euk_in_prok_correlates]

## Evidence from the NMDC eukaryotic-read analysis

The [[summaries/euk_in_prok_correlates__REPORT]] analysis quantified eukaryotic reads across 2,759 NMDC ReadbasedAnalysis runs from 9 studies using native `nmdc.results` classifications. [src: euk_in_prok_correlates]

GOTTCHA2 detected eukaryotic reads in 77% of the 2,759 runs, with a median eukaryotic fraction of 2.7%, a mean of 13.3%, and 20% of runs exceeding 20% eukaryotic reads. [src: euk_in_prok_correlates]

Among runs with detectable eukaryotic signal, plastid sequences represented a median 100% of that signal, indicating that the observed environmental eukaryotic component was dominated by plant or algal chloroplast DNA rather than animal-host DNA. [src: euk_in_prok_correlates]

Kraken2 and Centrifuge produced approximately 0 domain-level Eukaryota signal because their NMDC reference databases were prokaryote-restricted; Kraken2's only eukaryotic kingdom was Metazoa/human. [src: euk_in_prok_correlates]

This result supports the interpretation that the near-absence of a metazoan or host signal in the Kraken2 and Centrifuge outputs was not interchangeable with GOTTCHA2's eukaryotic estimate, because the classifiers had different representational coverage. [src: euk_in_prok_correlates]

GOTTCHA2 was therefore the only usable estimator of eukaryotic fraction in this analysis, and its values should be interpreted as relative or ordinal rather than calibrated absolute contamination. [src: euk_in_prok_correlates]

## Consequences for environmental comparisons

The apparent environmental pattern was strong in the GOTTCHA2-derived response: aquatic freshwater samples had 99.5% eukaryotic detection and a plastid share of 1.00, terrestrial soil samples had 55.7% detection and a plastid share of 0.43, and plant-root samples had 100% detection and a plastid share of 0.03. [src: euk_in_prok_correlates]

These findings support [[concepts/environment-embedding-geography]] only after classifier and database compatibility are established, because an environmental contrast can reflect differences in detectable taxonomic space rather than differences in biological composition. [src: euk_in_prok_correlates]

The [[summaries/ecotype_analysis__REPORT]] analysis **refines** this safeguard: environmental representation can also be incomplete before taxonomic classification, because AlphaEarth embeddings covered only 28.4% of genomes in an analysis of 13,381 genomes across 224 species, yielding correlation results for 172 species. [src: ecotype_analysis]

The eukaryotic fraction differed by matrix in a Kruskal–Wallis test with H=77.8 and p=1.3×10⁻¹⁷, and all pairwise matrix contrasts were significant after BH-FDR, where BH-FDR denotes the Benjamini–Hochberg false-discovery-rate procedure. [src: euk_in_prok_correlates]

However, these statistical results describe variation in one classifier-derived response and do not establish that the reported fractions are absolute or directly comparable across independently processed datasets. [src: euk_in_prok_correlates]

The report also found that environment explained no more variance than `study_id` alone in cross-study modeling: random cross-validation gave R²=0.35 for environment and R²=0.24 for `study_id` alone, whereas GroupKFold out-of-study validation gave R²=−0.30 for environment and R²=−0.39 for environment plus sequencing. [src: euk_in_prok_correlates]

GroupKFold is a cross-validation design in which complete studies are held out as groups, so these results show that cross-study environmental prediction was not portable even when sequencing metadata were added. [src: euk_in_prok_correlates]

The out-of-study detection AUC was 0.56, approximately chance, further weakening the interpretation of the cross-collection environmental association as a transferable biological rule. [src: euk_in_prok_correlates]

This refines [[concepts/cross-cohort-microbiome-portability]]: portability requires not only comparable sample metadata and validation splits, but also compatible classifier reference databases and taxonomic scopes. [src: euk_in_prok_correlates]

The ecotype analysis **supports** this portability caution at a different measurement layer: phylogeny dominated whole-genome gene-content similarity in most species, while significant environment effects were uncommon, suggesting that environmental signal may be confined to particular gene subsets rather than being reliably recoverable from genome-wide similarity. [src: ecotype_analysis]

## Database compatibility is part of the measurement model

A classifier-derived abundance is a measurement produced jointly by sequencing reads, the classifier, its reference database, and its taxonomic reporting scheme. [src: euk_in_prok_correlates]

In this analysis, the response was GOTTCHA2 relative eukaryotic abundance, defined as Eukaryota plus plastid abundance at superkingdom rank for each ReadbasedAnalysis run. [src: euk_in_prok_correlates]

Because Kraken2 and Centrifuge were prokaryote-restricted in this NMDC deployment while GOTTCHA2 was plastid- and eukaryote-aware, their outputs could not be treated as interchangeable measurements of eukaryotic fraction. [src: euk_in_prok_correlates]

This supports [[concepts/taxonomic-resolution-dependent-functional-inference]] and [[concepts/environmental-resistome]] at the measurement level: downstream ecological or functional conclusions inherit the representational limits of the upstream database. [src: euk_in_prok_correlates]

The ecotype analysis **refines** this claim by showing that environmental conclusions also inherit limitations in environmental embeddings and metadata: geographic coordinates were often missing or imprecise, and partial correlations assume linear relationships between distance matrices. [src: ecotype_analysis]

The same limitation applies to negative evidence: an approximately 0 Eukaryota signal from a prokaryote-restricted database cannot by itself demonstrate that eukaryotic reads were absent. [src: euk_in_prok_correlates]

## Analytical safeguards

Cross-collection contamination or eukaryotic-signal analyses should control for study or batch using GroupKFold by study, or should rely on within-study contrasts where classifier, database, and laboratory processing are held approximately constant. [src: euk_in_prok_correlates]

The report's within-study NEON analysis provides the stronger design: among 1,186 runs from one sampling program with a constant protocol and batch, local vegetation was associated with eukaryotic fraction at H=119.1 and p=7.6×10⁻²¹, and geography differed across 47 sites at H=310.4 and p=2.4×10⁻⁴⁶. [src: euk_in_prok_correlates]

A model using local environment and geography achieved within-study five-fold R²=+0.17 ± 0.06, contrasting with the cross-study out-of-study R²=−0.30; this supports a fine-scale environmental signal under approximately constant measurement conditions, while leaving possible sub-batch confounding. [src: euk_in_prok_correlates]

The analysis also avoided biosample-level pseudo-replication by working at the `workflow_run_id` level, because 1,067 of 2,759 runs were pooled from multiple biosamples. [src: euk_in_prok_correlates]

This data-structure choice complements [[concepts/cross-tenant-data-bridging]], where correct joins between workflow results, biosamples, and studies are necessary before classifier compatibility can be evaluated. [src: euk_in_prok_correlates]

For environmental-genome comparisons, the ecotype analysis **supports** the analogous use of direct environmental metadata and alternative embedding distances, and recommends testing specific COG categories rather than relying only on whole-genome gene content. [src: ecotype_analysis]

## Tensions

The data show both a strong matrix association and poor cross-study generalization: matrix contrasts were statistically significant, but the out-of-study environment model had R²=−0.30 and detection AUC=0.56. [src: euk_in_prok_correlates]

This is not a contradiction between the classifier and the ecological result; it is a tension between within-collection association and transportable inference, with classifier/database compatibility and study structure among the factors that must be controlled. [src: euk_in_prok_correlates]

The ecotype analysis presents a related but non-identical limitation: it found that phylogeny generally dominated environmental similarity as a predictor of genome-wide gene-content similarity, whereas the present analysis detected strong within-matrix classifier-derived environmental associations. These results cannot be directly reconciled because they use different responses, data structures, and environmental representations. [src: ecotype_analysis, euk_in_prok_correlates]

## Open Directions

- Reclassify the same raw reads with matched, eukaryote-aware Kraken2, Centrifuge, and GOTTCHA2 databases, then use paired agreement analyses to determine which environmental contrasts persist after database scope is harmonized. [src: euk_in_prok_correlates]
- Build a study-held-out benchmark using the 9 NMDC studies and GroupKFold, with classifier identity and reference-database version as recorded covariates, to test whether environmental prediction improves after measurement compatibility is controlled. [src: euk_in_prok_correlates]
- Compare classifier-derived eukaryotic fractions with targeted plastid, fungal, and protist markers in the 1,186-run NEON subset, using within-study models to ask whether the GOTTCHA2 signal tracks distinct biological sources or database-specific detection. [src: euk_in_prok_correlates]
- Reconstruct pooled-run metadata from all contributing biosamples rather than the representative `MIN(biosample_id)` record, then test whether metadata-label uncertainty changes the within-study vegetation and geography associations. [src: euk_in_prok_correlates]
- In the 172-species ecotype subset, compare direct environmental metadata and alternative embedding distances with classifier-compatible taxonomic measures, then test whether specific COG categories recover environmental effects missed by whole-genome similarity. [src: ecotype_analysis]
