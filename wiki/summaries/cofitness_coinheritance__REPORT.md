---
type: "Summary"
description: "Summary of the project Co-fitness and Co-inheritance in Bacterial Pangenomes."
doc_type: "short"
full_text: "sources/cofitness_coinheritance__REPORT.md"
---
# Co-fitness and Co-inheritance in Bacterial Pangenomes

This report asks whether gene pairs with correlated fitness (co-fitness, "cofit" pairs) tend to be inherited together across genomes in bacterial pangenomes. At the pair level the answer is a weak but consistent yes. The effect is small, and the test across organisms was not significant. [src: cofitness_coinheritance] A separate module-level analysis found within-module co-occurrence above a prevalence-matched null. [src: cofitness_coinheritance] That module signal was substantially stronger than the pairwise one, which the report reads as a sign that coordinated multi-gene regulation constrains co-inheritance more than pairwise similarity does. [src: cofitness_coinheritance]

## Key Findings

### Pairwise co-inheritance is weak but consistent

Co-fit gene pairs co-occur slightly more than prevalence-matched random pairs. The aggregate analysis covered 9 organisms, 2,253,491 cofit pairs and 22,534,910 random pairs. [src: cofitness_coinheritance] The report states that 7 of 9 organisms show a positive delta phi and that the aggregate signal is highly significant (p=1.66e-29). [src: cofitness_coinheritance] Overall mean phi (a co-occurrence coefficient) was 0.092 for cofit pairs and 0.089 for random pairs. [src: cofitness_coinheritance] Mean delta phi (cofit minus random) was +0.011 across organisms. Seven of 9 organisms were positive, and 8 of 9 were significant at p<0.05 (Mann-Whitney, two-sided). [src: cofitness_coinheritance] The aggregate delta was only +0.003 (Mann-Whitney p=1.66e-29). [src: cofitness_coinheritance] The report concludes that lab-measured functional coupling explains only a tiny fraction of co-inheritance patterns (delta=+0.003 overall, +0.011 mean across organisms). [src: cofitness_coinheritance] The Wilcoxon signed-rank test across organisms was not significant (W=9, p=0.13), which the report attributes to high inter-organism variance. [src: cofitness_coinheritance]

Per-organism results (cofit pairs, mean phi cofit vs random, delta, two-sided p):

- Ddia6719: 16,957 pairs, 0.182 vs 0.089, delta +0.093, p<1e-300. [src: cofitness_coinheritance]
- pseudo3_N2E3: 31,959 pairs, 0.458 vs 0.433, delta +0.026, p 6.6e-16. [src: cofitness_coinheritance]
- Phaeo: 14,728 pairs, 0.231 vs 0.222, delta +0.009, p 6.5e-4. [src: cofitness_coinheritance]
- SyringaeB728a: 129,385 pairs, 0.049 vs 0.043, delta +0.006, p 2.9e-4. [src: cofitness_coinheritance]
- Koxy: 162,160 pairs, 0.041 vs 0.038, delta +0.003, p 3.3e-2. [src: cofitness_coinheritance]
- Smeli: 230,516 pairs, 0.029 vs 0.026, delta +0.002, p <1e-17. [src: cofitness_coinheritance]
- Btheta: 242,676 pairs, 0.067 vs 0.067, delta +0.001, p <1e-6. [src: cofitness_coinheritance]
- Putida: 205,323 pairs, 0.171 vs 0.171, delta -0.000, p 0.41, so no difference. [src: cofitness_coinheritance]
- Korea: 7,994 pairs, 0.447 vs 0.489, delta -0.042, p <1e-6. [src: cofitness_coinheritance]

Ddia6719 had the strongest signal. The report says it kept enough accessory gene variation to detect co-inheritance, even though it is near-clonal (ANI, average nucleotide identity, 99.47%). [src: cofitness_coinheritance] pseudo3_N2E3 (ANI 99.66%) also shows a positive delta (+0.026). [src: cofitness_coinheritance] The report says that Ddia6719 and pseudo3_N2E3, which have more gene-content diversity, show the largest positive deltas. [src: cofitness_coinheritance] Despite low overall genome diversity, these species have sufficient accessory-gene variation to detect co-inheritance. [src: cofitness_coinheritance] The high baseline phi in these two species makes their absolute phi values less interpretable. [src: cofitness_coinheritance]

Korea's negative delta is attributed to noise. 95.2% of its cofit pairs had NaN (not a number) phi, because both genes were present in all 72 genomes, which gives zero-variance vectors. [src: cofitness_coinheritance] Only ~8,000 of 166,601 Korea pairs were computable. The report attributes the negative delta to statistical noise, not biology. [src: cofitness_coinheritance] Only 0.7% of cofit pairs were genomically adjacent (within 5 genes), and excluding them did not change the pattern. [src: cofitness_coinheritance]

