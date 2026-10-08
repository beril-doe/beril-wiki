---
type: "Summary"
description: "Summary of a comparison of 10 deep-clay and 62 soil-baseline Bacillota_B genomes that finds 547 anchor-enriched orthologous groups and larger deep-clay genomes, and that corrects the clay project's iron-reduction marker analysis."
doc_type: "short"
full_text: "sources/bacillota_b_subsurface_accessory__REPORT.md"
---
# Subsurface Bacillota_B Specialization — What Distinguishes Deep-Clay Lineages from Soil Congeners?

## Overview

This report compares 10 deep-clay Bacillota_B genomes with 62 soil-baseline Bacillota_B genomes using eggNOG orthologous-group (OG) enrichment, genome-content statistics, and a corrected multi-heme cytochrome detector. It identifies 547 significantly enriched OGs, finds that deep-clay genomes are larger rather than streamlined, and revises the clay-project iron-reduction comparison after detecting mismatched marker KOs. The report's four-panel synthesis figure is stored at figures/summary_figure.png. [src: bacillota_b_subsurface_accessory]

## Key Findings

### 1. Deep-clay genomes are enriched for anaerobic-niche and persistence functions

Per-OG Fisher’s exact tests across 14,109 eggNOG OGs (Firmicutes-level where available, with Bacteria/root-level fallbacks otherwise), comparing anchor n=10 with baseline n=62 and applying Benjamini–Hochberg false-discovery-rate correction, a fold-difference threshold of ≥3, and a minimum of ≥3 anchor genomes positive, identified 547 enriched OGs at q<0.05. This exceeded the preregistered H1 prediction of ≥10 and was strongly supported. The same screen identified 27 anchor-depleted OGs, and the top enriched hits had an odds ratio (OR) of ∞, with 7–10 anchor genomes positive versus 0 baseline genomes. [src: bacillota_b_subsurface_accessory]

The keyword-scanned enriched set included 42 anaerobic-respiration OGs, 24 sporulation-revival OGs, 12 mineral-attachment or exopolysaccharide OGs, 4 anaerobic-regulator OGs, 3 osmoadaptation OGs, and 462 other or unannotated OGs. Example annotations included hydrogenase, cytochrome, sulfite, sulfate, nitrate, fumarate reductase, NADH dehydrogenase, oxidoreductase, menaquinone, spore and germination functions, biofilm and capsule functions, sigma factors, two-component systems, betaine, ectoine, osmoprotectants, and K⁺ uptake. [src: bacillota_b_subsurface_accessory]

Manual inspection showed that the 462-OG “other” category undercounted anaerobic-respiration and electron-transfer functions. The report attributes this to the preregistered keyword scan missing signals that are encoded by gene-family or domain names rather than by the preregistered keywords. The additional hits came from manual inspection of the top 15 enriched OGs ranked by p_BH. COG1977, associated with molybdopterin cofactor metabolism, occurred in 10/10 anchors versus 11/62 baselines. The report reads this as a strong subsurface-niche signal because molybdopterin is the cofactor for anaerobic-respiration enzymes such as nitrate reductase, formate dehydrogenase and DMSO reductase; OG 1UIFM, a DsrE/DsrF/DsrH-like family belonging to the intracellular sulfite-handling complex coupled to dissimilatory sulfite reductase, occurred in 7/10 anchors versus 0/62 baselines, which the report reads as extending the clay project's SR finding to a tighter dsr-pathway component; OG 1VFGN, a 4Fe–4S dicluster associated with 2-oxoglutarate:ferredoxin oxidoreductase, occurred in 8/10 anchors versus 4/62 baselines; and OG 1V0WU, a Major Facilitator Superfamily transporter (KEGG K08177), occurred in 9/10 anchors versus 5/62 baselines and is proposed, but not shown, to be an osmoprotectant or solute-uptake transporter. The report estimates that, with manual reclassification of the “other” category, the H1-relevant total would be well above the keyword scanner's 42 and closer to 80–100 of the 547 enriched OGs; this is an estimate, not a finalized count. [src: bacillota_b_subsurface_accessory]

### 2. Deep-clay Bacillota_B genomes are larger and contain more OGs

