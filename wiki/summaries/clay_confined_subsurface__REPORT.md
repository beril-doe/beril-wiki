---
type: "Summary"
description: "Summary of the project Self-Sufficiency, Anaerobic Toolkit, and Cultivation Bias in Clay-Confined Cultured Bacterial Genomes."
doc_type: "short"
full_text: "sources/clay_confined_subsurface__REPORT.md"
---
# Self-Sufficiency, Anaerobic Toolkit, and Cultivation Bias in Clay-Confined Cultured Bacterial Genomes

This report asked whether cultured clay-confined bacterial genomes in the KBase Data Lakehouse show deep-subsurface signatures: sulfate reduction, an anaerobic toolkit, and biosynthetic self-sufficiency. Sulfate-reduction enrichment in deep clay isolates is strong and survives phylogenetic control. [src: clay_confined_subsurface] It also matches the Bagnoud (2016) porewater paradigm and diverges from the Mitzscherling rock-attached profile. [src: clay_confined_subsurface] The iron-reduction half of the story was withdrawn after a marker error. [src: clay_confined_subsurface] Within Bacillota_B, Wood–Ljungdahl and [NiFe]-hydrogenase carriage did not differ between deep clay and baseline isolates. [src: clay_confined_subsurface] Self-sufficiency was not supported, and the deep cohort is small. [src: clay_confined_subsurface] The report proposes follow-up work with deep-subsurface MAGs and expression-linked checks. [src: clay_confined_subsurface]

## Key Findings

### Cohort and cultivation bias

The deep clay cohort has 9 genomes: 8 from Mont Terri Opalinus boreholes and 1 from bentonite. [src: clay_confined_subsurface]

It was built from kbase_ke_pangenome.ncbi_env using clay-related isolation_source / env_* keywords, joined via genome.ncbi_biosample_id. [src: clay_confined_subsurface] The report used the kbase_ke_pangenome collection for cohort assembly, per-genome cluster mapping, KEGG/PFAM marker annotations and amino-acid pathway completeness. [src: clay_confined_subsurface]

The quality filter required CheckM ≥80% / ≤5%. [src: clay_confined_subsurface]

Filtering took anchor_deep from 9 to 6, with Mont Terri Opalinus borehole 8 (BRC-3 + BIC-A1) and bentonite formation 1. [src: clay_confined_subsurface]

anchor_shallow stayed at 30 (Coalvale silty clay 8, Cerrado clay 1, agricultural clay 21). [src: clay_confined_subsurface]

soil_baseline went from 150 to 137, phylum-stratified soil/sediment with no clay mention: Pseudomonadota 50, Bacillota 40, Bacillota_B 20, Bacteroidota 20, Actinomycetota 20. [src: clay_confined_subsurface]

The shallow comparison cohort is n=30 isolates from Coalvale, Cerrado and agricultural soils. [src: clay_confined_subsurface]

The deep genera include lineages Bagnoud (2016) found recurrent across 7 Mont Terri boreholes: Desulfosporosinus (×2), BRH-c8a (×2), BRH-c4a, Lutibacter, BRH-c54, Roseovarius and Stenotrophomonas. [src: clay_confined_subsurface] BRH-c8a is Peptococcaceae c8a in Bagnoud's nomenclature, BRH-c4a is Desulfotomaculales, Lutibacter and BRH-c54 are Bacteroidota, Roseovarius is Rhodobacterales, and Stenotrophomonas is the bentonite isolate. [src: clay_confined_subsurface]

The report describes porewater-cultured Mont Terri organisms as sulfate-reduction-rich and rock-attached communities as iron-reduction-rich. [src: clay_confined_subsurface] All 8 Opalinus genomes trace to BRC-3 or BIC-A1 borehole sources. The report reads this as a direct quantitative diagnostic that cultivation captures the porewater fraction, not the rock-attached fraction. [src: clay_confined_subsurface] It also says the Desulfosporosinus and BRH-c8a lineages match the three MAGs Bagnoud detected across seven boreholes, which it presents as cross-platform validation of indigeneity. [src: clay_confined_subsurface]

The report claims the first quantitative test of the porewater-versus-rock-attached dichotomy in cultured pangenome data. [src: clay_confined_subsurface] Bagnoud and Mitzscherling described it at community level. The report says it is preserved at genome-content level among cultured isolates, with the cohort unambiguously on the porewater side. [src: clay_confined_subsurface] It proposes comparing observed cohort SR/IR marker rates with published rock-attached frequencies as a p-valued cultivation-bias diagnostic for future cohorts. [src: clay_confined_subsurface]

The porewater-bias test (06_h3_porewater_bias.ipynb) applies binomial tests against the Mitzscherling rock-attached null and pairwise cohort Fisher tests on SR versus IR. [src: clay_confined_subsurface]

### Sulfate reduction (stands)

