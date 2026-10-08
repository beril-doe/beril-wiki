---
type: "Concept"
description: "How long-term experimental soil warming at Harvard Forest shifts microbial community composition with FDR support while gene-content, transcript and metabolite signals remain weak or nominal."
sources: ["summaries/harvard_forest_warming__REPORT.md"]
---
## Overview

At [[entities/harvard-forest]], long-term warming gives its clearest microbial signal in phylum composition in the organic horizon. Gene-content (DNA KO, i.e. KEGG Orthology functional group) enrichment for carbon cycling is weak. Transcript (RNA) signals for methanotrophy and the [[entities/glyoxylate-shunt]] are nominal only and do not survive false discovery rate (FDR) correction. Detectable metabolite richness drops in heated mineral soil. All of this evidence comes from one project at one site, so it is untested whether the pattern holds at other sites [src: harvard_forest_warming]. Differences between horizons are discussed further in [[concepts/soil-horizon-response-heterogeneity]].

## Composition: FDR-Significant Phylum Shifts

The report ran per-phylum Welch t-tests on [[entities/kraken2]] read-based relative abundance in 14 control and 14 heated direct samples. It applied [[entities/benjamini-hochberg-fdr]] (BH, a procedure that controls the expected fraction of false positives) across phyla × horizon. In the organic horizon, [[entities/actinobacteria]] rose from a control mean of 0.249 to a heated mean of 0.315 (log2 FC +0.341, q=0.049). Over the same comparison, [[entities/acidobacteria]] fell from 0.035 to 0.024 (log2 FC −0.549, q=0.049). These are the only phylum shifts in the table that reach q<0.05, and they pass that threshold narrowly. Three other organic-horizon phyla did not reach significance: Cyanobacteria (0.0032 to 0.0026, log2 FC −0.305, q=0.072), Proteobacteria (0.654 to 0.605, log2 FC −0.111, q=0.088) and Verrucomicrobia (0.0058 to 0.0041, log2 FC −0.513, q=0.088) [src: harvard_forest_warming].

The report states that its organic-horizon Actinobacteria-up / Acidobacteria-down result (q=0.049) reproduces the warming signature that the same Harvard Forest research team reported in earlier 16S-amplicon and metagenome work. The report does not say which method each cited study used. It cites DeAngelis et al. 2015 as finding that Actinobacteria, Alphaproteobacteria and Acidobacteria showed the strongest warming responses, with the shifts most pronounced in the organic horizon. It also cites Pold et al. 2016, which found that warming increases the fraction of carbohydrate-degrading genes affiliated with Actinobacteria. The report treats that finding as a mechanistic complement to its compositional result. This agreement with published work **supports** the compositional result. However, the comparison is the report's own reading of the literature, not an independent reanalysis [src: harvard_forest_warming].

## Gene Content: A Weak Carbon-Cycling Enrichment

In the DNA × organic pool, carbon-cycling KOs were enriched among heated-up KOs: 5 / 57 carbon-cycling KOs versus 428 / 12,806 other KOs. A one-sided [[entities/fishers-exact-test]] gave OR=2.78, p=0.042. The other pools showed no enrichment. DNA × mineral had 0 / 57 versus 2 / 12,806 (OR=0.0, p=1.0). RNA × organic and RNA × mineral each had 0 / 57 versus 0 / 14,245 (OR=NaN, p=1.0). The organic-horizon enrichment rests on five KOs and a borderline nominal p-value. There is also a confound: all organic-horizon DNA samples were lab-incubated, because the NMDC pipeline did not produce direct organic DNA. As a result, incubation cannot be cleanly separated from warming in this analysis. The enrichment **is consistent with** the organic-horizon compositional shift, but the two analyses are not directly comparable, because the taxonomy test used direct samples [src: harvard_forest_warming].

## Transcripts: Nominal Methanotrophy and Glyoxylate Signals

Several warming-associated RNA-pool signals are nominal only. No individual KO survives FDR (q<0.10) at n=11+11 across 14K KOs. The report attributes the limited power to sample size relative to the number of KOs tested. These signals are therefore leads, not established warming responses [src: harvard_forest_warming]. See [[concepts/null-results-under-limited-statistical-resolution]].

