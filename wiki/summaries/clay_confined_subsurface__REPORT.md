---
type: "Summary"
description: "Summary of the clay_confined_subsurface project, which tests biosynthetic self-sufficiency, an anaerobic toolkit, and porewater-versus-rock-attached cultivation bias in cultured deep-clay, shallow-clay, and soil-baseline bacterial genomes."
doc_type: "short"
full_text: "sources/clay_confined_subsurface__REPORT.md"
---
# Self-Sufficiency, Anaerobic Toolkit, and Cultivation Bias in Clay-Confined Cultured Bacterial Genomes

## Overview

This report analyzes cultured bacterial genomes from clay-related environments in the KBase KE pangenome, comparing 9 deep-confined genomes, 30 shallow-clay genomes, and a phylum-stratified soil baseline of 150 genomes (137 after quality filtering). It tests biosynthetic self-sufficiency, an anaerobic metabolic toolkit, and whether cultured clay genomes resemble porewater or rock-attached subsurface communities. The principal result is that the deep cultured cohort carries a robust dissimilatory sulfate-reduction signal associated with the Bagnoud Mont Terri porewater paradigm. Broader anaerobic-toolkit enrichment is largely explained by Bacillota_B phylogeny, and self-sufficiency is not elevated. [src: clay_confined_subsurface]

## Key Findings

### Cultured deep-clay genomes show a sulfate-reduction-rich porewater signature

The deep cohort has 9 genomes: 8 from Mont Terri Opalinus boreholes and 1 from a bentonite formation. Of these, 5/9 (56%) carried dissimilatory sulfate-reduction markers, compared with 1/9 iron-reduction-marker-positive genomes under the original, later-invalidated iron-reduction analysis. The rock-attached null came from Mitzscherling et al. (2023), with SRB ~0.2% and IRB ~7% of the community. Against that null, the sulfate-reduction enrichment was highly significant: 5 observed positives versus 0.018 expected among 9 genomes, binomial p = 4.0×10⁻¹². The original comparison of iron-reduction depletion against the same null was not significant: 1 observed versus 0.63 expected, p = 0.87. In the H3 pairwise Fisher comparisons of sulfate-reduction completeness, anchor_deep versus anchor_shallow gave OR = ∞, p = 2×10⁻⁴. Anchor_deep versus soil_baseline gave OR = 33.8, p = 5×10⁻⁵; this pairwise p-value is separate from the BH-adjusted per-marker test reported below. The sulfate-reduction comparison of anchor_shallow versus soil_baseline was not significant (OR = 0.0, p = 0.59). The report also describes the Mitzscherling et al. (2023) rock-attached community profile as SRB <0.2% and IRB 4.3–10.2%, dominated by *Geobacter* and *Geothrix*. This profile is a literature comparator, not an iron-marker result for the cultured cohort. [src: clay_confined_subsurface]