The report explains the attenuated pairwise signal as a prevalence ceiling. Most Fitness Browser genes map to core clusters (>95% prevalence), where phi approaches 0 for both cofit and random pairs because there is almost no variance to correlate. [src: cofitness_coinheritance] The report says the analysis is most informative for species with substantial auxiliary gene content. [src: cofitness_coinheritance]

### Module-level co-occurrence

Across 6 organisms, 195 ICA (independent component analysis) modules had within-module mean phi=0.229. The prevalence-matched null (1000 permutations) gave mean phi=0.177, so delta=+0.053. Of the modules, 51/195 (26%) were significant at p<0.05. [src: cofitness_coinheritance] After Benjamini-Hochberg false discovery rate (FDR) correction, 21/195 (11%) stayed significant at q<0.05. [src: cofitness_coinheritance]

Accessory modules had the highest mean delta phi, though the sample is small (n=11). The accessory-versus-core difference only trended toward significance (Mann-Whitney p=0.051). [src: cofitness_coinheritance] The report highlights accessory modules as showing particularly strong co-inheritance (73% significant, 36% after FDR). [src: cofitness_coinheritance]

- Accessory (<50% core), n=11: mean delta phi +0.108, 8/11 (73%) significant at p<0.05, 4/11 (36%) at FDR q<0.05. [src: cofitness_coinheritance]
- Core (>90% core), n=120: mean delta phi +0.059, 29/120 (24%) at p<0.05, 13/120 (11%) at FDR q<0.05. [src: cofitness_coinheritance]
- Mixed (50-90% core), n=64: mean delta phi +0.031, 14/64 (22%) at p<0.05, 4/64 (6%) at FDR q<0.05. [src: cofitness_coinheritance]

Per-organism module results (modules, significant, mean phi, null mean):

- Koxy: 44 modules, 14 (32%), 0.079 vs 0.040. [src: cofitness_coinheritance]
- Btheta: 36 modules, 22 (61%), 0.192 vs 0.086. [src: cofitness_coinheritance]
- Putida: 38 modules, 6 (16%), 0.266 vs 0.202. [src: cofitness_coinheritance]
- Korea: 29 modules, 0 (0%), 0.357 vs 0.308. [src: cofitness_coinheritance]
- Phaeo: 37 modules, 3 (8%), 0.108 vs 0.095. [src: cofitness_coinheritance]
- pseudo3_N2E3: 40 modules, 4 (10%), 0.444 vs 0.409. [src: cofitness_coinheritance]

Btheta had the strongest module-level signal. [src: cofitness_coinheritance] Korea was the best pairwise organism in the report's wording, yet it had no significant modules. All its modules are >90% core with prevalence near 1.0. [src: cofitness_coinheritance]

The report suggests that coordinated regulation across multiple genes, not just pairwise functional similarity, most strongly constrains co-inheritance. [src: cofitness_coinheritance] It frames the contrast this way: co-fitness captures pairwise relationships, while ICA modules capture multi-gene coordinated regulation that may better reflect the selective units that constrain co-inheritance. This is an interpretation, not a tested result. [src: cofitness_coinheritance] It describes the 48 accessory modules from the module_conservation project as functionally coherent units that travel together through the pangenome. [src: cofitness_coinheritance]

### Co-fitness strength and phylogeny

Stronger co-fitness weakly predicted lower phi (Spearman rho=-0.109, p<1e-300, across 1.04M pairs). [src: cofitness_coinheritance] The report suggests a prevalence ceiling effect. The strongest co-fitness pairs are core genes with near-universal prevalence, which leaves little variance for co-occurrence detection. [src: cofitness_coinheritance]

Cofit pair phi was higher among near genomes (mean=0.102) than medium genomes (mean=0.067), as expected from shared ancestry. [src: cofitness_coinheritance] Most species had no genomes in the far stratum (>0.05 branch distance). This limits how well functional coupling can be separated from phylogenetic signal. [src: cofitness_coinheritance]

### Functions of high-phi, high-cofit pairs

Among pairs in the top quartile of both phi and co-fitness, the most common SEED categories by gene count were Metabolism (15,936), Transport (11,940), Regulation (6,339), Motility (2,929), Mobile elements (2,716) and DNA (deoxyribonucleic acid) metabolism (2,490). [src: cofitness_coinheritance]

### Relation to published work

The report places its results against four papers. Whelan et al. (2020) developed Coinfinder to detect pangenome gene associations while controlling for phylogeny. The report extends this by asking whether fitness-measured coupling predicts those associations (PMID: 32100706). [src: cofitness_coinheritance] Hall et al. (2021) found that E. coli accessory genes co-occur by function and via mobile genetic elements, which the report says is consistent with its module-level result (PMID: 34499026). [src: cofitness_coinheritance] Choudhury et al. (2025) showed that P. aeruginosa phylogroups have distinct co-occurrence networks, reinforcing that accessory-genome structure is lineage-specific (PMID: 40304385). [src: cofitness_coinheritance] Price et al. (2018) established the Fitness Browser co-fitness data used here, and co-fitness identifies genes in the same pathway or complex (PMID: 29769716). [src: cofitness_coinheritance]