The deep cohort is enriched for sulfate-reduction (SR) markers (5/9 = 56%). [src: clay_confined_subsurface] The Mitzscherling et al. (2023) rock-attached null has SRB ~0.2% and IRB ~7% of community. [src: clay_confined_subsurface] Mitzscherling et al. reported SRB <0.2% and IRB 4.3–10.2%, dominated by Geobacter and Geothrix. [src: clay_confined_subsurface] Against the null the SR binomial p is 4.0×10⁻¹², with 5 observed versus 0.018 expected of 9. [src: clay_confined_subsurface] The IR depletion test against the null was not significant (n=9, observed 1, expected 0.63, p=0.87). [src: clay_confined_subsurface] The correction keeps the SR finding, because the SR markers were correctly identified. [src: clay_confined_subsurface]

Against the cultured shallow cohort, Fisher's exact gives OR=∞, p=2×10⁻⁴ for SR_complete. [src: clay_confined_subsurface] Against the soil baseline, the pairwise comparison gave OR=33.8 and p=5×10⁻⁵. [src: clay_confined_subsurface] Shallow versus soil baseline was not significant (OR=0.0, p=0.59). [src: clay_confined_subsurface] SR_complete occurred in 5/9 deep genomes versus 5/140 soil baseline genomes (OR=33.8, p_BH=2.5×10⁻⁴). [src: clay_confined_subsurface] The anchor_deep versus soil_baseline marker comparisons used per-marker Fisher tests with BH-FDR (Benjamini-Hochberg false discovery rate) adjustment. [src: clay_confined_subsurface]

Marker-class breakdown (CheckM-filtered):

| Cohort | IR_only | SR_only | both | neither |
|---|---|---|---|---|
| anchor_deep | 1 | 5 | 0 | 3 [src: clay_confined_subsurface] |
| anchor_shallow | 15 | 0 | 0 | 15 [src: clay_confined_subsurface] |
| soil_baseline | 29 | 4 | 1 | 106 [src: clay_confined_subsurface] |

Five of nine anchor_deep genomes carry the Sat, AprAB, DsrAB sulfate-reduction module. [src: clay_confined_subsurface] Seven carry group 1 [NiFe]-hydrogenase markers, including direct hits on BRH-c8a and Desulfosporosinus lineages. [src: clay_confined_subsurface] Bagnoud's Opalinus food web had Desulfobulbaceae c16a expressing complete Wood–Ljungdahl, group 1 [NiFe]-hydrogenase and Sat–AprAB–DsrAB, with three MAGs recurring across seven boreholes. [src: clay_confined_subsurface] Bagnoud (2016) reported protein-level expression of the toolkit modules. [src: clay_confined_subsurface] The report says its H3 result directly replicates this paradigm at population-genome level. [src: clay_confined_subsurface]

The report also says H3 directly diverges from the Mitzscherling rock-attached profile. Because the Lakehouse has no rock-attached MAGs from Mont Terri, it calls this divergence mechanistic: it shows what cultivation-accessible cohorts miss. [src: clay_confined_subsurface] H3 compartment results were robust to two stricter compartment definitions. [src: clay_confined_subsurface]

### Iron reduction (withdrawn and corrected)

The original iron-reduction (IR) analysis was driven by misidentified markers. [src: clay_confined_subsurface] K07811, K17324 and K17323 are TMAO reductase and glycerol ABC (ATP-binding cassette) transporter ATP-binding and permease genes, not iron-reduction genes. [src: clay_confined_subsurface] KEGG has no canonical KO (KEGG ortholog) for Geobacter omcS or Shewanella mtr multi-heme cytochromes, so unrelated genes were substituted. [src: clay_confined_subsurface] A sister project independently flagged this as a systematic problem for niche genes. [src: clay_confined_subsurface]

The withdrawn results include the 3.7-fold shallow-clay IR enrichment (p=0.0025). [src: clay_confined_subsurface] The narrative that the cohort diverges from the Mitzscherling community because shallow clay is IR-rich is also withdrawn. [src: clay_confined_subsurface] The corrected analysis uses a triple-signal multi-heme cytochrome detector: PF02085, PF22678 and ≥4 CXXCH motifs. [src: clay_confined_subsurface]

- anchor_deep (n=9): original IR marker rate 11.1%, corrected multi-heme rate 55.6%. [src: clay_confined_subsurface]
- anchor_shallow (n=30): original 50.0%, corrected 40.0%. [src: clay_confined_subsurface]
- soil_baseline (n=149): original 20.1%, corrected 40.9%. [src: clay_confined_subsurface]

After correction the pattern reverses (deep slightly higher than shallow), and no cohort comparison is significant (all Fisher p ≥ 0.46). [src: clay_confined_subsurface] The porewater-bias headline therefore holds on the SR side alone, and the rock-attached versus porewater dichotomy is unsupported on the IR side. [src: clay_confined_subsurface] With the original markers, IR_complete was 1/9 deep versus 30/140 baseline (OR=0.46, p_BH=0.69). [src: clay_confined_subsurface]

