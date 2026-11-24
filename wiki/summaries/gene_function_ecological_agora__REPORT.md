---
type: "Summary"
description: "Summary of the project Gene Function Ecological Agora."
doc_type: "short"
full_text: "sources/gene_function_ecological_agora__REPORT.md"
---
# Gene Function Ecological Agora

This report builds an atlas of gene-family innovation and horizontal gene transfer (HGT) across GTDB bacteria. Its producer score is paralog expansion above a per-rank null [src: gene_function_ecological_agora], and its consumer z-score is parent-phylum dispersion against a permutation null. [src: gene_function_ecological_agora] The atlas holds 13.7M rank × clade × KO producer/participation scores. [src: gene_function_ecological_agora] The pilot passed its gate with revision. [src: gene_function_ecological_agora] Some hypotheses were falsified or not reproduced at full scale. [src: gene_function_ecological_agora]

## Key Findings

### Pilot controls and null models

Positive controls behave as expected. The natural_expansion class (200 UniRef50 clusters with within-species paralog count ≥ 3 and presence in ≥ 5 pilot species) [src: gene_function_ecological_agora] has producer z that grows with rank. The means are +0.13 σ at genus (95% CI [0.08, 0.18], n = 975), +0.31 σ at order (CI [0.22, 0.39], n = 654) and +0.55 σ at phylum (CI [0.43, 0.67], n = 457). [src: gene_function_ecological_agora]

Negative controls were revised under M2. The report calls the negative producer scores of dosage-constrained genes biologically correct, because such genes carry fewer paralogs than typical genes at matched prevalence. [src: gene_function_ecological_agora] It labels this a methodology revision, not a methodology failure. [src: gene_function_ecological_agora] Negative controls then behaved correctly under M2. [src: gene_function_ecological_agora]

### Consumer z and vertical inheritance

The consumer z-score measures parent-phylum dispersion against a permutation null. The informative subset is UniRef50s in ≥ 3 clades. [src: gene_function_ecological_agora] At family rank the informative mean was −3.95 (n_informative = 329), interpreted as strong vertical inheritance. [src: gene_function_ecological_agora] The report says the class-rank approach of dispersion to the null is consistent with cross-class HGT becoming detectable above noise. It says vertical inheritance dominates from genus through order. [src: gene_function_ecological_agora]

### Null results on Alm 2006 and two-component systems

Two-component-system (TCS) histidine kinase (HK) UniRef50 clusters showed mean producer z ≈ −0.2 across all ranks, with only 4–11% above zero. [src: gene_function_ecological_agora] At order rank, 157 were scored, 7 (4%) were positive, and mean z was −0.19. [src: gene_function_ecological_agora] At phylum rank, 186 were scored, 9 (5%) were positive, and mean z was −0.23. [src: gene_function_ecological_agora] The report notes that each UniRef50 typically matches a single HK variant and cannot aggregate to the family. [src: gene_function_ecological_agora] It says the Phase 1A negative result rules out the interpretation that any sequence-cluster-level methodology will reproduce Alm 2006. [src: gene_function_ecological_agora]

At full GTDB scale, the Alm 2006 r ≈ 0.74 (TCS HK count versus LSE fraction) was not reproduced. Four framings gave r=0.10–0.29 (n=18,989). [src: gene_function_ecological_agora]

### Control detection

The v1 control detection used eggnog_mapper_annotations.PFAMs, which stores domain names rather than accessions. [src: gene_function_ecological_agora] Adding InterProScan accessions raised detected TCS HKs from 38,488 to 43,217, a 1.1× gain. [src: gene_function_ecological_agora] The v1 implementation needed 8 bug-fixing iterations, and results stabilized after the switch to InterProScan. [src: gene_function_ecological_agora] AMR alone failed the 80% coverage threshold, at 68.8%. The report calls this biologically expected for environmental and uncultivated lineages. [src: gene_function_ecological_agora] It also says a cross-phylum dispersion null makes intra-phylum AMR HGT look clumped. [src: gene_function_ecological_agora]

### Gate verdicts and diagnostics

The Phase 1A → 1B verdict was PASS_WITH_REVISION. [src: gene_function_ecological_agora] Alm 2006 reproduction was deferred to Phase 2/3. [src: gene_function_ecological_agora] Phase 1B could proceed at full GTDB scale (27,690 species, all UniRef50s) with M1–M4 applied. [src: gene_function_ecological_agora]

The NB08b relative-threshold test separated CAZymes from housekeeping genes by +0.78 σ at family rank (p = 1×10⁻⁴³). The effect is small, with Cohen's d of about 0.07–0.09. [src: gene_function_ecological_agora] The tree-aware Sankoff parsimony metric (NB08c) recovered positive HGT above negative housekeeping at p = 2.1×10⁻⁵. [src: gene_function_ecological_agora] The Phase 1B verdict was PASS_REFRAMED + qualified. Substrate hierarchy became an empirical bet on Phase 2 amplification, not an established conclusion. [src: gene_function_ecological_agora]

### Atlas, hypotheses and ecological grounding

The Producer × Participation categories are Innovator-Isolated, Innovator-Exchange, Sink-Broker-Exchange and Stable. Classification is direction-agnostic at deep ranks. [src: gene_function_ecological_agora] The effect-size signature uses KO-level Sankoff parsimony against per-rank nulls. [src: gene_function_ecological_agora]

- **Bacteroidota Innovator-Exchange on PUL CAZymes:** falsified at the deep-rank absolute-zero criterion. The UniRef50 NB08c diagnostic still recovered a small consumer-z signal of d=0.15. [src: gene_function_ecological_agora] Bacteroidota profiled as saccharolytic and glycoside-hydrolase-rich (n=577) [src: gene_function_ecological_agora], with 1.5× anaerobe enrichment. [src: gene_function_ecological_agora]
- **Mycobacteriaceae:** 7.88× enriched in host-pathogen environments, p<10⁻⁴⁵. [src: gene_function_ecological_agora]
- **Cyanobacteria PSII:** supported at class rank, but genus rank was too sparse to evaluate. [src: gene_function_ecological_agora] Cyanobacteriia were 2.77× enriched in photic aquatic environments, p<10⁻⁵². [src: gene_function_ecological_agora] Cluster 0 was marine+sponge dominant. [src: gene_function_ecological_agora]
- **MGE context:** the report regards per-cluster PUL/mycolic MGE-machinery results (0%/0.57%) as sufficient for its headline non-phage-borne conclusion. [src: gene_function_ecological_agora]
- **External support:** the report cites Burch et al. 2023 (PMID:37232518) as independent validation of the NB11 direction at Lactobacillaceae scale. [src: gene_function_ecological_agora]

The P4-D1 audit of 18,989 species found these coverages: ncbi_env geo_loc_name 88.8% [src: gene_function_ecological_agora], ncbi_env lat_lon 47.3% [src: gene_function_ecological_agora], kescience_mgnify biome_id 28.4% (5,392 species) with 18 biome categories [src: gene_function_ecological_agora], and NMDC species-taxid overlap 9.4% (1,791 species). [src: gene_function_ecological_agora] Biome assignment combined MGnify, ENVO env_broad_scale and isolation_source, covering 76.8–88.8%. [src: gene_function_ecological_agora] The first audit was wrong: it had recommended 5–7 days using only GTDB metadata, BacDive, NMDC and Fitness Browser. [src: gene_function_ecological_agora] Adding the overlooked substrates made P4-D1 a 3-day effort and substantially stronger. [src: gene_function_ecological_agora]

### Robustness and methods contributions

All atlas claims survived annotation-density residualization. [src: gene_function_ecological_agora] Producer_z was bias-immune (R²=0.000). Consumer_z carried small bias (R²=0.053) that changed no verdict. [src: gene_function_ecological_agora] The per-rank null and Producer × Participation framework categorizes clades without a direction at deep ranks, where DTL reconciliation is not tractable. [src: gene_function_ecological_agora] The report also demonstrated a pangenome-to-genome-context cross-walk for PSII MGE-cargo analysis. [src: gene_function_ecological_agora]

## Opening of the report

This part of the report gives its status and headline outcomes: all phases are closed, 2 of 4 pre-registered hypotheses were confirmed, and several literature comparisons, nulls and review responses are recorded. [src: gene_function_ecological_agora]

### Status and hypothesis outcomes

The report declares Phases 1A/1B/2/3 closed and Phase 4 complete, with P4-D1 through P4-D5 all closed. [src: gene_function_ecological_agora] Two of four pre-registered hypotheses were confirmed: Mycobacteriaceae × mycolic-acid Innovator-Isolated (NB12) and Cyanobacteria × PSII (photosystem II) Innovator-Exchange at class rank (NB16). [src: gene_function_ecological_agora] Both survive D2 residualization and are grounded in expected biomes at p < 10⁻¹¹. [src: gene_function_ecological_agora] The D2 annotation-density bias residualization was done in P4-D5, which closes what the report calls a long-standing pre-registration debt. [src: gene_function_ecological_agora] Phenotype anchors confirm the Mycobacteriaceae and Phase 1B Bacteroidota predictions. [src: gene_function_ecological_agora]

### Mobile-element context

The report interprets per-cluster MGE-machinery results (0%, 0%, 0.57%) and the PSII gene-neighborhood result (10.91% against a Poisson expectation of 10.6%) as showing that the PSII, PUL (polysaccharide utilization locus) and mycolic atlas KOs (KEGG orthologs) are not phage-borne. [src: gene_function_ecological_agora]

### Ecological and phenotype grounding (P4-D1)

NB23+24+25 find Cyanobacteriia 2.77× photic aquatic enrichment (p<10⁻⁵²). [src: gene_function_ecological_agora] They find Mycobacteriaceae 7.88× host-pathogen enrichment (p<10⁻⁴⁵). [src: gene_function_ecological_agora] They find Bacteroidota 1.40× gut/rumen enrichment (p<10⁻³⁵). [src: gene_function_ecological_agora] BacDive phenotype anchors confirm mycobacterial aerobic-rod and Bacteroidota saccharolytic profiles. [src: gene_function_ecological_agora] AlphaEarth environmental clustering recovers ecological structure, with focal clades concentrated in expected environmental clusters. [src: gene_function_ecological_agora]

### Literature comparisons and nulls

NB11 H1 is reframed. Its direction supports the Jain 1999 complexity hypothesis at small effect size, and the report says Burch et al. 2023 (PMID:37232518, PubMed identifier) independently validated it in the same direction. [src: gene_function_ecological_agora] The report did not reproduce Alm 2006 r ≈ 0.74 at GTDB scale; P4-D3 gave r = 0.10–0.29. [src: gene_function_ecological_agora] Methodological generalization of Alm 2006 holds (NB17 architectural concordance r = 0.67), but point-estimate reproduction does not. [src: gene_function_ecological_agora] P4-D4 returns an informative atlas-scale null, which the report reads as M22 and pangenome openness measuring distinct evolutionary phenomena. [src: gene_function_ecological_agora]

### Synthesis (NB28, v3.2)

The final synthesis pass provides 6 data deliverables and 7 figures. [src: gene_function_ecological_agora] M26 adds tree-based parsimony donor inference at genus rank, distinct from the deferred composition-based M25. [src: gene_function_ecological_agora] Per-hypothesis leaf_consistency (LC) is 0.88 for PSII, read as canonical class-defining. [src: gene_function_ecological_agora] PUL is 0.41, read as a phylum tendency. [src: gene_function_ecological_agora] Mycolic is 0.15, below the atlas value of 0.20, which reveals within-Mycobacteriaceae heterogeneity. [src: gene_function_ecological_agora] In the review response, the mycolic-positive sub-clade (10 of 13 genera) has producer Cohen's d=0.39 against family-rank d=0.31, a modest amplification. [src: gene_function_ecological_agora] The report adds 3 new verified citations (Williams 2024, López Sánchez 2026, Gisriel 2023). [src: gene_function_ecological_agora]

### Multiple testing and review

NB30's correction finds that 14 of 16 formal hypothesis tests survive family-wise Bonferroni. [src: gene_function_ecological_agora] The two that do not, Mycobacteriaceae × soil and NB11 regulatory-versus-metabolic, are null results the project already reports as such. [src: gene_function_ecological_agora] The report rejects the reviewer's "26-revision × FWER" framing as a category mistake, because M1–M26 are pre-registration corrections, not 26 alternative tests. [src: gene_function_ecological_agora] A chronological trail preserves each adversarial-review response, diagnostic and methodology revision (M1–M26) across 28 notebooks in 4 phases plus a synthesis pass. [src: gene_function_ecological_agora]

## Project Headlines: Pre-registered hypothesis verdicts

This part of the report gives verdicts on the pre-registered hypotheses. Three of the four main hypotheses are supported, one of them with a qualification. The fourth, an Alm 2006 reproduction, failed at GTDB scale. [src: gene_function_ecological_agora] The report states that 3 of 4 confirmed hypotheses survive D2 annotation-density residualization, are grounded in expected biomes at p<10⁻¹¹, are non-phage-borne, and have characterized within-clade structure. [src: gene_function_ecological_agora]

### H1: Bacteroidota PUL (polysaccharide utilization locus), Innovator-Exchange

The verdict is a qualified pass. Deep-rank absolute-zero is falsified, but the Sankoff diagnostic recovers, with atlas d=0.15 in NB08c. [src: gene_function_ecological_agora] Phenotype anchors are saccharolytic and GH-rich (n=577, NB24). [src: gene_function_ecological_agora] NB26c finds 0% MGE-machinery (mobile genetic elements), and the table cites Sonnenburg 2010 for ICE-mediated transfer. [src: gene_function_ecological_agora] PUL LC (leaf consistency) is 0.41, 2× atlas. The report reads this as a phylum tendency with within-phylum heterogeneity, consistent with Yu 2025. [src: gene_function_ecological_agora] See [[entities/bacteroidota]] and [[entities/leaf-consistency]].

### H2: Mycobacteriota mycolic-acid, Innovator-Isolated

Supported. NB12 gives producer d=+0.31 and consumer d=−0.19. [src: gene_function_ecological_agora] Phenotype anchors are aerobic-rod, Gram+ and catalase (n=318, NB24). [src: gene_function_ecological_agora] NB26c finds 0.57% MGE-machinery, and the table cites Marrakchi 2014 for chromosomal localization. [src: gene_function_ecological_agora]

Mycolic LC is 0.15 (0.75× atlas). The report reads this as sub-clade-specific rather than pan-family, with the mycolic-positive species in the M. tuberculosis / M. leprae complexes. [src: gene_function_ecological_agora] NB28f S7 gives LC 0.15 against an atlas reference of 0.20. It shows the family-rank finding is driven by mycolic-acid-positive species, not the family as a whole. [src: gene_function_ecological_agora] The synthesis therefore narrows the claim to sub-clades of Mycobacteriaceae. It treats the family-rank d=0.31 as a population-mixture average. [src: gene_function_ecological_agora] See [[entities/mycobacteriaceae]].

### H3: Cyanobacteria PSII (photosystem II), Innovator-Exchange

Supported at class rank, with NB16 producer d=+1.50 and consumer d=+0.70. [src: gene_function_ecological_agora] PSII shows 0% MGE-machinery in NB26c. Its gene-neighborhood association is 10.91% in NB26g, approximately the baseline of 10.6%. [src: gene_function_ecological_agora] The table notes that BacDive coverage is thin (n=4), which limits the phenotype grounding. [src: gene_function_ecological_agora] It also reports environmental cluster 0 as marine 35.6% (NB25). [src: gene_function_ecological_agora]

PSII LC is 0.88 (4.4× atlas). The report calls this canonical class-defining innovation and says it validates the Cardona 2018 framing. [src: gene_function_ecological_agora]

The result depends on rank. Genus rank is STABLE (n=2,350, d=0.08). [src: gene_function_ecological_agora] Class rank is INNOVATOR-EXCHANGE (n=21, d=1.50). [src: gene_function_ecological_agora] Phylum rank is INNOVATOR-ISOLATED (d=1.60). [src: gene_function_ecological_agora] The report regards class rank as biologically appropriate per Cardona 2018, because PSII evolved before Cyanobacteria diversified. A null at genus rank is therefore expected. [src: gene_function_ecological_agora] It calls the phylum reversal a substrate artifact caused by insufficient reference consumer data. [src: gene_function_ecological_agora] See [[concepts/clade-level-innovation-signals-and-their-rank-dependence]].

### H4: Alm 2006 reproduction (null result)

Alm 2006 r ≈ 0.74 was not reproduced at GTDB scale. The hypothesis table gives r=0.10–0.29 (n=18,989). [src: gene_function_ecological_agora] P4-D3 reports the same range. [src: gene_function_ecological_agora] The report says methodology generalization holds, with NB17 architectural concordance r=0.67. Point-estimate reproduction does not survive scaling from 207 to 18,989 genomes. It names three mechanisms: substrate-scale heterogeneity, tree-aware versus paralog-count operationalization, and tree-rank granularity. [src: gene_function_ecological_agora]

### Bonus: NB11 regulatory < metabolic

The hypothesis of regulatory < metabolic at d≥0.3 is reframed as a small effect. Consumer d=−0.21 is in the Jain 1999 direction, and the table says Burch 2023 validates it. [src: gene_function_ecological_agora] The NB11 table reports regulatory MGE 4.13% against metabolic MGE 0.37%. [src: gene_function_ecological_agora] See [[concepts/complexity-hypothesis-regulatory-versus-metabolic-gene-transfer-asymmetry]].

### Robustness and supporting results

The D2 annotation-density residualization finds producer_z bias-immune (R²=0.000). [src: gene_function_ecological_agora] It finds a small consumer_z bias (R²=0.053) that does not change any verdict. [src: gene_function_ecological_agora]

The report regards the per-cluster MGE-machinery measurements (0% for PUL, 0.57% for mycolic) as sufficient for its headline non-phage-borne conclusion. [src: gene_function_ecological_agora] The PUL and mycolic gene-neighborhood analysis was deferred. The cross-walk pipeline hit a pandas-merge out-of-memory failure at 723K Bacteroidota focal features × 210K contigs. [src: gene_function_ecological_agora] Only the PSII gene-neighborhood analysis shipped, at 10.91% MGE-neighbor at random baseline. [src: gene_function_ecological_agora]

Other results from the report:
- Architectural promiscuity correlates with HGT (horizontal gene transfer) propensity (NB15). Mixed-category KOs (KEGG orthologs) show a median of 46 architectures/KO, against 1 for PSII. [src: gene_function_ecological_agora]
- NB17 gives a consumer-side architectural-versus-KO concordance of r=0.67. The report frames it as the analog of Denise 2019, "modular systems exchange more". [src: gene_function_ecological_agora]
- The recent-to-ancient acquisition ratio is a function-class signature (NB10b/M22). CRISPR-Cas is at 24.5× (HGT-active). [src: gene_function_ecological_agora] Housekeeping-strict is at ~1×, read as vertical inheritance. [src: gene_function_ecological_agora]

### Methods and their status

- The report documents 26 methodology revisions, structured as pre-registration corrections and post-hoc diagnostic responses. [src: gene_function_ecological_agora]
- Producer × Participation (M5/M6) is the atlas's direction-agnostic per-clade framework. It sorts deep-rank clades into Innovator-Isolated, Innovator-Exchange, Sink-Broker-Exchange or Stable, using per-rank null models with prevalence-binned cohorts. [src: gene_function_ecological_agora]
- The NB08c diagnostic showed the parent-rank dispersion permutation null was the wrong metric. [src: gene_function_ecological_agora] [[entities/sankoff-parsimony]] with M22 recipient-rank gain attribution replaced it. It gives a tree-aware acquisition-depth signal at full GTDB scale, with 17M gain events on an 18,989-leaf tree. [src: gene_function_ecological_agora]
- Tree-based parsimony donor inference at genus rank (M26, NB28b) uses M22, the species tree and a presence matrix. It produces Open/Broker/Sink/Closed labels with explicit ambiguity. [src: gene_function_ecological_agora] It shipped as an exploratory layer. Full DTL (duplication transfer loss) reconciliation cross-validation (Liu 2021 DTLOR / Bansal 2013) is future work. [src: gene_function_ecological_agora]
- Composition-based donor inference (M25) was deferred because per-CDS sequence is absent from the queryable KBase Data Lakehouse schemas. [src: gene_function_ecological_agora]
- Supporting frameworks are the pangenome → genome-context cross-walk (P4-D2) for cargo-on-MGE measurement [src: gene_function_ecological_agora], leaf_consistency (NB28e) for per-event uncertainty and within-clade structure [src: gene_function_ecological_agora], and the multi-substrate convergence framework (P4-D1), which combines atlas effect-size, ecology and phenotype. [src: gene_function_ecological_agora]

## Project Headlines; Final Data Catalog

This part of the report covers its review process and the final catalog of Lakehouse tables and generated data files. The catalog lists inputs from the [[entities/kbase-data-lakehouse]] and 50+ output files from 28 notebooks. [src: gene_function_ecological_agora]

### Adversarial review

The report integrated 8 adversarial review rounds. [src: gene_function_ecological_agora] It states that reviewer quality improved monotonically: REVIEW_4/5/7 had fabricated citations, verified via PubMed, while REVIEW_8 had 0 fabrications and 7/7 DOIs auto-verified. [src: gene_function_ecological_agora] A verify-before-acting protocol was established and reinforced (project memory `feedback_adversarial_verify_before_acting.md`). The report calls it obsolete for REVIEW_8, because the BERIL adversarial-review tool's auto-verifier catches DOI failures programmatically. [src: gene_function_ecological_agora] See [[concepts/adversarial-review-pre-registration-and-multiple-testing-discipline]].

### Lakehouse inputs

| Database | Tables | Role |
|---|---|---|
| `kbase_ke_pangenome` | `genome`, `gtdb_species_clade`, `gtdb_taxonomy_r214v1`, `gtdb_metadata`, `pangenome` | Core scaffold (293K genomes / 27,690 species), genome quality, species pangenome size, isolation_source [src: gene_function_ecological_agora] |
| `kbase_ke_pangenome` | `gene_cluster`, `gene_genecluster_junction`, `gene` | Species-specific cluster membership, ~1B junction rows [src: gene_function_ecological_agora] |
| `kbase_ke_pangenome` | `bakta_annotations`, `bakta_db_xrefs`, `bakta_pfam_domains`, `bakta_amr` | Bakta v1.12.0 reannotation of 132M cluster reps, UniRef tier mapping, AMR-Finder products, Pfam hits [src: gene_function_ecological_agora] |
| `kbase_ke_pangenome` | `eggnog_mapper_annotations` | KO, COG, KEGG_Pathway and BRITE annotation per gene_cluster [src: gene_function_ecological_agora] |
| `kbase_ke_pangenome` | `interproscan_domains`, `interproscan_go`, `interproscan_pathways` | Authoritative Pfam (833M hits, 83.8% cluster coverage), GO, MetaCyc and KEGG pathways [src: gene_function_ecological_agora] |
| `kbase_ke_pangenome` | `phylogenetic_tree`, `phylogenetic_tree_distance_pairs` | GTDB-r214 species tree for Sankoff, per-species distance pairs [src: gene_function_ecological_agora] |
| `kbase_ke_pangenome` | `sample`, `ncbi_env`, `alphaearth_embeddings_all_years` | P4-D1 environment grounding [src: gene_function_ecological_agora] |
| `kbase_genomes` | `feature`, `contig_x_feature`, `name` | P4-D2 neighborhood cross-walk: 1B feature records with start/end/strand/contig, and a 1B-row name table mapping pangenome gene_id ↔ feature_id [src: gene_function_ecological_agora] |
| `kescience_mgnify` | `species`, `biome`, `genome` | P4-D1 biome labels, 28.4% species coverage, 18 biomes [src: gene_function_ecological_agora] |
| `kescience_bacdive` | `sequence_info`, `strain`, `metabolite_utilization`, `physiology`, `enzyme` | P4-D1 phenotype anchoring, 32% species coverage via GCF→GCA fallback [src: gene_function_ecological_agora] |
| `nmdc_arkin` | `taxonomy_features` | P4-D1 NMDC sample-level taxa enrichment, 9.4% species coverage [src: gene_function_ecological_agora] |
| `kescience_fitnessbrowser` | `fb_pangenome_link.tsv` | P4-D1 Fitness Browser BBH (bidirectional best hit) cross-walk, 35 species, for point-validation [src: gene_function_ecological_agora] |

The environment-grounding tables give per-genome BioSample mapping (100%). [src: gene_function_ecological_agora] The BioSample environmental metadata are 4.1M-row EAV data. Coverage is 76.8% for isolation_source [src: gene_function_ecological_agora], 88.8% for geo_loc_name [src: gene_function_ecological_agora], 48.6% for env_broad_scale [src: gene_function_ecological_agora] and 47.3% for lat_lon. [src: gene_function_ecological_agora] The catalog lists 27.2% AlphaEarth 64-dim environmental vectors. [src: gene_function_ecological_agora]

### Generated data: Phases 1A and 1B

- Phase 1A pilot files (`data/p1a_pilot_*`) have 1K–9K rows and cover extraction, null models, scores, the Alm 2006 backtest and power analysis. [src: gene_function_ecological_agora]
- `p1b_full_extract_local.parquet` has 1.54M (species, UniRef50) presence and paralog-count rows. [src: gene_function_ecological_agora]
- `p1b_full_species.tsv` has 18,989 qualified species representatives with taxonomy, quality and pangenome statistics. [src: gene_function_ecological_agora]
- `p1b_full_uniref50.tsv` has 100,192 rows, a UniRef50 panel with control_class assignment. [src: gene_function_ecological_agora]
- `p1b_full_scores.parquet` has 1.29M per-(rank, clade, UniRef50) producer and consumer z-score rows. [src: gene_function_ecological_agora]
- The NB08c per-class Sankoff diagnostic recovers the H1 direction. [src: gene_function_ecological_agora]
- The Phase 1B → Phase 2 gate verdict is PASS_REFRAMED. [src: gene_function_ecological_agora]

### Generated data: Phase 2

- `p2_ko_assignments.parquet` (MinIO) has 28M per-(species, KO) presence rows, the atlas substrate. [src: gene_function_ecological_agora]
- `p2_ko_atlas.parquet` has 13.74M per-(rank × clade × KO) producer/participation rows. [src: gene_function_ecological_agora]
- `p2_ko_sankoff_gains.parquet` and `p2_m22_gains_attributed.parquet` have 17M rows of Sankoff gain events, M22 recipient-rank attribution and acquisition-depth bins. [src: gene_function_ecological_agora]
- `p2_ko_pathway_brite.tsv` has 12,932 rows of KEGG pathway and BRITE annotation per KO. [src: gene_function_ecological_agora]
- `p2_ko_control_classes.tsv` has 13,062 per-KO control-class assignments. [src: gene_function_ecological_agora]
- Each `p2_m18*_gate_decision.json` holds 1 row, a Phase 2 entry M18 amplification-gate verdict. [src: gene_function_ecological_agora]
- The `p2_nb11_*` and `p2_nb12_*` outputs hold per-test results for the NB11 regulatory-versus-metabolic diagnostic and the NB12 mycolic-acid hypothesis test. [src: gene_function_ecological_agora]

### Generated data: Phase 3

- The NB13 substrate audit (`p3_pfam_completeness_audit.tsv` and `p3_pfam_audit_decision.json`, 33 rows) documents choosing interproscan_domains over bakta_pfam_domains. [src: gene_function_ecological_agora]
- `p3_candidate_set.tsv` has 10,750 NB14 Phase 3 candidate KOs. [src: gene_function_ecological_agora]
- The NB15 architecture census covers 4 focused subsets. It reports a novel architectural-promiscuity finding of mixed 46 archs/KO versus PSII (photosystem II) 1. [src: gene_function_ecological_agora]
- The `p3_nb16_*` outputs hold per-test results for the NB16 Cyanobacteria × PSII Innovator-Exchange test. [src: gene_function_ecological_agora]
- The NB17 TCS (two-component system) HK (histidine kinase) architectural Alm 2006 back-test reports consumer concordance r=0.67. [src: gene_function_ecological_agora]
- The Phase 3 → Phase 4 gate verdict is PASS_MIXED. [src: gene_function_ecological_agora]

### Generated data: Phase 4

- `p4d1_env_per_species.parquet` is 18,992 × 97 and joins ncbi_env EAV pivots, AlphaEarth, MGnify biome and isolation_source per species. [src: gene_function_ecological_agora]
- `p4d1_biome_enrichment_tests.tsv` has 6 Fisher's exact tests for pre-registered Cyano/Mycobac/Bacteroidota hypotheses against expected biomes. [src: gene_function_ecological_agora]
- The BacDive metabolite, physiology and enzyme per-species parquet files have 137K, 6K and 94K rows. They are joined to 6,066 P1B species via GCF→GCA fallback. [src: gene_function_ecological_agora]
- `p4d1_alphaearth_clusters.tsv` has 5,157 rows of k=10 K-means environmental clusters. [src: gene_function_ecological_agora]
- `p4d2_ko_genus_mge.parquet` has 3.94M per-(KO × genus) MGE (mobile genetic elements) machinery-fraction rows, with an atlas baseline of 1.37%. [src: gene_function_ecological_agora]
- `p4d2_recent_gain_mge_attributed.parquet` has 7.95M rows of recent-gain MGE-machinery and per-hypothesis breakdowns. [src: gene_function_ecological_agora]
- In the 26,864-row `p4d2_neighborhood_psii_per_feature.parquet`, 10.91% of focal PSII features have an MGE neighbor within ±5kb. This is at the Poisson baseline. [src: gene_function_ecological_agora]
- The P4-D3 files (18,989 + 4 rows) compare per-species HPK (histidine protein kinase) counts with recent-LSE. They also give 4 framings of the Alm 2006 reproduction, all r<0.30. [src: gene_function_ecological_agora]
- The P4-D4 comparison of pangenome openness with the M22 recent-gain rate (3,539 + 894 rows) is an informative null at atlas scale. [src: gene_function_ecological_agora]

## Final Data Catalog: Notebooks (28 + auxiliary scripts)

This part of the report catalogs the data files and the 28 notebooks (plus auxiliary scripts) behind the Gene Function Ecological Agora project. It lists the final synthesis outputs first, then the notebooks by phase. [src: gene_function_ecological_agora]

### Final data outputs

The P4-D5 D2-residualized atlas and hypothesis-replication outputs hold 13.74M + 8 rows, and all hypothesis verdicts are preserved under residualization. [src: gene_function_ecological_agora] The report labels the NB28 synthesis outputs as 5 deliverables plus 1 lookup parquet. [src: gene_function_ecological_agora]

| File | Rows | Content |
|---|---|---|
| `data/p4_pre_registered_verdicts.tsv` | 5 | Formal hypothesis verdicts: atlas, ecology, phenotype, MGE (mobile genetic elements), disposition [src: gene_function_ecological_agora] |
| `data/p4_deep_rank_pp_atlas.parquet` | 13.74M | 4-category P×P atlas at all deep ranks [src: gene_function_ecological_agora] |
| `data/p4_genus_rank_quadrants_tree_proxy.tsv` | 4.06M | M26 tree-based genus-rank donor inference on the Phase 3 candidate set, classified Open/Broker/Sink/Closed [src: gene_function_ecological_agora] |
| `data/p4_concordance_weighted_atlas.parquet` | 8.64M | Genus-rank atlas joined to tree-proxy data and a concordance flag [src: gene_function_ecological_agora] |
| `data/p4_conflict_analysis.tsv` | 2.55M | Per-tuple disagreements with hypothesis classification [src: gene_function_ecological_agora] |
| `data/p4_per_event_uncertainty.parquet` | 17.07M | M22 gains linked to n_leaves_under and leaf_consistency [src: gene_function_ecological_agora] |
| `data/p4_leaf_consistency_lookup.parquet` | 13.75M | Per-(rank × clade × ko) species-with-ko / total-clade-species lookup [src: gene_function_ecological_agora] |

The per-event uncertainty file covers 97.8% of events. Its leaf_consistency falls monotonically from 0.34 for recent gains to 0.20 for ancient gains. [src: gene_function_ecological_agora]

### Mycobacteriaceae mycolic-acid response to REVIEW_9 I10

Three small files answer REVIEW_9 I10. The first has 8 rows of Mycobacteriaceae × mycolic Cohen's d at family, all-genus, mycolic-positive sub-clade and mycolic-low sub-clade ranks. [src: gene_function_ecological_agora] The second has 13 rows of per-genus mean leaf_consistency on the mycolic KO (KEGG ortholog) panel, which is the basis for the sub-clade split. [src: gene_function_ecological_agora] The third is a 1-row JSON holding the NB29 audit log and sub-clade composition. [src: gene_function_ecological_agora]

### Notebooks by phase

**Phase 1A.** These notebooks cover the pilot.
- Notebook 01 extracts a pilot of 1K species × 1.2K UniRef50. [src: gene_function_ecological_agora]
- Notebook 02 builds multi-rank producer and consumer null models. [src: gene_function_ecological_agora]
- Notebook 03 does pilot scoring, control validation and the Alm 2006 reproduction. [src: gene_function_ecological_agora]
- Notebook 04 is the Phase 1A → 1B gate, recorded as PASS_WITH_REVISION. [src: gene_function_ecological_agora]
- Notebook 04b answers REVIEW_1 with effect-size and Alm power-analysis tables. [src: gene_function_ecological_agora]

**Phase 1B.** These notebooks scale up to the full data.
- Notebook 05 extracts the full GTDB UniRef50 data, with 28M presence rows. [src: gene_function_ecological_agora]
- Notebook 06 builds the full atlas of 18,989 species × 100,192 UniRef50. [src: gene_function_ecological_agora]
- Notebook 07 tests Bacteroidota PUL (polysaccharide utilization locus) Innovator-Exchange at deep ranks. [src: gene_function_ecological_agora]
- Notebook 08 is the Phase 1B → 2 gate, recorded as PASS_REFRAMED via a tree-aware diagnostic. [src: gene_function_ecological_agora]
- Notebooks 08b and 08c add a discrimination analysis and a Sankoff parsimony diagnostic that recovers the H1 direction. [src: gene_function_ecological_agora]

