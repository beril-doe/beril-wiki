---
type: "Concept"
description: "Short-term stability preserves persistent spatial structure in groundwater communities"
sources: ["summaries/enigma_sso_asv_ecology__REPORT.md"]
---
# Persistent spatial structure despite short-term groundwater community stability

## Scope and interpretation

This concept describes the coexistence of strong well-specific spatial structure with minimal community change over a 9-day groundwater sampling interval at the SSO subsurface site. [src: enigma_sso_asv_ecology] The evidence supports [[concepts/subsurface-hydrogeological-zonation]] and refines [[concepts/groundwater-sediment-community-partitioning]] by showing that spatial differences can persist even when short-term temporal turnover is low. [src: enigma_sso_asv_ecology]

The result should be interpreted as short-term persistence, not long-term ecological stability, because the groundwater comparison covered only 9 days and did not resolve seasonal or longer plume dynamics. [src: enigma_sso_asv_ecology]

## Evidence for persistent spatial structure

Groundwater communities from 5 wells sampled on September 9 and September 18, 2024 showed that well identity explained 49.9% of community variance, with p = 0.001. [src: enigma_sso_asv_ecology] Filter size explained 10.1% of variance, with p = 0.001, whereas depth within the saturated zone explained 2.5%, with p = 0.430, and sampling date explained 0.8%, with p = 0.998. [src: enigma_sso_asv_ecology]

The median Bray–Curtis dissimilarity, a measure of compositional difference based on taxon abundances, was 0.917 between spatial samples, compared with 0.351 between temporal samples and 0.750 between filter sizes. [src: enigma_sso_asv_ecology] This **supports** the interpretation that spatial separation contributed more community variation than the 9-day interval, although filter size was also a substantial source of variation. [src: enigma_sso_asv_ecology]

A Mantel test, which correlates distance matrices, found that the date-1 and date-2 distance matrices had Spearman ρ = 0.867 and p = 0.001. [src: enigma_sso_asv_ecology] This **supports** preservation of the well-to-well similarity ranking across the 9-day interval rather than random short-term rearrangement of groundwater communities. [src: enigma_sso_asv_ecology]

## Relation to sediment spatial structure

The sediment dataset contained 37 core samples aggregated across 9 wells arranged in a 3×3 grid spanning approximately 6 m. [src: enigma_sso_asv_ecology] Sediment communities also showed spatial distance-decay, with a Mantel Spearman ρ = 0.323, p = 0.029, and 9,999 permutations. [src: enigma_sso_asv_ecology]

Hydrogeological zone explained 27.5% of sediment community variance, with F = 4.05 and p = 0.0001, whereas well identity explained 19.2% and was not significant, with F = 0.80 and p = 0.979. [src: enigma_sso_asv_ecology] Samples from the same well but different depths had median Bray–Curtis dissimilarity = 0.977, while samples from the same depth zone in different wells had median Bray–Curtis dissimilarity = 0.835. [src: enigma_sso_asv_ecology]

The groundwater and sediment results therefore **support** a broader spatial-structure model in which location, hydrogeological position, and sampling configuration shape observed community differences, but they do not establish that the same mechanism operates in both materials. [src: enigma_sso_asv_ecology] The sediment cores were collected once per well during February–March 2023, whereas groundwater was sampled in September 2024, creating an 18-month material-and-time offset that prevents a direct temporal comparison between the two datasets. [src: enigma_sso_asv_ecology]

## What the stability result does and does not show

The 9-day result **supports** short-term persistence of spatial community organization, but it does not demonstrate stability across seasons, long-term plume fluctuations, or repeated sediment sampling. [src: enigma_sso_asv_ecology] It also does not show that the inferred contamination-plume explanation is correct, because direct SSO geochemistry was unavailable in the analyzed dataset. [src: enigma_sso_asv_ecology]

The report registered 221 geochemistry sample tubes in CORAL, but metals, ion chromatography/total organic carbon, isotopes, ammonia, and nitrite measurements had not been loaded. [src: enigma_sso_asv_ecology] Consequently, persistent spatial structure is an observed community pattern, whereas the proposed northeast-to-southwest plume mechanism remains a testable hypothesis. [src: enigma_sso_asv_ecology]

Groundwater ASV coverage was available for only 5 of 9 wells and excluded the inferred hotspot wells M5 and U3. [src: enigma_sso_asv_ecology] This **limits** the strength of any conclusion about plume persistence because the missing wells include locations central to the proposed spatial interpretation. [src: enigma_sso_asv_ecology]

## Tensions

The data show strong spatial structure and high similarity of spatial rankings between dates, but the sampling design cannot distinguish persistent environmental forcing from stable well-specific properties, filter effects, or other sampling effects. [src: enigma_sso_asv_ecology] This tension is unresolved because filter size explained 10.1% of variance, while date explained 0.8%, and the study did not provide repeated seasonal sampling or direct geochemistry. [src: enigma_sso_asv_ecology]

The sediment analysis suggests that hydrogeological zone can dominate well identity, whereas the groundwater analysis found well identity explaining 49.9% of variance and depth within the saturated zone explaining 2.5% with p = 0.430. [src: enigma_sso_asv_ecology] These results are not directly contradictory because the datasets differ in material, sampling period, and depth structure, but they **indicate** that the relative importance of spatial variables may be sample-type dependent. [src: enigma_sso_asv_ecology]

## Open Directions

- Load the 221 registered SSO geochemistry samples into CORAL and use spatial gradient analysis to test whether nitrate, pH, and metal concentrations follow the predicted northeast-to-southwest community pattern. [src: enigma_sso_asv_ecology]
- Add groundwater ASVs from the available Brick 460-462 pump-test data and compare M5, L8, and U2 with the existing wells to test whether the predicted *Rhodanobacter* maximum occurs at M5. [src: enigma_sso_asv_ecology]
- Repeat groundwater 16S sampling across seasons and apply variance partitioning to ask whether well identity continues to dominate date and seasonal effects. [src: enigma_sso_asv_ecology]
- Collect sediment and groundwater contemporaneously and use paired within-well Bray–Curtis comparisons to determine whether their separation reflects material-specific communities or the existing 18-month sampling offset. [src: enigma_sso_asv_ecology]
- Standardize filter size and apply PERMANOVA with filter, well, depth, and date terms to determine how much of the apparent spatial structure is attributable to sampling configuration. [src: enigma_sso_asv_ecology]
- Generate metagenomes at the same spatial resolution and compare functional genes with ASV-based assignments to test whether the persistent spatial pattern corresponds to measured metabolic capacity. [src: enigma_sso_asv_ecology]

## Related Pages

- [[summaries/enigma_sso_asv_ecology__REPORT]]
- [[concepts/subsurface-hydrogeological-zonation]]
- [[concepts/groundwater-sediment-community-partitioning]]
- [[concepts/collection-site-versus-microenvironment-mismatch]]
- [[concepts/environmental-embedding-ecological-validity]]
