---
type: "Concept"
description: "Whether AMR genes located near prophage markers in gene neighborhoods are more often accessory (strain-variable) than distal AMR genes, including threshold sensitivity and heterogeneity; stops at species-level breadth patterns."
sources: ["summaries/prophage_amr_comobilization__REPORT.md"]
---
# Prophage proximity and AMR gene conservation

Prophage-proximal antimicrobial resistance (AMR) genes are slightly more often accessory (strain-variable) than distal ones, but the effect is modest, depends on the distance threshold, and varies by species. [src: prophage_amr_comobilization] See also [[summaries/prophage_amr_comobilization__REPORT]].

## Literature Context

The candidate papers establish a general background: prophages are mobile genetic elements that can carry and spread antibiotic resistance genes. Reviews describe prophages, plasmids, transposons, integrons and resistance islands as DNA elements that frequently carry resistance genes into sensitive organisms [PMID 12190884](https://pubmed.ncbi.nlm.nih.gov/12190884/). Lysogenic phages can disseminate resistance genes by horizontal gene transfer [PMID 36851563](https://pubmed.ncbi.nlm.nih.gov/36851563/). In Klebsiella pneumoniae, prophages are one of several mobile element classes that mediate transfer of resistance and virulence genes [PMID 40298401](https://pubmed.ncbi.nlm.nih.gov/40298401/). In ESKAPE pathogens, some prophages (sal3, phiCTX, SEN34) harbored aminoglycoside resistance genes (aadA, aac) [PMID 35349073](https://pubmed.ncbi.nlm.nih.gov/35349073/). In Streptococcus pyogenes, lytic phages can mediate transfer of antibiotic resistance by generalized transduction, and endogenous prophages are vectors for toxins and other virulence factors [PMID 31111820](https://pubmed.ncbi.nlm.nih.gov/31111820/).

Two papers add cautions. A mini-review on SOS-independent induction lists the gap between bioinformatic predictions of prophage-associated ARGs and their functional transmissibility as an unresolved debate [PMID 43032091](https://pubmed.ncbi.nlm.nih.gov/43032091/). A large genomic analysis of 540 Elizabethkingia anophelis genomes found an open pan-genome with many accessory genes. It reported resistance factors in both the core genome and accessory sets, with the accessory ones often associated with mobile genetic elements within specific lineages. Its mobilome included prophage elements among genetic islands, integrative and conjugative elements, and a small portion of plasmids [PMID 39472795](https://pubmed.ncbi.nlm.nih.gov/39472795/). That paper does not compare prophage-proximal with distal resistance genes.

Against this background, the corpus result is best read as an extension, not as confirmation. None of the candidate papers tests whether AMR genes near prophage markers are more strain-variable than distal ones, so the corpus gene-neighborhood analysis addresses a question the literature here leaves open. The report found proximal genes (within 10 genes) 67.6% accessory and distal genes 65.5% accessory, with a one-sided OR of 1.10 (p=0.005). That is a modest effect. The general idea that prophages carry resistance genes makes a link plausible, but the reviews do not predict its size, its sign at different distances, or its variation among species.

The threshold dependence and heterogeneity are novel relative to these papers. The corpus reports a reversal at very close range (OR=0.78 at 3 genes, OR=0.92 at 5 genes) and stronger effects at broader thresholds (OR=1.19 at 15 genes, OR=1.28 at 50 genes). Only 33 of 74 testable species show OR>1, and the median species-level OR is 0.85. The candidate papers do not speak to these patterns. The corpus hypothesis that broad-range signal reflects genomic islands is compatible with the reported role of genetic islands in the E. anophelis mobilome [PMID 39472795](https://pubmed.ncbi.nlm.nih.gov/39472795/), but this is only suggestive. The corpus caveats still apply: distances are gene ordinals, and only 20 genomes per species were sampled. The prediction-versus-function gap noted in [PMID 43032091](https://pubmed.ncbi.nlm.nih.gov/43032091/) also applies, because co-localization does not show that a gene is mobilized.

## Dataset and co-localization

The gene-neighborhood dataset covers 36,041 AMR gene instances across 100 species, with 20 genomes sampled per species and 1,953 genomes in total. [src: prophage_amr_comobilization] Over half (55.7%) of AMR instances (20,073) sit on a contig that also carries strict prophage markers. [src: prophage_amr_comobilization] Among these co-localized genes, the median distance to the nearest prophage marker is 34 genes. [src: prophage_amr_comobilization] Closer proximity is much rarer. 12,026 instances (33.4%) are within 50 genes, and 7,137 (19.8%) are within 20 genes. [src: prophage_amr_comobilization] 3,731 instances (10.4%) are within 10 genes, and 1,991 (5.5%) are within 5 genes. [src: prophage_amr_comobilization]

## Proximity and accessory status

Proximal AMR genes (within 10 genes) are 67.6% accessory (2,523 accessory and 1,208 core). Distal genes (more than 10 genes) are 65.5% accessory (21,158 accessory and 11,152 core). [src: prophage_amr_comobilization] The report gives a one-sided Fisher's exact OR (odds ratio) of 1.10, p=0.005, with a bootstrap 95% CI (confidence interval) of [1.024, 1.185]. [src: prophage_amr_comobilization] See [[entities/fisher-s-exact-test-with-benjamini-hochberg-fdr]] for the test. The report calls this modest: a 2.1 percentage point difference in accessory fraction, heterogeneous across species. [src: prophage_amr_comobilization]

## Threshold sensitivity

The association depends on the threshold. It is reversed at very close range (OR=0.78 at 3 genes, OR=0.92 at 5 genes). It strengthens at broader thresholds (OR=1.19 at 15 genes, OR=1.28 at 50 genes). [src: prophage_amr_comobilization] The report offers two hypotheses. Genes immediately adjacent to phage structural genes may be core phage components rather than recently acquired cargo. [src: prophage_amr_comobilization] The report says prior contig-level studies did not capture this nuance. [src: prophage_amr_comobilization] Stronger effects at 15-50 genes could capture genomic islands that hold both phage remnants and laterally transferred genes. [src: prophage_amr_comobilization]

## Heterogeneity across species

Only 33 of 74 testable species show OR>1. The median species-level OR is 0.85. [src: prophage_amr_comobilization]

## Tensions

- The pooled estimate is OR=1.10 (p=0.005). [src: prophage_amr_comobilization] The median species-level OR is 0.85, and only 33 of 74 testable species have OR>1. [src: prophage_amr_comobilization]
- Proximity within 3 and 5 genes gives OR=0.78 and OR=0.92. Proximity within 15 and 50 genes gives OR=1.19 and OR=1.28. The sign of the association depends on the cutoff. [src: prophage_amr_comobilization]

## Caveats

- Distances are ordinal gene positions parsed from gene_id, not base pairs, so true genomic distances may differ. [src: prophage_amr_comobilization]
- Only 20 genomes per species were sampled. The report says exhaustive analysis of all 293K genomes would strengthen the findings. [src: prophage_amr_comobilization]
- Core/accessory labels come from species-level pangenome calling (motupan). The same gene can have different conservation status in different species. [src: prophage_amr_comobilization]

## Open Directions

- Repeat the analysis with base-pair distances in place of gene ordinals. This would test whether the 3-5 gene reversal survives a physical distance scale.
- Run all genomes per species instead of 20. This would check whether the modest pooled OR and the species heterogeneity are sampling effects.
- Model species-level ORs against species traits, such as prophage density or pangenome openness. This could explain why only 33 of 74 species have OR>1.
- Annotate genes at 3-5 genes from prophage markers as phage-core or cargo. This would test the core-phage-component hypothesis directly.
- Check whether the 15-50 gene signal falls on annotated genomic islands. This would test the island hypothesis.
