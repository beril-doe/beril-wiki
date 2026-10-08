---
type: "Compound"
description: "Sorbitol, a sugar alcohol that appears in this corpus as a predicted carbon-utilization pathway \u2014 frequently gap-flagged by pathway prediction across genomes and reduced in lung-adapted Pseudomonas aeruginosa genomes."
sources: ["summaries/cf_formulation_design__REPORT.md", "summaries/functional_dark_matter__REPORT.md"]
---
Sorbitol is a sugar alcohol that enters this corpus only as a *predicted* carbon-utilization capability: it is scored as a carbon-category pathway by [[entities/gapmind]] (which scores how completely a genome's annotations cover the steps of a known metabolic pathway), so the evidence below is about pathway-completeness scores and annotation gaps, not about measured growth on sorbitol [src: functional_dark_matter].

## Predicted pathway gaps across organisms

Across 44 FB-linked species, GapMind identified 1,256 organism-pathway pairs with nearly-complete metabolic pathways (score: `steps_missing_low`) in species that also harbor functionally dark genes with strong fitness effects, and sorbitol utilization is among the most frequently gapped carbon pathways: gaps in 30 organisms, with *D. desulfuricans*, *D. vulgaris* ([[entities/desulfovibrio-vulgaris-hildenborough]]) and Miyama given as example organisms — alongside [[entities/fucose]] utilization (32), [[entities/rhamnose]] utilization (31), [[entities/myoinositol]] utilization (28) and [[entities/gluconate]] utilization (26) [src: functional_dark_matter]. The report is explicit that these are organism-level co-occurrences and that no direct gene-to-gap enzymatic matching was performed, so no gene is assigned to a missing sorbitol step; "the co-occurrence suggests dark genes could encode missing steps, but confirming this requires EC number matching, structure prediction, or experimental validation" [src: functional_dark_matter].

## Reduced sorbitol pathway scores in lung-adapted Pseudomonas aeruginosa

In a genomic pathway comparison, lung [[entities/pseudomonas-aeruginosa]] (PA) genomes "lose sugar utilization pathways (sorbitol, mannitol, gluconate) while amino acid catabolism remains invariant"; the report draws from this the further conclusion that this is "confirming competitive exclusion targets are evolutionarily stable" [src: cf_formulation_design]. That evolutionary-stability reading is an inference from a cross-genome comparison of predicted pathways rather than a measured evolutionary outcome, and should be treated as a hypothesis [src: cf_formulation_design].

The same pangenome comparison reports that lung-adapted [[entities/streptococcus-salivarius]] genomes show enrichment for L-malate (+0.39 score) and depletion for sorbitol (−0.82), which the report reads as suggesting metabolic adaptation to the airway carbon landscape [src: cf_formulation_design].

## Where it matters

Because predicted sorbitol utilization is among the capabilities reduced in lung PA genomes while amino acid catabolism is reported as invariant, this corpus suggests the hypothesis that sorbitol is a weaker nutrient to compete for than the amino acid routes in [[concepts/competitive-exclusion-consortium-design]]; the comparison is genomic, and the prebiotic candidates the project advanced on this basis — "**Sugar alcohols (xylitol, myoinositol) and pentoses (xylose, arabinose, fucose, rhamnose)**", a list that keeps sugar alcohols and pentoses as separate classes and that does not include sorbitol — came from "genomic pathway comparison", not from the carbon-utilization assays, so these predicted capabilities remain untested [src: cf_formulation_design]. Separately, the recurrence of sorbitol utilization as a predicted pathway gap in 30 organisms makes it a standing candidate target for [[concepts/experimental-prioritization-of-functional-dark-matter]], where the gap to close is the missing gene-to-step assignment [src: functional_dark_matter].
