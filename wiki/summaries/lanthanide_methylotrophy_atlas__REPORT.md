---
type: "Summary"
description: "Summary of the project Lanthanide Methylotrophy Atlas — Distribution and Environmental Context of REE-Dependent Methanol Oxidation Across 293K Genomes."
doc_type: "short"
full_text: "sources/lanthanide_methylotrophy_atlas__REPORT.md"
---
# Lanthanide Methylotrophy Atlas — Distribution and Environmental Context of REE-Dependent Methanol Oxidation Across 293K Genomes

This page summarises the Lanthanide Methylotrophy Atlas project. The project asked how widespread rare-earth-dependent methanol oxidation (xoxF) is compared with the calcium-dependent form (mxaF) across 293,059 GTDB-r214 genomes in the KBase Data Lakehouse. It also asked where these genes occur, how lanmodulin and pyrroloquinoline quinone (PQQ) biosynthesis genes fit in, and what rare-earth acid mine drainage genomes carry. The main answer is that xoxF is far more common than mxaF, and this holds under three phylogenetic corrections. [src: lanthanide_methylotrophy_atlas] The evidence is strong for the xoxF:mxaF ratio. It is weaker for the REE-impacted enrichment, which has n=37 and does not clear the FDR threshold. [src: lanthanide_methylotrophy_atlas] The rare-earth acid-mine-drainage MAG set also has only 37 genomes, and only 4/37 carry any xoxF. [src: lanthanide_methylotrophy_atlas]

## Key Findings

### xoxF dominates mxaF

xoxF was annotated in 3,690 genomes and mxaF in 195 genomes, from eggNOG KEGG ortholog (KO) K00114 for xoxF and K14028 for mxaF. [src: lanthanide_methylotrophy_atlas] The global ratio is 18.92 : 1 (Clopper-Pearson 95% confidence interval [13.07, 27.69]). [src: lanthanide_methylotrophy_atlas] A one-sided binomial test against the pre-registered H1 threshold (xoxF fraction > 10/11) gave p = 7.6 × 10⁻²². [src: lanthanide_methylotrophy_atlas]

The report concludes that H1 is robust to all three phylogenetic-correction frameworks. [src: lanthanide_methylotrophy_atlas] The first two estimates below are xoxF fractions. The third is a ratio.
- Naive pooled genome-level estimate, 3,885 units: 0.950, interval [0.942, 0.956]. [src: lanthanide_methylotrophy_atlas]
- Family-level equal-weight estimate, 271 units: 0.960, interval [0.941, 0.976]. [src: lanthanide_methylotrophy_atlas]
- Variational-Bayes binomial mixed model (GLMM) with random intercepts for phylum and family: a phylogeny-corrected ratio of ~143 : 1, 95% credible interval [122, 169]. [src: lanthanide_methylotrophy_atlas] The report attributes this strongest signal to random effects absorbing phylum-level heterogeneity. [src: lanthanide_methylotrophy_atlas]

After Benjamini-Hochberg false discovery rate (BH-FDR) correction across 29 testable phyla, the directional H1 verdict survives in every phylum with MDH calls and adequate sample size. [src: lanthanide_methylotrophy_atlas]

### Taxonomic pattern

The largest per-genome xoxF rates occur in phyla rarely linked to one-carbon metabolism in textbook accounts. [src: lanthanide_methylotrophy_atlas]
- Gemmatimonadota: 98 xoxF and 1 mxaF calls in 386 genomes (25.4 % xoxF rate). [src: lanthanide_methylotrophy_atlas]
- Pseudomonadota: 2,988 xoxF and 171 mxaF calls in 117,619 genomes (2.5 %, ratio 17.5 : 1). [src: lanthanide_methylotrophy_atlas]
- Verrucomicrobiota: 19 xoxF and 5 mxaF calls in 2,440 genomes (0.78 %, ratio 3.8 : 1). [src: lanthanide_methylotrophy_atlas]
- Beijerinckiaceae: 171 xoxF genomes in 508 genomes (33.7 %). [src: lanthanide_methylotrophy_atlas]
- Bacteroidota, Cyanobacteriota, Chloroflexota, Planctomycetota, Campylobacterota, Actinomycetota, Halobacteriota and Thermoproteota are xoxF-only, with zero mxaF. [src: lanthanide_methylotrophy_atlas]

### Environmental association

xoxF is enriched in soil and sediment genomes (xoxF rate 6.84 %, odds ratio 1.92 against generic environmental, p_BH 6.1 × 10⁻³⁹). Marine genomes show a smaller enrichment (4.76 %, OR 1.31, p_BH 7.8 × 10⁻⁷). Host-associated genomes are strongly depleted (0.22 %, OR 0.058). [src: lanthanide_methylotrophy_atlas] Volcanic/geothermal (OR 0.86, p_BH 0.20), mining (OR 1.12, p_BH 0.38) and methylotrophic (5 genomes, OR 8.70, p_BH 0.20) categories are not significant. [src: lanthanide_methylotrophy_atlas]

REE-impacted samples show a 3.5-fold descriptive elevation (10.8 % vs 3.7 % baseline). With n=37 they do not clear the FDR threshold (p_BH = 0.082). [src: lanthanide_methylotrophy_atlas] Within Acidobacteriota, soil-sediment enrichment survives (within-phylum OR=2.16, p_BH=2.2 × 10⁻⁵). This suggests part of the soil signal is not pure phylogenetic confounding. [src: lanthanide_methylotrophy_atlas]

### Lanmodulin

Bakta-validated lanmodulin is found in 62 genomes from 10 species. [src: lanthanide_methylotrophy_atlas] Clade restriction strongly supports H3a (one-sided binomial p = 9.8 × 10⁻⁷ against an 80 % threshold). [src: lanthanide_methylotrophy_atlas] H3b is not formally supported: xoxF co-occurrence is 49 / 62 = 79.0 %, just under the 80 % threshold (p = 0.65). [src: lanthanide_methylotrophy_atlas] Methylobacterium extorquens is the dominant carrier, with 22 genomes and one copy each. [src: lanthanide_methylotrophy_atlas]

### REE-acid-mine-drainage MAGs

