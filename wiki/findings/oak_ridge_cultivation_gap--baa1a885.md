---
type: "Finding"
description: "NiFe-hydrogenase (2 KOs), predicted to be depleted in cultured genomes, shows mean log2 ratio +6.26, cultured enrichment, and 2/2 significant KOs."
finding_id: "oak_ridge_cultivation_gap--baa1a885"
result: "correction"
source: "oak_ridge_cultivation_gap"
quantities: [{"value": "+6.26", "what": "mean log2 ratio, cultured versus MAGs", "unit": "", "denominator": "", "scope": ""}, {"value": "2/2", "what": "KOs significant", "unit": "", "denominator": "", "scope": ""}]
caveat: "The result contradicts the Beaver & Neufeld (2024) prediction, either because the cultured collection captures hydrogenotrophic organisms better than expected or because the KO assignment conflates different hydrogenase groups."
first_added: "2026-11-24"
source_hash: "dfa453d2f23c3938c1555212e52ce3b01063128ef90398dc6fd588b785de1a70"
---
# NiFe-hydrogenase was cultured-enriched, contrary to predicted depletion

NiFe-hydrogenase (2 KOs), predicted to be depleted in cultured genomes, shows mean log2 ratio +6.26, cultured enrichment, and 2/2 significant KOs. [src: oak_ridge_cultivation_gap]

## Key figures

- **+6.26**: mean log2 ratio, cultured versus MAGs [src: oak_ridge_cultivation_gap]
- **2/2**: KOs significant [src: oak_ridge_cultivation_gap]

## Evidence

> | NiFe-hydrogenase | 2 | +6.26 | Cultured-enriched | 2/2 | No (predicted depleted) | [src: oak_ridge_cultivation_gap]

From the report [[summaries/oak_ridge_cultivation_gap__REPORT]].

## Caveat

The result contradicts the Beaver & Neufeld (2024) prediction, either because the cultured collection captures hydrogenotrophic organisms better than expected or because the KO assignment conflates different hydrogenase groups. [src: oak_ridge_cultivation_gap]

> This contradicts the prediction from Beaver & Neufeld (2024) that group 1 [NiFe]-hydrogenases are concentrated in uncultivated lineages — either the cultured collection captures hydrogenotrophic organisms better than expected, or the KO assignment conflates different hydrogenase groups. [src: oak_ridge_cultivation_gap]

## Other caveats in this report

- The report pivoted from 623 ORFRC-specific MAGs in enigma_coral because their assembly FASTAs at /h/jmc/data/ were inaccessible from JupyterHub, so its findings concern subsurface systems generally rather than Oak Ridge specifically. [src: oak_ridge_cultivation_gap]
- The report attributes much of the cultured-versus-MAG functional asymmetry to genome-size disparity rather than specific functional selection, substantially driven by MAG taxonomic composition. [src: oak_ridge_cultivation_gap]
- The report interprets the genomically encoded conjugation apparatus as well retained and suggests Goff et al. (2024)'s MGE-depletion prediction may apply specifically to episomal elements not captured by whole-genome sequencing in either cohort. [src: oak_ridge_cultivation_gap]
- The report predicts that excluding Patescibacteria would leave MAGs with substantially more KOs per genome and narrow the apparent functional gap with cultured genomes. [src: oak_ridge_cultivation_gap]
- The report cautions that the headline 78% of KOs showing significant bias conflates genome-size asymmetry with true functional divergence. [src: oak_ridge_cultivation_gap]
