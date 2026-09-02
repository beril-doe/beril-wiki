---
type: "Organism"
description: "Escherichia coli reference strain with fitness, pangenome, and disease-ecology evidence"
sources: ["summaries/annotation_gap_discovery__REPORT.md", "summaries/essential_metabolome__REPORT.md", "summaries/functional_dark_matter__REPORT.md", "summaries/ibd_phage_targeting__REPORT.md", "summaries/paperblast_explorer__REPORT.md", "summaries/webofmicrobes_explorer__REPORT.md", "summaries/conservation_vs_fitness__REPORT.md"]
---
# Escherichia coli

## Identity

Escherichia coli is a bacterial reference organism included in the cross-organism annotation-gap analysis. [src: annotation_gap_discovery]

Known aliases include E. coli and E. coli Keio (Keio). [src: annotation_gap_discovery]

A stable external identifier was not reported in this document. [src: annotation_gap_discovery]

## Findings in annotation-gap discovery

E. coli Keio was one of 14 organisms selected for analysis using carbon-source Fitness Browser data and random-barcode transposon sequencing (RB-TnSeq), a method that measures genome-wide mutant fitness with barcoded transposon libraries. [src: annotation_gap_discovery]

For E. coli Keio, 7 gapfilled reaction-organism pairs were evaluated and 4 were resolved, giving a reported resolution rate of 57.1%. [src: annotation_gap_discovery]

The E. coli Keio result contributed to the study's cross-organism integration of metabolic-model gapfilling, fitness phenotypes, pangenome annotations, GapMind pathway evidence, and BLAST homology. [src: annotation_gap_discovery]

The analysis used draft metabolic models based on ModelSEED and RAST annotations and evaluated them with flux-balance analysis (FBA), a constraint-based method for predicting metabolic flux and growth. [src: annotation_gap_discovery]

## Pangenome and GapMind coverage

The essential-metabolome analysis found 0 GapMind predictions for the E. coli K-12 Keio genome, GCF_000005845.2, in the KBase pangenome collection. [src: essential_metabolome] This missing coverage was attributed to E. coli's exclusion from GTDB pangenome construction because it had too many genomes for species-level analysis, contributing to reduction of the intended 45-organism analysis to a 7-organism pilot. [src: essential_metabolome]

The conservation-versus-fitness analysis **refines** that context: although the main Escherichia coli clade was absent because it contained too many genomes, E. coli BW25113/Keio mapped to the small s__Escherichia_coli_E clade at only 26.1% coverage. [src: conservation_vs_fitness] This supports interpreting the missing GapMind and limited pangenome evidence as coverage and clade-construction constraints rather than evidence that E. coli lacks conserved genes. [src: conservation_vs_fitness]

## Fitness Browser and Web of Microbes integration

The Web of Microbes (WoM) analysis **supports** E. coli Keio's role as a reference strain by matching E. coli BW25113 to the Fitness Browser's Keio record, with 4,610 genes and 168 experiments. [src: webofmicrobes_explorer] This **refines** the broader carbon-source fitness evidence: the WoM BW25113 record contained only 12 observations focused on sulfur metabolism in ZMMG medium, despite the richer Keio Fitness Browser resource. [src: webofmicrobes_explorer]

## Functional dark-matter prioritization

The functional-dark-matter analysis **supports** E. coli Keio's role as an experimentally useful reference by ranking E. coli Keio 14796 among its highest-priority essential dark-gene candidates, with score 0.875 and a YbeY domain prediction. [src: functional_dark_matter] Because essential genes lack viable RB-TnSeq mutants, the report recommends CRISPRi (CRISPR interference, transcriptional knockdown) followed by growth measurements under standard and stress conditions; this **refines** the earlier fitness-based characterization with a direct strategy for testing essential, uncharacterized genes. [src: functional_dark_matter]

## Literature coverage

PaperBLAST further **supports** E. coli's status as a heavily studied bacterial reference: E. coli K-12 had 8,860 papers, second among the three leading bacterial organisms in the collection after Mycobacterium tuberculosis H37Rv (9,079) and ahead of Pseudomonas aeruginosa PAO1 (5,928). [src: paperblast_explorer] This literature concentration **refines** the experimental-reference picture with a resource-level measure of research attention, while PaperBLAST's text-mining and open-access limitations mean paper counts do not establish complete functional characterization. [src: paperblast_explorer]

