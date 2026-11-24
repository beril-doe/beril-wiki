---
type: "Summary"
description: "Summary of the project NEON Metagenome Lineage Novelty and Functional Ecology."
doc_type: "short"
full_text: "sources/neon_mag_functional_discovery__REPORT.md"
---
# NEON Metagenome Lineage Novelty and Functional Ecology

This page summarizes the NEON Metagenome Lineage Novelty and Functional Ecology project. Its main results are a habitat partition of functional gene content (PERMANOVA pseudo-F = 137, p = 0.001) [src: neon_mag_functional_discovery] and a median of 343 field-only KOs (KEGG orthologs) per MAG (metagenome-assembled genome), with every MAG carrying at least 10. [src: neon_mag_functional_discovery] Soil lineage novelty is higher at higher pH. [src: neon_mag_functional_discovery] The report favors a GTDB coverage gap over true novelty as the explanation. [src: neon_mag_functional_discovery] The per-MAG analysis rests on a reduced cohort. [src: neon_mag_functional_discovery]

## Key Findings

### Cohort

The analysis draws on three NMDC-rehosted NEON studies: soil nmdc:sty-11-34xj1150 (n=6,489), surface water nmdc:sty-11-hht5sb92 (n=234) and benthic sediment nmdc:sty-11-pzmd0x14 (n=736). [src: neon_mag_functional_discovery] Together they contain 7,298 MAGs, of which 1,609 pass MQ+HQ quality. [src: neon_mag_functional_discovery]

### Lineage novelty rises with soil pH

Among soil MQ+HQ MAG records, the novel fraction (no GTDB genus call) rises with pH. It is 7.6% below pH 4.5 (396 records) [src: neon_mag_functional_discovery], 16.2% at pH 4.5–5.5 (678 records) [src: neon_mag_functional_discovery] and 37.0% above pH 6.5 (1,107 records). [src: neon_mag_functional_discovery] The spread is 29.4 percentage points across 3.23 ≤ pH ≤ 9.13. [src: neon_mag_functional_discovery] Kendall τ on the bin midpoints is 1.0 but p = 0.083, which reflects a small-N power floor of 2/4!. [src: neon_mag_functional_discovery]

This direction is opposite the literature prior that acidic and peat-bog soils hold the most novel lineages. [src: neon_mag_functional_discovery] The report proposes that alkaline and neutral soils are comparatively under-cultured, so novel lineages there are less likely to match a GTDB species. [src: neon_mag_functional_discovery] Without an independent 16S ground truth, the result fits either true novelty or a GTDB coverage gap. The report favors the coverage gap. [src: neon_mag_functional_discovery]

### Habitat structures functional gene content

Functional gene content partitions by habitat (PERMANOVA, permutational multivariate analysis of variance). The pseudo-F is 137 and p = 0.001, across soil n=1,800, benthic n=618 and water n=88 workflows. [src: neon_mag_functional_discovery] The test used Aitchison-distance PCoA (principal coordinates analysis) on 2,506 workflows and 9,584 prevalence-filtered KOs. [src: neon_mag_functional_discovery]

At BH-FDR (Benjamini-Hochberg false discovery rate) < 0.05, soil has 3 enriched KEGG modules and benthic has 23. [src: neon_mag_functional_discovery] The enrichment list is dominated by housekeeping modules such as ribosome, RNA polymerase, cytochrome c oxidase and ATPase. [src: neon_mag_functional_discovery] The report cautions that such enrichment usually reflects a taxonomic-abundance shift, not a new capability. [src: neon_mag_functional_discovery]

In soil, horizon (O/M) explains 2.2% of variance (pseudo-F = 40.5, p = 0.001) and fails the 5% effect-size threshold. The report states that only pH clears it. [src: neon_mag_functional_discovery]

### Field-only accessory content

The first H4 test used a community-level KO union as a proxy for per-MAG accessory content. For each shared genus it took KOs present in ≥ 50% of NEON workflows where the genus has a MAG, and contrasted them with the cultured pangenome accessory. [src: neon_mag_functional_discovery] This proxy was uninformative. Pooled NEON-only KOs covered 9,547 / 9,584 (99.6%) of the universe [src: neon_mag_functional_discovery], and no KEGG modules were enriched at FDR < 0.05. [src: neon_mag_functional_discovery] The proxy was dominated by KOs from co-occurring taxa, as the plan's own caveat had warned. [src: neon_mag_functional_discovery]

The per-MAG re-analysis (H4b) used a path to per-MAG KO content through contig IDs. [src: neon_mag_functional_discovery] It found a median MAG KO set size of 1,113 [src: neon_mag_functional_discovery] and a median of 343 field-only KOs per MAG. [src: neon_mag_functional_discovery] All MAGs had at least 10 field-only KOs. [src: neon_mag_functional_discovery] In pooled recurrent field-only KOs, 29 KEGG modules were enriched at FDR < 0.05. [src: neon_mag_functional_discovery]

Cyanobacterial (Planktothrix, Dolichospermum) and uncultured peat-soil (Palsa-465, Palsa-295, Sulfotelmatobacter) MAGs carry hundreds of accessory KOs absent from any cultured representative of their genus. [src: neon_mag_functional_discovery] Per-genus medians (MAG-KO count, field-only KOs, Jaccard similarity to the genus accessory pangenome):

| Genus | Habitat | MAGs | MAG KOs | Field-only KOs | Jaccard |
|---|---|---|---|---|---|
| Dolichospermum | water | 7 | 1,025 | 532 | 0.29 [src: neon_mag_functional_discovery] |
| Palsa-465 | soil | 3 | 1,222 | 502 | 0.45 [src: neon_mag_functional_discovery] |
| Sulfotelmatobacter | soil | 5 | 1,253 | 434 | 0.45 [src: neon_mag_functional_discovery] |
| Rubrivivax | benthic/water | 10 | 1,769 | 397 | 0.48 [src: neon_mag_functional_discovery] |
| Mycobacterium | soil | 1 | 1,088 | 71 | 0.54 [src: neon_mag_functional_discovery] |

Top enriched modules (FDR q) include:
- M00145, NAD(P)H:quinone oxidoreductase: 15 / 17, q = 1.5 × 10⁻⁵. [src: neon_mag_functional_discovery]
- M00163, Photosystem I: 11 / 11, q = 2.7 × 10⁻⁵. [src: neon_mag_functional_discovery]
- M00157, F-type ATPase: 8 / 8, q = 6.4 × 10⁻⁴. [src: neon_mag_functional_discovery]
- M00161, Photosystem II: 15 / 23, q = 2.5 × 10⁻³. [src: neon_mag_functional_discovery]
- M00165, Calvin cycle: 11 / 15, q = 3.6 × 10⁻³. [src: neon_mag_functional_discovery]
- M00097, lycopene biosynthesis: 8 / 9, q = 3.4 × 10⁻³. [src: neon_mag_functional_discovery]
- M00202, oligopeptide transport: 4 / 4, q = 3.6 × 10⁻². [src: neon_mag_functional_discovery]
- M00220, rhamnose transport: 4 / 4, q = 3.6 × 10⁻². [src: neon_mag_functional_discovery]

