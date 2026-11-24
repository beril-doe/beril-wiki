---
type: "Concept"
description: "Whether growth rate, lag time and yield can be predicted from KO presence/absence or bulk genome features under cross-genus holdout, and what features might be needed instead; it stops at binary growth."
sources: ["summaries/genotype_to_phenotype_enigma__REPORT.md", "summaries/pitfalls.md"]
---
# Predictability of continuous growth kinetics from gene content

Continuous growth kinetics (growth rate µmax, lag time and yield) could not be predicted from KEGG ortholog (KO) presence/absence or from bulk genome features when whole genera were held out. The evidence comes from one project, [[summaries/genotype_to_phenotype_enigma__REPORT|genotype_to_phenotype_enigma]], on ENIGMA strains. It is a consistent null across two model types, and the report reads it as biological, not as a data shortfall. [src: genotype_to_phenotype_enigma]

## Literature Context

The two candidate papers address the genomic feature the hub proposes as its next test, codon usage bias (CUB). Phydon is a framework for genome-based maximum growth rate prediction that combines codon statistics with phylogenetic information [PMID 40335538](https://pubmed.ncbi.nlm.nih.gov/40335538/). Its abstract says codon usage statistics provide useful signals for predicting growth rates of as-yet uncultivated organisms. It also says that adding phylogenetic information improves precision, especially when a close relative with a known growth rate is available. The authors apply it to a database of temperature-corrected growth rate estimates for 111,349 microbial species. They describe their work as giving insight into the predictive power of taxonomic information versus mechanistic, gene-based inference [PMID 40335538](https://pubmed.ncbi.nlm.nih.gov/40335538/).

The second paper qualifies the link between growth rate and CUB. Across bacteria, faster growth is associated with stronger selection for translational speed, more tRNA genes and higher CUB. Within γ-proteobacteria, however, CUB saturates with increasing growth rate even as tRNA gene number keeps rising [PMID 29385509](https://pubmed.ncbi.nlm.nih.gov/29385509/). Cysteine and the NNA/G codon family show weak CUB that does not increase with growth rate. The authors conclude that selection on translational speed alone cannot fully explain variation in CUB, which suggests a role for other functional constraints [PMID 29385509](https://pubmed.ncbi.nlm.nih.gov/29385509/).

The hub's finding is a null. Under genus-blocked holdout, KO presence/absence and bulk genome features gave negative R^2 for mumax, lag and max_A. That null is not contradicted by these papers, because neither tests KO presence/absence under cross-genus holdout. The papers do support the hub's proposed direction. Phydon's abstract reports codon statistics as a useful genomic signal for maximum growth rate, which is consistent with the report's proposal that CUB, through ribosomal efficiency, might explain µmax variation that KO presence cannot. The hub's reading that growth rate depends on factors beyond binary gene content is also compatible with the Phydon framing of mechanistic, gene-based inference as one route alongside taxonomic information. Phydon's abstract does not itself conclude that gene content alone is weak.

The abstracts leave several points untested, and the corpus does not settle them. Phydon's phylogenetic gain is described for cases with a close relative of known growth rate. Whether codon statistics alone would hold up when whole genera are held out, as in the ENIGMA test, is not addressed in the abstract. The saturation of CUB in γ-proteobacteria suggests the hypothesis that CUB may be a weaker predictor among fast growers, and may be less informative for ENIGMA taxa such as Pseudomonas. This is an extrapolation from a different clade and has not been tested. The proposed gRodon or ENC test on the ENIGMA strains therefore extends this literature to a cross-genus, strain-level setting. It is not a replication of either paper.

The hub's GC% inconsistency and the GC confounding of CUB reported in cf_formulation_design are not addressed by these abstracts, so they remain open.

## Evidence for non-predictability

Growth rate (mumax), lag time and yield (max_A) all showed negative R^2 under genus-blocked holdout. This held for the full KO model (NB07, 46K pairs) and for a dedicated bulk-feature regression. The bulk features were genome size, rRNA/tRNA copies, GC%, coding density, KO count and operons. [src: genotype_to_phenotype_enigma] A separate cross-strain test with n=7 also gave negative R^2 for mumax, lag and max_A. [src: genotype_to_phenotype_enigma]

Weak univariate correlations exist: n_unique_KOs against mumax gave r=+0.42, and n_tRNA against mumax gave r=+0.30. [src: genotype_to_phenotype_enigma] The report attributes both to phylogenetic confounding: large-genome Pseudomonas grow fast and small-genome Pedobacter grow slowly. [src: genotype_to_phenotype_enigma] Under cross-genus holdout these correlations gave zero predictive power. [src: genotype_to_phenotype_enigma]

## Why the report calls it biological

The report says that 46K training pairs and 123 ENIGMA strains with continuous targets are enough data. It therefore treats the limit as biological. [src: genotype_to_phenotype_enigma] KO presence tells you whether an organism can use a substrate, not how fast. [src: genotype_to_phenotype_enigma] Growth rate depends on enzyme kinetics (Kcat, Km), expression levels and ribosome efficiency, and binary KO presence/absence captures none of these. [src: genotype_to_phenotype_enigma]

## Features that were not tested

Some planned features were not computed for the growth model, so the null applies only to the features that were used. The report lists GC%, codon usage bias and Morgan molecular fingerprints as planned but not computed. [src: genotype_to_phenotype_enigma] GC% was available for only 32/727 genomes. [src: genotype_to_phenotype_enigma] The report's bulk-feature regression, however, lists GC% among its features. [src: genotype_to_phenotype_enigma] The claims do not say how this fits with the 32/727 coverage, so treat the GC% status as unresolved. Codon usage bias needs nucleotide sequences that JupyterHub cannot access. [src: genotype_to_phenotype_enigma] Morgan fingerprints need RDKit. [src: genotype_to_phenotype_enigma] The report says these would be needed for continuous growth-rate prediction. [src: genotype_to_phenotype_enigma] It also says such prediction would need CUB computation from GenBank files, which are on the CGCMS server but not reachable from JupyterHub, or else expression data. [src: genotype_to_phenotype_enigma]

## Codon usage bias as the proposed next feature

The report proposes [[entities/codon-usage-bias|codon usage bias]] as the natural next feature. It correlates with maximum growth rate through ribosomal protein optimization. [src: genotype_to_phenotype_enigma] The report cites Xu et al. (2025, Phydon) for this. [src: genotype_to_phenotype_enigma] The proposed test uses gRodon S-value or ENC from CDS nucleotide sequences. It asks whether ribosomal efficiency explains the µmax variation that KO presence cannot. [src: genotype_to_phenotype_enigma] This needs GenBank files on the CGCMS server that JupyterHub cannot currently reach. [src: genotype_to_phenotype_enigma]

## Tensions

- In cf_formulation_design, cross-species CUB comparisons were confounded by GC content, which varied 31–73%. [src: pitfalls] CUB is considered meaningful only within species or across species with similar GC content. [src: pitfalls] These claims concern cross-species comparisons in another project; they do not show how GC content would affect the proposed ENIGMA test. See also [[summaries/pitfalls]].
- The GC% status is inconsistent: it is listed among the bulk-feature regression inputs [src: genotype_to_phenotype_enigma], yet also as not computed and available for only 32/727 genomes. [src: genotype_to_phenotype_enigma]

## Open Directions

- Compute gRodon S-value or ENC from the CGCMS GenBank CDS sequences. Then test whether CUB predicts µmax under genus-blocked holdout, which closes the missing-feature gap.
- Check GC content variation among the ENIGMA genomes and include GC% as a covariate or stratifier in the CUB test, given the GC confounding of CUB reported elsewhere.
- Test whether expression data, where available, improves lag and yield prediction over the KO model.
- Clarify which genomes had GC% in the bulk-feature regression, and repeat it with GC% for all 727 genomes.
