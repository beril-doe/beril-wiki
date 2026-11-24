---
type: "Summary"
description: "Summary of the project Subsurface Bacillota_B Specialization — What Distinguishes Deep-Clay Lineages from Soil Congeners?."
doc_type: "short"
full_text: "sources/bacillota_b_subsurface_accessory__REPORT.md"
---
# Subsurface Bacillota_B Specialization — What Distinguishes Deep-Clay Lineages from Soil Congeners?

Summary of the project Subsurface Bacillota_B Specialization — What Distinguishes Deep-Clay Lineages from Soil Congeners?.

## Key Findings

### Accessory gene content (H1)

The report counts 547 enriched OGs, far above its H1 prediction of at least 10, and treats this as strongly supportive of H1. [src: bacillota_b_subsurface_accessory] The test was a per-OG Fisher's exact test on 14,109 Firmicutes-level eggNOG OGs. It used Benjamini-Hochberg false discovery rate (BH-FDR) correction, q<0.05, fold-difference ≥3 and ≥3 positive anchor genomes. [src: bacillota_b_subsurface_accessory] In the same run 27 OGs were anchor-depleted. [src: bacillota_b_subsurface_accessory] The top hits had OR=∞, with 7–10 anchor genomes positive versus 0 baseline genomes. [src: bacillota_b_subsurface_accessory] Enriched OGs were assigned to pre-registered categories by keyword scanning of eggNOG and bakta annotations. [src: bacillota_b_subsurface_accessory]

| Category | Enriched OGs |
|---|---|
| anaerobic respiration | 42 [src: bacillota_b_subsurface_accessory] |
| sporulation revival | 24 [src: bacillota_b_subsurface_accessory] |
| mineral attachment / EPS | 12 [src: bacillota_b_subsurface_accessory] |
| anaerobic regulators | 4 [src: bacillota_b_subsurface_accessory] |
| osmoadaptation | 3 [src: bacillota_b_subsurface_accessory] |
| other / unannotated | 462 [src: bacillota_b_subsurface_accessory] |

The "other" bucket is misleading. The report says the keyword scanner missed many anaerobic-niche signals, because these are encoded by gene-family or domain names rather than by the pre-registered keywords. [src: bacillota_b_subsurface_accessory] The 462-OG bucket contains substantial real anaerobic-niche signal, including COG1977 molybdopterin, DsrEFH and 2-oxoglutarate ferredoxin oxidoreductase. The report proposes an LLM-based pass over eggNOG Description and bakta product text to count categories accurately. [src: bacillota_b_subsurface_accessory] Manual inspection of the top 15 OGs by p_BH found more anaerobic-respiration and electron-transfer hits: [src: bacillota_b_subsurface_accessory]

- COG1977 (Mo-molybdopterin cofactor process) was in 10/10 anchor genomes versus 11/62 baseline genomes. [src: bacillota_b_subsurface_accessory] Molybdopterin is a cofactor for nitrate reductase, formate dehydrogenase and DMSO reductase. [src: bacillota_b_subsurface_accessory] The report calls recovery in 100% of anchors a strong subsurface-niche signal. [src: bacillota_b_subsurface_accessory]
- OG 1UIFM (DsrE/DsrF/DsrH-like) was in 7/10 anchor versus 0/62 baseline genomes. [src: bacillota_b_subsurface_accessory] The report describes DsrEFH as an intracellular sulfite-handling complex coupled to dissimilatory sulfite reductase. It sees this as extending the clay project's SR finding to a tighter dsr-pathway component. [src: bacillota_b_subsurface_accessory]
- OG 1VFGN (2-oxoglutarate:ferredoxin oxidoreductase, EC 1.2.7.3) was in 8/10 anchor versus 4/62 baseline genomes. [src: bacillota_b_subsurface_accessory]
- OG 1V0WU (KEGG K08177 Major Facilitator Superfamily transporter) was in 9/10 anchor versus 5/62 baseline genomes. The report suggests it is likely an osmoprotectant or solute uptake transporter. [src: bacillota_b_subsurface_accessory]

