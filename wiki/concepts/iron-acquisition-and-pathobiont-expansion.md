---
type: "Concept"
description: "Evidence that iron and heme acquisition is the dominant Crohn's-disease-enriched functional theme in gut metagenomes and a genomically concentrated Escherichia coli specialization, together with the comparator, interaction-test, mouse and clinical limits on reading it as a uniform iron effect."
sources: ["summaries/ibd_phage_targeting__REPORT.md"]
---
# Iron and Heme Acquisition as a Convergent Pathobiont Signature

Across this project's Crohn's disease (CD) gut-metagenome analyses, iron and heme acquisition emerges as the strongest CD-enriched biochemical theme: it was reported as the dominant CD-up [[entities/metacyc]] class-enriched theme (OR=8.1, FDR 7e-6) and judged **causally consistent** with the broader IBD-iron literature, where OR is the odds ratio and FDR the false-discovery-rate-adjusted p value [src: ibd_phage_targeting]. The project's own report is summarized at [[summaries/ibd_phage_targeting__REPORT]], and the element itself at [[entities/iron]].

## Cohort-level pathway-theme enrichment

The cohort-level enrichment statistics are explicit for the theme **08_iron_heme_acquisition**: background 32 / 409, CD-up **15 / 52 (29 %)**, expected 4.07, odds ratio **8.11**, p = 5.8e-7 and **FDR = 7.4e-6**, computed by [[entities/fishers-exact-test]] (an exact test of enrichment in a 2x2 count table) [src: ibd_phage_targeting].

This **supports** reading iron as a specialization rather than a diffuse metabolic shift: the report states iron/heme acquisition is the dominant CD-up biochemical theme at 8.1x over background, "29 % of CD-up pathways vs 8 % expected", and that the 15 CD-up pathways in this theme include heme biosynthesis (PWY-5920, rho = 0.64 with *E. coli* in NB07a section c, where rho is a [[entities/spearman-correlation]] rank coefficient), heme degradation, and siderophore-related pathways [src: ibd_phage_targeting].

The underlying per-theme cohort-level Fisher enrichment table (`data/nb07_h3a_v18_cohort_enrichment.tsv`, 12 rows) records the iron/heme theme at OR=8.1, FDR 7e-6 [src: ibd_phage_targeting].

Seven displayed cohort-level themes did not meet the support criterion, which **refines** the claim by bounding it: the CD-up signal is not generic pathway inflation across all displayed themes [src: ibd_phage_targeting].

| theme | background | CD-up | expected | odds ratio | p | FDR | supported — all rows [src: ibd_phage_targeting] |
|---|---|---|---|---|---|---|---|
| 09_anaerobic_respiration | 50 | 8 | 6.36 | 1.36 | 0.29 | 1.0 | — |
| 02_mucin_glycan_host | 83 | 11 | 10.55 | 1.06 | 0.50 | 1.0 | — |
| 12_aromatic_AA_chorismate_indole | 22 | 3 | 2.80 | 1.09 | 0.55 | 1.0 | — |
| 10_fat_metabolism_glyoxylate | 111 | 13 | 14.11 | 0.88 | 0.70 | 1.0 | — |
| 07_AA_decarboxylation | 62 | 7 | 7.88 | 0.85 | 0.71 | 1.0 | — |
| 11_purine_pyrimidine_recycling | 78 | 7 | 9.92 | 0.63 | 0.91 | 1.0 | — |
| 06_polyamine_urea | 90 | 6 | 11.44 | 0.42 | 0.99 | 1.0 | — |

(Null-result table: anaerobic respiration, mucin/glycan, fat metabolism and purine/pyrimidine recycling among the themes with FDR 1.0 and no support mark [src: ibd_phage_targeting].)

## Genomic biosynthetic-gene-cluster evidence

