---
type: "Summary"
description: "Summary of the project Fitness Cost of Antimicrobial Resistance Genes."
doc_type: "short"
full_text: "sources/amr_fitness_cost__REPORT.md"
---
# Fitness Cost of Antimicrobial Resistance Genes

This report asks whether antimicrobial resistance (AMR) genes impose a fitness cost in bacteria, using the Fitness Browser (FB) compendium of random barcode transposon sequencing (RB-TnSeq) data. Its main answer is that AMR knockouts have slightly higher fitness than other knockouts under non-antibiotic conditions, which the report reads as a small, consistent metabolic burden. The signal is consistent across organisms. The mechanism-level and conservation-level comparisons are null results. The report calls this the first pan-bacterial meta-analysis of AMR fitness costs using genome-wide transposon fitness data, built on 27M fitness measurements across 25 diverse bacteria. See [[concepts/fitness-cost-of-antimicrobial-resistance-genes]] for the wider topic. [src: amr_fitness_cost]

## Key Findings

### A small, consistent cost of resistance genes

AMR knockouts show higher fitness than non-AMR knockouts under non-antibiotic conditions, and the effect appears in every organism tested. [src: amr_fitness_cost] A DerSimonian-Laird random-effects meta-analysis (see [[entities/dersimonian-laird-random-effects-meta-analysis]]) across 25 organisms gives a pooled shift of +0.086 [95% confidence interval (CI): +0.074, +0.098], z = 14.3, p ~ 0. [src: amr_fitness_cost] All 25 of 25 organisms show a positive shift, which the report takes as evidence of universality. [src: amr_fitness_cost] The median per-organism Cohen's d is 0.18, which the report calls consistent with the literature prediction of +0.05 to +0.20 for costs after compensatory evolution. [src: amr_fitness_cost] Heterogeneity was moderate: I² was 54.3%, and Cochran's Q was 52.54 (p = 0.0007). [src: amr_fitness_cost] Per organism, 6 were nominally significant at p<0.05. Two were significant at false discovery rate (FDR) q<0.05: acidovorax_3H11 and Koxy. [src: amr_fitness_cost]

#### What the +0.086 means

The +0.086 is a relative effect. AMR knockouts are 0.086 fitness units less detrimental than the average gene knockout, so AMR genes are more dispensable than the typical gene. They are not absolutely beneficial to lose. [src: amr_fitness_cost] Absolute AMR knockout fitness averages −0.024, so AMR knockouts still grow slower than the pool average. The advantage is relative to a non-AMR background averaging around −0.11. [src: amr_fitness_cost] RB-TnSeq measures fitness relative to the pool average, not absolute fitness. [src: amr_fitness_cost] A one-sample Wilcoxon signed-rank test of AMR knockout fitness > 0 gave p = 0.999, so there is no support for AMR knockouts growing faster than the pool wildtype. [src: amr_fitness_cost] The relevant question is whether AMR knockouts are less costly than typical knockouts, which the per-organism Mann-Whitney design tests. [src: amr_fitness_cost]

The report interprets this as a small competitive advantage for a cell that loses an AMR gene instead of a random gene. It says this matters over evolutionary timescales but is invisible in short-term growth assays. [src: amr_fitness_cost] It argues that real but small costs reconcile resistance decline under stewardship with persistence long after antibiotic withdrawal. [src: amr_fitness_cost]

Only 4.6% of AMR genes were absent from the fitness matrices (putatively essential). The report compares this with a ~14% background essential rate from a prior analysis, `fitness_effects_conservation`, which used a different organism set. [src: amr_fitness_cost] The report reads this as consistent with AMR genes being more dispensable, and as arguing against strong right-censoring bias. [src: amr_fitness_cost] If the absent genes are the most costly AMR genes, the +0.086 estimate is a lower bound. [src: amr_fitness_cost] See [[concepts/essentiality-and-annotation-caveats-in-transposon-based-resistance-gene-fitness-analysis]].

