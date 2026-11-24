---
type: "Concept"
description: "Per-orthogroup enrichment tests contrasting deep subsurface (clay borehole/porewater) genomes with phylum-matched soil genomes, including functional categories of enriched OGs; stops at genome-size questions."
sources: ["summaries/bacillota_b_subsurface_accessory__REPORT.md"]
---
# Accessory gene-content enrichment in subsurface lineages relative to soil congeners

This page covers per-orthogroup (OG) enrichment tests that contrast deep subsurface clay borehole/porewater genomes with phylum-matched soil genomes. All the evidence comes from one report on Bacillota_B, so the findings are single-lineage results. In that report, 547 OGs were enriched in the deep-clay anchor, and the report treats this as strong support for its hypothesis H1 (predicted ≥10 enriched OGs). [src: bacillota_b_subsurface_accessory] The functional categories rest on keyword scanning, which the report says undercounts anaerobic-niche signal. [src: bacillota_b_subsurface_accessory] See [[summaries/bacillota_b_subsurface_accessory__REPORT]] and [[entities/bacillota-b]].

## Enrichment test and result

The test was a per-OG Fisher's exact test on 14,109 Firmicutes-level eggNOG OGs, with 10 anchor genomes and 62 baseline genomes. It used Benjamini-Hochberg false discovery rate (BH-FDR) correction, q<0.05, fold-difference≥3, and ≥3 positive anchor genomes. [src: bacillota_b_subsurface_accessory] See [[entities/fisher-s-exact-test-with-benjamini-hochberg-fdr]]. The result was 547 anchor-enriched OGs and 27 anchor-depleted OGs. [src: bacillota_b_subsurface_accessory] The top hits had odds ratio (OR)=∞, with 7–10 anchor genomes positive and 0 baseline genomes positive. [src: bacillota_b_subsurface_accessory] The report calls the 547 annotated OGs a target list for future biochemistry, fitness-screen and cultivation work. [src: bacillota_b_subsurface_accessory] It also claims this is the first quantitative gene-cluster-level characterization of subsurface Bacillota_B specialization, going beyond the curated marker dictionary of the clay_confined_subsurface project. [src: bacillota_b_subsurface_accessory]

## Functional categories of enriched OGs

Most enriched OGs fall in the "other / unannotated" bucket. Among the pre-registered categories, anaerobic respiration is the largest. Categories were assigned by keyword-scanning eggNOG Description/Preferred_name and bakta gene/product text. [src: bacillota_b_subsurface_accessory]

| Category | Enriched OGs | Example hits |
|---|---|---|
| anaerobic respiration | 42 | hydrogenase, cytochrome, sulfite, sulfate, nitrate, fumarate reductase, NADH dehydrogenase, oxidoreductase, menaquinone [src: bacillota_b_subsurface_accessory] |
| sporulation revival | 24 | spore, germination, gerA/gerB, safA, cwlJ, spoVA, cot [src: bacillota_b_subsurface_accessory] |
| mineral attachment / EPS | 12 | exopolysaccharide, biofilm, capsule, pilin, adhesin [src: bacillota_b_subsurface_accessory] |
| anaerobic regulators | 4 | sigma factor, sigF, sigE, two-component, response regulator [src: bacillota_b_subsurface_accessory] |
| osmoadaptation | 3 | betaine, ectoine, osmoprotectant, K⁺ uptake [src: bacillota_b_subsurface_accessory] |
| other / unannotated | 462 | hypothetical, DUFs, generic regulators [src: bacillota_b_subsurface_accessory] |

The report reads the anaerobic respiration, regulator and sporulation categories as matching Beller's Pelosinus HCF1 gene-content snapshot at population scale. [src: bacillota_b_subsurface_accessory] It reads the sporulation hits as replicating Vandieken 2017's description of Baltic Sea subsurface Desulfosporosinus as spore-forming with broad respiratory versatility. [src: bacillota_b_subsurface_accessory] Three Desulfosporosinus genomes in the anchor contributed to the sporulation-OG signal. [src: bacillota_b_subsurface_accessory] See [[entities/desulfosporosinus]].

### Individual OGs found by manual inspection

Manual inspection of the top 15 enriched OGs by p_BH found additional anaerobic-respiration and electron-transfer hits. [src: bacillota_b_subsurface_accessory]