The H2 prediction that deep-clay genomes would be smaller was rejected in the opposite direction: deep-clay Bacillota_B genomes were significantly larger than soil-baseline genomes, which the report summarizes as a 35% mean size difference with ~25% more eggNOG OGs per genome. The report also describes anchor genomes as ~1 Mbp larger than baseline genomes. Deep-clay anchor genomes had a mean genome size of 4,110,038 bp versus 3,046,124 bp for soil-baseline genomes, with Cohen’s d=+1.39 and Mann–Whitney p=0.025. CheckM-rescaled genome sizes were 4,323,230 bp versus 3,233,715 bp, with Cohen’s d=+1.37 and p=0.013. [src: bacillota_b_subsurface_accessory]

Mean GC content was 48.84% in anchors versus 47.76% in baseline genomes, with Cohen’s d=+0.21 and p=0.44. Mean eggNOG OG counts were 2,630 versus 2,106, with Cohen’s d=+1.30 and p=0.022; CheckM-rescaled OG counts were 2,771 versus 2,233, with Cohen’s d=+1.32 and p=0.009. [src: bacillota_b_subsurface_accessory]

Mean CheckM completeness was effectively identical between cohorts at 94.7% for anchors and 94.3% for baseline genomes, with Cohen’s d=+0.08 and p=0.93. The report therefore concludes that the larger anchor genomes and higher OG counts cannot be explained by a genome-quality artifact. [src: bacillota_b_subsurface_accessory]

The H2 prediction that deep-clay genomes would be smaller was rejected in the opposite direction: all four size and OG-count metrics indicated significantly larger anchor genomes, with p≤0.025 and Cohen’s d≥+1.30. The report contrasts this gene-content expansion with Tian et al. (2020)'s "small is mighty" streamlining finding, but notes that Tian's claim was specific to the Patescibacteria/CPR superphylum (≤1 Mbp genomes, episymbiotic lifestyle), whereas cultivable Bacillota_B are free-living anaerobic Firmicutes in a different subsurface niche. It presents the expansion as consistent with Beaver & Neufeld (2024)'s self-sufficiency hypothesis and with Becraft et al. (2021)'s account of *Ca.* Desulforudis audaxviator, whose genome GB_GCA_020725505.1 is in the anchor cohort and retains full N-fixation, amino-acid biosynthesis and C-fixation; the self-sufficiency link is an interpretation drawn from the literature, not a direct test in this project. [src: bacillota_b_subsurface_accessory]

### 3. Corrected multi-heme cytochrome detection removes the original iron-reduction contrast

