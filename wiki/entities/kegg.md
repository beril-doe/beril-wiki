---
type: "Dataset"
description: "Dataset for genes, pathways, and functional annotations"
sources: ["summaries/enigma_carbon_census_1__REPORT.md", "summaries/fitness_modules__REPORT.md", "summaries/genotype_to_phenotype_enigma__REPORT.md", "summaries/metal_fitness_atlas__REPORT.md", "summaries/truly_dark_genes__REPORT.md"]
---
# KEGG

## What this entity is

KEGG is the canonical dataset name used for the Kyoto Encyclopedia of Genes and Genomes resource in the ENIGMA Carbon Census. [src: enigma_carbon_census_1] Known alias: Kyoto Encyclopedia of Genes and Genomes. [src: enigma_carbon_census_1] No stable external identifier for this dataset was reported in the source document. [src: enigma_carbon_census_1]

KEGG is also used as a genome, pathway, and functional-annotation dataset in genotype-to-phenotype modeling, where KEGG orthologs (KOs) represent gene-level functional features. [src: genotype_to_phenotype_enigma] This **supports** KEGG's role as a broad pathway and functional reference while **refining** its use from compound-pathway linkage to genome-content-based phenotype prediction. [src: genotype_to_phenotype_enigma] The Pan-Bacterial Metal Fitness Atlas further **supports** this genome-content role by deriving a 1,286-KO metal functional signature for pangenome-scale analysis. [src: metal_fitness_atlas]

## Key facts from the ENIGMA Carbon Census

KEGG links were part of the census workflow connecting compound identities from [[entities/pubchem]] to reactions, pathways, and genome annotations. [src: enigma_carbon_census_1] Of the 83 enrichment compounds examined, 54 were linked to KEGG. [src: enigma_carbon_census_1]

The census identified 74/83 compounds (89%) as organism-dark, meaning that their genetic determinants of utilization were not linkable through the queried BERDL and curated resources. [src: enigma_carbon_census_1] Within that dark set, 33 compounds were KEGG-linked but had no reaction in the queried genomes, while 29 were fully orphan compounds with no KEGG link. [src: enigma_carbon_census_1]

The KEGG-linked evidence contributed to a tiered compound-to-organism workflow that also used [[entities/modelseed]], [[entities/gtdb]], ENIGMA genome-depot data, and measured fitness data. [src: enigma_carbon_census_1] The workflow resolved all 83 compounds to structures with InChIKeys, linked 54 to KEGG, and produced 9 callable compounds under the project definition before the xanthine carbon-catabolism correction. [src: enigma_carbon_census_1]

The project reported that xanthine was mis-scored as carbon-catabolic because reaction R02107, xanthine→urate, represents purine nitrogen acquisition rather than carbon catabolism. [src: enigma_carbon_census_1] Removing R02107 from the carbon allowlist reduced the effective carbon-callable set from 9 to 8, although committed tables still contained xanthine because they were not regenerated. [src: enigma_carbon_census_1]

KEGG representation was also part of the reported annotation ceiling: the callable compounds had median Complexity 133 versus 207 for dark compounds, with p=0.034, but the source cautioned that this pattern may reflect database and annotation coverage as much as biological bioavailability. [src: enigma_carbon_census_1]

## Role in genotype-to-phenotype prediction

The genotype-to-phenotype study **supports** KEGG's use as a genome-content reference: its combined modeling corpus contained 46,389 genome × condition pairs across 727 genomes and 363 conditions, with 4,293 shared KOs. [src: genotype_to_phenotype_enigma] Hierarchical clustering used 7,167 KO presence/absence features across 123 strains to identify 8 metabolic guilds spanning 20 taxonomic orders. [src: genotype_to_phenotype_enigma]

In the initial seven-strain model, 4,305 prevalence-filtered KO features were combined with 23 COG classes, condition variables, phylogeny, and bulk genome features; the model achieved AUC 0.633 under leave-one-strain-out validation. [src: genotype_to_phenotype_enigma] In the full corpus, LightGBM modeling used the 4,293 shared KOs, and adding KO × condition interactions increased mean AUC from 0.620 to 0.653, an improvement of 0.032, in 80 of 106 held-out genera. [src: genotype_to_phenotype_enigma]

This **refines** the earlier annotation-ceiling interpretation: KEGG-derived gene-content features supported prediction of binary growth capability for some conditions, but continuous µmax, lag, and yield-related max_A were not predictable under genus-blocked holdout from KO presence/absence or bulk genomic features. [src: genotype_to_phenotype_enigma] The study therefore distinguishes KEGG-level capacity to encode whether an organism can use a substrate from kinetic properties that depend on enzyme kinetics, expression, regulation, and ribosome efficiency. [src: genotype_to_phenotype_enigma]

