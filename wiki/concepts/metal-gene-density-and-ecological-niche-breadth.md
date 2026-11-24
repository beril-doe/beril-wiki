---
type: "Concept"
description: "Whether per-megabase density of metal-processing genes predicts how broad a genus's habitat range is, across domains, datasets and sensitivity analyses; stops at mechanism and at the streamlining baseline discussed elsewhere."
sources: ["summaries/comprehensive_metal_ecology__REPORT.md"]
---
# Metal-gene density and ecological niche breadth

Across 1,574 bacterial genera, genera with a higher per-megabase density of metal-processing genes tend to have narrower habitat ranges. The result is a single report's finding (comprehensive_metal_ecology; see [[summaries/comprehensive_metal_ecology__REPORT]]). It holds under most sensitivity checks. The archaeal test and the Australia-only test were not significant: the archaeal one was directionally consistent, and the Australia-only one was near zero. The effect is small. [src: comprehensive_metal_ecology]

## The primary bacterial result

Per-Mb Tier 1+2 metal-gene KO (KEGG ortholog) density was negatively associated with standardised Levins' niche breadth in 1,574 genera matched across [[entities/gtdb]] and global MGnify MAG (metagenome assembled genomes) data. The fit gave β = −0.021, SE = 0.0037, t = −5.63, p = 2.1×10⁻⁸, FDR (false discovery rate) joint p = 6.4×10⁻⁸, Pagel's λ = 0.757 and r² = 0.046. [src: comprehensive_metal_ecology] The set had 140 KOs, and the result survived correction for genome size, GC content, isolation source and dominant biome. [src: comprehensive_metal_ecology] The report states that its pre-registered hypothesis H1 (β < 0) is confirmed. [src: comprehensive_metal_ecology] The model was a PGLS (phylogenetic generalized least squares) fit ([[entities/phylogenetic-generalized-least-squares]]). [src: comprehensive_metal_ecology] The report reads the moderate λ as showing that shared ancestry explains the relationship only partly. [src: comprehensive_metal_ecology] See [[concepts/phylogenetic-signal-of-gene-content-and-traits]] for the wider context.

The effect is small. Metal-gene density explains a small fraction of genus-level niche-breadth variance, and the report says ecological breadth is multidimensionally determined. [src: comprehensive_metal_ecology]

## Sensitivity analyses

Most checks keep the negative sign and often strengthen it. The report states that 6 of 7 of its 8 pre-specified sensitivity analyses directionally confirm H1, with all β < 0 and 5 significant at p < 0.05. [src: comprehensive_metal_ecology] The p-values are raw, with one test per check and no within-family multiplicity correction. [src: comprehensive_metal_ecology]

| Check | β | raw p |
|---|---|---|
| Primary Tier 1+2 (140 KOs, 1,574 genera) | −0.021 | 2.1×10⁻⁸ [src: comprehensive_metal_ecology] |
| All non-ambiguous KOs (444 KOs, 1,073 genera) | −0.027 | 5.0×10⁻⁸ [src: comprehensive_metal_ecology] |
| BacMet-only (188 KOs, 1,073 genera) | −0.011 | 0.050, borderline [src: comprehensive_metal_ecology] |
| λ = 0 (OLS, ordinary least squares) | −0.032 | ≈0 [src: comprehensive_metal_ecology] |
| λ = 1 (Brownian) | −0.018 | 3.7×10⁻⁶ [src: comprehensive_metal_ecology] |
| Min n = 50 / 150 | −0.021 | 2.1×10⁻⁸, identical [src: comprehensive_metal_ecology] |
| Raw Levins' B | −0.286 | 1.1×10⁻¹¹ [src: comprehensive_metal_ecology] |
| Northern hemisphere | −0.030 | 3.2×10⁻⁶ [src: comprehensive_metal_ecology] |
| Soil-restricted | −0.033 | 0.007 [src: comprehensive_metal_ecology] |
| Archaea, min n = 5 | −0.018 | 0.084, underpowered [src: comprehensive_metal_ecology] |
| Australia only | −0.002 | 0.755, null [src: comprehensive_metal_ecology] |

The report takes the λ = 0 and λ = 1 results as showing the signal does not depend on one phylogenetic correction assumption. [src: comprehensive_metal_ecology] It describes the signal as stronger in northern hemisphere genera and in soil specialists. [src: comprehensive_metal_ecology]

## Tests that did not reach significance

The archaeal test (95 genera, GTDB archaeal tree) gave β = −0.014, SE = 0.0087, raw p = 0.119, joint-FDR p = 0.178. It is not significant but is directionally consistent with the bacterial result. [src: comprehensive_metal_ecology] The report suggests low power combined with a small effect size as the likely reason. [src: comprehensive_metal_ecology]

The Australia-only NGSA test (n = 482, λ = 0.346) is near zero, with β = −0.002 and p = 0.755. [src: comprehensive_metal_ecology] The report says this lowers confidence in the universality of the soil-concentration predictor. [src: comprehensive_metal_ecology]

An ENIGMA FRC within-site analysis ([[entities/enigma]]) of 29 MAGs from 3 wells gave burden ρ = −0.41 (p = 0.029). It is classified as uninformative because of a data coverage failure. [src: comprehensive_metal_ecology]

The culture-based geographic niche-breadth replication using [[entities/bacdive]] (NB09) is still pending execution. [src: comprehensive_metal_ecology]

## Status of the evidence

Findings 1–8 and 10–11 were fully pre-specified, with directional hypotheses and decision rules set before data inspection. [src: comprehensive_metal_ecology] Finding 9 and the exploratory analyses NB17–NB24 were designed after the P1 result was seen. They inform mechanism only and cannot change the H1 classification. [src: comprehensive_metal_ecology]

An exploratory inverse PGLS (NB27) reversed the direction. It found that niche-range breadth positively predicts per-Mb metal-gene density (n_biomes: β = 0.215, p ≈ 0). The report says this needs confirmatory pre-registration before further inference. [src: comprehensive_metal_ecology]

The report's systematic literature search found no earlier paper that correlates per-Mb metal-gene KO density across prokaryotic genera with standardised Levins' B using phylogenetically controlled analysis. [src: comprehensive_metal_ecology] It presents this as a cross-genus relationship, unlike earlier work on contaminated sites or within-species strains. [src: comprehensive_metal_ecology]

## Open Directions

- Finish the pending BacDive culture-based niche-breadth replication, to give an independent breadth measure.
- Increase archaeal sample size beyond n = 95 and run a power analysis, to test whether the non-significant β = −0.014 reflects low power or a true absence of effect.
- Pre-register and run the inverse PGLS (niche breadth predicting metal-gene density), to settle the direction of the association.
- Repeat the Australia-only test with a different breadth definition, to see why NGSA is near zero while Northern hemisphere and soil subsets are stronger.
- Obtain ENIGMA data with more than 3 wells, so the within-site analysis can say something.
