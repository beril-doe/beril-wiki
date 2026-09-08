---
type: Method
description: Independent component analysis for discovering bacterial fitness modules
sources:
- id: amr_cofitness_networks
  resource: ../summaries/amr_cofitness_networks__REPORT.md
  title: amr cofitness networks
- id: annotation_gap_discovery
  resource: ../summaries/annotation_gap_discovery__REPORT.md
  title: annotation gap discovery
- id: cofitness_coinheritance
  resource: ../summaries/cofitness_coinheritance__REPORT.md
  title: cofitness coinheritance
- id: conservation_fitness_synthesis
  resource: ../summaries/conservation_fitness_synthesis__REPORT.md
  title: conservation fitness synthesis
- id: counter_ion_effects
  resource: ../summaries/counter_ion_effects__REPORT.md
  title: counter ion effects
- id: discoveries
  resource: ../summaries/discoveries.md
  title: discoveries
- id: essential_genome
  resource: ../summaries/essential_genome__REPORT.md
  title: essential genome
- id: field_vs_lab_fitness
  resource: ../summaries/field_vs_lab_fitness__REPORT.md
  title: field vs lab fitness
- id: fitness_modules
  resource: ../summaries/fitness_modules__REPORT.md
  title: fitness modules
- id: functional_dark_matter
  resource: ../summaries/functional_dark_matter__REPORT.md
  title: functional dark matter
- id: metal_fitness_atlas
  resource: ../summaries/metal_fitness_atlas__REPORT.md
  title: metal fitness atlas
- id: metal_specificity
  resource: ../summaries/metal_specificity__REPORT.md
  title: metal specificity
- id: module_conservation
  resource: ../summaries/module_conservation__REPORT.md
  title: module conservation
- id: truly_dark_genes
  resource: ../summaries/truly_dark_genes__REPORT.md
  title: truly dark genes
title: Independent component analysis of fitness modules
---
# Independent component analysis of fitness modules

## What this entity is

**Canonical name:** Independent component analysis of fitness modules. [^amr_cofitness_networks]

**Known aliases:** ICA; ICA fitness modules. [^amr_cofitness_networks]

**Stable external identifier:** Not reported in the source documents. [^amr_cofitness_networks]

Independent component analysis (ICA) decomposes bacterial fitness matrices into gene modules representing shared fitness patterns across experimental conditions. [^amr_cofitness_networks] The annotation-gap study proposes ICA as complementary to per-gene analysis for detecting functional modules that individual-gene tests may miss. [^annotation_gap_discovery] The counter-ion analysis **supports** this role by proposing module-level ICA to distinguish shared stress responses from metal-specific fitness signals. [^counter_ion_effects]

The essential-genome analysis **extends** ICA from module discovery to indirect function prediction: fitness-module context from non-essential orthologs generated family-backed predictions for hypothetical essential genes, whose lethal disruption prevents direct fitness characterization. [^essential_genome] The fitness-modules benchmark **refines** this interpretation by showing that ICA is substantially stronger for process-level module context than precise gene-level function assignment. [^fitness_modules] The functional-dark-matter analysis **supports** ICA as a prioritization layer: 6,142 dark genes belonged to ICA fitness modules, although module membership remains an inference rather than direct functional validation. [^functional_dark_matter] The truly-dark-gene analysis **extends** this use to genes that remain hypothetical after modern annotation: 594 such genes belonged to ICA fitness modules, and module context linked them to candidate functions including phage integrases, metal transporters, chemotaxis systems, and iron regulation. [^truly_dark_genes]

## Evidence and architecture

The AMR cofitness analysis included 28 organisms with antimicrobial-resistance genes, fitness matrices, and ICA modules. [^amr_cofitness_networks] Of 801 AMR genes with fitness data, 192 (24%) were assigned to modules. [^amr_cofitness_networks] AMR-containing modules had a median of 46 genes versus 27 in non-AMR modules (Mann–Whitney U p=1.7×10⁻⁸); efflux and enzymatic AMR modules both had a median size of 48 (p=0.91). [^amr_cofitness_networks] There were 136 unique AMR-containing module families, and 208/209 (99%) AMR gene–module assignments belonged to cross-organism conserved families. [^amr_cofitness_networks] ICA was interpreted as capturing condition-specific co-regulation rather than only shared mean fitness, but module membership does not establish direct transcriptional control. [^amr_cofitness_networks]

