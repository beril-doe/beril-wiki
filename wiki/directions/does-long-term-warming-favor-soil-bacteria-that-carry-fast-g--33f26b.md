---
type: "Research direction"
description: "In Harvard Forest organic soil, Actinobacteria rose and Acidobacteria fell under long-term warming. Do the genera that rise share genome traits, such as the glyoxylate cycle and larger genomes, that the falling genera lack?"
hypothesis: "Warming-enriched genera carry the glyoxylate-cycle genes and other traits of fast-growing opportunists more often than warming-depleted genera. This would make the weak, uncorrected glyoxylate-gene signals a trait of the winners rather than noise."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "The catalog lists taxonomic profile, gene annotation and genome bin tables, but whether Harvard Forest bins are present was not shown, and the activity test needs new heated and control cores."
databases: ["kbase.ke_pangenome", "kbase.nmdc_mags", "nmdc.metadata", "nmdc.results"]
tables: ["nmdc.results.kraken2_classification_report", "nmdc.results.annotation_kegg_orthology", "kbase.nmdc_mags.mag_catalog", "kbase.nmdc_mags.bin_catalog", "kbase.ke_pangenome.gtdb_metadata", "nmdc.metadata.study_set"]
findings: ["harvard_forest_warming--5dcb42f7", "harvard_forest_warming--d1815e53", "harvard_forest_warming--4fcaf7c4", "harvard_forest_warming--8f0aae96"]
conflicts: []
papers: ["25762989", "27590813", "34512564", "40105318"]
builds_on: ["findings/harvard_forest_warming--5dcb42f7", "findings/harvard_forest_warming--d1815e53", "findings/harvard_forest_warming--4fcaf7c4", "findings/harvard_forest_warming--8f0aae96"]
projects: ["harvard_forest_warming"]
topics: ["ecotypes-and-environmental-gene-content-differentiation"]
---
# Does long-term warming favor soil bacteria that carry fast-growth and glyoxylate-cycle traits?

In Harvard Forest organic soil, Actinobacteria rose and Acidobacteria fell under long-term warming. Do the genera that rise share genome traits, such as the glyoxylate cycle and larger genomes, that the falling genera lack?

## Hypothesis

Warming-enriched genera carry the glyoxylate-cycle genes and other traits of fast-growing opportunists more often than warming-depleted genera. This would make the weak, uncorrected glyoxylate-gene signals a trait of the winners rather than noise.

## Why it matters

It would turn a phylum-level shift seen at one time point into a trait-based prediction of which soil bacteria gain under warming. That would inform models of warmed forest carbon, which currently treat the community as a block.

## How to test it

Step 1 (analysis): list the genera that rose or fell in the heated plots from the taxonomic profiles. Find genome bins from matching soils and compare winners with losers for the glyoxylate-cycle genes, genome size and annotated carbon-cycling gene content, using related species in the pangenome collection as a cross-check. Step 2 (experiment): in fresh heated and control cores from the same plots, add a labile carbon source such as acetate. Measure respiration and use quantitative PCR to follow the winner and loser groups.

## What would support or refute it

Support: winners carry the glyoxylate-cycle genes more often and respond more strongly to the acetate pulse in heated soil. Refutation: winners and losers do not differ in these traits, or the carbon pulse favors both groups equally. The original shifts came from one sampling date, and the organic-horizon samples were all lab-incubated, so a refutation could also mean those shifts do not recur.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. The catalog lists taxonomic profile, gene annotation and genome bin tables, but whether Harvard Forest bins are present was not shown, and the activity test needs new heated and control cores.

## Builds on

- Finding: [[findings/harvard_forest_warming--5dcb42f7|Organic-horizon Actinobacteria rise and Acidobacteria fall under long-term warming]] (Extends retrieved work)
- Finding: [[findings/harvard_forest_warming--d1815e53|Carbon-cycling genes enriched among warming-increased DNA functions in organic horizon only]] (Extends retrieved work)
- Finding: [[findings/harvard_forest_warming--4fcaf7c4|Nominal RNA signals: methane oxidation and glyoxylate genes up under warming]] (Candidate novel)
- Finding: [[findings/harvard_forest_warming--8f0aae96|No greater warming sensitivity of the transcript pool than the DNA pool]] (Insufficient literature evidence)

## Closest published work

- [PMID 25762989](https://pubmed.ncbi.nlm.nih.gov/25762989/) Long-term forest soil warming alters microbial communities in temperate forest soils.
- [PMID 27590813](https://pubmed.ncbi.nlm.nih.gov/27590813/) Long-Term Warming Alters Carbohydrate Degradation Potential in Temperate Forest Soils.
- [PMID 34512564](https://pubmed.ncbi.nlm.nih.gov/34512564/) The Transcriptional Response of Soil Bacteria to Long-Term Warming and Short-Term Seasonal Fluctuations in a Terrestrial Forest.
- [PMID 40105318](https://pubmed.ncbi.nlm.nih.gov/40105318/) Pangenomes suggest ecological-evolutionary responses to experimental soil warming.

PMID 25762989 reports individual Actinobacteria and Acidobacteria members responding to Harvard Forest warming, and PMID 34512564 and 40105318 describe warming-responsive transcripts and pangenome changes. None compares genome traits of rising and falling taxa or tests them with a carbon pulse.