**Phase 2.** These notebooks move to KOs.
- Notebooks 09 and 09b/c extract the KO atlas and run the M18 amplification gate, which records PASS at d=0.65–3.56. [src: gene_function_ecological_agora]
- NB10 produces the full KO atlas at 13.7M rows, plus recovery. [src: gene_function_ecological_agora]
- NB10b attributes acquisition depth (M22) across 17M gain events. [src: gene_function_ecological_agora]
- NB11 is the Tier-1 regulatory-versus-metabolic diagnostic, cataloged as REFRAMED in the complexity-hypothesis direction. [src: gene_function_ecological_agora]
- NB12 tests Mycobacteriaceae × mycolic acid, with H1 SUPPORTED at family and order ranks. [src: gene_function_ecological_agora]

**Phase 3.** These scripts build the candidate set and test it.
- Script 13 is the Pfam substrate audit, which chose interproscan_domains. [src: gene_function_ecological_agora]
- Script 14 selects 10,750 candidate KOs from the atlas off-(low,low). [src: gene_function_ecological_agora]
- Script 15 runs an architecture census on 4 focused subsets and reports an architectural promiscuity finding. [src: gene_function_ecological_agora]
- NB16 tests Cyanobacteriia × PSII (photosystem II) Innovator-Exchange, with H1 SUPPORTED at class rank. [src: gene_function_ecological_agora]
- NB17 backtests TCS (two-component system) HK (histidine kinase) architecture, with consumer concordance r=0.67. [src: gene_function_ecological_agora]
- Script 18 is the Phase 3 → Phase 4 gate, recorded as PASS_MIXED. [src: gene_function_ecological_agora]

**Phase 4.**
- The P4-D3 reproduction of Alm 2006 r ≈ 0.74 is recorded as NOT REPRODUCED, with r=0.10-0.29. [src: gene_function_ecological_agora]
- Script 20 performs the P4-D5 D2 annotation-density residualization. [src: gene_function_ecological_agora]
- Script 21 reports an informative null for P4-D4, which compared within-species pangenome openness with M22 recent acquisition. [src: gene_function_ecological_agora]
- Scripts 22[bcdef] audit P4-D1 substrates and record corrections for BacDive accession format, the MGnify catalog and pangenome.ncbi_env. [src: gene_function_ecological_agora]
- Scripts 23 and 23b pull the environment substrate and run biome enrichment tests. [src: gene_function_ecological_agora]
- Scripts 24 and 24b anchor BacDive phenotypes. [src: gene_function_ecological_agora]
- Script 25 runs AlphaEarth k=10 environment clustering. [src: gene_function_ecological_agora]
- Script 26 and its auxiliary iterations handle MGE context and the gene-neighborhood pipeline. [src: gene_function_ecological_agora]
- Prefix 27 is reserved and skipped, because P4-D5 was assigned 20. [src: gene_function_ecological_agora]
- The NB28 synthesis scripts cover verdicts, the 4-category atlas, tree-based donor inference, concordance, leaf_consistency and 10 figures. [src: gene_function_ecological_agora]

## Final Data Catalog; Phase 1A scope; Key Findings

This part of the report covers the final atlas-level signatures, the audit trail and runtime, the Spark lessons, and the Phase 1A null-model calibration. Phase 1A passed its gate with revision. It validated the producer null on natural_expansion controls and revised the negative-control criterion. It did not reproduce the Alm 2006 result or test the pre-registered hypotheses. [src: gene_function_ecological_agora]

### Atlas-level signatures

The acquisition-depth atlas shows that the recent-to-ancient ratio is a function-class signature: CRISPR-Cas is 24.5× and housekeeping is ~1×. [src: gene_function_ecological_agora] The report says the independent leaf_consistency (LC) signal validates the housekeeping-versus-HGT-active framework. [src: gene_function_ecological_agora] Within Mycobacteriaceae, mycolic LC=0.15 falls below the atlas reference of 0.20, which the report reads as mycolic-acid-positive species forming a sub-clade. [src: gene_function_ecological_agora] The report reads PSII LC=0.88 as confirming class-defining innovation. [src: gene_function_ecological_agora] It reads PUL LC=0.41 as a phylum tendency. [src: gene_function_ecological_agora] The report also says the atlas confidence ridge independently validates the M22 acquisition-depth signal. Its explanation is that deeper gains diversify with subsequent loss, while recent gains land in clades where the KO is propagated. [src: gene_function_ecological_agora] These readings are the report's interpretations.

### Audit trail and reproducibility

The report preserves 8 adversarial review files, ADVERSARIAL_REVIEW_1.md through ADVERSARIAL_REVIEW_8.md, with phase-specific responses in REPORT.md. [src: gene_function_ecological_agora] REVIEW_8 had 0 fabrications and 7/7 DOIs auto-verified, which the report calls its highest-quality round to date. [src: gene_function_ecological_agora] A standard review dated 2026-04-29 called the project "exceptionally comprehensive ... model for computational reproducibility". It gave 5 nice-to-have suggestions and no critical or important issues. [src: gene_function_ecological_agora]

End-to-end cold-start wall time is ~6–8 hours, made up of ~3h Spark-side and ~5h pandas-side. [src: gene_function_ecological_agora] With cached intermediate parquets, the NB28a → 28f synthesis pass takes ~5 minutes. [src: gene_function_ecological_agora] The README.md reproduction section gives per-notebook runtime estimates and Spark-versus-local annotations. [src: gene_function_ecological_agora]

### Performance lessons

The report presents these lessons as reusable for BERIL projects with 1B-row table joins, 28M-row species-level data, and 17M event attribution. [src: gene_function_ecological_agora] See also [[concepts/spark-query-scale-limits-and-notebook-session-constraints-in-lakehouse-analyses]].

- Spark-Connect caps driver results at 1 GB serialized. The workaround is MinIO staging: write parquet with coalesce, then read it locally. [src: gene_function_ecological_agora]
- Pandas spatial merges ran out of memory at ~10M+ rows in NB26h, the Bacteroidota PUL gene-neighborhood analysis of 723K × 210K contigs. Proposed workarounds are batching or full-Spark Stage 6. [src: gene_function_ecological_agora]
- Setting Spark autoBroadcastJoinThreshold = -1 was harmful: NB10 hung 17+ min until the setting was removed. [src: gene_function_ecological_agora]
- JupyterHub's idle timeout was ~17–25 min. For NB10, 10b and 26, the report converted notebooks to scripts and used nohup and intermediate parquets. [src: gene_function_ecological_agora]
- The default driver heap ceiling was -Xmx4g. The report recommends raising it through the environment for heavy coalesce writes. [src: gene_function_ecological_agora]

### Phase 1A scope

Phase 1A calibrated multi-rank null models, both producer and consumer. [src: gene_function_ecological_agora] Its results were mixed:

- It validated that the producer null detects real paralog signal, using the natural_expansion class. [src: gene_function_ecological_agora]
- It validated negative-control behavior only under a revised criterion. [src: gene_function_ecological_agora]
- It did not reproduce Alm 2006 TCS (two-component system) HK (histidine kinase) paralog expansion at UniRef50. The v2 plan deferred this to Phases 2/3. [src: gene_function_ecological_agora]
- It did not test the four pre-registered Phase 1B/2/3 hypotheses, which require full-scale runs. [src: gene_function_ecological_agora]
- The gate decision was PASS_WITH_REVISION. [src: gene_function_ecological_agora]

### Producer null: natural_expansion controls

The natural_expansion class comprises 200 UniRef50 clusters with documented within-species paralog count ≥ 3 and presence in ≥ 5 pilot species. [src: gene_function_ecological_agora] Its producer z-scores are positive at all five ranks and grow monotonically with rank. [src: gene_function_ecological_agora] The mean producer z, with 95% CI (confidence interval) and n, is:

- genus: +0.13 σ, CI [0.08, 0.18], n = 975. [src: gene_function_ecological_agora]
- family: +0.19 σ, CI [0.13, 0.26], n = 802. [src: gene_function_ecological_agora]
- order: +0.31 σ, CI [0.22, 0.39], n = 654. [src: gene_function_ecological_agora]
- class: +0.50 σ, CI [0.38, 0.61], n = 482. [src: gene_function_ecological_agora]
- phylum: +0.55 σ, CI [0.43, 0.67], n = 457. [src: gene_function_ecological_agora]

The report concludes that the clade-matched neutral-family null detects real paralog expansion above the cohort baseline. [src: gene_function_ecological_agora]

### Negative controls and the M2 revision

Ribosomal proteins, tRNA synthetases and RNAP (RNA polymerase) core subunits show negative producer z, −0.15 to −0.24 σ across ranks, with 95% CIs entirely below zero. [src: gene_function_ecological_agora] The report calls this biologically correct. Its reasoning is that dosage-constrained genes carry fewer paralogs than typical genes at matched prevalence. [src: gene_function_ecological_agora] The report says its pre-registered "near zero" criterion was wrong. The replacement criterion is "≤ 0 with CI not strongly positive." [src: gene_function_ecological_agora] It labels this methodology revision M2, not a methodology failure. [src: gene_function_ecological_agora] The producer null therefore distinguishes dosage-constrained genes from typical paralog-expansion patterns. [src: gene_function_ecological_agora] See [[concepts/paralog-expansion-and-gene-copy-number-constraint]].

### Consumer null: rank pattern

The consumer z-score measures parent-phylum dispersion against a permutation null. The informative subset is UniRef50s in ≥ 3 clades. [src: gene_function_ecological_agora] Mean consumer z by rank:

- genus: −3.77, n informative = 423, strong vertical inheritance. [src: gene_function_ecological_agora]
- family: −3.95, n informative = 329, strong vertical inheritance. [src: gene_function_ecological_agora]
- order: −4.10, n informative = 267, peak vertical clumping. [src: gene_function_ecological_agora]
- class: −1.36, n informative = 172, clumping weakens and a cross-class HGT (horizontal gene transfer) signal is emerging. [src: gene_function_ecological_agora]

The report calls this the first interpretable biological pattern in the atlas. At class rank, UniRef50 dispersion approaches the random-permutation null, which it reads as cross-class HGT becoming detectable above noise. From genus through order, vertical inheritance dominates. [src: gene_function_ecological_agora] The report says this aligns with literature. That literature describes most prokaryotic HGT as within-phylum and cross-phylum HGT as rarer and biased toward specific function classes. [src: gene_function_ecological_agora] See [[concepts/horizontal-gene-transfer-inference-metrics-and-control-class-calibration]].

## Key Findings: Finding 4 — Alm 2006 paralog expansion does not reproduce at UniRef50 …

The report treats this as a negative result for reproducing Alm 2006 at sequence-cluster resolution, not as a methodology failure. [src: gene_function_ecological_agora] This part also covers the substrate audit, the antimicrobial resistance (AMR) control, and the gate verdict for Phase 1B. See [[concepts/paralog-expansion-and-gene-copy-number-constraint]] for the wider topic.

### TCS histidine kinases: no reproduced expansion signal

TCS HK UniRef50 clusters have a mean producer z of about −0.2 across all ranks. Only 4–11% of them score above zero. [src: gene_function_ecological_agora] A few clusters still exceed 2σ at each rank, as the table shows.

| Rank | TCS UniRefs scored | Positive z | Above 2σ | Mean producer z |
|---|---|---|---|---|
| genus | 73 | 8 (11%) | 2 | −0.10 [src: gene_function_ecological_agora] |
| family | 124 | 8 (6%) | 2 | −0.16 [src: gene_function_ecological_agora] |
| order | 157 | 7 (4%) | 3 | −0.19 [src: gene_function_ecological_agora] |
| class | 174 | 9 (5%) | 2 | −0.23 [src: gene_function_ecological_agora] |
| phylum | 186 | 9 (5%) | 2 | −0.23 [src: gene_function_ecological_agora] |

### Why the report calls this a negative result, not a failure

Alm, Huang & Arkin (2006) counted distinct HK genes per genome at the HK-family level. [src: gene_function_ecological_agora] A UniRef50 cluster typically corresponds to a single HK protein variant, so it cannot be aggregated to the family. [src: gene_function_ecological_agora] The report says the negative result rules out the simpler interpretation that any sequence-cluster-level methodology will reproduce Alm 2006. [src: gene_function_ecological_agora] It says the pilot validates the v2 substrate hierarchy. Alm 2006 reproduction is pre-registered for Phase 2 and Phase 3. Phase 2 uses KO-level aggregation with KEGG ko02020. Phase 3 uses a Pfam multidomain architecture census. [src: gene_function_ecological_agora] Gate item M3 confirms this deferral. [src: gene_function_ecological_agora]

### Substrate audit

A mid-pilot audit found that the `interproscan_domains` table in the KBase Data Lakehouse had not been used in v1. It holds 146 M Pfam hits across 132.5 M cluster representatives, with 83.8 % cluster coverage. [src: gene_function_ecological_agora] The v1 control detection used `eggnog_mapper_annotations.PFAMs`. That column stores domain names such as HisKA, not accessions such as PF00512. [src: gene_function_ecological_agora]

Switching to a union with InterProScan accessions raised the number of controls detected:

| Control | Before | After | Gain |
|---|---|---|---|
| Ribosomal proteins (UniRef50s) | 9,005 | 19,389 | 2.2× [src: gene_function_ecological_agora] |
| tRNA synthetases | 5,640 | 8,514 | 1.5× [src: gene_function_ecological_agora] |
| TCS HKs | 38,488 | 43,217 | 1.1× [src: gene_function_ecological_agora] |

At the biological level, 4 of 5 controls reach 100% coverage across pilot species. [src: gene_function_ecological_agora] Only AMR fails the 80% threshold, at 68.8%. The report calls this biologically expected, because environmental and uncultivated lineages carry less AMR. [src: gene_function_ecological_agora]

The v1 implementation went through 8 iterations of bug-fixing before the audit. Results stabilized once it switched to InterProScan. [src: gene_function_ecological_agora] The report presents the lesson as a project pattern: audit substrate before implementing, not after debugging. [src: gene_function_ecological_agora]

### AMR consumer signal and the M1 revision

AMR shows strongly negative consumer z (−4.4 to −4.8) under parent-phylum dispersion at genus, family and order ranks. [src: gene_function_ecological_agora] The report interprets this as the parent-phylum anchor masking the signal, not as an absence of HGT (horizontal gene transfer). [src: gene_function_ecological_agora] Its reasoning is that AMR HGT is intense within Pseudomonadota or Bacillota but rare across phyla. A null that measures cross-phylum dispersion therefore makes intra-phylum HGT look clumped. [src: gene_function_ecological_agora] The M1 revision sets rank-stratified parent ranks for Phase 1B: genus → family, family → order, order → class, and class → phylum. [src: gene_function_ecological_agora]

### Gate verdict

The Phase 1A → 1B gate verdict was PASS_WITH_REVISION. [src: gene_function_ecological_agora] Besides M1 and M3, two revisions apply:

- M2 sets the negative-control criterion to a confidence interval (CI) upper bound ≤ 0.5, not "near zero". [src: gene_function_ecological_agora]
- M4 accepts paralog fallback option a for Phase 1B implementation, with sensitivity reported. [src: gene_function_ecological_agora]

Phase 1B may proceed at full GTDB scale, with 27,690 species and all UniRef50s, with M1–M4 applied. [src: gene_function_ecological_agora]

## Interpretation; Data

This part of the report interprets the Phase 1A pilot. It argues that the null-model methodology has signal-to-noise and that UniRef50 suits an existence test. It also lists what remains untested and the data the pilot used. [src: gene_function_ecological_agora]

### Interpretation

The report states that the atlas methodology has signal-to-noise. The producer null is responsive, because the natural_expansion control validates it. The consumer null is responsive, because negative controls show vertical inheritance. [src: gene_function_ecological_agora] The multi-rank cross-section shows an interpretable trend: vertical clumping is strong at deep ranks and weakens at class rank. [src: gene_function_ecological_agora] Quantitatively, UniRef50 parent-phylum dispersion was z ≈ −4 σ at genus, family and order rank and weakened to z ≈ −1.4 σ at class rank. The report presents this as a quantitative anchor for the qualitative phylum-clumping consensus. [src: gene_function_ecological_agora]

The pilot formulated, calibrated and validated a multi-rank Producer × Participation framework at pilot scale. It uses a clade-matched neutral-family producer null and a parent-rank dispersion permutation consumer null on UniRef50-scale substrates. [src: gene_function_ecological_agora] The natural_expansion positive control is made of UniRefs with documented paralog signal (max paralog ≥ 3 across species). These serve as the methodology's positive ground truth. [src: gene_function_ecological_agora]

The report reads the pilot as supporting the substrate-hierarchy intuition behind the three-phase design. UniRef50 is the right resolution for the Phase 1 existence test, but it is too narrow for Alm 2006-type family-level signals. [src: gene_function_ecological_agora] The report also concludes that "near zero" was the wrong criterion for negative controls. Dosage-constraint biology demands a "≤ 0" criterion, which revision M2 captures. [src: gene_function_ecological_agora]

### Literature anchors and the Alm 2006 null result

Alm, Huang & Arkin (2006) was the principal literature anchor. It reported that two-component-system histidine kinases follow different evolutionary strategies across bacterial niches: lineage-specific paralog expansion or HGT acquisition. [src: gene_function_ecological_agora] Phase 1A did not reproduce this at UniRef50. The report calls that negative result consistent with the original grain. Alm 2006 counted distinct HK genes per genome at the HK family level, and UniRef50 cannot aggregate to that level. [src: gene_function_ecological_agora] The report also cites Smillie et al (2011) for intense within-phylum gut microbiome HGT relative to cross-phylum events. It cites Soucy et al (2015) for broader HGT patterns and Hooper et al (2007) for HGT bias toward specific function classes. [src: gene_function_ecological_agora]

For substrate choice, the report recommends InterProScan `interproscan_domains` as the default for domain-accession queries on the lakehouse. eggNOG `PFAMs` stores domain names, not accessions. [src: gene_function_ecological_agora]

### Caveats

- The Phase 1B/2/3 hypotheses are untested. These are Bacteroidota PUL Innovator-Exchange, Mycobacteriota mycolic-acid Innovator-Isolated, Cyanobacteria PSII Broker, and Alm 2006 reproduction at higher resolutions. [src: gene_function_ecological_agora]
- The atlas is not yet hypothesis-generating. Meaningful per-clade × function quadrant verdicts need the full GTDB UniRef50 atlas of Phase 1B. [src: gene_function_ecological_agora]
- The effects of methodology revisions M1–M4 are untested until Phase 1B runs. [src: gene_function_ecological_agora]
- The pilot is biologically narrow: 1,000 species across 110 phyla and 1,200 UniRef50s in 6 classes. Headline verdicts need Phase 1B at 27,690 species and all UniRef50s. [src: gene_function_ecological_agora]
- Phase 1 is acquisition-only by design. Genus-rank direction inference is reserved for the Phase 3 architectural deep-dive. [src: gene_function_ecological_agora]
- Anchoring parents at phylum is suboptimal, and Phase 1B uses rank-stratified parents. [src: gene_function_ecological_agora]
- The n_gene_clusters paralog fallback, used when UniRef90 is absent, covers 21.5% of presence rows. Phase 1B should report sensitivity with and without it. [src: gene_function_ecological_agora]
- Under-representation of CPR (candidate phyla radiation) and DPANN is an acknowledged substrate constraint, not a Phase 1A failure. [src: gene_function_ecological_agora]

### Data

The `kbase_ke_pangenome` tables used are listed below.

| Table | Use |
|---|---|
| `genome`, `gtdb_species_clade`, `gtdb_taxonomy_r214v1`, `gtdb_metadata`, `pangenome` | core scaffold for species, taxonomy, quality and pangenome size [src: gene_function_ecological_agora] |
| `gene_cluster`, `gene_genecluster_junction` | species-specific gene cluster membership [src: gene_function_ecological_agora] |
| `bakta_db_xrefs` | UniRef50/90/100 mapping per gene_cluster, from `db = 'UniRef'` rows with the tier embedded in the accession [src: gene_function_ecological_agora] |
| `bakta_amr` | AMR (antimicrobial resistance) positive controls [src: gene_function_ecological_agora] |
| `eggnog_mapper_annotations` | KO (KEGG ortholog), COG (clusters of orthologous groups), KEGG_Pathway, BRITE and PFAMs, with a domain-name fallback for control detection [src: gene_function_ecological_agora] |
| `interproscan_domains` | authoritative Pfam source for accession-based control detection [src: gene_function_ecological_agora] |
| `interproscan_go` | per-cluster GO (Gene Ontology) term annotation [src: gene_function_ecological_agora] |
| `interproscan_pathways` | MetaCyc and KEGG pathway annotation [src: gene_function_ecological_agora] |

The `kbase_uniref50` and `kbase_uniref90` collections supply small UniRef cluster reference tables. [src: gene_function_ecological_agora]

The pilot's derived files have the following row counts.

| File | Rows | Content |
|---|---|---|
| p1a_pilot_species.tsv | 1,000 | phylum-stratified species with quality and annotation density [src: gene_function_ecological_agora] |
| p1a_pilot_uniref50.tsv | 1,200 | UniRef50 pilot controls and IPR/GO/pathway enrichment [src: gene_function_ecological_agora] |
| p1a_pilot_extract.parquet | 6,638 | (species, UniRef50) presence and paralog count [src: gene_function_ecological_agora] |
| p1a_null_producer_lookup.parquet | 876 | cohort moments per rank, clade and prevalence bin [src: gene_function_ecological_agora] |
| p1a_null_consumer_lookup.parquet | 4,800 | consumer z-score per rank and UniRef50 [src: gene_function_ecological_agora] |
| p1a_uniref_prevalence_bin.tsv | 6,000 | prevalence bin per rank and UniRef50 [src: gene_function_ecological_agora] |
| p1a_pilot_scores.parquet | 9,201 | producer and consumer z-scores per rank, clade and UniRef50 [src: gene_function_ecological_agora] |
| p1a_control_validation.tsv | 30 | score summary and pass/fail verdict per rank and control_class [src: gene_function_ecological_agora] |
| p1a_alm_2006_pilot_backtest.tsv | 5 | per-rank Alm 2006 TCS HK reproduction summary [src: gene_function_ecological_agora] |

Four JSON audit logs have one row each: extraction (NB01), null diagnostics (NB02), pilot atlas diagnostics (NB03) and the formal gate verdict (NB04). [src: gene_function_ecological_agora] The human-readable gate document is p1a_phase_gate_summary.md. [src: gene_function_ecological_agora] Most data files are gitignored and planned for archival to `microbialdiscoveryforge` MinIO on submission. The JSON audit logs and the gate summary are committed to git. [src: gene_function_ecological_agora]

## Supporting Evidence; Future Directions

The supporting notebooks run from Phase 1A data extraction to the gate decision, and the report then plans four further phases. [src: gene_function_ecological_agora] Three questions remain open after the pilot. [src: gene_function_ecological_agora]

### Supporting notebooks (Phase 1A)

- Notebook 01 extracts 1K species and 1.2K UniRef50s, using InterProScan-based control detection and the natural_expansion class. [src: gene_function_ecological_agora]
- Notebook 02 builds multi-rank producer and consumer null models, from genus to phylum. [src: gene_function_ecological_agora]
- Notebook 03 scores each (rank, clade, UniRef50) combination. It also validates the controls and reproduces Alm 2006. [src: gene_function_ecological_agora]
- Notebook 04 makes the Phase 1A to Phase 1B gate decision, with the M1–M4 methodology revisions. [src: gene_function_ecological_agora]
- The post-review appendix notebook 04b computes the effect-size and Alm 2006 power-analysis tables for report v1.1 in a reproducible way. [src: gene_function_ecological_agora]

### Future directions

The report plans four more phases, and each of the first three has a pre-registered hypothesis. The time estimates are 4, 5, 5 and 2 weeks. [src: gene_function_ecological_agora]

**Phase 1B (estimated 4 weeks)** is the full GTDB UniRef50 atlas with M1–M4 applied. [src: gene_function_ecological_agora]
- It runs multi-rank producer and consumer scoring on all 27,690 GTDB species and on the full UniRef50 pool of ~1.5 M unique UniRef50s. [src: gene_function_ecological_agora]
- It applies M1, which uses rank-stratified parent ranks for the consumer null. [src: gene_function_ecological_agora]
- It applies M2, a revised negative-control criterion. [src: gene_function_ecological_agora]
- It applies M4, a paralog fallback with a sensitivity check. [src: gene_function_ecological_agora]
- It tests the pre-registered hypothesis that Bacteroidota are Innovator-Exchange on PUL (polysaccharide utilization locus) CAZymes (carbohydrate-active enzymes) at a deep-rank category. [src: gene_function_ecological_agora]

**Phase 2 (estimated 5 weeks)** is a KO-resolution functional atlas, where KO means KEGG ortholog. [src: gene_function_ecological_agora]
- It aggregates the UniRef50 atlas into KO functional categories. [src: gene_function_ecological_agora]
- It reproduces the Alm 2006 TCS (two-component system) HK (histidine kinase) paralog expansion at KO level. This is one of two canonical reproductions under the v2 plan. [src: gene_function_ecological_agora]
- It tests the pre-registered hypothesis that Mycobacteriota are Innovator-Isolated on the mycolic-acid pathway. [src: gene_function_ecological_agora]
- It tests the headline regulatory-versus-metabolic asymmetry at KEGG BRITE B-level. [src: gene_function_ecological_agora]

**Phase 3 (estimated 5 weeks)** is a Pfam architecture census plus genus-rank donor inference. [src: gene_function_ecological_agora]
- It runs a Pfam multidomain architecture census on the Phase 2 candidate KOs. [src: gene_function_ecological_agora]
- It infers donors from composition at genus rank, to give full four-quadrant labels. [src: gene_function_ecological_agora]
- It reproduces Alm 2006 at architectural resolution, which the report identifies as the resolution Alm 2006 actually used. [src: gene_function_ecological_agora]
- It tests the pre-registered hypothesis that Cyanobacteria are Broker on PSII (photosystem II) architectures at genus rank, with donor inference. [src: gene_function_ecological_agora]

**Phase 4 (estimated 2 weeks)** is a cross-resolution synthesis. [src: gene_function_ecological_agora]
- It analyses concordance and conflict across the UniRef50, KO and Pfam architecture resolutions. [src: gene_function_ecological_agora]
- It produces a final atlas heatmap and a directed flow network. [src: gene_function_ecological_agora]
- It gives verdicts on all four pre-registered hypotheses. [src: gene_function_ecological_agora]
- It delivers a methodological lesson book and a future-work roadmap. [src: gene_function_ecological_agora]

### Questions left open by Phase 1A

- Do M1's rank-stratified consumer-null parents reveal an AMR-typical intra-phylum HGT (horizontal gene transfer) signal at full scale? The report says this is testable in the Phase 1B equivalent of NB02. [src: gene_function_ecological_agora]
- Does the cross-rank consumer-z trend hold across the full UniRef50 pool? The pilot trend runs from vertical at deep ranks to null at class. The alternative is that the trend is specific to the pilot. [src: gene_function_ecological_agora]
- Is natural_expansion the right positive control for full-scale Phase 1B? The alternative is to sample more broadly across paralog-count distributions. [src: gene_function_ecological_agora]

## Phase 1A response to adversarial review (v1.1): Raw paralog-count effect sizes (addresses …

This part of the report answers an adversarial review. It adds raw paralog-count effect sizes, a power analysis for the two-component system (TCS) histidine kinase (HK) result, and explicit framing changes. [src: gene_function_ecological_agora] Its quantitative analyses are derived in a review-response notebook, with raw outputs in two TSV files. [src: gene_function_ecological_agora]

### Raw effect sizes

The reviewer noted that z-scores alone do not convey biologically meaningful effect sizes. [src: gene_function_ecological_agora] The report therefore gives raw paralog-count differences from the cohort mean. In the pilot UniRef50 analysis, natural_expansion is above cohort at every rank, and the excess shrinks from phylum to genus. Columns: rank, n, observed mean, cohort mean, raw Δ, % above cohort, producer z. [src: gene_function_ecological_agora]

- phylum: n 457, 1.77, 1.27, +0.50, +39.5%, +0.55 [src: gene_function_ecological_agora]
- class: n 482, 1.74, 1.28, +0.46, +36.0%, +0.50 [src: gene_function_ecological_agora]
- order: n 654, 1.56, 1.28, +0.28, +22.3%, +0.31 [src: gene_function_ecological_agora]
- family: n 802, 1.45, 1.27, +0.18, +14.3%, +0.19 [src: gene_function_ecological_agora]
- genus: n 975, 1.31, 1.20, +0.11, +9.3%, +0.13 [src: gene_function_ecological_agora]

At phylum rank, the other classes sit below their cohort means (same columns):

- pos_tcs_hk: n 186, 1.07, 1.30, −0.24, −18.4%, −0.23 [src: gene_function_ecological_agora]
- neg_ribosomal: n 315, 1.04, 1.18, −0.13, −11.4%, −0.15 [src: gene_function_ecological_agora]
- neg_rnap_core: n 284, 1.01, 1.20, −0.18, −15.2%, −0.24 [src: gene_function_ecological_agora]
- neg_trna_synth: n 248, 1.02, 1.20, −0.18, −15.0%, −0.19 [src: gene_function_ecological_agora]
- pos_amr: n 272, 1.17, 1.34, −0.17, −12.6%, −0.16 [src: gene_function_ecological_agora]

The report reads the ribosomal, tRNA-synth and RNAP deviations as a dosage-constrained signature, about 12–15% below the cohort baseline. [src: gene_function_ecological_agora]

### Power analysis for the TCS HK signal

The UniRef50 TCS HK analysis has a minimum detectable d at 80% power of at most 0.29 at every rank, and the observed z is negative at every rank. The test was a one-sided t-test at α=0.05. [src: gene_function_ecological_agora] Columns: rank, n, min detectable d, observed z, power if d=0.3, power if d=0.5.

- genus: 73, 0.29, −0.10, 0.81, 0.99 [src: gene_function_ecological_agora]
- family: 124, 0.23, −0.16, 0.95, 1.00 [src: gene_function_ecological_agora]
- order: 157, 0.20, −0.19, 0.98, 1.00 [src: gene_function_ecological_agora]
- class: 174, 0.19, −0.23, 0.99, 1.00 [src: gene_function_ecological_agora]
- phylum: 186, 0.18, −0.23, 0.99, 1.00 [src: gene_function_ecological_agora]

The report concludes that this rules out underpowering. At UniRef50 the TCS HK paralog signal is absent and slightly negative, and the report calls the substrate-hierarchy argument the right interpretation. [src: gene_function_ecological_agora] It attributes the lost signal to resolution. The original Alm 2006 effect lives at family resolution, where one HK family aggregates many UniRef50s. UniRef50 cannot recover that signal. [src: gene_function_ecological_agora]

### Framing changes and caveats

- The reviewer correctly noted that revising the negative-control criterion ("near zero" → "≤ 0 with CI not strongly positive") after seeing data weakens pre-registration discipline. [src: gene_function_ecological_agora]
- Dosage constraint on housekeeping genes was anticipated in plan v2. Its quantitative consequence, a negative producer z rather than zero, was not encoded in the pre-registered criterion. [src: gene_function_ecological_agora]
- The revised expectation is that negative controls show no paralog expansion and do show dosage-constraint suppression. [src: gene_function_ecological_agora]
- REVIEW_1.md and ADVERSARIAL_REVIEW_1.md are committed at the project root as the audit trail. [src: gene_function_ecological_agora]
- Plan v2.1 has a hierarchical Tier-1 / Tier-2 / Tier-3 multiple-testing strategy. The BH-FDR (Benjamini-Hochberg false discovery rate) variant and the effective-N for KEGG-BRITE × GTDB-family clusters remain TBD. [src: gene_function_ecological_agora]
- v1 was iterated, not shipped, and no v1 results were used in scientific claims. [src: gene_function_ecological_agora]
- The framework tests the regulatory-versus-metabolic asymmetry empirically rather than assuming it. [src: gene_function_ecological_agora]
- Antimicrobial resistance (AMR) is the closest current consumer-null control. The parent-phylum anchor masks intra-phylum horizontal gene transfer (HGT). [src: gene_function_ecological_agora]

### Phase 1B commitments

- Add known-HGT positive controls: β-lactamase families with documented cross-phylum spread (CARD `bla` group) and class-I CRISPR-Cas systems (Pfam family). [src: gene_function_ecological_agora]
- Make phylogenetic independent contrasts mandatory for consumer-null and producer-null score reporting. They were optional sensitivity analysis in plan v2. [src: gene_function_ecological_agora]
- Have NB02 specify the BH-FDR variant and the effective-N within KEGG BRITE × GTDB family. [src: gene_function_ecological_agora]
- Add Sichert & Cordero (2021) as literature context for the Bacteroidota polysaccharide utilization locus (PUL) hypothesis. [src: gene_function_ecological_agora]

## Phase 1B Milestone (v1.2, 2026-04-27): Finding 1B.4 — HIGH 1 cross-phylum HGT positive …

Phase 1B applied the Phase 1A methodology revisions to the full GTDB set. The milestone reports verdict `PASS_REFRAMED`, with Phases 2–4 still in planning. [src: gene_function_ecological_agora] The natural_expansion and negative control classes behave as the methodology anticipates, but the pre-registered Bacteroidota hypothesis is falsified under its absolute criterion, and one order-rank control result is unresolved. [src: gene_function_ecological_agora] A relative criterion still shows graded signal. [src: gene_function_ecological_agora]

### Scale and runtime

Phase 1B applied revisions M1–M4 to 18,989 bacterial [[entities/gtdb]] representatives and 100,192 targeted [[entities/uniref]] UniRef50s, with a 10K-per-class cap. This gave 1.54 M (species, UniRef50) presence rows and 1.29 M (rank, clade, UniRef) producer scores. [src: gene_function_ecological_agora] Wall time was ≈ 1 hour total across NB05–NB08. [src: gene_function_ecological_agora]

### Natural-expansion control: producer signal

