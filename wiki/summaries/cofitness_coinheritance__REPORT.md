---
type: "Summary"
description: "Tests whether laboratory co-fitness predicts bacterial gene co-inheritance."
doc_type: "short"
full_text: "sources/cofitness_coinheritance__REPORT.md"
---
# Co-fitness and Co-inheritance in Bacterial Pangenomes

## Overview

This study tested whether laboratory-measured gene co-fitness predicts gene co-occurrence across bacterial pangenomes. It analyzed 2,253,491 cofit pairs against 22,534,910 prevalence-matched random pairs across 9 organisms with co-fitness data, and evaluated both pairwise relationships and coordinated multi-gene modules. Pairwise co-fitness showed a weak positive co-occurrence signal, whereas ICA (independent component analysis) modules—especially accessory modules—showed stronger co-inheritance. [src: cofitness_coinheritance]

## Key Findings

### Pairwise co-fitness weakly predicts co-occurrence

Across 9 organisms, cofit gene pairs had a mean delta phi (cofit minus random) of +0.011 across organisms; 7 of 9 organisms had positive effects and 8 of 9 were significant at p<0.05 by two-sided Mann-Whitney testing. The aggregate effect was delta=+0.003, with Mann-Whitney p=1.66e-29, while the Wilcoxon signed-rank test across organisms was not significant (W=9, p=0.13), indicating high inter-organism variance. [src: cofitness_coinheritance]

Organism-level deltas were Ddia6719 +0.093 (n cofit=16,957; mean phi cofit=0.182; random=0.089; p<1e-300), pseudo3_N2E3 +0.026 (31,959; 0.458; 0.433; p=6.6e-16), Phaeo +0.009 (14,728; 0.231; 0.222; p=6.5e-4), SyringaeB728a +0.006 (129,385; 0.049; 0.043; p=2.9e-4), Koxy +0.003 (162,160; 0.041; 0.038; p=3.3e-2), Smeli +0.002 (230,516; 0.029; 0.026; p<1e-17), Btheta +0.001 (242,676; 0.067; 0.067; p<1e-6), Putida -0.000 (205,323; 0.171; 0.171; p=0.41), and Korea -0.042 (7,994; 0.447; 0.489; p<1e-6). [src: cofitness_coinheritance]

Ddia6719 had the strongest signal despite being near-clonal at ANI 99.47%, retaining sufficient accessory-gene variation to detect co-inheritance. Korea’s negative delta was attributed to 95.2% of its cofit pairs having NaN phi because both genes were present in 100% of 72 genomes; only approximately 8,000 of 166,601 pairs were computable, so the negative value was interpreted as statistical noise rather than a biological signal. [src: cofitness_coinheritance]

### Operons are not a confound

Only 0.7% of cofit pairs were genomically adjacent within 5 genes, and excluding adjacent pairs did not change the result pattern. [src: cofitness_coinheritance]

### ICA modules show stronger co-inheritance

Across 195 ICA modules in 6 organisms, within-module co-occurrence had mean phi=0.229 versus a prevalence-matched null mean of 0.177 from 1000 permutations, for delta=+0.053. A total of 51/195 modules (26%) were significant at p<0.05, and 21/195 (11%) remained significant at q<0.05 after Benjamini-Hochberg FDR (false discovery rate) correction. [src: cofitness_coinheritance]

Accessory modules (<50% core) had mean delta phi +0.108, with 8/11 (73%) significant at p<0.05 and 4/11 (36%) significant at FDR q<0.05. Core modules (>90% core) had mean delta +0.059, with 29/120 (24%) significant at p<0.05 and 13/120 (11%) at q<0.05. Mixed modules (50–90%) had mean delta +0.031, with 14/64 (22%) significant at p<0.05 and 4/64 (6%) at q<0.05. The accessory-versus-core difference trended toward significance (Mann-Whitney p=0.051). [src: cofitness_coinheritance]

Per-organism module results were Koxy: 44 modules, 14 (32%) significant, mean phi=0.079, null mean=0.040; Btheta: 36, 22 (61%), 0.192, 0.086; Putida: 38, 6 (16%), 0.266, 0.202; Korea: 29, 0 (0%), 0.357, 0.308; Phaeo: 37, 3 (8%), 0.108, 0.095; and pseudo3_N2E3: 40, 4 (10%), 0.444, 0.409. Btheta showed the strongest module-level signal, while Korea had no significant modules because all Korea modules were >90% core with prevalence near 1.0. [src: cofitness_coinheritance]

The report interprets the stronger module-level result as evidence that coordinated regulation across multiple genes, rather than pairwise functional similarity alone, may more strongly constrain co-inheritance. It identifies the 48 accessory modules from the module_conservation project as functionally coherent units that travel together through the pangenome. [src: cofitness_coinheritance]

### Co-fitness strength and prevalence

