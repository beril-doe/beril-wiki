---
type: "Concept"
description: "Evidence that subsurface Bacillota_B expand genomes rather than streamline them"
sources: ["summaries/bacillota_b_subsurface_accessory__REPORT.md"]
---
# Genome Expansion Versus Streamlining in Specialized Microbes

## Scope

Genome specialization does not necessarily imply genome reduction: in the reported deep-clay comparison, cultivable Bacillota_B lineages had larger genomes and more orthologous groups than soil-baseline lineages, consistent with a self-sufficiency model rather than streamlining. [src: bacillota_b_subsurface_accessory] This finding refines [[concepts/subsurface-bacillota-specialization]] and contributes to [[concepts/pangenome-integration]]. [src: bacillota_b_subsurface_accessory]

## Core Evidence

The study compared 10 deep-clay Bacillota_B genomes with 62 soil-baseline Bacillota_B genomes using genome-content statistics and eggNOG orthologous groups (OGs), which are clusters of evolutionarily related proteins. [src: bacillota_b_subsurface_accessory] The deep-clay cohort included genomes from Mont Terri Opalinus borehole and rock-porewater samples plus two Russian Beyelii Yar borehole genomes, whereas the soil-baseline cohort covered multiple Bacillota_B orders. [src: bacillota_b_subsurface_accessory]

Mean genome size was 4,110,038 bp in the deep-clay anchors versus 3,046,124 bp in the soil baseline, with Cohen’s d=+1.39 and Mann–Whitney p=0.025. [src: bacillota_b_subsurface_accessory] CheckM-rescaled genome size was 4,323,230 bp versus 3,233,715 bp, with Cohen’s d=+1.37 and p=0.013. [src: bacillota_b_subsurface_accessory]

Mean eggNOG OG count was 2,630 in the anchors versus 2,106 in the baseline, with Cohen’s d=+1.30 and p=0.022. [src: bacillota_b_subsurface_accessory] CheckM-rescaled OG count was 2,771 versus 2,233, with Cohen’s d=+1.32 and p=0.009. [src: bacillota_b_subsurface_accessory]

The larger genomes and higher OG counts were not explained by an apparent completeness difference: mean CheckM completeness was 94.7% for anchors and 94.3% for baseline genomes, with Cohen’s d=+0.08 and p=0.93. [src: bacillota_b_subsurface_accessory] Across all four size and OG-count metrics, the comparison therefore rejected the preregistered prediction that deep-clay genomes would be smaller and instead supported larger genomes in the anchor cohort, with p≤0.025 and Cohen’s d≥+1.30. [src: bacillota_b_subsurface_accessory]

## Functional Interpretation

The deep-clay comparison identified 547 significantly enriched OGs among 14,109 Firmicutes-level eggNOG OGs after Fisher’s exact testing, Benjamini–Hochberg false-discovery-rate correction, a fold-difference threshold of ≥3, and a minimum of ≥3 positive anchor genomes at q<0.05. [src: bacillota_b_subsurface_accessory] The enriched set included keyword-scanned categories for anaerobic respiration, sporulation and revival, mineral attachment or exopolysaccharide production, anaerobic regulation, and osmoadaptation. [src: bacillota_b_subsurface_accessory]

Manual inspection indicated that the keyword categories undercounted anaerobic-respiration and electron-transfer functions, with the true anaerobic-respiration-related total estimated by the report at closer to 80–100 of the 547 enriched OGs. [src: bacillota_b_subsurface_accessory] Examples included COG1977, which occurred in 10/10 anchors versus 11/62 baselines, a DsrE/DsrF/DsrH-like OG present in 7/10 anchors versus 0/62 baselines, and a 4Fe–4S dicluster OG present in 8/10 anchors versus 4/62 baselines. [src: bacillota_b_subsurface_accessory] These enrichments support the hypothesis that expanded deep-clay genomes may encode broader anaerobic persistence and resource-use capacity, but the ecological interpretation remains qualified because the anchor cohort is small and phylogenetically clumped. [src: bacillota_b_subsurface_accessory]