The natural_expansion class consists of UniRefs with documented within-species paralog count ≥ 3 in ≥ 5 species. [src: gene_function_ecological_agora] At GTDB scale it shows monotone-growing positive producer z across all 5 ranks, stronger than at pilot scale. [src: gene_function_ecological_agora] See [[concepts/paralog-expansion-and-gene-copy-number-constraint]].

| Rank | Mean producer z | Raw paralog count above cohort |
|---|---|---|
| genus | +0.13 σ | +9.3 % [src: gene_function_ecological_agora] |
| family | +0.19 σ | +14.3 % [src: gene_function_ecological_agora] |
| order | +0.31 σ | +22.3 % [src: gene_function_ecological_agora] |
| class | +0.77 σ | +55.2 % [src: gene_function_ecological_agora] |
| phylum | +0.89 σ | +64.5 % [src: gene_function_ecological_agora] |

Negative controls (ribosomal, tRNA-synth and RNAP (RNA polymerase) core) sit ~12 % below cohort with z ≈ −0.15. The report calls this the dosage-constrained signature that M2 anticipates. [src: gene_function_ecological_agora]

### M1 consumer-null fix

The M1 fix stratifies the parent rank by child rank instead of always using phylum. [src: gene_function_ecological_agora] It produced a rank gradient that Phase 1A's parent-phylum-only anchor masked. [src: gene_function_ecological_agora] Informative mean consumer z values were:

- genus children with family parents: −10.48 [src: gene_function_ecological_agora]
- family children with order parents: −6.40 [src: gene_function_ecological_agora]
- order children with class parents: −4.18 [src: gene_function_ecological_agora]
- class children with phylum parents: −1.84 [src: gene_function_ecological_agora]

The report says the pilot's parent-phylum anchor gave a flat-then-jump pattern, ≈−4 σ at deep ranks and −1.36 at class. M1 shows the pattern is monotone. [src: gene_function_ecological_agora]

### Bacteroidota PUL hypothesis falsified under the absolute criterion

The pre-registered hypothesis was that [[entities/bacteroidota]] PUL (polysaccharide utilization locus) CAZyme (carbohydrate-active enzyme) UniRef50s are Innovator-Exchange. This meant both the producer and consumer 95 % CI (confidence interval) lower bounds were above 0. The hypothesis was falsified at all 4 deep ranks (0/4 supported). [src: gene_function_ecological_agora] Bacteroidota PUL CAZymes have producer z ∈ [−0.07, −0.10] across deep ranks, with 95 % CIs entirely below zero. [src: gene_function_ecological_agora] Their consumer z is in [−9.3, −2.8] at parent ranks. [src: gene_function_ecological_agora] Both legs therefore fail the absolute criterion. [src: gene_function_ecological_agora]

The report concludes that the absolute-zero criterion was over-stringent at UniRef50 resolution. [src: gene_function_ecological_agora] A relative threshold reveals a graded HGT (horizontal gene transfer) signal. At family→order parent rank, CAZymes show +0.78 σ less clumping than ribosomal proteins. Median consumer z is −6.21 vs −6.99, with Mann-Whitney U one-sided p = 1 × 10⁻⁴³. [src: gene_function_ecological_agora] This is a null for the specific hypothesis: Bacteroidota CAZymes show no additional lift relative to other phyla's CAZymes. [src: gene_function_ecological_agora] Data are in p1b_bacteroidota_pul_test.tsv and p1b_discrimination_diagnostic.tsv. [src: gene_function_ecological_agora]

### HGT positive controls

The pre-registered cross-phylum HGT positive controls (β-lactamase and class-I [[entities/crispr-cas]]) all have strongly negative absolute consumer z at parent ranks. [src: gene_function_ecological_agora] They still discriminate from housekeeping by 0.6–1.2 σ at UniRef50 resolution. [src: gene_function_ecological_agora] Family-rank values, with Δ against neg_ribosomal, are below.

| Control | Median consumer z | Δ vs neg_ribosomal | One-sided MW p |
|---|---|---|---|
| pos_amr | −7.37 | −0.37 | 0.94 [src: gene_function_ecological_agora] |
| pos_tcs_hk | −6.57 | +0.43 | 5×10⁻⁴ [src: gene_function_ecological_agora] |
| pos_betalac | −6.37 | +0.62 | 5×10⁻⁸ [src: gene_function_ecological_agora] |
| pos_crispr_cas | −5.81 | +1.18 | 1×10⁻⁸⁰ [src: gene_function_ecological_agora] |

The AMR (antimicrobial resistance) set is the [[entities/bakta-amr]] set, which is dominated by clade-specific resistance variants. [src: gene_function_ecological_agora] The report reads the absent AMR discrimination as consistent with that narrowness, not a methodology failure. [src: gene_function_ecological_agora] The report also corrects the gate document. Known-HGT controls fail the absolute Innovator-Exchange threshold but pass the relative-discrimination diagnostic, so "controls fail" overstates. [src: gene_function_ecological_agora] Notebook 08b holds this diagnostic. It was requested by the user after the original Phase 1B narrative was over-pessimistic. [src: gene_function_ecological_agora] See [[concepts/horizontal-gene-transfer-inference-metrics-and-control-class-calibration]].

### Unresolved order-rank anomaly

At order rank (parent=class), positive HGT controls are more clumped than negatives. Median consumer z is −4.51 vs −3.69, the opposite of expectation. [src: gene_function_ecological_agora] Mann-Whitney U one-sided p = 1.0, so there is no discrimination in the expected direction. [src: gene_function_ecological_agora] The anomaly occurs at one rank only. [src: gene_function_ecological_agora] The report offers three candidate explanations:

- Order rank has only 689 clades and 245 parent classes, and the small parent-clade count may inflate the consumer-null permutation variance. [src: gene_function_ecological_agora]
- Intra-phylum HGT-active genes may cluster within a few orders, making them more clumped at parent=class than housekeeping genes, which spread across many classes. [src: gene_function_ecological_agora]
- A metric mis-calibration specific to small-K parent-rank scenarios. [src: gene_function_ecological_agora]

Resolving this needs Phase 2 work. The same diagnostic at KO (KEGG ortholog) aggregation level should show whether the anomaly is metric-specific or substrate-specific. [src: gene_function_ecological_agora]

## Phase 1B Milestone (v1.2, 2026-04-27); Phase 1B closure summary

Phase 1B closed with a reframed pass: UniRef50 shows a small but real horizontal gene transfer (HGT) signal, not the null result first reported, and the pre-registered Bacteroidota hypothesis still fails. [src: gene_function_ecological_agora]

### Substrate hierarchy: revised from "cannot detect" to "small but real"

Phase 1A pre-registered the claim that UniRef50 captures sequence-cluster-specific variants and is too narrow to detect family-level HGT or paralog signal. [src: gene_function_ecological_agora] The report retracts the strict form of that claim. It concludes that UniRef50 produces small but real HGT signal. [src: gene_function_ecological_agora] The original NB07/NB08 narrative was "everything fails at UniRef50; substrate-hierarchy explains it; Phase 2 KO required". The report calls that too pessimistic. [src: gene_function_ecological_agora]

At UniRef50, carbohydrate-active enzymes (CAZymes), β-lactamases and class-I CRISPR-Cas show +0.6 to +1.2 σ less clumping than housekeeping at family rank, with p << 10⁻⁷. [src: gene_function_ecological_agora] The signal is well below the absolute Innovator-Exchange threshold that Phase 1B pre-registered. [src: gene_function_ecological_agora]

The substrate-hierarchy reasoning survives in a softer form. KEGG ortholog (KO) aggregation is expected to give much larger effect sizes, because it collapses sequence-cluster-specific clade restriction. This remains a prediction for Phase 2. [src: gene_function_ecological_agora]

### Diagnostics on effect size

- NB08b, a relative-threshold diagnostic, separates CAZymes from housekeeping by +0.78 σ at family rank (p = 1×10⁻⁴³). [src: gene_function_ecological_agora] The discrimination is small, with Cohen's d of about 0.07–0.09, below biologically meaningful effect sizes. [src: gene_function_ecological_agora]
- NB08c uses Sankoff parsimony, a tree-aware metric. It recovers the expected direction, with positive HGT above negative housekeeping at p = 2.1×10⁻⁵. [src: gene_function_ecological_agora] The effect at UniRef50 is small, with Cohen's d = 0.146. [src: gene_function_ecological_agora]
- Phase 2 must amplify the effect to d ≥ 0.3 to validate the substrate-hierarchy reasoning. If it does not, a reconciliation-based M11 redesign (gene tree versus species tree, AleRax sub-sampling) triggers. [src: gene_function_ecological_agora]

### Hypothesis outcome and null-model checks

The pre-registered Bacteroidota → Innovator-Exchange hypothesis for polysaccharide utilization locus (PUL) CAZymes fails at all 4 deep ranks under the pre-registered absolute-zero criterion. [src: gene_function_ecological_agora] It remains falsified under the relative criterion too. The relative framing changes only how the control-class behaviour is described. [src: gene_function_ecological_agora] See [[entities/bacteroidota]].

Several null-model checks passed:
- Multi-rank null-model construction works at full GTDB scale. M1 rank-stratified parents reveal a clean monotone clumping gradient. [src: gene_function_ecological_agora]
- The producer null is responsive. The natural_expansion class shows +64.5 % paralog above cohort at phylum rank, p ≈ 10⁻⁸⁰. [src: gene_function_ecological_agora]
- Negative controls show the expected dosage-constrained signature under M2. [src: gene_function_ecological_agora]

### Gate verdict and lessons

The Phase 1B → Phase 2 gate is PASS_REFRAMED with corrected scope. [src: gene_function_ecological_agora] The fuller verdict is `PASS_REFRAMED + qualified`. The methodology is not broken, but the substrate-hierarchy framing is now an empirical bet on Phase 2 amplification rather than an established conclusion. [src: gene_function_ecological_agora] The gate is documented in notebook 08 and `data/p1b_phase_gate_summary.md`, with the diagnostic correction in 08b. [src: gene_function_ecological_agora]

The report traces the error to a pre-registration omission. The Innovator-Exchange criterion in plan v2 set an absolute threshold without anchoring it to the empirically appropriate scale. [src: gene_function_ecological_agora] The lesson it draws is that atlas-level criteria should be calibrated against an empirical baseline such as housekeeping classes, not against absolute zero. This matters most where substrate resolution shifts the null distribution. [src: gene_function_ecological_agora] See [[concepts/horizontal-gene-transfer-inference-metrics-and-control-class-calibration]] and [[concepts/adversarial-review-pre-registration-and-multiple-testing-discipline]].

### Methodology revisions carried into Phase 2

- M6: the Phase 2 substrate is KO, not UniRef50. [src: gene_function_ecological_agora]
- M7: carry M1 rank-stratified parents forward. [src: gene_function_ecological_agora]
- M8: carry the M2 negative-control criterion forward. [src: gene_function_ecological_agora]
- M9: PIC is re-promoted to mandatory for Phase 2, after deferral from Phase 1B. [src: gene_function_ecological_agora]
- M10: use a per-class cap pattern at KO scale. [src: gene_function_ecological_agora]
- M11 (revised): if KO-level relative-threshold discrimination does not substantially amplify UniRef50's +0.6–1.2 σ at family rank, switch from parent-rank dispersion to direct phyletic-incongruence on KO presence/absence. [src: gene_function_ecological_agora]
- M12 (new at v2.4): report HGT-class versus housekeeping deltas as a primary atlas metric, alongside absolute consumer z. [src: gene_function_ecological_agora]

The deep-rank Innovator-Exchange definition changes accordingly. It becomes "≥ X σ less clumped than housekeeping at the rank's parent", not "absolute consumer z > 0". X is to be calibrated empirically from Phase 2 data. [src: gene_function_ecological_agora]

## Phase 1B Diagnostic Resolution (v1.3, 2026-04-27): Headline diagnostic outcome (NB08c)