The two annotation tiers gave the same result. Tier 1 (bakta_amr, N=110) and Tier 2 (keyword annotation, N=691) have indistinguishable fitness distributions (KS p = 0.17). [src: amr_fitness_cost] A Mann-Whitney U (MWU) test of T1 against T2 also found no difference (p = 0.26). [src: amr_fitness_cost]

### Antibiotic-dependent fitness flip

Under any antibiotic, 57% of AMR genes become relatively more important when knocked out than under non-antibiotic conditions (Wilcoxon signed-rank p = 0.0001, N = 797). [src: amr_fitness_cost] The mean flip is +0.045 (noabx − abx fitness), a shift from slight burden to slight importance. [src: amr_fitness_cost] The report notes that this analysis has much greater power than the class-matched one. [src: amr_fitness_cost] See [[concepts/antibiotic-dependent-fitness-flip-of-resistance-genes]].

The flip depends on mechanism, even though baseline cost does not. [src: amr_fitness_cost] Efflux genes show a stronger flip than enzymatic inactivation genes: +0.094 vs −0.001, MWU p = 0.007. [src: amr_fitness_cost] Broad-spectrum efflux pumps become significantly more important under any antibiotic, while narrow-spectrum enzymatic inactivation genes flip only under their matching antibiotic. [src: amr_fitness_cost] The report states that broad-spectrum mechanisms show stronger antibiotic-dependent importance than narrow-spectrum ones (MWU p = 0.007). [src: amr_fitness_cost] It explains this by saying broad-spectrum efflux pumps protect against many antibiotics. Narrow-spectrum enzymes such as beta-lactamases matter only with a matching antibiotic. [src: amr_fitness_cost] It suggests the 43% of genes that do not flip reflect narrow-spectrum resistance tested against non-matching antibiotics, not non-functional genes. [src: amr_fitness_cost]

The class-matched validation is a null result. It covers 157 gene-antibiotic pairs across 4 resistance classes. The mean flip is +0.113, but the Wilcoxon test is not significant (p = 0.14). [src: amr_fitness_cost] The report attributes this likely to small N per class and to heterogeneity across organisms. [src: amr_fitness_cost] The flip rate was 54.8% class-matched and 57.0% any-antibiotic. The mean flips were +0.113 and +0.045. [src: amr_fitness_cost] Within the class-matched set, chloramphenicol genes show the expected flip in 6/6 (100%) cases. Beta-lactam genes (105 pairs, 10 organisms) show a 50% flip rate, which the report considers consistent with many being tested against non-carbenicillin beta-lactams. [src: amr_fitness_cost]

### No difference in cost across mechanisms

Mechanism does not predict cost. Fitness costs do not differ across efflux (N=254), enzymatic inactivation (N=304), metal resistance (N=144) and unknown (N=74) groups (Kruskal-Wallis H = 0.65, p = 0.89). [src: amr_fitness_cost] The predicted ordering efflux > enzymatic > metal > unknown is not supported (Jonckheere-Terpstra z = 0.23, p = 0.41). [src: amr_fitness_cost] No pairwise comparison survives FDR correction. [src: amr_fitness_cost] Antibiotic-resistance and metal-resistance genes also do not differ (MWU p = 0.87). [src: amr_fitness_cost] See [[entities/metal-resistance-genes]].

The report hypothesizes that only AMR genes whose cost was minimized through compensatory evolution persist. [src: amr_fitness_cost] It notes that the RB-TnSeq organisms are lab-adapted strains with long evolutionary time to compensate. [src: amr_fitness_cost] It also proposes that the uniform cost may be a "floor", the irreducible overhead of maintaining any extra gene. [src: amr_fitness_cost] Similarly, it hypothesizes that +0.086 may be the irreducible cost after compensatory evolution: the minimum overhead of expressing a functional protein that gives no benefit without antibiotics. [src: amr_fitness_cost] It attributes the modest efflux cost shared with other mechanisms to compensation being a general outcome. [src: amr_fitness_cost]

### Core versus accessory genes