The report concludes that the cultured Mont Terri cohort matches the Bagnoud porewater paradigm and does not show that the rock-attached community is represented. All 8 Opalinus genomes trace to BRC-3 or BIC-A1 borehole isolation sources, and the report treats this as a direct, quantitative diagnostic of cultivation bias: the KBase Data Lakehouse captures the porewater fraction, not the rock-attached fraction. Five of the nine deep genomes carry the dissimilatory sulfate-reduction module (Sat, AprAB, DsrAB), and seven carry group 1 [NiFe]-hydrogenase markers. These include direct hits on the BRH-c8a (Peptococcaceae c8a in Bagnoud's nomenclature) and Desulfosporosinus lineages. The report attributes to Bagnoud a minimalistic Opalinus food web in which Desulfobulbaceae c16a expressed the complete Wood–Ljungdahl pathway, group 1 [NiFe]-hydrogenase, and Sat–AprAB–DsrAB. In that work, three MAGs (metagenome-assembled genomes) recurred across seven independent boreholes. The deep-cohort genera match lineages that Bagnoud (2016) identified as recurrent across 7 Mont Terri boreholes:
- Desulfosporosinus (×2)
- BRH-c8a (Peptococcaceae c8a; ×2)
- BRH-c4a (Desulfotomaculales)
- Lutibacter and BRH-c54 (Bacteroidota)
- Roseovarius (Rhodobacterales)
- Stenotrophomonas (the bentonite isolate) [src: clay_confined_subsurface]

The original iron-reduction (IR) analysis compared anchor_deep (1/9 IR-positive) with anchor_shallow (15/30 IR-positive) to argue that shallow clay showed a Mitzscherling rock-attached, IR-rich pattern. That analysis is invalid because K07811, K17324, and K17323 were misidentified as iron-reduction markers. They are TMAO reductase, glycerol ABC transport ATP-binding, and glycerol ABC transport permease, respectively. KEGG has no canonical KO for the Geobacter omcS / Shewanella mtr operon multi-heme outer-surface cytochromes, so the original analysis unknowingly substituted unrelated genes. The corrected analysis used a triple-signal multi-heme cytochrome detector: PFAM PF02085, PFAM PF22678, and counting of CXXCH heme-binding motifs, with a threshold of ≥4 motifs. Corrected iron-reduction rates were 55.6% for anchor_deep (n = 9), 40.0% for anchor_shallow (n = 30), and 40.9% for soil_baseline (n = 149). The original rates were 11.1%, 50.0%, and 20.1%, respectively. All corrected cohort comparisons had Fisher p ≥ 0.46. After correction, the original shallow-over-deep pattern reverses so that deep is slightly higher than shallow, but none of the cohort comparisons is statistically significant. The report withdraws its original iron-reduction narrative, which held that the clay cohort diverges from the Mitzscherling rock-attached profile because shallow clay shows the iron-reduction-rich pattern. The sulfate-reduction-side H3 finding stands. Its markers, K11180/K11181/K00394/K00395/K00958, were correctly identified, and the deep-cohort 5/9 SR-positive result against the Mitzscherling rock-attached null (p = 4×10⁻¹²) is robust. The porewater-bias headline therefore rests on the sulfate-reduction side alone. The report calls the rock-attached versus porewater dichotomy half-supported on the sulfate-reduction side and half-unsupported on the iron-reduction side after marker correction. [src: clay_confined_subsurface]

The report notes that sister project NB04 independently flags this K-number problem as systematic. KEGG KO assignment is unreliable for niche genes that lack canonical KOs (omcS, mtrCAB, MGE-borne resistance cassettes), and KEGG-based marker mining for such genes will silently substitute unrelated functions. The correction notice also supersedes the iron-reduction interpretation in the report's figure h3_porewater_vs_rock.png. That figure shows SR/IR rates by cohort against the Mitzscherling rock-attached reference, along with marker-class composition. Its sulfate-reduction comparison remains supported. Its IR rates and IR-dependent marker classes rely on misidentified markers and must not be read as validated iron-reduction results. [src: clay_confined_subsurface]

### The anaerobic toolkit is strongly enriched at cohort level but mostly phylum-driven

The anaerobic toolkit combined three modules: Wood–Ljungdahl (WL), group 1 [NiFe]-hydrogenase (NiFe), and dissimilatory sulfate reduction (SR). The report's prose gives mean toolkit scores of 1.89 for deep clay, 0.39 for the soil baseline, and 0.03 for shallow clay, out of 3 modules. The corresponding table values are 1.889 for anchor_deep (n = 9), 0.033 for anchor_shallow (n = 30), and 0.393 for soil_baseline (n = 140). The proportions with all three modules were 0.556, 0.000, and 0.021, respectively. The report's figure h2_toolkit_by_cohort.png shows these toolkit scores (0–3) as stacked bars, together with per-module presence rates by cohort. [src: clay_confined_subsurface]

Deep-cohort Fisher tests against the soil baseline were adjusted by BH-FDR (the Benjamini–Hochberg false-discovery-rate procedure):
- WL: 5/9 versus 15/140, OR = 10.4, p_BH = 0.004
- NiFe: 7/9 versus 35/140, OR = 10.5, p_BH = 0.004
- SR: 5/9 versus 5/140, OR = 33.8, p_BH = 2.5×10⁻⁴
- Nitrogenase (Nif_complete): 4/9 versus 18/140, OR = 5.4, p_BH = 0.035 [src: clay_confined_subsurface]

The per-marker table also lists IR OR = 0.46, p_BH = 0.69. That result came from the original, invalidated iron-reduction KOs and is superseded by the correction above. The WL and NiFe enrichments did not survive within-phylum control. [src: clay_confined_subsurface]

Within-phylum control exposed a phylogenetic confound. Bacillota_B contains Desulfosporosinus, BRH-c4a, and BRH-c8a, the lineages that dominate the deep cohort. This phylum carries WL and [NiFe]-hydrogenase at high background rates even in soil samples, with a toolkit mean of 1.65 in the Bacillota_B baseline. Within Bacillota_B, WL was present in 5/5 deep genomes versus 15/19 baseline genomes (raw p = 0.54, BH-adjusted p = 1.0). NiFe was present in 5/5 versus 14/19 (raw p = 0.54, BH-adjusted p = 1.0). Neither difference was significant, so these markers track the Bacillota_B lineage rather than deep-clay habitat itself. SR (dsrAB-aprAB-sat) was present in 5/5 deep genomes versus 4/19 baseline genomes, with OR = ∞ and p = 0.003. The adjusted p-value is reported as p_BH = 0.04 in the report's prose and as p_BH = 0.044 in its within-phylum table. Only sulfate reduction survived the reported phylogenetic control as a signal associated with deep clay. [src: clay_confined_subsurface]

### Biosynthetic self-sufficiency was not elevated in the cultured deep cohort

GapMind amino-acid pathway completeness was measured across an 18-pathway universe. Anchor_deep did not show higher completeness than the baseline in any comparison:
- Unfiltered: anchor_deep (n = 9) mean 16.22/18 versus baseline (n = 150) 16.66/18; Mann–Whitney p = 0.153, Cohen's d = −0.17
- After the CheckM filter (≥80% completeness, ≤5% contamination): anchor_deep (n = 6) mean 15.50/18 versus baseline (n = 137) 17.14/18; p = 0.009, d = −0.84
- Within Bacillota_B: 16.50 for 4 deep genomes versus 16.79 for 19 baseline genomes; p = 0.073, d = −0.13, which does not establish a difference [src: clay_confined_subsurface]

The report's figure h1_self_sufficiency_violin.png shows the distribution of complete amino-acid pathways by cohort, both unfiltered and CheckM-filtered. [src: clay_confined_subsurface]

Anchor_shallow instead showed higher completeness than the baseline:
- Unfiltered: mean 17.87/18 for 30 genomes versus 16.66/18 for 150 baseline genomes; p = 0.006, d = +0.52
- After filtering: 17.87/18 for 30 genomes versus 17.14/18 for 137 baseline genomes; p = 0.029, d = +0.43 [src: clay_confined_subsurface]

The report reads this as consistent with cultivation-quality selection among agricultural isolates. It also notes that the 18-pathway metric imposes a ceiling: most cultured organisms, deep or shallow, reach 17–18/18 regardless of habitat, which leaves little room to detect a positive signal at the upper end. [src: clay_confined_subsurface]

The negative deep-cohort result does not reject biosynthetic self-sufficiency as an adaptation of deep-subsurface life. It shows that the cultured KBase Data Lakehouse cohort lacks the extreme self-sufficient lineages emphasized in the literature. The Beaver & Neufeld (2024) synthesis presents *Ca.* Desulforudis audaxviator as the example of this canonical deep-subsurface adaptation. Such lineages are characteristically uncultivated and are recovered as MAGs (metagenome-assembled genomes) or single-cell genomes. [src: clay_confined_subsurface]

### Cohort composition and cultivation bias constrain interpretation

Cohorts were assembled from kbase_ke_pangenome.ncbi_env, filtered for clay-related isolation_source / env_* keywords, and joined to the pangenome via genome.ncbi_biosample_id. The kbase_ke_pangenome tables used were ncbi_env, genome, gtdb_metadata, gtdb_taxonomy_r214v1, gene, gene_genecluster_junction, eggnog_mapper_annotations, and gapmind_pathways. Together they supplied cohort assembly from biosample environmental metadata, per-genome cluster mapping, KEGG/PFAM marker annotations, and amino-acid pathway completeness. Counts before and after the CheckM quality filter (≥80% completeness, ≤5% contamination):
- anchor_deep: 9 → 6 genomes (8 Mont Terri Opalinus borehole genomes from BRC-3 and BIC-A1; 1 bentonite-formation genome)
- anchor_shallow: 30 → 30 genomes (8 Coalvale silty-clay, 1 Cerrado-clay, 21 agricultural-clay)
- soil_baseline: 150 → 137 genomes (soil/sediment with no clay mention, phylum-stratified before filtering as Pseudomonadota 50, Bacillota 40, Bacillota_B 20, Bacteroidota 20, Actinomycetota 20) [src: clay_confined_subsurface]

The report treats cultivation bias as the headline finding rather than a confounder. Because the cohort is cultured-only, all conclusions apply to cultivable, porewater-cultured deep-clay isolates, not to the full Mont Terri or bentonite microbial communities. Rock-attached Geobacter and Geothrix lineages and CPR/DPANN episymbionts are essentially absent from the cultured cohort. MAG-augmented work is needed to test whether the complete clay-confined community follows the same patterns. [src: clay_confined_subsurface]

### Analysis methods and output files

The report's notebooks used different tests for each hypothesis. H1 used Wilcoxon tests and Cohen's d on amino-acid-pathway completeness, with QC and per-phylum sensitivity analyses. H2 used Fisher tests, a Spearman trend test, and within-phylum Fisher tests on toolkit markers. The original H3 notebook ran binomial tests against the Mitzscherling rock-attached null and pairwise cohort Fisher tests on SR versus IR, so it is not a validated SR/IR comparison. The correction notice keeps its sulfate-reduction-side finding and withdraws its iron-reduction-side interpretation. The corrected IR rates are 55.6% (n = 9 deep), 40.0% (n = 30 shallow), and 40.9% (n = 149 baseline), with all corrected cohort-comparison Fisher p ≥ 0.46. [src: clay_confined_subsurface]

Several output tables carry the original, invalidated IR field and should be read with that in mind:
- data/cohort_assignments.tsv: 61 per-genome rows with cohort_class, sub_cohort, compartment, depth_class, and full GTDB taxonomy
- data/genome_features.parquet: 61 genomes with marker booleans (WL, NiFe, SR, IR, Nif), counts, toolkit_score, and GapMind amino-acid pathway counts; its original IR field is not validated iron-reduction evidence, because the correction notice identifies the original IR markers as unrelated functions
- data/baseline_features.parquet: 150 rows with the same schema for the phylum-stratified soil baseline, including the subsequently invalidated IR field
- data/h3_vs_mitzscherling.tsv: the original 2 binomial tests against the Mitzscherling 2023 rock-attached null; the sulfate-reduction side is retained and the iron-reduction-side interpretation is withdrawn
- data/h3_cohort_pairwise.tsv: 6 rows of pairwise cohort Fisher tests on SR and purported IR markers; the IR-side comparisons are not validated iron-reduction results
- data/h3_marker_class_table.tsv: a 4-row SR_only / IR_only / both / neither breakdown whose IR-dependent classes require re-evaluation with corrected detection [src: clay_confined_subsurface]

## Caveats

- The deep anchor cohort is small (n = 9 before quality filtering), so only large effects, described as Cohen's d > 0.7 for unfiltered comparisons, can be reliably detected. Marginal results, such as the within-Bacillota_B self-sufficiency comparison at p = 0.07, are descriptive only. [src: clay_confined_subsurface]
- Compartment annotations were inferred from keywords in isolation-source strings, so some bentonite or "rock" entries could be porewater or rock-attached. The report states that the H3 sulfate-reduction result held under two stricter compartment definitions. [src: clay_confined_subsurface]
- The GapMind metric covers only an 18-pathway amino-acid universe (gapmind_pathways), which saturates near 18 for most cultivable bacteria, so the metric has limited resolving power at its upper end. The report proposes a finer-grained sensitivity analysis that checks all standard amino-acid-biosynthesis EC numbers in eggNOG. [src: clay_confined_subsurface]
- eggNOG cluster-level annotations propagate within clusters of ≥90% AAI, so strain-level marker variants may be missed, including a single non-functional dsrA in an otherwise complete operon. [src: clay_confined_subsurface]
- The report recommends five follow-ups. The strongest next step is to ingest deep-subsurface MAGs from Mont Terri, Olkiluoto, MX-80 bentonite, and Oak Ridge into the pangenome, then re-run the H1/H2/H3 framework. This would test whether an H1 self-sufficiency signal emerges once rock-attached or uncultivated lineages are present, a question that remains untested. Any rerun of the H3 iron-reduction side would need the corrected detector. [src: clay_confined_subsurface]
- An exploratory direct comparison of BRC-3 porewater versus BIC-A1 borehole genomes, with 5 + 3 genomes per borehole, could test whether the Bagnoud-paradigm sulfate-reduction-rich pattern is borehole-specific or site-wide within Mont Terri. [src: clay_confined_subsurface]
- The sulfate-reduction/iron-reduction diagnostic could be applied to other subsurface settings. [src: clay_confined_subsurface]
- The 5/5 Bacillota_B sulfate-reduction enrichment is striking, but its "n=5 vs 19" structure may hide genus-level differences: Desulfosporosinus, BRH-c8a, and BRH-c4a may differ in which non-SR features they carry. The report proposes a within-Bacillota_B genus-level pangenome analysis to surface a possible deep-clay-specific accessory genome. [src: clay_confined_subsurface]
- Genome presence should be linked to Bagnoud's metaproteomic evidence. Bagnoud (2016) reported protein-level expression of the toolkit modules, but this genome-content analysis does not establish their expression in the genomes analyzed here. [src: clay_confined_subsurface]

## Slots Into

- [[concepts/subsurface-bacillota-specialization]] — The cohort-level anaerobic-toolkit signal is largely driven by Bacillota_B, while sulfate reduction stays enriched after within-phylum control. [src: clay_confined_subsurface]
- [[concepts/metabolic-model-gapfilling]] — GapMind pathway completeness gives a negative test of generalized biosynthetic self-sufficiency and reveals a ceiling effect that calls for finer-grained pathway-completeness analyses. [src: clay_confined_subsurface]
- [[concepts/functional-marker-validation]] — The misidentified iron-reduction KOs and the corrected multi-heme cytochrome detector show how marker mining based only on KEGG can silently substitute unrelated functions. [src: clay_confined_subsurface]
- [[concepts/ontology-and-category-schema-sensitivity]] — Niche genes without canonical KEGG KOs make KO-based functional categories unreliable. [src: clay_confined_subsurface]
- [[concepts/cultivation-collection-bias-in-ecological-genomics]] — The sulfate-reduction enrichment against a rock-attached null is a quantitative diagnostic that cultured genomes capture porewater rather than rock-attached communities. [src: clay_confined_subsurface]
- [[concepts/phylogenetic-confounding-of-pangenome-associations]] — WL and [NiFe]-hydrogenase enrichments disappear within Bacillota_B; only sulfate reduction survives. [src: clay_confined_subsurface]
- [[concepts/biosynthetic-self-sufficiency-and-cultivation]] — The cultured deep cohort shows no elevated GapMind completeness, and the report says extreme self-sufficient lineages are characteristically uncultivated. [src: clay_confined_subsurface]
- [[concepts/sampling-depth-and-downsampling-effects]] — Quality filtering shrinks the deep cohort from 9 to 6 genomes. The deep cohort's lower self-sufficiency relative to baseline is not significant before filtering but becomes significant after it. [src: clay_confined_subsurface]
- [[concepts/subsurface-hydrogeological-zonation]] — Sulfate-reduction completeness separates deep from shallow clay cohorts in the pairwise H3 comparison. [src: clay_confined_subsurface]
- [[concepts/confirmatory-exploratory-ecological-association-discordance]] — The same deep-versus-baseline sulfate-reduction contrast is reported with different p-values under pairwise and BH-adjusted testing. [src: clay_confined_subsurface]
- [[concepts/adversarial-research-quality-assurance]] — The report's correction notice withdraws its iron-reduction narrative after the marker misidentification was caught, and keeps the sulfate-reduction side. [src: clay_confined_subsurface]
- [[concepts/computational-pathway-prediction-validation]] — The GapMind ceiling prompts a proposed eggNOG EC-number sensitivity check for amino-acid biosynthesis. [src: clay_confined_subsurface]
- [[concepts/genomic-under-representation]] — CPR/DPANN episymbionts and rock-attached Geobacter/Geothrix lineages are essentially absent from the cultured cohort. [src: clay_confined_subsurface]
- [[concepts/pooled-run-pseudoreplication-and-metadata-label-noise]] — Porewater versus rock-attached compartment labels were keyword-inferred from isolation_source text. [src: clay_confined_subsurface]
- [[concepts/taxonomic-resolution-dependent-functional-inference]] — The phylum-level Bacillota_B comparison may hide genus-level differences among Desulfosporosinus, BRH-c8a, and BRH-c4a. [src: clay_confined_subsurface]
- [[concepts/occurrence-versus-catabolic-activity]] — Genome presence of toolkit modules is not protein-level expression, which the report attributes only to Bagnoud (2016). [src: clay_confined_subsurface]