The report estimates that, after manual reclassification, the H1-relevant total is closer to 80–100 of 547. This is above the scanner's 42. [src: bacillota_b_subsurface_accessory]

The report reads its categories as matching Beller 2012's Pelosinus HCF1, a subsurface aquifer Firmicute carrying 2 [NiFe] + 4 [FeFe] hydrogenases, dissimilatory N-oxide reductase, Cr/Fe reductase and the methylmalonyl-CoA pathway. It says the anaerobic respiration, regulator and sporulation categories match that gene-content snapshot at population scale. [src: bacillota_b_subsurface_accessory] It also says the sporulation-revival hits replicate Vandieken 2017's description of Baltic Sea subsurface Desulfosporosinus as spore-forming with broad respiratory versatility. The anchor cohort includes 3 Desulfosporosinus genomes that contributed to the sporulation-OG signal. [src: bacillota_b_subsurface_accessory] The report presents the 547 annotated OGs as a concrete target list for future biochemistry, fitness-screen and cultivation work. [src: bacillota_b_subsurface_accessory]

### Genome size (H2)

H2 was rejected, and the result went in the opposite direction. The H1 prediction was that the anchor would be smaller. [src: bacillota_b_subsurface_accessory] Deep-clay genomes were significantly larger than soil-baseline genomes, with a 35% mean size difference and ~25% more eggNOG OGs per genome. [src: bacillota_b_subsurface_accessory] The report states that anchor genomes are ~1 Mbp larger than baseline. [src: bacillota_b_subsurface_accessory] All four size/OG-count metrics were significant (p ≤ 0.025) with Cohen's d ≥ +1.30. [src: bacillota_b_subsurface_accessory]

| Metric | Anchor (n=10) | Baseline (n=62) | Cohen's d | Mann–Whitney p |
|---|---|---|---|---|
| genome size (bp) | 4,110,038 | 3,046,124 | +1.39 | 0.025 [src: bacillota_b_subsurface_accessory] |
| genome size, CheckM-rescaled | 4,323,230 | 3,233,715 | +1.37 | 0.013 [src: bacillota_b_subsurface_accessory] |
| eggNOG OGs | 2,630 | 2,106 | +1.30 | 0.022 [src: bacillota_b_subsurface_accessory] |
| eggNOG OGs, CheckM-rescaled | 2,771 | 2,233 | +1.32 | 0.009 [src: bacillota_b_subsurface_accessory] |
| GC % | 48.84 | 47.76 | +0.21 | 0.44 [src: bacillota_b_subsurface_accessory] |
| CheckM completeness | 94.7% | 94.3% | +0.08 | 0.93 [src: bacillota_b_subsurface_accessory] |

No statistically significant difference was detected in GC content or in completeness. [src: bacillota_b_subsurface_accessory] Because completeness was similar, the report concludes that the size gap cannot be a MAG-quality artefact. It says deep-clay Bacillota_B encode ~1 Mbp more genetic material at the same QC level. [src: bacillota_b_subsurface_accessory]

This is the opposite direction from Tian et al. (2020). Tian's streamlining claim was specific to Patescibacteria/CPR, with ≤1 Mbp genomes and an episymbiotic lifestyle. [src: bacillota_b_subsurface_accessory] The report says the apparent contradiction is limited, because Tian's finding was specific to host-dependent CPR and Tian notes that non-CPR phyla retain larger genomes. [src: bacillota_b_subsurface_accessory] It reads its result as consistent with streamlining being CPR-specific, with cultivable subsurface Firmicutes showing the opposite pattern. [src: bacillota_b_subsurface_accessory] The report interprets deep-clay specialization in cultivable, free-living anaerobic Bacillota_B as correlating with gene-content expansion. [src: bacillota_b_subsurface_accessory] It calls this consistent with Beaver & Neufeld (2024)'s self-sufficiency hypothesis. It also calls it consistent with Becraft et al. (2021), who found that Ca. Desulforudis audaxviator retains a self-sufficient genome without streamlining. [src: bacillota_b_subsurface_accessory] Becraft's genome is described as suggesting complete self-sufficiency, with all genes for carbon and nitrogen fixation and all amino acid biosynthesis pathways. [src: bacillota_b_subsurface_accessory] The report reads its ~25% more orthogroups as consistent with self-sufficiency and as extending a single-lineage finding to a within-phylum comparison. [src: bacillota_b_subsurface_accessory] That genome, GB_GCA_020725505.1, is in the anchor cohort. [src: bacillota_b_subsurface_accessory] The report presents this as a statistically supported refutation of "subsurface = streamlining" within cultivable Firmicutes. [src: bacillota_b_subsurface_accessory]