Core (intrinsic, N=638) and accessory (acquired, N=163) AMR genes have virtually identical fitness distributions: mean −0.024 vs −0.024, Cohen's d = 0.002, MWU p = 0.33. [src: amr_fitness_cost] See [[concepts/intrinsic-versus-acquired-resistance-gene-conservation]].

This null has a caveat. Most FB species have few genomes in GTDB (median 9, range 2–399), so the ≥95% prevalence threshold for "core" is imprecise. [src: amr_fitness_cost] With only 2–9 genomes, a gene present in all 9 could be accessory at larger sampling depth. [src: amr_fitness_cost] The report argues this imprecision should dilute a real difference, not create a false null. It therefore considers the null likely genuine, at least for well-sampled species: [[entities/klebsiella-michiganensis]] (399 genomes), [[entities/bacteroides-thetaiotaomicron]] (287) and [[entities/sinorhizobium-meliloti]] (241). [src: amr_fitness_cost]

The report offers a hypothesis for equal costs. Horizontal transfer may preferentially capture genes already cost-optimized in the donor lineage, or recipients may compensate rapidly. [src: amr_fitness_cost] It also reads identical core and accessory costs as consistent with rapid compensatory evolution, even for recently acquired genes. [src: amr_fitness_cost]

Mechanism does predict conservation. The association is strong (χ² = 69.3, p = 1.4×10⁻¹³, 6 groups). [src: amr_fitness_cost] Metal resistance genes are 44% accessory. Efflux (13%) and enzymatic inactivation (16%) genes are overwhelmingly core. [src: amr_fitness_cost] The report claims that mechanism predicting genomic location but not cost is a previously unobserved decoupling. [src: amr_fitness_cost] It suggests this decoupling means the forces governing retention, such as horizontal transfer frequency and environment-specific advantage, differ from those governing metabolic cost. [src: amr_fitness_cost] More specifically, it suggests conservation reflects how and when genes were acquired rather than how much they cost. [src: amr_fitness_cost] Efflux systems are often chromosomally encoded as part of general stress response and kept as core genes. Metal-resistance operons are frequently on mobile elements and remain accessory, but impose the same modest cost once established. [src: amr_fitness_cost]

### Relation to the literature

The report cites Melnyk et al. (2015), a meta-analysis of ~600 resistance-cost measurements that found costs in ~70% of cases and mean relative fitness 0.91–0.95 (5–9% cost). [src: amr_fitness_cost] Those are absolute differences between isogenic resistant and sensitive strains, whereas +0.086 is a relative AMR versus non-AMR knockout difference within pooled libraries, so the scales differ. [src: amr_fitness_cost] The report still reads both as converging on small single-digit percent costs. [src: amr_fitness_cost]

- Andersson & Hughes (2010) predicted that compensatory mutations reduce or eliminate costs, making reversal unlikely. [src: amr_fitness_cost]
- Levin, Perrot & Walker (2000) showed compensatory mutations arise faster than reversion, predicting resistance kept at reduced cost. [src: amr_fitness_cost]
- Vanacker, Lenuzza & Rasigade (2023) found in an *E. coli* meta-analysis that plasmid-borne resistance genes are less costly than chromosomal mutations. [src: amr_fitness_cost] The report proposes its modest estimate reflects many FB AMR genes being acquired determinants such as beta-lactamases and acetyltransferases, not costly target modifications. [src: amr_fitness_cost]
- Vogwill & MacLean (2015) found little systematic variation by mechanism after controlling for confounders, and stressed environment-dependence. [src: amr_fitness_cost]
- Olivares Pacheco & Alvarez (2017) showed *P. aeruginosa* efflux-pump costs are metabolic (proton motive force drain) and rapidly compensated by metabolic rewiring. [src: amr_fitness_cost]
- Durão, Balbontín & Gordo (2018) reviewed epistasis as a driver of cost variation. The report reads its signal across 25 organisms as suggesting robustness across genetic backgrounds. [src: amr_fitness_cost]
- Roux et al. (2015) showed resistance genes, especially efflux pumps, can be beneficial in vivo. The report cautions its in vitro cost may overestimate the ecological cost. [src: amr_fitness_cost]

