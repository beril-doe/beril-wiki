---
type: "Summary"
description: "Summary of the cofitness_coinheritance project, which tested whether Fitness Browser gene co-fitness predicts gene co-occurrence across bacterial pangenomes at pairwise and ICA-module levels."
doc_type: "short"
full_text: "sources/cofitness_coinheritance__REPORT.md"
---
# Co-fitness and Co-inheritance in Bacterial Pangenomes

## Overview

This study tested whether laboratory-measured gene co-fitness predicts gene co-occurrence across bacterial pangenomes. It analyzed 2,253,491 cofit pairs against 22,534,910 prevalence-matched random pairs across 9 organisms with co-fitness data. Co-occurrence was scored with phi coefficients, a correlation measure for binary presence/absence vectors. The study evaluated both pairwise relationships and coordinated multi-gene modules. Pairwise co-fitness showed a weak positive co-occurrence signal, whereas ICA (independent component analysis) modules, especially accessory modules, showed stronger co-inheritance. [src: cofitness_coinheritance]

## Key Findings

### Pairwise co-fitness weakly predicts co-occurrence

Across 9 organisms, cofit gene pairs had a mean delta phi (cofit minus random) of +0.011 across organisms. 7 of 9 organisms had positive effects, and 8 of 9 were significant at p<0.05 by two-sided Mann-Whitney testing. The aggregate effect was delta=+0.003, with Mann-Whitney p=1.66e-29. The Wilcoxon signed-rank test across organisms was not significant (W=9, p=0.13), indicating high inter-organism variance. [src: cofitness_coinheritance]

In the aggregate statistics, overall mean phi was 0.092 for cofit pairs and 0.089 for random pairs. The organism-level Wilcoxon signed-rank test of delta > 0 gave W=9, p=0.13, a null result at the across-organism level. [src: cofitness_coinheritance]

Organism-level deltas were as follows:
- Ddia6719: +0.093 (n cofit=16,957; mean phi cofit=0.182; random=0.089; p<1e-300).
- pseudo3_N2E3: +0.026 (31,959; 0.458; 0.433; p=6.6e-16).
- Phaeo: +0.009 (14,728; 0.231; 0.222; p=6.5e-4).
- SyringaeB728a: +0.006 (129,385; 0.049; 0.043; p=2.9e-4).
- Koxy: +0.003 (162,160; 0.041; 0.038; p=3.3e-2).
- Smeli: +0.002 (230,516; 0.029; 0.026; p<1e-17).
- Btheta: +0.001 (242,676; 0.067; 0.067; p<1e-6).
- Putida: -0.000 (205,323; 0.171; 0.171; p=0.41), so Putida showed no significant pairwise difference.
- Korea: -0.042 (7,994; 0.447; 0.489; p<1e-6). [src: cofitness_coinheritance]

Ddia6719 had the strongest signal despite being near-clonal at ANI (average nucleotide identity) 99.47%. The report attributes this to sufficient accessory-gene variation to detect co-inheritance. Korea's negative delta of -0.042 was attributed to 95.2% of its cofit pairs having NaN phi, because both genes were present in 100% of 72 genomes and produced zero-variance vectors. Only approximately 8,000 of 166,601 pairs were computable, so the report interprets the negative value as statistical noise in a small effective sample rather than a biological signal. [src: cofitness_coinheritance]

### Operons are not a confound

Only 0.7% of cofit pairs were genomically adjacent within 5 genes, and excluding adjacent pairs did not change the result pattern. [src: cofitness_coinheritance]

### ICA modules show stronger co-inheritance

Across 195 ICA modules in 6 organisms, within-module co-occurrence had mean phi=0.229. The prevalence-matched null mean was 0.177 from 1000 permutations, giving delta=+0.053. A total of 51/195 modules (26%) were significant at p<0.05, and 21/195 (11%) remained significant at q<0.05 after Benjamini-Hochberg FDR (false discovery rate) correction. [src: cofitness_coinheritance]

Results by module type:
- Accessory modules (<50% core) had mean delta phi +0.108, with 8/11 (73%) significant at p<0.05 and 4/11 (36%) significant at FDR q<0.05.
- Core modules (>90% core) had mean delta +0.059, with 29/120 (24%) significant at p<0.05 and 13/120 (11%) at q<0.05.
- Mixed modules (50–90%) had mean delta +0.031, with 14/64 (22%) significant at p<0.05 and 4/64 (6%) at q<0.05. [src: cofitness_coinheritance]

The accessory-versus-core difference only trended toward significance (Mann-Whitney p=0.051) and does not meet a p<0.05 threshold. [src: cofitness_coinheritance]

The module analysis covered the 6 organisms with ICA module data: Koxy, Btheta, Putida, Korea, Phaeo and pseudo3_N2E3. For each module, mean pairwise phi was computed within the module and compared to 1000 prevalence-matched random gene sets. P-values were corrected for multiple testing with Benjamini-Hochberg FDR. [src: cofitness_coinheritance]

