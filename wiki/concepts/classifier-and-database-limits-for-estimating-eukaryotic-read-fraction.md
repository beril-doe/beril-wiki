---
type: "Concept"
description: "Which read classifiers and reference databases can measure eukaryotic fraction, and how far values are calibrated or comparable across data sources."
sources: ["summaries/euk_in_prok_correlates__REPORT.md"]
---
# Classifier and database limits for estimating eukaryotic read fraction

In NMDC prokaryote-targeted metagenomes, only GOTTCHA2 gives a usable eukaryotic read fraction, and its values are relative rather than calibrated. The evidence comes from one report, [[summaries/euk_in_prok_correlates__REPORT]], and no other classifier or on-system data source fills the gap. [src: euk_in_prok_correlates]

## Literature Context

The candidate papers show that classifier output depends strongly on the reference database and the algorithm. In a benchmark of bloodstream pathogens and common blood-culture contaminants, Bracken with a standard database performed best. Its median species-level correct assignment was 97.8% (IQR 92.7:99.0) across Illumina and Nanopore data. Kraken2 with a mini database had a median of 86.4% (IQR 50.5:93.7). Human read misclassification was negligible [PMID 36269282](https://pubmed.ncbi.nlm.nih.gov/36269282/). That work used simulated and real data on clinical bacterial species, not environmental eukaryotes, so it speaks to database effects in general and not to eukaryotic fraction.

Other work shows that database coverage limits what k-mer classifiers can report. Kaiju uses protein-level matching and was reported to classify up to 10 times more reads in real metagenomes than k-mer-based classifiers. Its advantage is greatest in genera that are underrepresented in reference databases [PMID 27071849](https://pubmed.ncbi.nlm.nih.gov/27071849/). Kun-peng, run against a 4.3 TB pan-domain database of 204,477 genomes, classified 69.8%-94.3% of reads across 586 metagenomic samples. That was a 20%-60% gain over the standard Kraken2 database with 62,026 genomes. The authors attribute the gain to expanded reference coverage and note that a small fraction of false positives is inherent to k-mer methods [PMID 41838875](https://pubmed.ncbi.nlm.nih.gov/41838875/). MetageNN reports higher sensitivity than Kraken2 when the reference database is incomplete. It is described as proof-of-concept work on long reads [PMID 38627615](https://pubmed.ncbi.nlm.nih.gov/38627615/). KRANK reports that k-mer libraries are taxonomically imbalanced and that novel and poorly sampled groups are hurt most by subsampling [PMID 39209553](https://pubmed.ncbi.nlm.nih.gov/39209553/).

The corpus finding is consistent with this literature. In NMDC prokaryote-targeted metagenomes, Kraken2 and Centrifuge show domain-level Eukaryota signals of about 0. The report attributes this to NMDC reference databases restricted to prokaryotes. Separately, the Kraken database's only eukaryotic kingdom is Metazoa/human. The benchmarks above support the general point that a classifier cannot report taxa its database lacks, and that wider references raise classified fractions. The null Eukaryota signal is therefore a database limitation and not evidence of absent eukaryotes. The corpus extends the literature by applying this reasoning to eukaryotic read fraction, which these papers do not measure. It also treats GOTTCHA2 as the only usable estimator, with values read as relative or ordinal rather than calibrated. None of the candidates evaluates GOTTCHA2, so that recommendation is not tested by this literature.

The proposed remedies, calibration against a spike-in or SPF estimate and a many-study raw-read resource, have no direct counterpart in the candidates. Kun-peng suggests that pan-domain databases are becoming feasible with modest memory, so a broader eukaryote-aware reference for [[entities/kraken2]]-style classification may be attainable. That remains a hypothesis here, and the reported 586-sample evaluation does not show eukaryotic accuracy. A virome assembly comparison was also retrieved, but it concerns assembly and not read classification, so it does not bear on this page [PMID 30691529](https://pubmed.ncbi.nlm.nih.gov/30691529/).

## Which classifiers work

Kraken2 and Centrifuge show domain-level Eukaryota signals of about 0. Their NMDC reference databases are restricted to prokaryotes, so GOTTCHA2 is the only usable eukaryotic estimator. [src: euk_in_prok_correlates] Kraken's only eukaryotic kingdom in the NMDC reference database is Metazoa/human. [src: euk_in_prok_correlates] See [[entities/kraken2]] for that classifier.

The report recommends GOTTCHA2, which is plastid- and eukaryote-aware, to measure eukaryotic fraction. [src: euk_in_prok_correlates] Its response variable is GOTTCHA2 relative eukaryotic abundance (Eukaryota plus plastid) at superkingdom rank, per ReadbasedAnalysis run. [src: euk_in_prok_correlates]

## Calibration and comparability

GOTTCHA2 values depend on the classifier and its database. The report says to read them as relative or ordinal, not as calibrated absolute contamination. [src: euk_in_prok_correlates]

The report's data-landscape scan found no on-system source with per-sample eukaryotic read fraction across many studies. MGnify is a MAG (metagenome assembled genomes) catalog here. SPIRE, GEM and Tara are MAG collections. EMP (Earth Microbiome Project) is 16S. [src: euk_in_prok_correlates] Within the [[entities/kbase-data-lakehouse]], cross-source comparison of eukaryotic fraction therefore has no ready reference. [src: euk_in_prok_correlates]

## Proposed remedies

The report proposes absolute calibration of GOTTCHA2 eukaryotic fraction against a spike-in or SPF estimate, to move from ordinal to calibrated contamination estimates. [src: euk_in_prok_correlates] It also proposes importing a many-study raw-read resource, such as the SPF corpus with 136K metagenomes across thousands of studies, or computing eukaryotic fraction across a broader collection. This would break the batch confound and allow a properly powered cross-study correlate analysis. [src: euk_in_prok_correlates]

## Open Directions

- Calibrate GOTTCHA2 against a spike-in or SPF estimate, to close the ordinal-only gap. [src: euk_in_prok_correlates]
- Compute eukaryotic fraction across the SPF corpus, to break the batch confound and allow a properly powered cross-study analysis. [src: euk_in_prok_correlates]
