---
type: "Summary"
description: "Deep-clay Bacillota_B show gene-content expansion and corrected IR comparisons"
doc_type: "short"
full_text: "sources/bacillota_b_subsurface_accessory__REPORT.md"
---
# Subsurface Bacillota_B Specialization — What Distinguishes Deep-Clay Lineages from Soil Congeners?

## Overview

This report compares 10 deep-clay Bacillota_B genomes with 62 soil-baseline Bacillota_B genomes using eggNOG orthologous-group (OG) enrichment, genome-content statistics, and a corrected multi-heme cytochrome detector. It identifies 547 significantly enriched OGs, finds that deep-clay genomes are larger rather than streamlined, and revises the clay-project iron-reduction comparison after detecting mismatched marker KOs. [src: bacillota_b_subsurface_accessory]

## Key Findings

### 1. Deep-clay genomes are enriched for anaerobic-niche and persistence functions

Per-OG Fisher’s exact tests across 14,109 Firmicutes-level eggNOG OGs, comparing anchor n=10 with baseline n=62 and applying Benjamini–Hochberg false-discovery-rate correction, a fold-difference threshold of ≥3, and a minimum of ≥3 anchor genomes positive, identified 547 enriched OGs at q<0.05. This exceeded the preregistered H1 prediction of ≥10 and was strongly supported. [src: bacillota_b_subsurface_accessory]

The keyword-scanned enriched set included 42 anaerobic-respiration OGs, 24 sporulation-revival OGs, 12 mineral-attachment or exopolysaccharide OGs, 4 anaerobic-regulator OGs, 3 osmoadaptation OGs, and 462 other or unannotated OGs. Example annotations included hydrogenase, cytochrome, sulfite, sulfate, nitrate, fumarate reductase, NADH dehydrogenase, oxidoreductase, menaquinone, spore and germination functions, biofilm and capsule functions, sigma factors, two-component systems, betaine, ectoine, osmoprotectants, and K⁺ uptake. [src: bacillota_b_subsurface_accessory]

Manual inspection showed that the 462-OG “other” category undercounted anaerobic-respiration and electron-transfer functions. COG1977, associated with molybdopterin cofactor metabolism, occurred in 10/10 anchors versus 11/62 baselines; OG 1UIFM, a DsrE/DsrF/DsrH-like family, occurred in 7/10 anchors versus 0/62 baselines; OG 1VFGN, a 4Fe–4S dicluster associated with 2-oxoglutarate:ferredoxin oxidoreductase, occurred in 8/10 anchors versus 4/62 baselines; and OG 1V0WU, a Major Facilitator Superfamily transporter, occurred in 9/10 anchors versus 5/62 baselines. Manual reclassification suggested that the true anaerobic-respiration-related total was closer to 80–100 of the 547 enriched OGs. [src: bacillota_b_subsurface_accessory]

### 2. Deep-clay Bacillota_B genomes are larger and contain more OGs

Deep-clay anchor genomes had a mean genome size of 4,110,038 bp versus 3,046,124 bp for soil-baseline genomes, with Cohen’s d=+1.39 and Mann–Whitney p=0.025. CheckM-rescaled genome sizes were 4,323,230 bp versus 3,233,715 bp, with Cohen’s d=+1.37 and p=0.013. [src: bacillota_b_subsurface_accessory]

Mean GC content was 48.84% in anchors versus 47.76% in baseline genomes, with Cohen’s d=+0.21 and p=0.44. Mean eggNOG OG counts were 2,630 versus 2,106, with Cohen’s d=+1.30 and p=0.022; CheckM-rescaled OG counts were 2,771 versus 2,233, with Cohen’s d=+1.32 and p=0.009. [src: bacillota_b_subsurface_accessory]

Mean CheckM completeness was effectively identical between cohorts at 94.7% for anchors and 94.3% for baseline genomes, with Cohen’s d=+0.08 and p=0.93. The report therefore concludes that the larger anchor genomes and higher OG counts cannot be explained by a genome-quality artifact. [src: bacillota_b_subsurface_accessory]

The H2 prediction that deep-clay genomes would be smaller was rejected in the opposite direction: all four size and OG-count metrics indicated significantly larger anchor genomes, with p≤0.025 and Cohen’s d≥+1.30. The result is presented as supporting a self-sufficiency model for cultivable subsurface Bacillota_B and as contrasting with streamlining reported for Patescibacteria, while remaining consistent with the report’s distinction between these ecological and phylogenetic groups. [src: bacillota_b_subsurface_accessory]

### 3. Corrected multi-heme cytochrome detection removes the original iron-reduction contrast

The clay-confined-subsurface project’s original iron-reduction analysis used K07811, K17324, and K17323 as markers, although the report identifies these as TMAO reductase, glycerol ABC ATP-binding, and glycerol ABC permease genes rather than canonical iron-reduction markers. The corrected detector combined PFAM PF02085, PFAM PF22678, and a CXXCH heme-binding motif count of ≥4 in gene-cluster protein sequences; a genome was positive if any signal was present. [src: bacillota_b_subsurface_accessory]