The 37 metagenome-assembled genomes (MAGs) from REE-AMD river water are taxonomically diverse and not dominated by canonical methylotrophs. [src: lanthanide_methylotrophy_atlas] Only 4/37 carry any xoxF, and 0/37 carry bakta-validated lanmodulin or xoxJ. [src: lanthanide_methylotrophy_atlas] Their functional profile reads as acid-mine-drainage stress. Counts are MAGs out of 37: RecN 33, RecO 31, RecA 28, FtsH protease 31, MerR-family regulators 30, and thioredoxin reductase 25. [src: lanthanide_methylotrophy_atlas]

### PQQ cofactor support

The pilot exploration noted 2,320 xoxF-bearing genomes with no eggNOG PQQ-biosynthesis annotation. [src: lanthanide_methylotrophy_atlas] Complete eggNOG pqqA-E occurs in 33 genomes (0.9 % of the xoxF set). Bakta-only strong support (≥3 PQQ products) occurs in 899 genomes (24.4 %). Bakta-only partial support occurs in 389 genomes (10.5 %). [src: lanthanide_methylotrophy_atlas] Of 2,185 genomes with no eggNOG pqq, 1,288 (59 %) have ≥1 bakta PQQ product, which the report calls annotation gaps. [src: lanthanide_methylotrophy_atlas]

### Annotation-source choice

The report chooses the annotation source for each gene.
- Lanmodulin: bakta only. eggNOG Preferred_name='lanM' is noise (0 genomes called by both sources, 505 by eggNOG only, 62 by bakta only). [src: lanthanide_methylotrophy_atlas]
- xoxJ: bakta only, because KO K02030 is non-specific. [src: lanthanide_methylotrophy_atlas]
- mxaF: eggNOG K14028. [src: lanthanide_methylotrophy_atlas]
- pqqA-E: eggNOG primary, because bakta over-calls. [src: lanthanide_methylotrophy_atlas]

The eggNOG lanM false positives sit in unrelated gut Bacillota such as Streptococcus pneumoniae (10 genomes) and Blautia_A wexlerae (9 genomes). [src: lanthanide_methylotrophy_atlas] The report recommends using the bakta product field exclusively for lanmodulin work. [src: lanthanide_methylotrophy_atlas]

## Key Findings: xoxF (REE-dependent MDH) outnumbers mxaF (Ca-dependent MDH) by ~19:1 across …

This part of the report shows that xoxF is far more common than mxaF across GTDB-r214 genomes. [src: lanthanide_methylotrophy_atlas] H1 holds under three phylogenetic-correction frameworks. [src: lanthanide_methylotrophy_atlas] Lanmodulin is confined to the pre-specified methylotroph families, which supports H3a. [src: lanthanide_methylotrophy_atlas] Environmental enrichment is only partly supported (H2). [src: lanthanide_methylotrophy_atlas] See [[concepts/taxonomic-distribution-and-relative-prevalence-of-xoxf-and-mxaf-methanol-dehydrogenases]] for the wider context.

### Global xoxF versus mxaF

In eggNOG annotations, K00114 denotes xoxF (lanthanide-dependent methanol dehydrogenase, EC 1.1.2.8) and K14028 denotes mxaF (Ca-dependent methanol dehydrogenase, EC 1.1.2.7). [src: lanthanide_methylotrophy_atlas] Across 293,059 GTDB-r214 genomes, xoxF is annotated in 3,690 genomes and mxaF in 195. The global ratio is 18.92 : 1, with a Clopper-Pearson 95% confidence interval (CI) of [13.07, 27.69]. [src: lanthanide_methylotrophy_atlas] The xoxF fraction of joint MDH calls is 0.9498 [95% CI 0.9425, 0.9558]. [src: lanthanide_methylotrophy_atlas] A one-sided binomial test against the pre-registered H1 threshold (xoxF fraction > 10/11 ≈ 0.909) gives p = 7.6 × 10⁻²², so H1 is strongly supported. [src: lanthanide_methylotrophy_atlas]

After Benjamini-Hochberg false discovery rate (BH-FDR) correction across 29 testable phyla, the report says the direction of H1 survives in every phylum with MDH calls and adequate sample size. These include Pseudomonadota, Acidobacteriota, Actinomycetota, Bacteroidota, Campylobacterota, Verrucomicrobiota, Chloroflexota, Gemmatimonadota, Methylomirabilota, Halobacteriota and Thermoproteota. [src: lanthanide_methylotrophy_atlas] The report acknowledges that this per-phylum binomial framework does not formally control phylogenetic non-independence. [src: lanthanide_methylotrophy_atlas]

### Phylogenetic correction

The report concludes that H1 is robust to all three phylogenetic-correction frameworks. [src: lanthanide_methylotrophy_atlas] Each estimate is above the H1 threshold:

| Method | Units | xoxF fraction | Interval |
|---|---|---|---|
| NB03 naive pooled, genome level | 3,885 | 0.950 | [0.942, 0.956] [src: lanthanide_methylotrophy_atlas] |
| NB08 family-level equal weight | 271 | 0.960 | [0.941, 0.976] [src: lanthanide_methylotrophy_atlas] |
| NB08 Bayesian binomial GLMM, (1\|phylum) + (1\|family) | 3,885 | 0.993 | [0.992, 0.994] [src: lanthanide_methylotrophy_atlas] |

NB08 uses a variational-Bayes binomial GLMM (generalized linear mixed model) implemented with statsmodels.BinomialBayesMixedGLM. It has random intercepts for phylum and family. [src: lanthanide_methylotrophy_atlas] It gives a phylogeny-corrected ratio of ~143 : 1 with a 95% credible interval of [122, 169]. The report attributes this to random effects absorbing phylum-level heterogeneity, which reveals stronger dominance within typical phyla. [src: lanthanide_methylotrophy_atlas] The family-equal-weight bootstrap counts each of 271 MDH-informative families once. It confirms that H1 is not driven by Pseudomonadota's 117 K-genome size advantage. [src: lanthanide_methylotrophy_atlas]

### Taxonomic pattern

The report finds the biggest per-genome xoxF rates in phyla rarely linked to one-carbon metabolism in textbook accounts. [src: lanthanide_methylotrophy_atlas]