## IBD pathobiont and phage-targeting evidence

The IBD analysis **extends** E. coli's reference-organism evidence into disease-associated ecology: E. coli was one of six actionable Tier-A pathobionts, with total score 3.6, and was among five donor-2708-engraftment pathobionts that passed the confound-free CD-up test, with CLR-Δ = +1.43. [src: ibd_phage_targeting]

The analysis **supports** an E. coli-centered iron and genotoxin mechanism: E. coli correlated with heme biosynthesis at ρ = 0.640, had mean ρ = +0.45 with 15 iron pathways, and alone among the six actionable core species carried the iron-plus-genotoxin MIBiG signature, including 19 Yersiniabactin, 16 Enterobactin, 8 Colibactin, and 15 Microcin B17 BGCs. [src: ibd_phage_targeting]

The paired metabolomics analysis further associated E. coli with cadaverine at ρ = +0.45, and with choline and tryptophan at +0.25 for each; these findings **refine** the earlier multi-omics characterization but do not establish causality. [src: ibd_phage_targeting]

E. coli had direct phage evidence in PhageFoundry: the five-phage cocktail DIJ07_P2, LF73_P1, AL505_Ev3, 55989_P2, and LF110_P2 covered 94.7 % of 188 tested E. coli strains, although the dataset did not establish in-vivo efficacy or distinguish AIEC from commensal strains. [src: ibd_phage_targeting]

## Related pages

- [[summaries/annotation_gap_discovery__REPORT]] — source summary for the cross-organism annotation-gap study. [src: annotation_gap_discovery]
- [[summaries/conservation_vs_fitness__REPORT]] — source summary for linking Fitness Browser essentiality to pangenome conservation. [src: conservation_vs_fitness]
- [[summaries/essential_metabolome__REPORT]] — source summary for the GapMind essential-metabolome pilot. [src: essential_metabolome]
- [[summaries/functional_dark_matter__REPORT]] — source summary for essential dark-gene prioritization. [src: functional_dark_matter]
- [[summaries/ibd_phage_targeting__REPORT]] — source summary for IBD pathobiont prioritization and phage-cocktail design. [src: ibd_phage_targeting]
- [[summaries/paperblast_explorer__REPORT]] — source summary for PaperBLAST literature-coverage and protein-family analysis. [src: paperblast_explorer]
- [[summaries/webofmicrobes_explorer__REPORT]] — source summary for Web of Microbes cross-collection integration. [src: webofmicrobes_explorer]
- [[concepts/metabolic-model-gapfilling]] — the study resolved 4 of 7 E. coli Keio gapfilled pairs. [src: annotation_gap_discovery]
- [[concepts/gene-essentiality]] — E. coli Keio 14796 was prioritized as an essential dark-gene candidate for CRISPRi testing. [src: functional_dark_matter]
- [[concepts/condition-specific-fitness]] — E. coli Keio was analyzed using carbon-source fitness measurements. [src: annotation_gap_discovery]
- [[concepts/pangenome-integration]] — pangenome evidence was part of the candidate-gene assignment pipeline, while conservation-versus-fitness analysis exposed limited E. coli clade coverage. [src: annotation_gap_discovery; conservation_vs_fitness]
- [[concepts/multi-omics-integration]] — the studies combined fitness, annotation, pathway, homology, and metabolic-model evidence; the IBD analysis adds taxonomy–metabolomics and BGC evidence. [src: annotation_gap_discovery; ibd_phage_targeting]
- [[entities/kescience-fitnessbrowser]] — source of the organism's carbon-source fitness data. [src: annotation_gap_discovery]
- [[entities/tnseq]] — method family underlying the RB-TnSeq measurements. [src: annotation_gap_discovery]
- [[entities/modelseed]] — source of metabolic-model annotations and gapfilling reactions. [src: annotation_gap_discovery]
- [[entities/gapmind]] — pathway-completeness method whose collection lacked predictions for the Keio genome. [src: essential_metabolome]
- [[entities/gtdb]] — pangenome construction context associated with the missing GapMind coverage. [src: essential_metabolome]