NB08c asked whether the order-rank anomaly came from the parent-rank dispersion metric or from a failure of the methodology. Using [[entities/sankoff-parsimony]] on the GTDB-r214 tree, it found that the metric was at fault. Sankoff parsimony recovers the expected direction, but the effect at UniRef50 is small (Cohen's d = 0.15). [src: gene_function_ecological_agora]

### Why the substrate-hierarchy claim was reformulated

A close reading of Alm 2006 showed the project had misread it in three load-bearing ways. The four-quadrant framework is the project's own construction, not theirs. [src: gene_function_ecological_agora] Alm 2006 worked at single-domain level, about UniRef50, not at family level. [src: gene_function_ecological_agora] They used phylogenetic-tree-aware reconciliation, not parent-rank dispersion. [src: gene_function_ecological_agora] The substrate-hierarchy claim was therefore recast. It no longer says "UniRef50 is too narrow, aggregate to KO (KEGG ortholog)". It now says the project used the wrong metric on the right substrate. [src: gene_function_ecological_agora]

### Diagnostic panels

In panel A, positive HGT (horizontal gene transfer) and negative housekeeping UniRefs both have median order-rank K = 1, so UniRefs are clade-restricted whatever their class. [src: gene_function_ecological_agora] The two K distributions differ (p < 10⁻¹⁹) but share the same median, so K bias does not explain the anomaly. [src: gene_function_ecological_agora]

Within Pseudomonadota, positive controls show lower dispersion than negative housekeeping (pos median 0.25, neg median 0.33). [src: gene_function_ecological_agora] The report treats this as a bias of the metric. Housekeeping genes occur in every family, while HGT-active classes are clade-specific within the phylum. [src: gene_function_ecological_agora]

Panel C scores each class by Sankoff score per present leaf. Positive HGT classes (TCS HK, β-lactamase, CAZymes) sit above housekeeping (ribosomal, tRNA-synth, RNAP). [src: gene_function_ecological_agora] TCS is two-component system and HK is histidine kinase. CAZymes are carbohydrate-active enzymes, and RNAP is RNA polymerase. The direction is recovered with Cohen's d = 0.15 (p = 2.1×10⁻⁵). [src: gene_function_ecological_agora]

### AMR detection bias

Only AMR (antimicrobial resistance) is strongly Pseudomonadota-biased. Its median Pseudomonadota fraction is 50 %, and 49 % of AMR UniRefs are >50 % Pseudomonadota. [src: gene_function_ecological_agora] All other classes have a median ≤ 4 %. [src: gene_function_ecological_agora] The report attributes this to [[entities/bakta-amr]] being sourced from AMRFinderPlus's Pseudomonadota-heavy reference set. [src: gene_function_ecological_agora]

### Median Sankoff/n_present by class

| Class | Median | Note |
|---|---|---|
| none (random atlas baseline) | 24.5 | top; sparse-presence UniRefs require many gains [src: gene_function_ecological_agora] |
| pos_tcs_hk | 19.75 | above housekeeping [src: gene_function_ecological_agora] |
| pos_betalac | 19.0 | above housekeeping [src: gene_function_ecological_agora] |
| hyp_cazyme | 19.0 | above housekeeping [src: gene_function_ecological_agora] |
| neg_rnap_core | 17.5 | inversion: RNAP ranks above CRISPR-Cas (small) [src: gene_function_ecological_agora] |
| pos_crispr_cas | 17.0 | [src: gene_function_ecological_agora] |
| neg_trna_synth | 14.0 | [src: gene_function_ecological_agora] |
| neg_ribosomal | 12.8 | correctly the lowest housekeeping class [src: gene_function_ecological_agora] |
| pos_amr | 12.0 | anomalously low, attributed to Pseudomonadota detection bias [src: gene_function_ecological_agora] |
| natural_expansion | 4.5 | correctly lowest, from broad conservation by selection [src: gene_function_ecological_agora] |

The low natural_expansion score supports the metric's biological direction, because broadly conserved UniRefs need few gain events. [src: gene_function_ecological_agora] The analysis is recorded in notebook 08c_p1b_metric_diagnostic.ipynb. [src: gene_function_ecological_agora]

### Conclusion and limits

The report concludes that the order-rank anomaly is a parent-rank-dispersion artifact. Sankoff parsimony is the canonical Alm-2006-faithful tree-aware metric, and it recovers the expected direction. The framework is not broken. [src: gene_function_ecological_agora]

The effect at UniRef50 stays small. Cohen's d = 0.15 is well below the d ≥ 0.3 threshold the project pre-registered for atlas-grade discrimination. [src: gene_function_ecological_agora] The earlier "+0.6 to +1.2 σ less clumped than housekeeping" framing used parent-rank z-units, not Cohen's d, and overstated effect magnitude. [src: gene_function_ecological_agora] The report expects Phase 2 KO aggregation to amplify the real but small signal. It treats this as an empirical claim Phase 2 must demonstrate, not a guarantee. [src: gene_function_ecological_agora] The right within-phylum analog is per-phylum Sankoff parsimony. [src: gene_function_ecological_agora]

### Phase 2 decisions that follow

- M16 makes Sankoff parsimony on the GTDB-r214 tree topology the primary atlas metric for Phase 2. Parent-rank dispersion drops to diagnostic only. [src: gene_function_ecological_agora]
- M17 excludes bakta_amr from the Phase 2 positive controls because of the Pseudomonadota detection bias. β-lactamase, CRISPR-Cas and TCS HK remain positive controls, and natural_expansion serves as the paralog-signal sanity check. [src: gene_function_ecological_agora]
- M18 is a hard amplification gate. The Phase 2 KO atlas must show Cohen's d ≥ 0.3 on Sankoff parsimony for at least one positive HGT control against negative housekeeping. The UniRef50 baseline is d = 0.15. [src: gene_function_ecological_agora]
- If Phase 2 fails to reach d ≥ 0.3, the substrate-hierarchy claim is falsified. M11 redesign then triggers, switching from Sankoff to gene-tree-versus-species-tree reconciliation. [src: gene_function_ecological_agora]

## Lessons captured (project-level epistemic discipline): M14 — Misreading of Alm 2006 …

This part of the report describes three pre-registration omissions found across Phases 1A and 1B. Each was corrected for the next phase. [src: gene_function_ecological_agora] The report argues that all three were criterion or framing errors, not methodology failures. [src: gene_function_ecological_agora] See also [[concepts/adversarial-review-pre-registration-and-multiple-testing-discipline]].

### Omission 1: housekeeping negative control (Phase 1A)

The v2 criterion required producer mean within ±1σ of zero for housekeeping classes: ribosomal, tRNA-synthetase and RNAP (RNA polymerase) core. [src: gene_function_ecological_agora] The report says it anticipated, during plan v2 design, that dosage-constrained genes have fewer paralogs than typical genes at matched prevalence. It did not encode that prior in the criterion. [src: gene_function_ecological_agora] The Phase 1A pilot put all three negative controls at producer z ≈ −0.15, with confidence intervals (CIs) entirely below zero. [src: gene_function_ecological_agora] The criterion was revised post-hoc to "CI upper bound ≤ 0.5". [src: gene_function_ecological_agora] The lesson drawn is that a criterion with a known biological prior should state that prior, not the absolute-null value. [src: gene_function_ecological_agora]

### Omission 2: absolute-zero Innovator-Exchange (Phase 1B)

Plan v2 defined "Innovator-Exchange" as both producer and consumer 95 % CI lower bound > 0, an absolute-zero threshold. [src: gene_function_ecological_agora] In Phase 1B, all positive controls (β-lactamase, CRISPR-Cas, AMR (antimicrobial resistance), TCS HK (two-component system histidine kinase)) had strongly negative consumer z. All failed this criterion. [src: gene_function_ecological_agora] A post-gate diagnostic (NB08b) found the positive horizontal gene transfer (HGT) classes were still +0.6–1.2 σ less clumped than housekeeping at family rank (p << 10⁻⁷). [src: gene_function_ecological_agora] The report judged the absolute-zero threshold over-stringent at UniRef50 resolution, where the null distribution itself is shifted. [src: gene_function_ecological_agora] M12 therefore reformulated Innovator-Exchange as a relative metric, "≥ X σ less clumped than housekeeping baseline at the rank's parent", with X calibrated empirically. [src: gene_function_ecological_agora] The lesson is to calibrate atlas-level criteria against an empirical baseline, not absolute zero, especially where the null is shifted. [src: gene_function_ecological_agora]

### Omission 3: misreading of Alm 2006

The central research question framed the four-quadrant Open/Broker/Sink/Closed Innovator framework as a generalization of "the producer/consumer asymmetry observed by Alm-Huang-Arkin 2006." [src: gene_function_ecological_agora] A close reading of the paper found three misreadings:
- Alm 2006 never named producer/consumer or four-quadrant categories. It reported a correlation of r = 0.74 between HPK (histidine protein kinase) count and recent-LSE fraction. [src: gene_function_ecological_agora]
- It worked at the single-domain level (IPR005467 / COG4582), comparable to UniRef50, not at family aggregation. [src: gene_function_ecological_agora]
- It used phylogenetic-tree-aware reconciliation, not parent-rank dispersion. [src: gene_function_ecological_agora]

The claim that Phase 2 KO (KEGG ortholog) aggregation would recover Alm 2006-style signal therefore rested on a misreading. [src: gene_function_ecological_agora] M14 reframed the project as "Alm-2006-inspired" instead of generalizing the paper. [src: gene_function_ecological_agora] M15 made [[entities/sankoff-parsimony]], a lightweight tree-aware metric, mandatory. [src: gene_function_ecological_agora] The lesson is that foundational anchor papers must be close-read for exact methodology before infrastructure is built on extrapolations. [src: gene_function_ecological_agora]

### Corrective discipline

The report's rule is to run a focused diagnostic first when a result deviates from pre-registered expectations. Only then should one invoke substrate, methodology or "we need more data" explanations. [src: gene_function_ecological_agora] The diagnostics were NB04b (Phase 1A power analysis), NB08b (Phase 1B discrimination diagnostic) and NB08c (Phase 1B Sankoff diagnostic). [src: gene_function_ecological_agora] Together they took about 3 hours to write and ran in seconds to minutes. They distinguished metric or criterion problems from methodology failures. [src: gene_function_ecological_agora] The report says each saved the project from a wrong conclusion. [src: gene_function_ecological_agora]

## Phase 1B Adversarial Review 4 Response (v1.5, 2026-04-27): Concerns addressed in plan …

This part of the report answers the fourth adversarial review of the v1.4 milestone. The review raised 5 critical, 7 important and 4 suggested issues. [src: gene_function_ecological_agora] The report traces two critical findings to reviewer-side errors. [src: gene_function_ecological_agora] The substantive concerns led to plan v2.7 commitments M19 and M20 and to the retirement of M9 (phylogenetic independent contrasts, PIC). [src: gene_function_ecological_agora] The review file is kept verbatim in ADVERSARIAL_REVIEW_4.md. [src: gene_function_ecological_agora] See also [[concepts/adversarial-review-pre-registration-and-multiple-testing-discipline]].

### Reviewer errors

**C1 (missing Alm 2006 reference) is rejected as false.** [src: gene_function_ecological_agora] Alm 2006 is the first reference in references.md (line 9, "Methodological anchor" section). [src: gene_function_ecological_agora] DESIGN_NOTES.md references it ≥30 times, including the v2.4 entry that documents the close-reading. [src: gene_function_ecological_agora] The project has a dedicated 460-line memo at docs/alm_2006_methodology_comparison.md, linked from the README. [src: gene_function_ecological_agora] REPORT.md also cites it under M14 in the Phase 1B Diagnostic Resolution section (v1.3). [src: gene_function_ecological_agora] The report says the reviewer's literature-scan subagent did not read references.md or hallucinated its absence. [src: gene_function_ecological_agora] It recommends that future adversarial runs verify "Alm 2006 cited" by exact-string match before flagging a gap as critical. [src: gene_function_ecological_agora] DESIGN_NOTES.md adds a v2.6 entry recording the C1 hallucination as a reviewer-tooling pitfall. It also records the PIC framing correction as a generalizable lesson. [src: gene_function_ecological_agora]

**I8 (+64.5% versus +39.4%) is a phase-mixing error.** [src: gene_function_ecological_agora] The reviewer used Phase 1A pilot means (obs_mean = 1.77, cohort_mean = 1.27, ratio +39.4%). [src: gene_function_ecological_agora] The comparison reported the Phase 1B full-scale figure (obs_mean = 2.09, cohort_mean = 1.27, ratio +64.5%). [src: gene_function_ecological_agora] The report says both ratios are correctly computed at their own scales. It treats the increase from pilot to full scale as methodology validation. [src: gene_function_ecological_agora] The report's own text writes the pilot ratio as +39.4% in one place [src: gene_function_ecological_agora] and as +39.5% in the sentence that describes the increase. [src: gene_function_ecological_agora] The report does not reconcile the two figures. Notebook 08_p1b_phase_gate.ipynb line 338 documents the Phase 1B paralog values. [src: gene_function_ecological_agora]

### Concerns accepted

**Absolute-zero falsification and M12.** The report acknowledges that M12 (plan v2.4) reframed an absolute-zero falsification as relative discrimination. [src: gene_function_ecological_agora] The Bacteroidota PUL (polysaccharide utilization locus) hypothesis remains falsified at the pre-registered absolute-zero criterion. [src: gene_function_ecological_agora] M12's relative thresholds apply only to control-class methodology validation, not to hypothesis adjudication. [src: gene_function_ecological_agora] Plan v2.7 keeps absolute-criterion adjudication for four pre-registered hypotheses: Bacteroidota PUL, Mycobacteriota mycolic-acid, Cyanobacteria PSII (photosystem II), and Alm 2006 TCS (two-component system) reproduction. M12 governs methodology QC (quality control) only. [src: gene_function_ecological_agora]

**Circular producer-null validation.** The natural_expansion validation is circular. The class is selected for paralog count ≥ 3 and tested against a null designed to detect paralog expansion. [src: gene_function_ecological_agora] Plan v2.7 binds M20, an independent paralog holdout for Phase 2 producer-null validation. It is drawn from Pfam clans with documented paralog families or from KO (KEGG ortholog) orthogroups with cross-organism duplicates. [src: gene_function_ecological_agora] natural_expansion stays as a metric-direction sanity check, and the holdout becomes the load-bearing validation. [src: gene_function_ecological_agora] See [[concepts/paralog-expansion-and-gene-copy-number-constraint]].

**M9 (PIC) retired in favor of M19.** The reviewer is procedurally correct that M9, promoted to mandatory in plan v2.4, was never implemented. [src: gene_function_ecological_agora] The report argues that classical Felsenstein PIC addresses taxon non-independence in per-species traits. It says [[entities/sankoff-parsimony]] (M16) is already tree-aware, because per-leaf parsimony (gain_events / n_present_leaves) encodes tree topology. [src: gene_function_ecological_agora] The real residual concern is UniRef-cluster non-independence. Several UniRef50s within a Pfam family share related phylogenetic distributions, so Mann-Whitney tests across UniRefs treat them as independent and inflate effective N. [src: gene_function_ecological_agora] M19 is a cluster bootstrap of UniRefs at Pfam-family granularity (B = 200 resamples per function class). It recomputes per-leaf Sankoff Cohen's d under each bootstrap and reports a 95% CI (confidence interval). [src: gene_function_ecological_agora] M9 is retired, and M19 is the fix for the actual concern. [src: gene_function_ecological_agora]

**Pre-registration calibration.** Most methodology revisions came from biology engagement (M2 dosage cost, M14 Alm 2006 close-reading, M17 Pseudomonadota AMR bias) rather than data accommodation. The report still concedes that the cumulative count shows pre-registration was insufficiently calibrated to substrate-resolution behavior. [src: gene_function_ecological_agora] Plan v2.7 freezes methodology at M18 + M19 + M20. Further Phase 2 revisions need explicit milestone-revision call-outs with diagnostic rationale. [src: gene_function_ecological_agora]

### Responses to other items

- **M18 gate:** The Phase 2 KO atlas must reach Cohen's d ≥ 0.3 on Sankoff parsimony for at least one positive HGT (horizontal gene transfer) control class versus negative housekeeping. Otherwise the substrate-hierarchy claim is falsified and M11 redesign triggers. [src: gene_function_ecological_agora]
- **I1 (Bacteroidota CAZyme literature):** Liu et al 2024 and Hameleers et al 2024 describe rapid CAZyme (carbohydrate-active enzyme) HGT at PUL/family aggregation level. The Phase 1B falsification was at UniRef50 sequence-cluster level. The report calls these consistent, since family-level CAZyme HGT acts on aggregated functional units. [src: gene_function_ecological_agora]
- **S2 (integrate the Alm comparison):** The report says this was already done in the Phase 1B Diagnostic Resolution (v1.3), in "Lessons captured" M14, and in plan v2.5/v2.6. [src: gene_function_ecological_agora]
- **Primary metric:** Sankoff parsimony on the GTDB-r214 tree topology is the primary atlas metric from Phase 2 onward, per plan v2.6 M16. [src: gene_function_ecological_agora]

## Phase 2 Entry — M18 Amplification Gate (v1.6, 2026-04-27): M18 strict-class re-test …

This part of the report describes the Phase 2 gate for the Gene Function Ecological Agora project. The gate asks whether aggregating genes by KEGG ortholog (KO) amplifies the Sankoff parsimony Cohen's d signal from the UniRef50 baseline of d = 0.146 to at least 0.3 for at least one positive horizontal gene transfer (HGT) control class against negative housekeeping. [src: gene_function_ecological_agora] A pass leads to the full atlas. A fail triggers a redesign based on gene-tree versus species-tree reconciliation with AleRax sub-sampling. [src: gene_function_ecological_agora] The gate passed, but only after one diagnostic-driven correction round. [src: gene_function_ecological_agora] Strict housekeeping classes gave 6 of 9 passing pairs, and all three ribosomal comparisons still failed. [src: gene_function_ecological_agora]

### KO substrate (NB09)

The substrate uses the Phase 1B set of 18,989 species. KO assignments come from the eggNOG annotation table in the KBase Data Lakehouse. [src: gene_function_ecological_agora] The extraction covers 103,629,867 gene clusters, of which 74,450,297 carry eggNOG annotations (71.8%). [src: gene_function_ecological_agora] Parsing KEGG_ko gives 43,803,890 gene-cluster–KO edges and 13,062 unique KOs. [src: gene_function_ecological_agora] After aggregation there are 28,008,764 species–KO presence rows. Paralog count is the number of distinct UniRef90s per species–KO pair. [src: gene_function_ecological_agora] The projection assigns dominant KOs to 3,592,556 UniRef50s, with median dominant-fraction 1.0 and q25 0.97. [src: gene_function_ecological_agora]

Description matching found 748 control-panel KOs [src: gene_function_ecological_agora]:

- TCS HK (two-component system histidine kinase): 310 [src: gene_function_ecological_agora]
- β-lactamase: 110 [src: gene_function_ecological_agora]
- CRISPR-Cas: 6 [src: gene_function_ecological_agora]
- ribosomal: 249 [src: gene_function_ecological_agora]
- tRNA-synth: 54 [src: gene_function_ecological_agora]
- RNAP (RNA polymerase) core: 19 [src: gene_function_ecological_agora]

The full assignment parquet is 1.4 GB and sits on MinIO. A 2.69 MB control-panel subset is kept locally. [src: gene_function_ecological_agora] Spark Connect on this JupyterHub setup does not share a filesystem between workers and driver. Atlas-scale parquets therefore stay MinIO-only. [src: gene_function_ecological_agora] The extraction notebook supplies the assignment, panel, control-class, pathway/BRITE and UniRef50-to-KO projection data files. [src: gene_function_ecological_agora]

### First test: description-matched controls (NB09b)

The first test failed. NB09b scored Sankoff parsimony for all 748 panel KOs on the GTDB-r214 species tree, pruned to 18,989 leaves, in 11 seconds. [src: gene_function_ecological_agora] Confidence intervals (CI) came from M19 cluster bootstrapping (B = 200, KO-level resampling within class). [src: gene_function_ecological_agora] The best pair was pos_betalac vs neg_trna_synth, with d +0.2118, 95% CI [−0.138, +0.531] and one-sided MW p 1.1×10⁻⁵. [src: gene_function_ecological_agora] None of the 9 pairs passed d ≥ 0.3 with a CI lower bound above 0. [src: gene_function_ecological_agora] Ribosomal and RNAP core comparisons reversed the expected sign, with d = −0.66 to −2.97. [src: gene_function_ecological_agora]

Median Sankoff/n_present per class in NB09b:

- neg_rnap_core: 19 KOs, median 14.50 [src: gene_function_ecological_agora]
- neg_ribosomal: 249 KOs, median 11.35, median n_present_leaves ~29 [src: gene_function_ecological_agora]
- pos_betalac: 110 KOs, median 2.64, median n_present_leaves 390 [src: gene_function_ecological_agora]
- pos_crispr_cas: 6 KOs, median 2.04, median n_present_leaves 1499 [src: gene_function_ecological_agora]
- pos_tcs_hk: 310 KOs, median 1.47, median n_present_leaves 918 [src: gene_function_ecological_agora]
- neg_trna_synth: 54 KOs, median 0.30 [src: gene_function_ecological_agora]

The report notes that the neg_ribosomal class was dominated by clade-restricted accessory proteins and false matches, not universal ribosomal proteins. These were caught by the description-match rule. [src: gene_function_ecological_agora]

### Correction: strict housekeeping classes (NB09c)

NB09c replaced the negative classes with KO-range definitions:

- Ribosomal: K02860..K02899 ∪ K02950..K02998, 89 KOs, 83 in the panel. [src: gene_function_ecological_agora]
- tRNA synthetase: K01866..K01890, 25 KOs, 20 in the panel. [src: gene_function_ecological_agora]
- RNAP core: K03040, K03043 and K03046, 3 KOs, all in the panel. [src: gene_function_ecological_agora]

Positive controls were unchanged. They use Pfam-accession matching, which the report calls more specific than description matching. [src: gene_function_ecological_agora] NB09c reused NB09b's per-KO Sankoff scores and recomputed Cohen's d without further tree work. [src: gene_function_ecological_agora] Six of 9 strict pairs passed d ≥ 0.3 with CI lower bound above 0. [src: gene_function_ecological_agora] Passing pairs:

- pos_crispr_cas vs neg_trna_synth_strict (n 6 / 20): d +3.558, 95% CI [+2.93, +21.53], one-sided MW p 4×10⁻⁶ [src: gene_function_ecological_agora]
- pos_crispr_cas vs neg_rnap_core_strict (6 / 3): d +1.905, CI [+1.47, +11.88], p 0.012 [src: gene_function_ecological_agora]
- pos_betalac vs neg_trna_synth_strict (110 / 20): d +0.812, CI [+0.72, +0.95], p <10⁻¹⁵ [src: gene_function_ecological_agora]
- pos_betalac vs neg_rnap_core_strict (110 / 3): d +0.753, CI [+0.67, +0.86], p 0.0017 [src: gene_function_ecological_agora]
- pos_tcs_hk vs neg_trna_synth_strict (310 / 20): d +0.690, CI [+0.60, +0.88], p <10⁻¹⁵ [src: gene_function_ecological_agora]
- pos_tcs_hk vs neg_rnap_core_strict (310 / 3): d +0.665, CI [+0.58, +0.85], p 0.0015 [src: gene_function_ecological_agora]

Failing pairs, all against neg_ribosomal_strict:

- pos_betalac (110 / 83): d −0.836, CI [−1.17, −0.52], p 0.87 [src: gene_function_ecological_agora]
- pos_crispr_cas (6 / 83): d −0.919, CI [−1.15, −0.66], p 0.71 [src: gene_function_ecological_agora]
- pos_tcs_hk (310 / 83): d −1.705, CI [−2.15, −1.33], p 0.96 [src: gene_function_ecological_agora]

### Caveats

- The three ribosomal_strict failures persist. The report attributes them to the K02860-K02899 + K02950-K02998 range being a pre-2000 KEGG-numbering approximation that mixes universal ribosomal proteins with accessory variants. [src: gene_function_ecological_agora] This is the report's explanation, not a separate test. neg_ribosomal_strict has n 83, median Sankoff/n_present 18.83 (q25=0.11, q75=23.13, described as bimodal) and median n_present_leaves 13. [src: gene_function_ecological_agora]
- Several passing pairs rest on very few KOs. The strict RNAP core class has only 3 KOs, with median Sankoff/n_present 0.073 and median n_present_leaves 18,758. [src: gene_function_ecological_agora] Their CIs are wide, for example [+2.93, +21.53] for CRISPR-Cas against tRNA synthetase. [src: gene_function_ecological_agora]

### Slots Into

- [[concepts/horizontal-gene-transfer-inference-metrics-and-control-class-calibration]]: the description-matched controls gave 0/9 passing pairs, and the strict controls gave 6/9. [src: gene_function_ecological_agora]
- [[entities/sankoff-parsimony]]: Sankoff scoring of 748 KOs on the pruned GTDB-r214 tree took 11 seconds. [src: gene_function_ecological_agora]
- [[concepts/limits-of-keyword-and-marker-based-functional-annotation]]: the report notes that description matching produced false ribosomal matches. [src: gene_function_ecological_agora]
- [[concepts/spark-query-scale-limits-and-notebook-session-constraints-in-lakehouse-analyses]]: Spark Connect workers and driver share no filesystem, so large parquets stay on MinIO. [src: gene_function_ecological_agora]

## Phase 2 Entry — M18 Amplification Gate (v1.6, 2026-04-27); Phase 2 Atlas + M22 …

This part of the report covers the M18 amplification gate at KO (KEGG ortholog) resolution, the M21 commitment that followed from it, and the full-scale KO atlas (NB10) with its recipient-rank gain attribution (NB10b, M22). The gate passed at KO resolution and again on the full atlas. Ribosomal controls proved contaminated, so only tRNA synthetase and RNA polymerase (RNAP) core serve as clean housekeeping. [src: gene_function_ecological_agora]

### M18 gate at KO resolution (NB09c)

M18 passed on the cleanest housekeeping classes, tRNA-synth and RNAP core. Cohen's d rose from 0.146 at UniRef50 (NB08c, positive class versus all housekeeping) to 0.665–3.558 for the best KO pairs in NB09c. The report calls this a 4–25× amplification, depending on positive class. [src: gene_function_ecological_agora] It concludes that the substrate-hierarchy claim survives at KO resolution and that the full Phase 2 atlas can proceed. [src: gene_function_ecological_agora] The MARGINAL → PASS diagnostic took one hour and reused NB09b's per-KO Sankoff scores. [src: gene_function_ecological_agora]

The housekeeping classes differ in quality. tRNA synthetase and RNAP core are clean universal housekeeping. About half of the 83 strict ribosomal KOs are universal and half are clade-restricted. [src: gene_function_ecological_agora] The strict tRNA-synth negative class in NB09c had n 20, median Sankoff/n_present 0.032 and median n_present_leaves 18,917. [src: gene_function_ecological_agora]

### M21: restricting the housekeeping controls

M21 (plan v2.8) commits all Phase 2/3 d-based metrics and M18-style validation to tRNA-synth (K01866..K01890) and RNAP core (K03040, K03043, K03046). Ribosomal classes are reported as informational only. [src: gene_function_ecological_agora] The report broke plan v2.7's methodology freeze to admit M21. It says the contamination surfaced during Phase 2 entry, which the freeze's milestone-revision clause pre-authorized. [src: gene_function_ecological_agora]

The cause is aggregation. Description-based class detection was mostly clean at UniRef50 but fails at KO level, because the 50% majority-vote threshold admits accessory members of the class. [src: gene_function_ecological_agora] The report calls the approximate ribosomal K-ID range a pre-2000 numbering approximation. It recommends KEGG's modern bacterial ribosomal-protein KO list, or relying on tRNA-synth and RNAP core alone. [src: gene_function_ecological_agora]

### Full KO atlas (NB10)

NB10 and NB10b ran on 18,989 species × 13,062 KOs. [src: gene_function_ecological_agora] Outputs:

- 28,008,764 (species, KO) presence rows, materialized from MinIO. [src: gene_function_ecological_agora]
- 13,739,162 (rank, clade, KO) producer/consumer scores across 5 ranks, genus to phylum. [src: gene_function_ecological_agora]
- 17,073,194 Sankoff parsimony gain events on the GTDB-r214 tree (M16). [src: gene_function_ecological_agora]
- 18,988 internal tree nodes. [src: gene_function_ecological_agora]
- An atlas parquet of 94.7 MB locally. [src: gene_function_ecological_agora]

The deep-rank distribution of clade × KO tuples:

- Stable: 11,829,746 (low producer + low participation). [src: gene_function_ecological_agora]
- Innovator-Isolated: 803,196 (high producer + low participation). [src: gene_function_ecological_agora]
- Sink/Broker-Exchange: 741,587 (low producer + high participation). [src: gene_function_ecological_agora]
- Innovator-Exchange: 50,026 (high producer + high participation; rare; the v2 plan's hardest call). [src: gene_function_ecological_agora]
- insufficient_data: 314,607 (n_clades_with too low for consumer null). [src: gene_function_ecological_agora]

The report concludes that the four-quadrant structure exists at full GTDB scale and that the methodology can produce defensible scores at that resolution. [src: gene_function_ecological_agora] The insufficient_data tuples are a limit, because they lack enough clades for a consumer null. [src: gene_function_ecological_agora]

### M18 reproduced at full scale

The NB09c verdict reproduces on the full atlas: 6/6 strict pairs pass Cohen's d ≥ 0.3 with a 95% bootstrap confidence interval (CI) lower bound > 0. [src: gene_function_ecological_agora]

- pos_crispr_cas vs neg_trna_synth_strict: n_pos 6, n_neg 21, d 2.504, CI [1.31, 16.16]. [src: gene_function_ecological_agora]
- pos_crispr_cas vs neg_rnap_core_strict: n_pos 6, n_neg 3, d 1.905, CI [1.55, 11.58]. [src: gene_function_ecological_agora]
- pos_betalac vs neg_trna_synth_strict: n_pos 110, n_neg 21, d 0.792, CI [0.68, 0.90]. [src: gene_function_ecological_agora]
- pos_betalac vs neg_rnap_core_strict: n_pos 110, n_neg 3, d 0.753, CI [0.66, 0.86]. [src: gene_function_ecological_agora]
- pos_tcs_hk vs neg_trna_synth_strict: n_pos 310, n_neg 21, d 0.647, CI [0.54, 0.80]. [src: gene_function_ecological_agora]
- pos_tcs_hk vs neg_rnap_core_strict: n_pos 310, n_neg 3, d 0.665, CI [0.58, 0.82]. [src: gene_function_ecological_agora]

The d values match the NB09c panel-only test almost exactly. The report attributes the small drift from NB09c's best d = 3.558 (n_pos = 6, n_neg = 20) to slightly different sample composition. It treats the substrate-hierarchy claim as reconfirmed at full atlas scale. [src: gene_function_ecological_agora] The RNAP core negative class has only 3 KOs in these tests, so its intervals rest on a very small negative set. [src: gene_function_ecological_agora]

### Acquisition depth by class (NB10b, M22)

NB10b tags the 17M gain events by recipient-rank LCA. This yields a per-class acquisition-depth distribution across the GTDB tree. [src: gene_function_ecological_agora] Percentages of gains by depth (recent is genus level, ancient is phylum or above):

- pos_crispr_cas: recent 58.7, older_recent 27.6, mid 7.0, older 4.3, ancient 2.4; 20,898 gains. [src: gene_function_ecological_agora]
- pos_tcs_hk: 45.1, 32.9, 10.6, 7.0, 4.4; 518,106 gains. [src: gene_function_ecological_agora]
- pos_betalac: 44.2, 32.7, 10.7, 7.5, 4.9; 139,000 gains. [src: gene_function_ecological_agora]
- neg_ribosomal_strict: 38.9, 33.3, 12.4, 9.1, 6.3; 79,168 gains. [src: gene_function_ecological_agora]
- neg_rnap_core_strict: 38.5, 34.2, 12.2, 9.0, 6.0; 4,086 gains. [src: gene_function_ecological_agora]
- neg_trna_synth_strict: 24.7, 31.8, 17.5, 15.2, 10.7; 15,060 gains. [src: gene_function_ecological_agora]

Recent-to-ancient gain ratios, from the same figures:

- pos_crispr_cas: 58.7 / 2.4 = 24.5, highly recent-skewed and consistent with documented horizontal gene transfer (HGT) activity. [src: gene_function_ecological_agora]
- pos_tcs_hk: 45.1 / 4.4 = 10.3. [src: gene_function_ecological_agora]
- pos_betalac: 44.2 / 4.9 = 9.0. [src: gene_function_ecological_agora]
- neg_ribosomal_strict: 38.9 / 6.3 = 6.2, mixed, as expected for the contaminated strict-K range. [src: gene_function_ecological_agora]
- neg_rnap_core_strict: 38.5 / 6.0 = 6.4. [src: gene_function_ecological_agora]
- neg_trna_synth_strict: 24.7 / 10.7 = 2.3, the most ancient-skewed and consistent with universal vertical inheritance. [src: gene_function_ecological_agora]

The recent/ancient ratio for HGT-active classes is 4–10× higher than for clean housekeeping. [src: gene_function_ecological_agora] The report reads this as M22 doing what it was designed to do. M22 separates recent acquisition from ancient inheritance per clade × function-class across the full GTDB tree. [src: gene_function_ecological_agora]

## Phase 2 Atlas + M22 Acquisition Attribution (v1.7, 2026-04-27): Novel contribution

This part of the report lists the output files of the Phase 2 atlas and the M22 acquisition attribution. It also records how the long runs were executed, how the results relate to the literature, and the headline per-class acquisition signatures and validation results. The class signatures rest on one GTDB-scale atlas, and the explicit Alm 2006 reproduction is deferred. [src: gene_function_ecological_agora]

### Output files

The atlas stage writes six files and the M22 stage writes four. All are in `data/`. [src: gene_function_ecological_agora]

| File | Size | Content |
|---|---|---|
| p2_ko_atlas.parquet | 94.7 MB | per (rank, clade, KO) producer + participation + category [src: gene_function_ecological_agora] |
| p2_ko_sankoff.parquet | 245 KB | per-KO Sankoff score + n_present_leaves + control_class_m21 [src: gene_function_ecological_agora] |
| p2_ko_sankoff_gains.parquet | 33 MB | per-gain-event records (input for M22) [src: gene_function_ecological_agora] |
| p2_null_consumer_lookup.parquet | 1.5 MB | per-(rank, KO) consumer null moments [src: gene_function_ecological_agora] |
| p2_m21_sanity_rail.tsv | 757 B | M21 sanity rail at full scale [src: gene_function_ecological_agora] |
| p2_atlas_diagnostics.json | 2 KB | diagnostics [src: gene_function_ecological_agora] |
| p2_m22_gains_attributed.parquet | 84 MB | per-gain-event recipient-rank attribution + depth bin [src: gene_function_ecological_agora] |
| p2_m22_acquisition_profile.parquet | 20 MB | per (recipient_clade × ko × depth × rank), the v2.9 atlas core [src: gene_function_ecological_agora] |
| p2_m22_class_depth_summary.tsv | 906 B | per-class acquisition-depth distribution [src: gene_function_ecological_agora] |
| p2_m22_diagnostics.json | 316 B | M22 diagnostics [src: gene_function_ecological_agora] |

### Execution failures and the working pattern

NB10 and NB10b each needed several attempts. Long-running Python processes on the project's JupyterHub instance were killed silently after ~17–25 min, with no error message. [src: gene_function_ecological_agora] The report calls this consistent with cluster scheduler or session timeout behavior, not code errors. The inline 5-rank loop runs in 13 s, and the problem appears only in long sessions. [src: gene_function_ecological_agora]

The report's working pattern has four parts:
- Bypass `jupyter nbconvert --execute`. Convert the notebook to a plain `.py` script and run it with `nohup python3 -u script.py`. This removes ipykernel buffering and gives predictable backgrounding. [src: gene_function_ecological_agora]
- Save intermediates after each major stage, using direct `pd.to_parquet` rather than wrapper functions that reconstruct. [src: gene_function_ecological_agora]
- Use recovery scripts that load intermediates and finish the remaining stages. NB10 finalize and NB10b finalize2 are the templates. [src: gene_function_ecological_agora]
- Write small files (TSVs, summaries) before large parquet files, because the kill seems to fire mid-write on the largest parquet. [src: gene_function_ecological_agora]

The report calls the pattern reliable despite its added complexity. It recommends the same script-with-checkpoints design for Phase 2 NB11/NB12 and all of Phase 3/4. [src: gene_function_ecological_agora] See also [[concepts/spark-query-scale-limits-and-notebook-session-constraints-in-lakehouse-analyses]].

### Class-level acquisition signatures

The atlas provides 13.7 M (rank × clade × KO) producer/participation scores and 17 M gain events with recipient-rank and depth-bin attribution. [src: gene_function_ecological_agora] The report states the recent-to-ancient ratio (recent% / ancient%) per class as follows: [src: gene_function_ecological_agora]

| Class | Ratio |
|---|---|
| CRISPR-Cas | 24.5× [src: gene_function_ecological_agora] |
| TCS HK (two-component system histidine kinase) | 10.3× [src: gene_function_ecological_agora] |
| β-lactamase | 9.0× [src: gene_function_ecological_agora] |
| ribosomal | 6.2-6.3× [src: gene_function_ecological_agora] |
| RNAP core (RNA polymerase) | 6.4× [src: gene_function_ecological_agora] |
| tRNA-synth | 2.3× [src: gene_function_ecological_agora] |

The report reads these as matching the established horizontal gene transfer (HGT) literature and turning it into a quantitative per-class statistic at GTDB scale. [src: gene_function_ecological_agora] This is the report's interpretation. The comparisons are below.

- Recent-skewed gains for HGT-active classes align with Smillie et al. 2011 (within-phylum HGT in the human gut microbiome) and Forsberg et al. 2012 (cross-phylum antimicrobial resistance (AMR) resistome; β-lactamase families spread in soil and clinical lineages). [src: gene_function_ecological_agora]
- Bonomo (2017) documents cross-phylum spread of TEM, CTX-M, NDM and OXA-48 β-lactamase families. The report calls the +44.2% recent / 4.9% ancient signature for `pos_betalac` (n=139,000 gain events) the GTDB-scale instantiation of that pattern. [src: gene_function_ecological_agora]
- The [[entities/crispr-cas]] recent-skew (58.7% recent, 24.5× ratio) aligns with Metcalf et al. 2014 on cross-tree-of-life HGT of class-I CRISPR-Cas systems. The report reads it as consistent with recent dispersal mainly through mobile-element-borne transfers. [src: gene_function_ecological_agora]
- The TCS HK recent-skew (45.1% recent, 10.3× ratio) is consistent with Alm 2006, who found TCS HK abundance correlates with recent-LSE fraction (r = 0.74 in their 207-genome substrate). [src: gene_function_ecological_agora] Explicit reproduction at r ≈ 0.74 is deferred to Phase 4 (P4-D3). This milestone delivers the underlying methodology. [src: gene_function_ecological_agora]
- Housekeeping genes show a vertical-inheritance signature (tRNA-synth 24.7% recent / 10.7% ancient; ratio 2.3×). It extends Phillips et al. 2012, who found low paralogy in bacterial ribosomal proteins (geometric mean 1.02 paralogs vs 1.63 for other universal genes) due to dosage balance. [src: gene_function_ecological_agora] The report reads this as carrying low paralogy under dosage constraint over to low recent acquisition, both manifestations of the same selective regime. [src: gene_function_ecological_agora] See [[concepts/paralog-expansion-and-gene-copy-number-constraint]].

### Methodological position

[[entities/sankoff-parsimony]] at GTDB scale follows Mirkin et al. 2003 and Csurös 2010. They used parsimony as an HGT proxy where full duplication transfer loss (DTL) reconciliation (AleRax, ALE, Notung) is computationally infeasible. [src: gene_function_ecological_agora] M22 extracts gain locations from the parsimony reconstruction and assigns each to the rank-LCA of its descendant leaves. The report says this is the same level of phylogenetic-origin claim that Alm 2006 made through lineage-specific-expansion analysis. [src: gene_function_ecological_agora]

The four-quadrant Producer × Participation framework is this project's own construction, per the M14 close-reading correction in DESIGN_NOTES v2.4. [src: gene_function_ecological_agora] Its closest literature analog is the tree-vs-net decomposition of prokaryote evolution at genome scale by Puigbò et al. 2010. [src: gene_function_ecological_agora]

The report says prior HGT-atlas work was either clade-restricted (Smillie 2011, 1,093 gut-microbiome genomes) or function-class-restricted (Forsberg 2012, the AMR resistome). [src: gene_function_ecological_agora] It claims the Phase 2 atlas is the first full-bacterial-tree-scale, all-KO-spanning, depth-resolved acquisition map under a unified methodology. [src: gene_function_ecological_agora]

### Producer × Participation cross-classification

At full GTDB scale the cross-classification has 803K Innovator-Isolated, 50K Innovator-Exchange and 742K Sink/Broker-Exchange tuples. [src: gene_function_ecological_agora] Innovator-Exchange makes up 0.36% of scored tuples. The report calls it the methodology's hardest defensible call without donor inference. It says the rarity shows where to focus the Phase 3 architectural deep-dive. [src: gene_function_ecological_agora]

### Validation

The full-atlas M21 sanity rail agrees with the earlier panel-subset validation. NB09c (panel subset) passed 6/9 strict pairs at d ≥ 0.3, with best d = 3.56. [src: gene_function_ecological_agora] The NB10 M21 sanity rail (full atlas) passed 6/6 strict pairs, with best d = 2.50. [src: gene_function_ecological_agora] The two match within Cohen's d ≤ 0.04 across all comparable pairs. [src: gene_function_ecological_agora]

## Phase 2 Atlas + M22 Acquisition Attribution (v1.7, 2026-04-27); Phase 2 Adversarial …

This part of the report covers the Phase 2 atlas and M22 acquisition attribution, and the adversarial review of that milestone. The atlas methodology was delivered, but the pre-registered hypotheses were still untested at this point. The review's main fabricated citation was checked and rejected, while two genuine concerns led to new plan commitments. [src: gene_function_ecological_agora]

### Scope and status of the milestone

NB10/NB10b delivered the atlas methodology and substrate. NB11 (regulatory versus metabolic) and NB12 (Mycobacteriota mycolic acid) were to test the actual research-plan hypotheses. [src: gene_function_ecological_agora] The report treats the atlas-as-deliverable interpretation as independent of those test outcomes. [src: gene_function_ecological_agora]

The planned NB11 diagnostic joins the atlas and acquisition-profile tables to KEGG BRITE categories from NB09. Regulatory KOs (KEGG orthologs) are 09120 Genetic IP plus 09130 Environmental IP, and metabolic KOs are 09100 Metabolism. [src: gene_function_ecological_agora] It compares acquisition-depth profiles and Producer × Participation populations between the two categories at FWER<0.05. [src: gene_function_ecological_agora] NB12 tests Innovator-Isolated status for mycolic-acid KOs (KEGG ko00540, FAS-II, mycolyl transferase) in Mycobacteriota or Mycobacteriaceae. The threshold is q < 0.0125, Bonferroni-adjusted for 4 focal tests. [src: gene_function_ecological_agora]

Phase 3 candidate KOs need an off-(low,low) Producer × Participation signal at q<0.05 with Cohen's d ≥ 0.3, and at least 2 distinct Pfam architectures. [src: gene_function_ecological_agora] The Phase 3 deep-dive includes a Cyanobacteria PSII (photosystem II) Broker hypothesis at genus rank, with composition-based donor inference. [src: gene_function_ecological_agora]

### Limits of the atlas

- **Recipient and depth, not donor.** M22 reports the rank-LCA of leaves under each gain event. This is where the gain landed, not who donated it. [src: gene_function_ecological_agora] Donor inference at deep ranks is constrained by two things. Composition signal degrades for events older than ~10–100 Myr. Per-family DTL (duplication transfer loss) reconciliation is infeasible at GTDB scale. [src: gene_function_ecological_agora]
- **Ribosomal class.** The strict range K02860-K02899 + K02950-K02998 is bimodal, with q25=0.11 and median=18.83 on Sankoff/n_present. It mixes universal r-proteins with clade-restricted accessory variants. [src: gene_function_ecological_agora] M21 therefore defines clean housekeeping as tRNA-synth plus RNAP (RNA polymerase) core only, and reports ribosomal results as informational. [src: gene_function_ecological_agora]
- **AMR.** M17 excludes AMR (antimicrobial resistance) from the positive-control panel. The bakta_amr substrate is Pseudomonadota-biased, with 49% of AMR UniRefs >50% Pseudomonadota in NB08c Diagnostic D. [src: gene_function_ecological_agora] AMR is reported as `info_amr` (54.8% recent, 4.1% ancient) for transparency and is not load-bearing. [src: gene_function_ecological_agora]
- **Non-independence.** This is only partly addressed. KO aggregation collapses intra-Pfam-family UniRef duplication, and M19 cluster-bootstrap CIs (confidence intervals) cover function-class Cohen's d. Per-(clade × KO) tuple-level CIs are deferred. [src: gene_function_ecological_agora]
- **Annotation density.** D2 residualization is not yet implemented at atlas level. Per-genome `annotated_fraction` is stored but not regressed out per (rank × KO) score. P4-D5 is meant to close this. [src: gene_function_ecological_agora]
- **CPR / DPANN.** Underrepresentation is acknowledged, and D3 effective-N reporting flags it per phase. [src: gene_function_ecological_agora]

### Adversarial review 5

`ADVERSARIAL_REVIEW_5.md` raised 4 critical, 6 important and 3 suggested issues against the v1.8 milestone. [src: gene_function_ecological_agora] The report says one important finding rests on a fabricated citation. It says three critical findings restate concerns already addressed, and two misframe defensible methodology. [src: gene_function_ecological_agora] Two genuine new concerns drive plan-level commitments: a small-n caveat and M22 biological-validation anchors. [src: gene_function_ecological_agora]

**The fabricated citation.** The review cited Mendoza et al. 2020, "Hologenome evolution: mathematical model with horizontal gene transfer" (*Microbiome* 8:1, PMID:32160912). The report identifies this as fabricated. [src: gene_function_ecological_agora] PubMed verification shows PMID 32160912 is Rezaeipandari et al. (2020), a WHOQOL-OLD validation study for Persian-speaking populations (Health and Quality of Life Outcomes 18(1):67). It is unrelated to HGT (horizontal gene transfer). [src: gene_function_ecological_agora] Searches for "Mendoza Hologenome horizontal gene transfer" and "Mendoza horizontal gene transfer regulatory metabolic mathematical model" each returned 0 results. [src: gene_function_ecological_agora]

The report rejects the attached claim that regulatory genes show 50-fold lower transfer rates than metabolic genes. That claim was the cornerstone of finding I1 and a key piece of the H1 "partially supported" verdict. [src: gene_function_ecological_agora] No project change was required. The report extended its verify-before-acting protocol to fabricated papers that carry load-bearing quantitative claims. [src: gene_function_ecological_agora]

**Methodology and effect size.** The report attributes the M1–M22 revisions to engagement with dosage cost (M2), Alm 2006 close-reading (M14), Pseudomonadota AMR bias (M17) and ribosomal contamination (M21). It says they were not data accommodation. [src: gene_function_ecological_agora] It classifies Sankoff as the primary atlas metric, a methodology role. The KO-level d=0.665–3.558 is the biological signal. [src: gene_function_ecological_agora] The four pre-registered hypotheses keep absolute-criterion adjudication: Bacteroidota PUL (polysaccharide utilization locus), Mycobacteriota mycolic-acid, Cyanobacteria PSII and Alm TCS (two-component system) reproduction. M12 governs methodology QC only. [src: gene_function_ecological_agora]

The Bacteroidota PUL hypothesis remains falsified at UniRef50 under the pre-registered absolute-zero criterion. [src: gene_function_ecological_agora] The report concedes that the UniRef50 baseline d=0.146 is small. [src: gene_function_ecological_agora] It argues that the Phase 2 KO d values of 0.665, 0.753, 0.792, 1.905, 2.504 and 3.558 are not below biological significance under Cohen conventions. [src: gene_function_ecological_agora] It also states that the NB09c M18 amplification gate passed at d=0.665-3.558. The result was reproduced at full atlas scale, with 6/6 strict pairs passing and 95% CI lower bounds > 0. [src: gene_function_ecological_agora]

**Small-n response.** The pos_crispr_cas versus neg_rnap_core_strict pair has n_pos=6 versus n_neg=3, with bootstrap 95% CI [1.55, 11.58]. The report calls this imbalance a defensibility concern. [src: gene_function_ecological_agora] The CI lower bound is stably > 0 across all 6 passing pairs, so the d ≥ 0.3 plus positive-lower-CI criterion is robust to wide upper bounds. [src: gene_function_ecological_agora]

M23 (plan v2.10) pre-registers a minimum of n_neg ≥ 20 per group for primary hypothesis tests. [src: gene_function_ecological_agora] Pairs against neg_rnap_core_strict (n=3) and the M21-excluded neg_ribosomal_strict become informational only. Primary tests use neg_trna_synth_strict (n=20) as the load-bearing housekeeping control. [src: gene_function_ecological_agora] The 3 passing pairs against tRNA-synth (d=0.65, 0.79, 2.50) survive this constraint. [src: gene_function_ecological_agora]

### Validation anchors still pending

The M22 recent-to-ancient ratios are CRISPR-Cas 24.5× and tRNA-synth 2.3×. They align qualitatively with HGT literature (Smillie 2011, Forsberg 2012, Metcalf 2014, Phillips 2012) but have not been quantitatively cross-validated against an independent dataset. [src: gene_function_ecological_agora] Plan P4-D1 (phenotype/ecology grounding via Fitness Browser, BacDive and Web of Microbes) and P4-D3 (explicit Alm r ≈ 0.74 reproduction) are designed to supply these anchors. [src: gene_function_ecological_agora] The deferred grounding would cross-reference clade × function-class tuples against NMDC sample biomes, MGnify studies, GTDB isolation-source metadata, BacDive, Web of Microbes and Fitness Browser. [src: gene_function_ecological_agora] P4-D3 would use per-genome HPK (histidine protein kinase) count and the M22-derived recent-LSE fraction at three resolutions. [src: gene_function_ecological_agora]

## Phase 2 Adversarial Review 5 Response (v1.9, 2026-04-27); Phase 2 Tier-1 Diagnostic …

This part of the report covers the response to the fifth adversarial review (plan v1.9) and the NB11 test of whether regulatory KEGG ortholog (KO) categories differ from metabolic ones in innovation and acquisition signatures. The review response found fabricated citations in the reviews. NB11 found no test reaching the pre-registered effect size, so the strong regulatory-versus-metabolic hypothesis is not supported at GTDB scale. [src: gene_function_ecological_agora] See [[concepts/complexity-hypothesis-regulatory-versus-metabolic-gene-transfer-asymmetry]] and [[concepts/adversarial-review-pre-registration-and-multiple-testing-discipline]] for the wider context.

### Adversarial review 5 response

The response found factual errors in the reviews themselves and tightened the reporting rules. REVIEW_4 falsely claimed that Alm 2006 was not cited, although it appears in references.md line 9. [src: gene_function_ecological_agora] REVIEW_5 fabricated a paper, "Mendoza 2020 Hologenome evolution", using a PMID (PubMed identifier) taken from an unrelated quality-of-life study. [src: gene_function_ecological_agora] The report calls plausible-looking fabricated citations a stable failure mode of the adversarial_project.v1 prompt under standard depth. [src: gene_function_ecological_agora] The memory feedback_adversarial_verify_before_acting.md was updated with this second confirmed case and an explicit paper-verification protocol. [src: gene_function_ecological_agora] The report recommends PubMed verification of every reviewer-cited paper that carries quantitative claims before any project change is made on its basis. [src: gene_function_ecological_agora]

The report accepted the criticism that effect-size reporting was inconsistent across phases. [src: gene_function_ecological_agora] Plan v2.10 M24 now standardizes Cohen's d plus a 95% bootstrap CI (confidence interval) as the format for all primary comparisons. [src: gene_function_ecological_agora] External validation already planned NMDC, MGnify and Fitness Browser. [src: gene_function_ecological_agora] Anantharaman 2016 and Cordero & Polz 2014 are environmental-ecology HGT (horizontal gene transfer) literature to verify and add when Phase 4 starts. [src: gene_function_ecological_agora]

### NB11 regulatory versus metabolic test

NB11 compared KOs in regulatory categories (Genetic IP ko03xxx plus Environmental IP ko02010-ko02065) with metabolic KOs (ko00xxx-ko019xx). [src: gene_function_ecological_agora] The pre-registered criterion was Cohen's d ≥ 0.3 with a 95% CI excluding zero and Mann-Whitney p < α/4 = 0.0125, a Bonferroni correction for 4 headline tests. [src: gene_function_ecological_agora] The verdict was "H1 REFRAMED — H0-atlas fallback". [src: gene_function_ecological_agora] No test reached d ≥ 0.3. Two of four showed small Bonferroni-significant signals and two were null. [src: gene_function_ecological_agora] Results per test (regulatory n, metabolic n, Cohen's d, 95% bootstrap CI, two-sided MW p; MW is the Mann-Whitney test here):

- T1 producer_z_median: 1,554 and 4,970; d +0.059; CI [−0.011, +0.124]; p 0.71; no signal. [src: gene_function_ecological_agora]
- T2 consumer_z_median: 1,552 and 4,964; d −0.211; CI [−0.288, −0.150]; p <10⁻¹⁵; a small effect in the opposite direction that fails the combined criteria. [src: gene_function_ecological_agora]
- T3 recent_acquisition_pct: 1,554 and 4,970; d +0.141; CI [+0.092, +0.189]; p 3.0×10⁻⁶; a small effect with weak direction match that fails the combined criteria. [src: gene_function_ecological_agora]
- T4 n_clades_with_max: 1,552 and 4,964; d +0.020; CI [−0.045, +0.082]; p 0.12; no signal. [src: gene_function_ecological_agora]

The report says sample size is not the limit, because the pools are large, so the effects are genuinely small. [src: gene_function_ecological_agora]

### Interpretation

The T2 direction is contrary to the strong prior. Regulatory KOs are more clumped, which implies more vertical inheritance, than metabolic KOs. [src: gene_function_ecological_agora] The two-component system (TCS) histidine kinase (HK) signal is real, with TCS-HK versus tRNA-synthetase d = 0.65 in the NB10 M21 sanity rail. It does not generalize across the regulatory category as a whole. [src: gene_function_ecological_agora] T3 is weakly consistent with a softer hypothesis: regulatory KOs have slightly more recent acquisitions (47.3% vs 45.9% recent). The magnitude, d = 0.14, is below the report's biological-significance threshold. [src: gene_function_ecological_agora]

### Innovation and exchange classes by KO category

Mixed regulatory-and-metabolic KOs show twice the Innovator-Exchange rate (0.57%) of pure regulatory (0.27%) or pure metabolic (0.28%) KOs. [src: gene_function_ecological_agora] The report treats this as a hypothesis-generating observation that warrants a Phase 3 architectural deep-dive. [src: gene_function_ecological_agora] Per category, the figures are clade × KO tuples, then percent Innovator-Exchange, Innovator-Isolated, Sink/Broker-Exchange and Stable:

- Metabolic: 5,038,487; 0.28; 4.24; 5.20; 87.85. [src: gene_function_ecological_agora]
- Regulatory: 1,609,066; 0.27; 5.72; 7.16; 84.50. [src: gene_function_ecological_agora]
- Mixed: 4,888,614; 0.57; 8.04; 5.71; 83.68. [src: gene_function_ecological_agora]
- Other: 398,805; 0.33; 4.08; 9.96; 82.73. [src: gene_function_ecological_agora]
- Unannotated: 1,804,190; 0.13; 4.88; 2.52; 89.98. [src: gene_function_ecological_agora]

Sink/Broker-Exchange is somewhat higher for regulatory KOs (7.16%) than for metabolic KOs (5.20%). The report suggests regulatory KOs take part in more cross-clade exchange events, even when the direction is unclear. [src: gene_function_ecological_agora] NB10 maps 50K Innovator-Exchange clade × KO tuples at GTDB scale. NB11 confirms they are not concentrated by the regulatory-versus-metabolic split. [src: gene_function_ecological_agora]

### Acquisition depth by KO category

The report describes differences across categories as small. [src: gene_function_ecological_agora] Percentages are recent, older_recent, mid, older, ancient:

- Metabolic: 45.92; 32.17; 10.23; 7.04; 4.64. [src: gene_function_ecological_agora]
- Regulatory: 47.27; 32.07; 9.68; 6.64; 4.34. [src: gene_function_ecological_agora]
- Mixed: 47.62; 32.75; 9.82; 6.15; 3.66. [src: gene_function_ecological_agora]
- Other: 39.99; 30.17; 11.38; 9.71; 8.75. [src: gene_function_ecological_agora]
- Unannotated: 46.88; 31.37; 9.79; 6.95; 5.01. [src: gene_function_ecological_agora]

The "other" category comprises off-target ko04xxx organismal-systems and ko05xxx human-diseases pathways. [src: gene_function_ecological_agora] It has the most ancient-skewed profile. The report calls this consistent with mostly older or eukaryotic-derived annotations that pass through PROKKA → eggNOG mapping by accident. [src: gene_function_ecological_agora] At class level, NB10b M22 gives recent-to-ancient ratios of 24.5× for CRISPR-Cas, 2.3× for tRNA-synth and 9.0× for β-lactamase. [src: gene_function_ecological_agora]

## Phase 2 Tier-1 Diagnostic — Regulatory vs Metabolic (v2.0, 2026-04-27); Phase 2 …

This part covers the close of the Phase 2 regulatory-versus-metabolic diagnostic (NB11) and the Mycobacteriaceae mycolic-acid test (NB12). NB11 falsified the strong-form regulatory-versus-metabolic hypothesis. NB12 supported a specific pre-registered clade × function hypothesis, with direct tests at two ranks. [src: gene_function_ecological_agora]

### NB11: regulatory versus metabolic H1 falsified

Phase 2 H1 (regulatory-vs-metabolic) is falsified at the strong-form criterion. This triggers the H0-atlas fallback, so the atlas continues as a descriptive resource without the regulatory-asymmetry headline. [src: gene_function_ecological_agora] See [[concepts/complexity-hypothesis-regulatory-versus-metabolic-gene-transfer-asymmetry]].

The null does not invalidate the four pre-registered clade × function hypotheses. Each tests a specific tuple, so they survive. The null only means regulatory/metabolic asymmetry cannot be used to predict them. [src: gene_function_ecological_agora] Phase 3 architectural priorities now shift toward Pfam architectures of mixed-category pathway-overlap KOs (KEGG orthologs) in the Phase-3 candidate set. [src: gene_function_ecological_agora] The notebook ran as a script in 11 s. [src: gene_function_ecological_agora] Outputs include a T1-T4 results table (Cohen's d, 95% CI, Mann–Whitney p, pass/fail), two cross-tabs (Producer × Participation × KO category; acquisition depth × KO category) and a verdict and decision log. [src: gene_function_ecological_agora]

### NB12: Mycobacteriaceae and mycolic acid

The pre-registered H1 predicted that Mycobacteriaceae (GTDB f__Mycobacteriaceae / o__Mycobacteriales) is Innovator-Isolated (high Producer, low Participation) on mycolic-acid pathway KOs. The test used family and order ranks at q < 0.0125 (α/4 Bonferroni). [src: gene_function_ecological_agora] Both ranks passed: Producer above the atlas median, meaning more paralog expansion, and Consumer below it, meaning more clumping and less cross-clade exchange. [src: gene_function_ecological_agora]

Family rank: f__Mycobacteriaceae, 582 KOs, Producer d +0.309 (Mann–Whitney p >ref 2×10⁻⁶), Consumer d −0.193 (p <ref <10⁻¹⁵), Innovator-Isolated. [src: gene_function_ecological_agora]

Order rank: o__Mycobacteriales, 614 KOs, Producer d +0.288 (Mann–Whitney p >ref 5×10⁻⁶), Consumer d −0.285 (p <ref <10⁻¹⁵), Innovator-Isolated. [src: gene_function_ecological_agora]

Producer d at family rank just exceeds the d ≥ 0.3 threshold, and at order rank it falls just below. Directions are correct and p-values are well below 0.0125 in both cases. [src: gene_function_ecological_agora]

### Acquisition depth

Mycobacteriaceae mycolic-acid gains are almost entirely recent. In the atlas-wide set, depth is spread across all bins. [src: gene_function_ecological_agora]

- Mycobacteriaceae × mycolic gains (n=53,916): recent 79.87%, older_recent 16.72%, mid 3.41%, older 0.00%, ancient 0.00%. [src: gene_function_ecological_agora]
- All mycolic-acid gains atlas-wide (n=1.47M): recent 48.79%, older_recent 31.81%, mid 9.60%, older 6.12%, ancient 3.68%. [src: gene_function_ecological_agora]

The report calls essentially all Mycobacteriaceae gains genus-rank (recent, 79.9%) or family-rank (older_recent, 16.7%). Atlas-wide, 9.8% fall in the older and ancient bins combined. [src: gene_function_ecological_agora] The report reads this as a textbook Innovator-Isolated signature: high paralog expansion, within-clade-only recent acquisitions and no deep cross-clade exchange. [src: gene_function_ecological_agora]

### Producer × Participation classes

The family-rank subset has 582 (clade × KO) tuples. [src: gene_function_ecological_agora] Counts, subset percentage and atlas-wide percentage:

- Innovator-Isolated: 67, 11.51%, atlas 5.85 (803K / 13.7M). [src: gene_function_ecological_agora]
- Stable: 497, 85.40%, atlas 86.10. [src: gene_function_ecological_agora]
- Sink/Broker-Exchange: 17, 2.92%, atlas 5.40. [src: gene_function_ecological_agora]
- Innovator-Exchange: 1, 0.17%, atlas 0.36. [src: gene_function_ecological_agora]

The report states Innovator-Isolated enrichment is 2.0× the atlas baseline, which it reads as elevated lineage-specific paralog expansion and within-clade containment. [src: gene_function_ecological_agora] Innovator-Exchange is essentially absent: 1 tuple, against ≥ 50K typical of HGT-active classes. [src: gene_function_ecological_agora] This is the project's first empirically supported pre-registered weak-prior hypothesis. [src: gene_function_ecological_agora]

### Interpretation

The report presents these as interpretation. It is consistent with mycolic-acid biosynthesis being a defining cell-envelope trait of Corynebacteriales sensu lato. The autocatalytic process requires host enzymatic context, and the report says no case is documented of a non-mycolic-acid lineage acquiring functional mycolic-acid biosynthesis. [src: gene_function_ecological_agora] It proposes that the pathway evolved in the Corynebacteriales common ancestor, and that within-clade paralog expansion then drove pathway diversity in Mycobacteriaceae. It cites the *M. tuberculosis* PE/PPE family expansion as a within-genus example. [src: gene_function_ecological_agora] It reads the zero older-or-ancient gains as a cell-envelope coupling constraint that kept the pathway from moving across phyla. [src: gene_function_ecological_agora] See also [[entities/mycobacteriaceae]] and [[concepts/paralog-expansion-and-gene-copy-number-constraint]].

### KO set definition and caveats

The candidate set has 715 KOs. They were chosen by KEGG pathway membership (ko00061 Fatty acid biosynthesis, ko00071 Fatty acid degradation, ko01040 Biosynthesis of unsaturated fatty acids, and ko00540) or by a curated list of 11 mycolic-acid-specific KOs. [src: gene_function_ecological_agora] ko00540 is actually LPS (lipopolysaccharide) biosynthesis and was included for plan-faithfulness. [src: gene_function_ecological_agora] The curated list covers Pks13/K11778, KasA/K11533, KasB/K11534, InhA/K00208, Ag85 mycolyltransferases K01205/K11211/K11212, MmaA methyltransferases K20274/K11782, K00667 and K00507. All 11 are present in the GTDB substrate. [src: gene_function_ecological_agora]

The pool also includes general fatty-acid biosynthesis, which makes the test somewhat conservative. A stricter definition might amplify the signal, but at the cost of sample size. [src: gene_function_ecological_agora]

Outputs are a per-rank test table, a Producer × Participation breakdown, and a diagnostics file with test parameters and depth profiles. [src: gene_function_ecological_agora] The notebook ran as a script in 9.4 s. [src: gene_function_ecological_agora]

## Phase 2 Mycobacteriaceae × Mycolic-Acid Hypothesis (v2.1, 2026-04-27): Phase 2 closure …

This part of the report gives the Phase 2 status of its pre-registered hypotheses. One of the three currently testable hypotheses was supported (Mycobacteriaceae × mycolic acid), one was reframed to a null fallback (regulatory versus metabolic asymmetry), and others were not yet tested. [src: gene_function_ecological_agora]

### Hypothesis scoreboard

| Hypothesis | Status | Note |
|---|---|---|
| Bacteroidota PUL (polysaccharide utilization locus) → Innovator-Exchange (Phase 1B) | Falsified at UniRef50 absolute-zero criterion in NB07 | Reframed at v2.5 close-reading; KO (KEGG ortholog) retest deferred [src: gene_function_ecological_agora] |
| Regulatory-vs-metabolic asymmetry (Phase 2 Tier-1) | H1 reframed, H0 fallback in NB11 | Signals at d=0.14-0.21 are below the d ≥ 0.3 threshold [src: gene_function_ecological_agora] |
| Mycobacteriaceae × mycolic-acid → Innovator-Isolated | H1 supported in NB12 | Both criteria pass at family and order ranks; d=0.31 with strong p; striking depth signature. The order-rank producer d is 0.288 (see Caveats). [src: gene_function_ecological_agora] |
| Cyanobacteria × PSII (photosystem II) → Broker (Phase 3) | Not yet tested | Genus-rank architectural deep-dive planned [src: gene_function_ecological_agora] |
| Alm 2006 TCS (two-component system) HK (histidine kinase) reproduction at r ≈ 0.74 (P4-D3) | Not yet tested | Deferred to Phase 4 [src: gene_function_ecological_agora] |

The report concludes that the mycolic-acid result shows its atlas methodology recovers a biologically expected Innovator-Isolated signal at the pre-registered effect-size and significance thresholds. [src: gene_function_ecological_agora] It also concludes that innovation and acquisition depth, anchored to clade phylogeny, are the atlas's productive centerpiece. [src: gene_function_ecological_agora]

### Mycolic-acid result and its interpretation

The report reads the recovered phenotype as consistent with established mycolic-acid biology. [src: gene_function_ecological_agora] It cites Marrakchi et al. (2014) as describing mycolic acids as major, specific lipid components of the mycobacterial cell envelope, essential for the survival of members of the genus Mycobacterium. [src: gene_function_ecological_agora] It describes the mAGP complex as the host enzymatic context that mycolic-acid intermediates need for incorporation into the envelope. [src: gene_function_ecological_agora]

The report offers this coupling as the mechanistic basis for the M22 acquisition-depth result of zero ancient gains. In its account, cross-phylum acquisition is impossible without disrupting envelope integrity. [src: gene_function_ecological_agora] It attributes the 79.87% recent gains to paralog expansion within Mycobacteriaceae. In this account, expansion produces variant mycolic-acid synthesis genes adapted to mycobacterial envelope chemistry. [src: gene_function_ecological_agora] The *M. tuberculosis* PE/PPE family is its example. [src: gene_function_ecological_agora] These are interpretations, not separate measurements.

The report calls NB12 a quantitative phylogenomic confirmation of the literature-derived mechanism at GTDB scale. It used 459 Mycobacteriaceae species × 715 mycolic-acid candidate KOs with Sankoff parsimony attribution. [src: gene_function_ecological_agora] It also says the result is biologically consistent with Alm 2006. Alm tested histidine protein kinase (HPK) count against LSE fraction across 207 genomes, not Mycobacteriaceae × mycolic acid. Both results show paralog expansion as a clade-level signature in specific function classes. [src: gene_function_ecological_agora]

### Regulatory versus metabolic asymmetry (NB11)

The report treats the NB11 reframing as itself a finding. It says NB11 falsifies the strong-form regulatory-vs-metabolic asymmetry prior at GTDB scale and at the pre-registered d ≥ 0.3 threshold. [src: gene_function_ecological_agora] The effect sizes (d=0.14-0.21) are statistically significant but biologically small, within the range Cohen 1988 calls "small". [src: gene_function_ecological_agora] The report therefore treats the H0-atlas fallback as the right framing. The small signals are descriptive and are not evidence for a strong-form asymmetry. [src: gene_function_ecological_agora]

One new observation came out of NB11. Mixed-category KOs, which participate in both regulatory and metabolic pathways, show 2× the Innovator-Exchange rate of pure categories (0.57% vs 0.27% / 0.28%). [src: gene_function_ecological_agora] The report treats this as hypothesis-generating. It asks whether KOs at the regulatory/metabolic interface have distinct architectural diversity that drives the elevated exchange rate. [src: gene_function_ecological_agora]

### Caveats

- **Order-rank effect size.** The d=0.31 in the scoreboard is the family-rank figure. At order rank, NB12 producer Cohen's d is 0.288, just under the 0.3 threshold. The order-rank test passes through the producer_high, consumer_low and Bonferroni-significant criteria. The strict d ≥ 0.3 effect-size criterion is met cleanly only at family rank. [src: gene_function_ecological_agora] The report therefore offers a more conservative reading: the signature is strongest at family rank (Mycobacteriaceae) and weaker but directionally consistent at order rank (Mycobacteriales). [src: gene_function_ecological_agora]
- **Candidate set breadth.** The 715 candidate KOs include general fatty-acid biosynthesis pathways (ko00061, ko00071, ko01040). The set is broader than the strict mycolic-acid pathway, so the test is somewhat conservative. [src: gene_function_ecological_agora] The report predicts that a curated set of mycolic-acid-specific KEGG-KOs (n=11) would amplify the signal at very small sample size. It says the 715-KO pool balances signal and sample size. [src: gene_function_ecological_agora]
- **Atlas-derived scores.** All Phase 2 tests use atlas-derived scores. Tests against independent experimental HGT (horizontal gene transfer) datasets are deferred to Phase 4. [src: gene_function_ecological_agora]

### Next steps proposed by the report

- NB13–NB16 Phase 3 architectural deep-dive: test the Cyanobacteria × PSII Broker hypothesis at genus rank with composition-based donor inference. [src: gene_function_ecological_agora] The candidate set is Phase 2 KOs with strong Producer × Participation signal and ≥2 distinct Pfam architectures. Open / Broker / Sink / Closed labels are applied at genus rank only. [src: gene_function_ecological_agora]
- Mixed-category follow-up: ask whether pathway-overlap KOs with elevated Innovator-Exchange rates are structurally distinct, for example multidomain proteins with regulatory and catalytic domains. [src: gene_function_ecological_agora]
- NB12 refinement: apply Pfam architecture analysis to the 67 Mycobacteriaceae × mycolic Innovator-Isolated tuples. The aim is to find the most lineage-specific mycolic-acid-related architectures. [src: gene_function_ecological_agora]
- Phase 4 P4-D1: cross-reference the NB12 tuples with Mycobacteriaceae soil, animal-host and clinical metadata. This would test whether within-clade paralog expansion correlates with niche-specific phenotype. [src: gene_function_ecological_agora] The report cites documented niche divergence among *M. tuberculosis*, *M. avium*, *M. smegmatis* and environmental species as motivation. [src: gene_function_ecological_agora]
- Phase 4 P4-D3: run the explicit Alm r ≈ 0.74 correlation computation. [src: gene_function_ecological_agora]

## Phase 2 Adversarial Review 6 Response (v2.3, 2026-04-27): Reviewer findings sorted by …

### What the review raised and the one valuable contribution

ADVERSARIAL_REVIEW_6.md raised 5 critical, 7 important and 4 suggested issues against the v2.2 milestone, which had NB11 H1 REFRAMED and NB12 H1 SUPPORTED. [src: gene_function_ecological_agora] The report calls the missing Jain 1999 complexity-hypothesis citation the one genuinely valuable literature contribution. It reads NB11 as supporting that hypothesis at small effect size, not contradicting it. [src: gene_function_ecological_agora] It describes the rest as restated issues from earlier reviews plus two factually misframed critical findings. [src: gene_function_ecological_agora]

The report verified two foundational HGT (horizontal gene transfer) citations, Lawrence & Ochman 1998 and Jain et al. 1999, in PubMed. [src: gene_function_ecological_agora] It added them to the references as Jain 1999 (PMID:10097118) and Lawrence & Ochman 1998 (PMID:9689094). [src: gene_function_ecological_agora] It positions Lawrence & Ochman 1998 as the historical composition-based HGT-detection method. Sankoff parsimony (M16) is the tree-aware successor to that method. [src: gene_function_ecological_agora] Verification of Daubin et al. 2003, which the reviewer also flagged, was deferred until Phase 3 entry. [src: gene_function_ecological_agora]

### NB11 and the complexity hypothesis

Jain et al. attribute the lower probability of horizontal transfer for informational genes to their membership in large, complex systems. [src: gene_function_ecological_agora] In NB11 at GTDB scale, regulatory KOs (KEGG orthologs) were more phylogenetically clumped than metabolic KOs (consumer_z d=−0.211, MW p<10⁻¹⁵, n_reg=1,552 vs n_met=4,964). The report reads this as less HGT, as the hypothesis predicts. [src: gene_function_ecological_agora] NB11 did not reach the pre-registered strong-form asymmetry threshold of d ≥ 0.3 in any test, so the H1 REFRAMED verdict stands. The direction of the small effect is still consistent with the literature. [src: gene_function_ecological_agora]

The report interprets the effect as real and detectable across the full bacterial tree. It judges the effect too small to dominate per-clade × per-function-class innovation patterns at the pre-registered threshold. [src: gene_function_ecological_agora] NB11 also found mixed regulatory/metabolic KOs to be the most exchange-active. The report reads this as fewer constraints than either pure category imposes. [src: gene_function_ecological_agora]

### Effect-size threshold dispute

The report cites Cohen 1988 conventions: d=0.2 small, d=0.5 medium, d=0.8 large. [src: gene_function_ecological_agora] It defends its M18 threshold of d=0.3 as the boundary between small and medium effect. [src: gene_function_ecological_agora] It rejects the reviewer's use of d=0.8 as a floor for biological meaning, because d=0.8 marks a "large" effect and is not the point below which findings are meaningless. [src: gene_function_ecological_agora] Phase 2 KO results run from d=0.665 (medium-large) to d=3.56 (very large). The report regards these as well within the conventionally significant range. [src: gene_function_ecological_agora]

### Responses to the other issues

- Small samples (n=6 vs n=20): plan M23 requires n_neg ≥ 20 for primary tests. [src: gene_function_ecological_agora] The 3 PASS pairs against tRNA-synth (n=20) survive M23 with stable estimates. [src: gene_function_ecological_agora]
- Cumulative post-hoc optimisation of M1–M22: the report points to documented diagnostic rationales, the plan v2.7 methodology freeze and M23/M24. It says each revision has an explicit NB-diagnostic rationale and is not data accommodation. [src: gene_function_ecological_agora] M12 governs methodology QC (quality control) only. Hypothesis adjudication uses an absolute criterion. [src: gene_function_ecological_agora]
- Multiple testing: NB11 used Bonferroni α/4 = 0.0125 for 4 focal tests, NB12 used the same correction, and NB09c used per-pair bootstrap CIs (confidence intervals). [src: gene_function_ecological_agora] The 13.7M atlas scores are exploratory and descriptive by design. [src: gene_function_ecological_agora]
- M22 validation anchors: these are deferred to Phase 4. P4-D1 covers NMDC, MGnify and Fitness Browser cross-validation. P4-D3 is an explicit reproduction of Alm r ≈ 0.74. [src: gene_function_ecological_agora]
- Sankoff: M16 is methodology. The d=0.665+ signal at KO level is the biological signal. [src: gene_function_ecological_agora]
- Predictions on insignificant foundations: the report says M18 passing at d=0.665-3.56 in NB09c, reproduced at full atlas scale in the NB10 M21 sanity rail, directly contradicts this. [src: gene_function_ecological_agora]
- Bacteroidota PUL (polysaccharide utilization locus) remains falsified. [src: gene_function_ecological_agora]

### Mycolic acid and KO amplification

The mycolic-acid result at order rank has d=0.288, below threshold. The report says this was already in the v2.2 Limitations section. [src: gene_function_ecological_agora] The test passes at family rank with d=0.309 through the producer_high, consumer_low and Bonferroni-significant criteria. It is weaker but directionally consistent at order rank. [src: gene_function_ecological_agora]

The report describes the KO aggregation amplification (d=0.146 → 0.665+) as empirically observed. [src: gene_function_ecological_agora] M14 reframes it as metric correction rather than aggregation per se, because Alm 2006 worked at a single-domain level comparable to UniRef50. [src: gene_function_ecological_agora] The report says a clearer theoretical framing would help Phase 3 interpretation. It defers a mechanistic-interpretation paragraph until architectural results are in. [src: gene_function_ecological_agora]

### Review trend and status

Across three adversarial rounds, the substantive concerns are stable: the small-n caveat, the cumulative M1-M22 pattern, and the need for M22 validation anchors. [src: gene_function_ecological_agora] The report says all are already addressed at plan or report level. [src: gene_function_ecological_agora] Report v2.3 adds the REVIEW_6 response and makes no plan-level changes, because the genuine concerns were already in plan v2.10. [src: gene_function_ecological_agora]

| Review | New concerns | Fabrication or error noted |
|---|---|---|
| REVIEW_4 | PIC framing, circular producer-null [src: gene_function_ecological_agora] | 1 fabricated citation (Alm 2006 not cited) and a reviewer phase-mixing arithmetic error [src: gene_function_ecological_agora] |
| REVIEW_5 | small-n caveat, M22 validation [src: gene_function_ecological_agora] | 1 fabricated Mendoza 2020 citation, with a PMID taken from a Persian quality-of-life paper [src: gene_function_ecological_agora] |
| REVIEW_6 | foundational literature gap (Lawrence 1998, Jain 1999) [src: gene_function_ecological_agora] | 0 fabrications; 1 misframed direction claim on the complexity hypothesis (C5) [src: gene_function_ecological_agora] |

The report says the fabricated-citation rate dropped from 2/2 reviews to 0/3 in this round. It tentatively attributes this to prompt-engineering work on the reviewer skill. [src: gene_function_ecological_agora] The remaining failure modes are misframing of the project's results (REVIEW_6 C5) and effect-size threshold disagreements (REVIEW_6 C3). The report says both can be fixed by clearer report framing, with no project-level changes. [src: gene_function_ecological_agora] It concludes that the project has stabilized on its supportable claims after three independent adversarial rounds. [src: gene_function_ecological_agora] The standard /submit review (REVIEW.md, 2026-04-27) returned only suggestions and no critical or important issues. [src: gene_function_ecological_agora]

## Phase 3 Closure — Architectural Resolution + Cyanobacteria PSII Hypothesis (v2.4 …

Phase 3 of the report closed at gate verdict PASS_MIXED. Consumer concordance between KO and architecture was r=0.67 and confirmatory. Producer concordance was r=0.09 and exploratory. [src: gene_function_ecological_agora] The pre-registered Cyanobacteria PSII hypothesis was supported only at class rank, and support there does not identify the donor. [src: gene_function_ecological_agora] Six notebooks (NB13-NB18) closed in ~1 day total, 4× under the v2 plan budget. The report credits this to deferring composition-based donor inference, because the data were unavailable on the KBase Data Lakehouse. [src: gene_function_ecological_agora]

### Substrate audit: choosing the Pfam source

The audit showed that bakta_pfam_domains could not support the PSII test, so the report used interproscan_domains instead. The plan had specified bakta_pfam_domains as the architectural substrate, with HMMER recomputation as a fallback. A prior plant_microbiome_ecotypes audit had found 12/22 marker Pfams silently missing. [src: gene_function_ecological_agora] The NB13 audit reproduced the pattern here. 7 of 33 marker Pfams had zero clusters in bakta_pfam_domains, including all 4 critical PSII Pfams: PsbA/PF00124, PsbB/PF02530, PsbC/PF02533 and PsbD/PF00421. [src: gene_function_ecological_agora] interproscan_domains had only 1 zero-coverage marker, PF13415, a minor HATPase variant. The report calls it the authoritative Pfam source from the Phase 1A substrate audit. [src: gene_function_ecological_agora] The median bakta/IPS coverage ratio was 0.102, so IPS had ~10× higher coverage on average. [src: gene_function_ecological_agora] The report therefore used interproscan_domains for all Phase 3 architectural work and dropped the HMMER fallback. [src: gene_function_ecological_agora] Under the bakta substrate the PSII test would have been structurally impossible, because it offered zero PSII Pfam hits. [src: gene_function_ecological_agora] Outputs are p3_pfam_completeness_audit.tsv and p3_pfam_audit_decision.json. [src: gene_function_ecological_agora]

### Candidate selection and architecture census

Filtering the atlas to off-(low,low) Producer × Participation tuples gave 10,750 candidate KOs, 78% of the 13,062 atlas KOs. [src: gene_function_ecological_agora] The census covered 4 focused subsets totaling 376 KOs, and it ran in 131 s across 3.0M gene_clusters. [src: gene_function_ecological_agora] The report says the census shows that architectural promiscuity correlates with flow. [src: gene_function_ecological_agora] Architectural diversity per KO rose from PSII to the mixed-category subset:

| Subset | KOs | Median architectures per KO | Dominant fraction | Top architecture |
|---|---|---|---|---|
| PSII (K02703-K02727) | 24 | 1 | 1.00 | PF00124 (PsbA) [src: gene_function_ecological_agora] |
| TCS HK (pos_tcs_hk) | 292 | 15 | 0.66 | PF00072_PF00486, Response_reg + Trans_reg_C [src: gene_function_ecological_agora] |
| Mycolic-acid (NB12-curated specific) | 11 | 5 | 0.93 | PF13561, Enoyl-ACP reductase [src: gene_function_ecological_agora] |
| Mixed-top-50 (highest Innovator-Exchange in mixed-category) | 48 | 46 | 0.76 | PF00005, ABC transporter [src: gene_function_ecological_agora] |

Outputs are p3_candidate_set.tsv (10,750 rows), p3_architecture_census_per_ko.tsv (15,264 rows) and p3_architecture_summary_per_ko.tsv. [src: gene_function_ecological_agora]

### Cyanobacteria PSII hypothesis test (NB16)

The hypothesis held only at class rank. It was pre-registered under the plan v2.11 reframe per M25, which is donor-undistinguished with a joint Broker OR Open criterion. It predicts high Producer and high Participation on PSII Pfam architectures in Cyanobacteria. [src: gene_function_ecological_agora] Genus, family and order ranks gave STABLE verdicts. Consumer effects there were negative, and no producer test was significant. [src: gene_function_ecological_agora] Class rank gave a large positive effect on both axes. Phylum rank gave a producer effect but had no consumer null. [src: gene_function_ecological_agora]

| Rank | n_KOs | Producer d | Consumer d | Producer MW p | Consumer MW p | Verdict |
|---|---|---|---|---|---|---|
| genus (137 Cyano genera pooled) | 2,350 | +0.08 | −0.53 | 1.00 | 1.00 | STABLE [src: gene_function_ecological_agora] |
| family (42 families) | 705 | +0.20 | −1.28 | 0.97 | 1.00 | STABLE [src: gene_function_ecological_agora] |
| order (19 orders) | 301 | +0.19 | −1.42 | 0.99 | 1.00 | STABLE [src: gene_function_ecological_agora] |
| class (c__Cyanobacteriia) | 21 | +1.50 | +0.70 | 2×10⁻⁵ | 2×10⁻⁴ | INNOVATOR-EXCHANGE (H1 SUPPORTED) [src: gene_function_ecological_agora] |
| phylum (p__Cyanobacteriota) | 21 | +1.60 | NaN | 7×10⁻⁶ | n/a | INNOVATOR-ISOLATED (no consumer null at phylum) [src: gene_function_ecological_agora] |

At class rank both pre-registered criteria passed at α/4 = 0.0125. [src: gene_function_ecological_agora] PSII KOs were less phylogenetically clumped than typical non-housekeeping KOs at that rank. [src: gene_function_ecological_agora] The hypothesis is supported but donor-undistinguished per M25. [src: gene_function_ecological_agora]

The report offers an explanation for the rank gradient. Class-rank signal that washes out at finer ranks is consistent with PSII paralog expansion being a whole-Cyanobacteriia-class property. [src: gene_function_ecological_agora] Pooling 137 genera dilutes the signal because most genera lack the full PSII paralog repertoire. [src: gene_function_ecological_agora] These are interpretations, not separate tests. Outputs are p3_nb16_cyanobacteria_psii_test.tsv, p3_nb16_pp_distribution.tsv and p3_nb16_diagnostics.json. [src: gene_function_ecological_agora]

### Acquisition depth of PSII gains

Cyanobacteria PSII gains were far less ancient than PSII gains atlas-wide. [src: gene_function_ecological_agora]

| Population | recent% | older_recent% | mid% | older% | ancient% |
|---|---|---|---|---|---|
| Cyanobacteria PSII gains (n=1,026) | 32.26 | 36.26 | 12.96 | 16.47 | 2.05 [src: gene_function_ecological_agora] |
| All PSII gains atlas-wide (n=11K) | 27.37 | 30.58 | 12.85 | 14.31 | 14.90 [src: gene_function_ecological_agora] |

The report states that Cyanobacteria has 7× fewer ancient PSII gains. [src: gene_function_ecological_agora] It reads this as a donor-origin signature. PSII originated in or near the Cyanobacteria lineage per Cardona et al. 2018, so Cyanobacteria does not receive ancient cross-phylum PSII transfers. [src: gene_function_ecological_agora] It attributes the atlas-wide ancient fraction (14.9%) to non-Cyanobacteria phyla, including Chloroflexota and certain Proteobacteria. Those phyla received PSII via documented HGT (horizontal gene transfer). [src: gene_function_ecological_agora]

### TCS HK architectural decomposition (NB17)

Decomposing TCS HK by architecture kept the consumer signal and lost the producer signal. The 292 TCS HK candidate KOs split into ~4,000 distinct Pfam architectures across 3.2M gene_clusters. [src: gene_function_ecological_agora] At family rank, producer concordance was r = 0.093, exploratory and below the 0.6 threshold. [src: gene_function_ecological_agora] Consumer concordance was r = 0.673, confirmatory and above the 0.6 threshold. [src: gene_function_ecological_agora] The report explains the producer loss by saying paralog count is a per-KO quantity that does not map cleanly to per-architecture aggregation. [src: gene_function_ecological_agora] It explains the consumer result by saying cross-clade dispersion is a property of where an architecture lives in the tree. [src: gene_function_ecological_agora]

The top TCS HK architectures by gain count all show ~45% recent and ~4-5% ancient acquisition profiles. [src: gene_function_ecological_agora]

| Architecture | Interpretation | Gain events |
|---|---|---|
| PF00072_PF00486 | Response_reg + Trans_reg_C | 76,212 [src: gene_function_ecological_agora] |
| PF00072 | Response_reg alone | 39,861 [src: gene_function_ecological_agora] |
| PF00072_PF00196 | Response_reg + GerE | 37,528 [src: gene_function_ecological_agora] |
| PF00512_PF00672_PF02518 | HisKA + ExtSensor + HATPase_c | 25,878 [src: gene_function_ecological_agora] |
| PF00512_PF02518 | HisKA + HATPase_c, the canonical Alm 2006 architecture | 25,462 [src: gene_function_ecological_agora] |

The report treats HisKA + HATPase_c as the canonical Alm 2006 architecture, equivalent to their IPR005467 single-domain detection scaled to multidomain. Its 44.7% recent and 4.5% ancient profile is recent-skewed, which the report calls consistent with Alm 2006's lineage-specific-expansion finding. [src: gene_function_ecological_agora]

## Phase 3 Closure — Architectural Resolution + Cyanobacteria PSII Hypothesis (v2.4 … (2)

This part of the report closes Phase 3. It gives a mixed architectural verdict: consumer-side signal is confirmatory, producer-side signal is exploratory. It also tests the Cyanobacteria photosystem II (PSII) donor-origin hypothesis, and it sets the Phase 4 deliverables. [src: gene_function_ecological_agora]

### Architectural back-test of the two-component system histidine kinase (TCS HK) atlas

The back-test asks whether Pfam-architecture-level results agree with the KEGG-ortholog (KO)-level atlas. The agreement is mixed, and the phase-gate verdict is PASS_MIXED. [src: gene_function_ecological_agora] The method joined family-rank pp-categories through interproscan_domains. It then ran a Spearman correlation across 8,498 overlapping family × architecture tuples. [src: gene_function_ecological_agora] Consumer concordance (r=0.67) is confirmatory. [src: gene_function_ecological_agora] Producer concordance is exploratory (r=0.09). The report says paralog count is intrinsically per-KO, so decomposing it across architectures dilutes the signal. [src: gene_function_ecological_agora]

The report reads the mixed result as biologically interpretable. Consumer scores reflect cross-clade prevalence, which aggregates similarly across resolutions. Producer scores reflect within-clade paralog expansion, where the architecture grain captures domain-shuffling that the KO grain hides. [src: gene_function_ecological_agora]

Under plan v2.11, Phase 4 treats consumer/participation results as confirmatory (r ≥ 0.6) and producer results as exploratory (r < 0.6). [src: gene_function_ecological_agora] Phase 4 atlas claims rest mainly on Phase 1B and Phase 2 KO-level results. Phase 3 architecture supports consumer-side patterns and offers exploratory commentary on producer-side patterns. [src: gene_function_ecological_agora]

The canonical Alm 2006 architecture (HisKA + HATPase_c) appears at 25K gain events, with 44.7% recent and 4.5% ancient acquisition. The report calls this consistent with Alm 2006's lineage-specific-expansion finding. [src: gene_function_ecological_agora] The full r ≈ 0.74 reproduction, per-genome HPK count against recent-LSE fraction, is deferred to Phase 4 P4-D3. [src: gene_function_ecological_agora]

### Architectural diversity and cross-clade exchange

NB15 compares architectural diversity across four KO subsets. The report concludes that higher architectural diversity per KO correlates with elevated atlas-level cross-clade exchange. [src: gene_function_ecological_agora]

| Subset | Median architectures/KO | Median dominant_fraction | Linked result |
|---|---|---|---|
| PSII | 1 | 1.00 | Cyano-class Innovator-Exchange, rank-restricted (NB16) [src: gene_function_ecological_agora] |
| Mycolic-acid | 5 | 0.93 | Innovator-Isolated at family and order in Mycobacteriaceae (NB12) [src: gene_function_ecological_agora] |
| TCS HK | 15 | 0.66 | Atlas-wide signature class; M21 sanity rail PASS at d=0.65-0.79 [src: gene_function_ecological_agora] |
| Mixed-top-50 | 46 | 0.76 | NB11 Innovator-Exchange at 2× the rate for pure regulatory or metabolic KOs [src: gene_function_ecological_agora] |

The report states that a KO's structural diversity predicts its propensity to flow. It claims novelty: to its knowledge, no prior GTDB-scale atlas framed cross-clade exchange propensity as a function of within-KO architectural promiscuity. [src: gene_function_ecological_agora] The proposed mechanism is a hypothesis. KOs with many possible domain combinations may be more modular and less constrained by host-specific protein-protein interaction networks. This would apply the Jain 1999 complexity hypothesis at the architectural level. [src: gene_function_ecological_agora] Phase 4 P4-D2 (MGE context) and P4-D3 (Alm reproduction) could test the finding formally. [src: gene_function_ecological_agora]

### Cyanobacteria PSII hypothesis

The PSII test supports a donor-origin signature, but only at class rank. The literature anchor is Cardona et al. (2018). They give phylogenomic and Bayesian relaxed-clock evidence that a water-oxidizing photosystem appeared ~1 Gyr before the MRCA of described Cyanobacteria and before anoxygenic photosynthetic bacteria diversified. [src: gene_function_ecological_agora] The report uses this as an anchor: Cyanobacteria's ancestor evolved PSII, and non-Cyanobacteria phyla received it by horizontal gene transfer (HGT) well afterward. [src: gene_function_ecological_agora] It cites Smillie et al. 2011 and the Forsberg-Bonomo β-lactamase line for a recent-skewed acquisition signature in broadly HGT-active classes. [src: gene_function_ecological_agora] Low ancient acquisition for PSII within Cyanobacteria is the opposite signature, which the report calls the diagnostic complement consistent with PSII originating there. [src: gene_function_ecological_agora]

NB16 supports the donor-undistinguished Cyanobacteria × PSII joint Broker-OR-Open Innovator-Exchange hypothesis at class rank. Producer d=1.50, consumer d=0.70, p<10⁻³. Ancient acquisition is 7× lower than atlas-wide PSII, read as a donor-origin signature. [src: gene_function_ecological_agora]

Several caveats limit this result:
- The signal is class-rank-only. Pooling washes it out at family, order and genus. [src: gene_function_ecological_agora]
- The test is joint Innovator-Exchange (Broker OR Open) with no Broker-vs-Open separation. It makes the same level of phylogenetic-origin claim as Alm 2006. [src: gene_function_ecological_agora]
- Composition-based donor inference (codon usage, k-mers) was deferred under M25. Per-CDS sequence data are not in the KBase Data Lakehouse queryable schemas. [src: gene_function_ecological_agora]

### Pre-registered hypothesis scorecard

The report counts 2 of 4 currently-testable pre-registered hypotheses confirmed, 1 falsified at UniRef50, and 1 reframed at small effect size in the literature-predicted direction. [src: gene_function_ecological_agora]
- The Bacteroidota PUL → Innovator-Exchange hypothesis (Phase 1B, NB07) was falsified at the UniRef50 absolute-zero criterion. [src: gene_function_ecological_agora]
- The regulatory-versus-metabolic asymmetry hypothesis (NB11) is H1 REFRAMED. Its direction supports the Jain 1999 complexity hypothesis at small effect size. [src: gene_function_ecological_agora]
- Mycobacteriaceae × mycolic-acid → Innovator-Isolated (NB12) is H1 SUPPORTED at family and order. Producer d=0.31, consumer d=−0.19, p<10⁻¹⁵, with 79.9% recent and 0% ancient acquisition. [src: gene_function_ecological_agora]
- Cyanobacteria × PSII (NB16) is H1 SUPPORTED at class rank, as above. [src: gene_function_ecological_agora]

### Scope limits

The architecture census is focused: 376 KOs across 4 subsets, not atlas-wide. [src: gene_function_ecological_agora] An 833M-row IPS scan over the full 10,750-KO scope was infeasible via Spark Connect within practical timescales. This led the v2.11 reframe to focused Phase 3 subsets. [src: gene_function_ecological_agora]

### Proposed next work (Phase 4)

- **P4-D1 phenotype/ecology grounding** would use NMDC, MGnify, GTDB metadata, BacDive, Web of Microbes and Fitness Browser. It would test whether high-architectural-diversity KOs cluster in specific environments. [src: gene_function_ecological_agora]
- The PSII donor-origin signature would be checked against environmental metadata. Non-Cyanobacteria PSII recipients should overlap photic ecosystems. [src: gene_function_ecological_agora]
- **P4-D2** would test whether high-Innovator-Exchange KOs from Phase 2 and Phase 3 are mobile-genetic-element (MGE) mediated. [src: gene_function_ecological_agora] Phage, plasmid and integron context flagging would test a mechanism for why pathway overlap and architectural promiscuity correlate with cross-clade flow. [src: gene_function_ecological_agora]
- **P4-D3** would attempt to reproduce Alm 2006 r ≈ 0.74 using per-genome HPK count (PF00512 hits) against per-genome recent-LSE fraction derived from M22. [src: gene_function_ecological_agora]
- **P4-D4** would test whether high-Innovator-Exchange clades have open pangenomes (Tettelin 2005 / McInerney 2017). [src: gene_function_ecological_agora]
- **P4-D5** is annotation-density bias residualization, for D2 closure. [src: gene_function_ecological_agora]
- Individual Cyanobacteria lineages, such as Synechococcus and Prochlorococcus marine clades, could be tested for finer-grained PSII evolution. [src: gene_function_ecological_agora]

The phase-gate and architectural work are supplied by NB17 and NB18 notebooks. [src: gene_function_ecological_agora]

## Phase 3 Adversarial Review 7 Response (v2.5, 2026-04-28): Substantive concerns sorted

This part of the report covers the response to ADVERSARIAL_REVIEW_7, which raised 6 critical, 8 important and 5 suggested issues against the v2.4 Phase 3 closure milestone. [src: gene_function_ecological_agora] The most useful outcome was a literature check of the reviewer's citations, which confirmed several real papers, corrected one wrong identifier and flagged one fabrication. The main new support came from Burch et al. 2023 for the complexity-hypothesis reframing; see [[concepts/complexity-hypothesis-regulatory-versus-metabolic-gene-transfer-asymmetry]]. The review process itself is discussed in [[concepts/adversarial-review-pre-registration-and-multiple-testing-discipline]].

### Citation verification

The report checked the reviewer's citations. Bansal, Alm, Kellis 2013 on DTL (duplication transfer loss) reconciliation was verified as real. [src: gene_function_ecological_agora] Ślesak 2024 on PSII (photosystem II) evolution was verified, with a slight page-number error by the reviewer (actual pages 1055-1067). [src: gene_function_ecological_agora] Denise, Abby, Rocha 2019 on Type IV filament was verified, and the reviewer's quote was accurate. [src: gene_function_ecological_agora]

The reviewer gave Burch et al. 2023 the PMID (PubMed identifier) 37279472, which actually points to a COVID-19 sense-of-coherence study. The real paper has PMID 37232518 and DOI 10.1093/gbe/evad089, and it is relevant. [src: gene_function_ecological_agora] The reviewer self-flagged Koech et al. 2025 on nodD-like LysR α-Proteobacteria as fabricated, which REVIEW_4/5/6 did not do for their own citations. [src: gene_function_ecological_agora] The report calls this the first round to flag a fabrication explicitly, because the DOI was not found in Crossref. [src: gene_function_ecological_agora]

The report added Bansal et al. 2012 (PMID:22689773), Burch et al. 2023 (PMID:37232518, corrected from the reviewer's 37279472), Ślesak et al. 2024 (PMID:38439684) and Denise et al. 2019 (PMID:31323028) to its references, all PubMed-verified. [src: gene_function_ecological_agora]

### Literature support for the findings

**Burch 2023 and the complexity hypothesis.** The report treats Burch et al. 2023 as empirical validation of the complexity hypothesis at the genomic level, and treats its own NB11 finding as the GTDB-scale instantiation. [src: gene_function_ecological_agora] Burch et al. put shotgun libraries of 74 prokaryote genomes into *E. coli*. They found that transferability declines as connectivity increases, with translational proteins showing the strongest effect. [src: gene_function_ecological_agora] NB11 found regulatory KOs (KEGG orthologs) more phyletically clumped than metabolic KOs at the function-class pool level (d=−0.21 at p<10⁻¹⁵). [src: gene_function_ecological_agora] The report says the two studies recover the same signal at different scales. Burch measured per-(donor × *E. coli*) HGT (horizontal gene transfer) rate against connectivity. NB11 measured per-(clade × KO) clumping against the regulatory/metabolic split. [src: gene_function_ecological_agora] It frames the NB11 H1 REFRAMED verdict as a contribution to the empirical complexity-hypothesis literature at full-bacterial-tree scale, not a contradiction of the working hypothesis. [src: gene_function_ecological_agora] It also says REPORT v2.3 had already framed NB11 as direction-consistent with Jain 1999. [src: gene_function_ecological_agora]

**DTL reconciliation.** Bansal's DTL work is described as the principled methodology, with the report's Sankoff parsimony as the lightweight, tractable alternative at GTDB scale. [src: gene_function_ecological_agora] See [[entities/sankoff-parsimony]]. AleRax was reserved for sub-sample reconciliation, and Bansal 2012 is its algorithmic predecessor. [src: gene_function_ecological_agora]

**PSII and architecture.** NB16's 7× lower ancient % in Cyanobacteria is consistent with both Ślesak 2024 and Cardona 2018, which the report reads as joint support for PSII donor-origin. [src: gene_function_ecological_agora] Denise 2019 found that systems encoded in fewer loci were exchanged between taxa more often. The report calls this the genome-organization analog of NB15's finding that more architectures per KO accompany more exchange. [src: gene_function_ecological_agora] Both link structural simplicity to cross-clade flow. [src: gene_function_ecological_agora] The report therefore recasts NB15 as the GTDB-scale instance of an established modular gene-family pattern, not a novel observation. [src: gene_function_ecological_agora]

### Handling of the reviewer's issues

Several issues were already addressed or deferred:

- Missing validation anchors for M22 are acknowledged and deferred to Phase 4 P4-D1/P4-D3. [src: gene_function_ecological_agora]
- The mycolic-acid effect (d=0.288) is marginal at order rank and was already listed as a limitation. [src: gene_function_ecological_agora]
- TCS (two-component system) architectural concordance in NB17 is mixed. This is documented, and Phase 4 treats Phase 3 as PASS_MIXED. [src: gene_function_ecological_agora]
- Bonferroni correction is applied per test family: NB11, NB12 and NB16 each have 4 tests at α/4. [src: gene_function_ecological_agora] Atlas-wide testing across 13.7M scores is exploratory by design, under the H0-atlas fallback. [src: gene_function_ecological_agora]
- With M25 deferred, Phase 3 reports Innovator-Exchange as joint Broker OR (odds ratio) Open, with no donor distinction. [src: gene_function_ecological_agora]

### Cyanobacteria PSII sample size and rank dependence

The report accepts the n=21 sample size and the rank-dependent contradictions as real concerns. [src: gene_function_ecological_agora] At class rank, producer α=2×10⁻⁵ and consumer α=2×10⁻⁴ are both below the Bonferroni threshold α/4=0.0125, and the effect is d=1.50. [src: gene_function_ecological_agora] Cyanobacteria PSII is STABLE at genus, family and order ranks but INNOVATOR-EXCHANGE at class rank. [src: gene_function_ecological_agora] See [[concepts/clade-level-innovation-signals-and-their-rank-dependence]].

The report's explanation has two parts. The genus, family and order ranks pool 137, 42 and 19 individual Cyano clades respectively. [src: gene_function_ecological_agora] Most individual genera lack the full PSII paralog repertoire, which dilutes the signal. [src: gene_function_ecological_agora] The class rank pools all 21 PSII KOs across the single Cyanobacteriia clade. [src: gene_function_ecological_agora] The two are different statistical objects: many clades with variable content versus one clade with pooled content. [src: gene_function_ecological_agora] The report reads the class verdict as a class-level lineage signature, and the gradient as consistent with PSII being a class-wide rather than genus-wide property. [src: gene_function_ecological_agora]

The report's defence of the small sample has these points, and the first two are its own arguments:

- The M23 minimum of n_neg ≥ 20 does not directly apply. The comparison is against an atlas non-housekeeping reference with n_ref ≫ 1000, and the small sample is the target. [src: gene_function_ecological_agora]
- Cohen's d has higher variance at small N. The report argues that a stable d=1.50, with a bootstrap-CI-positive lower bound and α=2×10⁻⁵, is a real effect and not chance inflation. [src: gene_function_ecological_agora]
- Smaller N accompanying larger d partly reflects that small-N tests need larger d to clear significance, so it is not necessarily bias. [src: gene_function_ecological_agora]
- Limit: NB17's producer concordance of r=0.09 shows that small effects do not survive at architectural granularity even when reported. [src: gene_function_ecological_agora]

## Phase 3 Adversarial Review 7 Response (v2.5, 2026-04-28); Phase 4 Deliverables P4-D3 + …

This part of the report covers the seventh adversarial review and two Phase 4 deliverables. REVIEW_7 added the most literature value of any round so far. [src: gene_function_ecological_agora] P4-D3 did not reproduce Alm 2006's r ≈ 0.74. [src: gene_function_ecological_agora] P4-D5 found that annotation-density residualization left every hypothesis verdict intact. [src: gene_function_ecological_agora]

### REVIEW_7 and the trend across reviews

The report calls REVIEW_7 the strongest adversarial round to date. It contributed 4 real verified citations directly relevant to project findings. [src: gene_function_ecological_agora] It was also the first review in which the reviewer flagged its own fabricated citation (Koech 2025). A Burch 2023 PMID (PubMed identifier) error remained: the paper was cited at the wrong PMID, though the real paper exists at the correct one. [src: gene_function_ecological_agora] See [[concepts/adversarial-review-pre-registration-and-multiple-testing-discipline]].

- Review 4: 5 critical findings, 1 fabricated citation (Alm 2006 hallucination), 0 self-flags, M19/M20 actionable, medium net new value. [src: gene_function_ecological_agora]
- Review 5: 5 critical findings, 1 fabricated citation (Mendoza 2020 PMID hijack), 0 self-flags, M23 actionable, low net new value. [src: gene_function_ecological_agora]
- Review 6: 4 critical findings, 0 fabricated citations, 0 self-flags, Lawrence 1998 and Jain 1999 contributed, medium net new value. [src: gene_function_ecological_agora]
- Review 7: 6 critical findings, 1 fabricated citation (Koech 2025) plus 1 PMID error (Burch 2023), 1 self-flag (first time), HIGH net new value from Burch 2023, Bansal 2013, Ślesak 2024 and Denise 2019. [src: gene_function_ecological_agora]

### P4-D3: reproducing Alm 2006

P4-D3 was the project's headline quantitative anchor to Alm, Huang, Arkin 2006, which reported r ≈ 0.74. [src: gene_function_ecological_agora] It joined per-genome histidine protein kinase (HPK) counts, taken from PF00512 hits in interproscan_domains, to per-genome recent lineage-specific expansion (LSE) fractions from M22 recent-rank gain attribution. The join covered all 18,989 P1B-qualified species representatives. [src: gene_function_ecological_agora] The outputs were data/p4d3_correlations.tsv, data/p4d3_per_species_hpk_lse.tsv and data/p4d3_diagnostics.json. [src: gene_function_ecological_agora]

The verdict was NOT REPRODUCED. All correlations were statistically significant at n = 18,989 but biologically modest. The report states their range as r = 0.10–0.29, against Alm 2006's r ≈ 0.74 in 207 genomes. [src: gene_function_ecological_agora] The Spearman coefficient for the genus-rank test, 0.333, lies slightly above that stated range. [src: gene_function_ecological_agora]

Results at n = 18,989 species representatives (TCS is two-component system, HK is histidine kinase, KO is KEGG ortholog):
- HPK count vs recent TCS gains at genus rank: Pearson r = 0.288, Spearman r = 0.333, p <10⁻³⁰⁰. [src: gene_function_ecological_agora]
- HPK count vs recent-LSE fraction (per gene cluster): Pearson r = 0.157, Spearman r = 0.222, p <10⁻¹⁰⁵. [src: gene_function_ecological_agora]
- HPK count vs recent-LSE per TCS HK KO: Pearson r = 0.100, Spearman r = 0.152, p <10⁻⁴³. [src: gene_function_ecological_agora]
- Alm-2006-style HPK fraction vs recent-LSE fraction: Pearson r = 0.105, Spearman r = 0.106, p <10⁻⁴⁷. [src: gene_function_ecological_agora]

The report offers three explanations for the gap. These are its interpretations, not separate tests.
- **Substrate.** Alm 2006 used 207 genomes, mostly cultivated isolates with high annotation density. This project's substrate spans the full GTDB tree, including DPANN, CPR (candidate phyla radiation) and weakly annotated lineages where HPK detection is genuinely sparse. [src: gene_function_ecological_agora]
- **Method.** M22 uses Sankoff-parsimony recent-rank gain attribution on the species tree. It would miss expansions occurring entirely within a single recent species. The report says the two metrics measure overlapping but non-identical phenomena. [src: gene_function_ecological_agora] See [[entities/sankoff-parsimony]].
- **Definition of "recent".** In M22, recent means a leaf-adjacent gain, which captures within-genus diversification. Alm's per-genome paralog counts capture expansion at any phylogenetic depth. The two definitions converge for very recent expansions and diverge for older ones. [src: gene_function_ecological_agora]

The qualitative result still holds at architectural resolution. NB17 found the canonical PF00512 + PF02518 TCS HK architecture concentrated at recent ranks. Consumer-side concordance between architectural and KO-level signals was r = 0.67. [src: gene_function_ecological_agora] The report therefore describes the project's lineage as methodological generalization of Alm 2006, not point-estimate reproduction. [src: gene_function_ecological_agora] See [[concepts/paralog-expansion-and-gene-copy-number-constraint]].

### P4-D5: annotation-density residualization

D2 was specified in plan v1 and v2 as regressing per-genome annotated fraction out as a nuisance covariate. It was deferred several times across phases. [src: gene_function_ecological_agora] Adversarial reviews 4–7 repeatedly flagged it as a defensibility gap. [src: gene_function_ecological_agora] See [[concepts/annotation-coverage-and-annotation-density-bias-in-functional-enrichment]].

P4-D5 regressed four per-clade covariates against producer_z and consumer_z separately by ordinary least squares (OLS). The covariates were clade size, mean annotated fraction, mean GC% and mean genome size. It then re-ran the NB11, NB12 and NB16 hypothesis tests on the residuals. [src: gene_function_ecological_agora] Outputs were a residualized atlas of 13.7M rows, diagnostics, a hypothesis replication table and a residualization-panel figure. [src: gene_function_ecological_agora]

**Covariate models.**
- **Producer.** R² = 0.000, and producer_z was uncorrelated with all 4 covariates. The report attributes this to the within-rank null model already absorbing prevalence and clade-size effects. [src: gene_function_ecological_agora]
- **Consumer.** R² = 0.053, small but non-zero. [src: gene_function_ecological_agora]
- **Consumer coefficients.** The mean_annotated_fraction_z coefficient was −1.27. Higher-annotated clades had more-negative consumer_z, consistent with fewer missing KOs. [src: gene_function_ecological_agora] The clade_size_z coefficient was +1.13, so larger clades had less-negative consumer_z. [src: gene_function_ecological_agora] mean_genome_size_z was −0.49 [src: gene_function_ecological_agora] and mean_gc_z was −0.05. [src: gene_function_ecological_agora]

**Hypothesis tests.** Every verdict survived residualization. The largest attenuation was NB12 family-rank consumer-side, with d going from −0.19 to −0.16 (about 16% relative attenuation). It stayed significant. [src: gene_function_ecological_agora] Under residualization, NB11 stayed H1 REFRAMED in the complexity-hypothesis direction. Mycobacteriaceae × mycolic acid stayed Innovator-Isolated H1 SUPPORTED. Cyanobacteria × PSII (photosystem II) stayed class-rank Innovator-Exchange H1 SUPPORTED. [src: gene_function_ecological_agora] See [[concepts/complexity-hypothesis-regulatory-versus-metabolic-gene-transfer-asymmetry]] and [[entities/mycobacteriaceae]].

Raw Cohen's d, residualized d and residualized p for each test:
- NB11 regulatory vs metabolic producer_z: +0.06, +0.06, p = 0.69 (null). [src: gene_function_ecological_agora]
- NB11 regulatory vs metabolic consumer_z: −0.21, −0.21, p <10⁻¹⁰. [src: gene_function_ecological_agora]
- NB12 Mycobacteriaceae × mycolic family, producer_z: +0.31, +0.31, p = 2×10⁻⁶. [src: gene_function_ecological_agora]
- NB12 Mycobacteriaceae × mycolic family, consumer_z: −0.19, −0.16, p = 1.6×10⁻⁵. [src: gene_function_ecological_agora]
- NB12 Mycobacteriales × mycolic order, producer_z: +0.29, +0.29, p = 5×10⁻⁶. [src: gene_function_ecological_agora]
- NB12 Mycobacteriales × mycolic order, consumer_z: −0.29, −0.28, p <10⁻¹⁰. [src: gene_function_ecological_agora]
- NB16 Cyanobacteriia × PSII producer_z (class): +1.50, +1.50, p = 2.1×10⁻⁵. [src: gene_function_ecological_agora]
- NB16 Cyanobacteriia × PSII consumer_z (class): +0.70, +0.63, p = 2.3×10⁻⁵. [src: gene_function_ecological_agora]

### Planned remaining Phase 4 work

Three deliverables were still planned. [src: gene_function_ecological_agora]
- **P4-D4:** within-species pangenome openness validation, using Heaps' law or accumulation curves on the species representatives. [src: gene_function_ecological_agora]
- **P4-D2:** mobile genetic element (MGE) context per gain event, with ingestion verification of bakta_annotations and genomad_mobile_elements. [src: gene_function_ecological_agora]
- **P4-D1:** phenotype and ecology grounding using NMDC, MGnify, GTDB metadata, BacDive, Web of Microbes and Fitness Browser. [src: gene_function_ecological_agora]

## Phase 4 Deliverable P4-D4 — Pangenome Openness vs M22 Recent-Acquisition (v2.7 …

This part of the report tests whether species pangenome openness tracks M22 recent-rank gain attribution across genera. It finds a clear null atlas-wide, so openness does not work as cross-substrate validation of M22. It then describes the P4-D1 ecological grounding, where all three pre-registered findings sit in expected biomes. [src: gene_function_ecological_agora]

### P4-D4: pangenome openness versus M22 recent gains

P4-D4 cross-correlated per-species pangenome openness (1 − no_core/no_gene_clusters, from motupan output in kbase_ke_pangenome.pangenome) with genus-level M22 recent-rank gain attribution. It was designed as an independent-substrate cross-validation of M22. [src: gene_function_ecological_agora] The substrate was 18,989 P1B-qualified species representatives, of which 10,856 had no_genomes ≥ 3. [src: gene_function_ecological_agora] These covered 3,539 genera with at least one multi-genome species, and 894 genera with ≥3 multi-genome species formed the T1 substrate. [src: gene_function_ecological_agora] The M22 side used 7.95M recent-rank gain events (depth_bin = 'recent', recipient_genus non-null). [src: gene_function_ecological_agora]

The atlas-wide tests were null, and the two targeted clade tests were positive in direction but underpowered. [src: gene_function_ecological_agora] Results (KO = KEGG ortholog; PSII = photosystem II; CI = confidence interval):

- T1 atlas-wide openness vs log(recent gains), n = 894 genera: Pearson r = +0.017, Spearman r = −0.011, 95% CI (−0.08, +0.06); null. [src: gene_function_ecological_agora]
- T2 regulatory KOs only, n = 894: Pearson r = +0.023, Spearman r = −0.013, 95% CI (−0.08, +0.05); null. [src: gene_function_ecological_agora]
- T2 metabolic KOs only, n = 894: Pearson r = +0.010, Spearman r = −0.017, 95% CI (−0.08, +0.05); null. [src: gene_function_ecological_agora]
- T3a Mycobacteriaceae × mycolic, n = 10: Pearson r = +0.46, Spearman r = +0.41, 95% CI (−0.43, +0.86); directional, underpowered. [src: gene_function_ecological_agora]
- T3b Cyanobacteriia × PSII, n = 83: Pearson r = +0.11, Spearman r = +0.12, 95% CI (−0.10, +0.34); directional, underpowered. [src: gene_function_ecological_agora]

The report calls both T3 directions positive and consistent with the NB12/NB16 verdicts. Neither confidence interval excludes zero. [src: gene_function_ecological_agora] Multi-genome coverage was the limit: 289 species across 10 Mycobacteriaceae genera and 185 species across 83 Cyanobacteriia genera. [src: gene_function_ecological_agora]

The report explains the null by saying the two measures capture different things. M22 recent gains are between-species KO presence/absence transitions on the GTDB species tree, inferred by Sankoff parsimony; a recent gain is present in one species and absent in its sister. [src: gene_function_ecological_agora] Openness is within-species genome-set diversity, the fraction of non-core gene clusters; high openness means high strain-level variability. [src: gene_function_ecological_agora] The report reads them as independent. A genus can have many recent gains and compact species pangenomes, or the reverse. [src: gene_function_ecological_agora] This is the report's interpretation. It concludes that openness is not a valid cross-substrate validation of M22, although the design assumed the two would correlate. [src: gene_function_ecological_agora] The null clarifies that M22 detects lineage-level, between-species gain attribution, not within-species strain diversity. [src: gene_function_ecological_agora]

Two consequences follow. No headline verdict changes: NB11 H1 stays REFRAMED, and NB12 H1 and NB16 H1 stay SUPPORTED. [src: gene_function_ecological_agora] Cross-substrate validation of M22 remains an open project commitment. [src: gene_function_ecological_agora] The report proposes P4-D1 phenotype/ecology grounding as the remaining Phase 4 route. It asks whether high recent acquisition in a function class correlates with the expected biomes or phenotypes. [src: gene_function_ecological_agora] Outputs include a per-genus openness table (3,539 genera), a table for the 894 solid-substrate genera, and a diagnostics file. [src: gene_function_ecological_agora]

### P4-D1: environmental substrate audit

P4-D1 is the project's interpretive layer. It grounds the pre-registered atlas findings against three independent substrates inside the KBase Data Lakehouse. [src: gene_function_ecological_agora] The NB22a–22f audit found two pangenome-internal substrates the earlier plan had missed: ncbi_env (4.1M-row EAV environment metadata) and alphaearth_embeddings_all_years (64-dim satellite-imagery vectors). [src: gene_function_ecological_agora] Together with kescience_mgnify, which has 28.4% biome coverage, they give richer environmental annotation than the v2.9 plan's external list. [src: gene_function_ecological_agora]

The report admits its initial audit was wrong. That audit had recommended scoping P4-D1 to 5–7 days using only GTDB metadata, BacDive, NMDC and Fitness Browser. [src: gene_function_ecological_agora] The user pointed out that ncbi_env and alphaearth_embeddings had not been examined. [src: gene_function_ecological_agora] With them added, P4-D1 became 3 days and, per the report, substantially stronger. [src: gene_function_ecological_agora]

The audit measured coverage of the 18,989 species for each substrate, listed here. [src: gene_function_ecological_agora]

- ncbi_env isolation_source: 76.8%, text. [src: gene_function_ecological_agora]
- ncbi_env geo_loc_name: 88.8%, country/region text. [src: gene_function_ecological_agora]
- ncbi_env env_broad_scale (ENVO, Environment Ontology): 48.6%, controlled biome vocabulary. [src: gene_function_ecological_agora]
- ncbi_env lat_lon: 47.3%, numeric coordinates. [src: gene_function_ecological_agora]
- alphaearth_embeddings_all_years: 27.2% (5,157 species), 64-dim vectors. [src: gene_function_ecological_agora]
- kescience_mgnify.species biome_id: 28.4% (5,392 species), 18 biome categories. [src: gene_function_ecological_agora]
- BacDive phenotype tables (GCF→GCA fallback): 32% (6,066 species); 100% of matched species had metabolite/physiology/enzyme rows. [src: gene_function_ecological_agora]
- gtdb_metadata.ncbi_isolation_source: 74.6% non-trivial; redundant with ncbi_env. [src: gene_function_ecological_agora]
- NMDC species-taxid overlap: 9.4% (1,791 species), supplementary sample-level data. [src: gene_function_ecological_agora]
- Fitness Browser BBH (bidirectional best hit): 0.18% (35 species), point-validation only. [src: gene_function_ecological_agora]

### P4-D1: biome enrichment results

All three pre-registered findings ground in expected biomes at p < 10⁻¹¹. BacDive phenotype anchors confirm two of three, and AlphaEarth environmental-cluster concentration confirms all three. [src: gene_function_ecological_agora] The analysis joined biome assignments (MGnify first, then ENVO, then isolation_source) to the 18,989 species representatives. It ran one-sided Fisher's exact tests of clade enrichment against the atlas distribution. [src: gene_function_ecological_agora]

- **NB16 PSII Innovator-Exchange:** Cyanobacteriia (n=309) were 63.8% photic aquatic versus 23.0% of the atlas, 2.77× enrichment, p < 10⁻⁵². [src: gene_function_ecological_agora] They were 35.3% marine versus 15.1%, 2.33×, p < 10⁻¹⁸. [src: gene_function_ecological_agora]
- **NB12 mycolic-acid Innovator-Isolated:** Mycobacteriaceae (n=459) were 16.6% host-pathogen versus 2.1%, 7.88×, p < 10⁻⁴⁵. [src: gene_function_ecological_agora]
- **Phase 1B Bacteroidota PUL (polysaccharide utilization locus):** Bacteroidota (n=2,581) were 36.1% gut/rumen versus 25.8%, 1.40×, p < 10⁻³⁵. [src: gene_function_ecological_agora]

The narrower soil prediction for Mycobacteriaceae failed. They were 12.9% soil versus 14.5% of the atlas, 0.88×, p 0.87. [src: gene_function_ecological_agora] Soil or host-pathogen combined gave 29.0% versus 16.4%, 1.76×, p < 10⁻¹¹. [src: gene_function_ecological_agora] The report attributes the failed soil result to a clinical-isolate skew among species representatives. [src: gene_function_ecological_agora] The MGnify breakdown shows 53 human-skin, 16 human-vaginal, 15 human-gut and 11 chicken-gut species. [src: gene_function_ecological_agora] The report treats this as a refinement of NB12: the signature is concentrated in host-pathogen-niche mycobacteria, not soil ones. [src: gene_function_ecological_agora]

As a sanity check, phylum-level biome distributions matched established ecology. Cyanobacteriota were 33.2% marine and 60.7% photic, and Bacteroidota 36.1% gut/rumen. [src: gene_function_ecological_agora]

## Phase 4 Deliverable P4-D1 — Phenotype/Ecology Grounding (v2.8, 2026-04-28): NB25 …

This part of the report grounds the atlas findings in biome, BacDive phenotype and AlphaEarth environmental-cluster data. The report states that phylum-level biome distributions match well-established ecology, and that phenotype anchors confirm the Mycobacteriaceae and Bacteroidota predictions. [src: gene_function_ecological_agora] Cyanobacteriia could not be anchored by phenotype because BacDive coverage is too thin. [src: gene_function_ecological_agora]

### Biome sanity check (NB23)

The report states that phylum-level biome distributions match well-established ecology. [src: gene_function_ecological_agora] Bacillota_A (Clostridia) were 81.0% gut/rumen. [src: gene_function_ecological_agora] Bacteroidota were 36.1% gut/rumen. [src: gene_function_ecological_agora] Verrucomicrobiota were 65.6% photic. [src: gene_function_ecological_agora] Planctomycetota were 38.7% marine. [src: gene_function_ecological_agora] Chloroflexota were 47.0% photic. [src: gene_function_ecological_agora]

### BacDive phenotype anchors (NB24)

NB24 tabulated metabolite-utilization, physiology and enzyme phenotypes for 6,066 P1B species representatives with BacDive matches (32%, via GCF→GCA fallback). [src: gene_function_ecological_agora] The report says the [[entities/mycobacteriaceae]] and [[entities/bacteroidota]] profiles match the expected biology of each clade. [src: gene_function_ecological_agora]

**Mycobacteriaceae (n=318 BacDive species).**
- Gram stain was positive 171 / negative 1, consistent with acid-fast Gram-positive Actinobacteriota. [src: gene_function_ecological_agora]
- Cells were rod-shaped in 194/216 records (95%). [src: gene_function_ecological_agora]
- Species were non-motile in 195/196 records (99%). [src: gene_function_ecological_agora]
- Oxygen tolerance was 89.4% aerobic-leaning: aerobe 40.9%, obligate aerobe 31.1% and microaerophile 17.4%. [src: gene_function_ecological_agora]
- Catalase EC (Enzyme Commission) 1.11.1.6 appeared in 317 instances, read as an aerobic marker. [src: gene_function_ecological_agora]
- The top compounds tested were nitrate (552), sucrose (351), maltose (279), urea (251) and glycogen (241), a typical mycobacterial growth-test panel. [src: gene_function_ecological_agora]

**Bacteroidota (n=577 BacDive species).**
- Gram stain was negative 339 / positive 4. [src: gene_function_ecological_agora]
- Rod-shaped records numbered 344. [src: gene_function_ecological_agora]
- 78% were non-motile. [src: gene_function_ecological_agora]
- 33.2% were anaerobes, against 22.0% atlas-wide (1.5× enriched). This holds despite a type-strain culture bias toward aerobes. Aerobes were 48.7%. [src: gene_function_ecological_agora]
- Maltose (230+), raffinose (155+) and esculin (228+) were utilized, as were cellobiose, glucose and lactose. The report calls this the polysaccharide-utilization signature predicted by PUL (polysaccharide utilization locus) biology. It calls it the strongest available BacDive anchor for the Phase 1B PUL Innovator-Exchange finding. [src: gene_function_ecological_agora]
- The top enzymes were leucyl-aminopeptidase (415), β-galactosidase (391), α-galactosidase (340), β-glucosidase (339) and β-N-acetylhexosaminidase (299). The report calls this a glycoside-hydrolase-rich profile consistent with PUL. [src: gene_function_ecological_agora]

**Limit.** Cyanobacteriia BacDive coverage was too thin (n=4 species), so phenotype anchoring was not feasible. [src: gene_function_ecological_agora] Their anchoring rests on biome association (p < 10⁻⁵²) and environmental-cluster concentration. [src: gene_function_ecological_agora]

### AlphaEarth environmental clusters (NB25)

NB25 used k-means to cluster 4,633 P1B species, using AlphaEarth 64-dim environmental embeddings, into k=10 environmental clusters. [src: gene_function_ecological_agora] Several clusters had clear environmental themes:

- Cluster 0 (n=818): marine, sponge tissue and hypoxic seawater. [src: gene_function_ecological_agora]
- Cluster 1 (n=812): chicken gut, human gut and activated sludge. [src: gene_function_ecological_agora]
- Cluster 3 (n=684): mouse gut, pig gut and groundwater. [src: gene_function_ecological_agora]
- Cluster 4 (n=328): sheep rumen, stool and rumen. [src: gene_function_ecological_agora]
- Cluster 6 (n=228): hypersaline soda lake sediment and Microcystis lake. [src: gene_function_ecological_agora]
- Cluster 9 (n=203): soil, temperate grassland, groundwater and meadow soil. [src: gene_function_ecological_agora]

Recent-gain density was highest in mixed-biome clusters 5 and 8 and lowest in the hypersaline/extremophile cluster 6. [src: gene_function_ecological_agora] The values below are mean recent-gain counts per species (KOs, KEGG orthologs), given as regulatory / metabolic / mixed:

- Cluster 5 (mouse-gut + marine + acid mine drainage): 3,178 / 10,891 / 6,418. [src: gene_function_ecological_agora]
- Cluster 8 (marine + human-gut + soil): 3,091 / 10,063 / 6,008. [src: gene_function_ecological_agora]
- Cluster 1 (gut + sludge): 2,652 / 8,081 / 5,780. [src: gene_function_ecological_agora]
- Cluster 3 (gut): 2,627 / 8,173 / 5,446. [src: gene_function_ecological_agora]
- Cluster 9 (soil + grassland): 1,303 / 5,314 / 3,087. [src: gene_function_ecological_agora]
- Cluster 6 (hypersaline + Microcystis): 490 / 1,475 / 1,100. [src: gene_function_ecological_agora]

The report reads this as consistent with literature that environmental generalists have higher HGT (horizontal gene transfer) rates than extremophile specialists. It also reads it as consistent with the atlas-wide dominance of Innovator-Exchange over Innovator-Isolated clades. [src: gene_function_ecological_agora] This is an interpretation, not a direct test.

Clade distributions across clusters:
- Cyanobacteriia (n_AE=90) had 35.6% in cluster 0 and 17.8% in clusters 5+8. This is heavily marine-leaning and matches NB16 expectations. [src: gene_function_ecological_agora]
- Mycobacteriaceae (n_AE=50) had 34.0% in cluster 1 and 20.0% in cluster 3. This is host-clustered and matches the NB12 host-pathogen anchor. [src: gene_function_ecological_agora]
- Bacteroidota (n_AE=729) were spread across clusters 0/1/3 (~18% each). The report reads this as a wide gut and marine niche range. [src: gene_function_ecological_agora]

### Overall conclusions

The report states that every confirmed pre-registered hypothesis (NB12, NB16, Phase 1B Bacteroidota PUL) is now anchored to the expected biome at p < 10⁻¹¹. It adds that phenotype anchors confirm the Mycobacteriaceae and Bacteroidota predictions. [src: gene_function_ecological_agora] The mycolic-acid Innovator-Isolated signature concentrates in host-pathogen mycobacteria, with 7.88× enrichment in host-pathogen biomes. [src: gene_function_ecological_agora] Soil enrichment for this signature is null. [src: gene_function_ecological_agora]

The report notes that the pangenome-internal environmental tables are richer than the v2.9 plan's external-substrate list suggested. `ncbi_env` has 4.1M EAV rows and `alphaearth_embeddings` has 64-dim quantitative geospatial data. [src: gene_function_ecological_agora] It recommends that future `kbase_ke_pangenome` projects use these tables before external NMDC/MGnify/BacDive queries. [src: gene_function_ecological_agora]

### Outputs

The outputs are listed as `data/p4d1_env_per_species.parquet` (18,992 rows × 97 cols), biome-enrichment tests and diagnostics, BacDive utilization, physiology and enzyme tables, and AlphaEarth cluster tables with diagnostics. [src: gene_function_ecological_agora]

## Phase 4 Deliverable P4-D2 — MGE Context per Gain Event (v2.9, 2026-04-29): Result 2: PSII …

This part of the report measures how often pre-registered atlas KEGG orthologs (KOs) travel on mobile genetic elements (MGEs). It uses two substrates: per-cluster MGE machinery, and MGE cargo within ±5kb in genome assemblies. [src: gene_function_ecological_agora] Per-cluster results are near zero for all three hypothesis KO sets. The neighborhood test ran only for photosystem II (PSII), where it sits at random baseline. The polysaccharide utilization locus (PUL) and mycolic-acid neighborhood scans did not run at scale. [src: gene_function_ecological_agora]

### Substrate and method

The catalog check found that genomad_mobile_elements is not ingested in the KBase Data Lakehouse. [src: gene_function_ecological_agora] The available signal is keyword matching on bakta_annotations.product (phage, transposase, integrase, plasmid, IS-element, recombinase, conjugation) across all 132M gene_clusters. [src: gene_function_ecological_agora] Scripts 26b and 26c flag MGE-context products per KO × genus atlas-wide, using Spark and MinIO staging. [src: gene_function_ecological_agora] The per-KO × genus MGE-machinery fraction is MGE-flagged clusters divided by KO-bearing clusters. It was tagged onto 7.95M M22 recent-gain events. [src: gene_function_ecological_agora]

For the cargo test, each focal gene instance pulls all CDS features ±5kb on the same contig from kbase_genomes.feature and contig_x_feature. Neighbors are mapped to gene clusters through kbase_genomes.name and gene_genecluster_junction, then flagged using Bakta products. [src: gene_function_ecological_agora]

### Per-cluster MGE machinery

Across the atlas, 1.37% of KO-bearing gene_clusters carry MGE-context products (248,908 of 18,204,007). [src: gene_function_ecological_agora] The three pre-registered hypothesis sets all sit near zero. The report reads this to mean these KOs are not themselves phage, transposase, integrase or plasmid genes. [src: gene_function_ecological_agora]

| Hypothesis set | Recent gains | Mean MGE-machinery fraction |
|---|---|---|
| Mycobacteriaceae × mycolic-acid | 6,683 | 0.57% [src: gene_function_ecological_agora] |
| Cyanobacteriia × PSII | 236 | 0.00% [src: gene_function_ecological_agora] |
| Bacteroidota × PUL | 1,023 | 0.00% [src: gene_function_ecological_agora] |

By KO category, regulatory KOs have a ~10× higher MGE-machinery rate (4.13%) than metabolic (0.37%) or mixed (0.27%) KOs. The report calls this consistent with regulatory products that include transposon-bound and phage-bound regulators. [src: gene_function_ecological_agora] Biome-stratified MGE rates were similar (~1.1–2.0%), with no strong biome-specific elevation. [src: gene_function_ecological_agora]

### PSII gene-neighborhood result

PSII shows no MGE-cargo enrichment. The analysis covered 27,148 focal features and 218,321 neighbor pairs. [src: gene_function_ecological_agora] The mean MGE-neighbor fraction was 1.65%, close to the atlas rate of 1.37%. [src: gene_function_ecological_agora] Of focal features, 10.91% had at least one MGE neighbor within ±5kb. [src: gene_function_ecological_agora] The report's Poisson baseline uses an atlas MGE rate p = 0.014 and about 8 neighbors. It predicts about 10.6%. [src: gene_function_ecological_agora] The report therefore finds no enrichment. [src: gene_function_ecological_agora] It also says this rules out PSII gains traveling as phage/MGE cargo. [src: gene_function_ecological_agora]

Individual subunits vary around that mean:

| KO | Subunit | Features | With MGE neighbor |
|---|---|---|---|
| K02720 | PsbZ | 1,769 | 22.1% [src: gene_function_ecological_agora] |
| K02718 | PsbX/M | 1,500 | 15.5% [src: gene_function_ecological_agora] |
| K02704 | PsbB (CP47) | 1,794 | 14.2% [src: gene_function_ecological_agora] |
| K02703 | PsbA (D1, RC) | 4,217 | 13.7% [src: gene_function_ecological_agora] |
| K02710 | PsbE (cyt b559α) | 1,188 | 12.6% [src: gene_function_ecological_agora] |
| K02716 | PsbV (cyt c550) | 1,386 | 3.5% [src: gene_function_ecological_agora] |

The report suggests that the 3.5% to 22.1% spread reflects differential mobility within the complex. It notes that the ensemble mean sits at random-baseline expectation. [src: gene_function_ecological_agora]

### Scale failures and the decision to ship

The Bacteroidota PUL scan failed. Even the two canonical SusC/SusD KOs gave 723K focal features × 210K contigs. The 1.3GB serialized Stage 5 result exceeded spark.driver.maxResultSize at toPandas. [src: gene_function_ecological_agora] The report notes that Bacteroidota has 2,581 species, 8.4× Cyanobacteriia's 309. [src: gene_function_ecological_agora] Sampling 309 random Bacteroidota species still gave 80K focal features × 21K contigs × ~105 features/contig. The Stage 6 pandas merge was ~24M rows × 9 cols and ran out of memory on the 9GB DataFrame. [src: gene_function_ecological_agora] The Mycobacteriaceae sampled run never started. [src: gene_function_ecological_agora] Scaling would need batched processing of ~10K focal features per chunk, or a full-Spark Stage 6 spatial filter. The report estimates ~1-2 days of extra engineering. [src: gene_function_ecological_agora]

The report shipped without these scans. It argues they would refine the picture but not change the headline. [src: gene_function_ecological_agora] That rests on per-cluster results plus the PSII neighborhood result. The PUL and mycolic neighborhood results are therefore untested. [src: gene_function_ecological_agora]

### Conclusion

The report concludes that pre-registered atlas KOs are not phage, transposase, integrase or plasmid cargo. [src: gene_function_ecological_agora] The support differs by case:

- PSII was verified directly at gene-neighborhood scale, with 10.91% MGE neighbors at random baseline. [src: gene_function_ecological_agora]
- Mycobacteriaceae × mycolic-acid had 0.57% MGE machinery, well below the atlas 1.37%. The report adds the literature consensus on chromosomal mycolic-acid operons (Marrakchi 2014). [src: gene_function_ecological_agora]
- Bacteroidota × PUL had 0% MGE machinery, with the PUL neighborhood scan deferred for scale. The report cites literature consensus on Integrative Conjugative Element (ICE)-mediated transfer (Sonnenburg 2010). [src: gene_function_ecological_agora]

The report reads the atlas as consistent with mycolic-acid, PSII and PUL genes moving by chromosomal recombination and ICEs, not phage-mediated transduction. [src: gene_function_ecological_agora] See [[concepts/mobile-genetic-element-context-of-horizontally-acquired-gene-families]] for the wider context.

## Phase 4 Deliverable P4-D2 — MGE Context per Gain Event (v2.9, 2026-04-29); Final …

This part of the report gives the MGE (mobile genetic element) outputs of deliverable P4-D2 and the final synthesis. The synthesis reports 2 of 4 pre-registered weak-prior hypotheses confirmed at acceptable effect sizes, and all atlas claims surviving annotation-density residualization. [src: gene_function_ecological_agora] The report's own tally also speaks of "all 3 confirmed hypotheses" being ecologically and phenotypically grounded. [src: gene_function_ecological_agora] The "2 of 4" count and the "3 confirmed" count are both stated in the report and are not reconciled there. The per-hypothesis table below lists H2 and H3 as supported, H1 as falsified and H4 as not reproduced. [src: gene_function_ecological_agora] The headline was reframed from regulatory-versus-metabolic asymmetry to clade-level innovation plus an acquisition-depth atlas anchored to ecology. [src: gene_function_ecological_agora]

### Hypothesis outcomes

| Hypothesis | Result | Effect size |
|---|---|---|
| H1: Bacteroidota Innovator-Exchange on PUL (polysaccharide utilization locus) CAZymes (carbohydrate-active enzymes) | Falsified at the deep-rank absolute-zero criterion. The UniRef50 NB08c Sankoff diagnostic recovered a small consumer-z signal. [src: gene_function_ecological_agora] | d=0.15 [src: gene_function_ecological_agora] |
| H2: Mycobacteriota Innovator-Isolated on mycolic-acid pathway | Supported at family and order ranks [src: gene_function_ecological_agora] | producer d=+0.31, consumer d=−0.19 (NB12) [src: gene_function_ecological_agora] |
| H3: Cyanobacteria Innovator-Exchange on PSII (photosystem II) | Supported at class rank. Genus rank was too sparse to evaluate. [src: gene_function_ecological_agora] | producer d=+1.50, consumer d=+0.70 (NB16) [src: gene_function_ecological_agora] |
| H4: Alm 2006 r ≈ 0.74 (TCS (two-component system) HK (histidine kinase) count vs LSE fraction) | Not reproduced at full GTDB scale [src: gene_function_ecological_agora] | r=0.10–0.29 across four framings (n=18,989) [src: gene_function_ecological_agora] |

For H4, NB17 architectural concordance was r=0.67 consumer-side. The Alm 2006 qualitative result therefore holds at architectural resolution, but its quantitative point estimate does not. [src: gene_function_ecological_agora]

As a bonus reframe, the NB11 hypothesis of a regulatory-versus-metabolic d ≥ 0.3 asymmetry was reframed at small effect size. The direction (consumer d=−0.21) supports the Jain 1999 complexity hypothesis. [src: gene_function_ecological_agora] The report cites Burch et al. 2023 (PMID:37232518, PubMed identifier) as independent empirical validation of this direction at Lactobacillaceae scale. [src: gene_function_ecological_agora] See [[concepts/complexity-hypothesis-regulatory-versus-metabolic-gene-transfer-asymmetry]].

### Ecology and phenotype grounding

The report argues the atlas findings are robust because they converge across three independent measurement substrates. [src: gene_function_ecological_agora] These are the atlas effect sizes (KO-level Sankoff parsimony scoring against a per-rank null model), ecology grounding (NB23 Fisher's enrichment of focal-clade species in expected biomes) and phenotype anchors. [src: gene_function_ecological_agora] The report says a finding at any single layer would be circumstantial. [src: gene_function_ecological_agora] See [[concepts/ecological-and-phenotypic-grounding-of-gene-flow-signatures]].

- Bacteroidota: NB23 found 1.40× enrichment in gut/rumen, p<10⁻³⁵. [src: gene_function_ecological_agora] NB24 found saccharolytic, glycoside-hydrolase-rich profiles in n=577 [src: gene_function_ecological_agora], with 1.5× anaerobe enrichment. [src: gene_function_ecological_agora]
- Mycobacteriaceae: NB23 found 7.88× enrichment in host-pathogen environments, p<10⁻⁴⁵. [src: gene_function_ecological_agora] NB24 found 89.4% aerobic-leaning, Gram-positive, non-motile, rod-shaped, catalase-positive profiles [src: gene_function_ecological_agora], with an aerobic-rod-catalase anchor in n=318. [src: gene_function_ecological_agora]
- Cyanobacteria: NB23 found Cyanobacteriia 2.77× enriched in photic aquatic environments, p<10⁻⁵². [src: gene_function_ecological_agora] NB25 found Cluster 0 marine+sponge dominant. [src: gene_function_ecological_agora] The BacDive phenotype anchor had only n=4 coverage, judged too thin. [src: gene_function_ecological_agora]

### MGE context

For Cyanobacteria PSII, NB26c found 0% MGE-machinery. The gene-neighborhood rate was 10.91%, equal to the Poisson baseline (NB26g), and the report says this is not phage-cargo per Cardona 2018. [src: gene_function_ecological_agora] See [[concepts/mobile-genetic-element-context-of-horizontally-acquired-gene-families]].

### Atlas structure

The atlas covers 18,989 P1B-qualified species representatives spanning the bacterial domain of GTDB r214, with 13.7M (rank × clade × KO) producer/participation scores. [src: gene_function_ecological_agora] It reports clade × function-class tuples at every rank from genus to phylum. [src: gene_function_ecological_agora] Its components are:

- Production rate is paralog expansion above the per-rank null, given as producer_z from the M5/M6 null framework. [src: gene_function_ecological_agora]
- The acquisition profile uses M22 Sankoff parsimony recipient-rank attribution of 17M gain events on the GTDB-r214 species tree, split into recent, older_recent, mid, older and ancient depths. [src: gene_function_ecological_agora]
- The Producer × Participation categories are Innovator-Isolated, Innovator-Exchange, Sink-Broker-Exchange and Stable. They are deep-rank and direction-agnostic, following M25's deferral of donor inference. [src: gene_function_ecological_agora]
- The MGE-machinery rate is the fraction of constituent gene clusters with phage, transposase, integrase, plasmid, IS-element or recombinase bakta products. The atlas baseline is 1.37%. [src: gene_function_ecological_agora]
- Biome assignment uses MGnify, ENVO (Environment Ontology) env_broad_scale and isolation_source, with 76.8–88.8% coverage. [src: gene_function_ecological_agora]

### Outputs and pipeline

- data/p4d2_ko_genus_mge.parquet holds 3.9M ko × genus rows. [src: gene_function_ecological_agora]
- data/p4d2_recent_gain_mge_attributed.parquet records MGE-machinery per recent gain. [src: gene_function_ecological_agora]
- data/p4d2_neighborhood_psii_per_feature.parquet holds 26,864 PSII focal-feature × MGE-neighbor records. [src: gene_function_ecological_agora]
- Diagnostics are in data/p4d2_diagnostics.json and data/p4d2_neighborhood_psii_diagnostics.json. [src: gene_function_ecological_agora]

The report presents the feature–contig cross-walk plus bakta product keyword matching as a reusable KBase Data Lakehouse pipeline for cargo-on-MGE measurement at gene-neighborhood scale. [src: gene_function_ecological_agora] See [[concepts/spark-query-scale-limits-and-notebook-session-constraints-in-lakehouse-analyses]].

### Caveats and scale limits

- BacDive phenotype anchors cover only 32% of atlas species. [src: gene_function_ecological_agora] AlphaEarth 64-dim satellite-imagery embeddings cover 27%. [src: gene_function_ecological_agora]
- Spark-Connect toPandas reaches its 1GB serialized driver result-size cap when joining 1B-row tables filtered to >200K elements. [src: gene_function_ecological_agora]
- Pandas spatial-range merges run out of memory at ~10M+ rows and need batching. [src: gene_function_ecological_agora]
- Beyond ~20K focal features × ~20K contigs, the report recommends full-Spark spatial filters that collect only per-feature aggregates to the driver, or batched MinIO-staged processing. [src: gene_function_ecological_agora]

## Final Synthesis — Project Conclusion (v3.0, 2026-04-29): Project deliverables tally

This part of the report lists what the project contributes as method, what it could not do, and how its review process worked. The main point is that the atlas is presented as methodologically sound, biologically interpretable and mechanism-informed, with stated limits on what it reproduces from Alm 2006 and on what could be run at scale. [src: gene_function_ecological_agora]

### Methodology contributions

The report names two constructions that handle deep ranks. The per-rank null model with the Producer × Participation framework (M5/M6) gives direction-agnostic per-clade categorization at deep ranks, where duplication transfer loss (DTL) reconciliation is not tractable. [src: gene_function_ecological_agora] [[entities/sankoff-parsimony|Sankoff parsimony]] with M22 recipient-rank gain attribution gives a tree-aware acquisition-depth signal at full GTDB scale. It replaces the parent-rank dispersion permutation null, which a diagnostic (NB08c) showed to be the wrong metric. [src: gene_function_ecological_agora]

The D2 annotation-density residualization (P4-D5) closes a pre-registration debt. It found producer_z bias-immune (R²=0.000). [src: gene_function_ecological_agora] It found a small consumer_z bias (R²=0.053) that did not change any verdict. [src: gene_function_ecological_agora] A pangenome-to-genome-context cross-walk was demonstrated for gene-neighborhood mobile-genetic-element (MGE) cargo analysis at GTDB scale. The demonstration used photosystem II (PSII). [src: gene_function_ecological_agora]

### What generalizes from Alm 2006

The qualitative two-component system (TCS) histidine kinase (HK) recent-skew generalizes from Alm 2006 at architectural resolution, with r=0.67 consumer-side concordance. [src: gene_function_ecological_agora] The quantitative r ≈ 0.74 point estimate did not survive scaling from 207 to 18,989 genomes. [src: gene_function_ecological_agora]

### Limits and deferrals

- Donor identification at deep ranks was deferred (M25). Per-CDS sequence is not in the KBase Data Lakehouse queryable schemas, and external FASTA plus codon profiling would break the Phase 3 budget. [src: gene_function_ecological_agora]
- Phase 3 reports the Innovator-Exchange joint label, which does not distinguish Broker from Open-donor. This is the level at which Alm 2006 made claims. [src: gene_function_ecological_agora]
- AleRax / ALE does not run at full GTDB scale. Four-quadrant labels exist only at genus rank for the Phase 3 candidate set (~10K KOs), not atlas-wide. [src: gene_function_ecological_agora] KO is KEGG ortholog.
- Polysaccharide utilization locus (PUL) and mycolic gene-neighborhood analysis at scale was deferred. Bacteroidota's 2,581 species (8× Cyanobacteriia) caused a pandas spatial-merge OOM. [src: gene_function_ecological_agora] The report holds that the per-cluster MGE-machinery result (0%/0.57%) suffices for the headline non-phage-borne conclusion. [src: gene_function_ecological_agora]
- P4-D1 used MGnify categorical biome labels (28% species coverage, 18 biome categories). It did not query per-sample taxa-coverage matrices, which the report names as a direction for finer-grained ecological inference. [src: gene_function_ecological_agora]

### Project discipline and review

The project documents 25 methodology revisions (M1–M25) in RESEARCH_PLAN.md, each with rationale and triggering observation. [src: gene_function_ecological_agora] Three pre-registration omissions were surfaced and corrected: M2 dosage biology, M12 absolute-zero criterion, and M14 misreading-of-Alm-2006. [src: gene_function_ecological_agora] The project integrated 7 adversarial reviews, from REVIEW_1 at plan stage through REVIEW_7 at Phase 3 closure. [src: gene_function_ecological_agora] Three reviewer-side fabrications were detected: Mendoza 2020 PMID-hijack (PMID is PubMed identifier) at REVIEW_5, Koech 2025 at REVIEW_7, and Burch 2023 PMID error at REVIEW_7. [src: gene_function_ecological_agora] A verify-before-acting protocol was established, and reviewer self-flagging of fabrications is now active. [src: gene_function_ecological_agora] New verified citations were used as biological or methodological context: Phillips 2012, Marrakchi 2014, Lawrence 1998, Jain 1999, Cardona 2018, Bansal 2012/2013, Burch 2023, Ślesak 2024 and Denise 2019. [src: gene_function_ecological_agora]

### Final-state assessment

The report calls the atlas biologically interpretable because 3 of 3 confirmed hypotheses are anchored in expected biomes and phenotypes. It calls it mechanism-informed because the pre-registered KOs are not phage-borne and the literature implicates ICEs and chromosomal recombination. [src: gene_function_ecological_agora]

### Deliverables

The project reports 28 notebooks and 6 helper / finalize scripts across Phases 1A through 4. [src: gene_function_ecological_agora] Notebooks 09–18 hold Phase 2/3 analyses and 19–26 hold Phase 4 deliverables. [src: gene_function_ecological_agora] Key data products:

| File | Contents |
|---|---|
| p1b_full_extract_local.parquet | 28M (species, UniRef50) presence rows [src: gene_function_ecological_agora] |
| p2_ko_atlas.parquet | 13.7M (rank × clade × KO) producer/participation scores [src: gene_function_ecological_agora] |
| p2_m22_gains_attributed.parquet | 17M Sankoff gain events with recipient-rank attribution [src: gene_function_ecological_agora] |
| p4d1_env_per_species.parquet | 18,992 species × 97 env attributes [src: gene_function_ecological_agora] |
| p4d2_ko_genus_mge.parquet | 3.9M (KO × genus) MGE-machinery fractions [src: gene_function_ecological_agora] |
| p4d2_neighborhood_psii_per_feature.parquet | 26,864 PSII gene-neighborhood MGE-cargo records [src: gene_function_ecological_agora] |
| p4d5_residualized_atlas.parquet | 13.7M atlas rows × raw + D2-residualized scores [src: gene_function_ecological_agora] |

## Phase 4 Adversarial Review 8 Response (v3.1, 2026-04-29): Addressed: C9 PSII …

This part of the report answers Adversarial Review 8, which raised 3 critical, 4 important and 2 suggested issues against the v3.0 Final Synthesis. [src: gene_function_ecological_agora] The response addresses two critical findings and one important finding directly. It reports the remainder as already addressed or out of scope. [src: gene_function_ecological_agora] The citation auto-verifier resolved 7/7 DOIs and found no reviewer fabrications this round. [src: gene_function_ecological_agora]

### PSII rank dependence (C9)

The report checked the reviewer's numbers against project data. The C9 figures at genus rank (n=2,350, d=0.08) are accurate. [src: gene_function_ecological_agora] The verdict changes with taxonomic rank, as the table shows. n is the number of PSII KOs (KEGG orthologs) present; d is the effect size.

| Rank | n PSII KOs | Producer d | Consumer d | Verdict |
|---|---|---|---|---|
| genus | 2,350 | +0.08 | −0.53 | STABLE [src: gene_function_ecological_agora] |
| family | 705 | +0.20 | −1.28 | STABLE [src: gene_function_ecological_agora] |
| order | 301 | +0.19 | −1.42 | STABLE [src: gene_function_ecological_agora] |
| class | 21 | +1.50 | +0.70 | INNOVATOR-EXCHANGE, the project's supported finding [src: gene_function_ecological_agora] |
| phylum | 21 | +1.60 | NaN (insufficient reference consumer data) | INNOVATOR-ISOLATED [src: gene_function_ecological_agora] |

The report reads the genus, family and order STABLE verdicts as biologically expected. Within Cyanobacteria, PSII is near-universal with deep ancestry. [src: gene_function_ecological_agora] It cites Cardona et al. 2019, who state that PSII evolution predates the diversification of Cyanobacteria. [src: gene_function_ecological_agora] It reads the d ≈ 0.08–0.20 producer signals at finer ranks as this expected near-uniformity, not ongoing innovation. [src: gene_function_ecological_agora] It calls class rank the appropriate resolution, because Cyanobacteriia as a class carries PSII innovation relative to the rest of the bacterial tree. [src: gene_function_ecological_agora]

The class-rank n=21 counts PSII KOs (K02703–K02727 minus a few absent from the atlas). Each KO is one observation against 554,280 class-rank KO × clade tuples. It does not count independent species. [src: gene_function_ecological_agora] PSII KOs sit higher in Cyanobacteriia's score distribution than reference KOs do in their own class distributions (d=1.50, p=2×10⁻⁵). [src: gene_function_ecological_agora]

The report treats the phylum-rank INNOVATOR-ISOLATED reversal as a substrate artifact, not a contradiction. Consumer data are too thin at phylum rank, so the verdict shifts solely for that reason. [src: gene_function_ecological_agora] The phylum producer signal (d=1.60) is consistent with the class signal (d=1.50). [src: gene_function_ecological_agora] The report keeps one caveat: PSII Innovator-Exchange is specifically a class-rank phenomenon. It is not a generic Cyanobacteria-wide horizontal gene transfer (HGT) signature at every rank. [src: gene_function_ecological_agora]

The class-level exchange claim rests on ecology and acquisition depth. Photic enrichment is 2.77× (p<10⁻⁵²). The ancient fraction is 2.05% versus 14.9% atlas-wide, which the report calls consistent with donor origin. [src: gene_function_ecological_agora]

### Sankoff parsimony versus modern DTL methods

The report concedes that its [[entities/sankoff-parsimony|Sankoff parsimony]] approximation has no principled benchmark against modern duplication-transfer-loss (DTL) reconciliation methods. [src: gene_function_ecological_agora] The reviewer cited two relevant papers.
- Liu et al. (2021) extends DTL to the DTLOR model. It handles gene origin from outside the sampled species tree and rearrangement of gene syntenic regions. [src: gene_function_ecological_agora]
- Kundu and Bansal (2018) document multiple optimal rootings in a large fraction of gene trees. They quantify which aspects of DTL reconciliation are conserved across rootings. [src: gene_function_ecological_agora]

The project's approximation lacks this rooting-uncertainty quantification. [src: gene_function_ecological_agora] The report admits the methodology is a generation behind the state of the art. [src: gene_function_ecological_agora]

It offers three mitigations.
- Sankoff parsimony is tractable at full GTDB scale (17M gain events on an 18,989-leaf tree), where exact DTL methods are not. [src: gene_function_ecological_agora]
- The Producer × Participation framework gives a complementary signal that needs no donor inference. [src: gene_function_ecological_agora]
- M22 acquisition-depth attribution gives recipient-and-when signal at scale without principled DTL reconciliation. [src: gene_function_ecological_agora]

Cross-validation against Liu 2021 DTLOR or Bansal 2012/2013 SPR-based DTL on a representative GTDB subset is out of scope. It would need external tools and per-family gene-tree estimation. [src: gene_function_ecological_agora]

### Multiple testing and methodology revisions

The report calls C8 partially valid. It says C8 conflates methodology-revision transparency with multiple-hypothesis testing. [src: gene_function_ecological_agora] It argues that most M-numbered revisions are pre-registration corrections, substrate audits, control additions or metric corrections, not alternative hypothesis tests. [src: gene_function_ecological_agora] Examples are M1 (AMR/CRISPR-Cas positive controls), M2 (a dosage-biology pre-registration omission), M12 (explicit absolute-zero criterion), M14 (Sankoff parsimony replacing parent-rank dispersion) and M21 (strict-class housekeeping). [src: gene_function_ecological_agora]

Only 4 pre-registered hypotheses are tested: Bacteroidota PUL, Mycobacteriota mycolic, Cyanobacteria PSII, and Alm 2006 r ≈ 0.74. [src: gene_function_ecological_agora] At Bonferroni α = 0.05 / 4 = 0.0125, the reported significant findings survive trivially. They are NB12 mycolic-acid p<10⁻⁶, NB16 PSII class p<10⁻⁵ and P4-D1 enrichments all p<10⁻¹¹. [src: gene_function_ecological_agora]

Three revisions were genuine post-hoc metric changes on collected data: M14 Sankoff, M21 strict-class housekeeping and M23 n_neg ≥ 20 minimum. Each followed a failed diagnostic test and was documented as such. [src: gene_function_ecological_agora] The p-values are not corrected for these changes. The report advises weighting findings by effect size, ecological grounding and phenotype-anchor convergence. [src: gene_function_ecological_agora]

### Mobile genetic elements, architecture and uncertainty

The gene-neighborhood mobile genetic element (MGE) cargo analysis cannot detect Integrative Conjugative Element (ICE)-mediated transfer for Bacteroidota PUL (polysaccharide utilization locus). [src: gene_function_ecological_agora] The report had already deferred the PUL gene-neighborhood scan because of scale, citing literature consensus on ICE-mediated transfer. [src: gene_function_ecological_agora] Bakta product-keyword matching finds MGE machinery genes. It does not find cargo genes without synteny analysis. [src: gene_function_ecological_agora]

Mixed-category KOs show a median of 46 architectures per KO, against 1 for PSII. [src: gene_function_ecological_agora] The report flags this as exploratory and not pre-registered. Structural validation against AlphaFold confidence scores or domain-shuffling literature is a valid future direction but out of scope. [src: gene_function_ecological_agora]

Cross-phase uncertainty is not propagated. This covers Phase 1 UniRef50→KO projection errors, Phase 2 Sankoff errors, Phase 3 architectural coverage gaps and Phase 4 residualization assumptions. No unified atlas confidence interval exists. [src: gene_function_ecological_agora] Monte Carlo error propagation would take about 1-2 weeks and is deferred. Readers should weight findings by convergence across atlas effect size, ecology grounding and phenotype anchor. [src: gene_function_ecological_agora]

Integration of PaperBLAST, AlphaFold and eggNOG is future work, because the project closes at atlas construction and interpretation, not experimental validation. [src: gene_function_ecological_agora] The project documents a Spark-Connect driver result-size cap (1GB serialized) and pandas spatial-merge out-of-memory thresholds in the P4-D2 caveat. [src: gene_function_ecological_agora]

## Phase 4 Adversarial Review 8 Response (v3.1, 2026-04-29); NB28 Final Synthesis — Outputs …

This part of the report covers the REVIEW_8 response and the NB28 atlas synthesis. It adds new literature anchors, the output datasets, the exploratory M26 tree-based donor inference, and a leaf_consistency analysis that the report treats as independent validation of its framework. [src: gene_function_ecological_agora]

### REVIEW_8 response and literature

The report rates REVIEW_8 its highest-quality adversarial round. It found zero fabrications, all citations resolved, all numerical claims were verified against project data, and 4 new verified citations were added. [src: gene_function_ecological_agora] The report calls the review's PSII rank-dependence critique substantively correct and acknowledges it explicitly. [src: gene_function_ecological_agora] Earlier rounds (REVIEW_4/5/7) had fabricated citations that the project's verify-before-acting protocol caught. That protocol is now obsolete for REVIEW_8 because the BERIL adversarial review tool's auto-verifier catches DOI failures programmatically. [src: gene_function_ecological_agora]

Two new citations bear on HGT (horizontal gene transfer) at different depths:
- Benzerara et al. (2026) report that the ccyA gene moved from Cyanobacteria to Gammaproteobacteria. The report treats this as direct evidence of recent Cyanobacteria-to-Gammaproteobacteria HGT, supporting Cyanobacteria as HGT donors at recent ranks. [src: gene_function_ecological_agora]
- Yu et al. (2025) find that vertical inheritance dominates alginate utilization locus evolution in Flagellimonas (Bacteroidota). This complicates a simple "PUL = HGT" framing. PUL is polysaccharide utilization locus. [src: gene_function_ecological_agora] The report's Bacteroidota PUL result was a falsification at the deep-rank absolute-zero criterion, recovered as a small consumer-z signal. The report says this is consistent with within-Bacteroidota PUL evolution being more vertical than horizontal at fine taxonomic resolution. [src: gene_function_ecological_agora]

### Cyanobacteriia × PSII rank dependence

The PSII (photosystem II) producer effect changes with rank. At genus rank it is d=0.08 (n=2,350, STABLE). At class rank it is d=1.50 (n=21, INNOVATOR-EXCHANGE). At phylum rank it is d=1.60 (n=21, INNOVATOR-ISOLATED). [src: gene_function_ecological_agora] The report frames PSII as a class-defining innovation following Cardona 2018. On that framing the class-rank verdict is biologically appropriate and the genus null is expected. [src: gene_function_ecological_agora] See [[concepts/clade-level-innovation-signals-and-their-rank-dependence]].

### NB28 synthesis outputs

The atlas synthesis produced 6 data deliverables and 7 figures. [src: gene_function_ecological_agora]

| File | Rows | Content |
|---|---|---|
| p4_pre_registered_verdicts.tsv | 5 hypotheses | H1 qualified pass; H2 SUPPORTED; H3 SUPPORTED at class; H4 NOT REPRODUCED; NB11 REFRAMED [src: gene_function_ecological_agora] |
| p4_deep_rank_pp_atlas.parquet | 13.74M | Innovator-Isolated 803K, Innovator-Exchange 50K, Sink-Broker-Exchange 742K, Stable 11.83M, Insufficient-Data 315K [src: gene_function_ecological_agora] |
| p4_genus_rank_quadrants_tree_proxy.tsv | 4.06M | Open-Innovator 2.38M, Broker 153K, Sink 182K, Closed-Stable / Insufficient 1.34M; confidence high 1.36M, medium 646K, low 711K [src: gene_function_ecological_agora] |
| p4_concordance_weighted_atlas.parquet | 8.64M | agree 169K, conflict 2.55M, insufficient 5.92M [src: gene_function_ecological_agora] |
| p4_conflict_analysis.tsv | 2.55M | per-tuple disagreements; most are the expected deep-stable plus genus-active relationship, with ~22K real rank-dependent conflicts [src: gene_function_ecological_agora] |
| p4_per_event_uncertainty.parquet | 17.07M | M22 gain events; n_leaves_under median 10, 75th pct 39; leaf_consistency coverage 97.8% [src: gene_function_ecological_agora] |

Mean leaf_consistency is 0.34 for recent gains and 0.20 for ancient gains. The report says this validates the M22 depth signal. [src: gene_function_ecological_agora] leaf_consistency is the fraction of species in the recipient clade carrying the KO (KEGG ortholog). [src: gene_function_ecological_agora]

### M26 tree-based donor inference (exploratory)

M26 is tree-based parsimony donor inference at genus rank. It is distinct from the deferred composition-based inference. [src: gene_function_ecological_agora] For a recent-rank gain of KO K into family F, candidate donors are the genera in F with K present, minus the recipient genus. [src: gene_function_ecological_agora] Each genus × KO tuple gets recipient gains, donor-candidate events (computed algebraically as R_FK − self_recipient) and a donor-recipient ratio. [src: gene_function_ecological_agora] Labels are Open-Innovator at ratio≥2, Broker at 0.5≤ratio<2, Sink at ratio<0.5, Closed-Stable when both counts are near zero, and Insufficient when total events are <5. [src: gene_function_ecological_agora]

| Group | Tuples | Open-Innovator | Broker | Sink | Insufficient |
|---|---|---|---|---|---|
| Mycobacteriaceae | 28,389 | 75.3% (21,365) | 13.0% (3,701) | 9.2% (2,619) | 2.5% (704) [src: gene_function_ecological_agora] |
| Cyanobacteriia | 54,582 | 47.9% (26,158) | 3.7% (1,999) | 4.4% (2,395) | 44.0% (24,030) [src: gene_function_ecological_agora] |
| Bacteroidota | 439,968 | 56.5% (248,581) | 4.5% (19,663) | 5.4% (23,612) | 33.7% (148,112) [src: gene_function_ecological_agora] |

The report reads Mycobacteriaceae as strongly Open-Innovator (75%), consistent with NB12 and the tree-proxy. It reads Cyanobacteriia and Bacteroidota as majority Open-Innovator with a Broker/Sink tail reflecting environment-driven flow. [src: gene_function_ecological_agora]

Two caveats limit these labels. The algebraic formula counts every KO-positive genus as a potential donor for all family-mates' gains, which biases toward Open-Innovator dominance. [src: gene_function_ecological_agora] Composition-based confirmation (M25, deferred) would be needed to separate empirically donor-like genera from merely parsimoniously donor-compatible ones, so the tree-proxy is reported as exploratory. [src: gene_function_ecological_agora]

### Function-class signatures

The report says convergence across independent measurement substrates supports robust verdicts. [src: gene_function_ecological_agora] The atlas centerpiece claim is that the recent-to-ancient gain ratio is itself a function-class signature. [src: gene_function_ecological_agora] CRISPR-Cas has a 24.5× ratio, read as HGT-active. Housekeeping classes sit near 1×, read as vertical inheritance dominant. [src: gene_function_ecological_agora] In the family-rank heatmap, Cyanobacteriota and Actinomycetota show elevated Innovator-* fractions for AMR (antimicrobial resistance) and CRISPR-Cas. Housekeeping classes show low Innovator-* fractions throughout. [src: gene_function_ecological_agora]

### Leaf-consistency signature plane

The report calls leaf_consistency its cleanest independent validation of the housekeeping-versus-HGT-active framework. No pre-registered hypothesis test used this axis. [src: gene_function_ecological_agora] See [[entities/leaf-consistency]].
- Strict housekeeping classes sit in the low-recent, high-LC (leaf consistency) vertical-inheritance quadrant: RNAP (RNA polymerase) core strict 0.97, tRNA-synth strict 0.94, ribosomal strict 0.92. [src: gene_function_ecological_agora]
- CRISPR-Cas (LC 0.29), AMR (0.11) and TCS HK (two-component system histidine kinase, 0.13) sit in the high-recent, low-LC HGT-active patchy quadrant. [src: gene_function_ecological_agora]
- Loose housekeeping classes fall in the middle, because their definitions include paralogs and weakly-housekeeping members. Strict housekeeping separates cleanly to vertical inheritance. [src: gene_function_ecological_agora]
- The ancient-patchy quadrant is sparse and holds only paralog-inflated loose-housekeeping classes. [src: gene_function_ecological_agora]

### Focal-clade leaf consistency

| Focal group | Focal n | Median LC | Atlas reference | Relative |
|---|---|---|---|---|
| Cyanobacteriia × PSII | 1,005 | 0.88 | 0.20 | 4.4× higher [src: gene_function_ecological_agora] |
| Bacteroidota × PUL | 6,070 | 0.41 | 0.20 | 2.0× higher [src: gene_function_ecological_agora] |
| Mycobacteriaceae × mycolic | 33,643 | 0.15 | 0.20 | 0.75× LOWER [src: gene_function_ecological_agora] |

PSII KOs occur in 88% of Cyanobacteriia species. The report reads this as a class-defining innovation, with the NB16 d=1.50 resting on a near-uniform population. [src: gene_function_ecological_agora] PUL KOs occur in 41% of Bacteroidota species, a phylum tendency with substantial within-phylum heterogeneity. [src: gene_function_ecological_agora]

Mycolic gains land in clades where the KO is present in only 15% of family members. The report concludes that mycolic-acid-positive species are a sub-clade within Mycobacteriaceae. [src: gene_function_ecological_agora] It says this fits established biology: mycolic-acid biosynthesis is not uniform across Mycobacteriaceae, and only a subset produces mycolates of the chain length characteristic of M. tuberculosis. [src: gene_function_ecological_agora] Deep-rank Producer × Participation aggregation obscured this heterogeneity, and leaf_consistency surfaces it. [src: gene_function_ecological_agora] See [[entities/mycobacteriaceae]].

This limits the NB12 result. The family-rank producer d=0.31 averages mycolic-positive sub-clades (M. tuberculosis, M. leprae and M. avium complexes) with mycolic-negative or atypical members. [src: gene_function_ecological_agora] The report narrows the supported claim to say that sub-clades of Mycobacteriaceae are mycolic-acid Innovator-Isolated. It treats the family-rank effect as a population-mixture average. [src: gene_function_ecological_agora] It also attributes the Mycobacteriaceae 7.88× host-pathogen biome enrichment (P4-D1 NB23) primarily to the mycolic-positive pathogenic sub-clades. [src: gene_function_ecological_agora]

## NB28 Final Synthesis — Outputs (v3.2, 2026-04-29); Phase 4 Adversarial Review 9 Response …

This part of the report covers the final leaf_consistency (LC) build, the deferred work it lists, and the response to Adversarial Review 9. The review response centres on a recomputation of the Mycobacteriaceae effect in a mycolic-positive sub-clade. [src: gene_function_ecological_agora]

### Leaf_consistency build and what it shows

NB28e computed leaf_consistency as species-with-KO divided by total species in each rank × clade × KO grouping. It merged the result to 16.7M gain events with 97.8% coverage. [src: gene_function_ecological_agora] The report calls the initial v3.2 deferral of this step a planning error. The full 28M-row species-level KO presence table had been on MinIO since Phase 2 NB10. [src: gene_function_ecological_agora] The build shows that this table supports per-(rank × clade × KO) prevalence in a ~36s vectorized merge. [src: gene_function_ecological_agora] See [[entities/leaf-consistency]] and [[entities/kbase-data-lakehouse]].

Median LC falls monotonically with gain depth: recent 0.34, older_recent 0.30, mid 0.26, older 0.23, ancient 0.20. The report reads this as validating M22. [src: gene_function_ecological_agora] Recent gains have a long right tail toward 1.0, while ancient gains compress toward 0. The report attributes this to diversification and loss. [src: gene_function_ecological_agora] The report therefore treats recent-gain attribution as cleaner. Ancient-gain signal is diluted by later within-clade losses. [src: gene_function_ecological_agora]

The substrate can separate near-fixed (high LC) from patchy (low LC) clade signals. It can also expose within-clade heterogeneity that deep-rank averaging hides. [src: gene_function_ecological_agora]

### Other synthesis components and deferred work

The synthesis adds an exploratory genus-rank donor inference layer (M26). It uses tree-based parsimony to give Open, Broker, Sink and Closed labels. This replaces the deferred composition-based approach. [src: gene_function_ecological_agora] It also adds a concordance and conflict analysis of cross-rank consistency for the candidate set. [src: gene_function_ecological_agora] A pre-registered verdict TSV is supplied as a formal artifact. [src: gene_function_ecological_agora]

Three items stay out of scope:
- Bootstrap per-event uncertainty (~50 hr compute) was deferred. n_leaves_under shipped as the primary proxy. [src: gene_function_ecological_agora]
- DTL (duplication transfer loss) reconciliation cross-validation (Liu 2021 DTLOR / Bansal 2013) is out of scope. REVIEW_8 I9 acknowledged this, and the report calls it an honest reportable limit. [src: gene_function_ecological_agora]
- Composition-based donor inference (M25) was deferred because per-CDS sequence is not in the queryable schemas of the KBase Data Lakehouse. [src: gene_function_ecological_agora]

### Adversarial Review 9

ADVERSARIAL_REVIEW_9.md raised 3 critical, 4 important and 2 suggested issues against the v3.4 synthesis-complete state. [src: gene_function_ecological_agora] The citation auto-verifier resolved 8/8 DOIs. All 4 contradictory-evidence papers proved real. One carryover author-list error, the Burch 2023 Dykhuizen DE attribution, was corrected from the project's references list. [src: gene_function_ecological_agora]

### Mycolic sub-clade recomputation (NB29)

The review correctly noted that Cohen's d had never been recomputed on the mycolic-positive sub-clade alone. NB29 does this. [src: gene_function_ecological_agora] The S7 LC analysis had already suggested heterogeneity. Within Mycobacteriaceae LC was 0.15, below the atlas reference of 0.20. This suggested the family-rank d=0.31 was a population-mixture average. [src: gene_function_ecological_agora] See [[entities/mycobacteriaceae]] and [[concepts/clade-level-innovation-signals-and-their-rank-dependence]].

- Family-rank Mycobacteriaceae (original NB12): 13 genera, producer d +0.309, consumer d −0.193. [src: gene_function_ecological_agora]
- All genera (genus rank, no LC filter): 13 genera, producer d +0.326, consumer d +0.020. [src: gene_function_ecological_agora]
- Mycolic-positive (LC ≥ 0.5): 10 genera, producer d +0.394, consumer d +0.006. [src: gene_function_ecological_agora]
- Mycolic-low (LC < 0.5): 3 genera, producer d +0.211, consumer d +0.043. [src: gene_function_ecological_agora]

The mycolic-positive group is Williamsia, Smaragdicoccus, Lawsonella, Hoyosella, Tomitella, Tsukamurella, Dietzia, Gordonia, Nocardia and Williamsia_A. The report describes all of them as known mycolate-producing Mycobacteriales/Corynebacteriales genera. [src: gene_function_ecological_agora] The mycolic-low group is g__Mycobacterium, g__Corynebacterium and g__Rhodococcus. [src: gene_function_ecological_agora] The report calls it surprising that g__Mycobacterium sits in the mycolic-low group, with mean LC=0.36 and median 0.08. [src: gene_function_ecological_agora] Its explanation is that the 11-KO mycolic panel is calibrated to long-chain Mycobacterium-style mycolate biosynthesis. Only the M. tuberculosis complex carries all panel KOs at high prevalence, and many environmental Mycobacterium species do not. [src: gene_function_ecological_agora] The mycolic-positive group is the broader set of lineages that uniformly carry the panel. [src: gene_function_ecological_agora]

The report draws four conclusions:
- The producer effect is modestly amplified in the mycolic-positive sub-clade (d=0.39 versus family-rank d=0.31). Within-clade heterogeneity does not dramatically dilute the original finding. [src: gene_function_ecological_agora]
- The consumer signal vanishes at genus rank (d=+0.006 versus d=−0.193 at family rank). The report attributes the original effect to family-rank aggregation, not to a sub-clade-specific signal. [src: gene_function_ecological_agora] The consumer-side Innovator-Isolated component is therefore weaker than the family-rank framing implied. [src: gene_function_ecological_agora]
- The supported claim is refined. The mycolate-producing sub-clade (10 of 13 genera) is mycolic-acid Innovator-Isolated, with producer d=0.39 at genus rank. [src: gene_function_ecological_agora]
- The original NB12 family-rank finding holds but is sharpened. The producer-side signature is robust, and the consumer-side complementary signal is rank-dependent. [src: gene_function_ecological_agora]

Outputs are p4_review9_mycolic_subclade_d.tsv, p4_review9_mycolic_genus_lc.tsv and p4_review9_mycolic_subclade_diagnostics.json. [src: gene_function_ecological_agora]

### Literature integrated in response

- Williams et al. 2024 (DOI 10.1093/ismejo/wrae129, PMID 39001714) is a modern phylogenetic reconciliation review. [src: gene_function_ecological_agora] It qualifies the report's "DTL doesn't scale to GTDB" framing. Principled DTL methods are scaling, but not yet to the full 18,989-leaf tree. [src: gene_function_ecological_agora]
- López Sánchez et al. 2026 (DOI 10.1177/15578666261426009, PMID 41955011) presents a directly parallel Sankoff-Rousseau algorithm for HGT (horizontal gene transfer) inference using KEGG functions on bacterial species. [src: gene_function_ecological_agora] The report calls M22 conceptually similar. It proposes benchmarking M22 outputs against that algorithm on a shared substrate. [src: gene_function_ecological_agora] See [[entities/sankoff-parsimony]].
- Gisriel et al. 2023 (DOI 10.3389/fpls.2023.1289199, PMID 38053766) reports within-Cyanobacteria HGT of FaRLiP photosystem I variants. [src: gene_function_ecological_agora] The report says this qualifies but does not contradict the Cardona 2018 PSII (photosystem II) donor-origin framing used for NB16. That claim holds for PSII core machinery. The PSI FaRLiP variants are a separate niche-specific subset. [src: gene_function_ecological_agora]

### Pre-registered versus exploratory results

The report separates pre-registered tests from exploratory work. Pre-registered tests have specific Cohen's d thresholds and RESEARCH_PLAN falsification criteria. Exploratory observations and synthesis findings are descriptive patterns surfaced during the synthesis pass. The report says the two should not be conflated. [src: gene_function_ecological_agora] See [[concepts/adversarial-review-pre-registration-and-multiple-testing-discipline]].

## Phase 4 Adversarial Review 9 Response (v3.5, 2026-04-29): Reported (out-of-scope …

This part of the report answers the ninth adversarial review. It reframes ecological claims as association, treats leaf_consistency as a descriptive statistic, and lists the open limits that remain. It also records how citation quality changed across review rounds 4 to 9. [src: gene_function_ecological_agora]

### Ecology framing: association, not causation

The biome enrichments show statistical association between focal clades and expected biomes. They do not establish causal mechanisms. The enrichments are Mycobacteriaceae 7.88× in host-pathogen, Cyanobacteriia 2.77× in photic aquatic and Bacteroidota 1.40× in gut/rumen (P4-D1 NB23). [src: gene_function_ecological_agora] The report therefore changes "ecology grounding" to "ecology consistency" or "ecology anchoring", and "grounded in" to "consistent with" the expected biome. [src: gene_function_ecological_agora] The atlas, ecology and phenotype convergence framework gives convergent evidence from three independent measurement substrates, but it does not establish causation. [src: gene_function_ecological_agora] See [[concepts/ecological-and-phenotypic-grounding-of-gene-flow-signatures]].

### leaf_consistency and uncertainty

The report treats leaf_consistency as a descriptive statistic. It is a per-event uncertainty proxy and a within-clade-structure characterization, not a hypothesis test. [src: gene_function_ecological_agora] Using it as a test statistic in future work would need multiple-testing correction. The current synthesis does not test it against null distributions. [src: gene_function_ecological_agora] Across n=16.7M gain events, per-depth_bin medians range from 0.05 (ancient) to 0.26 (recent). [src: gene_function_ecological_agora] Bootstrap-based per-event uncertainty remains future work. [src: gene_function_ecological_agora] The bootstrap confidence interval (CI) on the M22 attribution is deferred because it needs about 50 hours of compute. [src: gene_function_ecological_agora] See [[entities/leaf-consistency]].

### Multiple testing and pre-registration

The report states that its methodology revisions are pre-registration corrections, not 25 alternative tests. It has only 4 pre-registered hypotheses, so the Bonferroni α is 0.0125. [src: gene_function_ecological_agora] It states that the significant findings survive trivially: NB12 p<10⁻⁶, NB16 p<10⁻⁵ and P4-D1 p<10⁻¹¹. [src: gene_function_ecological_agora] Only M14, M21 and M23 are genuine post-hoc metric changes. [src: gene_function_ecological_agora] See [[concepts/adversarial-review-pre-registration-and-multiple-testing-discipline]].

### Framing responses

- The photosystem II (PSII) null at genus rank is framed as expected, because PSII is a class-defining innovation according to Cardona 2018. [src: gene_function_ecological_agora]
- The report positions its parsimony approximation against the duplication transfer loss (DTL) reconciliation literature: Williams 2024, López Sánchez 2026, Liu 2021, Kundu 2018 and Bansal 2012. [src: gene_function_ecological_agora]
- It frames its intellectual lineage as methodology generalization of Alm 2006, not point-estimate reproduction. The atlas-as-flow-and-acquisition-map is the alternative framework. [src: gene_function_ecological_agora]
- The README reproduction section documents 5 computational caveats: Spark-Connect driver result-size cap, pandas spatial-merge out-of-memory failures, the autoBroadcast harmful default, JupyterHub idle-timeout and the driver heap ceiling. [src: gene_function_ecological_agora] See [[concepts/spark-query-scale-limits-and-notebook-session-constraints-in-lakehouse-analyses]].

### Remaining limits

REVIEW_9 carries forward 15 still-open items consolidated from REVIEW_1 through REVIEW_8. [src: gene_function_ecological_agora] The report names these genuine open items:

- Sample-size effect inflation, especially PSII n=21. [src: gene_function_ecological_agora]
- Phylogenetic non-independence, because phylogenetic independent contrasts (PIC) correction is not implemented. [src: gene_function_ecological_agora]
- Cross-phase error propagation, which is unquantified. [src: gene_function_ecological_agora]
- Two-component system (TCS) architectural concordance, which is mixed. [src: gene_function_ecological_agora]

The M26 donor inference is exploratory. Validating it against documented horizontal gene transfer (HGT) cases would strengthen it but is outside the current synthesis scope. The cases named are the Cyanobacteria to plastid PSII transfer, antimicrobial resistance (AMR) plasmid transfers and ICE-mediated polysaccharide utilization locus (PUL) transfers (Sonnenburg 2010). [src: gene_function_ecological_agora]

### Review-round citation quality

The table gives severity and citations for each review round from 4 to 9. [src: gene_function_ecological_agora]

| Round | Severity | Citations | Note |
|---|---|---|---|
| 4 | 5 | 0 | Mendoza 2020 fabricated (PMID hijack) [src: gene_function_ecological_agora] |
| 5 | 5 | 0 | Continued fabrication patterns [src: gene_function_ecological_agora] |
| 6 | 4 | 2 (Lawrence 1998, Jain 1999) | First clean citations [src: gene_function_ecological_agora] |
| 7 | 6 | 4 (Burch, Bansal, Ślesak, Denise) + 1 fabrication (Koech) + 1 PMID error | Higher quality; introduced self-flagging [src: gene_function_ecological_agora] |
| 8 | 9 | 7 (Liu, Kundu, Marrakchi, Cardona, Burch, Benzerara, Yu) | 0 fabrications, 7/7 DOI auto-verified [src: gene_function_ecological_agora] |

The report gives the round 9 count as 8 and does not state how it relates to the 7 citations of round 8. [src: gene_function_ecological_agora] REVIEW_9 contributed 3 useful citations (Williams 2024, López Sánchez 2026, Gisriel 2023). It also contributed the I10 mycolic sub-clade prompt, which produced a refined-effect-size finding. [src: gene_function_ecological_agora] The auto-verifier catches DOI fabrications, but author-list hallucinations need manual metadata verification. [src: gene_function_ecological_agora]

## Multiple-testing correction pass (v3.6, 2026-04-29); Phase 1A pilot diagnostic figures

This part of the report applies family-wise multiple-testing correction to the project's formal significance claims, then lists Phase 1A pilot diagnostic figures. Of 16 formal tests, 14 survive Bonferroni correction, and the 2 that fail were already reported as nulls. [src: gene_function_ecological_agora] The report also argues that descriptive layers need no correction. [src: gene_function_ecological_agora] See [[concepts/adversarial-review-pre-registration-and-multiple-testing-discipline]] for the wider discipline.

### Correction design (NB30)

NB30 enumerates the formally tested significance claims, groups them into test families, applies family-wise Bonferroni and Benjamini-Hochberg false discovery rate (FDR) correction, and reports survival. [src: gene_function_ecological_agora] The report names the 4 pre-registered hypotheses H1–H4 as the actual hypothesis-test family. Biome enrichment and residualization replication are supporting families. [src: gene_function_ecological_agora] Outputs are data/p4_multiple_testing_correction.json, data/p4_multiple_testing_correction_summary.tsv and notebooks/30_multiple_testing_correction.py. [src: gene_function_ecological_agora]

| Family | Tests | Survive Bonferroni |
|---|---|---|
| 1: Pre-registered hypotheses | 4 | 4 (100%) [src: gene_function_ecological_agora] |
| 2: P4-D1 biome enrichment | 6 | 5 (83%) [src: gene_function_ecological_agora] |
| 3: P4-D5 residualization replication | 6 | 5 (83%) [src: gene_function_ecological_agora] |
| Total formal tests | 16 | 14 (88%) [src: gene_function_ecological_agora] |

### Pre-registered hypotheses

All 4 pre-registered tests survive family-wise correction and keep their verdicts. [src: gene_function_ecological_agora]
- H1, Bacteroidota PUL (polysaccharide utilization locus) Innovator-Exchange: raw p=1×10⁻³, survives, qualified pass. [src: gene_function_ecological_agora]
- H2, Mycobacteriota mycolic Innovator-Isolated (family): raw p=1×10⁻⁶, survives, supported. [src: gene_function_ecological_agora]
- H3, Cyanobacteria PSII (photosystem II) Innovator-Exchange (class): raw p=2.1×10⁻⁵, survives, supported. [src: gene_function_ecological_agora]
- H4, Alm 2006 r ≈ 0.74 reproduction: raw p=1×10⁻⁴³ and survives, but it is not reproduced. The observed r=0.10–0.29 is too small, and the significance reflects large n. [src: gene_function_ecological_agora]

### Biome enrichment (P4-D1)

5 of 6 tests survive. The one failure is the Mycobacteriaceae soil null, which the project already reported as "0.88× — NOT enriched", so it is not a false positive. [src: gene_function_ecological_agora] See [[entities/mycobacteriaceae]] and [[entities/bacteroidota]].
- Cyanobacteriia × marine: raw p=8.3×10⁻¹⁹, survives. [src: gene_function_ecological_agora]
- Cyanobacteriia × photic aquatic: raw p=1.5×10⁻⁵³, survives. [src: gene_function_ecological_agora]
- Mycobacteriaceae × soil: raw p=0.87, fails, 0.88× fold. [src: gene_function_ecological_agora]
- Mycobacteriaceae × host-pathogen: raw p=3.6×10⁻⁴⁶, survives. [src: gene_function_ecological_agora]
- Mycobacteriaceae × (soil OR host-pathogen): raw p=8.0×10⁻¹², survives. [src: gene_function_ecological_agora]
- Bacteroidota × gut/rumen: raw p=3.6×10⁻³⁶, survives. [src: gene_function_ecological_agora]

### Residualization replication (P4-D5)

This family has 6 tests with Bonferroni α=0.00833. [src: gene_function_ecological_agora] 5 of 6 survive. The failure is the NB11 regulatory-versus-metabolic null. The project had reframed it in the small-effect complexity-hypothesis direction, so it is not a false positive. [src: gene_function_ecological_agora] See [[concepts/complexity-hypothesis-regulatory-versus-metabolic-gene-transfer-asymmetry]].

| Test | d_residualized | p_residualized | Survives |
|---|---|---|---|
| NB11 producer_z reg vs metabolic | +0.06 | 0.69 | No; original H1 d≥0.3 stays falsified and reframed [src: gene_function_ecological_agora] |
| NB12 Mycobacteriaceae × mycolic family producer_z | +0.31 | 2×10⁻⁶ | Yes [src: gene_function_ecological_agora] |
| NB12 Mycobacteriaceae × mycolic family consumer_z | −0.16 | 1.6×10⁻⁵ | Yes [src: gene_function_ecological_agora] |
| NB12 Mycobacteriales × mycolic order producer_z | +0.29 | 5×10⁻⁶ | Yes [src: gene_function_ecological_agora] |
| NB16 Cyanobacteriia × PSII producer_z (class rank) | +1.50 | 2.1×10⁻⁵ | Yes [src: gene_function_ecological_agora] |
| NB16 Cyanobacteriia × PSII consumer_z (class rank) | +0.63 | 2.3×10⁻⁵ | Yes [src: gene_function_ecological_agora] |

### Analyses outside the correction

The report rejects a reviewer's suggestion to treat M1–M26 as 26 independent hypothesis tests on the same data. [src: gene_function_ecological_agora] Most M-numbers are pre-registration corrections, documented for transparency rather than as alternative hypothesis tests. [src: gene_function_ecological_agora] Three are post-hoc metric corrections on already-collected data: M14 Sankoff replaces parent-rank dispersion, M21 strict-housekeeping, and M23 n_neg ≥ 20. Each was triggered by a failed diagnostic and reported with it. [src: gene_function_ecological_agora] See [[entities/sankoff-parsimony]].

Two descriptive layers receive no correction:
- leaf_consistency is the fraction of clade species carrying a KO (KEGG ortholog), per rank × clade × KO. [src: gene_function_ecological_agora] The report treats it as a descriptive point estimate, not a tested significance claim. Medians (mycolic 0.15, PSII 0.88, PUL 0.41) are observations, not p-values. [src: gene_function_ecological_agora] See [[entities/leaf-consistency]].
- M26 tree-based donor inference assigns each genus × KO to Open, Broker, Sink or Closed using parsimony rules and a minimum event count of ≥5. [src: gene_function_ecological_agora] The report calls it descriptive classification, not a null-hypothesis test, and reports it as an exploratory layer under plan v2.16. [src: gene_function_ecological_agora]

### Phase 1A pilot: producer and consumer nulls

The producer null uses neutral-family UniRef50 paralog-count means and standard deviations for each rank × prevalence_bin cohort. [src: gene_function_ecological_agora] All bins have ≥30 cohort members at all 5 ranks. The report reads this as showing that producer-z scoring against the null is statistically tractable. [src: gene_function_ecological_agora]

The consumer null permutes UniRef50 prevalence patterns, and the consumer score is z-versus-permutation. [src: gene_function_ecological_agora] The null is unimodal per rank, with distinct shapes across ranks. The report reads this as showing that consumer-z is comparable across ranks. [src: gene_function_ecological_agora] This single-rank version was later superseded by the NB08c Sankoff parsimony diagnostic (M14), which uses tree-aware reconciliation. The pilot is kept for provenance. [src: gene_function_ecological_agora]

### Phase 1A pilot: paralog counts by control class

The pilot used boxplots of paralog count per UniRef50 within each control class, on 1K species × 1.2K UniRef50s. [src: gene_function_ecological_agora] Natural_expansion showed the wide distribution expected of paralog-rich families. [src: gene_function_ecological_agora] Positive controls (AMR, antimicrobial resistance, and CRISPR-Cas) showed modest paralog inflation. [src: gene_function_ecological_agora] Negative controls clustered tightly at 1 paralog, consistent with single-copy housekeeping. [src: gene_function_ecological_agora] See [[concepts/paralog-expansion-and-gene-copy-number-constraint]].

## Caveats and Open Work

- Donor identification at deep ranks was deferred. Per-CDS sequence is not in the KBase Data Lakehouse queryable schemas, and composition-based donor inference would need external FASTA plus codon profiling, which the report says breaks the Phase 3 budget. [src: gene_function_ecological_agora]
- AleRax / ALE does not run at full GTDB scale. Four-quadrant labels exist only at genus rank for the Phase 3 candidate set (~10K KOs), not atlas-wide. [src: gene_function_ecological_agora]
- The cross-walk was demonstrated on PSII. PUL and mycolic analyses were deferred at scale because of a pandas spatial-merge out-of-memory failure. [src: gene_function_ecological_agora]
- Three pre-registration omissions were corrected: M2 dosage biology, M12 absolute-zero criterion and M14 misreading of Alm 2006. [src: gene_function_ecological_agora] Three reviewer-side fabrications were detected: Mendoza 2020 and Koech 2025 and a Burch 2023 PMID error. [src: gene_function_ecological_agora]
- The Cyanobacteria PSII genus-rank test was too sparse to evaluate. [src: gene_function_ecological_agora] The UniRef50 unit cannot aggregate to the HK family. [src: gene_function_ecological_agora]

## Slots Into

- [[concepts/paralog-expansion-and-gene-copy-number-constraint]]: producer z rises with rank for natural_expansion controls [src: gene_function_ecological_agora], and dosage-constrained genes score negative. [src: gene_function_ecological_agora]
- [[concepts/horizontal-gene-transfer-inference-metrics-and-control-class-calibration]]: the NB08b and NB08c diagnostics and the control revisions bear on how well each metric separates classes. [src: gene_function_ecological_agora]
- [[concepts/complexity-hypothesis-regulatory-versus-metabolic-gene-transfer-asymmetry]]: TCS HK clusters scored negative on producer z, and the Alm 2006 correlation was not reproduced. [src: gene_function_ecological_agora]
- [[concepts/ecological-and-phenotypic-grounding-of-gene-flow-signatures]]: the biome enrichments and the substrate coverage audit. [src: gene_function_ecological_agora]
- [[concepts/annotation-coverage-and-annotation-density-bias-in-functional-enrichment]]: residualization showed producer_z is bias-immune. [src: gene_function_ecological_agora]
- [[concepts/adversarial-review-pre-registration-and-multiple-testing-discipline]]: the pre-registration omissions and reviewer fabrications. [src: gene_function_ecological_agora]
- [[concepts/mobile-genetic-element-context-of-horizontally-acquired-gene-families]]: the PUL/mycolic MGE-machinery result. [src: gene_function_ecological_agora]
