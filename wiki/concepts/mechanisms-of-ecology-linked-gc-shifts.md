---
type: "Concept"
description: "Proposed mutational and selective explanations (gBGC, oxidative damage, drift-barrier selection, codon usage) for small within-species GC shifts; hypotheses not directly tested."
sources: ["summaries/gc_ecotype_ecology__REPORT.md"]
---
# Mechanisms of ecology-linked GC shifts

This page collects the mutational and selective explanations proposed for small within-species GC shifts tied to ecology. All of them are hypotheses: the source report did not test them directly. [src: gc_ecotype_ecology] See [[summaries/gc_ecotype_ecology__REPORT]] and [[concepts/genome-gc-content-as-an-ecological-signal]] for the underlying observations.

## Literature Context

The candidate papers address the same question the hub raises: what forces set bacterial GC content, and whether mutation, gene conversion or selection dominates. A study of synonymous polymorphism in 149 bacterial species found a large excess of segregating GC→AT over AT→GC mutations in all but the most AT-rich bacteria [PMID 20838593](https://pubmed.ncbi.nlm.nih.gov/20838593/). The authors argued that this excess is inconsistent with mutation bias alone, and that it is probably not due to translational selection or biased gene conversion. Their reasons were that optimal codons tend to be AT-rich and that the excess also appears in datasets with no evidence of recombination. They concluded that selection acts to increase synonymous and genomic GC content in many bacteria [PMID 20838593](https://pubmed.ncbi.nlm.nih.gov/20838593/).

Other work supports an AT-biased mutational input. Clonal pathogens evolving under severely relaxed selection (five pathogens from four clades) showed mutation biased toward AT, even in clades with high genomic GC content, mainly through C/G to T/A transitions [PMID 20838599](https://pubmed.ncbi.nlm.nih.gov/20838599/). The authors inferred that selection, or a selection-like process such as biased gene conversion, must shape nucleotide content. A comparison of recombinant alleles across microbial species with many sequenced strains found that recombination-introduced polymorphisms are also biased toward A and T, to a degree similar to mutation. The authors concluded that recombination alone, without selection, is unlikely to counteract the AT-enrichment of bacterial genomes [PMID 28957503](https://pubmed.ncbi.nlm.nih.gov/28957503/). A review of stop-codon usage adds that GC-biased gene conversion is clear in mammals and birds, but that TGA enrichment in other GC-rich genomes is less clear. It also describes a "TAG paradox", in which TAG usage in bacteria and archaea mostly does not respond to GC pressure. For that pattern, no mutational, selective or gBGC model currently has good support [PMID 35867377](https://pubmed.ncbi.nlm.nih.gov/35867377/).

The hub's framing is partly consistent with this literature. Its proposal that selection can act on very small GC effects fits the view that bacterial GC content is not set by mutation alone [PMID 20838593](https://pubmed.ncbi.nlm.nih.gov/20838593/) [PMID 20838599](https://pubmed.ncbi.nlm.nih.gov/20838599/). Its oxidative-damage hypothesis, which invokes G→T transversions, is a mutational explanation. It is compatible with the AT-biased mutation seen in those studies, but none of the candidate papers tests it.

The hub's gBGC hypothesis is in tension with parts of this evidence. The hub proposes that differing recombination rates between gut and free-living lineages could drive GC offsets. The recombination study found that recombinant alleles are AT-biased, so recombination alone is unlikely to raise GC [PMID 28957503](https://pubmed.ncbi.nlm.nih.gov/28957503/). The 149-species study also judged gBGC an improbable explanation for the specific excess of segregating GC→AT polymorphisms [PMID 20838593](https://pubmed.ncbi.nlm.nih.gov/20838593/). This does not rule out gBGC as a source of small within-species shifts. Those studies address genome-wide GC maintenance, not niche-linked offsets of 0.1–0.9%. The hub's codon-usage hypothesis is not directly addressed by the candidates. The stop-codon review shows that codon-level GC effects can be unexplained [PMID 35867377](https://pubmed.ncbi.nlm.nih.gov/35867377/). The corpus's within-species, ecology-linked framing extends this literature and remains untested. It does not resolve the mechanism.

## The size of the effect

Within-species ecological GC signals typically involve 0.1–0.9% GC shifts. The report reads this as consistent with fine-grained selective or mutational pressure rather than ancestral inheritance. [src: gc_ecotype_ecology] For a typical 3 Mbp bacterial genome, a 0.3% GC shift corresponds to ≈ 9,000 net biased substitutions distributed across the genome. [src: gc_ecotype_ecology] The report treats reproducible shifts of this size as an ongoing, niche-tunable mutation-and-selection balance on top of a phylogeny-dominated GC level, and says they are not noise. [src: gc_ecotype_ecology] The report names the dominant explanatory framework as biased gene conversion plus ancient environmental adaptation, and says this framework leaves an open question. [src: gc_ecotype_ecology]

## Why selection can act on tiny GC effects

Bacterial point-mutation rates are on the order of 10⁻⁹ to 10⁻¹⁰ per nucleotide per generation. [src: gc_ecotype_ecology] Effective population sizes for free-living bacteria are commonly estimated at 10⁸–10¹⁰. [src: gc_ecotype_ecology] On this basis the report argues that μN_e is ~10⁻¹ to 10¹. Very weakly selected GC-changing substitutions (|s| ≈ 10⁻⁷ to 10⁻⁹) would then lie above the drift barrier and could be fixed by selection. [src: gc_ecotype_ecology]

## Candidate mechanisms

### Differential biased gene conversion

Biased gene conversion (gBGC) is described as well established in bacteria, and its intensity is expected to vary with recombination rate. [src: gc_ecotype_ecology] The report proposes that its intensity differs across microhabitats, for example if recombination differs between gut and free-living lifestyles. [src: gc_ecotype_ecology] It states that host-associated bacteria typically recombine less than environmental bacteria, because of population structure, transmission bottlenecks and host-induced restriction systems. [src: gc_ecotype_ecology] A 2× difference in bN_e between gut and free-living lineages of one species is proposed to be enough to produce a fraction-of-a-percent GC offset over ≈ 10⁶ generations. [src: gc_ecotype_ecology]

### Oxidative damage and mutational asymmetry

Oxidative damage produces G→T transversions. The report suggests that differences in oxidative environment, such as aerobic soil versus anaerobic gut, could induce 0.1–1% GC shifts over recent within-species divergence. [src: gc_ecotype_ecology] More generally, it proposes mutational asymmetries from oxidative stress or replication-fork dynamics that differ between hosts and free-living environments. [src: gc_ecotype_ecology]

### Codon-usage selection

The report proposes codon-usage selection that responds to nutrient availability, particularly nitrogen. [src: gc_ecotype_ecology] It cites Gralka et al. 2023 for a cross-species relationship between GC and sugar-versus-acid metabolism. The within-species analogue would be a smaller, niche-specific shift in codon-encoded amino-acid bias. [src: gc_ecotype_ecology]

## Fit with the observed species

The species with the largest within-species effects are Burkholderia vietnamiensis, Vibrio parahaemolyticus, Klebsiella quasipneumoniae and Lactiplantibacillus plantarum. They span niches that differ in recombination rate and likely oxidative environment, such as soil/plant (high recombination, aerobic) versus gut/clinical (lower recombination, partly anaerobic). [src: gc_ecotype_ecology] The report finds their GC offsets consistent with a few hundred to a few thousand generations of differential mutation or selection pressure since recent lineage divergence. [src: gc_ecotype_ecology] This fit is interpretive. The mechanisms themselves remain untested. [src: gc_ecotype_ecology]

## Open Directions

- Measure recombination rates per niche within the species that show the largest GC effects, and test whether GC offsets track them. This would test the gBGC hypothesis.
- Compare mutation spectra, especially the G→T rate, between aerobic and anaerobic lineages of the same species. This would test the oxidative-damage hypothesis.
- Test whether GC-increasing and GC-decreasing substitutions differ in codon and amino-acid usage across niches, in light of nitrogen availability. This would test the codon-usage hypothesis.
- Estimate divergence times for the lineage pairs to check the few-hundred to few-thousand-generation estimate against the proposed rates.
