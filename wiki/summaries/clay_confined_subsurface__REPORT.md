---
type: "Summary"
description: "Tests clay-subsurface cultivation bias, anaerobic traits, and biosynthetic self-sufficiency."
doc_type: "short"
full_text: "sources/clay_confined_subsurface__REPORT.md"
---
# Self-Sufficiency, Anaerobic Toolkit, and Cultivation Bias in Clay-Confined Cultured Bacterial Genomes

## Overview

This report analyzes cultured bacterial genomes from clay-related environments in the KBase KE pangenome, comparing 9 deep-confined genomes, 30 shallow-clay genomes, and a phylum-stratified soil baseline of 150 genomes (137 after quality filtering). It tests biosynthetic self-sufficiency, an anaerobic metabolic toolkit, and whether cultured clay genomes resemble porewater or rock-attached subsurface communities. The principal result is that the deep cultured cohort carries a robust dissimilatory sulfate-reduction signal associated with the Bagnoud Mont Terri porewater paradigm, while broader anaerobic-toolkit enrichment is largely explained by Bacillota_B phylogeny and self-sufficiency is not elevated. [src: clay_confined_subsurface]

## Key Findings

### Cultured deep-clay genomes show a sulfate-reduction-rich porewater signature

The deep cohort contained 5/9 genomes with dissimilatory sulfate-reduction markers, compared with 1/9 iron-reduction-marker-positive genomes under the original analysis. Relative to the Mitzscherling (2023) rock-attached null, the sulfate-reduction enrichment was highly significant: 5 observed positives versus 0.018 expected among 9 genomes, binomial p = 4.0×10⁻¹². The comparison to the rock-attached null for iron-reduction depletion was not significant: 1 observed versus 0.63 expected, p = 0.87. [src: clay_confined_subsurface]

The report concludes that the cultured Mont Terri cohort matches the Bagnoud porewater paradigm rather than demonstrating representation of the rock-attached community. The 8 Opalinus genomes trace to BRC-3 or BIC-A1 borehole isolation sources, and the cohort includes Desulfosporosinus, BRH-c8a, BRH-c4a, Lutibacter, BRH-c54, Roseovarius, and Stenotrophomonas lineages. [src: clay_confined_subsurface]

The original iron-reduction analysis was corrected because K07811, K17324, and K17323 were misidentified as iron-reduction markers; they are TMAO reductase, glycerol ABC transport ATP-binding, and glycerol ABC transport permease, respectively. A corrected triple-signal multi-heme cytochrome detector used PFAM PF02085, PFAM PF22678, and CXXCH heme-binding motif counting with a threshold of ≥4 motifs. Corrected iron-reduction rates were 55.6% for anchor_deep (n = 9), 40.0% for anchor_shallow (n = 30), and 40.9% for soil_baseline (n = 149), versus original rates of 11.1%, 50.0%, and 20.1%, respectively; all corrected cohort comparisons had Fisher p ≥ 0.46. The original shallow-greater-than-deep iron-reduction narrative is withdrawn, while the sulfate-reduction finding remains supported. [src: clay_confined_subsurface]

### The anaerobic toolkit is strongly enriched at cohort level but mostly phylum-driven

The anaerobic toolkit combined Wood–Ljungdahl (WL), group 1 [NiFe]-hydrogenase (NiFe), and dissimilatory sulfate-reduction (SR) modules. Mean toolkit scores were 1.889 for anchor_deep (n = 9), 0.033 for anchor_shallow (n = 30), and 0.393 for soil_baseline (n = 140); the proportions with all three modules were 0.556, 0.000, and 0.021, respectively. Against the soil baseline, deep-cohort Fisher tests adjusted by BH-FDR (the Benjamini–Hochberg false-discovery-rate procedure) gave WL OR = 10.4, p_BH = 0.004; NiFe OR = 10.5, p_BH = 0.004; SR OR = 33.8, p_BH = 2.5×10⁻⁴; IR OR = 0.46, p_BH = 0.69; and nitrogenase OR = 5.4, p_BH = 0.035. [src: clay_confined_subsurface]

Within Bacillota_B, WL was present in 5/5 deep genomes versus 15/19 baseline genomes, with p = 0.54 and p_BH = 0.54 (1.0 as reported in the within-phylum table), while NiFe was present in 5/5 versus 14/19, also with p = 0.54 and p_BH = 0.54 (1.0 as reported). SR was present in 5/5 deep genomes versus 4/19 baseline genomes, with OR = ∞, p = 0.003, and p_BH = 0.044. Thus, only sulfate reduction survived the reported phylogenetic control as a deep-clay-associated signal; WL and NiFe primarily tracked the Bacillota_B lineage. [src: clay_confined_subsurface]