The genomic side reports nominally far larger odds ratios than the cohort analysis, but on a comparator the report itself disowns, so it cannot be graded as the stronger evidence: BGC-theme Fisher enrichment of the Tier-A core set against the catalog background (`data/nb08a_bgc_theme_enrichment.tsv`, 4 rows) reports iron OR=44 and genotoxin OR=234 — BGC meaning biosynthetic gene cluster — while the report separately cautions that the iron comparator is unmatched, stating that the "Tier-A 'background' comparator is the full BGC catalog (10,060 BGCs across all species), not a matched comparator", that "The Fisher OR of 44x for iron_siderophore is partly inflated by the catalog-wide rarity of iron MIBiG matches (51 / 9,774 = 0.5 %)", and that "The 44x number should not be treated as a precise effect size, but the qualitative finding — *E. coli* alone among actionable Tier-A carries the iron-siderophore signature — is robust across choice of comparator" [src: ibd_phage_targeting]. This angle is developed further in [[concepts/pathobiont-biosynthetic-gene-cluster-repertoires]].

Per-species counts place essentially the whole genomic signal in one organism: the six-row table `data/nb08a_tier_a_iron_genotoxin_per_species.tsv` reports [[entities/escherichia-coli]] at 54 iron plus 25 genotoxin MIBiG matches (MIBiG being the curated reference catalog of characterized BGCs) and the other species at 0+0 [src: ibd_phage_targeting].

The named matches are concrete rather than category-level: Yersiniabactin and Enterobactin, both siderophores, were matched to *E. coli* MIBiG hits [src: ibd_phage_targeting].

The project's own verdict keeps the grading conservative: iron-siderophore OR=44 (E. coli only); genotoxin OR=234; ebf/ecf p<1e-31 across 4 cohorts — and yet the formal H3c verdict remained PARTIALLY SUPPORTED [src: ibd_phage_targeting]. The limitation behind that verdict is consequential rather than cosmetic: the report records that "the strict species x BGC interaction-term test specified in the original H3c is untested" (it "would require species-stratified per-sample BGC abundance, not in the current pre-computed mart slice"), that the per-species CD-up enrichment "is consistent with H3c but does not formally distinguish 'species x BGC interaction' from 'species main effect + BGC main effect'", and that the interaction-term test was "dropped per plan v1.9 as a structural project-scope limitation, not a deferred follow-up" [src: ibd_phage_targeting]. The main-effect evidence therefore does not establish that iron-BGC enrichment exceeds what species abundance alone would produce.

## Convergence across analytical granularities

The claim "AIEC iron-acquisition is the dominant CD pathobiont specialization" (AIEC = adherent-invasive *Escherichia coli*) is reported as supported from five independent evidence streams across three distinct analytical granularities: literature-MIBiG lookup, sample-level pathway x species correlation, cohort-level pathway-class enrichment, sample-level pathway x species co-variation, and genomic BGC content [src: ibd_phage_targeting].

The convergent but methodologically distinct items are enumerated as: (1) NB05 section 5g — *E. coli* MIBiG matches: **Yersiniabactin + Enterobactin** (both iron siderophores) + Colibactin (same pks pathogenicity island); (2) NB07a section c — top pathway-pathobiont attribution: heme biosynthesis to *E. coli* (rho = 0.640); (3) NB07 v1.8 H3a (b) — iron/heme is the dominant CD-up theme (OR = 8.11, FDR = 7e-6); (4) AIEC literature — Dalmasso 2021 (yersiniabactin), Prudent 2021 (LF82 IBC formation via yersiniabactin), Dogan 2014 (AIEC iron-pathway enrichment) all flag iron acquisition as central AIEC fitness mechanism [src: ibd_phage_targeting].

The report's interpretation is that **iron is not just a host nutrient but a pathobiont-selective resource, and CD pathobionts have systematically over-invested in iron-acquisition machinery** (siderophores, heme uptake, heme biosynthesis as a precursor for haem-containing iron uptake / regulation systems) [src: ibd_phage_targeting]. Because the genomic arm rests on a single organism, an admittedly unmatched comparator whose odds ratio the report says should not be read as a precise effect size, and an untested species x BGC interaction term, this is carried here as the hypothesis that iron availability selects for pathobiont expansion, not as an established mechanism [src: ibd_phage_targeting].

## Figures

`NB07_H3a_v18_class_enrichment.png` — NB07 v1.8 cohort-level Fisher enrichment bar chart (iron/heme dominant) plus a per-species per-theme heatmap [src: ibd_phage_targeting].