The broader discoveries synthesis reports the same AMR-module size contrast and InterProScan enrichments for flagellar motility, flagellum assembly, histidine-biosynthesis, and tryptophan-biosynthesis, whereas legacy Fitness Browser SEED annotations detected 0/280 significant enrichments. [^discoveries] The functional-dark-matter analysis **extends** ICA beyond AMR: among 57,011 dark genes identified among 228,709 genes across 48 organisms, 6,142 belonged to ICA modules; metals, oxidative stress, and osmotic stress dominated strong dark-gene phenotypes. [^functional_dark_matter]

The cofitness–coinheritance study **supports** coordinated multi-gene structure: across 195 ICA modules in 6 organisms, within-module co-occurrence exceeded a prevalence-matched null by delta phi=+0.053; 51/195 (26%) were significant at p<0.05 and 21/195 (11%) remained significant at q<0.05 after Benjamini–Hochberg FDR (false discovery rate) correction. [^cofitness_coinheritance] Accessory modules had mean delta phi +0.108 versus +0.059 for core modules, with the difference trending toward significance (Mann–Whitney p=0.051). [^cofitness_coinheritance] This **refines** the AMR result because module-level structure was stronger than pairwise cofitness, whose aggregate delta was only +0.003. [^cofitness_coinheritance]

The fitness-modules analysis used an absolute membership threshold of |weight| >= 0.3 and a maximum of 50 genes, recovering 1,116 stable modules across 32 organisms, each supported by at least 100 experiments. [^fitness_modules] Module sizes had a median range of 7-50 genes; 94.2% showed significantly elevated within-module cofitness at p < 0.05, with within-module mean |r|=0.34 versus 0.12 in the background, a 2.8x enrichment, and 22.7x genomic-adjacency enrichment. [^fitness_modules] The initial D'Agostino K-squared membership approach instead produced 100-280 genes per module with 59% enrichment and 1-17x correlation; absolute weight thresholding produced the reported 94% enrichment and 2.8x correlation enrichment. [^fitness_modules] This **refines** the discoveries synthesis's robust-ICA/DBSCAN account, which reported stability at 17–52 modules per organism, 94.2% elevated cofitness, mean |r|=0.34 versus background 0.12, and 22.7× mean genomic-adjacency enrichment. [^discoveries]

The module-conservation analysis **supports and qualifies** this architecture: among 974 modules with >=3 mapped genes, 577 (59%) were >90% core genes, 349 (36%) were mixed (50-90% core), and 48 (5%) were <50% core; the median module was 93.4% core. [^module_conservation] Module genes were 86.0% core versus 81.5% for all genes (OR=1.46, p=1.6e-87), a statistically strong but modest +4.5 percentage-point enrichment because the baseline was already high. [^module_conservation] This extends pangenome conservation from individual genes to co-regulated functional units. [^module_conservation] Thirty-eight families had <50% core genes; their possible horizontal-transfer or niche-specific-operon interpretation is a hypothesis, because the analysis measured conservation patterns rather than directly demonstrating transfer or niche-specific regulation. [^module_conservation] Family breadth did not predict conservation (Spearman rho=-0.01, p=0.914), redirecting interpretation toward gene-level conservation rather than cross-organism module scope. [^module_conservation]

The truly-dark-gene analysis **supports** the use of ICA for annotation-resistant genes but also narrows the inference: among 4,394 truly dark genes in organisms with integrated condition analysis data, 41% of neighboring genes were also hypothetical, 25.9% showed operon-like cofitness with adjacent genes using |r| ≥ 0.3, and 594 genes belonged to ICA fitness modules. [^truly_dark_genes] The resulting guilt-by-association links to phage integrases, metal transporters, chemotaxis systems, and iron regulation are candidate functional hypotheses, not validated assignments. [^truly_dark_genes]

Cross-organism alignment produced 1.15M bidirectional-best-hit (BBH) pairs across 32 organisms and 13,402 ortholog groups. [^fitness_modules] It identified 156 module families spanning 2+ organisms, including 28 spanning 5+, 7 spanning 10+, and 1 spanning 21 organisms; 145 families had consensus functional labels, representing 93% of families. [^fitness_modules] This **supports** the discoveries result that alignment found 156 families, including 28 spanning 5+ organisms and one spanning 21 of 32 organisms, while indicating conserved fitness architecture rather than identical molecular functions for every member. [^discoveries][^fitness_modules]