### Biosynthetic self-sufficiency was not elevated in the cultured deep cohort

GapMind amino-acid pathway completeness was measured across an 18-pathway universe. In the unfiltered comparison, anchor_deep had mean 16.22/18 versus 16.66/18 for the baseline, with Mann–Whitney p = 0.153 and Cohen’s d = −0.17. After the CheckM completeness filter of ≥80% completeness and ≤5% contamination, anchor_deep had mean 15.50/18 versus 17.14/18 for the baseline, with p = 0.009 and d = −0.84. Within Bacillota_B, the corresponding means were 16.50 versus 16.79, with p = 0.073 and d = −0.13. [src: clay_confined_subsurface]

Anchor_shallow instead showed higher completeness than the baseline: mean 17.87/18 versus 16.66/18 unfiltered, p = 0.006 and d = +0.52; and 17.87/18 versus 17.14/18 after filtering, p = 0.029 and d = +0.43. The report interprets this as consistent with cultivation-quality selection among agricultural isolates, while noting that the 18-pathway metric saturates near 18 for many cultured bacteria. [src: clay_confined_subsurface]

The negative deep-cohort result does not reject biosynthetic self-sufficiency as an adaptation in deep subsurface life; it indicates that the cultured KBase Data Lakehouse cohort does not contain the extreme self-sufficient lineages emphasized in the literature, which are often represented by MAGs or single-cell genomes. [src: clay_confined_subsurface]

### Cohort composition and cultivation bias constrain interpretation

After the stated CheckM quality filter, the cohort comprised anchor_deep 9 → 6 genomes, anchor_shallow 30 → 30 genomes, and soil_baseline 150 → 137 genomes. Anchor_deep included 8 Mont Terri Opalinus borehole genomes and 1 bentonite-formation genome; anchor_shallow included 8 Coalvale silty-clay genomes, 1 Cerrado clay genome, and 21 agricultural-clay genomes. The baseline was phylum-stratified across Pseudomonadota 50, Bacillota 40, Bacillota_B 20, Bacteroidota 20, and Actinomycetota 20 before the reported quality-filtered analyses. [src: clay_confined_subsurface]

The study applies only to cultivable porewater-cultured deep-clay isolates, not to the full Mont Terri or bentonite microbial communities. Rock-attached Geobacter and Geothrix lineages and CPR/DPANN episymbionts are essentially absent from the cultured cohort, so MAG-augmented work is required to test whether the complete clay-confined community follows the same patterns. [src: clay_confined_subsurface]

## Caveats

- The deep anchor cohort is small (n = 9 before quality filtering), so only large effects, described as Cohen’s d > 0.7 for unfiltered comparisons, are reliably detectable; marginal results such as the within-Bacillota_B self-sufficiency comparison at p = 0.07 are descriptive. [src: clay_confined_subsurface]
- Compartment annotations were inferred from keywords in isolation-source strings, so some bentonite or “rock” entries could plausibly be porewater or rock-attached; the H3 sulfate-reduction result was reported as robust to two stricter compartment definitions. [src: clay_confined_subsurface]
- The GapMind metric covers 18 amino-acid pathways and has limited resolving power near the upper end; the report proposes checking all standard amino-acid-biosynthesis EC numbers in eggNOG as a finer-grained sensitivity analysis. [src: clay_confined_subsurface]
- eggNOG cluster-level annotations propagate within ≥90% AAI clusters, so strain-level marker variants, including a single non-functional dsrA in an otherwise complete operon, may be missed. [src: clay_confined_subsurface]
- The report recommends adding deep-subsurface MAGs from Mont Terri, Olkiluoto, MX-80 bentonite, and Oak Ridge; comparing BRC-3 and BIC-A1 directly; applying the sulfate-reduction/iron-reduction diagnostic to other subsurface settings; resolving Bacillota_B differences at genus level; and linking genome presence to Bagnoud’s metaproteomic evidence. [src: clay_confined_subsurface]

## Slots Into

- [[concepts/subsurface-bacillota-specialization]] — The cohort-level anaerobic-toolkit signal is largely Bacillota_B-driven, while sulfate reduction remains enriched after within-phylum control. [src: clay_confined_subsurface]
- [[concepts/metabolic-model-gapfilling]] — GapMind pathway completeness provides a negative test of generalized biosynthetic self-sufficiency and identifies a ceiling effect requiring finer-grained pathway-completeness analyses. [src: clay_confined_subsurface]
