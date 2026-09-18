# BERIL Knowledge Wiki

Most of these projects analysed data already in the [KBase Data Lakehouse](https://hub.berdl.kbase.us); a few brought their own. See [[about|About This Wiki]] for what that means for citing anything here.

This wiki compiles the research output of the BERIL Research Observatory, where AI agents conduct microbial-biology investigations against the KBase Data Lakehouse. Each project starts from a question that the available data can be pushed at, runs its own analysis, and writes a report. The reports cover gene fitness assays, pangenomes, metabolic reconstructions, environmental sampling, and the data infrastructure all of it runs on. Two cross-project digests, one of discoveries and one of pitfalls, collect what repeated across projects.

Topics are the entry points. Each topic hub states a question, names the instruments the corpus brings to it, and links the concept pages that argue it out. Start there if you want to know what the corpus says about something rather than what one project did.

Concepts, entities, and summaries are the reference layers underneath. A concept page argues a single claim across projects and carries a per-claim citation to the project it came from, plus a Tensions section where projects disagree. An entity page collects what the corpus knows about one named thing: an organism, a gene, a compound, a method, or a dataset. A summary page records one project report and lists the concepts it feeds. Numbers on every page are copied from the source report, not reconciled across reports.

## Topics

- [[topics/gene-fitness-landscapes-and-cofitness-modules|Gene Fitness Landscapes and Cofitness Modules]] (11 concepts): Maps how much each gene matters for growth across many environments, and which genes' fitness profiles move together, built at scale from RB-TnSeq (random barcode transposon sequencing, which estimates mutant fitness from barcode abundance after pooled growth).
- [[topics/gene-essentiality-and-perturbation-assay-validity|Gene Essentiality and Perturbation-Assay Validity]] (6 concepts): Treats "essential" as the output of one assay in one condition, and asks what a perturbation experiment has actually measured when it calls a gene required.
- [[topics/laboratory-fitness-versus-natural-selection-and-gene-conservation|Laboratory Fitness Versus Natural Selection and Gene Conservation]] (6 concepts): Compares what a gene does for growth in a tested flask condition against whether a clade retained that gene over evolutionary time.
- [[topics/pangenome-structure-and-genome-evolution|Pangenome Structure and Genome Evolution]] (9 concepts): Asks what the split between core and accessory gene families means biologically, and whether it marks a real two-speed genome architecture.
- [[topics/ecotypes-and-environmental-gene-content-differentiation|Ecotypes and Environmental Gene-Content Differentiation]] (6 concepts): Tests whether genomes cluster into recoverable gene-content groups and whether gene content tracks the environment a genome came from, and finds the two halves do not answer alike.
- [[topics/metabolic-traits-auxotrophy-and-community-dependence|Metabolic Traits, Auxotrophy, and Community Dependence]] (9 concepts): Asks whether a bacterium makes its own amino acids or scavenges them from neighbours, using pathway predictions across hundreds of thousands of genomes alongside laboratory gene-fitness data.
- [[topics/metabolic-models-and-pathway-level-evidence|Metabolic Models and Pathway-Level Evidence]] (6 concepts): Examines the two instruments that carry a genome sequence to a claim about metabolism, flux balance analysis and the GapMind pathway predictor.
- [[topics/functional-dark-matter-and-annotation-resolution|Functional Dark Matter and Annotation Resolution]] (9 concepts): Asks what kind of gap unannotated protein sequence is and at what resolution it can be closed, separating darkness into layers such as sequence-space representation.
- [[topics/resistance-defense-systems-and-mobile-elements|Resistance, Defense Systems, and Mobile Elements]] (8 concepts): Brings pangenome inventories spanning tens of thousands of species together with RB-TnSeq measurements, across resistance genes, metal tolerance, anti-phage defense, and the mobile genetic elements that may move any of them.
- [[topics/sampling-coverage-and-statistical-confounding|Sampling Coverage and Statistical Confounding]] (10 concepts): Asks when an environment-genome or phenotype-genotype association reflects biology, and when it reflects which organisms were cultured or which reference database the classifier used.
- [[topics/data-infrastructure-provenance-and-research-practice|Data Infrastructure, Provenance, and Research Practice]] (6 concepts): Covers what happens between a table existing and a claim being defensible: resource discovery, identifier reconciliation, cross-tenant join validation, and challenging a claim after the analysis has run.
- [[topics/translational-microbiome-and-phage-therapeutics|Translational Microbiome and Phage Therapeutics]] (3 concepts): Works on converting ecological and host-range measurements into an intervention for a named patient: which organism to remove or add, with what agent, and at what point in the disease course.
- [[topics/subsurface-community-ecology|Subsurface Community Ecology]] (3 concepts): Asks what organizes microbial communities below the rooting zone, from depth and groundwater flow to confined clay and deep boreholes, and how much of a community is set by its past rather than its present environment.

## Corpus

73 project reports + 2 cross-project digests, 92 concepts, 139 entities, 13 topics

## Browse

- [[catalog|Full page catalog]]
- [[summaries/discoveries|Discoveries digest]]
- [[summaries/pitfalls|Pitfalls digest]]
- [[authors/index|Authors]]
- [[data/index|Data collections]]