The clay-confined-subsurface project’s original iron-reduction analysis used K07811, K17324, and K17323 as markers, although the report identifies these as TMAO reductase (threshold 1336.87), glycerol ABC ATP-binding (threshold 363.93), and glycerol ABC permease (threshold 318.27) genes rather than iron-reduction markers; KEGG has no canonical KO for the Geobacter omcS / Shewanella mtr multi-heme outer-surface cytochromes, so the clay project (PR #231) unknowingly substituted unrelated genes. The report attributes the earlier "Mitzscherling rock-attached signature in shallow clay" framing to these mismatched gene IDs combined with the standard eggNOG-mapper threshold, which filters on sequence similarity rather than KO biological identity. The corrected detector combined PFAM PF02085 (Cytochrom_CIII multi-heme c-type), PFAM PF22678 (Cytochrom_c_NrfB-like multi-heme nitrite reductase), and a CXXCH heme-binding motif count of ≥4 in gene_cluster.faa_sequence protein sequences; a genome was positive if any signal was present. [src: bacillota_b_subsurface_accessory]

In the corrected comparison, anchor_deep (Mont Terri Opalinus + bentonite, n=9) had 5/9 positive genomes, or 55.6%, versus 1/9, or 11.1%, under the original marker set. Anchor_shallow (Coalvale + Cerrado + agricultural, n=30) had 12/30, or 40.0%, versus 15/30, or 50.0%, originally. Soil_baseline (n=149) had 61/149, or 40.9%, versus 30/149, or 20.1%, originally. [src: bacillota_b_subsurface_accessory]

Corrected pairwise Fisher tests found no significant cohort differences: deep versus shallow had odds ratio 1.88 and p=0.46; deep versus baseline had odds ratio 1.80 and p=0.49; and shallow versus baseline had odds ratio 0.96 and p=1.0. The original clay-project analysis had shown shallow >> deep (50% vs 11%), whereas with the corrected detector shallow (40%) is lower than deep (56%) and the difference is not statistically significant; the original shallow-enrichment narrative therefore loses statistical support, while corrected multi-heme cytochrome content is similar across the clay cohorts and soil baseline. [src: bacillota_b_subsurface_accessory]

The clay project’s sulfate-reduction (SR) side finding remains supported because its SR markers (K11180, K11181, K00394, K00395, K00958) were correctly identified: 5/9 deep-cohort genomes were positive versus a Mitzscherling rock-attached null rate of 0.2%, with binomial p=4×10⁻¹². The report consequently considers the clay-project porewater-bias headline supported through SR alone, and the "Mitzscherling rock-attached vs Bagnoud porewater" framing half-supported (SR side) and half-unsupported (iron-reduction side, after marker correction). [src: bacillota_b_subsurface_accessory]

### 4. Cohort, pangenome, and marker-availability context

The Bacillota_B universe contained 334 genomes in the KBase Data Lakehouse pangenome, substantially fewer than the v1.1 plan’s estimate of 6,700. The generated data/bacillota_b_universe.tsv file of all Bacillota_B genomes is listed with 314 rows, and the report does not reconcile that count with the 334 total. The anchor_deep_clay cohort comprised 10 genomes: 5 from the Mont Terri Opalinus borehole (Desulfosporosinus, BRH-c8a×2, BRH-c4a, and 1 metagenomic Desulfosporosinus), 3 Mont Terri rock-porewater MAGs (metagenome-assembled genomes), and 2 from the Russian Beyelii Yar borehole (*Ca.* Desulforudis audaxviator and Ch130 Thermacetogeniaceae); the soil_baseline cohort comprised 62 phylum-matched soil or sediment genomes spanning Syntrophomonadales 29, Desulfitobacteriales 16, Moorellales 6, Thermacetogeniales 4, Ammonifexales 2, Carboxydocellales 2, Desulfotomaculales 1, Heliobacteriales 1, and Thermincolales 1. [src: bacillota_b_subsurface_accessory]

Within Bacillota_B, PF02085 had 4 hits in 4 clusters, PF00034 had 1 hit in 1 cluster, PF13442 had 1 hit in 1 cluster, PF22678 had 1 hit in 1 cluster, and PF14537 had 0 hits in 0 clusters. The report confirms PF14537 as silently absent, matching a documented plant_microbiome_ecotypes pitfall. Multi-heme cytochrome PFAMs were sparse within Bacillota_B, with only ~6 clusters across all four PFAMs, so CXXCH motif counting on gene_cluster.faa_sequence carried most of the corrected iron-reduction signal; this is why the corrected rates (40–56%) are far higher than PFAM-only detection would yield. [src: bacillota_b_subsurface_accessory]

### 5. Literature concordance

The report states that the H1 functional categories align with Beller 2012's *Pelosinus* HCF1, a single subsurface aquifer Firmicute carrying 2 [NiFe] + 4 [FeFe] hydrogenases plus dissimilatory N-oxide reductase, Cr/Fe reductase and a methylmalonyl-CoA pathway; the anchor-enriched categories (anaerobic respiration, regulators, sporulation) are described as matching that gene-content snapshot at population scale. This is a literature comparison, not a direct analysis of *Pelosinus*. [src: bacillota_b_subsurface_accessory]

The report also states that the H1 sporulation-revival hits replicate Vandieken 2017's (PMID 28646634) characterization of Baltic Sea subsurface *Desulfosporosinus* species as spore-forming with broad respiratory versatility, and that 3 anchor *Desulfosporosinus* genomes contributed to the sporulation-OG signal. The report's cohort composition and confounding caveat list 2 *Desulfosporosinus* genomes; the source does not reconcile the two counts. [src: bacillota_b_subsurface_accessory]

## Caveats

The anchor cohort contains 10 genomes and the baseline contains 62. Fisher’s exact testing is considered adequate for the large 547-OG effect, but marginal effects supported by anchor counts of 3–5 should be treated descriptively rather than inferentially. Spanning four orders (Desulfotomaculales, Desulfitobacteriales, Ammonifexales, Thermacetogeniales) only partly mitigates genus-level phylogenetic confounding. [src: bacillota_b_subsurface_accessory]

The anchor cohort is borehole- and porewater-dominated by construction, reflecting cultivation bias toward porewater isolates. The comparison therefore cannot test whether rock-attached Bacillota_B differ in gene content. The 10-genome anchor was assembled ~entirely from `ncbi_env` keyword search. BacDive expansion through the kescience_bacdive isolation and taxonomy tables yielded zero additional Bacillota_B genomes in this run. [src: bacillota_b_subsurface_accessory]

Genus-level phylogenetic confounding is only partly mitigated: the cohort spans four orders, but the 10-genome anchor is clumped among 3 BRH-c8a genomes, 2 BRH-c4a genomes, 2 Desulfosporosinus genomes, Desulforudis, Ch130, and 1 other genome. Some enriched OGs may therefore be lineage markers rather than recurrent subsurface-specialization features. The report states that a per-genus analysis is needed to separate genus-specific lineage-marker OGs from OGs that recur across multiple subsurface-specialist genera. It also states that with n=10 anchor genomes such a decomposition is at the limit of statistical resolution. [src: bacillota_b_subsurface_accessory]

The OG hierarchy is imperfect. The analysis used Firmicutes-level OGs (eggNOG tax 1239) where available and Bacteria/root fallbacks otherwise; some enriched OGs are at root level, which is coarse. A Bacillota_B-specific eggNOG tier was unavailable because Bacillota_B is GTDB-defined while eggNOG uses NCBI taxonomy, where Bacillota_B genomes are spread across Firmicutes / Negativicutes / Tissierellia at the legacy class level. [src: bacillota_b_subsurface_accessory]

Keyword-based functional categorization undercounted relevant functions: the 462-OG “other_or_unannotated” group contained substantial anaerobic-respiration and electron-transfer signal, including COG1977 molybdopterin metabolism, DsrEFH-like proteins, and 2-oxoglutarate:ferredoxin oxidoreductase. Manual reclassification or an LLM-based extractor would be needed to refine category counts. [src: bacillota_b_subsurface_accessory]

The corrected iron-reduction analysis is considered robust for the multi-heme cytochrome signal but is a Phase 1 correction. It does not fully determine whether the original clay-project comparison with the Bagnoud porewater pattern should be retained; the SR side remains robust, whereas the iron-reduction side loses force. A planned amendment to the clay-project report would clarify that the iron-reduction side of the clay project's H3 finding is artefactual and that the SR side stands. The report presents this amendment as pending, not as already applied. [src: bacillota_b_subsurface_accessory]

The report proposes applying the correction to the clay-project branch, refining the 462-OG category with an LLM-based scan, decomposing the H1 signal by genus, and seeking BacDive linkage to additional clay-isolated Bacillota_B. It also proposes localizing the functions responsible for the larger anchor genomes through a COG / KEGG-pathway breakdown of the "extra" gene fraction. Finally, it proposes testing the same enrichment framework in other phylum-matched subsurface comparisons. Whether the H1 functional-category signal generalizes beyond Bacillota_B or is Bacillota_B-specific therefore remains untested. [src: bacillota_b_subsurface_accessory]

## Data Artifacts and Figures

The project's data outputs include the following tables. [src: bacillota_b_subsurface_accessory]
- A cohort-assignment table (data/cohort_assignments.tsv, 124 rows: anchor_deep_clay 10 + soil_baseline 62 + anchor_other_clay + unclassified).
- A 4-row NB01 gate output (data/ir_pfam_availability.tsv) of PFAM hit counts for iron-reduction-detection PFAMs within Bacillota_B.
- A long-format per-genome × OG presence table (data/cohort_og_presence.parquet, 156,850 rows, 14,109 unique OGs). It was built in 02_og_presence.ipynb from Firmicutes-level OGs with Bacteria/root fallbacks.
- Full per-OG Fisher results for 14,109 OGs (data/og_per_test.parquet), produced in 03_og_enrichment.ipynb.
- The 547 H1 anchor-enriched OGs (q<0.05, fold≥3, n_anchor≥3) in data/og_enrichment.tsv.
- The 27 anchor-depleted OGs in data/og_depletion.tsv.
- A 547-entry NB04 functional annotation of enriched OGs (eggNOG + bakta + pre-registered category).
- A 6-row H2 table (data/h2_compactness.tsv) of Wilcoxon tests and Cohen's *d* on size, OG count, GC and CheckM.

For the clay correction, 06_clay_h3_correction.ipynb applied the triple-signal multi-heme cytochrome detector to the clay project cohort. It produced per-genome corrected scores for the clay project's full cohort of 211 genomes (data/clay_h3_ir_corrected.tsv). It also produced 3 pairwise Fisher tests on corrected multi-heme cytochrome rates (data/clay_h3_ir_corrected_fisher.tsv). A 5-row cohort-level original-versus-corrected iron-reduction table (data/clay_h3_ir_orig_vs_corrected.tsv) completes the set, and the report calls it the headline correction table. [src: bacillota_b_subsurface_accessory]

The headline 4-panel figure (figures/summary_figure.png) shows the following. [src: bacillota_b_subsurface_accessory]
- Panel A: H1 enriched-OG functional categories.
- Panel B: H2 anchor-larger genome size.
- Panel C: the top 10 H1 enriched OGs, with anchor versus baseline rates.
- Panel D: clay H3 iron-reduction original versus corrected, per cohort.

Three supporting figures accompany it. [src: bacillota_b_subsurface_accessory]
- h1_functional_categories.png gives a detailed COG-category breakdown of the 547 enriched OGs.
- h2_compactness.png gives anchor-versus-baseline boxplots of genome size, OG count and GC%.
- clay_h3_ir_corrected.png shows the clay project's iron-reduction results, original versus corrected by cohort, with a triple-signal breakdown.

## Slots Into

- [[concepts/pangenome-integration]] — The 547 enriched OGs, genome-size expansion, cohort construction, and taxonomic limitations provide a within-lineage pangenome comparison.
- [[concepts/subsurface-bacillota-specialization]] — The central finding that deep-clay Bacillota_B encode anaerobic-respiration, sporulation-revival, mineral-attachment, regulatory, and osmoadaptation features while retaining larger genomes.
- [[concepts/functional-marker-validation]] — The corrected triple-signal detector and the resulting loss of the original shallow-versus-deep iron-reduction contrast provide a reusable marker-correction workflow.
- [[concepts/adversarial-research-quality-assurance]] — The mismatched iron-reduction KOs and their thresholds show how a merged analysis carried an artefactual framing until re-checked. [src: bacillota_b_subsurface_accessory]
- [[concepts/biosynthetic-self-sufficiency-and-cultivation]] — Larger anchor genomes are linked to a self-sufficiency hypothesis for cultivable subsurface Bacillota_B. [src: bacillota_b_subsurface_accessory]
- [[concepts/ontology-and-category-schema-sensitivity]] — Keyword categorization undercounted anaerobic-respiration OGs, and coarse OG levels affect annotation. [src: bacillota_b_subsurface_accessory]
- [[concepts/sampling-depth-and-downsampling-effects]] — Small anchor cohort and matched CheckM completeness bound what the size and enrichment contrasts can show. [src: bacillota_b_subsurface_accessory]
- [[concepts/subsurface-hydrogeological-zonation]] — The corrected detector removes the shallow-versus-deep iron-reduction contrast across clay cohorts. [src: bacillota_b_subsurface_accessory]
- [[concepts/genomic-under-representation]] — The Bacillota_B pangenome universe was far smaller than planned. [src: bacillota_b_subsurface_accessory]
- [[concepts/homology-search-negative-evidence]] — PF14537 was silently absent and multi-heme PFAMs were sparse, so absence by PFAM is weak evidence. [src: bacillota_b_subsurface_accessory]
- [[concepts/phylogenetic-confounding-of-pangenome-associations]] — Genus clumping in the anchor means some enriched OGs may be lineage markers. [src: bacillota_b_subsurface_accessory]
- [[concepts/callability-limited-comparative-inference]] — A porewater-dominated anchor cannot test rock-attached gene content. [src: bacillota_b_subsurface_accessory]
- [[concepts/taxonomic-resolution-dependent-functional-inference]] — No Bacillota_B-specific eggNOG tier forced Firmicutes or root-level OGs. [src: bacillota_b_subsurface_accessory]
- [[concepts/cultivation-collection-bias-in-ecological-genomics]] — The anchor came ~entirely from `ncbi_env` keyword search and is porewater-dominated. [src: bacillota_b_subsurface_accessory]
- [[concepts/phenotype-database-coverage-bias]] — BacDive expansion yielded zero additional Bacillota_B genomes. [src: bacillota_b_subsurface_accessory]
