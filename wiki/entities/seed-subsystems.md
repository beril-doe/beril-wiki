---
type: "Dataset"
description: "SEED functional categories and subsystem annotations used to classify genes and to map pathway members to Fitness Browser genes."
sources: ["summaries/amr_cofitness_networks__REPORT.md", "summaries/cofitness_coinheritance__REPORT.md", "summaries/conservation_vs_fitness__REPORT.md", "summaries/core_gene_tradeoffs__REPORT.md", "summaries/costly_dispensable_genes__REPORT.md", "summaries/essential_genome__REPORT.md", "summaries/metabolic_capability_dependency__REPORT.md"]
aliases: ["SEED", "SEED annotations", "SEED functional categories", "SEED subsystems annotation"]
---
# SEED subsystems

This page covers SEED subsystems, the SEED functional categories and subsystem annotations used to classify genes and to map pathway members to Fitness Browser genes. Several projects use them to assign genes to functional categories. [src: cofitness_coinheritance, conservation_vs_fitness, core_gene_tradeoffs, essential_genome] One project also uses them as a proxy for pathway membership. [src: metabolic_capability_dependency] Annotation coverage and proxy noise limit some of the evidence. [src: costly_dispensable_genes, metabolic_capability_dependency]

## Key facts

- The conservation_vs_fitness report attributes SEED annotations to Overbeek et al. (2014) as a source of functional-category assignments. [src: conservation_vs_fitness]
- Several reports read the same file, `conservation_vs_fitness/data/seed_annotations.tsv`, for category assignments. These are cofitness_coinheritance, core_gene_tradeoffs and essential_genome. [src: cofitness_coinheritance, core_gene_tradeoffs, essential_genome]
- The metabolic_capability_dependency report took gene-level fitness scores for 48 organisms from the `genefitness`, `gene` and `seedannotation` tables of `kescience_fitnessbrowser`. It used SEED subsystems as a proxy for pathway membership. [src: metabolic_capability_dependency]

## Functional categories of essential and costly genes

Essential-core genes are enriched in some SEED categories and depleted in others. [src: conservation_vs_fitness]

- Essential-core genes are enriched in Protein Metabolism (+13.7 percentage points versus non-essential), Cofactors/Vitamins (+6.2%), Cell Wall (+3.9%) and Fatty Acid biosynthesis (+3.1%). [src: conservation_vs_fitness]
- They are depleted in Carbohydrates (-7.9%), Amino Acids (-5.6%) and Membrane Transport (-4.0%). The report describes these functions as tending to be conditionally important rather than universally essential. [src: conservation_vs_fitness]
- The top essential-auxiliary subsystems are ribosomes, DNA (deoxyribonucleic acid) replication, type 4 secretion and plasmid replication. The report suggests these are strain-specific variants of core machinery plus mobile genetic elements. [src: conservation_vs_fitness]

Costly but dispensable genes show a different pattern. See mobile element origin of costly non conserved genes.

- In costly+dispensable genes, 14 SEED top-level categories are significantly depleted (false discovery rate, FDR < 0.05). They include Protein Metabolism, Respiration, Carbohydrates, Amino Acids, Cofactors/Vitamins, Motility, Stress Response and RNA (ribonucleic acid) Metabolism. [src: costly_dispensable_genes]
- The category "Phages, Prophages, Transposable elements, Plasmids" is 11.7x enriched in costly+dispensable versus costly+conserved genes (FDR=1.3e-17). [src: costly_dispensable_genes]
- Virulence is 26.7x enriched (FDR=5.6e-14), but this rests on small counts of 21 versus 4 genes. [src: costly_dispensable_genes]

## Categories among co-fit, co-inherited pairs

Among gene pairs in the top quartile of both phi and co-fitness, the report counts genes by SEED category. Metabolism has 15,936 genes, and Transport has 11,940. [src: cofitness_coinheritance] Regulation has 6,339, and Motility has 2,929. [src: cofitness_coinheritance] Mobile elements has 2,716, and DNA metabolism has 2,490. [src: cofitness_coinheritance]

## Annotation quality as a limit

- SEED annotations cover 50.8% of costly+dispensable genes versus 74.9% of costly+conserved genes. [src: costly_dispensable_genes]
- SEED/KEGG annotations cover only 56-79% of genes in that analysis. The unannotated fraction may have different functional profiles. [src: costly_dispensable_genes]
- In antimicrobial resistance (AMR) cofitness support networks, old SEED annotations detected no significant enrichment (0/280 tests). The report calls this a demonstration that annotation quality matters. [src: amr_cofitness_networks]
- A permutation enrichment using old SEED annotations gave 23 significant tests out of 250 at FDR<0.05. The top signal was membrane/cell wall (24%, fold 1.12). [src: amr_cofitness_networks]

## Use as a pathway proxy

The metabolic_capability_dependency report used SEED subsystem annotations to map [[entities/gapmind]] pathway members to [[entities/fitness-browser]] genes for each organism. [src: metabolic_capability_dependency] The proxy has several limits:

- It introduces false positives from related subsystems. These dilute fitness signals and may misclassify pathways that differ in conservation. [src: metabolic_capability_dependency]
- GapMind deoxyribonate and myoinositol pathways had no matching SEED subsystem role descriptions and are absent from all analyses. [src: metabolic_capability_dependency]
- The full-name phenylalanine and tyrosine entries also lacked SEED coverage. Their phe and tyr equivalents were included through abbreviation-based matching. [src: metabolic_capability_dependency]
- Alanine appears in fitness metrics but was excluded from classification for all organisms. Fewer than 3 SEED-annotated genes met the minimum coverage threshold. [src: metabolic_capability_dependency]
- The report notes that direct gene-to-pathway mapping using GapMind gene assignments would improve precision. [src: metabolic_capability_dependency]

See also [[concepts/metabolic-capability-versus-fitness-dependency]] and [[concepts/essential-genes-and-core-genome-conservation]].