The report also lists M00164 [src: neon_mag_functional_discovery], M00022 [src: neon_mag_functional_discovery], M00179 [src: neon_mag_functional_discovery], M00322 [src: neon_mag_functional_discovery], M00004 [src: neon_mag_functional_discovery], M00017 [src: neon_mag_functional_discovery], M00156 [src: neon_mag_functional_discovery] and M00166. [src: neon_mag_functional_discovery]

The photosystem and Calvin cycle dominance is attributed to heavy weighting of Planktothrix and Dolichospermum, whose cultured isolates are a thin slice of true diversity. [src: neon_mag_functional_discovery] The report reads the niche-specific transport and secondary-metabolism modules as the most directly H4-supporting signals. [src: neon_mag_functional_discovery] It locates the biologically meaningful signal there, not in the housekeeping modules. [src: neon_mag_functional_discovery]

## Summary; Key Findings

This part of the report covers the cohort, the hypothesis outcomes, lineage novelty across soil pH, habitat structure of functional gene content, soil chemistry effects, and the field-versus-cultured accessory gene test. Three of four hypotheses are supported, one in the opposite direction from prior expectation. The fourth, the H4 community proxy, returned a methodological null. [src: neon_mag_functional_discovery]

### Cohort

The analysis uses three NMDC-rehosted NEON metagenome studies: soil nmdc:sty-11-34xj1150 (n=6,489), surface water nmdc:sty-11-hht5sb92 (n=234) and benthic sediment nmdc:sty-11-pzmd0x14 (n=736). [src: neon_mag_functional_discovery] Together they contain 7,298 MAGs (metagenome assembled genomes), of which 1,609 pass MQ+HQ quality. [src: neon_mag_functional_discovery] See [[entities/nmdc-neon-metagenome-studies]].

### Lineage novelty rises with soil pH

The soil analysis uses 3,161 MQ+HQ MAG–biosample pairs with pH. [src: neon_mag_functional_discovery] The novel fraction, defined as no GTDB genus call, rises steadily from acidic to alkaline soils. [src: neon_mag_functional_discovery]

| Soil pH bin | n MAG-records | Novel fraction |
|---|---|---|
| < 4.5 | 396 | 7.6% [src: neon_mag_functional_discovery] |
| 4.5–5.5 | 678 | 16.2% [src: neon_mag_functional_discovery] |
| 5.5–6.5 | 980 | 25.0% [src: neon_mag_functional_discovery] |
| > 6.5 | 1,107 | 37.0% [src: neon_mag_functional_discovery] |

Novelty spans 29.4 percentage points across the observed range 3.23 ≤ pH ≤ 9.13. [src: neon_mag_functional_discovery] Ordinary least squares (OLS) on raw records gives a slope of +0.079 per pH unit, p = 9.1 × 10⁻⁴⁷. [src: neon_mag_functional_discovery] Kendall τ on the four bin midpoints is τ = 1.0 but p = 0.083. The report attributes this to a small-N power floor of 2/4! ≈ 0.083. [src: neon_mag_functional_discovery]

This direction is opposite the literature prior that acidic and peat-bog soils harbor the most novel and uncultured lineages. [src: neon_mag_functional_discovery] The report proposes, as an explanation and not a measurement, that GTDB culture-mining bias is the most parsimonious cause. Acidobacteriota and Verrucomicrobia have received decades of cultivation effort, so their species-level representation is mature. [src: neon_mag_functional_discovery] It also proposes that alkaline and neutral soils, including Pseudomonadota lineages of arid systems, are under-cultured, so novel lineages there are less likely to match a GTDB species. [src: neon_mag_functional_discovery] Without independent ground truth from full-length 16S phylogeny against an unbiased reference, the result fits both true biological novelty in alkaline soils and a GTDB coverage gap there. The report favors the coverage gap. [src: neon_mag_functional_discovery] See [[concepts/lineage-novelty-and-reference-database-culture-bias-across-environmental-gradients]] and [[entities/gtdb]].

### Habitat structure of functional gene content

Functional gene content partitions strongly by habitat. The test was an Aitchison-distance principal coordinates analysis (PCoA) on 2,506 MetagenomeAnnotation workflows and 9,584 prevalence-filtered KOs (KEGG orthologs). [src: neon_mag_functional_discovery] PERMANOVA (permutational multivariate analysis of variance) gives pseudo-F = 137, p = 0.001 for habitat (soil n=1,800; benthic n=618; water n=88). [src: neon_mag_functional_discovery] PC1 captures 43.8% of variance and separates cyanobacterial/water samples from soil. [src: neon_mag_functional_discovery]

At Benjamini-Hochberg false discovery rate (BH-FDR) < 0.05, enriched KEGG modules number 3 for soil, 23 for benthic and 16 for water. [src: neon_mag_functional_discovery] The list is dominated by central modules: M00178 ribosome, M00184 RNA polymerase, M00155 cytochrome c oxidase and M00159 ATPase. [src: neon_mag_functional_discovery] The report cautions that enrichment of such universal machinery usually reflects a taxonomic-abundance shift, such as Cyanobacteria over-represented in water, and not new functional capability. [src: neon_mag_functional_discovery] The interpretable signal lies in niche-specific modules. These are photosystems M00161 and M00163 in water and benthic samples, anaerobic-respiration markers and transport systems in benthic samples, and substrate-degradation modules in soil. [src: neon_mag_functional_discovery]

Interpretation was limited because nmdc_arkin.kegg_module_terms has 370 rows with only module_id and empty name and category fields. Labels for top hits came from external KEGG references. [src: neon_mag_functional_discovery] See [[concepts/habitat-and-soil-chemistry-structuring-of-metagenomic-functional-gene-content]].

### Soil chemistry: pH passes the effect-size threshold, horizon does not

Both soil factors are significant, but only pH clears the pre-registered 5% effect-size threshold. [src: neon_mag_functional_discovery] The smallest permutation p-value attainable with 999 permutations is p = 0.001. [src: neon_mag_functional_discovery]

- pH bin (4 levels): n = 1,700, pseudo-F = 32.5, p = 0.001, R² = 5.4%, passes. [src: neon_mag_functional_discovery]
- Soil horizon (O / M): n = 1,800, pseudo-F = 40.5, p = 0.001, R² = 2.2%, fails. [src: neon_mag_functional_discovery]

The report reads the weak horizon R² as consistent with pH absorbing much of the horizon signal, since organic-horizon samples tend toward lower pH and mineral samples toward neutral. [src: neon_mag_functional_discovery] A nested model might show a pH × horizon interaction. That test was not pre-registered and is left for follow-up. [src: neon_mag_functional_discovery]