The report's per-organism module table gives the following results. Koxy had 44 modules, 14 (32%) significant, with mean phi 0.079 against a null mean of 0.040. Btheta had 36 modules, 22 (61%) significant, 0.192 against 0.086. Putida had 38, 6 (16%), 0.266 against 0.202. Korea had 29, 0 (0%), 0.357 against 0.308. Phaeo had 37, 3 (8%), 0.108 against 0.095. pseudo3_N2E3 had 40, 4 (10%), 0.444 against 0.409. The module and significant-module counts in this table do not add up to the headline totals of 195 modules and 51 significant modules. The report does not explain the discrepancy, so it remains unresolved, and the per-organism and headline counts should not be treated as interchangeable. [src: cofitness_coinheritance]

Btheta showed the strongest module-level signal. Korea had no significant modules, which the report explains by all Korea modules being >90% core with prevalence near 1.0. The same passage calls Korea "the best pairwise organism". That label conflicts with Korea's negative pairwise delta of -0.042 and with the report's own reading of that delta as noise. The source leaves this inconsistency unresolved. [src: cofitness_coinheritance]

The report reads the stronger module-level result as suggesting that coordinated regulation across multiple genes most strongly constrains co-inheritance, more than pairwise functional similarity alone. This is an interpretation, not a separately measured result. The report also asserts that the 48 accessory modules from the module_conservation project are functionally coherent units that travel together through the pangenome. That assertion is an attributed cross-project interpretation, not a result shown independently by this project's analyses. [src: cofitness_coinheritance]

### Co-fitness strength and prevalence

Co-fitness strength weakly anti-correlated with co-occurrence: Spearman rho=-0.109, p<1e-300 across 1.04M pairs. The report suggests a prevalence ceiling as the explanation. In this view, the strongest co-fitness pairs are often core genes with near-universal prevalence, which leaves little variance for detecting co-occurrence. This explanation is interpretive. [src: cofitness_coinheritance]

### Phylogenetic stratification

Cofit-pair phi was higher among near genomes (mean=0.102) than among medium-distance genomes (mean=0.067), consistent with shared ancestry. Most species lacked genomes in the far stratum (>0.05 branch distance), which limits separation of functional coupling from phylogenetic signal. [src: cofitness_coinheritance]

### Functional categories

Functional categories from SEED annotations were tabulated for pairs in the top quartile of both phi and co-fitness. The most common categories, reported as gene counts rather than pair counts, were Metabolism (15,936 genes), Transport (11,940), Regulation (6,339), Motility (2,929), Mobile elements (2,716) and DNA metabolism (2,490). [src: cofitness_coinheritance]

### Literature context

The report cites the following studies as context; none of these findings were measured in this project.
- Hall et al. (2021; PMID: 34499026) found that *Escherichia coli* accessory genes co-occur by function and via mobile genetic elements. The report treats this as consistent with its module-level result.
- Whelan et al. (2020; PMID: 32100706) developed Coinfinder to detect gene associations in pangenomes while controlling for phylogeny. This project extends that work by asking whether fitness-measured functional coupling predicts the associations Coinfinder would detect.
- Choudhury et al. (2025; PMID: 40304385) showed that *Pseudomonas aeruginosa* phylogroups have distinct co-occurrence networks, which the report reads as reinforcing that accessory genome structure is lineage-specific. [src: cofitness_coinheritance]

### Data extraction and analysis scope

The study initially targeted 11 species (genomes; clusters; cofit pairs):
- Koxy: 399; 4,942; 423,936.
- Btheta: 287; 4,649; 328,455.
- Smeli: 241; 6,004; 528,699.
- RalstoniaUW163: 141; 4,413; 0.
- Putida: 128; 5,409; 458,688.
- SyringaeB728a: 126; 4,999; 371,004.
- Korea: 72; 4,075; 230,724.
- RalstoniaGMI1000: 70; 4,723; 0.
- Phaeo: 43; 3,790; 192,138.
- Ddia6719: 66; 4,694; 250,488.
- pseudo3_N2E3: 40; 5,513; 507,828. [src: cofitness_coinheritance]

All had phylogenetic trees except Phaeo and pseudo3_N2E3. [src: cofitness_coinheritance]

Ralstonia UW163 and Ralstonia GMI1000 were excluded from the primary analysis because they had zero co-fitness data in the Fitness Browser, despite being in its organism table. Spark extracted presence matrices for the 11 target species by joining gene_genecluster_junction with gene, two billion-row tables. BROADCAST hints on small filter tables reduced query time to approximately 210s per organism. [src: cofitness_coinheritance]

For each organism, cofit pairs were mapped to pangenome cluster pairs using fb_pangenome_link.tsv and deduplicated. Phi coefficients were then computed from binary genome-by-cluster presence vectors. Ten prevalence-matched random pairs were generated per cofit pair, matching each cluster's prevalence independently within a tolerance of +/-5%. Adjacency was taken from Fitness Browser gene coordinates and defined as being within 5 loci on the same scaffold. [src: cofitness_coinheritance]

