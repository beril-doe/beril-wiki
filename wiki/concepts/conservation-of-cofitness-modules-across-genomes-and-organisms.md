---
type: "Concept"
description: "Whether ICA fitness modules are conserved, core-enriched or co-inherited across genomes beyond prevalence-matched random gene sets, and whether family breadth tracks conservation."
sources: ["summaries/amr_cofitness_networks__REPORT.md", "summaries/cofitness_coinheritance__REPORT.md", "summaries/conservation_fitness_synthesis__REPORT.md", "summaries/discoveries.md", "summaries/field_vs_lab_fitness__REPORT.md", "summaries/fitness_modules__REPORT.md", "summaries/metal_fitness_atlas__REPORT.md", "summaries/module_conservation__REPORT.md", "summaries/pathway_capability_dependency__REPORT.md", "summaries/pitfalls.md"]
---
# Conservation of cofitness modules across genomes and organisms

ICA (independent component analysis) fitness modules are mostly core, and many module families recur across organisms. Their co-inheritance beyond prevalence-matched random gene sets is positive but modest, and module-family breadth does not track core fraction. [src: conservation_fitness_synthesis, fitness_modules, cofitness_coinheritance] The co-inheritance test covered 6 organisms. [src: cofitness_coinheritance] Metal-responsive modules show the same core enrichment. [src: metal_fitness_atlas]

## Conservation across organisms

ICA decomposition identified 1,116 co-regulated fitness modules across 32 organisms. [src: conservation_fitness_synthesis] Cross-organism alignment used 1.15M bidirectional best hit (BBH) pairs across 32 organisms, giving 13,402 ortholog groups. [src: fitness_modules] It found 156 module families spanning 2+ organisms: 28 span 5+, 7 span 10+ and 1 spans 21. [src: fitness_modules, discoveries] The largest family spans 21 of 32 organisms across Proteobacteria, Bacteroidetes, Firmicutes and Archaea, which the report reads as deeply conserved fitness regulons. [src: discoveries, fitness_modules] The fitness_modules report also says this largest family provides evidence for deeply conserved co-regulation programs. [src: fitness_modules] Of the families, 145 (93%) had consensus functional labels. [src: fitness_modules]

Ortholog scope matters a great deal. Using BBH pairs from 5 organisms (10K pairs, 1,861 ortholog groups) instead of all 32 organisms (1.15M pairs, 13,402 ortholog groups) gave radically different results. [src: discoveries] Module families rose from 27 to 156, families spanning 5+ organisms rose from 0 to 28, and family-backed predictions rose from 31 (4%) to 493 (56%). [src: discoveries] The pilot had no family spanning more than 4 organisms. [src: discoveries] The report advises extracting orthologs for all organisms, because the ortholog graph is not additive and new organisms create transitive connections. [src: discoveries] The pitfalls digest repeats this advice: extract BBH pairs for all organisms, not a pilot subset. [src: pitfalls] It says the 5-organism orthologs gave 6x fewer module families for a 32-organism analysis and missed all families spanning 5+ organisms. [src: pitfalls] Partial extraction severely underestimates cross-organism conservation because each new organism adds transitive connections. [src: pitfalls]

Among antimicrobial resistance (AMR) genes, 136 unique module families contain them, and 99% (208/209) of AMR gene-module assignments are in cross-organism conserved families. [src: amr_cofitness_networks] The report interprets this as ancient regulatory relationships. [src: amr_cofitness_networks]

## Core enrichment

ICA modules are enriched in core genes: 86% core versus an 81.5% baseline (odds ratio 1.46, p=1.6e-87). [src: conservation_fitness_synthesis, module_conservation] That is a difference of +4.5 percentage points. [src: module_conservation] Because the baseline is already about 81.5%, the ceiling limits observable enrichment, and the +4.5pp difference is statistically significant but a modest absolute effect. [src: module_conservation] Of the modules, 59% are more than 90% core. [src: conservation_fitness_synthesis] The report concludes that the core genome contains coordinated functional units, not just individual essential genes. [src: conservation_fitness_synthesis] It reads the 59% figure as extending "core" from individual genes to functionally coherent regulatory units. [src: module_conservation]

Metal-responsive modules show the same pattern. The 183 modules with conservation data have a mean core fraction of 0.826 and a median of 0.929, so most are predominantly core genes. [src: metal_fitness_atlas]

Family breadth does not predict conservation. Families spanning more organisms do not have higher core fractions (rho=-0.01, p=0.91; p=0.914 in the module_conservation report). [src: conservation_fitness_synthesis, module_conservation] Families are nearly all core regardless of how many organisms they span. [src: module_conservation] The pathway_capability_dependency report cites this same null. [src: pathway_capability_dependency] The report attributes it to a baseline so high (~82%) that there is no room for a gradient. [src: conservation_fitness_synthesis, module_conservation] It also interprets the null as suggesting that conservation is a property of individual genes, not of the cross-organism scope of their regulatory module. [src: module_conservation]

The analysis found 38 module families with <50% core genes, described as co-regulated accessory gene modules conserved across organisms. [src: module_conservation] The report hypothesizes that these may be horizontally transferred functional units or niche-specific operons. [src: module_conservation]

The report leaves two questions open: whether universally essential gene families exist across all 43 organisms, and which co-regulated functions live exclusively in the flexible genome in the 48 accessory modules. [src: conservation_fitness_synthesis] The fitness_modules report proposes integrating module predictions with core, auxiliary and singleton pangenome classes, and testing which modules are enriched in accessory genes. [src: fitness_modules]

In DvH, 52 ICA modules have a mean core fraction of 0.886 and a median of 1.000. [src: field_vs_lab_fitness] Using the mean as the threshold, modules split into four classes. [src: field_vs_lab_fitness]

