---
type: "Finding"
description: "Growth rate, lag time and yield show negative R^2 under genus-blocked holdout in both the full KO model and a bulk-feature regression, and weak univariate correlations (r=+0.42, r=+0.30) are phylogenetically confounded and give zero predictive power across genera."
finding_id: "genotype_to_phenotype_enigma--ccab2bff"
result: "null result"
source: "genotype_to_phenotype_enigma"
quantities: [{"value": "r=+0.42", "what": "univariate correlation of n_unique_KOs with mumax", "unit": "", "denominator": "", "scope": "not transferable across genera"}, {"value": "r=+0.30", "what": "univariate correlation of n_tRNA with mumax", "unit": "", "denominator": "", "scope": "not transferable across genera"}]
caveat: "GC%, codon usage bias and Morgan fingerprints were planned but not computed, as GC% was available for only 32/727 genomes and nucleotide sequences were inaccessible from JupyterHub."
first_added: "2026-10-27"
source_hash: "e69de667de1b74a70a09c07dc5b5bfb99aa3f042b003017eb1e60ec118fbab42"
---
# Continuous growth parameters are not predictable across genera from gene content

Growth rate, lag time and yield show negative R^2 under genus-blocked holdout in both the full KO model and a bulk-feature regression, and weak univariate correlations (r=+0.42, r=+0.30) are phylogenetically confounded and give zero predictive power across genera. [src: genotype_to_phenotype_enigma]

## Key figures

- **r=+0.42**: univariate correlation of n_unique_KOs with mumax (scope not transferable across genera) [src: genotype_to_phenotype_enigma]
- **r=+0.30**: univariate correlation of n_tRNA with mumax (scope not transferable across genera) [src: genotype_to_phenotype_enigma]

## Evidence

> Growth rate (mumax), lag time, and yield (max_A) show negative R^2 under genus-blocked holdout in BOTH the full KO model (NB07, 46K pairs) and a dedicated bulk-feature regression (genome size, rRNA/tRNA copies, GC%, coding density, KO count, operons). Weak univariate correlations exist (n_unique_KOs vs mumax: r=+0.42; n_tRNA vs mumax: r=+0.30) but they are phylogenetically confounded — large-genome genera (Pseudomonas) grow fast, small-genome genera (Pedobacter) grow slowly. Under cross-genus holdout, these correlations provide zero predictive power. [src: genotype_to_phenotype_enigma]

From the report [[summaries/genotype_to_phenotype_enigma__REPORT]].

## Caveat

GC%, codon usage bias and Morgan fingerprints were planned but not computed, as GC% was available for only 32/727 genomes and nucleotide sequences were inaccessible from JupyterHub. [src: genotype_to_phenotype_enigma]

> **What was NOT used**: GC%, codon usage bias (CUB), and molecular fingerprints (Morgan FP) were planned but not computed — GC% is only available for 32/727 genomes, CUB requires nucleotide sequences not accessible from JupyterHub, and Morgan FP requires RDKit. These would be needed for continuous growth rate prediction. [src: genotype_to_phenotype_enigma]

## Other caveats in this report

- Ribose transporter and protocatechuate cycloisomerase are interpretable feature examples, but concordance with Fitness Browser is weak at 1.19× enrichment; cross-genus gene presence and within-strain essentiality address different questions. [src: genotype_to_phenotype_enigma]
- GTDB-based profiles classify global Pseudomonas genomes as 37.8% clinical, 12.9% soil/plant, and 9.4% aquatic, whereas ENIGMA Pseudomonas are in environmental Pseudomonas_E. Rhodanobacter is reported as 55% aquatic, 10% contaminated, and 0% clinical. Transfer from clinical phenotype databases may be biased. [src: genotype_to_phenotype_enigma]
- Different pH-dependent growth profiles and predictive genomic features for the two clusters are proposed expectations, not reported validation results. [src: genotype_to_phenotype_enigma]
- Matching ENIGMA strains by `ncbi_strain_identifiers` caused 12 of 32 genus-level mismatches. [src: genotype_to_phenotype_enigma]
- The MT20 collision linked Rhodanobacter glycinis to unrelated Streptococcus pneumoniae and introduced 1,751 spurious clinical genomes. GTDB-Tk taxonomy and genus checks reduced verified linkages from 32 to 20 while eliminating false matches. [src: genotype_to_phenotype_enigma]
