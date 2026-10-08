---
type: "Concept"
description: "Across a genome-scale atlas, annotations for the lanthanide-dependent methanol dehydrogenase xoxF far outnumber those for the calcium-dependent mxaF, globally and within every adequately sampled phylum carrying either gene."
sources: ["summaries/lanthanide_methylotrophy_atlas__REPORT.md"]
---
Methylotrophic bacteria oxidize methanol with pyrroloquinoline-quinone methanol dehydrogenases (MDH) of two kinds: the lanthanide-dependent [[entities/xoxf]] (EC 1.1.2.8) and the calcium-dependent [[entities/mxaf]] (EC 1.1.2.7). This page tracks the claim that, at the level of genome annotation, the lanthanide-dependent form is by far the more widespread. The evidence comes from [[entities/eggnog]] KEGG orthology (KO) calls across [[entities/gtdb]] (Genome Taxonomy Database) genomes [src: lanthanide_methylotrophy_atlas].

## Genome-scale ratio

Across 293,059 GTDB-r214 genomes, eggNOG annotated `K00114` (xoxF) in 3,690 genomes and `K14028` (mxaF) in 195 genomes. That gives a global xoxF:mxaF ratio of 18.92 : 1, with a Clopper-Pearson 95% CI of [13.07, 27.69]. The xoxF fraction of joint MDH calls (xoxF + mxaF) is 0.9498 [95% CI 0.9425, 0.9558]. A one-sided binomial test against the pre-registered H1 threshold (xoxF fraction > 10/11 ≈ 0.909) gave p = 7.6 × 10⁻²². The report elsewhere states the same result as "the 19 : 1 global ratio with 95% CI [13.07, 27.69]". It says this ratio at 293K genomes confirms an earlier literature hypothesis of xoxF predominance "at substantially larger scale". The two ratio figures are presentations of one result, not conflicting measurements [src: lanthanide_methylotrophy_atlas].

## Phylogenetic breadth of the result

The directional result **supports** predominance as a cross-lineage pattern rather than one driven by a single clade. The report applied Benjamini-Hochberg false discovery rate (FDR) correction across 29 testable phyla; FDR correction controls the expected share of false positives among the tests called significant. After correction, xoxF predominance held in every phylum that had any MDH calls and adequate sample size. The phyla named include Pseudomonadota, Acidobacteriota, Actinomycetota, Bacteroidota, Campylobacterota, Verrucomicrobiota, Chloroflexota, Gemmatimonadota, Methylomirabilota, and the archaeal Halobacteriota and Thermoproteota. The report does not say that all 29 testable phyla passed; the qualifier "with any MDH calls and adequate sample size" is part of the claim (see [[entities/benjamini-hochberg-fdr]]) [src: lanthanide_methylotrophy_atlas].

| Phylum | Genomes | xoxF | mxaF | xoxF rate | xoxF:mxaF | Adjusted p | Source |
|---|---|---|---|---|---|---|---|
| Acidobacteriota | 1,006 | 285 | 3 | 28.3 % | 95 : 1 | 1.2 × 10⁻⁷⁹ | [src: lanthanide_methylotrophy_atlas] |
| [[entities/gemmatimonadota]] | 386 | 98 | 1 | 25.4 % | 98 : 1 | 1.5 × 10⁻²⁷ | [src: lanthanide_methylotrophy_atlas] |
| [[entities/methylomirabilota]] | 80 | 23 | 7 | 28.7 % | 3.3 : 1 | 0.011 | [src: lanthanide_methylotrophy_atlas] |
| [[entities/pseudomonadota]] | 117,619 | 2,988 | 171 | 2.5 % | 17.5 : 1 | 0.0 (as reported) | [src: lanthanide_methylotrophy_atlas] |
| Verrucomicrobiota | 2,440 | 19 | 5 | 0.78 % | 3.8 : 1 | 0.015 | [src: lanthanide_methylotrophy_atlas] |

