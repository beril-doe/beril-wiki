---
type: "Concept"
description: "How method choice (multivariate versus univariate) must match sample size when linking gene presence to metabolite production or consumption in a handful of strains; it stops at growth-phenotype prediction."
sources: ["summaries/genotype_to_phenotype_enigma__REPORT.md", "summaries/webofmicrobes_explorer__REPORT.md"]
---
# Gene-metabolite association discovery in small exometabolomic datasets

In the ENIGMA-linked Web of Microbes (WoM) analysis, a multivariate model failed at six strains. Simple per-metabolite correlations still found many gene-metabolite associations. [src: genotype_to_phenotype_enigma] See [[summaries/genotype_to_phenotype_enigma__REPORT]] and [[entities/web-of-microbes]].

## Multivariate failure at n=6

Exometabolomic prediction on WoM (6 strains, 105 metabolites) fails under multivariate gradient boosted decision trees (GBDT). [src: genotype_to_phenotype_enigma] The GBDT reached an AUC (area under curve) of 0.500 at n=6. [src: genotype_to_phenotype_enigma] The report describes this as a method change needed at small n. [src: genotype_to_phenotype_enigma]

## Univariate per-metabolite correlation

Per-metabolite point-biserial correlation between KO (KEGG ortholog) presence and metabolite production identifies 940 strong associations (|r| > 0.7) across all 62 variable metabolites. [src: genotype_to_phenotype_enigma] The associations split into 454 production and 486 consumption associations. [src: genotype_to_phenotype_enigma] Notebook NB08 records the same result. [src: genotype_to_phenotype_enigma]

Examples of production associations are K01048 PAPS synthase with taurine [src: genotype_to_phenotype_enigma] and K05710 thymidine phosphorylase with thymine. [src: genotype_to_phenotype_enigma] Examples of consumption associations are K02613 lactate permease with lactate [src: genotype_to_phenotype_enigma] and K07334 xanthine oxidase with hypoxanthine. [src: genotype_to_phenotype_enigma]

The feature set has 156 KOs. They have significant rich-media fitness effects in Pseudomonas Fitness Browser (FB) anchor organisms and vary across the 6 WoM strains. [src: genotype_to_phenotype_enigma]

## Relation to growth prediction

The report pairs two regimes. For cross-genus growth prediction (n=46K pairs), multivariate GBDT identifies condition-specific features. For within-genus metabolite prediction (n=6 strains), univariate correlation recovers signal that multivariate models miss. [src: genotype_to_phenotype_enigma] The report concludes that gene content explains both growth and metabolite production when the method suits the sample size and resolution. [src: genotype_to_phenotype_enigma]

The growth-predictive KOs and the metabolite-production KOs are different feature sets (Spearman rho=0.043). [src: genotype_to_phenotype_enigma]

## Caveats

The WoM set of 37 organisms (20 experimental) is too small for statistical analyses across organism groups. [src: webofmicrobes_explorer] See [[concepts/taxonomic-and-single-laboratory-coverage-limits-of-exometabolomic-data]].

## Open Directions

- Run permutation tests on the 940 associations at n=6 to estimate how many |r| > 0.7 hits arise by chance. This would show how many associations are real.
- Check whether associated KOs are confounded with strain phylogeny. This would separate mechanism from relatedness.
- Test the associations on a larger exometabolomic dataset with more strains. This would show whether they hold beyond six strains.
- Compare the 156-KO Fitness Browser-cognate feature set with an unrestricted KO set. This would show what the filter contributes.
