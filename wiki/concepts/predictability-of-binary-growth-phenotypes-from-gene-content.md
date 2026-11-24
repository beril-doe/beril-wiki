---
type: "Concept"
description: "How well KEGG ortholog presence/absence, and pathway-completeness rules compared with machine-learning models (with or without literature-corpus transfer), predict whether a genome grows on a substrate, by condition class and held-out genus; stops at continuous growth kinetics."
sources: ["summaries/genotype_to_phenotype_enigma__REPORT.md"]
---
# Predictability of binary growth phenotypes from gene content

In the ENIGMA genotype-to-phenotype report, binary growth is predictable from KEGG ortholog (KO) presence/absence for amino acids and nucleosides, only moderately for carbon sources, and not for metals, antibiotics or nitrogen. [src: genotype_to_phenotype_enigma] The evidence comes from one report. It validates with genus-blocked holdout, where each genus is held out in turn. [src: genotype_to_phenotype_enigma] It stops at binary growth: growth rate is not predicted by gene content here. [src: genotype_to_phenotype_enigma] See also the [[summaries/genotype_to_phenotype_enigma__REPORT|report summary]].

## Literature Context

Only one candidate paper bears directly on predicting binary phenotypes from gene content. [PMID 42505143](https://pubmed.ncbi.nlm.nih.gov/42505143/) used complete genomes of 48 isolates from Alaskan permafrost, seasonally frozen active layer soils and terrestrial ice. It annotated them with KEGG orthologs and compared the annotations with phenotypic tests. Genome-predicted sugar-acid preference (SAP), a glycolytic versus gluconeogenic catabolic preference index, explained over 50% of the variance in observed SAP. Regularized elastic net models linked KEGG genes to specific substrate utilization and sensitivity phenotypes. They gave moderate but reproducible accuracy (AUC 0.70-0.79) for 11 substrates. The authors conclude that specific substrate responses may be predictable from relatively small subsets of KO genes. They describe the work as useful for hypothesis generation. They also note that environmental taxa are underrepresented in genomic databases. The abstract does not describe the validation procedure, so its AUCs cannot be compared directly with held-out-genus results.

The second candidate, [PMID 33622858](https://pubmed.ncbi.nlm.nih.gov/33622858/), is a dynamic genome-scale metabolic model of a Clostridium acetobutylicum/Clostridium ljungdahlii syntrophic coculture. It simulates growth kinetics and metabolite yields when cell fusion is active. It is a simulation study, not a test of binary growth prediction from gene content, so it gives no benchmark for the corpus's AUC values. It is relevant only as an example of the continuous growth-kinetics modeling at which the corpus stops. The corpus finds that growth rate is not predicted by gene content, and that finding is not tested against this paper.

The corpus's findings are consistent with the permafrost study. The permafrost AUCs of 0.70-0.79 for 11 substrates are close to the corpus's class-level AUCs for carbon sources (0.695), amino acids (0.775) and nucleosides (0.780). Both support the view that KO presence/absence carries a moderate, substrate-specific signal. The corpus extends this to a much larger collection: 46,389 pairs, 727 genomes and 4,293 shared KOs. It also reports results by condition class, with each of 106 genera held out in turn. The permafrost paper reports no genus-blocked evaluation, so which test is stricter is not established. The corpus's negative results are new relative to these candidates. Metals (0.605, with a 98% growth rate), antibiotics (0.619) and nitrogen (0.435, worse than random) are weak or uninformative. The permafrost paper does not examine these classes. The comparisons with GapMind pathway rules and with CSP transfer, and the gain from interaction features (mean AUC 0.620 to 0.653), have no counterpart in the candidate set. They rest on the single ENIGMA report.

The permafrost abstract also links GC content and phylum to metabolic strategy. This suggests that phylogenetic structure may help explain some predictability. The corpus's genus-blocked design is aimed at that kind of confound, but it did not test GC content.

## Preliminary comparison of methods

AUC is area under curve. GBDT is gradient boosted decision tree. CSP is carbon source phenotypes.

| Method | AUC | Accuracy | Coverage |
|---|---|---|---|
| ENIGMA-only GBDT, generic KO features (n=7) | 0.633 [src: genotype_to_phenotype_enigma] | not reported [src: genotype_to_phenotype_enigma] | 100% [src: genotype_to_phenotype_enigma] |
| [[entities/gapmind]] pathway completeness, amino acids and carbon | 0.646 [src: genotype_to_phenotype_enigma] | 78.8% [src: genotype_to_phenotype_enigma] | 24.3% [src: genotype_to_phenotype_enigma] |
| CSP-trained KO transfer, matched conditions | 0.800 [src: genotype_to_phenotype_enigma] | 76.8% [src: genotype_to_phenotype_enigma] | 23% [src: genotype_to_phenotype_enigma] |

CSP internal 5-fold evaluation gave AUC 0.858, presented as an achievable ceiling with sufficient data. [src: genotype_to_phenotype_enigma] On 118 testable pairs, GapMind reached 96.5% recall and 79% precision. It almost never misses a grower but sometimes predicts growth when the pathway is present but unused. [src: genotype_to_phenotype_enigma] The report calls GapMind and GBDT complementary: GapMind gives high-confidence pathway-level calls, and GBDT gives broader coverage with lower confidence. [src: genotype_to_phenotype_enigma] It judges CSP transfer supported for matched conditions. [src: genotype_to_phenotype_enigma] For more on pathway rules see [[concepts/reliability-and-coverage-limits-of-gapmind-pathway-predictions]].

About 76% of ENIGMA conditions (metals, antibiotics, nitrogen, stress) have neither GapMind coverage nor CSP training data. [src: genotype_to_phenotype_enigma] On those conditions prediction falls to AUC ~0.63, no better than generic KO features. [src: genotype_to_phenotype_enigma]

## Full-corpus model by condition class

The full model trained on 46,389 pairs (13,632 ENIGMA and 32,757 CSP), 727 genomes and 4,293 shared KOs. Each of 106 genera with at least 50 pairs was held out in turn, and the model trained on all other genera. [src: genotype_to_phenotype_enigma] Overall AUC was 0.620. [src: genotype_to_phenotype_enigma] Class-level results aggregate the holdout predictions. [src: genotype_to_phenotype_enigma]

| Class | AUC | Pairs | Report's reading |
|---|---|---|---|
| Nucleosides | 0.780 [src: genotype_to_phenotype_enigma] | 829 | well-predicted [src: genotype_to_phenotype_enigma] |
| Amino acids | 0.775 [src: genotype_to_phenotype_enigma] | 7,765 | genuinely predictable [src: genotype_to_phenotype_enigma] |
| Carbon sources | 0.695 [src: genotype_to_phenotype_enigma] | 8,965 | moderately predictable [src: genotype_to_phenotype_enigma] |
| Other | 0.654 [src: genotype_to_phenotype_enigma] | 24,590 | mixed [src: genotype_to_phenotype_enigma] |
| Antibiotics | 0.619 [src: genotype_to_phenotype_enigma] | 238 | marginal [src: genotype_to_phenotype_enigma] |
| Metals | 0.605 [src: genotype_to_phenotype_enigma] | 232 | trivially "predicted" because of a 98% growth rate [src: genotype_to_phenotype_enigma] |
| Nitrogen | 0.435 [src: genotype_to_phenotype_enigma] | 152 | worse than random [src: genotype_to_phenotype_enigma] |

The weakest classes are organic acids and nitrogen-cycle compounds. These matter for Oak Ridge contamination chemistry. [src: genotype_to_phenotype_enigma]

## Individual conditions

Of 343 conditions with at least 30 predictions and both growth classes [src: genotype_to_phenotype_enigma], 95 had AUC > 0.75. [src: genotype_to_phenotype_enigma] The best-predicted substrates were tryptophan (AUC 0.933), phenylalanine (0.932), valine (0.927), mannose (0.904) and galactose (0.895). [src: genotype_to_phenotype_enigma] The worst were turanose (0.059) and adonitol (0.010), complex sugars with rare catabolic pathways. [src: genotype_to_phenotype_enigma]

## Interaction features

KEGG-pathway-based KO-by-condition interaction features raised mean AUC from 0.620 to 0.653 (+0.032). [src: genotype_to_phenotype_enigma] They helped 80 of 106 held-out genera. [src: genotype_to_phenotype_enigma] The largest gains were for Microbacterium (+0.088) and Sphingomonas (+0.074). [src: genotype_to_phenotype_enigma] The report reads this as support for matching feature resolution to phenotype resolution (its H1). Binary amino-acid growth is best predicted by condition-specific KOs, whereas growth rate needs bulk features such as CUB that are not yet available. [src: genotype_to_phenotype_enigma]

## Open Directions

- Test whether interaction features lift nitrogen and antibiotic classes, which sit near or below chance. This needs per-class AUC with and without the features.
- Add curated condition-specific pathway annotations for metals, antibiotics and nitrogen, the classes with no GapMind or CSP coverage.
- Rerun the metals class on data with more non-growth labels, since the 98% growth rate makes its AUC uninformative.
- Combine GapMind calls with GBDT scores in one stacked model, and score it on the 118 testable pairs.
- Explain the worst substrates, such as turanose and adonitol, by checking whether the relevant KOs are rare across genomes.