| Phylum | Genomes | xoxF | mxaF | xoxF rate | xoxF:mxaF | p_BH |
|---|---|---|---|---|---|---|
| Acidobacteriota | 1,006 | 285 | 3 | 28.3 % | 95 : 1 | 1.2 × 10⁻⁷⁹ [src: lanthanide_methylotrophy_atlas] |
| Gemmatimonadota | 386 | 98 | 1 | 25.4 % | 98 : 1 | 1.5 × 10⁻²⁷ [src: lanthanide_methylotrophy_atlas] |
| Methylomirabilota | 80 | 23 | 7 | 28.7 % | 3.3 : 1 | 0.011 [src: lanthanide_methylotrophy_atlas] |
| Pseudomonadota | 117,619 | 2,988 | 171 | 2.5 % | 17.5 : 1 | 0.0 [src: lanthanide_methylotrophy_atlas] |
| Verrucomicrobiota | 2,440 | 19 | 5 | 0.78 % | 3.8 : 1 | 0.015 [src: lanthanide_methylotrophy_atlas] |

Within Pseudomonadota, Pseudomonadaceae alone contributes 566 xoxF genomes versus 1 mxaF genome. [src: lanthanide_methylotrophy_atlas] Xanthobacteraceae (Bradyrhizobium) and Rhizobiaceae (Mesorhizobium) follow. [src: lanthanide_methylotrophy_atlas] Beijerinckiaceae has 171 xoxF genomes in 508 genomes, a 33.7 % rate. [src: lanthanide_methylotrophy_atlas] Hyphomicrobiaceae has 33 in 56, a 58.9 % rate. [src: lanthanide_methylotrophy_atlas] Several phyla are xoxF-only with zero mxaF: Bacteroidota, Cyanobacteriota, Chloroflexota, Planctomycetota, Campylobacterota, Actinomycetota, and the archaeal Halobacteriota and Thermoproteota. [src: lanthanide_methylotrophy_atlas]

### Lanmodulin

Lanmodulin is clade-restricted, but its co-occurrence with xoxF falls just short of the pre-registered threshold. Bakta-validated Lanmodulin is detected in 62 genomes representing 10 species. [src: lanthanide_methylotrophy_atlas] All 62 (100 %) fall within Beijerinckiaceae, Acetobacteraceae or Hyphomicrobiaceae, the three α-Proteobacterial methylotroph families pre-specified in H3. [src: lanthanide_methylotrophy_atlas] A one-sided binomial test against the 80 % threshold gives p = 9.8 × 10⁻⁷, so H3a is strongly supported. [src: lanthanide_methylotrophy_atlas]

Co-occurrence with xoxF from any source is 49 / 62 = 79.0 %, just under the 80 % threshold. The one-sided binomial p is 0.65, so H3b is not formally supported. [src: lanthanide_methylotrophy_atlas] The report suggests the 13 lanmodulin-without-xoxF genomes may reflect annotation incompleteness or genuine alternative lanthanide-handling pathways. Lanmodulin can bind REEs without being co-located with a lanthanide-MDH operon. [src: lanthanide_methylotrophy_atlas]

The dominant carrier is *Methylobacterium extorquens*, with 22 genomes and 1 lanmodulin copy each, so there is no paralog story. [src: lanthanide_methylotrophy_atlas] Other contributors are:

- an uncharacterised Acetobacteraceae genus, g__BOG-930, with 12 genomes [src: lanthanide_methylotrophy_atlas]
- *M. thiocyanatum*, with 6 [src: lanthanide_methylotrophy_atlas]
- *M. rhodesianum*, with 6 [src: lanthanide_methylotrophy_atlas]
- *M. aminovorans*, with 4 [src: lanthanide_methylotrophy_atlas]
- *Hyphomicrobium_B*, with 2 [src: lanthanide_methylotrophy_atlas]
- *Methylocella*, with 2 [src: lanthanide_methylotrophy_atlas]

### Environmental association

The report calls H2 partially supported. Soil/sediment is by far the strongest broad-class enrichment, which the report finds consistent with methanol oxidation as a known soil process and with soil lanthanide mineral reservoirs. [src: lanthanide_methylotrophy_atlas] The tests are per-class Fisher's exact tests of any_xoxF against the generic_environmental reference, with BH-FDR correction. [src: lanthanide_methylotrophy_atlas] The reference class has 21,538 genomes and an xoxF rate of 3.69 %. [src: lanthanide_methylotrophy_atlas]

| Class | Genomes | xoxF rate | OR vs reference | p_BH |
|---|---|---|---|---|
| soil_sediment | 13,779 | 6.84 % | 1.92 | 6.1 × 10⁻³⁹ [src: lanthanide_methylotrophy_atlas] |
| marine | 15,554 | 4.76 % | 1.31 | 7.8 × 10⁻⁷ [src: lanthanide_methylotrophy_atlas] |
| host_associated | 107,600 | 0.22 % | 0.058 | 0.0 [src: lanthanide_methylotrophy_atlas] |
| volcanic_geothermal | 3,450 | 3.19 % | 0.86 | 0.20 [src: lanthanide_methylotrophy_atlas] |
| mining | 1,636 | 4.10 % | 1.12 | 0.38 [src: lanthanide_methylotrophy_atlas] |
| ree_impacted | 37 | 10.81 % | 3.51 | 0.082 [src: lanthanide_methylotrophy_atlas] |
| methylotrophic | 5 | 20.0 % | 8.70 | 0.20 [src: lanthanide_methylotrophy_atlas] |

Volcanic_geothermal, mining and methylotrophic show no significant difference. [src: lanthanide_methylotrophy_atlas] REE-impacted samples show a 3.5-fold descriptive elevation (10.8 % versus a 3.7 % baseline). With n=37 this is too small to clear the FDR threshold. [src: lanthanide_methylotrophy_atlas] Host-associated environments are strongly depleted in xoxF, which the report reads as consistent with absent methylotrophy in the gut/host niche. [src: lanthanide_methylotrophy_atlas] Within Acidobacteriota, soil-sediment enrichment survives (within-phylum OR=2.16, p_BH=2.2 × 10⁻⁵). The report suggests that at least part of the broader soil signal is not pure phylogenetic confounding. [src: lanthanide_methylotrophy_atlas]