`NB07c_anchor_pathobiont_coupling.png` — 2-panel figure: anchor x pathobiont species rho heatmap (E1_CD top half / E3_CD bottom half) plus mean iron-pathway co-variation per pathobiont heatmap [src: ibd_phage_targeting].

## Tensions

The convergent association does **not** license a uniform "more iron, more pathobiont" rule. Ellermann 2020 (PMID 31179826) directly demonstrated that dietary iron variably modulates intestinal microbiota assembly in colitis-resistant and colitis-susceptible mice — [[entities/mus-musculus]]-model evidence of variable effects across those two colitis-susceptibility backgrounds, not a demonstrated uniform human effect [src: ibd_phage_targeting].

On the clinical side the report cautions that **oral iron supplementation can exacerbate disease activity in a subset of IBD patients** — a subset, not all patients, which is what a resource-selection mechanism with variable host context would predict and what any intervention reading must respect [src: ibd_phage_targeting].

## Cited external literature and its stated limits

- Dalmasso G et al. (2021). "Yersiniabactin siderophore of Crohn's disease-associated adherent-invasive Escherichia coli." *Int J Mol Sci* 22(7):3512. PMID: 33805299 — cited for yersiniabactin as a siderophore of Crohn's-associated AIEC [src: ibd_phage_targeting].
- Ellermann M et al. (2020). "Dietary iron variably modulates assembly of the intestinal microbiota in colitis-resistant and colitis-susceptible mice." *Gut Microbes* 12(1):1599794. PMID: 31179826 — variable, not uniform, effects of dietary iron on microbiota assembly across colitis-resistant and colitis-susceptible mice [src: ibd_phage_targeting].
- Buret AG et al. (2019). "Pathobiont release from dysbiotic gut microbiota biofilms in intestinal inflammatory diseases: a role for iron?" *J Biomed Sci* 26(1):1. PMID: 30602371 — this work raises, rather than settles in its title, a possible role for iron in pathobiont release from dysbiotic gut biofilms [src: ibd_phage_targeting].

## Open Directions

- Re-run the Tier-A BGC theme enrichment against the "matched-niche" pathobiont comparator the report proposes (gut Proteobacteria plus CD-associated Firmicutes at similar genome-assembly depth) instead of the full catalog background, since the report flags the iron comparator as unmatched and the OR partly inflated by catalog-wide rarity; this would close the gap between the strong cohort-level enrichment (OR=8.1, FDR 7e-6) and a genomic odds ratio the report says must not be read as a precise effect size [src: ibd_phage_targeting].
- Extend per-species iron/genotoxin MIBiG counting beyond the six species tabulated, where *E. coli* carries 54+25 and others 0+0, to establish whether the zero counts reflect genuine absence or a species list chosen around *E. coli* [src: ibd_phage_targeting].
- Separate the existing cross-sample result from the coupling claim it is often read as: the heme-biosynthesis-to-*E. coli* rho = 0.640 is a pathway x pathobiont attribution across samples, not demonstrated within-patient tracking, so a repeated-measures design on longitudinal cohorts is needed to test whether heme-pathway abundance follows *E. coli* within a patient over time and independently of CD status [src: ibd_phage_targeting].
- Acquire the species-stratified per-sample BGC abundance (from raw HUMAnN3 / antiSMASH outputs) that the untested species x BGC interaction-term test requires, since without it the enrichment cannot be distinguished from a species main effect plus a BGC main effect [src: ibd_phage_targeting].
- Stratify cohorts by documented oral iron supplementation and host inflammatory phenotype to test the subset-exacerbation caveat against the colitis-susceptible / colitis-resistant mouse result, which is the specific analysis that would convert the resource-selection hypothesis into a testable patient-stratification rule, linking to [[concepts/gut-microbiome-ecotypes-as-patient-strata]] [src: ibd_phage_targeting].
- Ask whether iron restriction alters the outcome of pathobiont-directed phage targeting, since the H3c verdict remained PARTIALLY SUPPORTED and the siderophore enrichment is *E. coli*-only; this ties the mechanism to intervention design in [[concepts/phage-therapy-evidence-translation]] [src: ibd_phage_targeting].