- [[entities/pmoa]] (K10944, particulate methane monooxygenase α): log2 FC +0.730 (p=0.009) in organic and +0.743 (p=0.029) in mineral [src: harvard_forest_warming].
- [[entities/pmob]] (K10945, β subunit): log2 FC +0.669 (p=0.012) in organic and +0.880 (p=0.054) in mineral [src: harvard_forest_warming].
- Mineral glyoxylate-cycle genes: [[entities/acea-icl]] (K01637, isocitrate lyase, log2 FC +0.460, p=0.037) and [[entities/aceb-glcb]] (K01638, malate synthase, log2 FC +0.268, p=0.037) [src: harvard_forest_warming].
- Organic chiA (K01183, chitinase): log2 FC +0.236 (p=0.074) [src: harvard_forest_warming].
- Organic lpdA (K00382, dihydrolipoyl dehydrogenase): log2 FC −0.161 (p=0.021). None of these p-values survive FDR across 14K KOs [src: harvard_forest_warming].

There is a measurement caveat as well. The metatranscriptome KOs come from contig annotations. They describe the composition of the transcript pool, not TPM-quantified expression. Contig-level annotation counts approximate relative transcript abundance but are biased by assembly quality. Even the nominal upregulation therefore reflects shifts in pool composition, not measured expression levels [src: harvard_forest_warming].

The report cites Aliyu et al. 2016 (FEMS Microbiol. Ecol., PMID:26884466) as an external precedent for a glyoxylate-shunt induction signature. The report describes coordinated icl/aceA and aceB/glcB upregulation as a published signature of stress or C2-substrate use in Actinobacteria. It calls its heated-mineral observation 'mechanistically self-consistent' because Actinobacteria are enriched in this soil. That framing gives mechanistic context but does not prove a Harvard Forest mechanism, and the transcript signals underneath it are nominal only [src: harvard_forest_warming].

## Metabolites: Reduced Detectable Richness in Heated Mineral Soil

Heated mineral samples had lower detectable metabolite richness than controls (155 vs 167 ChEBI, p=0.012). The report links this qualitatively to earlier literature on soil-carbon loss and substrate depletion. It cites Melillo et al. 2017 for a four-phase oscillating soil-C loss trajectory under +5°C warming. It cites Domeignoz-Horta et al. 2022, from 28-year warmed plots, for the view that the apparent warming response reflects reduced substrate quantity and quality, not thermal acclimation. The report calls the richness drop 'the direct molecular signature' that this substrate-depletion model predicts. The evidence supports only qualitative consistency, because one richness comparison does not demonstrate substrate depletion [src: harvard_forest_warming].

## Hypothesis: A Warming-Activated Ruderal Subset

The report proposes that warming may activate a fraction of the community characterized by Actinobacteria, glyoxylate-cycle-active organisms and methanotrophy. It suggests cross-linking this idea with Choudoir et al. 2025 pangenome data. The report explicitly frames this as a hypothesis to test, not an established finding. Two of its three components, the glyoxylate and pmoA/pmoB transcript signals, are nominal only [src: harvard_forest_warming].

## Tensions

In places, the report's interpretive language is stronger than its statistics. It calls the metabolite-richness drop the 'direct molecular signature' of substrate depletion and the glyoxylate signal 'mechanistically self-consistent'. Yet the transcript signals do not survive FDR correction and measure transcript-pool composition, not quantified expression. The carbon-cycling KO enrichment (OR=2.78, p=0.042) also appears only in the DNA × organic pool, where incubation is confounded with warming. Composition (q=0.049) is therefore the best-supported layer, and the functional and mechanistic claims should be read as hypotheses [src: harvard_forest_warming]. Integrating these layers across omics types is discussed in [[concepts/multi-omics-integration]].

## Open Directions

- Test whether the heated-mineral pmoA/pmoB and aceA/aceB transcript increases come from Actinobacteria-assigned reads. Taxonomically binned RNA KO counts would show whether these reflect a single ruderal subset or separate responses that happen to co-occur [src: harvard_forest_warming].
- Cross-link the warming-responsive phyla with Choudoir et al. 2025 pangenome data, as the report proposes. This would test whether genomes of warming-enriched taxa carry glyoxylate-shunt and methanotrophy genes [src: harvard_forest_warming].
- Re-test the nominal RNA KO signals (n=11+11) against a small, pre-specified carbon-cycling KO panel instead of genome-wide FDR. This would lighten the multiple-testing burden. If signals remained non-significant, though, the result alone could not establish a true lack of effect. Adding samples, or quantifying transcripts rather than counting contig annotations, would also be needed [src: harvard_forest_warming].
- Generate direct (non-incubated) organic-horizon DNA so the DNA × organic carbon-cycling enrichment can be separated from the effect of lab incubation [src: harvard_forest_warming].
- Compare compound classes, not just richness, between heated and control mineral metabolomes. This would show whether the drop is concentrated in labile substrates, as the substrate-depletion model predicts [src: harvard_forest_warming].

Source summary: [[summaries/harvard_forest_warming__REPORT]].
