---
type: "Concept"
description: "Separating pleiotropic biosynthesis genes that matter in every minimal-medium condition from genes specific to one carbon or nitrogen source in fitness screens."
sources: ["summaries/fw300_metabolic_consistency__REPORT.md"]
---
# Housekeeping versus substrate-specific fitness genes

Fitness Browser (FB) screens of FW300-N2E3 mix two kinds of genes. The top 18 genes, all amino acid biosynthesis enzymes, were significant in all 21 metabolite conditions. The report interprets them as essential for growth on any minimal medium. [src: fw300_metabolic_consistency] A smaller set of about 370 genes was significant in only one or two conditions and is called substrate-specific. [src: fw300_metabolic_consistency] The evidence is one report on one organism, so treat it as a worked example. See [[entities/pseudomonas-fluorescens-fw300-n2e3]] and [[summaries/fw300_metabolic_consistency__REPORT]].

## The screen and its scale

Across 21 Web of Microbes (WoM) metabolites with matching [[entities/fitness-browser]] experiments, FW300-N2E3 showed significant fitness effects (|fit| > 1, |t| > 4) for 601 unique genes. [src: fw300_metabolic_consistency] Those genes made up 4,764 significant gene-condition hits. [src: fw300_metabolic_consistency] The most genetically complex metabolisms were carnitine (283 genes), alanine (295 genes across D/L forms), arginine (270 genes), and tryptophan (231 genes). [src: fw300_metabolic_consistency]

## Housekeeping genes

In FW300-N2E3, 231 genes were significant in 3 or more metabolite conditions. [src: fw300_metabolic_consistency] The top 18 genes were significant in all 21 conditions. They are amino acid biosynthesis enzymes, such as homoserine O-acetyltransferase (methionine), ATP (adenosine triphosphate) phosphoribosyltransferase (histidine), dihydroxy-acid dehydratase (branched-chain amino acids), isopropylmalate dehydrogenase (leucine), shikimate dehydrogenase (aromatic amino acids) and imidazoleglycerol-phosphate dehydratase (histidine). [src: fw300_metabolic_consistency] The report says these genes are significant everywhere because they are essential amino acid biosynthesis genes, not substrate-specific catabolism genes. [src: fw300_metabolic_consistency] It interprets them as essential for growth on any minimal medium, so they reflect "housekeeping fitness" and not substrate-specific metabolism. [src: fw300_metabolic_consistency]

## Substrate-specific genes

About 370 genes were significant in only 1–2 conditions. The report calls these the truly substrate-specific genes. Examples are carnitine-specific transporters, lactate dehydrogenases and trehalose-specific phosphotransferases. [src: fw300_metabolic_consistency]

## Direction of the effect

The report splits significant genes by WoM action. Emerged metabolites are produced de novo. Increased metabolites are already present but amplified. [src: fw300_metabolic_consistency]

| WoM action | N metabolites | Mean sig genes | Mean detrimental | Mean beneficial |
|---|---|---|---|---|
| Emerged | 7 | 184.4 +/- 115.5 | 221.0 | 21.0 [src: fw300_metabolic_consistency] |
| Increased | 14 | 163.5 +/- 74.1 | 206.5 | 12.8 [src: fw300_metabolic_consistency] |

Emerged metabolites had slightly more fitness-important genes than Increased ones, but the variance was high. [src: fw300_metabolic_consistency] The report describes both categories as having detrimental:beneficial ratios of about 10:1. It reads this as most fitness-significant genes being required for growth on these substrates, not inhibitory. [src: fw300_metabolic_consistency]

## Caveat

The fitness signal contains both housekeeping and substrate-specific components. The report recommends separating them in future WoM–FB integration. [src: fw300_metabolic_consistency]

## Open Directions

- Remove the genes significant in 3 or more conditions, then recount genes per metabolite. This would show how much of the carnitine, alanine, arginine and tryptophan complexity is housekeeping. [[concepts/condition-specific-gene-phenotypes-and-functional-annotation-yield]] covers the related annotation question.
- Repeat the 1–2 versus 3+ condition split in other organisms in the Fitness Browser. This would test whether the split generalizes beyond FW300-N2E3.
- Compare WoM Emerged and Increased metabolites using only substrate-specific genes. This could clarify the slight, high-variance difference. See also [[concepts/condition-specific-fitness-correlation-across-carbon-sources]].