## Key Findings: REE-acid-mine-drainage MAGs are dominated by acidophiles, not methylotrophs

This part of the report shows that the 37 rare-earth-element acid-mine-drainage (REE-AMD) metagenome assembled genomes (MAGs) are taxonomically diverse and not dominated by canonical methylotrophs. Their functional signature reads as an acid-mine-drainage stress profile. [src: lanthanide_methylotrophy_atlas]

### Taxonomy and marker content of the REE-AMD MAGs

The 37 MAGs come from samples tagged as REE-AMD contaminated river water (BioSamples SAMN16745347-..., MIMAG.water.6.0 package). They are taxonomically diverse and not dominated by canonical methylotrophs. [src: lanthanide_methylotrophy_atlas] Acidophilic and metal-tolerant lineages lead the community: Acidocella, Acidiphilium, Thiomonas, Metallibacterium, several Burkholderiaceae_A/_B genera (Limnohabitans, Rhodoferax_A, Trinickia), Chitinophagaceae, Acidimicrobiia, Chloroflexota and Cyanobacteriota. [src: lanthanide_methylotrophy_atlas] A previously uncharacterised clade, f__REEB76 / g__REEB76, was discovered from these samples and named for them. [src: lanthanide_methylotrophy_atlas]

None of the 37 carries bakta-validated lanmodulin [src: lanthanide_methylotrophy_atlas] or bakta-validated xoxJ. [src: lanthanide_methylotrophy_atlas]

### Stress-response signature

The functional signature reads as a textbook acid-mine-drainage stress profile. The counts below are the number of MAGs, out of 37, in which each bakta product appears. [src: lanthanide_methylotrophy_atlas]

| Class | Bakta product | MAGs (of 37) |
|---|---|---|
| DNA repair | RecN | 33 [src: lanthanide_methylotrophy_atlas] |
| DNA repair | RadA | 32 [src: lanthanide_methylotrophy_atlas] |
| DNA repair | RecO | 31 [src: lanthanide_methylotrophy_atlas] |
| DNA repair | RecA | 28 [src: lanthanide_methylotrophy_atlas] |
| DNA repair | RadC | 24 [src: lanthanide_methylotrophy_atlas] |
| Acid resistance | FtsH zinc metalloprotease | 31 [src: lanthanide_methylotrophy_atlas] |
| Acid resistance | Proton-translocating NAD(P)+ transhydrogenase | 27 [src: lanthanide_methylotrophy_atlas] |
| Heavy-metal response | MerR-family regulators | 30 [src: lanthanide_methylotrophy_atlas] |
| Oxidative stress | Thioredoxin reductase | 25 [src: lanthanide_methylotrophy_atlas] |
| Oxidative stress | Glutathione peroxidase | 24 [src: lanthanide_methylotrophy_atlas] |

The case study is documented in notebook 06_ree_amd_case_study.ipynb. [src: lanthanide_methylotrophy_atlas] See also [[concepts/community-function-of-rare-earth-acid-mine-drainage-mags]].

### PQQ support in xoxF-bearing genomes

The pilot exploration found 2,320 xoxF-bearing genomes with no eggNOG PQQ-biosynthesis annotation, even though PQQ is an obligate XoxF cofactor. [src: lanthanide_methylotrophy_atlas] Notebook 07 cross-checks these genomes against PQQ matches in the bakta product field. [src: lanthanide_methylotrophy_atlas] The categories below are shares of the xoxF set.

| Category | Genomes | Share |
|---|---|---|
| Complete eggNOG pqqA-E | 33 | 0.9 % [src: lanthanide_methylotrophy_atlas] |
| Partial eggNOG pqq (1–4 of A-E) | 1,472 | 39.9 % [src: lanthanide_methylotrophy_atlas] |
| Bakta-only strong (≥3 PQQ products) | 899 | 24.4 % [src: lanthanide_methylotrophy_atlas] |
| Bakta-only partial (1–2 PQQ products) | 389 | 10.5 % [src: lanthanide_methylotrophy_atlas] |
| No PQQ detected by either source | 897 | 24.3 % [src: lanthanide_methylotrophy_atlas] |

Of 2,185 genomes with no eggNOG pqq, 1,288 (59 %) have at least one bakta PQQ product. The report calls these pure annotation gaps, where bakta detects PQQ that eggNOG misses. [src: lanthanide_methylotrophy_atlas]

The 897 genomes with no PQQ evidence from either source (24 % of xoxF carriers) are candidates for assembly incompleteness, pseudogenization or reliance on community-acquired PQQ. None of these explanations is established. [src: lanthanide_methylotrophy_atlas] Telling them apart needs sequence-level inspection, which is outside the report's scope. [src: lanthanide_methylotrophy_atlas] The analysis is in notebook 07_pqq_supply_asymmetry.ipynb. [src: lanthanide_methylotrophy_atlas] See [[concepts/pqq-cofactor-biosynthesis-support-in-xoxf-bearing-genomes]].

### Agreement between annotation sources

Agreement between eggNOG and bakta varies sharply by marker. The counts below are genomes in a 134,578-row hit-bearing matrix. [src: lanthanide_methylotrophy_atlas] See [[concepts/annotation-source-disagreement-and-coverage]].

| Marker | Both | eggNOG only | Bakta only | Source trusted |
|---|---|---|---|---|
| lanmodulin | 0 | 505 | 62 | bakta only, because eggNOG Preferred_name='lanM' is noise [src: lanthanide_methylotrophy_atlas] |
| xoxJ | 41 | 46,369 | 20 | bakta only, because KO (KEGG ortholog) K02030 is non-specific [src: lanthanide_methylotrophy_atlas] |
| xoxF | 418 | 3,272 | 1,402 | eggNOG K00114 as primary, bakta as union [src: lanthanide_methylotrophy_atlas] |
| mxaF | 4 | 191 | 8 | eggNOG K14028 [src: lanthanide_methylotrophy_atlas] |
| pqqA-E | varied | varied | 50–90K | eggNOG primary, because bakta over-calls [src: lanthanide_methylotrophy_atlas] |

