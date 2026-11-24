---
type: "Concept"
description: "How xoxF carriage varies across environment classes (soil, marine, host, REE-impacted), with caveats on environmental classification and coverage."
sources: ["summaries/lanthanide_methylotrophy_atlas__REPORT.md"]
---
# Environmental association of lanthanide-dependent methanol oxidation genes

How xoxF carriage varies across environment classes (soil, marine, host, REE-impacted), with caveats on environmental classification and coverage.

## Literature Context

The one candidate paper is an experimental study of lanthanide-dependent methylotrophy in a sediment-derived community. It used a synthetic coculture of a methanotroph and two nonmethanotrophic methylotrophs, all isolated from Lake Washington sediment, with lanthanum added as the rare earth element [PMID 28028242](https://pubmed.ncbi.nlm.nih.gov/28028242/). Its gene-expression profiles and mutant analyses suggest that methanol is the dominant carbon and energy source the methanotroph provides to the nonmethanotrophs. When the nonmethanotroph was present, expression of the dominant methanol dehydrogenase (MDH) in the methanotroph shifted from the lanthanide-dependent XoxF type to the calcium-dependent MxaF type. Methanol was released into the medium only when the methanotroph expressed MxaF-type MDH [PMID 28028242](https://pubmed.ncbi.nlm.nih.gov/28028242/). The authors present this as a cross-feeding mechanism that pure-culture studies cannot reveal. The evidence comes from one defined model community, and only the abstract was available for this review. It does not address how widespread xoxF is across environments.

The corpus reports a genome-scale environmental pattern. xoxF carriage is enriched in soil_sediment (OR = 1.92, p_BH = 6.1 × 10⁻³⁹) and, more weakly, in marine genomes (OR = 1.31). It is strongly depleted in host_associated genomes (OR = 0.058). Volcanic_geothermal and mining are null results. The REE-impacted class has an elevated descriptive rate (10.8 % vs 3.7 % baseline) but only n=37 genomes and p_BH = 0.082, so that result is not significant.

The sediment enrichment is consistent with the literature paper. That paper shows XoxF-type MDH is actively used by a methanotroph from lake sediment, so sediment is a plausible habitat for lanthanide-dependent methanol oxidation [PMID 28028242](https://pubmed.ncbi.nlm.nih.gov/28028242/). The match is indirect, because the paper is a single-system laboratory experiment and does not measure carriage across environment classes. The paper's other finding is that the methanotroph switches between XoxF and MxaF depending on its partner. This suggests the hypothesis that xoxF presence in a genome does not show whether the lanthanide-dependent enzyme is the one expressed in situ. The corpus measures gene carriage only, so it cannot test this. The host depletion, the soil and marine contrasts, and the null REE-mining and volcanic results are not addressed by the candidate paper. They stand as novel, genome-wide observations that this paper neither supports nor contradicts.

The corpus's own caveats still apply: the small REE-impacted sample from a single bioproject, text-mined environment classes, and within-phylum stratification instead of a phylogeny-aware model.

## Class-level enrichment

The environmental signal is dominated by soil/sediment, not by volcanic or REE-mining environments (OR = odds ratio; BH-FDR = Benjamini-Hochberg false discovery rate). [src: lanthanide_methylotrophy_atlas] Associations were tested with per-class Fisher's exact tests of any_xoxF against the generic_environmental reference class, with BH-FDR correction. [src: lanthanide_methylotrophy_atlas] The report considers its hypothesis H2 only partially supported. [src: lanthanide_methylotrophy_atlas]

| Class | Genomes | xoxF rate | OR | p_BH |
|---|---|---|---|---|
| generic_environmental (reference) | 21,538 | 3.69 % | 1.00 | — [src: lanthanide_methylotrophy_atlas] |
| soil_sediment | 13,779 | 6.84 % | 1.92 | 6.1 × 10⁻³⁹ [src: lanthanide_methylotrophy_atlas] |
| marine | 15,554 | 4.76 % | 1.31 | 7.8 × 10⁻⁷ [src: lanthanide_methylotrophy_atlas] |
| volcanic_geothermal | 3,450 | 3.19 % | 0.86 | 0.20 [src: lanthanide_methylotrophy_atlas] |
| mining | 1,636 | 4.10 % | 1.12 | 0.38 [src: lanthanide_methylotrophy_atlas] |
| ree_impacted | 37 | 10.81 % | 3.51 | 0.082 [src: lanthanide_methylotrophy_atlas] |
| methylotrophic | 5 | 20.0 % | 8.70 | 0.20 [src: lanthanide_methylotrophy_atlas] |
| host_associated | 107,600 | 0.22 % | 0.058 | 0.0 [src: lanthanide_methylotrophy_atlas] |

Volcanic_geothermal and mining are null results, and so are the two small classes (ree_impacted and methylotrophic). [src: lanthanide_methylotrophy_atlas]

### Soil and sediment

The report reads the soil enrichment as consistent with methanol oxidation being a known soil process and with the reservoir of lanthanide minerals in soil. [src: lanthanide_methylotrophy_atlas] Soil typically contains 100–300 mg/kg total REE and is the natural habitat of the methylotroph families that carry the cassette. [src: lanthanide_methylotrophy_atlas] Within Acidobacteriota (see [[entities/acidobacteria]]), the highest per-genome xoxF carrier, the soil-sediment enrichment survives with within-phylum OR=2.16 and p_BH=2.2 × 10⁻⁵. The report suggests that at least part of the broader soil signal is not pure phylogenetic confounding. [src: lanthanide_methylotrophy_atlas]

### Host-associated depletion

Host-associated environments are strongly depleted in xoxF (OR=0.058). The report reads this as consistent with absence of methylotrophy in the gut/host niche. [src: lanthanide_methylotrophy_atlas]

### REE-impacted samples

REE-impacted samples show a 3.5-fold descriptive elevation (10.8 % vs 3.7 % baseline). Their n=37 is too small to clear the FDR threshold (p_BH = 0.082). [src: lanthanide_methylotrophy_atlas] See [[entities/rare-earth-elements]] and [[concepts/community-function-of-rare-earth-acid-mine-drainage-mags]].

## Caveats on classification and coverage

- The REE-AMD (acid mine drainage) anchor is small (n=37) and comes from a single bioproject. It is descriptive only, and inferential claims about REE-impacted environments need a larger and more independent collection. [src: lanthanide_methylotrophy_atlas]
- The report proposes recruiting REE-mining tailings, leachate and bioreactor metagenomes from existing sequence archives to make the REE-impacted signal inferential rather than descriptive. [src: lanthanide_methylotrophy_atlas]
- The ncbi_env classification derives from text mining with hierarchical regex priorities. The host_associated class is broad and includes gut, skin, oral and infection contexts. [src: lanthanide_methylotrophy_atlas] See [[entities/ncbi-env-environmental-metadata]].
- Misclassifications are possible, but the report states that soil/sediment enrichment and host depletion survive. [src: lanthanide_methylotrophy_atlas]
- AlphaEarth coverage of xoxF genomes is 39.5 % (1,457 / 3,690), against a 28 % pangenome baseline. [src: lanthanide_methylotrophy_atlas] This leaves 60.5 % of xoxF carriers without environmental coordinates. [src: lanthanide_methylotrophy_atlas] See [[entities/alphaearth-environmental-embeddings]] and [[concepts/metadata-and-annotation-coverage-gaps-biasing-environmental-genome-cohorts]].
- Embedding-based niche analysis was scoped out of the report, although a coverage-restricted supplementary analysis is feasible. [src: lanthanide_methylotrophy_atlas]
- H2 still relies on within-phylum stratified analyses rather than a fully phylogeny-aware mixed model. [src: lanthanide_methylotrophy_atlas]

## Open Directions

- Recruit REE-mining tailings, leachate and bioreactor metagenomes from existing sequence archives. This would test whether REE supply per se selects for the cassette and could make the REE-impacted signal inferential.
- Fit a phylogeny-aware mixed model of xoxF carriage on environment class, using that larger REE-impacted collection. This would replace the within-phylum stratification.
- Run a coverage-restricted AlphaEarth embedding analysis on the 1,457 xoxF genomes that have coordinates. This would show whether embedding-based niches agree with the text-mined classes.
- Re-run the class tests with a finer split of host_associated (gut, skin, oral, infection). This would check whether the broad class hides any methylotrophic niches.
