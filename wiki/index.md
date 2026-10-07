# BERIL Knowledge Wiki

Most of these projects analysed data already in the [KBase Data Lakehouse](https://hub.berdl.kbase.us); a few brought their own. See [[about|About This Wiki]] for what that means for citing anything here.

This wiki compiles the reports of the BERIL Research Observatory. In this observatory, AI agents conduct microbial-biology research over the KBase Data Lakehouse. Each project report records one investigation. Two cross-project digests collect the discoveries and the pitfalls that recur across projects.

Start with the topics. Each topic hub introduces a research question and links to the concept pages that argue it across projects. Concept pages synthesize evidence from several reports and cite each claim to its source project. Entity pages describe specific organisms, genes, compounds, methods and datasets. Summary pages condense a single report and list the concepts it feeds.

## Topics

- [[topics/gene-fitness-landscapes-and-cofitness-modules|Gene Fitness Landscapes and Cofitness Modules]] (11 concepts): Groups genes by how disrupting them changes growth across many conditions. Cofitness measures how similar two genes' fitness profiles are across conditions, and a fitness module is a group of genes with coordinated fitness patterns across experiments.
- [[topics/gene-essentiality-and-perturbation-assay-validity|Gene Essentiality and Perturbation-Assay Validity]] (6 concepts): Treats direct perturbation and measured growth as the strongest evidence of essentiality, treats conservation, annotation and modeling as predictors, and tests the measurements themselves.
- [[topics/laboratory-fitness-versus-natural-selection-and-gene-conservation|Laboratory Fitness Versus Natural Selection and Gene Conservation]] (6 concepts): Asks whether a gene's laboratory growth effect explains whether a species keeps or loses it in nature. Several projects link genome-wide mutant fitness data from the Fitness Browser, measured by random barcode transposon sequencing (RB-TnSeq), to conservation across the pangenome, the full set of gene clusters across a species' genomes.
- [[topics/pangenome-structure-and-genome-evolution|Pangenome Structure and Genome Evolution]] (9 concepts): Splits a species' gene clusters into a core, the conserved component, and auxiliary genes that vary between genomes. Projects set the core threshold in different ways.
- [[topics/ecotypes-and-environmental-gene-content-differentiation|Ecotypes and Environmental Gene-Content Differentiation]] (7 concepts): Asks whether environment shapes which accessory genes bacteria carry. One broad test covers 172 species, and many targeted tests ask where any such signal sits.
- [[topics/metabolic-traits-auxotrophy-and-community-dependence|Metabolic Traits, Auxotrophy, and Community Dependence]] (12 concepts): Reads pathway gaps in genomes as possible auxotrophies, meaning dependence on an externally supplied nutrient, and asks whether shared metabolites let community members lose costly functions. The corpus pairs GapMind, a predictor of pathway completeness, with measured gene-fitness data.
- [[topics/metabolic-models-and-pathway-level-evidence|Metabolic Models and Pathway-Level Evidence]] (6 concepts): Asks how far genome-derived metabolic predictions can be trusted. It covers genome-scale models run with flux balance analysis (FBA), a constraint-based method that predicts feasible metabolic fluxes and growth, and pathway-completeness calls from GapMind.
- [[topics/lanthanide-dependent-methylotrophy|Lanthanide-Dependent Methylotrophy]] (3 concepts): Follows the use of rare-earth elements as cofactors for methanol oxidation by the xoxF methanol dehydrogenase. The calcium-dependent mxaF form contrasts with it.
- [[topics/functional-dark-matter-and-annotation-resolution|Functional Dark Matter and Annotation Resolution]] (9 concepts): Separates genes that lack functional annotation from genes that lack connected publications. A gene without text-mined papers may still carry curated knowledge.
- [[topics/resistance-defense-systems-and-mobile-elements|Resistance, Defense Systems, and Mobile Elements]] (7 concepts): Brings together antimicrobial-resistance genes, metal tolerance and anti-phage defense with the mobile genetic elements that can move these functions between genomes.
- [[topics/sampling-coverage-and-statistical-confounding|Sampling Coverage and Statistical Confounding]] (14 concepts): Asks when an apparent microbial pattern reflects biology and when it reflects which samples were collected or how the analysis was built.
- [[topics/data-infrastructure-provenance-and-research-practice|Data Infrastructure, Provenance, and Research Practice]] (8 concepts): Covers how data in the KBase Data Lakehouse is owned, named, joined and ingested. Several projects audit the platform itself.
- [[topics/distributed-computation-and-analysis-execution|Distributed Computation and Analysis Execution]] (9 concepts): Covers where queries run on the Spark SQL cluster and how results reach a single Python driver. It also lists the failures that stop work, some of which raise no error.
- [[topics/translational-microbiome-and-phage-therapeutics|Translational Microbiome and Phage Therapeutics]] (13 concepts): Asks which organism should be removed or added in which patient, and at what cost to the rest of the community. A Crohn's disease gut project carries the argument end to end.
- [[topics/subsurface-and-soil-community-ecology|Subsurface and Soil Community Ecology]] (6 concepts): Weighs five candidate drivers of community structure in groundwater, sediments, clay formations and layered soils.

## Corpus

73 project reports + 2 cross-project digests, 126 concepts, 185 entities, 15 topics

## Browse

- [[catalog|Full page catalog]]
- [[summaries/discoveries|Discoveries digest]]
- [[summaries/pitfalls|Pitfalls digest]]
- [[authors/index|Authors]]
- [[data/index|Data collections]]