### Anaerobic toolkit and phylogenetic confound

Deep isolates carry a higher mean toolkit score (1.89 versus 0.39 in soil baseline and 0.03 in shallow clay, of 3 modules: Wood–Ljungdahl, group 1 [NiFe]-hydrogenase, and dissimilatory SR). [src: clay_confined_subsurface]

- anchor_deep (n=9): WL=0.556, NiFe=0.778, SR=0.556, mean toolkit=1.889, % toolkit=3 0.556. [src: clay_confined_subsurface]
- anchor_shallow (n=30): WL=0.000, NiFe=0.033, SR=0.000, mean toolkit=0.033, % toolkit=3 0.000. [src: clay_confined_subsurface]
- soil_baseline (n=140): WL=0.107, NiFe=0.250, SR=0.036, mean toolkit=0.393, % toolkit=3 0.021. [src: clay_confined_subsurface]

Versus soil baseline, Wood–Ljungdahl had OR=10.4, p_BH=0.004. [src: clay_confined_subsurface] [NiFe]-hydrogenase had OR=10.5, p_BH=0.004. [src: clay_confined_subsurface] Nif_complete was 4/9 versus 18/140 (OR=5.4, p_BH=0.035). [src: clay_confined_subsurface]

A within-phylum control undercuts the habitat reading for Wood–Ljungdahl and [NiFe]-hydrogenase. Bacillota_B contains Desulfosporosinus, BRH-c4a and BRH-c8a, which dominate the deep cohort. [src: clay_confined_subsurface] It carries Wood–Ljungdahl and [NiFe]-hydrogenase at high background rates, with a baseline toolkit mean of 1.65. [src: clay_confined_subsurface] Within Bacillota_B, Wood–Ljungdahl (5/5 vs 15/19, p=0.54) and [NiFe]-hydrogenase (5/5 vs 14/19, p=0.54) do not differ. [src: clay_confined_subsurface] Both have OR=∞ and BH-adjusted p=1.0. [src: clay_confined_subsurface] Only SR survives: 5/5 versus 4/19 (OR=∞, p=0.003, p_BH=0.04). [src: clay_confined_subsurface] The report describes the 5/5 Bacillota_B SR enrichment as striking. [src: clay_confined_subsurface] The report summarises that cohort-level enrichment (1.89 vs 0.39) is real but mostly Bacillota_B-driven, and only sulfate reduction stays enriched within phylum (p_BH=0.04). [src: clay_confined_subsurface] It warns that phylum control changes which signals survive. [src: clay_confined_subsurface]

The report interprets the cohort-level signal as oversampling of toolkit-carrying Desulfotomaculales and Desulfitobacteriales in clay habitats. [src: clay_confined_subsurface] It calls the pattern a phylum-level signature picked up by habitat sampling, not in-situ adaptation beyond what phylum congeners encode. [src: clay_confined_subsurface] The within-phylum result matches Beaver & Neufeld's (2024) prediction that Bacillota dominate deeper isolated fluids partly through the Wood–Ljungdahl pathway and spore formation. [src: clay_confined_subsurface]

### Biosynthetic self-sufficiency (not supported)

The Beaver & Neufeld (2024) synthesis proposes self-sufficiency as the canonical deep-subsurface adaptation, exemplified by Ca. Desulforudis audaxviator. [src: clay_confined_subsurface] GapMind amino-acid pathway completeness (out of 18) was tested with two-sided Mann–Whitney U and Cohen's d. [src: clay_confined_subsurface]

- Deep vs baseline, unfiltered (9 vs 150): means 16.22 vs 16.66, d=−0.17, p=0.153. [src: clay_confined_subsurface]
- Shallow vs baseline, unfiltered (30 vs 150): 17.87 vs 16.66, d=+0.52, p=0.006. [src: clay_confined_subsurface]
- Deep vs baseline, CheckM≥80 (6 vs 137): 15.50 vs 17.14, d=−0.84, p=0.009. [src: clay_confined_subsurface]
- Shallow vs baseline, CheckM≥80 (30 vs 137): 17.87 vs 17.14, d=+0.43, p=0.029. [src: clay_confined_subsurface]
- Deep vs baseline within Bacillota_B (4 vs 19): 16.50 vs 16.79, d=−0.13, p=0.073. [src: clay_confined_subsurface]

The negative result is consistent with critiques of streamlining or self-sufficiency as universal subsurface adaptations. Props et al. 2019 documented expansion and positive selection in oligotrophic engineered cooling water. [src: clay_confined_subsurface] Cortez et al. 2022 showed streamlining is acidophile-specific. [src: clay_confined_subsurface] The report asserts the archetype holds for uncultivated MAG/SAG lineages such as Ca. Desulforudis audaxviator but does not propagate to the cultivable cohort. [src: clay_confined_subsurface]

