---
type: "Compound"
description: "Carbon-source substrate linked to demanding growth and respiratory-chain requirements."
sources: ["summaries/adp1_deletion_phenotypes__REPORT.md", "summaries/aromatic_catabolism_network__REPORT.md", "summaries/respiratory_chain_wiring__REPORT.md"]
---
# Acetate

## What this entity is

**Canonical name:** Acetate. [src: adp1_deletion_phenotypes]

**Known aliases:** No additional aliases are reported in this document. [src: adp1_deletion_phenotypes]

**Stable external identifier:** None is reported in this document. [src: adp1_deletion_phenotypes]

## Key facts

Acetate was one of the 8 carbon sources tested in the *Acinetobacter baylyi* ADP1 deletion-collection growth matrix, which measured 2,034 genes. [src: adp1_deletion_phenotypes]

Acetate belongs to the demanding condition tier, together with urea and butanediol; these conditions had mean growth ratios of 0.41–0.65 and 95–100% of genes showing defects at a growth ratio below 0.8. [src: adp1_deletion_phenotypes] Growth ratios were calculated as mutant/wild-type values, with values below 1.0 indicating growth defects. [src: adp1_deletion_phenotypes]

Among the 28 condition pairs, acetate–butanediol had the highest Pearson correlation, at **r = 0.58**, indicating that these two demanding conditions shared the strongest measured association in the matrix. [src: adp1_deletion_phenotypes]

Acetate-specific genes included **fadB**, malate synthase G, and **citB**, mapping acetate utilization to fatty acid β-oxidation and the [[entities/glyoxylate-shunt]]. [src: adp1_deletion_phenotypes] The acetate-associated phenotype therefore contributes to the report’s broader finding that gene importance varies continuously with the growth condition rather than being fully captured by binary essentiality labels. [src: adp1_deletion_phenotypes]

The aromatic-catabolism analysis **refines** acetate’s role as a demanding comparison condition: acetate produced the largest reported Complex I fitness defect relative to background, **-1.55**, and is interpreted as a non-aromatic substrate that generates high NADH flux through the TCA cycle. [src: aromatic_catabolism_network] This result **supports** the hypothesis that Complex I dependence tracks NADH-generating substrate use rather than aromatic catabolism alone; across the transferred dataset, Complex I orthologs had mean fitness values of **-1.35** on aromatic conditions versus **-0.77** on comparison conditions, with Mann-Whitney **p < 0.0001**. [src: aromatic_catabolism_network]

The respiratory-chain analysis further **refines** this interpretation: acetate requires Complex I, cytochrome bo3, ACIAD3522, and additional respiratory components, with no listed component dispensable in the reported profile. [src: respiratory_chain_wiring] Acetate generated 3 NADH, or 1.50 NADH per carbon, with production assigned to the TCA cycle; Complex I had a growth ratio of 0.49, while ACIAD3522 had a growth ratio of 0.013 and was described as lethal in this condition. [src: respiratory_chain_wiring] These findings **support** a condition-specific respiratory configuration driven by NADH flux and capacity constraints, while the theoretical stoichiometry does not constitute a measured flux distribution. [src: respiratory_chain_wiring]

## Related pages

The acetate findings feed into [[concepts/condition-specific-fitness]] because they quantify carbon-source-dependent growth requirements and refine the distinction between demanding-condition phenotypes and high-NADH-flux respiratory dependence. [src: adp1_deletion_phenotypes, aromatic_catabolism_network, respiratory_chain_wiring]

They also refine [[concepts/gene-essentiality]] by showing that deletion effects depend on the tested condition. [src: adp1_deletion_phenotypes]

The respiratory result supports [[concepts/metabolic-model-gapfilling]] because growth-optimized FBA routes NADH through the ATP-favorable pathway and can miss alternative condition-specific respiratory requirements. [src: respiratory_chain_wiring]

The complete deletion-phenotype analysis is summarized in [[summaries/adp1_deletion_phenotypes__REPORT]]. [src: adp1_deletion_phenotypes]

The aromatic respiratory interpretation is detailed in [[summaries/aromatic_catabolism_network__REPORT]]. [src: aromatic_catabolism_network]

The condition-specific respiratory-chain analysis is detailed in [[summaries/respiratory_chain_wiring__REPORT]]. [src: respiratory_chain_wiring]
