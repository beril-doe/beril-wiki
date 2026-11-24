---
type: "Concept"
description: "Whether genera with high metal-gene density have more co-occurrence partners, what those partners look like, and how far the signal is independent of niche breadth; stops at causal assembly mechanisms."
sources: ["summaries/comprehensive_metal_ecology__REPORT.md"]
---
# Co-occurrence network structure and metal-tolerance guilds

In one exploratory analysis, genera with higher metal-gene density had more significant positive co-occurrence partners in all three [[entities/microbeatlas]] strata. Soil genera that were rich in metal genes also had partners that were richer in metal genes, and those partners were enriched in Firmicutes. The evidence is correlational and comes from one report ([[summaries/comprehensive_metal_ecology__REPORT]]). The signal is correlated with niche breadth, and the report did not run the control that would separate the two. [src: comprehensive_metal_ecology]

## Literature Context

The candidate papers are mostly amplicon or metagenomic surveys of contaminated soils and related systems. They do not test whether genera with many metal-resistance genes have more co-occurrence partners. Their network results also point in different directions. In a comparison of contaminated and uncontaminated agricultural areas, the bacterial-fungal co-occurrence network was more complex in the contaminated area. It had more keystone taxa, and those taxa were completely different from the uncontaminated area's. The authors suggest that microorganisms adapt to long-term, moderate contamination through enhanced interactions [PMID 38800759](https://pubmed.ncbi.nlm.nih.gov/38800759/). In the Sedum alfredii phyllosphere, networks of the hyperaccumulating ecotype were more complex than those of the non-hyperaccumulating ecotype. The proportion of positive associations in the hyperaccumulator's bacterial networks rose with heavy metal concentration [PMID 40049897](https://pubmed.ncbi.nlm.nih.gov/40049897/). That comparison is between ecotypes, so it is not a pure exposure contrast. Against these, long-term mining-related contamination in northwestern China substantially reduced network complexity, with fewer nodes, edges and keystone taxa. The same study predicted more functions related to metal resistance and detoxification [PMID 42289642](https://pubmed.ncbi.nlm.nih.gov/42289642/). Metal exposure therefore does not simply make networks denser.

Several papers link metal tolerance to particular taxa or genes. Paddy soils along a Cu and Cd pollution gradient showed enrichment of metal-resistance genes. Chloroflexi lineages (AD3 and HSB_OF53-F07), Rokubacteriales and Nitrospira were identified as tolerant [PMID 37105465](https://pubmed.ncbi.nlm.nih.gov/37105465/). Paddy soils under long-term treated-wastewater irrigation showed co-occurrence of metal and antibiotic resistance genes, and Proteobacteria were the dominant hosts [PMID 37406708](https://pubmed.ncbi.nlm.nih.gov/37406708/). The other candidates cover chromium stress in a millet rhizosphere, biochar amendments, a synthetic consortium, zero-valent iron, and Zn in wetland fuel cells. They add little beyond the general point that stress and amendments reshape networks. Their abstracts do not address genus-level metal-gene density.

The corpus finding is that genera with higher metal-gene density had more significant positive partners in all three MicrobeAtlas strata. The PGLS β values were 138.4 for all samples, 134.0 for environmental samples and 210.5 for soil. This is largely novel, because none of these studies relates gene density to partner count across genera. It is also a different design: the corpus uses genus-level trait density in large survey networks, whereas the literature compares sites or ecotypes. The soil result, that metal-rich genera had partners richer in metal genes and enriched in Firmicutes (40.4% against 39.9% Proteobacteria in controls), is only loosely related to the literature. It is consistent with the idea of tolerant guilds in [PMID 37105465](https://pubmed.ncbi.nlm.nih.gov/37105465/). It differs in taxa from the Proteobacteria hosts in [PMID 37406708](https://pubmed.ncbi.nlm.nih.gov/37406708/), though that study concerns resistance-gene hosts in irrigated paddies, not co-occurrence partners.

The corpus signal is correlational, and it is correlated with niche breadth. The literature is also split on whether metal stress raises or lowers network complexity ([PMID 38800759](https://pubmed.ncbi.nlm.nih.gov/38800759/); [PMID 42289642](https://pubmed.ncbi.nlm.nih.gov/42289642/)). The corpus's non-causal, density-limited reading is therefore consistent with the field's uncertainty. It does not settle a mechanism for non-random assembly.

## Network setup

The report built MicrobeAtlas co-occurrence networks of 3,149–3,389 genera. It used hypergeometric tests (Veech 2013, FDR (false discovery rate) < 5%) and phi coefficients. [src: comprehensive_metal_ecology] The three strata were all samples (n = 462,716), environmental samples (n = 382,483) and soil samples (n = 162,022). [src: comprehensive_metal_ecology] The report regressed z-scored metal-gene KO (KEGG ortholog) density (`ko_per_mb_primary`) on the number of significant positive partners per genus. It used PGLS (phylogenetic generalized least squares). [src: comprehensive_metal_ecology]

## Do metal-rich genera have more partners?

Yes, in all three strata. The PGLS β was positive in each stratum: 138.4 (ALL), 134.0 (ENV) and 210.5 (SOIL). [src: comprehensive_metal_ecology] The report's summary quotes β = 138.4–210.5 with all p < 3.4×10⁻²². [src: comprehensive_metal_ecology]

| Stratum | n genera | β | SE | t | p | λ |
|---|---|---|---|---|---|---|
| ALL | 3,389 → 1,572 | 138.4 | 13.7 | 10.08 | 3.4×10⁻²³ | 0.599 [src: comprehensive_metal_ecology] |
| ENV | 3,382 → 1,572 | 134.0 | 13.8 | 9.74 | 8.5×10⁻²² | 0.625 [src: comprehensive_metal_ecology] |
| SOIL | 3,149 → 1,547 | 210.5 | 15.3 | 13.78 | 8.2×10⁻⁴¹ | 0.570 [src: comprehensive_metal_ecology] |

Metal-gene density was also associated with weighted phi-degree in all strata (β = 15.2–16.5, p = 3.5×10⁻³²–9.9×10⁻³²). [src: comprehensive_metal_ecology] It was associated with negative partners too (all β = 27–45, p = 1.6×10⁻⁵–2.2×10⁻⁴). [src: comprehensive_metal_ecology]

Soil showed the strongest positive effect (β = 210.5 against 138.4 for all samples). The report describes this as a 2.5× larger β than the all-sample stratum. That ratio does not match the two coefficients, which differ by about 1.5×. [src: comprehensive_metal_ecology] Soil also had the smallest negative-partner coefficient (soil sig_neg β = 27.4, all = 39.5, env = 45.3). [src: comprehensive_metal_ecology] The report links this to the primary soil enrichment (Finding 10; β = −0.033, p = 0.007). It suggests that metal-gene-rich genera sit in more cooperative, less competitive soil networks. [src: comprehensive_metal_ecology] That reading is an interpretation, not a direct test.

## Network density limits the interpretation

All three networks were extremely dense, with 38–42% significant positive pairs and a mean of at least 1,200 partners per genus. [src: comprehensive_metal_ecology] Clustering coefficients, betweenness centrality and MPD/SES analysis were therefore not possible, because these metrics become degenerate in near-complete networks. [src: comprehensive_metal_ecology] The positive-partner signal reflects relative enrichment within a near-saturated genus-level network. It does not show exclusive associations. Weighted phi-degree and partner count remain informative. [src: comprehensive_metal_ecology]

## What the partners look like in soil

The report compared the top-50 soil focal genera by `ko_per_mb_primary` (mean = 20.32 ko/Mb) with 50 phylum-matched controls of similar ko/Mb (±0.5 SD (standard deviation) of median = 7.95). [src: comprehensive_metal_ecology] Strong partners were defined as φ > 0.3. Only 0.91% of significant positive pairs passed this threshold, which the report reads as near-saturation for moderate associations. [src: comprehensive_metal_ecology]

Partners of focal genera had higher metal-gene density than partners of controls. [src: comprehensive_metal_ecology]

| Metric | Top-50 focal | Control-50 |
|---|---|---|
| Mean partner ko/Mb | 12.776 ± 3.884 | 8.903 ± 1.792 [src: comprehensive_metal_ecology] |
| Partners in top quartile | 56.1% | 26.3% [src: comprehensive_metal_ecology] |
| Dominant partner phylum | Firmicutes (40.4%) | Proteobacteria (39.9%) [src: comprehensive_metal_ecology] |

The difference in partner ko/Mb was significant (MWU (Mann-Whitney U) U = 2005, p = 1.98×10⁻⁷). [src: comprehensive_metal_ecology] Partner phylum distributions differed (χ² = 113.74, p = 2.77×10⁻¹³). [src: comprehensive_metal_ecology] Across all 100 genera, focal ko/Mb correlated with mean partner ko/Mb (Spearman ρ = 0.604, p = 2.82×10⁻¹¹). [src: comprehensive_metal_ecology]

The Firmicutes bias stands out because Proteobacteria make up 43% of genera in the full PGLS table. [src: comprehensive_metal_ecology] The report notes that Firmicutes such as Bacillus and Clostridium are well represented in metal-contaminated soils and carry large metal-resistance gene sets. It calls the pattern consistent with a metal-tolerance guild, in which genera that invest heavily in metal processing co-occur with similarly adapted neighbours. [src: comprehensive_metal_ecology] The report also suggests the Firmicutes bias indicates non-random assembly. [src: comprehensive_metal_ecology]

The guild is not strictly assortative. Within the top 50, the focal–partner correlation was weaker (ρ = 0.284, p = 0.045) than across all 100 genera (ρ = 0.604). Some high-KO focal genera still associate with lower-KO partners. [src: comprehensive_metal_ecology]

## Independence from niche breadth

The signal is not independent of niche breadth. B_std correlated with positive partner count (Spearman ρ = 0.33–0.37, p < 10⁻⁴⁰), and the primary P1 predictor is niche breadth. [src: comprehensive_metal_ecology] Partial analyses controlling for B_std are needed before the co-occurrence signal can be called independent of the primary specialisation axis. [src: comprehensive_metal_ecology] The report proposes regressing partner count on KO density with B_std as a covariate, to learn whether the signal is independent of niche breadth or mediated by it. [src: comprehensive_metal_ecology] It also proposes comparing mean focal-genus-to-partner phylogenetic distances with a random null from the same network, to test whether the guild is phylogenetically structured. [src: comprehensive_metal_ecology] Neither analysis is in the report.

## Open Directions

- Regress partner count on KO density with B_std as a covariate in each stratum. This would show whether the signal is independent of niche breadth or mediated by it.
- Compute mean phylogenetic distance between focal genera and their partners against a random null from the same network. This would test whether the guild is phylogenetically structured.
- Repeat the partner characterisation with a stricter or rank-based edge threshold. This would address the near-saturated networks, where the φ > 0.3 filter keeps only 0.91% of pairs.
- Test whether the Firmicutes partner bias holds when focal genera are matched to controls on niche breadth as well as phylum.
