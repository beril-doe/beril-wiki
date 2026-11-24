---
type: "Concept"
description: "Covers how reaction-direction and carbon-versus-nitrogen filters, signature completeness and certainty scoring decide which compounds count as callable, and the errors they introduce."
sources: ["summaries/enigma_carbon_census_1__REPORT.md"]
---
# Catabolic-direction filtering and mis-scored carbon calls

Catabolic-direction filtering and mis-scored carbon calls is the topic of this page. The evidence comes from one project, enigma_carbon_census_1 ([[summaries/enigma_carbon_census_1__REPORT]]). It documents one clear mis-scored compound (xanthine) and one metric that is not comparable across compounds (signature completeness). [src: enigma_carbon_census_1]

## Catabolic-direction filtering

The NB03 filter keeps only catabolic-direction evidence: 846 Tier-2 pathway and 102 Tier-3 signature genome-compound calls. [src: enigma_carbon_census_1] Biosynthetic-only signatures are excluded and land in the dark set. [src: enigma_carbon_census_1]

The 8 enigma_isolate_call callables rest on a genome-prevalence-<10% signature-reaction filter. It keeps a reaction only if it is catabolic for the compound, judged by KEGG degradation map membership or a 3-reaction curated allowlist. [src: enigma_carbon_census_1]

Lauric acid, the 9th callable, rests on an independent measured-fitness basis and is not subject to this filter. [src: enigma_carbon_census_1] See [[concepts/measured-fitness-as-independent-evidence-of-carbon-utilization]]. A different filter would move the callable/dark boundary, so the dark fraction depends on this choice. [src: enigma_carbon_census_1]

## The xanthine carbon-versus-nitrogen error

Xanthine was mis-scored as carbon-callable. Its allowlisted reaction R02107 (xanthine to urate, xanthine oxidase) belongs to the purine pathway, which is nitrogen acquisition and not carbon catabolism. [src: enigma_carbon_census_1] The carbon-callable set is therefore effectively 8 of the 9 callable compounds. [src: enigma_carbon_census_1]

A bacterial carbon route for purines exists, but it is a distinct anaerobic gene cluster that the project does not score. [src: enigma_carbon_census_1]

R02107 has been removed from the carbon allowlist in build_nb03.py. [src: enigma_carbon_census_1] The committed tables still list xanthine because they were not regenerated after the fix. Rerunning NB03→NB04→NB08 would drop it. [src: enigma_carbon_census_1]

## Signature completeness and certainty

The sig_completeness metric is the fraction of each compound's own signature reactions that a genome carries. [src: enigma_carbon_census_1] High-certainty calls are therefore not comparable across compounds. A single-reaction signature, such as terephthalic acid with 1 required reaction, scores 1.0 ("high") for any carrier. A 3-reaction signature, such as phthalic acid, cannot do this. [src: enigma_carbon_census_1]

For this reason the report calls the "terephthalic 34/34 high" headline the weakest completeness call, not the strongest. [src: enigma_carbon_census_1] It describes the "34 all high-certainty" result as a single-reaction-signature artifact, not a strength. [src: enigma_carbon_census_1] The report recommends reading certainty as the raw n_sig_carried / n_required, which is reported in phylo_utilizer_map.tsv. [src: enigma_carbon_census_1]

## Open Directions

- Regenerate the NB03→NB04→NB08 tables with R02107 removed. This would confirm the carbon-callable count of 8 and show how the dark set changes.
- Audit every allowlisted and KEGG-map reaction for carbon-versus-nitrogen role. This would find other errors like xanthine.
- Re-score the callable/dark boundary under alternative direction filters. This would measure how far the dark fraction depends on the filter.
- Replace normalized completeness with raw n_sig_carried / n_required, or weight it by signature size. This would make certainty comparable across compounds.
- Add the anaerobic purine carbon gene cluster to the signature set. This would test whether xanthine becomes legitimately callable.