### Field-versus-cultured accessory genes (H4)

The original H4 test (NB04) used a community-level KO union as a proxy for per-MAG accessory content. For each shared genus, it took KOs present in at least 50% of NEON workflows where that genus has a MAG. It contrasted these with the cultured KE-pangenome accessory content of the genus. [src: neon_mag_functional_discovery] It analyzed 24 shared genera. [src: neon_mag_functional_discovery] The result was uninformative:
- Pooled NEON-only KOs covered 9,547 / 9,584 (99.6%) of the entire universe. [src: neon_mag_functional_discovery]
- No KEGG modules were enriched at FDR < 0.05. [src: neon_mag_functional_discovery]
- Median Jaccard similarity between the NEON community and pangenome accessory content was 0.19. [src: neon_mag_functional_discovery]

The proxy is dominated by KOs from co-occurring taxa and not from the target genus. The plan's own caveat had warned of this, and the data confirmed it. [src: neon_mag_functional_discovery]

The report then found a previously overlooked path to per-MAG KO content. In the KBase Data Lakehouse, workflow_execution_set_mags_list.members_id is an array<string> of contig IDs per MAG. The gene_id in nmdc_results.annotation_kegg_orthology has the structure <contig_id>_<start>_<end>. [src: neon_mag_functional_discovery] Equi-joining on the extracted contig portion links gene KO calls to specific MAGs, and NB04b is this per-MAG re-analysis. [src: neon_mag_functional_discovery] H4b supports the hypothesis on the available cohort. It inherits a 53% cohort attrition from a habitat-biased gap in NMDC per-gene annotation tables. [src: neon_mag_functional_discovery] See [[concepts/annotation-and-environmental-metadata-table-gaps-in-the-data-lakehouse]] and [[concepts/join-key-validity-and-identifier-format-mismatches]].

Cyanobacterial Planktothrix and Dolichospermum MAGs, and uncultured peat-soil Palsa-465, Palsa-295 and Sulfotelmatobacter MAGs, carry hundreds of accessory KOs absent from any cultured representative of their genus. [src: neon_mag_functional_discovery] Their accessory KOs show KEGG-module enrichments for Photosystem I & II (M00161, M00163), the Calvin cycle (M00165) and lycopene biosynthesis (M00097). [src: neon_mag_functional_discovery] They also show enrichments for niche-specific transport modules M00202 oligopeptide, M00220 rhamnose and M00246 nickel. [src: neon_mag_functional_discovery] Module names were resolved from current and legacy KEGG snapshots. [src: neon_mag_functional_discovery] See [[concepts/field-only-accessory-gene-content-absent-from-cultured-pangenomes]].

## Key Findings: H4b per-MAG result — environmental MAGs carry hundreds of KOs absent from …

This part of the report contrasts the KEGG ortholog (KO) content of individual NEON metagenome-assembled genomes (MAGs) with cultured pangenomes. Every usable MAG carried field-only KOs. The pooled enrichment is dominated by a ribosome artifact and by cyanobacterial photosynthesis modules, and the report treats niche-specific transport and secondary-metabolism modules as the meaningful signal. The contrast used 73 usable MAGs across 19 genera. [src: neon_mag_functional_discovery] See [[concepts/field-only-accessory-gene-content-absent-from-cultured-pangenomes]] for the wider concept.

### Cohort-level results

The cohort had a median MAG KO set size of 1,113 and a median of 343 field-only KOs per MAG. [src: neon_mag_functional_discovery] The median Jaccard similarity between MAG KOs and the genus accessory pangenome was 0.42. [src: neon_mag_functional_discovery] All MAGs (100%) had at least 10 field-only KOs. [src: neon_mag_functional_discovery] In pooled recurrent field-only KOs, 29 KEGG modules were enriched at a false discovery rate (FDR) below 0.05. [src: neon_mag_functional_discovery]

### Genus-level results

Values below are medians per genus; Jaccard is against the genus accessory pangenome.

| Genus | Habitat | MAGs | MAG KOs | Field-only KOs | Jaccard |
|---|---|---|---|---|---|
| Planktothrix | water | 8 | 1,073 | 689 | 0.28 [src: neon_mag_functional_discovery] |
| Dolichospermum | water | 7 | 1,025 | 532 | 0.29 [src: neon_mag_functional_discovery] |
| Palsa-465 | soil | 3 | 1,222 | 502 | 0.45 [src: neon_mag_functional_discovery] |
| Puia | soil | 2 | 1,082 | 467 | 0.47 [src: neon_mag_functional_discovery] |
| Sulfotelmatobacter | soil | 5 | 1,253 | 434 | 0.45 [src: neon_mag_functional_discovery] |
| Rubrivivax | benthic/water | 10 | 1,769 | 397 | 0.48 [src: neon_mag_functional_discovery] |
| Palsa-295 | soil | 3 | 1,046 | 384 | 0.51 [src: neon_mag_functional_discovery] |
| Mycobacterium | soil | 1 | 1,088 | 71 | 0.54 [src: neon_mag_functional_discovery] |

The two water cyanobacterial genera have the most field-only KOs and the lowest Jaccard values in this list. Mycobacterium rests on a single MAG. [src: neon_mag_functional_discovery]

### Enriched modules

Module names were resolved from the KEGG REST (representational state transfer) API and legacy KEGG snapshots. [src: neon_mag_functional_discovery] Values are field-only KOs over total KOs in the module, with FDR q.

