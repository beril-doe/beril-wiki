---
type: "Concept"
description: "Why metal cofactor-biosynthesis genes track niche breadth like housekeeping genes while resistance, regulatory and non-metal transporter gene sets show null associations; covers true-negative categories, split-magnitude permutations and jackknives."
sources: ["summaries/comprehensive_metal_ecology__REPORT.md"]
---
# Constitutive versus inducible gene classes in niche-breadth associations

Cofactor-biosynthesis genes track prokaryotic niche breadth as strongly as housekeeping genes, while resistance genes and several non-metal gene sets show no association. [src: comprehensive_metal_ecology] The cofactor and resistance results come from the report's global MGnify metagenome-assembled genome (MAG) niche-breadth analysis, and the report adds permutation and jackknife checks. [src: comprehensive_metal_ecology] The cofactor result rests on only 7 KEGG orthologs (KOs). [src: comprehensive_metal_ecology] The added evidence supports the split with a permutation test, a jackknife and per-metal results, and it adds sub-category nulls for two-component systems and ABC transporters. See [[summaries/comprehensive_metal_ecology__REPORT]] for the whole report.

## The constitutive end: cofactor biosynthesis

Cofactor biosynthesis (7 KOs, Fe–S cluster and molybdopterin) shows the strongest metal-gene signal, β = −0.033 with false discovery rate (FDR) p = 5.2×10⁻⁹. [src: comprehensive_metal_ecology] It is the largest metal functional-category effect. [src: comprehensive_metal_ecology] It equals the housekeeping streamlining baseline. [src: comprehensive_metal_ecology] The category is anchored by Fe–S cluster assembly, molybdopterin synthesis and cobalamin pathway genes. The report describes these as constitutively required where core metabolism depends on metal cofactors, such as nitrogen fixation, anaerobic respiration and methanogenesis. [src: comprehensive_metal_ecology] It links the signal to Fe–S cluster assembly being one of the most conserved, vertically inherited gene sets in prokaryotes. [src: comprehensive_metal_ecology] See also [[entities/iron-sulfur-cluster-biogenesis]]. No cofactor KO appears in the double-signal KO set, which the report reads as consistent with constitutive requirement and vertical inheritance. [src: comprehensive_metal_ecology]

Other categories in the global MGnify MAG analysis are also significant and negative:
- Transport/Homeostasis (213 KOs): β = −0.022, FDR p = 2.8×10⁻⁵. [src: comprehensive_metal_ecology]
- Metal-dependent Metabolism (54 KOs): β = −0.021, FDR p = 1.2×10⁻⁴. [src: comprehensive_metal_ecology]
- Sensing/Regulation (48 KOs): β = −0.018, FDR p = 9.1×10⁻⁴. [src: comprehensive_metal_ecology]

Among ABC transporters, Lipid/LPS (lipopolysaccharide) export is the only significantly negative subcategory (16 KOs, β = −0.030, q = 3.3×10⁻⁵). It is comparable to the metal cofactor signal, and the report interprets it as likely constitutive outer-membrane lipid maintenance. [src: comprehensive_metal_ecology]

## The inducible end: resistance genes

Resistance/detoxification genes (106 KOs) show no association (β ≈ 0, p = 0.66). [src: comprehensive_metal_ecology] The report classes them as a near-null category sharing the character of the true-negative categories. [src: comprehensive_metal_ecology] The MAG table gives β = +0.003, SE (standard error) = 0.006, FDR p = 0.656. [src: comprehensive_metal_ecology] The report places them among the five confirmed true-negative categories. It describes these as variable, inducible, horizontal gene transfer (HGT)-mobile gene sets with no constitutive coupling to genome size. [src: comprehensive_metal_ecology] It argues that HGT decouples resistance gene content from ecological specialisation and from vertical inheritance. [src: comprehensive_metal_ecology] The null is precise rather than intermediate, because these genes lie among the true negatives and not between the streamlining baseline and the null. [src: comprehensive_metal_ecology] All 13 double-signal KOs are resistance, transport or sensing genes, which matches this null. [src: comprehensive_metal_ecology]

