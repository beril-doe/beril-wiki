---
type: "Topic"
description: "This topic asks how far genome-derived metabolic predictions can be trusted."
sources: []
---
# Metabolic Models and Pathway-Level Evidence

This topic asks how far genome-derived metabolic predictions can be trusted.

No overview of this topic has passed review. Its concept pages follow.

## What the Corpus Shows

- [[concepts/annotation-coverage-bias-in-chemical-class-callability|Annotation-coverage bias in chemical-class callability]]: Covers whether the chemical class or physicochemical properties of a compound predict whether its catabolism can be called from genomes, and how annotation coverage confounds this; it stops at class-level tests with small numbers of callables.
- [[concepts/catabolic-direction-filtering-and-mis-scored-carbon-calls|Catabolic-direction filtering and mis-scored carbon calls]]: Covers how reaction-direction and carbon-versus-nitrogen filters, signature completeness and certainty scoring decide which compounds count as callable, and the errors they introduce.
- [[concepts/coarse-cog-fraction-proxies-versus-pathway-level-stress-evidence|Coarse COG-fraction proxies versus pathway-level stress evidence]]: Limits of broad COG-category functional proxies, annotation conventions and genus aggregation for detecting metal-response functional effects.
- [[concepts/compound-identifier-ambiguity-in-linking-metabolites-to-metabolic-models|Compound identifier ambiguity in linking metabolites to metabolic models]]: How exact-name versus formula-only matching of measured metabolites to biochemistry databases and pathway tools yields definitive, ambiguous or failed links; stops at the matching step, not model predictions.
- [[concepts/concordance-of-genome-scale-metabolic-model-predictions-with-experimental-data|Concordance of genome-scale metabolic model predictions with experimental data]]: How well flux balance analysis and draft automated model predictions agree with experimental gene essentiality (TnSeq or knockout lethality) and carbon-source growth, and how gapfilling and media assumptions limit that agreement; stops at growth-rate prediction within dispensable genes.
- [[concepts/cross-database-concordance-of-metabolite-evidence|Cross-database concordance of metabolite evidence]]: How well exometabolomic, mutant-fitness, species-phenotype and pathway-prediction databases agree on the same metabolites, and how matching coverage, circularity and medium differences limit that comparison.
- [[concepts/disagreement-among-deltag-estimation-methods|Disagreement among deltaG estimation methods]]: How much the choice of deltaG estimation tool (eQuilibrator, dGPredictor) and pKa source (Marvin vs OPAM2, via the Legendre transform) changes reaction free-energy estimates and sign calls; stops at downstream flux effects.
- [[concepts/effect-of-pka-source-on-flux-predictions-across-diverse-organisms|Effect of pKa source on flux predictions across diverse organisms]]: Whether Marvin versus OPAM2 deltaG changes alter TMFA flux distributions, blocked reactions, or growth across phylogenetically diverse models; stops at experimental validation.
- [[concepts/genome-predicted-pathway-completeness-and-community-metabolite-chemistry|Genome-predicted pathway completeness and community metabolite chemistry]]: Whether GapMind pathway completeness aggregated across taxa predicts community metabolite chemistry; stops at gene presence versus expression and annotation limits.
- [[concepts/limits-of-keyword-and-marker-based-functional-annotation|Limits of keyword and marker-based functional annotation]]: How keyword scanning, eggNOG OG tiers, and wrong or unavailable KO markers cause missed or spurious functional signals, and how multi-signal detection (PFAM plus motif counting) corrects them.
- [[concepts/measured-fitness-as-independent-evidence-of-carbon-utilization|Measured fitness as independent evidence of carbon utilization]]: Covers using measured carbon-source fitness experiments in reference organisms to call compound utilization independently of genome-annotation filters, and its limits for target isolates.
- [[concepts/metabolic-capability-versus-fitness-dependency|Metabolic capability versus fitness dependency]]: Whether a genomically complete metabolic pathway is actually needed for growth, comparing GapMind pathway-completeness predictions with measured growth and RB-TnSeq fitness, including pathway-to-gene mapping and coverage limits; stops at pangenome-level evolutionary inference.
- [[concepts/metabolic-model-prediction-of-growth-defects-among-dispensable-genes|Metabolic model prediction of growth defects among dispensable genes]]: Whether FBA class or flux predicts quantitative mutant growth defects among genes dispensable by TnSeq, including threshold sensitivity and per-carbon-source correlations; stops at lethality calls.
- [[concepts/metabolic-pathway-gap-filling-by-unannotated-genes|Metabolic pathway gap-filling by unannotated genes]]: Whether dark genes co-occurring with nearly complete pathways could encode missing enzymatic steps, using GapMind pathway calls and curated domain matching; limited to organism-level co-occurrence.
- [[concepts/module-level-enrichment-artifacts-from-broad-substrate-enzymes|Module-level enrichment artifacts from broad-substrate enzymes]]: How pathway-module enrichment can be driven by generic or broad-substrate KOs, and how per-KO step dissection (e.g. limonene degradation) corrects false-positive pathway calls.
- [[concepts/nadh-flux-rate-versus-nadh-yield-as-determinant-of-complex-i-dependence|NADH flux rate versus NADH yield as determinant of Complex I dependence]]: Covers whether the rate or concentration of NADH production, rather than total NADH yield per carbon, explains dependence on Complex I across substrates, including stoichiometric evidence and untested predictions.
- [[concepts/ontology-versus-name-pattern-categorization-in-pathway-enrichment-tests|Ontology versus name-pattern categorization in pathway enrichment tests]]: How the choice of category schema (regex on pathway names versus a curated class hierarchy) can reverse a pathway-enrichment verdict on identical data; stops at the specific biology of the enriched themes.
- [[concepts/pathway-completeness-inference-from-ko-annotations-and-pleiotropic-enzymes|Pathway completeness inference from KO annotations and pleiotropic enzymes]]: How reliably a biosynthetic pathway can be called from eggNOG/KEGG KO annotations, including pleiotropic precursor enzymes, missing regulators and failed domain-class assignment.
- [[concepts/predictability-of-binary-growth-phenotypes-from-gene-content|Predictability of binary growth phenotypes from gene content]]: How well KEGG ortholog presence/absence, and pathway-completeness rules compared with machine-learning models (with or without literature-corpus transfer), predict whether a genome grows on a substrate, by condition class and held-out genus; stops at continuous growth kinetics.
- [[concepts/predictability-of-continuous-growth-kinetics-from-gene-content|Predictability of continuous growth kinetics from gene content]]: Whether growth rate, lag time and yield can be predicted from KO presence/absence or bulk genome features under cross-genus holdout, and what features might be needed instead; it stops at binary growth.
- [[concepts/reliability-and-coverage-limits-of-gapmind-pathway-predictions|Reliability and coverage limits of GapMind pathway predictions]]: How far GapMind genome-derived pathway completeness calls can be trusted: database coverage gaps, score-category and scope aggregation, resolution for niche-specific metabolism, and agreement with ModelSEED gapfilling; stops at links to fitness and community chemistry.
- [[concepts/reliability-of-kegg-ortholog-markers-for-multi-heme-cytochrome-iron-reduction|Reliability of KEGG ortholog markers for multi-heme cytochrome iron reduction]]: How misidentified or non-canonical KEGG orthologs corrupted an iron-reduction marker analysis and how a domain-and-motif multi-heme cytochrome detector replaces them; stops at marker-calling methodology.
- [[concepts/species-level-conservation-of-metabolic-pathways-across-pangenomes|Species-level conservation of metabolic pathways across pangenomes]]: Whether GapMind pathway predictions on isolates generalize across genomes of a species, with clade-definition caveats; stops at pathogen genomes.
- [[concepts/sphingolipid-and-shared-lpt-transport-in-lipid-a-deficient-bacteria|Sphingolipid and shared Lpt transport in lipid A-deficient bacteria]]: Whether sphingolipid biosynthesis is induced or constitutive during lipid A loss and whether the sphingolipid transporters share the LPS Lpt machinery; stops at Caulobacter transcript and proteome evidence.
- [[concepts/systematic-blind-spots-of-flux-balance-models-for-condition-specific-requirements|Systematic blind spots of flux balance models for condition-specific requirements]]: Where flux balance models miss condition-specific gene requirements (aromatic catabolism medium assumptions, cofactor supply, iron, respiratory capacity, threshold effects) and which genes lack reaction mappings; stops at growth-defect quantification among dispensable genes.
- [[concepts/thermodynamic-constraint-formulation-in-flux-balance-models|Thermodynamic constraint formulation in flux balance models]]: How hard deltaG cutoffs versus concentration-aware TMFA constraints affect growth, flux, directionality and carbon-source growth predictions (12-condition panel) in genome-scale models.