The metal-fitness analysis **refines** this result rather than simply contradicting it: the 1,286-KO metal signature was scored across 27,702 pangenome species, but a simple gene-presence repertoire score failed to predict metal fitness. [src: metal_fitness_atlas] This contrast indicates that KO presence can support some condition-specific capability prediction while remaining insufficient for metal-fitness prediction, where regulation, expression, exposure, and context are important. [src: metal_fitness_atlas]

After genome-size normalization by metal clusters divided by total KEGG-annotated clusters, *Leptospirillum* ranked at the 91st percentile, *Acidithiobacillus* at the 77th, *Marinobacter* at the 75th, and *Sulfobacillus* at the 71st; bioleaching genera were not significantly enriched over background (Mann-Whitney p=0.17). [src: metal_fitness_atlas] Without normalization, species with large open pangenomes, including *K. pneumoniae* and *P. aeruginosa*, dominated scores because of genome size. [src: metal_fitness_atlas]

## Relation to persistent annotation gaps

The truly-dark-gene analysis **refines** the annotation-ceiling interpretation by showing that KEGG often recognizes sequence-level similarity without assigning a functional KO: only 4.6% of truly dark genes had KEGG KOs, although 84.7% had database cross-references and 79.4% had UniRef50 links. [src: truly_dark_genes] Among 5,870 unique truly dark gene clusters, the report found only 6 KEGG entries and 1 EC number in cross-reference data. [src: truly_dark_genes] This **supports** treating KEGG as a broad but incomplete functional reference, especially for short, accessory, taxonomically restricted genes that remain hypothetical after Bakta reannotation. [src: truly_dark_genes] These findings are summarized in [[summaries/truly_dark_genes__REPORT]].

## Relation to fitness-module annotation

The fitness-module analysis **refines** KEGG's role by showing that KEGG KOs are gene-level assignments and are poorly suited to assigning exact functions to independently decomposed fitness modules: in held-out benchmarking, ortholog transfer achieved 95.8% strict precision, 91.2% coverage, and 0.934 F1, whereas Module-ICA achieved <1% strict precision and 23.3% coverage. [src: fitness_modules] The report therefore treats ICA modules as process-level context rather than KO identities, while retaining KEGG enrichment as one source of module annotation. [src: fitness_modules]

This **supports** the existing annotation-ceiling interpretation: KEGG provided the broadest pathway and functional reference in the compound workflow, but KEGG's gene-specific granularity limits direct transfer to multi-gene fitness modules. [src: fitness_modules] In the fitness-module analysis, lowering the enrichment-overlap threshold from 3 to 2 and adding PFam increased the module annotation rate from 8% to 80%; KEGG KOs were too gene-specific for module-level enrichment. [src: fitness_modules]

## Related pages

- [[summaries/enigma_carbon_census_1__REPORT]] — source summary for the ENIGMA Carbon Census. [src: enigma_carbon_census_1]
- [[summaries/fitness_modules__REPORT]] — source summary for pan-bacterial fitness-module analysis. [src: fitness_modules]
- [[summaries/genotype_to_phenotype_enigma__REPORT]] — source summary for genotype-to-phenotype prediction from ENIGMA growth curves. [src: genotype_to_phenotype_enigma]
- [[summaries/metal_fitness_atlas__REPORT]] — source summary for the pan-bacterial metal fitness atlas. [src: metal_fitness_atlas]
- [[summaries/truly_dark_genes__REPORT]] — source summary for persistent unknown genes after modern annotation. [src: truly_dark_genes]
- [[concepts/metabolic-model-gapfilling]] — KEGG-linked/no-reaction compounds define pathway-linkage gaps. [src: enigma_carbon_census_1]
- [[concepts/cross-tenant-data-bridging]] — the census connected KEGG with compound, genome, fitness, taxonomy, and environmental resources. [src: enigma_carbon_census_1]
- [[concepts/multi-omics-integration]] — KEGG annotations were integrated with chemical, fitness, taxonomic, and metagenomic evidence. [src: enigma_carbon_census_1]
- [[concepts/pangenome-integration]] — KEGG pathway and enzyme annotations were linked across genome collections, including the metal-fitness pangenome signature. [src: enigma_carbon_census_1, metal_fitness_atlas]
- [[entities/pubchem]] — source of compound structure resolution before KEGG linkage. [src: enigma_carbon_census_1]
- [[entities/modelseed]] — complementary metabolic annotation resource in the workflow. [src: enigma_carbon_census_1]