- Housekeeping and energy: M00178 Ribosome, bacteria, 52 / 54, q = 9.5 × 10⁻²⁶. [src: neon_mag_functional_discovery] M00157 F-type ATPase, 8 / 8, q = 6.4 × 10⁻⁴. [src: neon_mag_functional_discovery] M00164 ATP synthase (legacy), 8 / 8, q = 6.4 × 10⁻⁴. [src: neon_mag_functional_discovery] M00179 Ribosome, archaea (legacy), 30 / 65, q = 6.9 × 10⁻³. [src: neon_mag_functional_discovery] M00149 Succinate dehydrogenase, 4 / 4, q = 3.6 × 10⁻². [src: neon_mag_functional_discovery] M00156 Cytochrome c oxidase, cbb3-type, 4 / 4, q = 3.6 × 10⁻². [src: neon_mag_functional_discovery]
- Photosynthesis and carbon fixation: M00145 NAD(P)H:quinone oxidoreductase, 15 / 17, q = 1.5 × 10⁻⁵. [src: neon_mag_functional_discovery] M00163 Photosystem I, 11 / 11, q = 2.7 × 10⁻⁵. [src: neon_mag_functional_discovery] M00161 Photosystem II, 15 / 23, q = 2.5 × 10⁻³. [src: neon_mag_functional_discovery] M00165 Calvin cycle, 11 / 15, q = 3.6 × 10⁻³. [src: neon_mag_functional_discovery] M00166 Reductive pentose phosphate (legacy), 4 / 4, q = 3.6 × 10⁻². [src: neon_mag_functional_discovery] M00004 Pentose phosphate pathway, 7 / 10, q = 3.6 × 10⁻². [src: neon_mag_functional_discovery]
- Biosynthesis: M00016 Lysine, 11 / 12, q = 1.9 × 10⁻⁴. [src: neon_mag_functional_discovery] M00026 Histidine, 12 / 15, q = 6.4 × 10⁻⁴. [src: neon_mag_functional_discovery] M00096 C5 isoprenoid, 8 / 9, q = 3.4 × 10⁻³. [src: neon_mag_functional_discovery] M00097 Lycopene, 8 / 9, q = 3.4 × 10⁻³. [src: neon_mag_functional_discovery] M00022 Shikimate, 10 / 13, q = 3.6 × 10⁻³. [src: neon_mag_functional_discovery] M00119 Pantothenate, 6 / 6, q = 5.3 × 10⁻³. [src: neon_mag_functional_discovery] M00017 Methionine, 7 / 10, q = 3.6 × 10⁻². [src: neon_mag_functional_discovery] M00123 Biotin, 4 / 4, q = 3.6 × 10⁻². [src: neon_mag_functional_discovery]
- Transport and degradation: M00322 Limonene degradation (legacy), 5 / 5, q = 1.6 × 10⁻². [src: neon_mag_functional_discovery] M00323 Urea cycle (legacy), 5 / 5, q = 1.6 × 10⁻². [src: neon_mag_functional_discovery] M00202 Oligopeptide transport (legacy), 4 / 4, q = 3.6 × 10⁻². [src: neon_mag_functional_discovery] M00220 Rhamnose transport (legacy), 4 / 4, q = 3.6 × 10⁻². [src: neon_mag_functional_discovery] M00246 Nickel transport (legacy), 4 / 4, q = 3.6 × 10⁻². [src: neon_mag_functional_discovery]

### Interpretation and caveats

The ribosome result is an artifact. Ribosomal protein KOs are core genes biologically, yet they appear field-only in 52 of 54 cases. The report attributes this to the pangenome's `is_core = false` definition, which can label ribosomal genes accessory when they vary across species within a genus. [src: neon_mag_functional_discovery] The report places the meaningful signal in the niche-specific modules, not the housekeeping ones. [src: neon_mag_functional_discovery]

The report attributes the photosystem and Calvin cycle dominance to heavy weighting of Planktothrix and Dolichospermum. It argues that cultured cyanobacterial isolates are a thin slice of true diversity. [src: neon_mag_functional_discovery] This is the report's interpretation, not a separate test.

The report calls oligopeptide, rhamnose and nickel transport, limonene degradation and the urea cycle the most directly H4-supporting signals. It says they are plausibly niche-specific accessory functions under environmental selection that lab cultivation does not reproduce. [src: neon_mag_functional_discovery] This is a plausibility argument. Each of these modules has only 4 or 5 KOs. [src: neon_mag_functional_discovery]

The analysis is documented in notebook 04b_per_mag_accessory_contrast.ipynb. [src: neon_mag_functional_discovery]

## Caveats and Limitations: Sensitivity analysis for the 57% annotation coverage gap

This part of the report asks how far the NEON H4b result depends on the 173 MAGs (metagenome assembled genomes) that lack per-gene annotation tables. Four sensitivity estimators show the central claim holds except in one scenario the report calls unrealistic. The coverage gap itself is strongly habitat-biased, so the result generalizes only to a water-skewed sub-cohort. [src: neon_mag_functional_discovery]

### The coverage gap and its bias

The per-MAG re-analysis was limited because nmdc_results.annotation_kegg_orthology covers only 57% of NEON MetagenomeAnnotation workflows (1,799 / 3,137). [src: neon_mag_functional_discovery] The 73-MAG H4b cohort is a non-random 30% subset of the 246-MAG analysis target. Per-gene-table coverage is 100% for water genera and 0–30% for soil. [src: neon_mag_functional_discovery] Coverage and survival into the NB04b cohort fall together across habitat groups:

| Genus group | Coverage | NB04b outcome |
|---|---|---|
| Surface-water cyanobacteria (Planktothrix, Dolichospermum, Rubrivivax) | 100% | All 27 MAGs survived [src: neon_mag_functional_discovery] |
| Benthic generalists (Ferruginibacter, Flavobacterium, UBA953) | ~85% | 16 / 19 survived [src: neon_mag_functional_discovery] |
| Soil acidobacteria (Sulfotelmatobacter, Palsa-465, Palsa-1447) | ~30% | 12 / 40 survived [src: neon_mag_functional_discovery] |
| Soil cultured genera (Mycobacterium, Bradyrhizobium, Acidoferrum) | ~10% | 5 / 65 survived [src: neon_mag_functional_discovery] |
| Soil unculturable / novel (Acidocella, BOG-234, Pseudolabrys, Pseudonocardia, Reyranella) | 0% | 0 / 28 survived [src: neon_mag_functional_discovery] |

The report says the five fully attrited soil genera are the kind of MAGs that NB02 flagged as novel-lineage candidates. It thinks they most likely sit in workflows that NMDC has not yet fully processed into per-gene tables. [src: neon_mag_functional_discovery] The report records partial, habitat-biased annotation coverage as a generalizable pitfall in docs/pitfalls.md. [src: neon_mag_functional_discovery] See [[concepts/metadata-and-annotation-coverage-gaps-biasing-environmental-genome-cohorts]].

### Four sensitivity estimators

To bound the dependence on the missing 173 MAGs, the report computed four estimators. [src: neon_mag_functional_discovery] The first three leave the result essentially unchanged. Only the worst case fails.

| Estimator | Median field-only KOs / MAG | Median Jaccard | Fraction of MAGs with ≥ 10 field-only KOs |
|---|---|---|---|
| Naive (observed only, n=73) | 371 [src: neon_mag_functional_discovery] | 0.43 [src: neon_mag_functional_discovery] | 100% [src: neon_mag_functional_discovery] |
| Inverse-coverage-reweighted (effective n=218) | 319 [src: neon_mag_functional_discovery] | 0.43 [src: neon_mag_functional_discovery] | 100% [src: neon_mag_functional_discovery] |
| Best-case imputation (missing MAGs = same-genus median) | 371 [src: neon_mag_functional_discovery] | not reported [src: neon_mag_functional_discovery] | 100% [src: neon_mag_functional_discovery] |
| Worst-case (missing MAGs = 0 field-only) | 0 [src: neon_mag_functional_discovery] | not reported [src: neon_mag_functional_discovery] | 29.7% [src: neon_mag_functional_discovery] |