In the corrected comparison, anchor_deep had 5/9 positive genomes, or 55.6%, versus 1/9, or 11.1%, under the original marker set. Anchor_shallow had 12/30, or 40.0%, versus 15/30, or 50.0%, originally. Soil_baseline had 61/149, or 40.9%, versus 30/149, or 20.1%, originally. [src: bacillota_b_subsurface_accessory]

Corrected pairwise Fisher tests found no significant cohort differences: deep versus shallow had odds ratio 1.88 and p=0.46; deep versus baseline had odds ratio 1.80 and p=0.49; and shallow versus baseline had odds ratio 0.96 and p=1.0. The original shallow-enrichment narrative therefore loses statistical support, while corrected multi-heme cytochrome content is similar across the clay cohorts and soil baseline. [src: bacillota_b_subsurface_accessory]

The clay project’s sulfite-reduction-side finding remains supported: 5/9 deep-cohort genomes were positive versus a Mitzscherling rock-attached null rate of 0.2%, with binomial p=4×10⁻¹². The report consequently considers the clay-project porewater-bias interpretation supported through sulfite reduction but unsupported on the corrected iron-reduction side. [src: bacillota_b_subsurface_accessory]

### 4. Cohort, pangenome, and marker-availability context

The Bacillota_B universe contained 334 genomes in the BERDL pangenome, substantially fewer than the v1.1 plan’s estimate of 6,700. The anchor_deep_clay cohort comprised 10 genomes from Mont Terri Opalinus borehole and rock-porewater samples plus two Russian Beyelii Yar borehole genomes; the soil_baseline cohort comprised 62 phylum-matched soil or sediment genomes spanning Syntrophomonadales, Desulfitobacteriales, Moorellales, Thermacetogeniales, Ammonifexales, Carboxydocellales, Desulfotomaculales, Heliobacteriales, and Thermincolales. [src: bacillota_b_subsurface_accessory]

Within Bacillota_B, PF02085 had 4 hits in 4 clusters, PF00034 had 1 hit in 1 cluster, PF13442 had 1 hit in 1 cluster, PF22678 had 1 hit in 1 cluster, and PF14537 had 0 hits in 0 clusters. The report states that CXXCH motif counting carried most of the corrected iron-reduction signal because multi-heme cytochrome PFAMs were sparse. [src: bacillota_b_subsurface_accessory]

## Caveats

The anchor cohort contains 10 genomes and the baseline contains 62. Fisher’s exact testing is considered adequate for the large 547-OG effect, but marginal effects supported by anchor counts of 3–5 are described as primarily descriptive. [src: bacillota_b_subsurface_accessory]

The anchor cohort is borehole- and porewater-dominated by construction, reflecting cultivation bias toward porewater isolates. The comparison therefore cannot test whether rock-attached Bacillota_B differ in gene content. [src: bacillota_b_subsurface_accessory]

Genus-level phylogenetic confounding is only partly mitigated: the cohort spans four orders, but the 10-genome anchor is clumped among 3 BRH-c8a genomes, 2 BRH-c4a genomes, 2 Desulfosporosinus genomes, Desulforudis, Ch130, and 1 other genome. Some enriched OGs may therefore be lineage markers rather than recurrent subsurface-specialization features. [src: bacillota_b_subsurface_accessory]

The OG hierarchy is imperfect. The analysis used Firmicutes-level OGs where available and bacteria/root fallbacks otherwise; some enriched OGs are therefore at coarse taxonomic levels. A Bacillota_B-specific eggNOG tier was unavailable because Bacillota_B genomes are distributed across legacy NCBI-taxonomy classes. [src: bacillota_b_subsurface_accessory]

Keyword-based functional categorization undercounted relevant functions: the “other_or_unannotated” group contained substantial anaerobic-respiration and electron-transfer signal, including COG1977 molybdopterin metabolism, DsrEFH-like proteins, and 2-oxoglutarate:ferredoxin oxidoreductase. Manual reclassification or an LLM-based extractor would be needed to refine category counts. [src: bacillota_b_subsurface_accessory]

The corrected iron-reduction analysis is considered robust for the multi-heme cytochrome signal but is a Phase 1 correction. It does not fully determine whether the original clay-project comparison with the Bagnoud porewater pattern should be retained; the sulfite-reduction side remains robust, whereas the iron-reduction side loses force. [src: bacillota_b_subsurface_accessory]

The report proposes applying the correction to the clay-project branch, refining the 462-OG category with an LLM-based scan, decomposing the H1 signal by genus, localizing the functions responsible for the larger anchor genomes, and testing the same enrichment framework in other phylum-matched subsurface comparisons. [src: bacillota_b_subsurface_accessory]

## Slots Into

- [[concepts/pangenome-integration]] — The 547 enriched OGs, genome-size expansion, cohort construction, and taxonomic limitations provide a within-lineage pangenome comparison.
- [[concepts/subsurface-bacillota-specialization]] — The central finding that deep-clay Bacillota_B encode anaerobic-respiration, sporulation-revival, mineral-attachment, regulatory, and osmoadaptation features while retaining larger genomes.
- [[concepts/functional-marker-validation]] — The corrected triple-signal detector and the resulting loss of the original shallow-versus-deep iron-reduction contrast provide a reusable marker-correction workflow.
