---
type: "Method"
description: "ICA decomposition of fitness matrices into condition-specific co-regulated gene modules, with cross-organism module families."
sources: ["summaries/amr_cofitness_networks__REPORT.md", "summaries/annotation_gap_discovery__REPORT.md", "summaries/cofitness_coinheritance__REPORT.md", "summaries/conservation_fitness_synthesis__REPORT.md", "summaries/discoveries.md", "summaries/essential_genome__REPORT.md", "summaries/field_vs_lab_fitness__REPORT.md", "summaries/fitness_modules__REPORT.md", "summaries/functional_dark_matter__REPORT.md", "summaries/metal_fitness_atlas__REPORT.md", "summaries/metal_specificity__REPORT.md", "summaries/module_conservation__REPORT.md", "summaries/pitfalls.md", "summaries/truly_dark_genes__REPORT.md"]
aliases: ["FastICA", "ICA", "ICA fitness modules", "ICA modules", "Module-ICA", "fitness modules"]
---
# Independent component analysis fitness modules

This page covers independent component analysis (ICA) fitness modules: ICA decomposition of fitness matrices into condition-specific co-regulated gene modules, with cross-organism module families. Across the cited reports they are validated by cofitness and genomic adjacency, they are mostly core genes, and they support process-level inference. [src: discoveries, fitness_modules, conservation_fitness_synthesis] Modules also seed dark-gene hypotheses and metal-response analyses, but module-level metal specificity was not found with z-scored profiles in one report. [src: functional_dark_matter, metal_fitness_atlas, metal_specificity] Also known as: FastICA, ICA, ICA fitness modules, ICA modules, Module-ICA, fitness modules.

## Key facts

- ICA decomposition identified 1,116 co-regulated fitness modules across 32 organisms. [src: conservation_fitness_synthesis, fitness_modules, module_conservation]
- Robust ICA (30-50 FastICA runs plus DBSCAN clustering) finds 17-52 stable modules per organism across 32 bacteria. [src: discoveries]
- Median module size is 7-50 genes per module, described as a biologically correct range. [src: fitness_modules]
- Module membership files are in fitness_modules/data/modules/, and cross-organism families are in fitness_modules/data/module_families/. [src: amr_cofitness_networks, module_conservation]
- The fitness_modules report extends transcriptomic ICA to fitness data across 32 organisms. It reports biologically coherent co-regulation structure in phenotypic compendia. [src: fitness_modules]
- Price et al. (2018) is credited with generating the Fitness Browser data and developing the ICA decomposition approach used to identify co-regulated fitness modules. [src: module_conservation]
- Saelens et al. (2018) is cited as showing that ICA outperforms other decomposition methods for microbial gene expression data. [src: module_conservation]
- Genes in ICA modules are described as co-regulated functional units that skew toward the conserved core genome. [src: module_conservation]

## Construction and validation

The membership rule mattered more than the ICA components. Initial D'Agostino K² normality-based thresholding gave 100-280 genes per module, which was biologically meaningless. [src: discoveries] ICA weight distributions are intentionally heavy-tailed and non-Gaussian, so the normality test always rejects normality and uses a permissive z-threshold of 2.5. [src: pitfalls] The report attributes the problem to membership selection, not the ICA components. [src: discoveries] Switching to |Pearson r| ≥ 0.3 with the module profile and max 50 genes reduced modules to 5-50 genes. [src: discoveries, fitness_modules, module_conservation] The pitfalls digest calls this the single most impactful parameter in the pipeline. [src: pitfalls] Cofitness enrichment improved from 59% to 94.2%. [src: discoveries] Within-module |r| improved from 0.047 to 0.34, as a mean across 32 organisms. [src: discoveries]

With the strict thresholds, 94.2% of modules showed significantly elevated within-module cofitness (Mann-Whitney U, p < 0.05). [src: fitness_modules] Mean within-module |r| was 0.34 versus background 0.12, a 2.8x enrichment. [src: discoveries, fitness_modules] Genomic adjacency enrichment averages 22.7× across organisms, which the report takes as confirmation that modules capture operon-like co-regulated groups. [src: discoveries]

Limits and practical pitfalls:

- Capping components at 40% of experiments is needed because higher ratios cause FastICA convergence failures and extreme slowness. [src: discoveries, pitfalls] Each failed run reaches max_iter, and an organism with 150 experiments should use at most 60 components. [src: pitfalls]
- The cap may miss modules in low-experiment organisms. [src: fitness_modules]
- Organisms with fewer than ~100 experiments give weaker modules. Caulo, with 198 experiments, showed only 2.9x correlation enrichment. [src: fitness_modules]
- Cosine distances defined as 1 - |cosine_similarity| can become slightly negative from floating-point error, and DBSCAN with metric="precomputed" rejects them. [src: pitfalls] The fix is np.clip(cos_dist, 0, 1, out=cos_dist) before clustering. [src: pitfalls]
- Module annotation depended on enrichment settings. With min_annotated=3 and KEGG KOs (~1.2 genes per KO), only 8% of modules got any enrichment, because almost no KEGG term has 3+ genes in a 5-50 gene module. [src: pitfalls] Lowering to min_annotated=2 with FDR correction and adding PFam domains (814 terms with 2+ genes) alongside TIGRFam (88 terms) raised annotation from 8% to 80%. [src: pitfalls]

See also [[concepts/construction-and-validity-of-cofitness-gene-groups]].

## Cross-organism module families

Cross-organism alignment with bidirectional best hit (BBH) ortholog fingerprints found 156 module families spanning 2+ organisms. [src: discoveries, fitness_modules] Of these, 28 span 5+ organisms, 7 span 10+, and 1 spans 21. [src: fitness_modules] 145 families (93%) have consensus functional labels. [src: fitness_modules] The largest family spans 21 organisms and is described as a pan-bacterial fitness module. [src: fitness_modules]

## Conservation

Modules are enriched in core genes: 86% core versus 81.5% baseline (OR=1.46, p=1.6e-87). [src: conservation_fitness_synthesis] The module_conservation analysis reports 86.0% versus 81.5% across 29 organisms. Its per-organism paired Wilcoxon gave p=1.0e-03, with 22/29 organisms showing enrichment. [src: discoveries] 59% of modules are >90% core genes. [src: conservation_fitness_synthesis, discoveries]

In Desulfovibrio vulgaris Hildenborough (DvH), 52 ICA modules have mean core fraction 0.886 and median 1.000. [src: field_vs_lab_fitness] Using 0.886 as the threshold, the modules split into four classes. [src: field_vs_lab_fitness]

- Ecological (field-active + conserved): 21 modules, mean core fraction 0.980. [src: field_vs_lab_fitness]
- Conserved-quiet (low field activity + conserved): 17 modules, mean core fraction 0.983. [src: field_vs_lab_fitness]
- Field-variable (field-active + less conserved): 5 modules, mean core fraction 0.829. [src: field_vs_lab_fitness]
- Lab (low field + less conserved): 9 modules, mean core fraction 0.516. [src: field_vs_lab_fitness]

The lab modules are notably less conserved and contain accessory-genome genes. [src: field_vs_lab_fitness] See [[entities/desulfovibrio-vulgaris-hildenborough]] and [[concepts/conservation-of-cofitness-modules-in-the-core-genome]].

Modules also co-occur across genomes. In 6 organisms, 195 modules had within-module mean phi=0.229, against a prevalence-matched null mean phi=0.177 from 1000 permutations. The delta was +0.053, and 51/195 modules (26%) were significant at p<0.05. [src: cofitness_coinheritance] The test used Benjamini-Hochberg false discovery rate (FDR) correction. [src: cofitness_coinheritance] The report describes the 48 accessory modules from module_conservation as functionally coherent units that travel together through the pangenome. [src: cofitness_coinheritance] See [[concepts/conservation-of-cofitness-modules-across-genomes-and-organisms]].

## Function prediction

The fitness_modules report states that modules capture process-level co-regulation, not specific molecular function. [src: discoveries] In a held-out KEGG ortholog (KO) prediction benchmark across 32 organisms, ortholog transfer dominated gene-level prediction, with 95.8% precision and 91.2% coverage. [src: discoveries] Module-ICA had <1% precision at the KO level. [src: discoveries]