Ortholog scope increased module families from 27 to 156, families spanning 5+ organisms from 0 to 28, and family-backed predictions from 31 to 493. [^discoveries] Pfam-domain evidence increased module annotation from 92/1,116 (8.2%) to 890/1,116 (79.7%), predictions from 878 to 6,691, and annotated families from 32 to 145 of 156. [^discoveries] Adding Pfam domains and lowering the enrichment-overlap threshold from 3 to 2 increased module annotation from 8% to 80%, expanded annotated modules from 92 to 890, and unlocked 7.6x more function predictions; Pfam provided the broadest coverage, whereas KEGG KOs were too gene-specific for module-level enrichment. [^fitness_modules]

The analysis generated 6,691 function predictions for hypothetical proteins: 2,455 were family-backed (37%) and 4,236 were module-only predictions, using enrichment from KEGG, SEED, TIGRFam, and Pfam. [^fitness_modules] Ortholog transfer achieved 95.8% strict precision, 91.2% coverage, and 0.934 F1 in held-out benchmarking; domain-based prediction achieved 29.1% precision, 66.6% coverage, and 0.401 F1; Module-ICA achieved <1% strict precision and 23.3% coverage; and cofitness voting achieved <1% strict precision and 73.0% coverage. [^fitness_modules] Thus, the results **refine** ICA's role toward process-level module discovery rather than precise gene-level assignment. [^discoveries][^fitness_modules] Near-zero strict KEGG KO precision is expected because KEGG KO groups are gene-level assignments averaging approximately 1.2 genes per unique KO, so a module with 20 annotated members typically contained 20 different KOs. [^fitness_modules]

The essential-genome analysis **supports and qualifies** this role: module transfer produced 1,382 function predictions for hypothetical essential genes, equal to 35.3% of predictable targets, across all 48 organisms, including TIGR00254 signal transduction, PF00460 flagellar basal body rod, and PF00356 lactoylglutathione lyase among top predicted functions. [^essential_genome] The functional-dark-matter accounting reports 6,691 module predictions while 6,142 dark genes belonged to modules; these prediction and module-associated-gene counts should not be treated as identical. [^functional_dark_matter]

## Stress, conservation, and limitations

The field-versus-lab analysis **refines** the conservation interpretation in a single-organism test: across 52 ICA modules in *Desulfovibrio vulgaris* Hildenborough, mean core fraction was 0.886 and median 1.000, and conservation did not significantly correlate with field-condition activity (Spearman rho=0.071, p=0.62). [^field_vs_lab_fitness] Using 0.886 as the threshold, ecological modules averaged 0.980 core, conserved-quiet modules 0.983, field-variable modules 0.829, and lab modules 0.516; the 21 ecological modules contained 239 genes, including 52 unannotated candidates for environmental-adaptation functions. [^field_vs_lab_fitness]

The counter-ion analysis **refines** the stress interpretation: across 19 organisms and 14 metals, 4,304 of 10,821 metal-important gene records (39.8%) were also NaCl-important, and it proposes ICA to separate shared NaCl–metal signals from metal-specific effects without reporting a completed test. [^counter_ion_effects] Zinc had a DvH whole-genome correlation of r=0.715 with NaCl despite zinc sulfate delivering 0 mM chloride, whereas iron had r=0.086; these are fitness-profile extrapolations rather than direct biochemical tests. [^counter_ion_effects]

The metal-fitness atlas **supports** core-enriched module architecture at broader scale: among 183 metal-responsive modules with conservation data, mean core fraction was 0.826 and median 0.929. [^metal_fitness_atlas] It identified 600 responsive module records with |z| > 2.0 among 19,453 module × metal-experiment records (3.1%), including 47 DvH modules across 12 metals and 11 psRCH2 modules across six metals. [^metal_fitness_atlas] The metal-specificity analysis **contradicts** a strong expectation of metal-specific ICA structure but not the broader module model: it identified 0 metal-specific modules. [^metal_specificity] Per-module z-normalization yielded maximum absolute z values <2.0 for most metal experiments because those experiments were a small fraction of each organism's experiments; raw scores also differed from the precomputed z-scored profiles used in the Metal Atlas. [^metal_specificity] The negative result therefore **refines** rather than disproves module organization and motivates use of precomputed z-scored activities. [^metal_specificity]

The conservation analysis found 0 essential genes in any module. [^module_conservation] Because ICA requires measurable transposon-insertion fitness variation and essential genes lack usable insertions, this describes the non-essential portion of the genome rather than demonstrating that essential genes lack modules. [^module_conservation] The essential-genome result likewise shows that transfer from non-essential orthologs is indirect and may fail when an essential gene's function has diverged. [^essential_genome]