Co-fitness strength weakly anti-correlated with co-occurrence: Spearman rho=-0.109, p<1e-300 across 1.04M pairs. The report attributes this pattern to a prevalence ceiling in which the strongest co-fitness pairs are often core genes with near-universal prevalence, leaving little variance for co-occurrence detection. [src: cofitness_coinheritance]

### Phylogenetic stratification

Cofit-pair phi was higher among near genomes (mean=0.102) than medium-distance genomes (mean=0.067), consistent with shared ancestry. Most species lacked genomes in the far stratum (>0.05 branch distance), limiting separation of functional coupling from phylogenetic signal. [src: cofitness_coinheritance]

### Functional categories

Among pairs in the top quartile for both phi and co-fitness, the most common SEED functional categories were Metabolism (15,936 genes), Transport (11,940), Regulation (6,339), Motility (2,929), Mobile elements (2,716), and DNA metabolism (2,490). [src: cofitness_coinheritance]

### Data extraction and analysis scope

The study initially targeted 11 species. Koxy had 399 genomes, 4,942 clusters, and 423,936 cofit pairs; Btheta 287, 4,649, and 328,455; Smeli 241, 6,004, and 528,699; RalstoniaUW163 141, 4,413, and 0; Putida 128, 5,409, and 458,688; SyringaeB728a 126, 4,999, and 371,004; Korea 72, 4,075, and 230,724; RalstoniaGMI1000 70, 4,723, and 0; Phaeo 43, 3,790, and 192,138; Ddia6719 66, 4,694, and 250,488; and pseudo3_N2E3 40, 5,513, and 507,828. All had phylogenetic trees except Phaeo and pseudo3_N2E3. [src: cofitness_coinheritance]

Ralstonia UW163 and Ralstonia GMI1000 were excluded from the primary analysis because they had zero co-fitness data in the Fitness Browser. Presence matrices were extracted by Spark from gene_genecluster_junction joined with gene; BROADCAST hints on small filter tables reduced query time to approximately 210s per organism. [src: cofitness_coinheritance]

For each organism, cofit pairs were mapped to pangenome cluster pairs using fb_pangenome_link.tsv, deduplicated, and evaluated with phi coefficients from binary genome-by-cluster presence vectors. Ten prevalence-matched random pairs were generated per cofit pair, matching each cluster’s prevalence independently within tolerance +/-5%; adjacency was defined as being within 5 loci on the same scaffold. [src: cofitness_coinheritance]

## Caveats and Open Directions

The prevalence ceiling limits interpretability because most Fitness Browser genes map to core clusters (>95% prevalence), where phi approaches 0 for both cofit and random pairs. The analysis is therefore most informative for species with substantial auxiliary gene content. [src: cofitness_coinheritance]

The two Ralstonia organisms were excluded despite being the most phylogenetically diverse and lowest-ANI organisms in the target set, removing species that might have been especially informative. [src: cofitness_coinheritance]

Phylogenetic control was limited: stratification was available for 7 of 9 organisms, and most species lacked genomes in the far stratum (>0.05 branch distance). The near-versus-medium difference of mean phi=0.102 versus 0.067 was consistent with shared ancestry, but the missing far stratum limited full disentanglement of functional and phylogenetic effects. [src: cofitness_coinheritance]

Pairwise co-fitness captures gene-pair relationships, whereas ICA modules capture multi-gene coordinated regulation and may better represent selective units constraining co-inheritance. [src: cofitness_coinheritance]

Near-clonal species behaved differently: Ddia6719 (ANI 99.47%) had delta=+0.093 and pseudo3_N2E3 (ANI 99.66%) had delta=+0.026. Both retained enough accessory variation to detect co-inheritance, but their high baseline phi values make absolute phi values less interpretable. [src: cofitness_coinheritance]

Proposed next analyses are to restrict comparisons to auxiliary-only pairs where both clusters are below 95% prevalence; calculate co-fitness directly from raw genefitness data for Ralstonia and other organisms lacking precomputed values; resolve reference-genome mapping for improved phylogenetic control; build module co-transfer networks and test cross-module prediction; and expand to species with >30% auxiliary genes and existing co-fitness data. [src: cofitness_coinheritance]

## Slots Into

- [[concepts/cofitness-network-architecture]] — Supports the conclusion that pairwise co-fitness weakly predicts pangenome co-occurrence, while multi-gene ICA modules show a stronger co-inheritance signal. [src: cofitness_coinheritance]
- [[concepts/pangenome-integration]] — Adds prevalence-matched pangenome presence/absence analysis linking Fitness Browser co-fitness to accessory and core gene co-occurrence. [src: cofitness_coinheritance]
- [[concepts/cross-tenant-data-bridging]] — Demonstrates integration of Fitness Browser, KBase pangenome, phylogenetic-distance, ICA-module, and SEED annotation datasets through Spark and linked files. [src: cofitness_coinheritance]