The report asks where the extra DNA goes. It proposes a COG (clusters of orthologous groups) / KEGG-pathway breakdown of the extra gene fraction, and names mobile-element-borne accessory operons, sporulation regulons and anaerobic-respiration accessories as candidate mechanisms. [src: bacillota_b_subsurface_accessory]

### Correction of the clay project's iron-reduction result

The clay project used K07811, K17324 and K17323 as IR markers. These KOs are actually TMAO reductase, glycerol ABC transport and glycerol permease. [src: bacillota_b_subsurface_accessory] Specifically, K07811 is a TMAO reductase (threshold 1336.87), K17324 a glycerol ABC ATP-binding protein (threshold 363.93) and K17323 a glycerol ABC permease (threshold 318.27). None is an iron-reduction gene. [src: bacillota_b_subsurface_accessory] KEGG has no canonical KO for Geobacter omcS or Shewanella mtr multi-heme cytochromes. [src: bacillota_b_subsurface_accessory] The report calls this a real bug fix in PR #231. [src: bacillota_b_subsurface_accessory] It attributes the clay project's "Mitzscherling rock-attached signature in shallow clay" to mismatched gene IDs combined with an eggNOG-mapper threshold that filters sequence similarity, not KO biological identity. [src: bacillota_b_subsurface_accessory] The corrected detector scores a genome positive if any one of three signals is present: [src: bacillota_b_subsurface_accessory]

- PFAM PF02085 (Cytochrom_CIII). [src: bacillota_b_subsurface_accessory]
- PFAM PF22678 (Cytochrom_c_NrfB-like). [src: bacillota_b_subsurface_accessory]
- A CXXCH heme-binding motif count ≥4, a canonical method since Methé et al. 2003. [src: bacillota_b_subsurface_accessory]

The detector was applied to the clay project cohort in the notebook 06_clay_h3_correction.ipynb. [src: bacillota_b_subsurface_accessory] The report proposes this triple-signal detection as a reusable pattern when KEGG KO assignment is unreliable, applicable wherever IR or extracellular-electron-transfer questions arise. [src: bacillota_b_subsurface_accessory]

| Cohort | n | Original wrong-KO IR | Corrected IR |
|---|---|---|---|
| anchor_deep (Mont Terri Opalinus + bentonite) | 9 | 11.1% (1/9) [src: bacillota_b_subsurface_accessory] | 55.6% (5/9) [src: bacillota_b_subsurface_accessory] |
| anchor_shallow (Coalvale + Cerrado + agricultural) | 30 | 50.0% (15/30) [src: bacillota_b_subsurface_accessory] | 40.0% (12/30) [src: bacillota_b_subsurface_accessory] |
| soil_baseline | 149 | 20.1% (30/149) [src: bacillota_b_subsurface_accessory] | 40.9% (61/149) [src: bacillota_b_subsurface_accessory] |

No corrected pairwise Fisher comparison was significant: deep vs shallow OR=1.88 p=0.46 [src: bacillota_b_subsurface_accessory], deep vs baseline OR=1.80 p=0.49 [src: bacillota_b_subsurface_accessory], and shallow vs baseline OR=0.96 p=1.0. [src: bacillota_b_subsurface_accessory] The original shallow-greater-than-deep pattern disappears. [src: bacillota_b_subsurface_accessory] The corrected rates are 40–56%, far above what PFAM-only detection would give, because CXXCH motif counting carried most of the signal. Multi-heme cytochrome PFAMs are sparse in Bacillota_B, with only ~6 clusters across four PFAMs. [src: bacillota_b_subsurface_accessory] Corrected rates are saved for a separate correction commit on the clay project's branch. [src: bacillota_b_subsurface_accessory] The report proposes a correction notebook and a report amendment for the clay project. It characterizes the IR-side H3 finding as artefactual and says the SR side stands. [src: bacillota_b_subsurface_accessory]