The 505 eggNOG lanM false positives are concentrated in unrelated gut Bacillota, none of them lanthanide users. [src: lanthanide_methylotrophy_atlas] They include Streptococcus pneumoniae (10) [src: lanthanide_methylotrophy_atlas], Blautia_A wexlerae (9) [src: lanthanide_methylotrophy_atlas], Enterococcus faecalis (8) [src: lanthanide_methylotrophy_atlas], Ruminococcus_B gnavus (8) [src: lanthanide_methylotrophy_atlas] and Streptococcus pyogenes (7). [src: lanthanide_methylotrophy_atlas] In contrast, bakta product='Lanmodulin' matches 62 genomes, all in canonical α-Proteobacterial methylotroph clades. [src: lanthanide_methylotrophy_atlas] The report therefore recommends using the bakta product exclusively for lanmodulin work in the KBase Data Lakehouse pangenome. [src: lanthanide_methylotrophy_atlas] Marker-source calibration is in notebook 01_marker_calibration.ipynb. [src: lanthanide_methylotrophy_atlas] See also [[concepts/lanmodulin-clade-restriction-and-xoxf-co-occurrence]].

## Interpretation: What the data say

This part of the report interprets the pangenome survey. It treats the survey as the first quantitative test of the hypothesis that lanthanide-dependent methanol/ethanol oxidation has displaced the calcium-dependent canonical pathway across bacteria. The survey used the KBase Data Lakehouse pangenome of 293K genomes, which the report calls the largest annotated bacterial / archaeal collection assembled to date. [src: lanthanide_methylotrophy_atlas]

### xoxF dominance and taxonomic reach

The report calls the answer unambiguous. xoxF outnumbers mxaF by approximately 19 : 1, and the direction of the result survives BH-FDR (Benjamini-Hochberg false discovery rate) correction across phyla. [src: lanthanide_methylotrophy_atlas] Bacteroidota, Chloroflexota, Cyanobacteriota, Planctomycetota, Campylobacterota, Actinomycetota and archaea have zero mxaF annotations while carrying xoxF. [src: lanthanide_methylotrophy_atlas] See [[concepts/taxonomic-distribution-and-relative-prevalence-of-xoxf-and-mxaf-methanol-dehydrogenases]].

xoxF is enriched in canonical methylotroph families. The per-genome rate is 33.7 % in Beijerinckiaceae and 58.9 % in Hyphomicrobiaceae. [src: lanthanide_methylotrophy_atlas] The highest per-genome rates are in Acidobacteriota (28 %) and Gemmatimonadota (25 %), which the report notes are rarely cited in the methylotrophy literature. [src: lanthanide_methylotrophy_atlas] The report reads this as expanding the candidate set of free-living lanthanide-utilising organisms beyond classical methylotrophs. [src: lanthanide_methylotrophy_atlas] It places ~3,690 xoxF-bearing genomes across diverse phyla, including Acidobacteriota, Gemmatimonadota, Bacteroidota and archaea. [src: lanthanide_methylotrophy_atlas]

### Environmental context

The environmental xoxF signal is dominated by soil/sediment (OR, odds ratio, 1.92 for any-xoxF, p_BH=6×10⁻³⁹). The report contrasts this with the more spectacular volcanic and REE-mining environments that brought XoxF to attention. [src: lanthanide_methylotrophy_atlas] Soil typically contains 100–300 mg/kg total REE and is the natural habitat of the methylotroph families carrying the cassette. [src: lanthanide_methylotrophy_atlas] See [[concepts/environmental-association-of-lanthanide-dependent-methanol-oxidation-genes]].

The report calls this consistent with hostile, carbon-poor, low-pH water selecting for chemolithotrophic acidophiles. [src: lanthanide_methylotrophy_atlas] The REE-AMD enrichment (n=37, OR=3.51, p_BH=0.082) is descriptive-only at this sample size. A larger collection of explicitly REE-impacted metagenomes would test whether REE supply per se selects for the cassette. [src: lanthanide_methylotrophy_atlas] See [[concepts/community-function-of-rare-earth-acid-mine-drainage-mags]].

### Lanmodulin

Lanmodulin is restricted 100 % to Beijerinckiaceae / Acetobacteraceae / Hyphomicrobiaceae, in 62/62 genomes. [src: lanthanide_methylotrophy_atlas] The report concludes it is not a phylogenetically widespread REE handler, but only at this 62-genome resolution. [src: lanthanide_methylotrophy_atlas] xoxF and lanmodulin co-occur in 79 % of cases. [src: lanthanide_methylotrophy_atlas] The report suggests the mismatch in both directions means lanmodulin has binding/transport roles decoupled from methanol-oxidation operons. It also suggests some XoxF-bearing genomes handle REEs without lanmodulin's small-protein chelation pathway. [src: lanthanide_methylotrophy_atlas] See [[concepts/lanmodulin-clade-restriction-and-xoxf-co-occurrence]].

### PQQ and annotation sources

The report recommends that future PQQ (pyrroloquinoline quinone) work in the pangenome use the union of eggNOG and bakta sources. [src: lanthanide_methylotrophy_atlas] About 24 % of xoxF carriers have no PQQ evidence. These include candidates for assembly fragmentation, pseudogenization or community-PQQ acquisition. The report proposes sequence-level genome-quality filtering to discriminate among them. [src: lanthanide_methylotrophy_atlas]

Its calibration found that bakta's curated product field outperforms eggNOG's Preferred_name for specialty markers such as lanmodulin and XoxJ. The report calls this pattern generalizable beyond REE biology. [src: lanthanide_methylotrophy_atlas] eggNOG Preferred_name='lanM' returns 505 false positives in unrelated gut Bacillota. The report suggests the eggNOG seed-ortholog labelling for lanmodulin is stale or based on a propagated misannotation, and that it is worth reporting upstream. [src: lanthanide_methylotrophy_atlas] See [[concepts/annotation-source-disagreement-and-coverage]]. Bakta is described by Schwengers et al. (2021, Microbial Genomics), and eggNOG-mapper by Cantalapiedra et al. (2021, Mol Biol Evol). [src: lanthanide_methylotrophy_atlas]