Data sources:
- Fitness Browser co-fitness: top-20 co-fitness partners per gene, from the `cofit` table via Spark.
- KBase pangenome: genome-by-cluster presence matrices, from the `gene_genecluster_junction` and `gene` tables via Spark.
- ICA fitness modules: co-regulated gene modules, from `fitness_modules/data/modules/`.
- SEED annotations: functional category assignments, from `conservation_vs_fitness/data/seed_annotations.tsv`. [src: cofitness_coinheritance]

### Figures

- `figures/fig1_cofit_cooccurrence.png`: phi versus prevalence curves for cofit versus random pairs, per organism and aggregated.
- `figures/fig2_operon_control.png`: adjacent versus distant cofit pairs, and the signal after excluding operons.
- `figures/fig3_phylo_control.png`: cofit-pair phi stratified by phylogenetic distance from the reference strain.
- `figures/fig4_cofit_strength.png`: co-fitness score versus phi coefficient, as a scatter and as binned means.
- `figures/fig5_module_coinheritance.png`: module co-inheritance, phi versus null by module type, and size effects.
- `figures/fig6_functional.png`: functional categories enriched among high-phi, high-cofit pairs. [src: cofitness_coinheritance]

## Caveats and Open Directions

The prevalence ceiling attenuates the pairwise signal. Most Fitness Browser genes map to core clusters (>95% prevalence), where phi approaches 0 for both cofit and random pairs because there is almost no variance to correlate. The analysis is therefore most informative for species with substantial auxiliary gene content. [src: cofitness_coinheritance]

The two Ralstonia organisms were excluded even though they were the most phylogenetically diverse and lowest-ANI organisms in the target set. This removed the species likely to have been most informative. [src: cofitness_coinheritance]

Phylogenetic control was limited. Stratification was available for 7 of 9 organisms, and most species lacked genomes in the far stratum (>0.05 branch distance). The near-versus-medium difference (mean phi=0.102 versus 0.067) was consistent with shared ancestry, but the missing far stratum prevents full disentanglement of functional and phylogenetic effects. [src: cofitness_coinheritance]

Pairwise co-fitness captures gene-pair relationships. ICA modules capture multi-gene coordinated regulation and may better represent the selective units that constrain co-inheritance. [src: cofitness_coinheritance]

Near-clonal species behaved differently: Ddia6719 (ANI 99.47%) had delta=+0.093 and pseudo3_N2E3 (ANI 99.66%) had delta=+0.026. Both retained enough accessory variation to detect co-inheritance, but their high baseline phi makes absolute phi values less interpretable. [src: cofitness_coinheritance]

Proposed next analyses:
- Restrict comparisons to auxiliary-only pairs in which both clusters are below 95% prevalence, to maximize presence/absence variance.
- For Ralstonia and other organisms lacking precomputed values, calculate co-fitness directly as pairwise Pearson correlations from raw genefitness data.
- Resolve reference-genome mapping to improve phylogenetic control.
- Build module co-transfer networks and test cross-module prediction.
- Expand to species with >30% auxiliary genes and existing co-fitness data. [src: cofitness_coinheritance]

## Slots Into

- [[concepts/module-level-coinheritance]] — Pairwise co-fitness only weakly predicts co-occurrence (aggregate delta=+0.003), while ICA modules, especially accessory ones, show stronger co-inheritance. The module counts carry an unresolved discrepancy between the per-organism table and the headline totals. [src: cofitness_coinheritance]
- [[concepts/cofitness-network-architecture]] — Supports the conclusion that pairwise co-fitness weakly predicts pangenome co-occurrence, while multi-gene ICA modules show a stronger co-inheritance signal. [src: cofitness_coinheritance]
- [[concepts/pangenome-core-boundary-and-clade-size-bias]] — A prevalence ceiling at >95% core prevalence attenuates phi. Near-clonal species still show signal, and an auxiliary-only reanalysis is proposed. [src: cofitness_coinheritance]
- [[concepts/phylogenetic-confounding-of-pangenome-associations]] — Near-genome phi exceeds medium-genome phi, and the far stratum is mostly missing. Together with the excluded Ralstonia, this limits separation of functional coupling from ancestry. Coinfinder is cited as context. [src: cofitness_coinheritance]
- [[concepts/gene-cooccurrence-ecological-guilds]] — Functional categories among high-phi, high-cofit genes, with literature context on function- and lineage-structured accessory co-occurrence. [src: cofitness_coinheritance]
- [[concepts/genomic-dispersal-functional-coupling]] — Only 0.7% of cofit pairs are adjacent, and excluding them leaves the pattern unchanged. [src: cofitness_coinheritance]
- [[concepts/genetic-perturbation-coverage-bias]] — The Ralstonia organisms lack precomputed co-fitness, so computing it from raw genefitness is proposed. [src: cofitness_coinheritance]
- [[concepts/pangenome-integration]] — Adds a prevalence-matched pangenome presence/absence analysis that links Fitness Browser co-fitness to accessory and core gene co-occurrence, using KBase pangenome presence matrices. [src: cofitness_coinheritance]
- [[concepts/cross-tenant-data-bridging]] — Demonstrates integration of Fitness Browser, KBase pangenome, phylogenetic-distance, ICA-module and SEED annotation datasets through Spark and linked files. [src: cofitness_coinheritance]