## Data and Methods

Data assembly identified 1,352 AMR genes across 43 organisms (178 Tier 1, 1,174 Tier 2). [src: amr_fitness_cost] Tier 1 identification used bakta_amr and Tier 2 used keyword annotation. [src: amr_fitness_cost] The report used the KBase Data Lakehouse tables `bakta_amr` and `bakta_annotations` in `kbase_ke_pangenome` for AMR gene identification, and `genefitness`, `gene` and `experiment` in `kescience_fitnessbrowser` for fitness, gene metadata and experiment classification. [src: amr_fitness_cost] Cross-project inputs were `conservation_vs_fitness/fb_pangenome_link.tsv`, which bridges FB genes to pangenome clusters, and pre-cached matrices in `fitness_modules/matrices/*`. [src: amr_fitness_cost] 28 organisms had both AMR genes and fitness matrices, and 25 qualified for per-organism tests (≥5 AMR genes). [src: amr_fitness_cost] The report classified 6,804 experiments: 2,868 carbon/nitrogen, 1,862 stress, 727 standard, 447 metal and 443 antibiotic. [src: amr_fitness_cost] The class distribution lists beta-lactam (44 T1), mercury (27), arsenic (22) and efflux_rnd (22). [src: amr_fitness_cost]

## Caveats and Open Work

- The class-matched flip validation did not reach significance, probably because of small per-class samples and organism heterogeneity. [src: amr_fitness_cost] Only 4 AMR classes (beta-lactam, aminoglycoside, chloramphenicol, tetracycline) have matched antibiotic experiments, and macrolide, glycopeptide and polymyxin classes could not be validated. [src: amr_fitness_cost]
- The core/accessory null depends on imprecise core calls from few genomes per species (median 9), so it should be read cautiously for species with <20 genomes. [src: amr_fitness_cost]
- The organisms are lab-adapted, so costs may already be compensated. [src: amr_fitness_cost] All 25 are lab-adapted, so compensatory evolution during maintenance may mean natural-population costs are underestimated. [src: amr_fitness_cost]
- 86% of AMR genes are Tier 2 keyword matches from bakta annotations that may include non-AMR genes such as general efflux transporters. The Tier 1 sensitivity analysis gives consistent results, which mitigates this. [src: amr_fitness_cost]
- The Tier 2 classifier omits fosfomycin and tellurite resistance annotations, leaving ~25 genes in the "unknown" mechanism group. They could be reclassified as enzymatic_inactivation and metal_resistance respectively. [src: amr_fitness_cost]
- Transposon insertions can cause polar effects on downstream genes, which may confound fitness for AMR genes in operons. [src: amr_fitness_cost]
- Comparisons with isogenic-competition literature are reassuring but not direct equivalences. [src: amr_fitness_cost]
- The explanations (cost floor, donor optimization, compensatory evolution) are proposals, not measurements. [src: amr_fitness_cost]

### Next analyses the report proposes

- Test whether mechanism predicts cost within a single genetic background in organisms with many AMR genes (Cup4G11: 77, BFirm: 50), controlling for phylogenetic differences. [src: amr_fitness_cost]
- Distinguish narrow-spectrum drug pumps from general RND systems such as AcrAB-TolC, and test whether constitutively expressed efflux systems have lower costs. [src: amr_fitness_cost]
- Instead of averaging across all non-antibiotic experiments, test whether AMR costs vary under metal, osmotic and carbon-limitation stresses. [src: amr_fitness_cost]
- Cross-reference the 144 metal resistance genes with fitness data against the `metal_fitness_atlas` project, to test whether genes costly under standard conditions are protective under metal stress. [src: amr_fitness_cost]
- Scale the analysis from 25 FB organisms to all 293K KBase Data Lakehouse genomes by predicting AMR cost from gene-cluster conservation patterns. [src: amr_fitness_cost]