### Relation to prior literature

- Pol et al. (2014, Nature) is the founding paper for lanthanide-dependent methanol dehydrogenase. It characterised XoxF in Methylacidiphilum fumariolicum SolV from a volcanic mudpot. [src: lanthanide_methylotrophy_atlas] The survey supports their assertion that XoxF is the more widespread enzyme. It extends the count from a handful of species to thousands of genomes spanning bacteria and archaea. [src: lanthanide_methylotrophy_atlas]
- Skovran & Martinez-Gomez (2015, Science) is a review establishing the lanthanide switch in Methylobacterium. [src: lanthanide_methylotrophy_atlas] The report finds xoxF in 102/209 Methylobacterium genomes and lanmodulin in 46/209. It calls both consistent with their model. [src: lanthanide_methylotrophy_atlas]
- Cotruvo et al. (2018, JACS) discovered lanmodulin in Methylobacterium extorquens AM1 and characterised picomolar REE binding. [src: lanthanide_methylotrophy_atlas] The report says its 100 % clade restriction at this scale tightens the restriction substantially compared to Cotruvo's small-scale survey. [src: lanthanide_methylotrophy_atlas]
- Picone & Op den Camp (2019, Curr Opin Biotechnol) reviewed REE-dependent enzymes. They noted XoxF distribution beyond cultured methylotrophs was an open question. [src: lanthanide_methylotrophy_atlas]
- Chistoserdova (2016, Curr Opin Microbiol) reviewed methylotroph diversity and hypothesised xoxF predominance from ~hundreds of genomes. The report says its 19 : 1 ratio at 293K genomes confirms this at substantially larger scale. [src: lanthanide_methylotrophy_atlas]
- Parks et al. (2022, Nat Biotechnol) describes GTDB r214, the taxonomic backbone of the pangenome. All H1/H2/H3 phylogenetic stratification uses GTDB phylum, class, family and genus assignments. [src: lanthanide_methylotrophy_atlas]

## Interpretation: Novel Contribution

This part of the report states what the atlas adds and what limits it. It describes the first pangenome-scale (293K-genome) atlas of the lanthanide-dependent methanol-oxidation cassette. [src: lanthanide_methylotrophy_atlas] It adds a numerical xoxF-dominance ratio, new xoxF-carrying phyla, a first description of rare-earth-element acid-mine-drainage (REE-AMD) metagenome-assembled genome (MAG) function, and a calibration of annotation sources. [src: lanthanide_methylotrophy_atlas]

### Novel contributions

**XoxF dominance.** The report presents a 19 : 1 global xoxF-dominance ratio, with 95% confidence interval (CI) [13.07, 27.69], as the first numerical answer at scale to how dominant xoxF is. [src: lanthanide_methylotrophy_atlas] For [[entities/xoxf-lanthanide-dependent-methanol-dehydrogenase]], the report ran three checks for phylogenetic non-independence of H1: a naive pooled analysis, a family-level equal-weight bootstrap, and a Bayesian binomial generalized linear mixed model (GLMM) with (1|phylum) + (1|family) random intercepts. [src: lanthanide_methylotrophy_atlas] All three confirm H1, with 95% CI lower bounds above the 10 : 1 threshold. [src: lanthanide_methylotrophy_atlas] The GLMM gives a phylogeny-corrected ratio of ~143 : 1. [src: lanthanide_methylotrophy_atlas] See [[concepts/taxonomic-distribution-and-relative-prevalence-of-xoxf-and-mxaf-methanol-dehydrogenases]].

**New xoxF carriers.** The report identifies high-rate xoxF carriers outside the methylotroph canon, in phyla rarely studied for lanthanide biology. These are Acidobacteriota (28 % carriage), Gemmatimonadota (25 %) and Methylomirabilota (29 %). [src: lanthanide_methylotrophy_atlas]

**REE-AMD MAGs.** The report gives the first descriptive characterization of community function for 37 MAGs from rare-earth-elements-acid-mine-drainage water. [src: lanthanide_methylotrophy_atlas] They are dominated by acidophilic metal-tolerant lineages (Acidocella, Acidiphilium, Thiomonas, Metallibacterium). [src: lanthanide_methylotrophy_atlas] They also include the previously uncharacterised f__REEB76 clade. [src: lanthanide_methylotrophy_atlas] See [[concepts/community-function-of-rare-earth-acid-mine-drainage-mags]].

**Lanmodulin.** Bakta-validated lanmodulin has a tight 100 % clade boundary. All 62 genomes fall in three α-Proteobacterial methylotroph families. [src: lanthanide_methylotrophy_atlas] See [[concepts/lanmodulin-clade-restriction-and-xoxf-co-occurrence]].

**Marker calibration.** In the KBase Data Lakehouse, eggNOG Preferred_name='lanM' is unusable, and KO (KEGG ortholog) K02030 is non-specific for xoxJ. [src: lanthanide_methylotrophy_atlas] The bakta product field is the trustworthy lanmodulin source. [src: lanthanide_methylotrophy_atlas] See [[concepts/annotation-source-disagreement-and-coverage]].

**PQQ paradox.** The report attributes 59 % of xoxF-without-PQQ (pyrroloquinoline quinone) cases to eggNOG annotation gaps that bakta detects. [src: lanthanide_methylotrophy_atlas] The remaining ~24 % of xoxF carriers genuinely lack PQQ evidence and are candidates for further investigation. [src: lanthanide_methylotrophy_atlas] See [[concepts/pqq-cofactor-biosynthesis-support-in-xoxf-bearing-genomes]].

### Limits

