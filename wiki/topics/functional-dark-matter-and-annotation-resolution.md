---
type: "Topic"
description: "In this corpus, \"dark\" genes are genes that lack functional annotation: hypothetical proteins, DUFs (domains of unknown function) and uncharacterized proteins ."
sources: []
---
# Functional Dark Matter and Annotation Resolution

In this corpus, "dark" genes are genes that lack functional annotation: hypothetical proteins, DUFs (domains of unknown function) and uncharacterized proteins .

No overview of this topic has passed review. Its concept pages follow.

## Literature Context

The candidate papers establish that unannotated genes are a large, well-recognised fraction of bacterial genomes. One review states that 25-50% of a bacterial genome comprises hypothetical proteins (HPs) [PMID 35422211](https://pubmed.ncbi.nlm.nih.gov/35422211/). A survey of over 27 000 bacterial genomes from the Genome Taxonomy Database found that 52 and 79 % of the average bacterial proteome could be annotated by protein-based and domain-based homology searches, respectively [PMID 32124724](https://pubmed.ncbi.nlm.nih.gov/32124724/). Coverage by protein homology ranged from as low as 14 % in some species to as high as 98 % in others. Taxonomy was a major factor, and the lowest completeness was in Patescibacteria. Genome size was associated with annotation incompleteness, likely because accessory proteomes are less characterised than core proteomes. Research bias also mattered: early model organisms showed high completeness relative to other genomes in their own lineages [PMID 32124724](https://pubmed.ncbi.nlm.nih.gov/32124724/).

Most other candidates are single-organism efforts to resolve HPs. For Mycobacterium tuberculosis, orthology assigned annotations to 497 genes, and genomic-context analysis and literature mining linked another 125 to interacting proteins. This raised the fraction of the proteome with some functional annotation to 88% [PMID 22485162](https://pubmed.ncbi.nlm.nih.gov/22485162/). A separate functional interaction network was used to predict functions for M. tuberculosis HPs and to compare their network properties with those of known proteins [PMID 22837694](https://pubmed.ncbi.nlm.nih.gov/22837694/). A domain-screening and structure-based study of M. tuberculosis HPs went on to epitope prediction for prioritising targets [PMID 27374154](https://pubmed.ncbi.nlm.nih.gov/27374154/). Reannotating Mycoplasma hyopneumoniae HPs assigned putative functions to 159 of 244 proteins and raised genome annotation from 65% to 87%. It also flagged potential virulence factors [PMID 34864146](https://pubmed.ncbi.nlm.nih.gov/34864146/). Bacillus studies assigned functions to 37 of 414 HPs [PMID 36228026](https://pubmed.ncbi.nlm.nih.gov/36228026/) and 56 of 1007 HPs [PMID 40092810](https://pubmed.ncbi.nlm.nih.gov/40092810/). A Pseudomonas aeruginosa PAC1 study narrowed 828 HPs to two candidates [PMID 40854634](https://pubmed.ncbi.nlm.nih.gov/40854634/). A Coxiella burnetii study used in silico analysis to propose a role for one protein in adipogenesis and as a drug target [PMID 39039093](https://pubmed.ncbi.nlm.nih.gov/39039093/). These are computational predictions without experimental validation in the abstracts. The framing of HPs as drug targets and pathogenesis factors is reviewed in [PMID 35422211](https://pubmed.ncbi.nlm.nih.gov/35422211/).

The corpus's census and tiering of dark genes, and its finding that annotation coverage varies with annotation source and pipeline, are consistent with the survey evidence that completeness depends on method and taxonomy [PMID 32124724](https://pubmed.ncbi.nlm.nih.gov/32124724/). The hub's questions about reannotation lag, and about whether unannotated genes are accessory or core, extend that survey. They ask which genes resist newer pipelines and how their properties differ. The literature's resolution rates, such as 88% annotated in M. tuberculosis, are consistent with the idea that many HPs yield to newer tools [PMID 22485162](https://pubmed.ncbi.nlm.nih.gov/22485162/). The candidates also show that orthology, interaction networks and genomic context can assign function to HPs [PMID 22485162](https://pubmed.ncbi.nlm.nih.gov/22485162/), [PMID 22837694](https://pubmed.ncbi.nlm.nih.gov/22837694/). The corpus's guilt-by-association work, which uses cofitness and fitness modules, relates to these but uses different evidence. None of the candidates test the corpus's cofitness, fitness-module or pangenome-wide analyses, or its resource-darkness of compound catabolism, so those parts are novel relative to this set. The candidate papers also concern single genomes, whereas the corpus works across organisms.

## What the Corpus Shows

- [[concepts/annotation-based-false-negatives-in-comparative-presence-absence-searches|Annotation-based false negatives in comparative presence/absence searches]]: How text-matching (PaperBLAST) and curated-annotation (NCBI) searches differ in false-negative rates for presence/absence claims, and how naming conventions and unannotated paralogs limit them; stops at screening-method validity.
- [[concepts/annotation-coverage-and-resolution-in-genome-wide-cofitness-analysis|Annotation coverage and resolution in genome-wide cofitness analysis]]: How the coverage and uniformity of functional annotations (legacy SEED/KEGG versus InterProScan GO or Pfam) determine whether cofitness enrichment is detectable.
- [[concepts/annotation-pipeline-concordance-for-kegg-ortholog-calls|Annotation pipeline concordance for KEGG ortholog calls]]: How consistent KO assignments are between different annotation pipelines (Genome Depot versus eggNOG-mapper versus bakta) and how that limits cross-cohort comparisons.
- [[concepts/annotation-source-disagreement-and-coverage|Annotation source disagreement and coverage]]: How annotation sources (Bakta, eggNOG, UniRef50 bridges, KO assignments) differ in coverage and reliability, including false positives for specialty marker genes, and which source to use for which analysis; stops at dark-gene biology.
- [[concepts/census-and-evidence-depth-classification-of-functionally-dark-genes|Census and evidence-depth classification of functionally dark genes]]: How many bacterial genes lack functional annotation, how much residual evidence each carries (darkness tiers, partial clues), and how multi-evidence scoring ranks them for follow-up; stops short of the specific inference layers.
- [[concepts/classifier-and-database-limits-for-estimating-eukaryotic-read-fraction|Classifier and database limits for estimating eukaryotic read fraction]]: Which read classifiers and reference databases can measure eukaryotic fraction, and how far values are calibrated or comparable across data sources.
- [[concepts/conserved-metal-phenotype-gene-families-and-novel-metal-tolerance-candidates|Conserved metal-phenotype gene families and novel metal-tolerance candidates]]: Ortholog families with metal fitness phenotypes across organisms, whether specificity classes match metal-resistance annotations, and how unannotated candidate families differ in specificity, pleiotropy and pangenome conservation; stops at predictions awaiting validation.
- [[concepts/domain-based-marker-detection-and-annotation-method-bias|Domain-based marker detection and annotation-method bias]]: How the choice of detection evidence (eggNOG descriptions, specific or broad Pfam/InterPro domains, versioned domain IDs) changes marker-gene and defense prevalence estimates or produces false absences, and how to detect and recover them.
- [[concepts/function-prediction-for-uncharacterized-genes-by-guilt-by-association-and-ortholog-transfer|Function prediction for uncharacterized genes by guilt-by-association and ortholog transfer]]: How cofitness, module enrichment and fitness-module context transferred from orthologs are used to assign function to hypothetical or unannotated (including essential) genes, how far they reach and how they benchmark; stops at group construction.
- [[concepts/functional-annotation-of-amr-genes-and-mechanism-classification|Functional annotation of AMR genes and mechanism classification]]: How AMR genes are annotated and classified (COG categories, keyword mechanism classes, annotation depth, CARD ontology) and the limits of that classification.
- [[concepts/functional-characterization-of-plant-enriched-gene-families|Functional characterization of plant-enriched gene families]]: What the orthologous groups enriched in plant-associated species do, whether they are dark or characterized, and which mechanistic hypotheses they suggest.
- [[concepts/multi-evidence-triangulation-of-metabolic-annotation-gaps|Multi-evidence triangulation of metabolic annotation gaps]]: Whether combining gapfilling, fitness, pangenome conservation, GapMind and sequence homology can assign genes to gapfilled reactions, including dark reactions lacking EC numbers and how confidence tiers are set; stops at experimental validation.
- [[concepts/reannotation-lag-versus-genuinely-unannotatable-dark-genes|Reannotation lag versus genuinely unannotatable dark genes]]: How many genes labelled hypothetical are resolved by newer annotation pipelines versus remain unannotated, the properties of those that resist, and where archaeal and database-coverage bias enters; stops short of experimental function assignment.
- [[concepts/resource-darkness-of-compound-catabolism|Resource-darkness of compound catabolism]]: Covers how many candidate carbon compounds lack a linkable utilization determinant in queried resources, why they are dark, and how to prioritize them; it stops at the claim that dark means unlinked, not unknown to science.
- [[concepts/sequence-clustering-resolution-and-protein-family-definition|Sequence clustering resolution and protein family definition]]: How clustering thresholds (90/50/30% identity) shape the redundancy and family structure of a protein sequence collection, including the arbitrariness of cutoffs.
- [[concepts/sequence-composition-and-conservation-of-unannotatable-genes|Sequence composition and conservation of unannotatable genes]]: Comparison of length, GC, core/accessory status, essentiality and ortholog breadth between persistently unannotated and later-annotated genes, including confounds such as gene length.
- [[concepts/shallow-alphafold-msa-depth-and-annotation-of-conserved-core-genes|Shallow AlphaFold MSA depth and annotation of conserved core genes]]: Covers how AlphaFold multiple-sequence-alignment (MSA) depth relates to annotation richness (InterPro hits and families) across pangenome classes, including universally conserved but unannotated core genes with shallow MSAs; stops short of experimental characterisation of function.
- [[concepts/taxonomic-resolution-and-reference-database-limits-in-amplicon-profiling|Taxonomic resolution and reference database limits in amplicon profiling]]: How OTU versus exact-variant clustering and choice of 16S/ITS reference databases limit taxonomic assignment in amplicon studies.
- [[concepts/unknown-function-genes-in-niche-differentiated-accessory-genomes|Unknown-function genes in niche-differentiated accessory genomes]]: The large share of ecotype differentiation attributable to COG S (unknown function) genes and annotation gaps in niche-specific genes.
- [[concepts/unstudied-protein-families-and-the-literature-defined-dark-proteome|Unstudied protein families and the literature-defined dark proteome]]: How many protein families, defined by sequence clustering, have little or no literature, and how family size relates to literature coverage; stops at dark-family identification, not function assignment.
- [[concepts/validity-of-curated-metal-gene-annotation|Validity of curated metal-gene annotation]]: How reliable curated KEGG-ortholog lists and curated HMMs are for annotating metal processing and resistance genes, including cross-reactivity, weak 'other' categories, category overlaps, substrate-binding transporter gaps and absence of manual validation.

## Tensions and Caveats

Each concept page above states the tensions and caveats of its own evidence.

## Where to Go Deeper

- [[summaries/acinetobacter_adp1_explorer__REPORT]]
- [[summaries/alphafold_msa_annotation__REPORT]]
- [[summaries/amr_cofitness_networks__REPORT]]
- [[summaries/amr_environmental_resistome__REPORT]]
- [[summaries/amr_fitness_cost__REPORT]]
- [[summaries/amr_pangenome_atlas__REPORT]]
- [[summaries/annotation_gap_discovery__REPORT]]
- [[summaries/bacillota_b_subsurface_accessory__REPORT]]
- [[summaries/caulobacter_fur_lipida_loss__REPORT]]
- [[summaries/comprehensive_metal_ecology__REPORT]]
- [[summaries/discoveries]]
- [[summaries/ecotype_functional_differentiation__REPORT]]
- [[summaries/enigma_carbon_census_1__REPORT]]
- [[summaries/enigma_sso_asv_ecology__REPORT]]
- [[summaries/essential_genome__REPORT]]
- [[summaries/euk_in_prok_correlates__REPORT]]
- [[summaries/fitness_modules__REPORT]]
- [[summaries/functional_dark_matter__REPORT]]
- [[summaries/lanthanide_methylotrophy_atlas__REPORT]]
- [[summaries/lignin_community_enrichment__REPORT]]
- [[summaries/metal_fitness_atlas__REPORT]]
- [[summaries/metal_specificity__REPORT]]
- [[summaries/microbeatlas_metal_ecology__REPORT]]
- [[summaries/oak_ridge_cultivation_gap__REPORT]]
- [[summaries/paperblast_explorer__REPORT]]
- [[summaries/phage_defense_arsenal__REPORT]]
- [[summaries/phb_granule_ecology__REPORT]]
- [[summaries/pitfalls]]
- [[summaries/plant_microbiome_ecotypes__REPORT]]
- [[summaries/snipe_defense_system__REPORT]]
- [[summaries/truly_dark_genes__REPORT]]