Two points about the table. First, as a descriptive observation, high carrier rates and strong dominance ratios do not always go together across these phyla. Pseudomonadota hold the most xoxF genomes but have a low carrier rate. Methylomirabilota and Verrucomicrobiota show weaker ratios with marginal adjusted p values. The report does not formally test how rate and ratio relate. Second, the report's discussion rounds the carrier rates to Acidobacteriota 28 %, Gemmatimonadota 25 % and Methylomirabilota 29 %. The Pseudomonadota adjusted p is printed as 0.0 rather than as an exact value [src: lanthanide_methylotrophy_atlas].

Within Pseudomonadota, *Pseudomonadaceae* alone contributes 566 xoxF genomes versus 1 mxaF. *Xanthobacteraceae* ([[entities/bradyrhizobium]]) and *Rhizobiaceae* ([[entities/mesorhizobium]]) follow. They sit alongside the canonical methylotroph-rich *Beijerinckiaceae* (171 xoxF in 508 genomes; 33.7 % rate) and *Hyphomicrobiaceae* (33 in 56; 58.9 %). Several phyla are xoxF-only, with zero mxaF annotations: [[entities/bacteroidota]], Cyanobacteriota, Chloroflexota, Planctomycetota, Campylobacterota, Actinomycetota, and the archaeal lineages Halobacteriota and Thermoproteota [src: lanthanide_methylotrophy_atlas].

The report sets this breadth against prior literature, which had left open how far XoxF extends beyond cultured methylotrophs. The atlas places ~3,690 xoxF-bearing genomes across diverse phyla, including Acidobacteriota, Gemmatimonadota, Bacteroidota and archaea [src: lanthanide_methylotrophy_atlas].

## Evidence strength and caveats

The predominance of xoxF over mxaF *annotations* rests on direct counts and strong statistics, so this page states it as a finding. The claim is about gene carriage inferred from eggNOG KO assignment, not about enzyme activity, expression, or lanthanide use in situ. The idea that lanthanide-dependent methanol oxidation is the ecologically dominant mode is therefore a hypothesis these data support, not an established result. All figures come from a single project; no second corpus project independently measures the ratio [src: lanthanide_methylotrophy_atlas].

## Related Pages

- [[concepts/environmental-distribution-of-lanthanide-methylotrophy]] covers where xoxF carriers occur.
- [[concepts/lanmodulin-narrow-distribution]] covers the lanthanide-binding protein [[entities/lanmodulin]]. The atlas detects it in 62 genomes, all within three α-Proteobacterial methylotroph families [src: lanthanide_methylotrophy_atlas].
- [[concepts/functional-marker-validation]] bears on whether KO-based xoxF calls are trustworthy markers.
- The source summary is [[summaries/lanthanide_methylotrophy_atlas__REPORT]].

## Open Directions

- **Split xoxF calls by clade.** Run phylogenetic placement of the 3,690 `K00114` hits against characterized XoxF clades. This would test whether the KO lumps distinct dehydrogenase families together, which could inflate the ratio [src: lanthanide_methylotrophy_atlas].
- **Test whether lineage composition drives the ratio.** Recompute the ratio at genus level within the zero-mxaF phyla, and again with *Pseudomonadaceae* excluded. That family contributes 566 of the xoxF genomes against 1 mxaF, so this would check whether the global ratio depends on a few heavily sampled lineages [src: lanthanide_methylotrophy_atlas].
- **Resolve xoxF carriers that lack PQQ.** The atlas finds 897 genomes (24 % of all xoxF carriers) with no PQQ evidence from either eggNOG or bakta. It names three unresolved explanations: assembly incompleteness, pseudogenization, or genuine reliance on community-acquired PQQ. Many other apparent PQQ absences are annotation gaps between the two sources. Sequence-level inspection of these genomes, covering contig ends, frameshifts in [[entities/pqq-biosynthesis]] loci, and assembly completeness, would test which explanation applies. The report flags this as out of scope [src: lanthanide_methylotrophy_atlas].
- **Adjust for GTDB sampling bias.** Reweight per-phylum carrier rates by genome quality and by isolate-versus-MAG status (MAG: metagenome-assembled genome), following [[concepts/cultivation-collection-bias-in-ecological-genomics]]. This would test whether rates in thinly sampled phyla such as Methylomirabilota (80 genomes) are stable [src: lanthanide_methylotrophy_atlas].