- **Phylogeny.** H2 still relies on within-phylum stratified analyses rather than a fully phylogeny-aware mixed model. Extending it would benefit from a higher-quality REE-impacted sample collection. [src: lanthanide_methylotrophy_atlas]
- **Annotation variance.** eggNOG and bakta calls disagree substantially for xoxJ, lanmodulin and PQQ biosynthesis. Headline statistics use a calibrated source of truth per marker, and secondary union-of-sources analyses are reported alongside. [src: lanthanide_methylotrophy_atlas]
- **REE-AMD anchor.** The anchor is small (n=37), comes from a single bioproject, and is descriptive only. Inferential environmental claims need a larger and more independent collection. [src: lanthanide_methylotrophy_atlas]
- **Coverage.** AlphaEarth coverage of xoxF genomes is 39.5 % (1,457 / 3,690), against a 28 % pangenome baseline. [src: lanthanide_methylotrophy_atlas] That leaves 60.5 % of xoxF carriers without environmental coordinates. [src: lanthanide_methylotrophy_atlas] Embedding-based niche analysis was scoped out, though a coverage-restricted supplementary analysis is feasible. [src: lanthanide_methylotrophy_atlas]
- **Environment labels.** The ncbi_env classification derives from text mining with hierarchical regex priorities. Its broad host_associated class includes gut, skin, oral and infection contexts. [src: lanthanide_methylotrophy_atlas] Misclassifications are possible, but the report states that soil/sediment enrichment and host depletion survive. [src: lanthanide_methylotrophy_atlas] See [[concepts/environmental-association-of-lanthanide-dependent-methanol-oxidation-genes]].
- **Sequence level.** xoxF and PQQ presence/absence is assessed at the gene-call level. The report does not screen for pseudogenes, truncated ORFs or assembly fragmentation. [src: lanthanide_methylotrophy_atlas]
- **Annotation bound.** The atlas is bounded by eggNOG and bakta annotations. It would not detect genuinely novel REE-handling enzymes that lack KEGG/RefSeq homologs. [src: lanthanide_methylotrophy_atlas]

## Data; Supporting Evidence

This part of the report lists the data sources and the derived data tables behind the atlas. The tables cover marker calls, taxonomic rollups, hypothesis tests (H1, H2, H3), the REE-AMD case study, PQQ supply and phylogenetic validation. The report also describes notebooks that carry out each analysis. [src: lanthanide_methylotrophy_atlas]

### Source tables

The atlas draws on the kbase_ke_pangenome tables eggnog_mapper_annotations, bakta_annotations, gene, gene_genecluster_junction, gene_cluster, genome, gtdb_taxonomy_r214v1 and ncbi_env. They supply per-genome marker calls (eggNOG and bakta), gene-to-genome mapping, GTDB taxonomy and environmental metadata. [src: lanthanide_methylotrophy_atlas]

The report also uses the kescience_bacdive tables culture_condition, strain and metabolite_utilization. DSMZ methylotroph media serve as a taxonomic anchor and as a check on BacDive's lanthanide and methanol coverage. [src: lanthanide_methylotrophy_atlas] That check found no lanthanide or methanol coverage in metabolite_utilization. [src: lanthanide_methylotrophy_atlas]

### Marker calibration tables

The marker matrix has 134,578 rows. It holds per-genome binary calls for xoxF, mxaF, xoxJ, pqqA-E and lanM, from eggNOG, bakta and either source, for genomes with at least one marker hit. [src: lanthanide_methylotrophy_atlas] A 9-row table gives eggNOG versus bakta concordance counts per marker. [src: lanthanide_methylotrophy_atlas]

Two tables bear on lanmodulin calls:
- 264 species-level taxa have an eggNOG Preferred_name='lanM' call but no bakta Lanmodulin call. The report treats these as the false-positive set. [src: lanthanide_methylotrophy_atlas]
- 10 species-level taxa have a bakta product='Lanmodulin' call. The report treats these as the trustworthy lanmodulin set. [src: lanthanide_methylotrophy_atlas]

The first notebook extracts the per-genome eggNOG and bakta markers and calibrates the source of truth. It also identifies the eggNOG lanM Preferred_name false positives. [src: lanthanide_methylotrophy_atlas]

### Taxonomic rollups and H1

The second notebook joins markers to full GTDB taxonomy, computes phylum, family and genus rollups and previews H1. [src: lanthanide_methylotrophy_atlas] The rollups have 142 rows at phylum level, about 3,000 at family level and about 12,000 at genus level. [src: lanthanide_methylotrophy_atlas]

The H1 tests compare xoxF with mxaF.
- The formal test uses BH-FDR (Benjamini-Hochberg false discovery rate) correction across phyla. It also gives a global ratio with 95% CI (confidence interval) and a one-sided binomial test against the 10:1 threshold. [src: lanthanide_methylotrophy_atlas]
- The per-phylum binomial tests with raw p-values have 29 rows. The BH-FDR-corrected version also has 29 rows. [src: lanthanide_methylotrophy_atlas]
- The global summary is a single row with the xoxF:mxaF ratio, its 95% CI and a binomial test against the H1 threshold. [src: lanthanide_methylotrophy_atlas]
- A drill-down of Pseudomonadota families with xoxF presence has 138 rows. [src: lanthanide_methylotrophy_atlas]
- A three-row validation table gives pooled, family-equal-weight and GLMM estimates, each with a 95% CI. [src: lanthanide_methylotrophy_atlas]

The validation notebook runs three methods: naive pooling, a family-level equal-weight bootstrap, and a Bayesian binomial GLMM with (1|phylum) + (1|family) random intercepts. The report says this closes the PGLS (phylogenetic generalized least squares) and PGLMM recommendation of its review. [src: lanthanide_methylotrophy_atlas]

### Environment and H2

The environment notebook classifies environments by text mining of ncbi_env. It runs per-class Fisher's exact tests on cassette presence and gives phylum-stratified breakdowns. [src: lanthanide_methylotrophy_atlas]
- The per-genome classification table has 293,059 rows, with cassette flags. [src: lanthanide_methylotrophy_atlas]
- Cassette-presence rates by environment class take 9 rows. [src: lanthanide_methylotrophy_atlas]
- The Fisher's exact test table has 70 rows. It tests each class against the generic_environmental reference, pooled and within the top 3 phyla, with BH-FDR correction. [src: lanthanide_methylotrophy_atlas]

### Lanmodulin H3

The H3 notebook runs a binomial test of H3a, clade restriction to Beijerinckiaceae, Acetobacteraceae and Hyphomicrobiaceae. It also runs the H3b test of xoxF co-occurrence. [src: lanthanide_methylotrophy_atlas] The results table has 2 rows. [src: lanthanide_methylotrophy_atlas] A 62-row table lists per-genome lanmodulin inventory with xoxF status and taxonomy. [src: lanthanide_methylotrophy_atlas]