Module size does not establish direct transcriptional co-regulation. [^amr_cofitness_networks][^cofitness_coinheritance] ICA modules indicate shared fitness phenotypes, and AMR-module size may reflect shared dispensability. [^amr_cofitness_networks][^cofitness_coinheritance] The fitness-modules predictions should therefore be treated as biological-process hypotheses: Pfam provides broad domain-level coverage and may overcount functional associations, while Module-ICA had <1% strict KEGG KO precision. [^fitness_modules] The truly-dark-gene results **reinforce** this caution because module membership and adjacent-gene cofitness supplied candidate functions for genes lacking direct annotation rather than experimental confirmation. [^truly_dark_genes]

The 40% component cap, imposed because components could not exceed 40% of the number of experiments to avoid FastICA convergence failures, may cause modules to be missed in organisms with few experiments. [^fitness_modules] Organisms with fewer than approximately 100 experiments produced weaker modules; Caulo, with 198 experiments, showed only 2.9x correlation enrichment. [^fitness_modules] The strict threshold and annotation results depend on membership and enrichment-overlap choices, and BBH-based families represent aligned conservation patterns rather than proof of identical molecular functions. [^fitness_modules] The module-conservation analysis covered a 29/32 organism subset because Cola, Kang, and SB2B lacked sufficient GTDB genomes for pangenome construction; its >90% and <50% core cutoffs are convenient rather than biologically motivated boundaries. [^module_conservation]

The field-versus-lab analysis found cross-validated AUC 0.517 for field fitness alone, 0.531 for lab fitness alone, 0.548 for combined field plus lab fitness, and 0.645 after adding gene length; gene length is confounded with fitness-measurement quality and core status. [^field_vs_lab_fitness] The functional-dark-matter collection contained 37/48 Pseudomonadota, and its top 500 dark-gene candidates contained 417 Gammaproteobacteria, 71 Alphaproteobacteria, 17 Deltaproteobacteria, 12 Bacteroidetes, 10 Betaproteobacteria, 5 Firmicutes, 2 Cyanobacteria, and 0 Archaea, Actinobacteria, or Epsilonproteobacteria, limiting cross-phylum generalization. [^functional_dark_matter] Korea had no significant co-inheritance modules because all Korea modules were >90% core with prevalence near 1.0. [^cofitness_coinheritance]

## Open directions and related pages

Fitness-matched permutation sampling of random non-AMR genes in the proposed −0.05 to +0.05 mean-fitness range could test whether AMR-module enrichment reflects condition-specific organization or shared dispensability. [^amr_cofitness_networks] Carbon-source fitness data could test whether ICA adds functional structure beyond individual-gene associations. [^annotation_gap_discovery] Precomputed z-scored module activities could determine whether the zero metal-specific-module result reflects scale and sparsity rather than biology. [^metal_specificity] Metal-responsive modules should be tested with concentration-normalized fitness, regulatory or expression data, and direct perturbations; CRISPRi knockdown under module-informed conditions could validate the 1,382 transferred essential-gene functions. [^metal_fitness_atlas][^essential_genome] Validation should use held-out annotations and perturbations rather than treating module membership as a KO assignment, and module-associated dark genes should be tested under stress, carbon-source, and nitrogen-source conditions. [^fitness_modules][^functional_dark_matter] The truly-dark-gene study further proposes testing its top candidates with structure prediction, module-informed growth assays, mobile-CRISPRi, and targeted analysis of dark genomic islands. [^truly_dark_genes]