The SR side stands. The deep cohort had 5/9 SR-positive genomes against the Mitzscherling rock-attached null of 0.2% (binomial p=4×10⁻¹²). [src: bacillota_b_subsurface_accessory] The SR markers K11180, K11181, K00394, K00395 and K00958 were correctly identified. [src: bacillota_b_subsurface_accessory] The porewater-bias headline therefore holds via SR alone. The Mitzscherling rock-attached versus Bagnoud porewater framing is unsupported on the corrected IR side. [src: bacillota_b_subsurface_accessory] The report adds that the IR correction does not settle whether the original porewater narrative is fully recovered or partly undercut: the SR side is robust and the IR-side narrative loses force. [src: bacillota_b_subsurface_accessory]

### Claimed contributions

The report claims the first quantitative gene-cluster-level characterization of subsurface Bacillota_B specialization, going beyond the clay project's curated marker dictionary to the full KBase Data Lakehouse pangenome accessory genome. [src: bacillota_b_subsurface_accessory]

## Data and Methods

The anchor cohort has 10 genomes. Five come from the Mont Terri Opalinus borehole (Desulfosporosinus, BRH-c8a×2, BRH-c4a, and one metagenomic Desulfosporosinus). Three are Mont Terri rock-porewater MAGs. Two come from the Russian Beyelii Yar borehole (Ca. Desulforudis audaxviator and Ch130 Thermacetogeniaceae). [src: bacillota_b_subsurface_accessory] The baseline has 62 phylum-matched soil/sediment genomes: Syntrophomonadales 29, Desulfitobacteriales 16, Moorellales 6, Thermacetogeniales 4, Ammonifexales 2, Carboxydocellales 2, Desulfotomaculales 1, Heliobacteriales 1 and Thermincolales 1. [src: bacillota_b_subsurface_accessory] One claim puts the total at 334 Bacillota_B genomes in the KBase Data Lakehouse pangenome, far fewer than the v1.1 plan's 6,700 estimate. [src: bacillota_b_subsurface_accessory] The report's universe table has 314 rows and is described as covering all Bacillota_B genomes in the pangenome with QC and isolation metadata. [src: bacillota_b_subsurface_accessory] The two counts are reported separately, and the claims do not explain the difference between them.

The analysis drew on the kbase_ke_pangenome collection for the Bacillota_B universe, cohort metadata, per-cluster annotations and protein sequences for the CXXCH scan. [src: bacillota_b_subsurface_accessory] Tables used were gtdb_taxonomy_r214v1, genome, gtdb_metadata, ncbi_env, gene, gene_genecluster_junction, gene_cluster, eggnog_mapper_annotations, bakta_pfam_domains and bakta_annotations. [src: bacillota_b_subsurface_accessory] BacDive expansion (kescience_bacdive isolation and taxonomy) yielded zero additional Bacillota_B; the 10-genome anchor came almost entirely from an ncbi_env keyword search. [src: bacillota_b_subsurface_accessory] OG orthology was hierarchical: Firmicutes-level OGs (eggNOG tax 1239) where present, falling back to Bacteria/root. [src: bacillota_b_subsurface_accessory] Output tables include a 124-row cohort assignment table (anchor_deep_clay 10, soil_baseline 62, anchor_other_clay and unclassified), 156,850 genome-by-OG presence rows covering 14,109 unique OGs, and 547 annotated enriched OGs. [src: bacillota_b_subsurface_accessory] The clay IR correction table has 211 per-genome rows. [src: bacillota_b_subsurface_accessory] A final notebook, 07_synthesis.ipynb, generates the report's 4-panel summary figure. [src: bacillota_b_subsurface_accessory]

## Caveats and Open Work