## Data and Methods

The report analyzed 11 target species. Presence matrices were extracted with Spark by joining two billion-row tables, gene_genecluster_junction and gene. [src: cofitness_coinheritance] BROADCAST hints on small filter tables cut query time to ~210s per organism. [src: cofitness_coinheritance] Co-fitness came from the top-20 co-fitness partners per gene in the Fitness Browser cofit table, and pairwise genome distances came from the phylogenetic_tree_distance_pairs table. [src: cofitness_coinheritance] Gene-to-cluster mapping used a link table of 177K links. [src: cofitness_coinheritance]

Extracted datasets (genomes, clusters, cofit pairs, tree):

- Koxy: 399, 4,942, 423,936, tree. [src: cofitness_coinheritance]
- Btheta: 287, 4,649, 328,455, tree. [src: cofitness_coinheritance]
- Smeli: 241, 6,004, 528,699, tree. [src: cofitness_coinheritance]
- RalstoniaUW163: 141, 4,413, 0, tree. [src: cofitness_coinheritance]
- Putida: 128, 5,409, 458,688, tree. [src: cofitness_coinheritance]
- SyringaeB728a: 126, 4,999, 371,004, tree. [src: cofitness_coinheritance]
- Korea: 72, 4,075, 230,724, tree. [src: cofitness_coinheritance]
- RalstoniaGMI1000: 70, 4,723, 0, tree. [src: cofitness_coinheritance]
- Ddia6719: 66, 4,694, 250,488, tree. [src: cofitness_coinheritance]
- Phaeo: 43, 3,790, 192,138, no tree. [src: cofitness_coinheritance]
- pseudo3_N2E3: 40, 5,513, 507,828, no tree. [src: cofitness_coinheritance]

The pairwise method mapped cofit pairs to pangenome cluster pairs with fb_pangenome_link.tsv, deduplicated them, and computed phi from binary genome-by-cluster presence vectors. [src: cofitness_coinheritance] The null used 10 random pairs per cofit pair, matching each cluster's prevalence independently (tolerance +/-5%). [src: cofitness_coinheritance] Adjacency came from FB (Fitness Browser) gene coordinates, as within 5 loci on the same scaffold. [src: cofitness_coinheritance] The module method covered 6 organisms (Koxy, Btheta, Putida, Korea, Phaeo, pseudo3_N2E3). It compared within-module mean pairwise phi with 1000 prevalence-matched random gene sets and applied Benjamini-Hochberg FDR correction. [src: cofitness_coinheritance]

## Caveats and Open Work

Ralstonia UW163 and GMI1000 were excluded from the primary analysis. They have zero co-fitness data in the Fitness Browser despite appearing in its organism table. [src: cofitness_coinheritance] The report notes that these two organisms, the most phylogenetically diverse with the lowest ANI, would likely have been the most informative. [src: cofitness_coinheritance] Phylogenetic distance stratification was computed for 7 of 9 organisms, and the missing far stratum means functional coupling cannot be fully separated from phylogenetic signal. [src: cofitness_coinheritance] Other limits sit next to the results above: the Korea artifact, the small overall effect, the non-significant cross-organism test, and the prevalence ceiling. [src: cofitness_coinheritance]

The report proposes these next steps:

- Re-analyze using only gene pairs where both clusters are auxiliary (<95% prevalence), to maximize presence/absence variance. [src: cofitness_coinheritance]
- Calculate pairwise Pearson correlations from raw genefitness data for Ralstonia and other organisms lacking pre-computed co-fitness. [src: cofitness_coinheritance]
- Resolve the reference-genome mapping to enable phylogenetic distance stratification. [src: cofitness_coinheritance]
- Build module co-transfer networks across species and test whether co-fitness predicts cross-module co-inheritance. [src: cofitness_coinheritance]
- Target additional organisms with >30% auxiliary genes and existing co-fitness data. [src: cofitness_coinheritance]

## Slots Into

- [[concepts/co-fitness-as-a-predictor-of-gene-co-inheritance-in-pangenomes]]: the pairwise delta is small but mostly positive across organisms (7 of 9), and a separate module analysis also finds above-null co-occurrence. [src: cofitness_coinheritance]
- [[concepts/core-gene-prevalence-ceiling-on-co-occurrence-signal]]: Korea's zero-variance pairs, the negative co-fitness-phi correlation and the >95% prevalence of most mapped genes fit a prevalence ceiling. [src: cofitness_coinheritance]
- [[concepts/phylogenetic-confounding-of-gene-co-occurrence]]: phi is higher among near genomes, and far genomes are mostly missing. [src: cofitness_coinheritance]
- [[concepts/conservation-of-cofitness-modules-across-genomes-and-organisms]]: ICA modules show within-module co-occurrence above the null, and accessory modules had the highest mean delta phi (+0.108) versus core (+0.059) and mixed (+0.031). [src: cofitness_coinheritance]
