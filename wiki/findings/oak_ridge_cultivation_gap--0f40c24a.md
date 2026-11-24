---
type: "Finding"
description: "Of 10,845 KEGG orthologs tested, 8,482 (78.2%) show statistically significant prevalence differences (Fisher's exact, BH-FDR < 0.05) between 3,102 cultured ENIGMA Genome Depot isolates and 2,279 subsurface/groundwater MAGs from the KBase Data Lakehouse pangenome."
finding_id: "oak_ridge_cultivation_gap--0f40c24a"
result: "observation"
source: "oak_ridge_cultivation_gap"
quantities: [{"value": "10,845", "what": "KEGG orthologs tested", "unit": "KOs", "denominator": "", "scope": ""}, {"value": "8,482", "what": "KOs with significant prevalence difference", "unit": "KOs", "denominator": "10,845 KOs tested", "scope": ""}, {"value": "78.2%", "what": "share of KOs significantly different", "unit": "", "denominator": "10,845 KOs tested", "scope": ""}]
caveat: "The report cautions that the headline 78% of KOs showing significant bias conflates genome-size asymmetry with true functional divergence."
first_added: "2026-11-24"
source_hash: "dfa453d2f23c3938c1555212e52ce3b01063128ef90398dc6fd588b785de1a70"
---
# Most KOs differ in prevalence between cultured isolates and subsurface MAGs

Of 10,845 KEGG orthologs tested, 8,482 (78.2%) show statistically significant prevalence differences (Fisher's exact, BH-FDR < 0.05) between 3,102 cultured ENIGMA Genome Depot isolates and 2,279 subsurface/groundwater MAGs from the KBase Data Lakehouse pangenome. [src: oak_ridge_cultivation_gap]

## Key figures

- **10,845 KOs**: KEGG orthologs tested [src: oak_ridge_cultivation_gap]
- **8,482 KOs**: KOs with significant prevalence difference (denominator 10,845 KOs tested) [src: oak_ridge_cultivation_gap]
- **78.2%**: share of KOs significantly different (denominator 10,845 KOs tested) [src: oak_ridge_cultivation_gap]

## Evidence

> Of 10,845 KEGG orthologs tested, 8,482 (78.2%) show statistically significant prevalence differences (Fisher's exact, BH-FDR < 0.05) between 3,102 cultured ENIGMA Genome Depot isolates and 2,279 subsurface/groundwater MAGs from the BERDL pangenome. [src: oak_ridge_cultivation_gap]

From the report [[summaries/oak_ridge_cultivation_gap__REPORT]].

## Caveat

The report cautions that the headline 78% of KOs showing significant bias conflates genome-size asymmetry with true functional divergence. [src: oak_ridge_cultivation_gap]

> The headline number — 78% of KOs showing significant bias — initially suggests a dramatic functional mismatch. However, this number conflates two distinct phenomena: [src: oak_ridge_cultivation_gap]

## Other caveats in this report

- The report pivoted from 623 ORFRC-specific MAGs in enigma_coral because their assembly FASTAs at /h/jmc/data/ were inaccessible from JupyterHub, so its findings concern subsurface systems generally rather than Oak Ridge specifically. [src: oak_ridge_cultivation_gap]
- The report attributes much of the cultured-versus-MAG functional asymmetry to genome-size disparity rather than specific functional selection, substantially driven by MAG taxonomic composition. [src: oak_ridge_cultivation_gap]
- The report says its NiFe-hydrogenase result contradicts Beaver & Neufeld (2024)'s prediction of group 1 [NiFe]-hydrogenase concentration in uncultivated lineages, possibly because the cultured collection captures hydrogenotrophs better than expected or KO assignments conflate hydrogenase groups. [src: oak_ridge_cultivation_gap]
- The report interprets the genomically encoded conjugation apparatus as well retained and suggests Goff et al. (2024)'s MGE-depletion prediction may apply specifically to episomal elements not captured by whole-genome sequencing in either cohort. [src: oak_ridge_cultivation_gap]
- The report predicts that excluding Patescibacteria would leave MAGs with substantially more KOs per genome and narrow the apparent functional gap with cultured genomes. [src: oak_ridge_cultivation_gap]