- The keyword scanner undercounts anaerobic signals, and 462 of 547 OGs fall in "other". The 80–100 estimate comes from manual reclassification. [src: bacillota_b_subsurface_accessory]
- The anchor cohort is only 10 genomes, against 62 in the baseline. Fisher's exact is adequate for large effects and the 547 enriched OGs are robust, but marginal effects with anchor counts of 3–5 should be treated descriptively. [src: bacillota_b_subsurface_accessory]
- The 10-genome anchor is genus-clumped: 3 BRH-c8a + 2 BRH-c4a + 2 Desulfosporosinus + Desulforudis + Ch130 + 1 other. [src: bacillota_b_subsurface_accessory]
- Genus-level phylogenetic confounding is partly mitigated by the cohort spanning four orders (Desulfotomaculales, Desulfitobacteriales, Ammonifexales, Thermacetogeniales), but not eliminated. [src: bacillota_b_subsurface_accessory]
- The anchor cohort is borehole/porewater-dominated by construction, so the comparison cannot test whether rock-attached Bacillota_B differs in gene content. [src: bacillota_b_subsurface_accessory]
- Some enriched OGs sit at coarse root level. eggNOG has no Bacillota_B-specific tier, because Bacillota_B is GTDB-defined while eggNOG uses NCBI taxonomy. [src: bacillota_b_subsurface_accessory]
- Within Bacillota_B, the PFAM cytochrome hits are few: PF02085.21 has 4 hits in 4 clusters. PF00034.26, PF13442.11 and PF22678.1 each have 1 hit in 1 cluster. [src: bacillota_b_subsurface_accessory] PF14537 (Cytochrom_NNT) has 0 hits and 0 clusters, confirmed as silently absent, the documented plant_microbiome_ecotypes pitfall. [src: bacillota_b_subsurface_accessory]
- Corrected IR detection leaves the clay project's IR-side comparisons non-significant. [src: bacillota_b_subsurface_accessory]

Next analyses the report proposes:

- A per-genus H1 analysis would separate genus-specific lineage-marker noise from enriched OGs recurrent across several subsurface-specialist genera, the genuine deep-clay signature. [src: bacillota_b_subsurface_accessory] With n=10 this is at the limit of statistical resolution. More clay-isolated Bacillota_B from BacDive linkage or future KBase Data Lakehouse pangenome ingests would improve power. [src: bacillota_b_subsurface_accessory]
- Retarget the NB01–04 pipeline to within-Bacteroidota, within-Pseudomonadota and within-Acidobacteriota deep-clay versus soil comparisons. Each would test whether the H1 functional-category signal generalizes or is Bacillota_B-specific. [src: bacillota_b_subsurface_accessory]
- Break down the extra gene fraction by COG / KEGG pathway to localize the genome expansion. [src: bacillota_b_subsurface_accessory]

## Slots Into

- [[concepts/accessory-gene-content-enrichment-in-subsurface-lineages-relative-to-soil-congeners]]: 547 enriched OGs in deep-clay Bacillota_B. [src: bacillota_b_subsurface_accessory]
- [[concepts/limits-of-keyword-and-marker-based-functional-annotation]]: the keyword scanner missed anaerobic signals. [src: bacillota_b_subsurface_accessory]
- [[concepts/genome-streamlining-and-genome-size-in-ecological-specialists]]: deep-clay genomes are larger, not streamlined. [src: bacillota_b_subsurface_accessory]
- [[concepts/reliability-of-kegg-ortholog-markers-for-multi-heme-cytochrome-iron-reduction]]: the wrong KOs were used as IR markers. [src: bacillota_b_subsurface_accessory]
- [[concepts/iron-and-sulfate-reduction-signatures-in-clay-subsurface-porewater-versus-rock-attached-communities]]: the SR signal is robust and the IR contrast vanishes. [src: bacillota_b_subsurface_accessory]
- [[concepts/small-cohort-and-phylogenetic-confounding-in-lineage-level-comparisons]]: 10 vs 62 genomes, with confounding only partly mitigated and a genus-clumped anchor. [src: bacillota_b_subsurface_accessory]
- [[concepts/biosynthetic-self-sufficiency-as-a-deep-subsurface-adaptation]]: larger genomes are read as consistent with self-sufficiency. [src: bacillota_b_subsurface_accessory]
