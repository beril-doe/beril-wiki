# BERIL Knowledge Wiki

Most of these projects analysed data already in the [KBase Data Lakehouse](https://hub.berdl.kbase.us); a few brought their own. See [[about|About This Wiki]] for what that means for citing anything here.

This wiki compiles the research of the BERIL Research Observatory, where AI agents conduct microbial-biology research projects over the KBase Data Lakehouse. The wiki draws on the project reports and on two central digests, one of discoveries and one of pitfalls, that collect findings across projects.

Start with the topics. Each topic hub poses a question that several projects address and links to the concept pages that argue across those projects. Concept pages connect findings and record where sources disagree. Entity pages cover specific organisms, genes, compounds, methods and datasets. Summary pages report the content of one source each. On concept and entity pages, each factual claim cites the source project or central digest it comes from.

## Topics

- [[topics/gene-fitness-landscapes-and-cofitness-modules|Gene Fitness Landscapes and Cofitness Modules]] (11 concepts): How the growth effects of disrupting each gene, measured across many conditions, group genes by cofitness (similarity in their fitness profiles across conditions) and into modules with coordinated fitness patterns.
- [[topics/gene-essentiality-and-perturbation-assay-validity|Gene Essentiality and Perturbation-Assay Validity]] (6 concepts): Treats direct perturbation and measured growth as the strongest evidence that growth depends on a gene under a defined condition, tests the measurements themselves, and treats conservation, annotation and modeling as predictors rather than definitions.
- [[topics/laboratory-fitness-versus-natural-selection-and-gene-conservation|Laboratory Fitness Versus Natural Selection and Gene Conservation]] (6 concepts): Asks whether a gene's growth effect in the laboratory, measured by random barcode transposon sequencing (RB-TnSeq) in the Fitness Browser, explains whether genomes in nature keep or lose that gene.
- [[topics/pangenome-structure-and-genome-evolution|Pangenome Structure and Genome Evolution]] (9 concepts): How the gene clusters across a species' genomes divide into a conserved core and variable auxiliary genes, and how projects define the core in different ways.
- [[topics/ecotypes-and-environmental-gene-content-differentiation|Ecotypes and Environmental Gene-Content Differentiation]] (7 concepts): Asks whether environment shapes which genes bacteria carry, pairing one broad test across 172 species with many targeted tests.
- [[topics/metabolic-traits-auxotrophy-and-community-dependence|Metabolic Traits, Auxotrophy, and Community Dependence]] (12 concepts): Reads biosynthetic and catabolic pathways from genomes, uses pathway gaps to flag possible auxotrophy (dependence on an externally supplied nutrient), and pairs GapMind predictions with measured gene fitness to ask whether community members can lose costly functions.
- [[topics/metabolic-models-and-pathway-level-evidence|Metabolic Models and Pathway-Level Evidence]] (6 concepts): How far genome-derived metabolic predictions hold up, covering GapMind pathway-completeness calls and genome-scale models run with flux balance analysis (FBA), a constraint-based method that predicts feasible metabolic fluxes and growth.
- [[topics/lanthanide-dependent-methylotrophy|Lanthanide-Dependent Methylotrophy]] (3 concepts): Bacteria that use rare-earth elements as cofactors for methanol oxidation through the xoxF methanol dehydrogenase, in contrast to the calcium-dependent mxaF form.
- [[topics/functional-dark-matter-and-annotation-resolution|Functional Dark Matter and Annotation Resolution]] (9 concepts): Genes that lack functional annotation, and the separate layer of literature darkness, where a gene with no text-mined papers may still carry curated knowledge.
- [[topics/resistance-defense-systems-and-mobile-elements|Resistance, Defense Systems, and Mobile Elements]] (7 concepts): Antimicrobial-resistance genes, metal tolerance and anti-phage defense, along with the mobile genetic elements that can move these functions between genomes.
- [[topics/sampling-coverage-and-statistical-confounding|Sampling Coverage and Statistical Confounding]] (14 concepts): When an apparent microbial pattern reflects biology and when it reflects what was collected, what a reference database could represent, or how the analysis was built.
- [[topics/data-infrastructure-provenance-and-research-practice|Data Infrastructure, Provenance, and Research Practice]] (8 concepts): How the corpus organizes, names, joins and audits its data, including an inventory of the KBase Data Lakehouse and a provenance audit of one overloaded resource name.
- [[topics/distributed-computation-and-analysis-execution|Distributed Computation and Analysis Execution]] (9 concepts): Where queries run on the Spark SQL cluster, how results reach a single Python driver process, and which code patterns and failures slow or stop large genomic jobs, sometimes without an error.
- [[topics/translational-microbiome-and-phage-therapeutics|Translational Microbiome and Phage Therapeutics]] (13 concepts): Which organism to remove or add in which patient, by what agent and at what cost to the community, worked through a Crohn's disease gut project and a second body site.
- [[topics/subsurface-and-soil-community-ecology|Subsurface and Soil Community Ecology]] (6 concepts): What structures microbial communities in groundwater, sediments, clay formations and layered soils, with the corpus addressing five candidate drivers.

## Corpus

73 project reports + 2 cross-project digests, 126 concepts, 185 entities, 15 topics

## Browse

- [[catalog|Full page catalog]]
- [[summaries/discoveries|Discoveries digest]]
- [[summaries/pitfalls|Pitfalls digest]]
- [[authors/index|Authors]]
- [[data/index|Data collections]]
