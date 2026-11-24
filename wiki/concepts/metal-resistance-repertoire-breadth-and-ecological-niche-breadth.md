---
type: "Concept"
description: "Whether genera with more diverse metal-resistance gene repertoires occupy broader ecological ranges after phylogenetic control, and which direction of causation the data allow; stops at robustness checks, which have their own pages."
sources: ["summaries/microbeatlas_metal_ecology__REPORT.md"]
---
# Metal resistance repertoire breadth and ecological niche breadth

Genera with more diverse metal-resistance repertoires tend to have broader ecological ranges, even after phylogenetic control. The evidence is one cross-sectional study, microbeatlas_metal_ecology (see [[summaries/microbeatlas_metal_ecology__REPORT]]). It supports a correlation, not a direction of causation. [src: microbeatlas_metal_ecology]

## The association after phylogenetic control

The raw ordinary least squares (OLS) correlation between mean metal type diversity and Levins' B_std is modest (r ≈ 0.21). The report says this reflects baseline phylogenetic structure in both variables. [src: microbeatlas_metal_ecology] See [[entities/levins-niche-breadth]] for the niche-breadth measure and [[entities/phylogenetic-generalized-least-squares]] for the method.

The phylogenetic generalized least squares (PGLS) effect is the extra covariation left after removing shared ancestry, as estimated by the λ-transformed variance-covariance matrix. [src: microbeatlas_metal_ecology] In the simple bacterial model, Levins' B_std against z-scored metal types gave n = 606, λ_PGLS = 0.708, β = +0.021, SE = 0.0056, p = 1.5×10⁻⁴ and ΔAIC = −12.4. This meets Bonferroni significance. [src: microbeatlas_metal_ecology] A Benjamini-Hochberg false discovery rate (BH-FDR) adjustment also left it significant (β = +0.0215, q = 0.003). [src: microbeatlas_metal_ecology]

In the multi-predictor model (λ = 0.706, AIC = −743.67), metal types stayed significant (β = +0.023, SE = 0.0067, p = 5.5×10⁻⁴). [src: microbeatlas_metal_ecology] The BH-FDR q was 0.004. [src: microbeatlas_metal_ecology] The report says the association is robust to genome size, species richness, prevalence filtering, OTU (operational taxonomic unit) abundance filtering and all 13 environment categories. [src: microbeatlas_metal_ecology] Those checks have their own pages.

## Breadth, not depth

Metal type diversity is the only bacterial metal AMR (antimicrobial resistance) predictor that survives Bonferroni correction in the simple PGLS models. [src: microbeatlas_metal_ecology] Other predictors did not reach Bonferroni significance against Levins' B_std:

- AMR clusters: β = +0.010, p = 0.090. [src: microbeatlas_metal_ecology]
- Core fraction: β = +0.003, p = 0.523. [src: microbeatlas_metal_ecology]

In the multi-predictor model, AMR clusters (β = −0.002, p = 0.789) and core fraction (β = +0.006, p = 0.288) were also non-significant. [src: microbeatlas_metal_ecology]

For number of environments as the response, no predictor was Bonferroni-significant:

- Metal types: β = −0.007, p = 0.923. [src: microbeatlas_metal_ecology]
- AMR clusters: β = −0.071, p = 0.290. [src: microbeatlas_metal_ecology]
- Core fraction: β = +0.142, p = 0.038. [src: microbeatlas_metal_ecology]

The report reads this as a link between ecological versatility and the breadth of the repertoire, not its depth (many genes for few metals). [src: microbeatlas_metal_ecology] It says this parallels other stress domains, where breadth of response predicts biogeographic range. [src: microbeatlas_metal_ecology] It also says the PGLS result indicates that HGT-driven (horizontal gene transfer) expansion of metal types covaries with niche breadth beyond phylogenetic relatedness. [src: microbeatlas_metal_ecology] See [[concepts/horizontal-transfer-signatures-of-metal-resistance-genes]].

## Consistency with other studies

Qi et al. (2022) independently found that multiple heavy metal contamination favours microbial generalists as soil network keystones. The report treats this as consistent. [src: microbeatlas_metal_ecology] It also treats the result as consistent with Ma et al. (2025), who reported broader metal tolerance repertoires in coastal-sediment generalists. [src: microbeatlas_metal_ecology] Those site-specific studies could not tell whether total gene burden, core resistance or breadth of metal type coverage was the relevant variable. The report says its global PGLS points to metal type diversity. [src: microbeatlas_metal_ecology] The report claims this is the first PGLS-controlled link between genus-level metal type diversity and global niche breadth. [src: microbeatlas_metal_ecology] See [[entities/microbeatlas]] and [[concepts/phylogenetic-confounding-of-environment-amr-associations]].

## What direction of causation the data allow

The data allow no direction. The cross-sectional comparison of genera, using observational global survey data, cannot establish the direction. [src: microbeatlas_metal_ecology] Genome-size adjustment does not change this: the association stays correlational. [src: microbeatlas_metal_ecology] The report states that its PGLS coefficient is a partial correlation, not a causal estimate. [src: microbeatlas_metal_ecology] It also states that the coefficient reflects covariation of inferred niche breadth and inferred metal tolerance capacity, not confirmed physiology. [src: microbeatlas_metal_ecology] The report says it directly addressed three scenarios, none distinguishable, and removed causal phrasing from its Key Findings and Interpretation. [src: microbeatlas_metal_ecology] It names two ways to tell them apart: time-series genomic data tracking metal resistance alongside range shifts, or longitudinal metal-enrichment experiments in defined microbial communities. [src: microbeatlas_metal_ecology]

The three scenarios are:

1. Metal tolerance enables habitat expansion, because taxa with diverse resistance can colonise chemically diverse environments. [src: microbeatlas_metal_ecology]
2. Ecological generalism enables gene acquisition, because broad-niche genera meet more environments, HGT donors and metal concentrations. [src: microbeatlas_metal_ecology]
3. A shared driver, such as genome size, metabolic versatility or biofilm capacity, promotes both broad niches and diverse tolerance. [src: microbeatlas_metal_ecology]

The report says one result slightly favours scenario 1 or 3 over a genome-size-only driver. Total AMR cluster count is non-significant while metal type diversity is significant. A sole genome-size driver would predict that cluster count is also significant, because it scales more directly with genome size. [src: microbeatlas_metal_ecology]

The report also offers a metabolic versatility hypothesis. It links diverse repertoires, such as Hg detoxification, As efflux and Cu oxidation, to broader ranges. [src: microbeatlas_metal_ecology] It suggests that broad metal tolerance may proxy overall environmental tolerance. Multi-metal-stress environments are also chemically complex in redox gradients, salinity and organic carbon variation. [src: microbeatlas_metal_ecology]

## Tensions

- The report asserts that the HGT-labile diversity component is what covaries with ecological range. [src: microbeatlas_metal_ecology] The same report says direction cannot be established. [src: microbeatlas_metal_ecology] The first statement is a stronger reading than the design supports.
- The report claims novelty for its phylogenetic partitioning of core versus type diversity. [src: microbeatlas_metal_ecology] That is a claim by the report and has not been checked against other work.

## Open Directions

- Use time-series genomic data that track metal resistance evolution alongside range shifts. This would test whether repertoire expansion precedes or follows range expansion.
- Run longitudinal metal-enrichment experiments on defined communities. This would separate scenario 1 from scenario 2.
- Add candidate shared drivers (metabolic versatility, biofilm capacity) as covariates beyond genome size. This would test scenario 3.
- Validate the inferred metal tolerance against measured physiology in a subset of genera. This would close the gap noted in the caveat on inferred traits.