- Ecological (field-active + conserved): 21 modules, mean core fraction 0.980. [src: field_vs_lab_fitness]
- Conserved-quiet (low field activity + conserved): 17 modules, mean core fraction 0.983. [src: field_vs_lab_fitness]
- Field-variable (field-active + less conserved): 5 modules, mean core fraction 0.829. [src: field_vs_lab_fitness]
- Lab (low field + less conserved): 9 modules, mean core fraction 0.516. [src: field_vs_lab_fitness]

Conservation does not correlate with field-condition activity (Spearman rho=0.071, p=0.62), so the hypothesis H2 was not supported. [src: field_vs_lab_fitness] The nine lab modules are notably less conserved and contain accessory-genome genes. [src: field_vs_lab_fitness] The report suggests accessory-genome modules exist and tend to respond to lab-type conditions. [src: field_vs_lab_fitness] The 21 ecological modules contain 239 genes, of which 52 are unannotated candidates for environmental adaptation. [src: field_vs_lab_fitness] The report regards them as supporting a functional core relevant to environmental survival. [src: field_vs_lab_fitness]

## Co-inheritance beyond a prevalence-matched null

For 6 organisms (Koxy, Btheta, Putida, Korea, Phaeo, pseudo3_N2E3), within-module mean pairwise phi was compared with 1000 prevalence-matched random gene sets. P-values were corrected with Benjamini-Hochberg false discovery rate (FDR). [src: cofitness_coinheritance] Across 195 modules, mean phi was 0.229 against a null mean of 0.177 (delta=+0.053). [src: cofitness_coinheritance] Of these, 51/195 (26%) were significant at p<0.05, and 21/195 (11%) remained significant at q<0.05 after FDR. [src: cofitness_coinheritance]

Accessory modules show the strongest signal, but the accessory-versus-core difference only trended toward significance (Mann-Whitney p=0.051). [src: cofitness_coinheritance]

- Accessory (<50% core), n=11: mean delta phi +0.108, 8/11 (73%) significant at p<0.05, 4/11 (36%) at FDR q<0.05. [src: cofitness_coinheritance]
- Core (>90% core), n=120: mean delta phi +0.059, 29/120 (24%) at p<0.05, 13/120 (11%) at FDR q<0.05. [src: cofitness_coinheritance]
- Mixed (50-90%), n=64: mean delta phi +0.031, 14/64 (22%) at p<0.05, 4/64 (6%) at FDR q<0.05. [src: cofitness_coinheritance]

The pathway_capability_dependency report treats the result that 73% of accessory modules show co-inheritance with co-fitness as validating pathway-level fitness aggregation. [src: pathway_capability_dependency]

Organisms differ widely in modules, significant modules, mean phi and null mean. [src: cofitness_coinheritance]

- Koxy: 44 modules, 14 (32%) significant, 0.079 vs null 0.040. [src: cofitness_coinheritance]
- Btheta: 36 modules, 22 (61%) significant, 0.192 vs null 0.086. [src: cofitness_coinheritance]
- Putida: 38 modules, 6 (16%) significant, 0.266 vs null 0.202. [src: cofitness_coinheritance]
- Korea: 29 modules, 0 (0%) significant, 0.357 vs null 0.308. [src: cofitness_coinheritance]
- Phaeo: 37 modules, 3 (8%) significant, 0.108 vs null 0.095. [src: cofitness_coinheritance]
- pseudo3_N2E3: 40 modules, 4 (10%) significant, 0.444 vs null 0.409. [src: cofitness_coinheritance]

Btheta shows the strongest module-level signal. [src: cofitness_coinheritance] Korea, the best pairwise organism, has no significant modules. All its modules are more than 90% core with prevalence near 1.0. [src: cofitness_coinheritance]

The report suggests that coordinated multi-gene regulation, not only pairwise functional similarity, most strongly constrains co-inheritance. [src: cofitness_coinheritance] It describes the 48 accessory modules from the module_conservation project as functionally coherent units that travel together through the pangenome. [src: cofitness_coinheritance] It cites Hall et al. (2021; PMID 34499026) on E. coli accessory genes co-occurring by function and via mobile genetic elements. [src: cofitness_coinheritance] It also cites Choudhury et al. (2025; PMID 40304385) on distinct co-occurrence networks among P. aeruginosa phylogroups. [src: cofitness_coinheritance]

## Tensions

- Modules are enriched in core genes, and most are over 90% core. [src: conservation_fitness_synthesis] Yet the strongest co-inheritance beyond the null is in the few accessory modules, while Korea's modules, all more than 90% core with prevalence near 1.0, show none. [src: cofitness_coinheritance]
- Cross-organism families are widespread, but breadth does not track core fraction. [src: fitness_modules, conservation_fitness_synthesis]
- Accessory-module co-inheritance is only a trend against core modules (p=0.051). [src: cofitness_coinheritance] It rests on only 11 modules. [src: cofitness_coinheritance]

## Open Directions

- Test whether the module-versus-null delta persists when core modules are compared against nulls matched on both prevalence and core status. This would show whether the Korea null result is a ceiling effect.
- Extend the co-inheritance test beyond 6 organisms, and add more accessory modules to settle the p=0.051 trend.
- Identify the co-regulated functions of the 48 accessory modules in the flexible genome.
- Ask whether universally essential gene families exist across all 43 organisms.
- Test family breadth against core fraction within a stricter set of non-core modules, where the high baseline cannot hide a gradient.
- Integrate module predictions with core, auxiliary and singleton pangenome classes, and test which modules are enriched in accessory genes.