A bootstrap of 2,000 weighted resamples gave a 95% CI (confidence interval) of 180–384 on the reweighted median field-only KO (KEGG ortholog) count. This overlaps the naive 371 estimate. [src: neon_mag_functional_discovery] The report concludes that the claim of hundreds of accessory KOs absent from cultured pangenomes survives reweighting and best-case imputation with essentially no change. [src: neon_mag_functional_discovery] It places the realistic range for the missing cohort between the reweighted and best-case scenarios, and both fully support H4b. [src: neon_mag_functional_discovery] See [[concepts/field-only-accessory-gene-content-absent-from-cultured-pangenomes]].

### The worst-case failure

In the worst case, all 173 missing MAGs return zero field-only KOs. The fraction with ≥10 then falls to 29.7%, right at the pre-registered 30% falsification threshold. This is the only scenario where H4b fails. [src: neon_mag_functional_discovery] The report calls it biologically unrealistic. None of the 5 fully attrited soil genera is a known monoterpene-naïve or aldehyde-dehydrogenase-only lineage. Published Acidobacteriota genome content suggests they would carry substantial niche-specific accessory genes. [src: neon_mag_functional_discovery]

Even so, the H4b result generalizes only within a water-skewed sub-cohort. The report attributes the photosystem-heavy enrichment list to that bias, not to a unique feature of field-only KOs across all NEON MAGs. [src: neon_mag_functional_discovery]

### Other limits on the NEON cohort

- The NMDC NEON re-host holds bacterial / archaeal metagenomes only. No metatranscriptomic, metaproteomic, metabolomic, lipidomic or NOM data are associated with these three studies, so multi-omics framing is not feasible. [src: neon_mag_functional_discovery] The nmdc_arkin _gold tables return zero NEON rows. [src: neon_mag_functional_discovery]
- Of the 1,609 MQ+HQ MAGs, only 40 are archaeal, all from soil and 4 of them HQ. [src: neon_mag_functional_discovery]
- A clean cross-domain functional comparison was not feasible at this sample size. Archaea remain a soil-only side panel for future work. [src: neon_mag_functional_discovery]
- nmdc_arkin.kegg_module_terms in the KBase Data Lakehouse has empty name, description and category columns for all 370 modules, and only module_id is populated. [src: neon_mag_functional_discovery] The report therefore resolved module IDs (identifiers) against an external KEGG reference. [src: neon_mag_functional_discovery]

## Data Sources; Supporting Evidence; Biotech Outlook: Cold-Active ε-Lactone Hydrolases from …

This part of the report lists the data sources and derived files behind the NEON analysis. It also gives the follow-up finding that K14731, an ε-lactone hydrolase, is a more actionable signal than the initial limonene-degradation module hit. The enzyme finding rests on the report's own per-step dissection and a targeted post-hoc literature review. The commercial-niche statement is the report's proposal. [src: neon_mag_functional_discovery]

### Data sources

The analysis drew on several Data Lakehouse tables. The `nmdc_metadata` tables hold study, biosample, MAG (metagenome assembled genome), workflow, and per-workflow KO (KEGG ortholog), COG (clusters of orthologous groups) and Pfam data. [src: neon_mag_functional_discovery] Per-gene KO calls in nmdc_results.annotation_kegg_orthology were joined on `members_id` to build per-MAG KO sets. [src: neon_mag_functional_discovery] The tables nmdc_arkin.kegg_ko_module and kegg_module_terms mapped KOs to modules for Fisher enrichment. [src: neon_mag_functional_discovery] The kbase_ke_pangenome tables gtdb_species_clade, gene_cluster and eggnog_mapper_annotations supplied a 27,690-species pangenome, accessory gene clusters and KO assignments. [src: neon_mag_functional_discovery]

By design, the report excluded the nmdc_arkin _gold tables, which have zero NEON coverage. It also excluded external NEON portal data: climate stations, vegetation and eddy-covariance. [src: neon_mag_functional_discovery]

### Derived data products

| File | Size | Content |
|---|---|---|
| data/sample_inventory.tsv | 7,459 rows | Per-biosample metadata: coordinates, depth, pH, chemistry, environmental-scale terms, habitat [src: neon_mag_functional_discovery] |
| data/workflow_inventory.tsv | 14,255 records | Per-workflow workflow_id, data_generation_id, type, habitat [src: neon_mag_functional_discovery] |
| data/mag_inventory.tsv | 7,298 rows | Per-MAG GTDB taxonomy, completeness, contamination, bin_quality, habitat, lowest_rank [src: neon_mag_functional_discovery] |
| data/biosample_field_coverage.json | 1,398 fields × 3 habitats | Non-null counts per biosample_set field per study [src: neon_mag_functional_discovery] |
| data/03_ko_matrix.tsv.gz | 2,506 × 9,584 | Workflow by prevalence-filtered-KO count matrix [src: neon_mag_functional_discovery] |

The remaining outputs are grouped by analysis stage:
- data/02_* holds lineage-novelty cross-tabulations and pH-bin tables. [src: neon_mag_functional_discovery]
- data/03_* holds habitat and soil PCoA (principal coordinates analysis) and PERMANOVA (permutational multivariate analysis of variance), per-KO Welch tests, and module enrichment. [src: neon_mag_functional_discovery]
- data/04_* holds the underpowered community-level field-versus-lab contrast. [src: neon_mag_functional_discovery]
- data/04b_* holds per-MAG KO sets, per-MAG and per-genus contrasts, and pooled module enrichment. [src: neon_mag_functional_discovery]
- data/05_* holds the findings summary and top candidate MAGs. [src: neon_mag_functional_discovery]

