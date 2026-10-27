---
type: "Research direction"
description: "Inside classes where phenotype varies, is the catalase-metal association a lineage-composition effect that keeps dissolving at finer ranks, or does a lineage-independent association remain?"
hypothesis: "The within-class catalase-negative advantage (Actinomycetes, Gammaproteobacteria, Betaproteobacteria) shrinks toward zero when order, family and genus are held fixed, so the pooled positive effect and the within-class reversals are both composition effects. If a real association exists, it survives genus-level stratification and holds when measured tolerance replaces the genome-derived score."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "The phenotype and pangenome tables are in the lakehouse, but the measured-MIC arm needs new growth assays and the finer-rank models need building."
collections: ["kbase-phenotype", "kbase-ke-pangenome"]
findings: ["bacdive_phenotype_metal_tolerance--a1b67557", "bacdive_phenotype_metal_tolerance--885a4ca9", "bacdive_phenotype_metal_tolerance--9b04bc8d", "bacdive_phenotype_metal_tolerance--202a67ef"]
conflicts: []
papers: ["32683159", "17183702", "37290750", "33279087"]
builds_on: ["findings/bacdive_phenotype_metal_tolerance--a1b67557", "findings/bacdive_phenotype_metal_tolerance--885a4ca9", "findings/bacdive_phenotype_metal_tolerance--9b04bc8d", "findings/bacdive_phenotype_metal_tolerance--202a67ef"]
projects: ["bacdive_phenotype_metal_tolerance"]
topics: ["data-infrastructure-provenance-and-research-practice"]
---
# Does the catalase sign reversal inside classes persist at finer lineage ranks?

Inside classes where phenotype varies, is the catalase-metal association a lineage-composition effect that keeps dissolving at finer ranks, or does a lineage-independent association remain?

## Hypothesis

The within-class catalase-negative advantage (Actinomycetes, Gammaproteobacteria, Betaproteobacteria) shrinks toward zero when order, family and genus are held fixed, so the pooled positive effect and the within-class reversals are both composition effects. If a real association exists, it survives genus-level stratification and holds when measured tolerance replaces the genome-derived score.

## Why it matters

It would show whether routine phenotypes such as catalase can screen for metal tolerance, or only proxy for taxonomy. Gram stain cannot be tested this way, because no Gram-positive Proteobacteria or Gram-negative Actinomycetes exist in the data.

## How to test it

Step 1 (lakehouse): bridge BacDive phenotypes to pangenome species and fit nested mixed models of the metal score on catalase, with random effects for order, family and genus within each class. Taxonomy alone explained 35.4% of variance and taxonomy plus phenotype was no better. Step 2: because the scores are genome-based predictions, measure minimum inhibitory concentrations (MICs) of copper, nickel and zinc in catalase-positive and catalase-negative strains matched within genus. Report the composite-score and measured-MIC results separately.

## What would support or refute it

Support: the catalase coefficient is null at genus level and the measured MICs do not differ between matched strains. Refute: catalase-negative strains keep a higher score at genus level, or show higher measured tolerance in matched pairs. The score-based result alone cannot establish mechanism either way.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. The phenotype and pangenome tables are in the lakehouse, but the measured-MIC arm needs new growth assays and the finer-rank models need building.

- Collection: [[data/kbase-phenotype|Phenotype Collection]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/bacdive_phenotype_metal_tolerance--a1b67557|Catalase association reverses within every major class (Simpson's paradox)]] (Insufficient literature evidence)
- Finding: [[findings/bacdive_phenotype_metal_tolerance--885a4ca9|Phenotype signal is absorbed by taxonomy; gene-cluster count lifts prediction]] (Candidate novel)
- Finding: [[findings/bacdive_phenotype_metal_tolerance--9b04bc8d|Gram-negative advantage is the largest effect but is a between-lineage signal]] (Insufficient literature evidence)
- Finding: [[findings/bacdive_phenotype_metal_tolerance--202a67ef|Urease positivity associates with lower metal score, driven by Actinomycetes]] (Candidate novel)

## Closest published work

- [PMID 32683159](https://pubmed.ncbi.nlm.nih.gov/32683159/) Distinction between Cr and other heavy-metal-resistant bacteria involved in C/N cycling in contaminated soils of copper producing sites.
- [PMID 17183702](https://pubmed.ncbi.nlm.nih.gov/17183702/) Catalases are NAD(P)H-dependent tellurite reductases.
- [PMID 37290750](https://pubmed.ncbi.nlm.nih.gov/37290750/) Genotypic and Phenotypic Characterization of Antimicrobial and Heavy Metal Tolerance in Salmonella enterica and Escherichia coli Isolates from Swine Feed Mills.
- [PMID 33279087](https://pubmed.ncbi.nlm.nih.gov/33279087/) Heat resistance and genomics of spoilage Alicyclobacillus spp. Isolated from fruit juice and fruit-based beverages.

PMID 32683159 links catalase-producing Proteobacteria to multimetal resistance and PMID 17183702 shows catalase-mediated tellurite resistance, but neither stratifies by lineage rank or compares genome-predicted with measured tolerance across species.