Modules still help with dark genes. 6,142 dark genes (10.8% of the 57,011 dark genes in the census) belong to ICA modules with function predictions. [src: functional_dark_matter] The functional_dark_matter report counts this as support for functional coherence (H1a), because these genes co-regulate with annotated genes. [src: functional_dark_matter] Among the top 100 dark-gene candidates, 85 have module-based function predictions. [src: functional_dark_matter] The report calls the fitness_modules guilt-by-association approach its single strongest inference layer. [src: functional_dark_matter] Its 6,691 module-based predictions are guilt-by-association inferences, not direct experimental validation. [src: functional_dark_matter]

In the truly dark genes report, 594 genes in ICA organisms belong to ICA fitness modules, and guilt-by-association reveals functions including phage integrases, metal transporters, chemotaxis systems and iron regulation. [src: truly_dark_genes] Among top candidates, 34 are essential, 53 are in operons and 30 are in ICA fitness modules. [src: truly_dark_genes] Examples are PV4/5210953 (score 10; motility phenotype, |f| = 5.5; operon with TatC; module M016) and ANA3/7026383 (score 9; nitrogen source phenotype, |f| = 8.6; operon with an ABC transporter; module M018). [src: truly_dark_genes] That report presents the approach as extending Oliver's (2000) expression-based guilt by association to fitness data. [src: truly_dark_genes]

Essential genes have no fitness data, so ICA cannot see them. Their non-essential orthologs in other organisms can join modules. Transferring module context this way generated 1,382 predictions for hypothetical essential genes, covering 35.3% of predictable targets. [src: essential_genome] See [[concepts/function-prediction-for-uncharacterized-genes-by-guilt-by-association-and-ortholog-transfer]].

## Metal responses

In the Pan-Bacterial Metal Fitness Atlas, NB05 analyzed 19,453 module × metal-experiment records across 31 organisms. [src: metal_fitness_atlas] The atlas describes its module profiles in two ways: standardized per module across all experiments [src: metal_fitness_atlas], and standardized across all experiments per organism. [src: metal_fitness_atlas] The cited quotes do not reconcile these descriptions. Using z-scored module activity profiles, the atlas identified 600 metal-responsive module records at |z| > 2.0, which is 3.1% of the 19,453 records. [src: metal_fitness_atlas] DvH led with 47 responsive modules across 12 metals, and psRCH2 had 11 modules across 6 metals. [src: metal_fitness_atlas] An initial attempt with raw activity scores from module_conditions.csv gave 0 responsive modules, because raw scores (max 0.96) are on a different scale than z-scores. [src: metal_fitness_atlas]

The metal_specificity report limits this. Its module-level specificity analysis using z-scored activity profiles found 0 metal-specific modules. [src: metal_specificity] Per-module z-normalization gives max |z| below 2.0 for most metal experiments, because metal experiments are a small fraction of each organism's experiments. [src: metal_specificity] It also notes that raw module-condition scores differ in scale from the z-scored profiles of Metal Atlas NB05. [src: metal_specificity] See [[concepts/metal-responsive-ica-fitness-modules]].

## Antimicrobial resistance (AMR) genes

Only 24% of AMR genes (192/801) are assigned to ICA modules. [src: amr_cofitness_networks] The modules they occupy are larger than non-AMR modules, with median 46 versus 27 genes (Mann-Whitney U p = 1.7×10⁻⁸). [src: amr_cofitness_networks] The report regards this as robust, because ICA captures condition-specific co-regulation, not just shared mean fitness. [src: amr_cofitness_networks] 136 unique module families contain AMR genes, and 99% of those are cross-organism conserved families. [src: amr_cofitness_networks] The report interprets this as AMR genes being embedded in broad cellular programs with genuine co-regulatory structure. [src: amr_cofitness_networks] See [[concepts/amr-genes-in-ica-fitness-modules]].

## Proposed extension

The annotation_gap_discovery report proposes that ICA approaches could identify functional gene modules that resolve gaps missed by per-gene analysis. [src: annotation_gap_discovery] It cites Borchert et al. (2024, mSystems), who per PubMed applied ICA to Pseudomonas putida RB-TnSeq fitness data and identified 84 functional gene modules. [src: annotation_gap_discovery]

## Sources

Module data came from the fitness_modules and module_conservation data tables. [src: cofitness_coinheritance, conservation_fitness_synthesis, essential_genome, field_vs_lab_fitness]