### REE-AMD case study and PQQ supply

The case-study notebook describes the 37 REE-AMD MAGs (metagenome assembled genomes). It covers taxonomy, marker presence and top metal and stress-response products. [src: lanthanide_methylotrophy_atlas]
- The inventory table holds the 37 MAGs with the full marker matrix and taxonomy. [src: lanthanide_methylotrophy_atlas]
- A table of about 200 rows ranks metal-, acidophily- and REE-relevant bakta products by genome prevalence. [src: lanthanide_methylotrophy_atlas]

For PQQ (pyrroloquinoline quinone) supply, one notebook cross-checks about 2,300 xoxF-without-PQQ genomes against bakta PQQ products. It separates annotation gaps from genuine absence. [src: lanthanide_methylotrophy_atlas] The resulting table has 2,185 rows. It categorizes xoxF-bearing genomes that lack eggNOG PQQ as annotation gap or no-PQQ-detected. [src: lanthanide_methylotrophy_atlas]

## Future Directions

This part of the report lists seven proposed follow-up analyses. They address gaps in PQQ detection, environmental embedding analysis, REE-impacted sampling, an uncharacterised clade, wet-lab fitness tests, lanmodulin diversity and an annotation error. [src: lanthanide_methylotrophy_atlas]

### Sequence-level and environmental follow-ups

The report proposes sequence-level analysis of about 897 xoxF genomes with no PQQ detected. It would use per-genome ORF integrity and CheckM2 completeness scoring. The aim is to distinguish assembly fragmentation, pseudogenization and genuine community-PQQ acquisition. [src: lanthanide_methylotrophy_atlas]

AlphaEarth embedding coverage is 39.5 % in the xoxF genome set, above the pangenome baseline. [src: lanthanide_methylotrophy_atlas] The report proposes phylum-stratified PCA (principal component analysis) or UMAP (uniform manifold approximation and projection) of these embeddings. This would test whether xoxF-bearing organisms cluster in distinct biogeographic niches. [src: lanthanide_methylotrophy_atlas]

### REE-impacted samples and the REEB76 clade

The n=37 REE-AMD anchor is descriptive-only. [src: lanthanide_methylotrophy_atlas] The report proposes recruiting REE-mining tailings, leachate and bioreactor metagenomes from existing sequence archives. This would make the H2 REE-impacted signal inferential rather than descriptive. [src: lanthanide_methylotrophy_atlas]

The `f__REEB76` clade was discovered from REE-AMD samples and is uncharacterised. The report proposes studying its phylogenomic placement, predicted metabolism and any xoxF or lanmodulin presence. It calls this a high-novelty side study. [src: lanthanide_methylotrophy_atlas]

### Wet-lab and lanmodulin diversity

The report proposes targeted RB-TnSeq (random barcode transposon sequencing) with lanthanum and cerium chloride in the FitnessBrowser organism panel. This picks up the metal_fitness_atlas Priority 2 wet-lab proposal. [src: lanthanide_methylotrophy_atlas] Genome-wide gene fitness under La/Ce stress would identify the first transposon-validated REE-tolerance gene set. The target organisms are xoxF-carrying soil organisms such as *Pseudomonas putida*, *Cupriavidus* and *Sphingomonas*. [src: lanthanide_methylotrophy_atlas]

The report describes 22 *Methylobacterium extorquens* genomes with 1 lanmodulin copy each. [src: lanthanide_methylotrophy_atlas] It proposes multiple-sequence alignment of representative cluster proteins. This would test whether lanmodulin has diversified within a single operon-defined locus or is invariant across the species. [src: lanthanide_methylotrophy_atlas]

### Annotation error report

The report finds 505 eggNOG `Preferred_name='lanM'` false positives. They are concentrated in a handful of *Streptococcus*, *Blautia* and *Enterococcus* species among unrelated gut Bacillota. [src: lanthanide_methylotrophy_atlas] The report suggests this pattern likely reflects a single seed-ortholog label that has propagated. It proposes reporting the pattern to the eggNOG-mapper team for review. [src: lanthanide_methylotrophy_atlas]

## Caveats and Open Work

- The REE-impacted enrichment is descriptive only, because n=37 is too small to clear the FDR threshold. [src: lanthanide_methylotrophy_atlas]
- H3b falls just under its pre-registered threshold. [src: lanthanide_methylotrophy_atlas]
- 897 xoxF genomes (24 %) lack PQQ evidence from either source. The candidate explanations are assembly incompleteness, pseudogenization or reliance on community-acquired PQQ. Telling them apart needs sequence-level inspection, which the report leaves out of scope. [src: lanthanide_methylotrophy_atlas]
- Source choice matters. eggNOG lanM calls are false positives, and bakta over-calls pqqA-E. [src: lanthanide_methylotrophy_atlas]

## Slots Into

- [[concepts/taxonomic-distribution-and-relative-prevalence-of-xoxf-and-mxaf-methanol-dehydrogenases]]: the 18.92 : 1 ratio and the per-phylum rates. [src: lanthanide_methylotrophy_atlas]
- [[concepts/environmental-association-of-lanthanide-dependent-methanol-oxidation-genes]]: soil and marine enrichment and host-associated depletion. [src: lanthanide_methylotrophy_atlas]
- [[concepts/lanmodulin-clade-restriction-and-xoxf-co-occurrence]]: H3a supported and H3b not formally supported. [src: lanthanide_methylotrophy_atlas]
- [[concepts/pqq-cofactor-biosynthesis-support-in-xoxf-bearing-genomes]]: bakta recovers PQQ support that eggNOG misses. [src: lanthanide_methylotrophy_atlas]
- [[concepts/community-function-of-rare-earth-acid-mine-drainage-mags]]: the stress-response profile and the scarcity of xoxF. [src: lanthanide_methylotrophy_atlas]
- [[concepts/annotation-source-disagreement-and-coverage]]: the eggNOG and bakta disagreement for lanmodulin, xoxJ and pqqA-E. [src: lanthanide_methylotrophy_atlas]