The data/*.tsv* and data/*.parquet files are gitignored and regenerable. Notebooks, figures, the discovery JSON, the discovery summary and the markdown documents are committed. [src: neon_mag_functional_discovery]

The notebooks map to the report's hypotheses as follows:
- Notebook 01 reproduces the discovery-probe counts and emits the canonical inventories. [src: neon_mag_functional_discovery]
- Notebook 02 tests H1 with per-MAG novelty distributions across habitat and soil pH, using OLS (ordinary least squares) and logistic tests on per-record data. [src: neon_mag_functional_discovery]
- Notebook 03 tests H2 and H3 with the workflow-by-KO matrix, PCoA and PERMANOVA, per-KO Welch tests and module enrichment. [src: neon_mag_functional_discovery]
- Notebook 04 holds the original underpowered H4 community-proxy run, documented as a methodological dead-end. [src: neon_mag_functional_discovery]
- Notebook 04b is the proper per-MAG H4 test, using the `members_id` to `gene_id` join. [src: neon_mag_functional_discovery]
- Notebook 05 produces a single 6-panel synthesis figure and the findings summary. [src: neon_mag_functional_discovery]

### From limonene degradation to ε-lactone hydrolase

The KEGG-module enrichment in NB04b first flagged M00322 (limonene degradation, limonene to β-ketoadipate) as field-only-enriched. [src: neon_mag_functional_discovery] Per-step pathway dissection shows this limonene framing is largely an artifact. [src: neon_mag_functional_discovery] The novel signal lies in K14731, ε-lactone hydrolase (EC 3.1.1.83, Enzyme Commission number). It is carried by 15 sub-Arctic palsa-peat soil Acidobacteriota MAGs whose cultured pangenome accessory lacks the gene. [src: neon_mag_functional_discovery]

### Biotech outlook: cold-active ε-lactone hydrolases

A targeted post-hoc literature review finds cold-active or psychrophilic ε-lactone hydrolases to be a published gap. [src: neon_mag_functional_discovery] Three observations support this:
- Every characterized MlhB-class enzyme is mesophilic. The example given is Rhodococcus erythropolis DCL14, with T_opt ~30 °C. [src: neon_mag_functional_discovery]
- Every metagenomic LEH/MlhB discovery to date has targeted hot environments. [src: neon_mag_functional_discovery]
- Every engineering effort has pushed temperature upward. Wijma et al. 2014 raised Re-LEH T_m from 50 → 85 °C via FRESCO. [src: neon_mag_functional_discovery]

The report describes the lactone-hydrolase market as well established. Its uses are commercial-scale vitamin B5 manufacturing, Baeyer-Villiger product workup in monoterpene/flavor chemistry, zearalenone mycotoxin detoxification, and emerging chiral-heterocycle synthesis. [src: neon_mag_functional_discovery] It proposes that a cold-active variant would fill a genuine, currently unfilled niche. [src: neon_mag_functional_discovery]

### Literature cited for context

- The canonical limonene to β-ketoadipate pathway is defined in Rhodococcus erythropolis DCL14 (van der Werf et al. 1999, AEM PMID 10224006, where PMID is PubMed identifier). [src: neon_mag_functional_discovery]
- Marmulla & Harder 2014, Front. Microbiol. PMID 25076942, reviews the four-enzyme route. [src: neon_mag_functional_discovery]
- Biotech bioconversion precedents use oil/alkane-contaminated soil and hot-spring isolates:
  - van Beilen et al. 2005 (PMID 15811996) used Mycobacterium HXN-1500 CYP153A6. [src: neon_mag_functional_discovery]
  - Cornelissen et al. 2013 (PMID 23239244) used Pseudomonas putida. [src: neon_mag_functional_discovery]
  - Ferrandi et al. 2015 (PMID 26032250) used a hot-spring metagenomic LEH. [src: neon_mag_functional_discovery]
  - Ma et al. 2026 (PMID 41265579) used engineered yeast at 15.2 g/L. [src: neon_mag_functional_discovery]
- Ayoub et al. 2025 (PMID 41441891) is cited as a recent comprehensive review. [src: neon_mag_functional_discovery]
- Free-living forest-soil Bradyrhizobium are known oligotrophic aromatic-carbon degraders (VanInsberghe et al. 2015, ISME J PMID 25909973). [src: neon_mag_functional_discovery] The report treats this as supportive context, not direct evidence of limonene catabolism. [src: neon_mag_functional_discovery]

## Biotech Outlook: Cold-Active ε-Lactone Hydrolases from Sub-Arctic Palsa-Peat …

This part of the report dissects limonene-pathway content in NEON metagenome assembled genomes (MAGs) one KEGG ortholog (KO) at a time. It downgrades a novel limonene-degrader claim to a broader proposal for cold-active ε-lactone hydrolases from the Toolik palsa-peat site. The biotech applications are the report's proposals, not measurements. [src: neon_mag_functional_discovery]

### Per-KO dissection of the limonene pathway

Module-level M00322 enrichment hides which pathway step each MAG encodes. [src: neon_mag_functional_discovery] KEGG ko00903 supplies five informative KOs. [src: neon_mag_functional_discovery]

- K14733 is the entry-step (S)-limonene 1,2-monooxygenase, EC 1.14.13.107. [src: neon_mag_functional_discovery]
- K10533 is limonene-1,2-epoxide hydrolase, EC 3.3.2.8, which converts epoxide to diol at Step 2. [src: neon_mag_functional_discovery]
- K14732 is limonene hydroxylase in the carveol/perillyl branch, an alternative entry route. [src: neon_mag_functional_discovery]
- K14731 is ε-lactone hydrolase, EC 3.1.1.83. It is a broad-substrate late-pathway enzyme, not limonene-exclusive. [src: neon_mag_functional_discovery]
- K00128 is NAD-dependent aldehyde dehydrogenase, EC 1.2.1.3. It is a housekeeping enzyme present in essentially every aerobic organism. [src: neon_mag_functional_discovery]

Classifying MAGs by these KOs gives the following classes.

| Class | MAGs | Content |
|---|---|---|
| GENERIC_ONLY | 43 | K00128 only. Includes all 14 Planktothrix and Dolichospermum MAGs. [src: neon_mag_functional_discovery] |
| LATE_ONLY | 15 | K14731 ± K00128. These MAGs can process lactone intermediates but cannot initiate limonene oxidation. [src: neon_mag_functional_discovery] |
| PARTIAL_NO_HYDROLASE | 2 | Both are Bradyrhizobium. They carry the entry monooxygenase and lactone hydrolase but lack the diol-forming step. [src: neon_mag_functional_discovery] |
| OTHER | 1 | A 13-2-20CM-66-19 MAG with only the Step 2 hydrolase K10533. [src: neon_mag_functional_discovery] |
| ENTRY_ONLY | 1 | A Rubrivivax MAG with K14733 and nothing downstream. [src: neon_mag_functional_discovery] |
| FULL | 1 | A Mycobacterium MAG with entry, step2 and late steps (5 KOs). [src: neon_mag_functional_discovery] |

The LATE_ONLY MAGs concentrate in soil Acidobacteriota: Sulfotelmatobacter (4), Palsa-465 (3), Palsa-1447 (3), Acidoferrum (1), 13-2-20CM-66-19 (1), Terracidiphilus (1), Rhizomicrobium (1), Palsa-295 (0, generic-only), plus Rubrivivax (1). [src: neon_mag_functional_discovery]

### What the classes mean

None of the novel-genus MAGs carry the entry-point monooxygenase K14733. [src: neon_mag_functional_discovery] The palsa-peat Acidobacteriota cannot initiate limonene catabolism. They can only process downstream ring-opened intermediates supplied by other community members or natural plant-litter lactones. [src: neon_mag_functional_discovery]

The report therefore downgrades its novel sub-Arctic Acidobacteriota limonene-degradation claim. Their field-only KO is K14731, which also acts on caprolactam, Baeyer-Villiger products and other ε-lactones. [src: neon_mag_functional_discovery]

The only full canonical pathway is in a [[entities/mycobacterium|Mycobacterium]] MAG. Mycobacterium is the already-cultured reference limonene degrader (van Beilen 2005, PMID 15811996). [src: neon_mag_functional_discovery] It has been the workhorse of cultivated limonene biocatalysis for about 20 years, so the report finds no lineage novelty there. [src: neon_mag_functional_discovery]

The [[entities/bradyrhizobium|Bradyrhizobium]] partial-pathway KOs are also in the cultured Bradyrhizobium pangenome, so they are not field-only. [src: neon_mag_functional_discovery] Bradyrhizobium MAGs carry K14733 at field abundance comparable to cultured representatives. The report flags them as additional soil biocatalyst candidates, but not novel relative to cultured accessory. [src: neon_mag_functional_discovery]

### Cyanobacterial false positive

The apparent M00322 enrichment in 14 Planktothrix and Dolichospermum MAGs at NEON PRLA (Prairie Lake, ND) was driven entirely by K00128. [src: neon_mag_functional_discovery] These MAGs carry none of K14733, K07381, K07382 or K14731. [src: neon_mag_functional_discovery] The report says this fits the cyanobacterial literature, which frames these organisms exclusively as terpene producers, not degraders. [src: neon_mag_functional_discovery]

The report draws a methodological lesson. Module-level enrichment should be cross-checked with per-KO step assignment, because a broad-substrate housekeeping enzyme shared by dozens of pathways can drive spurious enrichment alone. [src: neon_mag_functional_discovery] See [[concepts/module-level-enrichment-artifacts-from-broad-substrate-enzymes]].

### Sub-Arctic ε-lactone hydrolases as a biotech proposal

The K14731 enzymes from Sulfotelmatobacter, Palsa-465, Palsa-1447 and Acidoferrum are real enzymes that the cultured pangenome accessory of those genera does not encode. [src: neon_mag_functional_discovery] The report calls them cold-active by virtue of their source habitat, Toolik palsa, with ~−10 °C mean annual temperature and pH ≈ 5.2. [src: neon_mag_functional_discovery] It proposes them as candidates for broad lactone biocatalysis, including Baeyer-Villiger product processing, caprolactone chemistry and polyhydroxyalkanoate intermediate hydrolysis. It does not limit them to limonene-derived substrates. [src: neon_mag_functional_discovery] See [[entities/toolik-palsa-peat-site]] and [[concepts/biocatalyst-potential-of-uncultured-soil-bacterial-enzymes]].

#### Established industrial footprint

ε-Lactone hydrolases (EC 3.1.1.83) and the broader MlhB family have an established industrial footprint. [src: neon_mag_functional_discovery]

- Kinetic resolution of D/L-pantolactone for vitamin B5 manufacturing is the canonical commercial use. [src: neon_mag_functional_discovery] The original Fuji Pharmaceutical process uses Fusarium oxysporum lactonase (Shimizu et al. 2001, PMID 11640988). [src: neon_mag_functional_discovery]
- A recent benchmark deracemized 1.25 M dl-pantolactone to D-pantolactone at 98.6% ee and 107 g/L/d productivity in a 3-enzyme Escherichia coli whole-cell cascade (Jin et al. 2023, PMID 37513182). [src: neon_mag_functional_discovery]
- A Baeyer-Villiger monooxygenase (BVMO) plus lactone-hydrolase tandem is established. Lactones are opened to ω-hydroxy acids for monoterpene/flavor chemistry (van der Werf et al. 2000, PMID 10832640). [src: neon_mag_functional_discovery]
- ZHD-class lactone hydrolases enable food/feed-safe zearalenone mycotoxin detoxification (Yu et al. 2020, PMID 31760747). [src: neon_mag_functional_discovery]
- Engineered Re-LEH performs Baldwin cyclizations with >99% conversion and 99:1 e.r. (Li et al. 2022, PMID 36535947). [src: neon_mag_functional_discovery]

#### Cold-active white space

A focused PubMed, Google Scholar and bioRxiv search on 2026-05-22 returned zero hits coupling "cold-active" or "psychrophilic" with "lactone hydrolase" or EC 3.1.1.83. [src: neon_mag_functional_discovery]

- The prototype MlhB from Rhodococcus erythropolis DCL14 is mesophilic, with T_opt ≈ 30 °C and pH optimum 9.5 (PMID 11157238). [src: neon_mag_functional_discovery]
- Two thermophilic LEHs with divergent stereoselectivity came from hot-spring metagenomic libraries (Ferrandi et al. 2015, PMID 26032250). [src: neon_mag_functional_discovery]
- Genome mining yielded 8 active enzymes, including 2 LEHs from mesophilic soil bacteria (Stojanovski et al. 2020, PMID 32732040). [src: neon_mag_functional_discovery]
- Engineering has been directionally upward. Wijma et al. 2014 (PMID 24402331) raised Re-LEH apparent T_m from 50 to 85 °C with FRESCO design, and the report states no reciprocal cold-adaptation effort has been published. [src: neon_mag_functional_discovery]
- All published variants of closely related zearalenone lactone hydrolases lose activity rapidly above 55 °C. [src: neon_mag_functional_discovery]

#### Proposed applications and mining plan

The report proposes these uses.

- Pharmaceutical kinetic resolutions at 5–15 °C, to protect enantiomeric purity and substrate yield. [src: neon_mag_functional_discovery]
- Zearalenone-class mycotoxin detoxification in refrigerated food and feed chains, where mesophilic ZHD enzymes are inactive. [src: neon_mag_functional_discovery]
- PCL ring-opening or depolymerization at sub-ambient temperatures. The search found no EC 3.1.1.83 hydrolases applied to PCL, so the report calls this a white-space sub-niche. [src: neon_mag_functional_discovery]
- Pairing cold-adapted enzymes with cold-tolerant Pseudomonas, Rhodococcus or Psychrobacter hosts. Limonene and lactone substrates are membrane-toxic to mesophilic Pseudomonas hosts above the mid-30s °C (Vermaas et al. 2018, PMID 30352510). [src: neon_mag_functional_discovery]

The plan is anchored on the 15 LATE_ONLY K14731-carrying MAGs from the NEON Toolik palsa-peat site. [src: neon_mag_functional_discovery] It proposes sequence-first mining. K14731 and homologous LEH/MlhB Pfam-domain protein sequences would be extracted from the 15 Toolik MAGs. [src: neon_mag_functional_discovery] The cohort is Sulfotelmatobacter ×4, Palsa-465 ×3, Palsa-1447 ×3, Acidoferrum ×1, 13-2-20CM-66-19 ×1, Terracidiphilus ×1, Rhizomicrobium ×1 and Rubrivivax ×1. [src: neon_mag_functional_discovery]

## Biotech Outlook: Cold-Active ε-Lactone Hydrolases from Sub-Arctic Palsa-Peat … (2)

This part of the report sets out follow-up work for the Toolik palsa-peat lactone-hydrolase candidates (a sequence-mining and expression plan, plus cultivation and metagenomic-library options). It also lists the coverage limits that make the current cohort a lower bound, and further analyses the report proposes. These are proposals and caveats, not measured results. [src: neon_mag_functional_discovery]

### Sequence-mining cohort and expression plan

The report proposes extracting K14731 sequences (and homologous LEH/MlhB Pfam-domain proteins) from 15 Toolik MAGs (metagenome assembled genomes). The cohort is Sulfotelmatobacter ×4, Palsa-465 ×3, Palsa-1447 ×3, Acidoferrum ×1, 13-2-20CM-66-19 ×1, Terracidiphilus ×1, Rhizomicrobium ×1 and Rubrivivax ×1. [src: neon_mag_functional_discovery] It proposes heterologous expression in Escherichia coli at 15 °C. Screening would use (R)/(S) limonene-1,2-epoxide, pantolactone, ε-caprolactone and zearalenone as model substrates. [src: neon_mag_functional_discovery]

### Cultivation and library routes

The report describes the Toolik biosample nmdc:bsm-11-cypgnq21 as coming from 68.62°N, -149.63°W, pH 5.24, O horizon. Toolik biosamples are physically archived at the NEON Biorepository at Arizona State University. [src: neon_mag_functional_discovery] It suggests that enrichment cultivation of archived samples at 5–10 °C, with lactones as sole carbon source, could isolate the source organisms for stable enzyme expression. [src: neon_mag_functional_discovery] Acidobacteriota strain JP12 (Huber/Pester et al. 2026, PMID 41739071; PMID is a PubMed identifier) is named as a candidate cultured peat reference. Its genome could be checked for a K14731 homolog. [src: neon_mag_functional_discovery]

Robinson et al. 2004 (PMID 15713477) demonstrated direct integron-cassette mining of soil for LEH-superfamily folds, including the Bal32a structure. [src: neon_mag_functional_discovery] The report proposes extending this to sub-Arctic peat or permafrost metagenomic libraries, which it calls methodologically established and aimed at an open niche. [src: neon_mag_functional_discovery]

### Hypothesis on uncharacterized folds

The report hypothesizes that many environmental Acidobacteriota carry uncharacterized LEH-family folds that lack KO (KEGG ortholog) annotation. [src: neon_mag_functional_discovery] To test this, it proposes re-running the dissection with Pfam PF03157 (LEH fold) and Pfam PF12697 (α/β-hydrolase fold-3). This depends first on verifying pfam_annotation_gff coverage on the soil cohort on JupyterHub. [src: neon_mag_functional_discovery]

### Coverage limits

The 73-MAG H4b cohort over-represents water habitats. Cyanobacteria have 100% per-gene KO coverage, while soil has 0–30%. [src: neon_mag_functional_discovery] Five soil genera with strong a-priori monoterpene- and lactone-catabolism relevance returned 0 MAGs with per-gene KO data. They are Acidocella, BOG-234, Pseudolabrys, Pseudonocardia and Reyranella. [src: neon_mag_functional_discovery]

The report therefore treats the 15-MAG K14731 cohort as a lower bound. The full sub-Arctic peat soil cohort likely holds more novel lactone-hydrolase carriers hidden by the annotation gap. [src: neon_mag_functional_discovery] It makes the same statement about the dissected pathway-class distribution and novel limonene-pathway carriers. [src: neon_mag_functional_discovery]

Bounded SQL (structured query language) could not query per-workflow coverage in pfam_annotation_gff and annotation_enzyme_commission. So the report does not know whether those tables fill the soil-genera gap left by annotation_kegg_orthology. [src: neon_mag_functional_discovery] It estimates that a PySpark scan on JupyterHub would resolve this in about 30 minutes and unlock the H4 re-analysis for the excluded soil genera. [src: neon_mag_functional_discovery]

### Further analyses proposed

- The file data/05_top_field_only_candidates.tsv lists 15 MAGs whose accessory gene content most exceeds the cultured pangenome. The report offers them as testable hypotheses for cultivation or synthetic-construct work. [src: neon_mag_functional_discovery]
- A within-genus Mantel-like test would ask whether MAG-pair functional distance tracks GTDB-Tk ANI (average nucleotide identity) distance. It would separate uniformly diverged accessory content from habitat-stratified gene gain or loss. [src: neon_mag_functional_discovery]
- A curated full-length 16S phylogeny against SILVA NR99 would test whether NEON OTUs (operational taxonomic units) from alkaline soils are genuinely more divergent or just less GTDB-represented. [src: neon_mag_functional_discovery]
- The 40 soil archaeal MAGs are too few for the main analysis. They are enough for a focused per-MAG functional contrast, since Methanobacterium, Methanosarcina and Nitrososphaera are all present. [src: neon_mag_functional_discovery]

### Provenance

The report names the NMDC NEON Python notebook page as its notebook entry point. [src: neon_mag_functional_discovery] Its author is Chris Mungall of Lawrence Berkeley National Laboratory, ORCID 0000-0002-6601-2165. [src: neon_mag_functional_discovery]

## Caveats and Open Work

- The H4b analysis supports the hypothesis only on the available cohort. It inherits a 53% cohort attrition from a habitat-biased gap in NMDC per-gene annotation tables. [src: neon_mag_functional_discovery] See [[concepts/metadata-and-annotation-coverage-gaps-biasing-environmental-genome-cohorts]].
- The soil novelty trend cannot separate biological novelty from a GTDB coverage gap without a full-length 16S phylogeny against an unbiased reference. [src: neon_mag_functional_discovery]
- The nmdc_arkin.kegg_module_terms table has 370 rows with only module_id and empty name and category fields. Module labels therefore came from external KEGG references. [src: neon_mag_functional_discovery]
- The soil horizon test is capped at p = 0.001 by 999 permutations. [src: neon_mag_functional_discovery] A nested model with a pH × horizon interaction is untested follow-up work. [src: neon_mag_functional_discovery]

## Slots Into

- [[concepts/lineage-novelty-and-reference-database-culture-bias-across-environmental-gradients]]: soil novelty rises from 7.6% to 37.0% with pH, which is opposite the literature prior and may reflect a GTDB coverage gap. [src: neon_mag_functional_discovery]
- [[concepts/habitat-and-soil-chemistry-structuring-of-metagenomic-functional-gene-content]]: habitat PERMANOVA pseudo-F = 137, while soil horizon explains only 2.2%. [src: neon_mag_functional_discovery]
- [[concepts/field-only-accessory-gene-content-absent-from-cultured-pangenomes]]: a median of 343 field-only KOs per MAG, with 29 modules enriched. [src: neon_mag_functional_discovery]
- [[concepts/metadata-and-annotation-coverage-gaps-biasing-environmental-genome-cohorts]]: the 53% cohort attrition from a habitat-biased annotation gap. [src: neon_mag_functional_discovery]
- [[concepts/annotation-and-environmental-metadata-table-gaps-in-the-data-lakehouse]]: the empty name and category fields in kegg_module_terms. [src: neon_mag_functional_discovery]