- [module_conservation__REPORT](../summaries/module_conservation__REPORT.md) — source summary of ICA-module conservation, core/accessory architecture, family breadth, and essential-gene coverage. [^module_conservation]
- [metal_specificity__REPORT](../summaries/metal_specificity__REPORT.md) — source summary of metal-specific versus general-stress gene classification and its ICA module test. [^metal_specificity]
- [metal_fitness_atlas__REPORT](../summaries/metal_fitness_atlas__REPORT.md) — source summary of the pan-bacterial metal fitness atlas and its ICA module analysis. [^metal_fitness_atlas]
- [functional_dark_matter__REPORT](../summaries/functional_dark_matter__REPORT.md) — source summary of dark-gene scale, ICA-associated candidates, conservation, and experimental prioritization. [^functional_dark_matter]
- [fitness_modules__REPORT](../summaries/fitness_modules__REPORT.md) — source summary of ICA thresholds, cross-organism architecture, annotation coverage, and held-out function-prediction benchmarking. [^fitness_modules]
- [amr_cofitness_networks__REPORT](../summaries/amr_cofitness_networks__REPORT.md) — source summary describing the ICA module analysis and its interpretation. [^amr_cofitness_networks]
- [annotation_gap_discovery__REPORT](../summaries/annotation_gap_discovery__REPORT.md) — source summary proposing ICA analysis of fitness data to identify functional modules missed by per-gene analysis. [^annotation_gap_discovery]
- [cofitness_coinheritance__REPORT](../summaries/cofitness_coinheritance__REPORT.md) — source summary testing ICA-module co-inheritance in bacterial pangenomes. [^cofitness_coinheritance]
- [conservation_fitness_synthesis__REPORT](../summaries/conservation_fitness_synthesis__REPORT.md) — synthesis connecting ICA module architecture with gene conservation across organisms. [^conservation_fitness_synthesis]
- [counter_ion_effects__REPORT](../summaries/counter_ion_effects__REPORT.md) — analysis proposing ICA to separate shared-stress from metal-specific fitness architecture. [^counter_ion_effects]
- [discoveries](../summaries/discoveries.md) — cross-project synthesis of ICA module stability, cross-organism architecture, annotation, and AMR-network validation. [^discoveries]
- [essential_genome__REPORT](../summaries/essential_genome__REPORT.md) — pan-bacterial essentiality analysis using ICA modules for indirect function prediction. [^essential_genome]
- [field_vs_lab_fitness__REPORT](../summaries/field_vs_lab_fitness__REPORT.md) — DvH analysis testing whether field-versus-lab fitness modules predict pangenome conservation. [^field_vs_lab_fitness]
- [truly_dark_genes__REPORT](../summaries/truly_dark_genes__REPORT.md) — analysis using ICA modules and cofitness neighborhoods to prioritize genes that remain hypothetical after modern annotation. [^truly_dark_genes]
- [condition-specific-fitness](../concepts/condition-specific-fitness.md) — cofitness and ICA modules may reflect condition-specific shared dispensability rather than direct co-regulation. [^amr_cofitness_networks]
- [gene-essentiality](../concepts/gene-essentiality.md) — fitness phenotypes and dispensability are central to interpreting AMR-containing modules. [^amr_cofitness_networks]
- [cofitness-network-architecture](../concepts/cofitness-network-architecture.md) — ICA modules show stronger co-inheritance structure than pairwise cofitness and are enriched for core genes. [^cofitness_coinheritance][^conservation_fitness_synthesis]
- [metal-cross-resistance](../concepts/metal-cross-resistance.md) — metal-responsive ICA modules connect shared fitness architecture with cross-metal stress responses. [^metal_fitness_atlas]
- [multi-omics-integration](../concepts/multi-omics-integration.md) — module-level fitness activity motivates integration with regulatory and expression measurements. [^metal_fitness_atlas]
- [kescience-fitnessbrowser](kescience-fitnessbrowser.md) — Fitness Browser matrices supplied the fitness data analyzed with ICA. [^amr_cofitness_networks]

[^amr_cofitness_networks]: [amr cofitness networks](../summaries/amr_cofitness_networks__REPORT.md)
[^annotation_gap_discovery]: [annotation gap discovery](../summaries/annotation_gap_discovery__REPORT.md)
[^counter_ion_effects]: [counter ion effects](../summaries/counter_ion_effects__REPORT.md)
[^essential_genome]: [essential genome](../summaries/essential_genome__REPORT.md)
[^fitness_modules]: [fitness modules](../summaries/fitness_modules__REPORT.md)
[^functional_dark_matter]: [functional dark matter](../summaries/functional_dark_matter__REPORT.md)
[^truly_dark_genes]: [truly dark genes](../summaries/truly_dark_genes__REPORT.md)
[^discoveries]: [discoveries](../summaries/discoveries.md)
[^cofitness_coinheritance]: [cofitness coinheritance](../summaries/cofitness_coinheritance__REPORT.md)
[^module_conservation]: [module conservation](../summaries/module_conservation__REPORT.md)
[^field_vs_lab_fitness]: [field vs lab fitness](../summaries/field_vs_lab_fitness__REPORT.md)
[^metal_fitness_atlas]: [metal fitness atlas](../summaries/metal_fitness_atlas__REPORT.md)
[^metal_specificity]: [metal specificity](../summaries/metal_specificity__REPORT.md)
[^conservation_fitness_synthesis]: [conservation fitness synthesis](../summaries/conservation_fitness_synthesis__REPORT.md)