## Caveats and Open Work

- The IR results are withdrawn, and the rock-attached versus porewater dichotomy is only half supported. [src: clay_confined_subsurface]
- The negative self-sufficiency result is read as showing that the cultured cohort lacks the extreme self-sufficient lineages, which are characteristically uncultivated MAGs (metagenome assembled genomes) or single-cell genomes. [src: clay_confined_subsurface]
- The 18-pathway GapMind universe has a ceiling, since most cultured organisms reach 17–18/18. [src: clay_confined_subsurface] The report likewise says it saturates near 18 for most cultivable bacteria, limiting upper-end resolution. [src: clay_confined_subsurface] It suggests a finer metric, such as presence of all standard amino-acid biosynthesis EC (Enzyme Commission) numbers in eggNOG, as a sensitivity check. [src: clay_confined_subsurface]
- Cohorts are small: 6 deep genomes after filtering, and 4 within Bacillota_B. [src: clay_confined_subsurface] With n=9 deep genomes only large effects (Cohen's d > 0.7) are reliably detectable in unfiltered comparisons. [src: clay_confined_subsurface] Marginal p-values, such as H1 within-Bacillota_B p=0.07, are descriptive. [src: clay_confined_subsurface]
- The "n=5 vs 19" structure of the Bacillota_B comparison may hide further granularity, because Desulfosporosinus, BRH-c8a and BRH-c4a may differ in which non-SR features they carry. [src: clay_confined_subsurface] A within-Bacillota_B genus-level pangenome analysis could surface the deep-clay-specific accessory genome. [src: clay_confined_subsurface]
- The cohort is cultured-only, so conclusions apply to cultivable porewater-cultured deep-clay isolates, not the full Mont Terri / bentonite community. [src: clay_confined_subsurface] CPR (candidate phyla radiation) / DPANN episymbionts and rock-attached Geobacter / Geothrix lineages are essentially absent. [src: clay_confined_subsurface] MAG-augmented work is needed to test whether the real community matches literature predictions. [src: clay_confined_subsurface]
- The compartment field is keyword-inferred from isolation_source strings, so some bentonite or rock entries could be porewater or rock-attached. [src: clay_confined_subsurface]
- eggNOG annotations propagate within ≥90% AAI clusters, so strain-level variants such as a single non-functional dsrA in a complete operon may be missed. [src: clay_confined_subsurface]

### Proposed next steps

- The report's strongest proposed next step is to ingest deep-subsurface MAGs from Mont Terri, Olkiluoto, MX-80 bentonite and Oak Ridge into the pangenome and re-run the H1/H2/H3 framework with the expanded cohort. This would test whether the self-sufficiency signal (H1) emerges once rock-attached and uncultivated lineages are present. [src: clay_confined_subsurface]
- An exploratory within-Mont-Terri comparison of the BRC-3 porewater and BIC-A1 borehole genomes (5 + 3 genomes per borehole) could test whether the Bagnoud-paradigm SR-rich pattern is borehole-specific or site-wide. [src: clay_confined_subsurface]
- Granite-hosted (Olkiluoto), basalt-hosted (Oak Ridge) and salt-cavern subsurface cohorts in the KBase Data Lakehouse or future ingests could be tested with the same SR/IR marker framework. [src: clay_confined_subsurface]
- For Lakehouse Opalinus genomes that match Bagnoud's MAGs by ANI (average nucleotide identity), a future project could ask whether the observed gene presence corresponds to expression-validated activity. [src: clay_confined_subsurface]

## Slots Into

- [[concepts/cultivation-bias-toward-porewater-versus-rock-attached-subsurface-communities]]: all 8 Opalinus genomes come from borehole sources, a diagnostic of porewater capture, and SR enrichment against the rock-attached null gives p=4.0×10⁻¹². [src: clay_confined_subsurface]
- [[concepts/phylum-level-confounding-of-habitat-specific-anaerobic-gene-content]]: within Bacillota_B, only SR survives. [src: clay_confined_subsurface]
- [[concepts/biosynthetic-self-sufficiency-as-a-deep-subsurface-adaptation]]: deep clay is not above baseline in GapMind completeness. [src: clay_confined_subsurface]
- [[concepts/iron-and-sulfate-reduction-signatures-in-clay-subsurface-porewater-versus-rock-attached-communities]]: the SR signal stands and the IR signal is withdrawn. [src: clay_confined_subsurface]
- [[concepts/reliability-of-kegg-ortholog-markers-for-multi-heme-cytochrome-iron-reduction]]: KEGG has no canonical KO for omcS or mtr cytochromes. [src: clay_confined_subsurface]