The result contrasts with a simple streamlining expectation for specialized subsurface microbes: the studied deep-clay Bacillota_B were larger and more functionally expansive than the soil baseline rather than smaller. [src: bacillota_b_subsurface_accessory] The report presents this pattern as supporting a self-sufficiency model for cultivable subsurface Bacillota_B, while distinguishing it from streamlining reported for Patescibacteria, which are an ecological and phylogenetic comparison rather than the focal group here. [src: bacillota_b_subsurface_accessory]

## Limits on Generalization

The Bacillota_B universe contained 334 genomes in the BERDL pangenome, substantially fewer than the v1.1 plan’s estimate of 6,700, so the available comparison does not establish that genome expansion is a general property of all subsurface Bacillota_B. [src: bacillota_b_subsurface_accessory] The anchor cohort contained 10 genomes, while the baseline contained 62, and effects supported by anchor counts of 3–5 were considered primarily descriptive. [src: bacillota_b_subsurface_accessory]

The anchor cohort was borehole- and porewater-dominated because of cultivation bias, and the comparison therefore could not test whether rock-attached Bacillota_B differ in gene content. [src: bacillota_b_subsurface_accessory] The 10 anchor genomes were also clumped among 3 BRH-c8a genomes, 2 BRH-c4a genomes, 2 Desulfosporosinus genomes, Desulforudis, Ch130, and 1 other genome, leaving genus-level phylogenetic confounding only partly mitigated. [src: bacillota_b_subsurface_accessory] Some enriched OGs may therefore be lineage markers rather than recurrent subsurface-specialization features, linking this interpretation to [[concepts/phylogenetic-confounding-of-pangenome-associations]]. [src: bacillota_b_subsurface_accessory]

The analysis used Firmicutes-level OGs where available and bacteria/root fallbacks otherwise, because a Bacillota_B-specific eggNOG tier was unavailable; this heterogeneous OG hierarchy may affect functional resolution. [src: bacillota_b_subsurface_accessory] Keyword-based categorization also placed 462 enriched OGs in an “other or unannotated” group even though manual inspection found substantial anaerobic-respiration and electron-transfer signal in that group. [src: bacillota_b_subsurface_accessory]

## Relation to the Wider Wiki

This finding **supports** [[concepts/subsurface-bacillota-specialization]] by showing that the deep-clay phenotype is associated with expanded genome content alongside anaerobic-respiration, persistence, attachment, regulatory, and osmoadaptation functions. [src: bacillota_b_subsurface_accessory] It **refines** [[concepts/pangenome-integration]] by showing that a within-lineage accessory-genome comparison can reveal expansion even when the ecological question is framed around specialization. [src: bacillota_b_subsurface_accessory] It also **qualifies** interpretations connected to [[concepts/genome-size-confounding-of-functional-scores]], because the observed OG enrichment co-occurs with a large genome-size difference that should be modeled when comparing functional scores. [src: bacillota_b_subsurface_accessory]

## Open Directions

- Partition the 547 enriched OGs by genus and phylogenetic background using genus-stratified enrichment or a phylogenetically controlled model to determine which signals persist beyond lineage structure. [src: bacillota_b_subsurface_accessory]
- Reclassify the 462 “other or unannotated” OGs with an LLM-assisted or manual functional scan, then test whether the inferred 80–100 anaerobic-respiration-related OGs remain enriched after standardized annotation. [src: bacillota_b_subsurface_accessory]
- Compare genome size, OG count, and functional categories across additional phylum-matched subsurface cohorts to test whether expansion is specific to these Bacillota_B lineages or recurs across subsurface specialists. [src: bacillota_b_subsurface_accessory]
- Add rock-attached Bacillota_B genomes and repeat the same pangenome comparison to test whether the observed expansion characterizes porewater-associated isolates specifically or deep-clay Bacillota_B more broadly. [src: bacillota_b_subsurface_accessory]
- Use pathway-level reconstruction and phenotype or growth data to test whether the additional genome content improves predicted self-sufficiency under anaerobic subsurface conditions rather than merely reflecting lineage-specific accessory genes. [src: bacillota_b_subsurface_accessory]

See the source-level discussion in [[summaries/bacillota_b_subsurface_accessory__REPORT]].
