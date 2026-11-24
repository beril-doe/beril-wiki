---
type: "Concept"
description: "Whether apparent enrichment of anaerobic markers (Wood–Ljungdahl, [NiFe]-hydrogenase, sulfate reduction) in deep habitats survives control for phylum composition; covers the deep clay cohort versus soil baseline."
sources: ["summaries/bacillota_b_subsurface_accessory__REPORT.md", "summaries/clay_confined_subsurface__REPORT.md", "summaries/discoveries.md"]
---
# Phylum-level confounding of habitat-specific anaerobic gene content

This page asks whether the enrichment of anaerobic markers (Wood–Ljungdahl, group 1 [NiFe]-hydrogenase, sulfate reduction (SR)) in deep clay isolates survives control for phylum. In the clay_confined_subsurface report it mostly does not: Wood–Ljungdahl and [NiFe]-hydrogenase track the [[entities/bacillota-b]] lineage, and only sulfate reduction stays enriched within phylum. [src: clay_confined_subsurface]

## Literature Context

The candidate papers are mostly metagenomic or isolate descriptions of deep and anoxic habitats. None of them tests whether habitat enrichment of anaerobic markers survives control for phylum. They give context on which lineages carry these traits in deep environments.

A 2.6 km deep Siberian thermal aquifer was anoxic and dominated by sulfate-reducing Firmicutes and Deltaproteobacteria. It also held uncultured Chloroflexi, Ignavibacteriae and Aminicenantes. A Chloroflexi bacterium in that aquifer had the Wood-Ljungdahl pathway [PMID 30101334](https://pubmed.ncbi.nlm.nih.gov/30101334/). That fits the idea that a few lineages carry the pathway in deep settings. It is a metagenome with 25 genomes of more than 90% completeness, so it does not compare habitats. In Gulf of Mexico seep sediments, deep-biosphere taxa such as Atribacteria, Aminicenantes and Thermoprofundales were enriched in gas-positive sediments. They were predicted to be anaerobic heterotrophs, and the authors link this to upward dispersal from the subsurface [PMID 32354993](https://pubmed.ncbi.nlm.nih.gov/32354993/). Taxon identity shaped the community there, which parallels the phylum-composition issue. A Scotian Basin seep study found that anaerobic hydrocarbon oxidizers were not necessarily tied to sulfate reduction [PMID 33203858](https://pubmed.ncbi.nlm.nih.gov/33203858/). Other work describes a deep-subsurface clostridial family in anaerobic glycine betaine metabolism [PMID 31464644](https://pubmed.ncbi.nlm.nih.gov/31464644/). It also reports a hydrogen-producing anaerobe isolated from deep shale groundwater [PMID 40465470](https://pubmed.ncbi.nlm.nih.gov/40465470/). Both show that anaerobic traits are spread across several lineages in deep habitats. Crystal Geyser and Colorado River aquifer metagenomes likewise show deep fluids populated by many lineages with hydrogen and anaerobic carbon metabolism [PMID 25727367](https://pubmed.ncbi.nlm.nih.gov/25727367/), [PMID 25702576](https://pubmed.ncbi.nlm.nih.gov/25702576/).

The corpus finding is that in the deep clay cohort, Wood-Ljungdahl and [NiFe]-hydrogenase enrichment against soil baseline (odds ratios of 10.4 and 10.5) disappears within Bacillota_B (5/5 vs 15/19 and 5/5 vs 14/19, BH-adjusted p=1.0). Only sulfate reduction stays enriched within phylum (5/5 vs 4/19, p_BH=0.04). This is consistent with the literature above, where deep anoxic communities are shaped by particular taxa, including sulfate-reducing Firmicutes [PMID 30101334](https://pubmed.ncbi.nlm.nih.gov/30101334/). It extends that picture with an explicit within-phylum control, which the candidate papers do not run. The within-phylum sulfate-reduction result is small (n=5 vs 19) and sits near the significance threshold. The candidate papers neither confirm nor contradict it.

The phylum-controlled comparison of habitat against soil baseline appears novel relative to these candidates. The clay conclusion is also limited to one cohort of 9 deep isolates.

## Cohort-level signal

Deep-confined clay isolates look strongly enriched at cohort level. Mean toolkit score (of 3 modules) is 1.89 in deep clay, 0.39 in soil baseline and 0.03 in shallow clay. [src: clay_confined_subsurface] The underlying table lists anchor_deep n=9 (toolkit mean 1.889), anchor_shallow n=30 (0.033) and soil_baseline n=140 (0.393). [src: clay_confined_subsurface]

Per-marker tests against soil baseline used Fisher's exact test with BH-FDR (Benjamini-Hochberg false discovery rate) adjustment; see [[entities/fisher-s-exact-test-with-benjamini-hochberg-fdr]]. [src: clay_confined_subsurface] All three markers were highly significant: Wood–Ljungdahl OR=10.4, p_BH=0.004 [src: clay_confined_subsurface]; [NiFe]-hydrogenase OR=10.5, p_BH=0.004 [src: clay_confined_subsurface]; sulfate reduction OR=33.8, p_BH=2×10⁻⁴. [src: clay_confined_subsurface] The detailed table gives the sulfate-reduction p_BH as 2.5×10⁻⁴, while the summary sentence gives 2×10⁻⁴ for the same test; the report states both. [src: clay_confined_subsurface] The detailed counts are:

| Marker | Deep | Baseline | OR | p_BH |
|---|---|---|---|---|
| WL_complete | 5/9 | 15/140 | 10.4 | 0.004 [src: clay_confined_subsurface] |
| NiFe_complete | 7/9 | 35/140 | 10.5 | 0.004 [src: clay_confined_subsurface] |
| SR_complete | 5/9 | 5/140 | 33.8 | 2.5×10⁻⁴ [src: clay_confined_subsurface] |

Two other modules differ. IR_complete was not enriched (1/9 vs 30/140, OR=0.46, p_BH=0.69). [src: clay_confined_subsurface] Nif_complete was enriched (4/9 vs 18/140, OR=5.4, p_BH=0.035). [src: clay_confined_subsurface] OR is odds ratio. The [[entities/wood-ljungdahl-pathway]] and [[entities/group-1-nife-hydrogenase]] results are the ones tested for confounding below. The discoveries digest describes the cohort signal as looking like a strong deep-clay versus soil signal. [src: discoveries]

## Phylum confound

Within-phylum control shows a confound. Bacillota_B contains Desulfosporosinus, BRH-c4a and BRH-c8a, the lineages that dominate the deep anchor cohort. [src: clay_confined_subsurface] Even in soil baseline, Bacillota_B carries Wood–Ljungdahl and [NiFe]-hydrogenase at high rates, with toolkit mean 1.65. [src: clay_confined_subsurface, discoveries] See also [[entities/desulfosporosinus]].

Within Bacillota_B, deep versus baseline comparisons for the two markers are not significant:

- Wood–Ljungdahl: 5/5 vs 15/19, p=0.54, BH-adjusted p=1.0. [src: clay_confined_subsurface, discoveries]
- [NiFe]-hydrogenase: 5/5 vs 14/19, p=0.54, BH-adjusted p=1.0. [src: clay_confined_subsurface, discoveries]

The report concludes that these markers track the Bacillota_B lineage, not deep-clay habitat per se. [src: clay_confined_subsurface]

Sulfate reduction (dsrAB-aprAB-sat) is the exception. Within Bacillota_B, 5/5 deep isolates carry it versus 4/19 baseline isolates (OR=∞, p=0.003, p_BH=0.04). [src: clay_confined_subsurface, discoveries] See [[entities/dissimilatory-sulfate-reduction-pathway]].

## Interpretation

The report calls the cohort-level enrichment (1.89 vs 0.39) real but mostly Bacillota_B-driven. [src: clay_confined_subsurface] It interprets the pattern as a phylum-level signature picked up by habitat sampling, not an in-situ adaptation beyond what phylum congeners already encode. [src: clay_confined_subsurface] In its explanation, sampling clay-confined habitats over-samples toolkit-carrying lineages (Bacillota_B Desulfotomaculales, Desulfitobacteriales). [src: clay_confined_subsurface] This is an interpretation, not a direct test. The report says it is consistent with Beaver & Neufeld (2024), who predicted that Bacillota dominate deeper isolated fluids partly because they favor the Wood–Ljungdahl pathway and form spores. [src: clay_confined_subsurface] Both the report and the digest present this as a methodological warning: phylum control changes which signals survive, and a habitat signal may be a phylum signature from biased sampling. [src: clay_confined_subsurface, discoveries]

## Related accessory-gene evidence

A separate report compared deep-clay Bacillota_B anchors with soil-baseline congeners (see [[concepts/accessory-gene-content-enrichment-in-subsurface-lineages-relative-to-soil-congeners]]). Among enriched ortholog groups (OGs), 42 were classed as anaerobic respiration, with hits including hydrogenase, cytochrome, sulfite, sulfate, nitrate, fumarate reductase, NADH dehydrogenase, oxidoreductase and menaquinone. [src: bacillota_b_subsurface_accessory] A manual look at the top 15 enriched OGs found further anaerobic-respiration and electron-transfer hits. [src: bacillota_b_subsurface_accessory] Separately, COG1977 (Mo-molybdopterin cofactor metabolic process) was present in 10/10 anchor genomes versus 11/62 baseline genomes. [src: bacillota_b_subsurface_accessory] That report reads its enriched categories as matching Beller's Pelosinus HCF1 gene-content snapshot at population scale. [src: bacillota_b_subsurface_accessory]

## Caveats

- eggNOG annotations propagate within ≥90% AAI clusters, so strain-level variants, such as a single non-functional dsrA in an otherwise complete operon, may be missed. [src: clay_confined_subsurface]
- The 5/5 Bacillota_B SR enrichment (n=5 vs 19) may hide finer structure, because Desulfosporosinus, BRH-c8a and BRH-c4a may differ in their non-SR features. [src: clay_confined_subsurface]

## Open Directions

- Run the proposed within-phylum deep-clay versus soil comparisons for Bacteroidota, Pseudomonadota and Acidobacteriota. This would show whether the functional signal generalizes or is Bacillota_B-specific.
- Run a genus-level Bacillota_B pangenome analysis (Desulfosporosinus, BRH-c8a, BRH-c4a). It would resolve the granularity hidden by n=5 vs 19 and could surface a deep-clay-specific accessory genome.
- Check the sulfate-reduction result with operon-level or strain-level marker checks, for example for non-functional dsrA. This would address the cluster-level annotation propagation caveat.
- Add more deep Bacillota_B genomes. The 5/5 vs 4/19 result, with p_BH=0.04, is near the threshold.
