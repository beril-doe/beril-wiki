---
type: "Concept"
description: "Bakta-validated lanmodulin, a lanthanide-binding protein, is confined to three \u03b1-Proteobacterial methylotroph families and does not reliably co-occur with xoxF, so chelator presence cannot be read off lanthanide-dependent dehydrogenase presence."
sources: ["summaries/lanthanide_methylotrophy_atlas__REPORT.md"]
---
# Lanthanide-Chelator Machinery Is Far Narrower Than Lanthanide-Dependent Dehydrogenase Distribution

According to the lanthanide methylotrophy atlas report, [[entities/lanmodulin]] can bind rare-earth elements (REEs) [src: lanthanide_methylotrophy_atlas]. That report found lanmodulin, validated by [[entities/bakta]] annotation, in 62 genomes, all in three α-Proteobacterial methylotroph families [src: lanthanide_methylotrophy_atlas]. These are genome-annotation counts from one report. They are not measurements of protein expression or REE binding [src: lanthanide_methylotrophy_atlas].

The report detected Bakta-validated `product = 'Lanmodulin'` in 62 genomes from 10 species. All of them (62 / 62 = 100 %) fall within Beijerinckiaceae, Acetobacteraceae or Hyphomicrobiaceae, the three α-Proteobacterial methylotroph families pre-specified in hypothesis H3. A one-sided binomial test against the 80 % threshold gave p = 9.8 × 10⁻⁷, and the report rated H3a as strongly supported [src: lanthanide_methylotrophy_atlas].

The dominant lanmodulin carrier is [[entities/methylobacterium-extorquens]], with 22 genomes and 1 lanmodulin copy each, so paralogs do not explain the pattern. The other contributors are an uncharacterised Acetobacteraceae genus (`g__BOG-930`, 12 genomes), *M. thiocyanatum* (6), *M. rhodesianum* (6), *M. aminovorans* (4), *Hyphomicrobium_B* (2) and *Methylocella* (2) [src: lanthanide_methylotrophy_atlas].

Among *Methylobacterium* genomes, the report found [[entities/xoxf]] in 102/209 and lanmodulin in 46/209. In this genus, the lanthanide-dependent methanol dehydrogenase gene therefore appears more often than the chelator. The report describes these counts as consistent with an existing model and as broader population-genomic context for it [src: lanthanide_methylotrophy_atlas]. This **supports** the page's central claim that chelator carriage is narrower than dehydrogenase carriage, and it connects to [[concepts/lanthanide-dependent-methanol-dehydrogenase-predominance]] [src: lanthanide_methylotrophy_atlas].

## Dehydrogenase Presence Does Not Imply Chelator Presence

xoxF, from any annotation source, co-occurred in 49 / 62 = 79.0 % of lanmodulin-bearing genomes. This is just under the pre-registered 80 % threshold (one-sided binomial p = 0.65), so H3b was not formally supported. The report gives two possible explanations for the 13/62 lanmodulin-without-xoxF genomes. One is incomplete annotation. The other is a genuine alternative lanthanide-handling pathway, because lanmodulin can bind REEs without being co-located with a lanthanide-MDH operon. The report does not decide between them [src: lanthanide_methylotrophy_atlas]. This null result **refines** the narrow-distribution claim: lanmodulin is restricted to methylotroph families, but the threshold miss does not by itself show that lanmodulin is weakly coupled to xoxF. Biological decoupling remains a hypothesis alongside annotation incompleteness [src: lanthanide_methylotrophy_atlas].

Taken together, these counts suggest the hypothesis that the two genes do not mark each other reliably in either direction. Many *Methylobacterium* genomes carry xoxF without lanmodulin, and some lanmodulin genomes lack annotated xoxF. If this holds, it matters for environmental surveys that rely on dehydrogenase markers, such as those discussed in [[concepts/environmental-distribution-of-lanthanide-methylotrophy]]. The inference rests on annotation-based counts from a single project [src: lanthanide_methylotrophy_atlas].

## Open Directions

- Re-annotate the 13/62 lanmodulin-without-xoxF genomes with a profile-HMM or homology search for xoxF and other lanthanide-MDH genes. This would test whether the shortfall below the 80 % threshold reflects annotation incompleteness or a genuine alternative lanthanide-handling pathway [src: lanthanide_methylotrophy_atlas].
- Map xoxF carriage (102/209 *Methylobacterium* genomes) and lanmodulin carriage (46/209) onto a *Methylobacterium* phylogeny. This would show whether lanmodulin gain or loss is clade-structured and whether the chelator-dehydrogenase mismatch has a phylogenetic basis [src: lanthanide_methylotrophy_atlas].
- Screen the uncharacterised Acetobacteraceae genus `g__BOG-930` (12 lanmodulin genomes) for methylotrophy genes and environmental origin. This would test whether lanmodulin carriage outside *Methylobacterium* also tracks a methylotrophic lifestyle [src: lanthanide_methylotrophy_atlas].