- COG1977 (Mo-molybdopterin cofactor metabolic process, EC 2.8.1.12; EC is Enzyme Commission) occurred in 10/10 anchor versus 11/62 baseline genomes. [src: bacillota_b_subsurface_accessory] The report notes that molybdopterin is the cofactor for nitrate reductase, formate dehydrogenase and DMSO reductase. [src: bacillota_b_subsurface_accessory] It calls recovery in 100% of anchor genomes a strong subsurface-niche signal. [src: bacillota_b_subsurface_accessory]
- OG 1UIFM, the DsrE/DsrF/DsrH-like family, occurred in 7/10 anchor versus 0/62 baseline genomes. [src: bacillota_b_subsurface_accessory] The report describes DsrEFH as the intracellular sulfite-handling complex coupled to dissimilatory sulfite reductase. It says the anchor-specific recovery extends the clay project's sulfate reduction finding to a tighter dsr-pathway component. [src: bacillota_b_subsurface_accessory]
- OG 1VFGN (4Fe-4S dicluster, EC 1.2.7.3, 2-oxoglutarate:ferredoxin oxidoreductase) occurred in 8/10 anchor versus 4/62 baseline genomes. [src: bacillota_b_subsurface_accessory]
- OG 1V0WU (KEGG K08177 Major Facilitator Superfamily transporter) occurred in 9/10 anchor versus 5/62 baseline genomes and is likely an osmoprotectant or solute uptake transporter. [src: bacillota_b_subsurface_accessory]

## Caveats

Keyword categorization undercounts the real signal. The scanner missed many anaerobic-niche signals because they are encoded by gene-family or domain names rather than the pre-registered keywords. [src: bacillota_b_subsurface_accessory] The 462-OG other bucket contains real anaerobic-respiration and electron-transfer signal. [src: bacillota_b_subsurface_accessory] It includes COG1977, DsrEFH and 2-oxoglutarate ferredoxin oxidoreductase, and the report proposes an LLM-based pass over eggNOG Description and bakta product text to fix the counts. [src: bacillota_b_subsurface_accessory] The report estimates that, after manual reclassification, the H1-relevant total is closer to 80–100 of 547, above the scanner's 42. [src: bacillota_b_subsurface_accessory] See [[concepts/limits-of-keyword-and-marker-based-functional-annotation]].

Cohort size and phylogeny also limit the result:
- Fisher's exact is adequate for large effects, and the report considers the 547 OGs robust. Marginal effects with anchor counts of 3–5 should be treated descriptively. [src: bacillota_b_subsurface_accessory]
- The 10-genome anchor is genus-clumped: 3 BRH-c8a, 2 BRH-c4a, 2 Desulfosporosinus, Desulforudis, Ch130 and 1 other. [src: bacillota_b_subsurface_accessory]
- Four orders (Desulfotomaculales, Desulfitobacteriales, Ammonifexales, Thermacetogeniales) partly mitigate genus-level confounding, but do not eliminate it. [src: bacillota_b_subsurface_accessory] See [[concepts/small-cohort-and-phylogenetic-confounding-in-lineage-level-comparisons]].
- The anchor is borehole/porewater-dominated by construction, so the comparison cannot test whether rock-attached Bacillota_B differs in gene content. [src: bacillota_b_subsurface_accessory] See [[concepts/cultivation-bias-toward-porewater-versus-rock-attached-subsurface-communities]].

The report proposes follow-up work for these limits. A per-genus H1 analysis would separate genus-specific lineage markers from OGs recurrent across several subsurface-specialist genera. [src: bacillota_b_subsurface_accessory] With n=10 this is at the limit of statistical resolution, and more clay-isolated Bacillota_B from BacDive linkage or future KBase Data Lakehouse pangenome ingests would improve power. [src: bacillota_b_subsurface_accessory] It also proposes retargeting the NB01–04 pipeline to within-Bacteroidota, within-Pseudomonadota and within-Acidobacteriota comparisons, to test whether the signal generalizes beyond Bacillota_B. [src: bacillota_b_subsurface_accessory]

## Open Directions

- Run the per-genus H1 analysis, adding clay-isolated Bacillota_B genomes to raise power. This would identify which of the 547 OGs recur across genera and which are lineage-marker noise.
- Run an LLM-based pass over the 462-OG other bucket. This would test the estimate of 80–100 H1-relevant OGs.
- Retarget the NB01–04 pipeline to Bacteroidota, Pseudomonadota and Acidobacteriota. This would show whether the functional-category signal is specific to Bacillota_B.
- Add rock-attached genomes to the anchor, if they become available. This would close the porewater-bias gap.