## Tensions and Caveats

Each concept page above states the tensions and caveats of its own evidence.

## Where to Go Deeper

- [[summaries/acinetobacter_adp1_explorer__REPORT]]
- [[summaries/adp1_triple_essentiality__REPORT]]
- [[summaries/annotation_gap_discovery__REPORT]]
- [[summaries/aromatic_catabolism_network__REPORT]]
- [[summaries/bacillota_b_subsurface_accessory__REPORT]]
- [[summaries/caulobacter_fur_lipida_loss__REPORT]]
- [[summaries/cf_formulation_design__REPORT]]
- [[summaries/clay_confined_subsurface__REPORT]]
- [[summaries/discoveries]]
- [[summaries/enigma_carbon_census_1__REPORT]]
- [[summaries/enigma_contamination_functional_potential__REPORT]]
- [[summaries/essential_metabolome__REPORT]]
- [[summaries/functional_dark_matter__REPORT]]
- [[summaries/fw300_metabolic_consistency__REPORT]]
- [[summaries/gene_function_ecological_agora__REPORT]]
- [[summaries/genotype_to_phenotype_enigma__REPORT]]
- [[summaries/ibd_phage_targeting__REPORT]]
- [[summaries/lanthanide_methylotrophy_atlas__REPORT]]
- [[summaries/metabolic_capability_dependency__REPORT]]
- [[summaries/neon_mag_functional_discovery__REPORT]]
- [[summaries/nmdc_community_metabolic_ecology__REPORT]]
- [[summaries/pathway_capability_dependency__REPORT]]
- [[summaries/pgp_pangenome_ecology__REPORT]]
- [[summaries/phb_granule_ecology__REPORT]]
- [[summaries/pitfalls]]
- [[summaries/plant_microbiome_ecotypes__REPORT]]
- [[summaries/prophage_amr_comobilization__REPORT]]
- [[summaries/pseudomonas_carbon_ecology__REPORT]]
- [[summaries/respiratory_chain_wiring__REPORT]]
- [[summaries/thermodynamic_impact__REPORT]]
- [[summaries/webofmicrobes_explorer__REPORT]]
