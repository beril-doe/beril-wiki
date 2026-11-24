---
type: "Finding"
description: "Sulfate-reduction aprAB (K00394) shows no significant difference in prevalence between cultured genomes and subsurface MAGs, unlike dsrAB, which is depleted in cultured genomes."
finding_id: "oak_ridge_cultivation_gap--5b9b603e"
result: "null result"
source: "oak_ridge_cultivation_gap"
quantities: []
caveat: "MAGs are inherently less complete than isolate genomes (mean completeness 78.7% in the QC-filtered cohort), so some KOs scored as absent from MAGs may lie in the missing 20% of the genome."
first_added: "2026-11-24"
source_hash: "dfa453d2f23c3938c1555212e52ce3b01063128ef90398dc6fd588b785de1a70"
---
# Sulfate-reduction aprAB shows no significant prevalence difference

Sulfate-reduction aprAB (K00394) shows no significant difference in prevalence between cultured genomes and subsurface MAGs, unlike dsrAB, which is depleted in cultured genomes. [src: oak_ridge_cultivation_gap]

## Evidence

> The dsrAB genes (K11180, K11181) are 3.0-3.1 log2 depleted in cultured, but aprAB (K00394) shows no significant difference and sat/PAPSS (K00395, K00958) are cultured-enriched. [src: oak_ridge_cultivation_gap]

From the report [[summaries/oak_ridge_cultivation_gap__REPORT]].

## Caveat

MAGs are inherently less complete than isolate genomes (mean completeness 78.7% in the QC-filtered cohort), so some KOs scored as absent from MAGs may lie in the missing 20% of the genome. [src: oak_ridge_cultivation_gap]

> MAGs are inherently less complete than isolate genomes (mean completeness 78.7% in our QC-filtered cohort). Some KOs scored as "absent from MAGs" may simply be in the missing 20% of the genome. [src: oak_ridge_cultivation_gap]

## Other caveats in this report

- The report pivoted from 623 ORFRC-specific MAGs in enigma_coral because their assembly FASTAs at /h/jmc/data/ were inaccessible from JupyterHub, so its findings concern subsurface systems generally rather than Oak Ridge specifically. [src: oak_ridge_cultivation_gap]
- The report attributes much of the cultured-versus-MAG functional asymmetry to genome-size disparity rather than specific functional selection, substantially driven by MAG taxonomic composition. [src: oak_ridge_cultivation_gap]
- The report says its NiFe-hydrogenase result contradicts Beaver & Neufeld (2024)'s prediction of group 1 [NiFe]-hydrogenase concentration in uncultivated lineages, possibly because the cultured collection captures hydrogenotrophs better than expected or KO assignments conflate hydrogenase groups. [src: oak_ridge_cultivation_gap]
- The report interprets the genomically encoded conjugation apparatus as well retained and suggests Goff et al. (2024)'s MGE-depletion prediction may apply specifically to episomal elements not captured by whole-genome sequencing in either cohort. [src: oak_ridge_cultivation_gap]
- The report predicts that excluding Patescibacteria would leave MAGs with substantially more KOs per genome and narrow the apparent functional gap with cultured genomes. [src: oak_ridge_cultivation_gap]
