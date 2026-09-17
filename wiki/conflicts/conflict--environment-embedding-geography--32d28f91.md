<!-- tension-hash: 32d28f91957f3d29 -->
# How strong is the metal–microbiome association when attribution is tested?

Two projects in this corpus report metal–microbiome associations of very different apparent strength, and both attach caveats that cut in the same direction — toward weaker attribution than the headline number implies. One reports a large multivariate association between soil metal concentrations and community function; the other reports a small but phylogenetically controlled per-genus effect that does not survive a stricter data filter. The disagreement is not about whether metals matter but about how much of a reported association survives when the denominator, the threshold, and the correlated structure of metal contamination are made explicit. It matters because the same corpus uses both results to argue that environmental chemistry is embedded in genomic and functional patterns ([[concepts/environment-embedding-geography]]).

## Evidence Sides

**Strong conditional multivariate association, uncertain attribution.** The soil-metal study reports distance-based redundancy analysis (db-RDA — a multivariate ordination that regresses community composition on predictors) with conditional R² = 0.799, p = 0.005, but the unconditional metal-only R² was not reported; chromium, copper, lead, and zinc co-vary, the 60% discovery rate may be inflated by correlated tests, and proximity within 10 km does not guarantee co-location. [src: soil_metal_functional_genomics] The R² is therefore a share of residual, not total, variance, and the discovery rate is a proportion of tests called significant, not an independent replication count.

**Small phylogenetically controlled effect that is threshold-sensitive and null in one stratum.** MicrobeAtlas produced β = +0.021 (a per-unit regression slope), p = 1.5×10⁻⁴, but strict prevalence gave p = 0.092 and groundwater-specific fold enrichment was null (rho = +0.042, p = 0.242). [src: microbeatlas_metal_ecology] Rho here is a rank (Spearman) correlation coefficient. The strict-prevalence result is not a weaker positive: at that threshold the effect is not significant, and the groundwater result is a null.

## Possible Reconciliations

- *Hypothesis:* the two effect sizes are not comparable because they have different denominators — one is variance in community function after conditioning out batch structure, the other is a per-genus slope after removing shared ancestry — so both could be correct without either constraining the other.
- *Hypothesis:* correlated metal co-contamination inflates the apparent breadth of the soil signal while the same correlation is absent or averaged away at genus scale, producing the size gap.
- *Hypothesis:* the effect is real but confined to strata with high metal load, so that permissive filters and non-groundwater habitats retain it while strict prevalence and groundwater do not.

## Resolving Work

- Report the unconditional metal-only db-RDA R² alongside the conditional R² = 0.799 on the same soil samples, to state what share of total community variance metals explain. [src: soil_metal_functional_genomics]
- Refit the COG–metal tests — COG being clusters of orthologous groups, i.e. functional gene categories — under a partial-correlation or joint model that admits chromium/copper/lead/zinc co-variation, and ask whether the 60% discovery rate persists when tests are not treated as independent. [src: soil_metal_functional_genomics]
- Re-run the metal-type predictor across a sweep of prevalence thresholds, reporting β and p at each, to show whether p = 1.5×10⁻⁴ versus p = 0.092 is a filter artefact or a genuine boundary. [src: microbeatlas_metal_ecology]
- Test whether the groundwater null (rho = +0.042, p = 0.242) reflects low power or true absence by comparing habitat-stratified sample counts and effect estimates. [src: microbeatlas_metal_ecology]
- Restrict the soil analysis to samples with genome co-location tighter than 10 km and ask whether the association strengthens, weakens, or holds. [src: soil_metal_functional_genomics]