The resistance null has a limit. Its confidence intervals do not exclude small effects, so the report reads it as absence of a substantial phylogenetically conserved association. [src: comprehensive_metal_ecology] The report interprets the resistance-null/constitutive-significant contrast as specific to metal genes. In its view the contrast needs constitutive metabolic coupling to the predictor category, which inducible resistance and regulatory gene sets lack. [src: comprehensive_metal_ecology]

## True-negative categories

Five non-metal categories serve as true-negative controls (NB18, the report's functional-landscape analysis). All have |β| < 0.006 and q > 0.45. [src: comprehensive_metal_ecology] The report treats them as confirmed controls for the specificity of the metal-gene signal. [src: comprehensive_metal_ecology] Standalone phylogenetic generalized least squares (PGLS) results against niche breadth are given for each category in the table. [src: comprehensive_metal_ecology] The NB18 table characterises each one as follows. [src: comprehensive_metal_ecology]

| Category | KOs | Genera | β | q (NB18) | NB18 character |
|---|---|---|---|---|---|
| ABC (ATP-binding cassette) transporters, non-metal | 475 | 1,073 | −0.00546 | 0.457 [src: comprehensive_metal_ecology] | Inducible; substrate-specific [src: comprehensive_metal_ecology] |
| Antimicrobial resistance (AMR), beta-lactam | 112 | 1,073 | −0.00387 | 0.505 [src: comprehensive_metal_ecology] | HGT-mobile; condition-acquired [src: comprehensive_metal_ecology] |
| Glycan biosynthesis (peptidoglycan) | 73 | 1,050 | +0.00119 | 0.767 [src: comprehensive_metal_ecology] | Near-universal; niche-independent [src: comprehensive_metal_ecology] |
| Cell motility | 153 | 1,063 | +0.00397 | 0.505 [src: comprehensive_metal_ecology] | Environment-dependent expression [src: comprehensive_metal_ecology] |
| Two-component systems | 521 | 1,073 | +0.00592 | 0.457 [src: comprehensive_metal_ecology] | Inducible regulatory network [src: comprehensive_metal_ecology] |

A standalone rerun matched the NB18 results exactly, with all five non-significant (p > 0.36). [src: comprehensive_metal_ecology]

Sub-functional resolution refines this picture:
- All AMR and two-component-system subcategories are positive, which the report describes as inducible/HGT character. [src: comprehensive_metal_ecology]
- Efflux pumps are significantly positive (β = +0.018, q = 0.016). Enzymatic inactivation (β = +0.006, q = 0.21) and target modification (β = +0.009, q = 0.19) are positive but non-significant. [src: comprehensive_metal_ecology] See also [[entities/efflux-pumps]].
- Two-component sensor kinases are positive but non-significant (β = +0.008, q = 0.25). [src: comprehensive_metal_ecology]
- Two-component response regulators (β = +0.009, q = 0.25) and phosphotransfer proteins (β = +0.003, q = 0.68) are likewise positive and non-significant, in an exploratory analysis. [src: comprehensive_metal_ecology]
- All ABC substrates other than Lipid/LPS export are near-zero or positive (q > 0.25). [src: comprehensive_metal_ecology]

## Split magnitude, permutations and jackknife

The distinctive feature of the metal-gene set is its internal functional split, not its overall β. Resistance has β ≈ 0 and cofactor biosynthesis has β = −0.033. [src: comprehensive_metal_ecology] The report calls this split distinctive to metal genes and says the contrast is not a general feature of heterogeneous gene categories. [src: comprehensive_metal_ecology]

- **Permutation (NB25).** The exploratory test randomly partitioned the 140-KO metal set 1,000 times into groups of 106 and 7, matching the resistance and cofactor group sizes. [src: comprehensive_metal_ecology] The observed Δβ = 0.035259 exceeded all 1,000 null splits (p < 0.001; 0/1,000 permutations exceeded). The null median was −0.006 and the SD (standard deviation) was 0.007, so the observed split sat about 6 SD above the null. [src: comprehensive_metal_ecology] The report concludes the contrast is not an artefact of unequal group sizes or sampling variance. [src: comprehensive_metal_ecology]
- **Comparison families.** ABC transporters have Δβ = 0.032 (Lipid/LPS versus all others), AMR 0.012 and TCS (two-component systems) 0.006. All are smaller than the metal set's Δβ = 0.035. [src: comprehensive_metal_ecology] The NB25 summary gives comparison families Δβ < 0.033. [src: comprehensive_metal_ecology]
- **Replication.** The contrast (Δβ ≈ 0.036 across five functional subcategories) is not replicated in AMR, TCS or ABC transporters at the same resolution (NB19). Their subcategories share the same directional character. [src: comprehensive_metal_ecology]
- **Jackknife (NB26).** Three of the seven cofactor KOs were absent from the MGnify MAG dataset and contributed zero density, so the exploratory jackknife used only the four detectable KOs. [src: comprehensive_metal_ecology] Leave-one-KO-out on those 4 assignable KOs (K01772, K02225, K03635, K22225) kept every remainder significant, with β from −0.016 to −0.029, all p < 0.001 and no sign changes. [src: comprehensive_metal_ecology] Excluding K01772 gave β = −0.016 (SE = 0.00441, p = 0.000222). [src: comprehensive_metal_ecology] Excluding K02225 gave β = −0.027 (SE = 0.00444, p = 1.4×10⁻⁹). [src: comprehensive_metal_ecology] Excluding K03635 gave β = −0.029 (SE = 0.00443, p = 1.3×10⁻¹⁰). [src: comprehensive_metal_ecology] Excluding K22225 gave β = −0.028 (SE = 0.00478, p = 8.2×10⁻⁹). [src: comprehensive_metal_ecology] No single KO drives the association; the report says the signal is distributed across the Fe–S cluster, molybdopterin and cobalamin pathway. [src: comprehensive_metal_ecology]

The report concludes that metal-cofactor dependence, not stress-response capacity, is the mechanistic driver most consistent with these patterns. [src: comprehensive_metal_ecology] The report also proposes a causal-pathway test: regress niche breadth on cofactor density while controlling for overall primary-set density, and use a partial R² test to separate a cofactor-driven association from collinearity with broader metal-gene investment. [src: comprehensive_metal_ecology] The metal-gene effect is also uniform across 9 chemically diverse metals, all FDR-significant. [src: comprehensive_metal_ecology] Related: [[concepts/single-metal-dominance-versus-distributed-metal-type-diversity-effects]].

### Per-metal sets

Each metal-specific KO set has a significant negative association with niche breadth (BH-FDR, Benjamini-Hochberg FDR). [src: comprehensive_metal_ecology]

| Metal | KOs | β | BH-FDR p |
|---|---|---|---|
| Tl | 45 | −0.027 | 1.1×10⁻⁸ [src: comprehensive_metal_ecology] |
| Fe | 98 | −0.025 | 1.2×10⁻⁷ [src: comprehensive_metal_ecology] |
| Ni | 84 | −0.025 | 1.9×10⁻⁷ [src: comprehensive_metal_ecology] |
| Zn | 67 | −0.023 | 1.1×10⁻⁶ [src: comprehensive_metal_ecology] |
| Al | 34 | −0.023 | 8.8×10⁻⁶ [src: comprehensive_metal_ecology] |
| Co | 101 | −0.022 | 3.9×10⁻⁶ [src: comprehensive_metal_ecology] |
| S | 74 | −0.021 | 4.9×10⁻⁵ [src: comprehensive_metal_ecology] |
| Cu | 71 | −0.019 | 7.7×10⁻⁵ [src: comprehensive_metal_ecology] |
| Mn | 34 | −0.017 | 3.8×10⁻⁴ [src: comprehensive_metal_ecology] |

The report argues that this uniformity across chemically diverse metals argues against any single element driving the signal. [src: comprehensive_metal_ecology]

## Open Directions

- Expand the cofactor set beyond 7 KOs (only 4 assignable in the jackknife), then rerun the association test and the leave-one-out test. This would show whether the signal generalises beyond Fe–S, molybdopterin and cobalamin genes.
- Run the partial R² regression of niche breadth on cofactor density, controlling for primary-set density, to settle collinearity with broader metal-gene investment.
- Test whether the HGT-decoupling explanation holds by comparing resistance KOs on mobile elements with chromosomal ones against niche breadth.
- Apply the split-magnitude permutation to further non-metal families, so the largest-split claim rests on more than three comparators.
- Probe why efflux pumps are significantly positive while other AMR subcategories are not, using finer subcategory models.
