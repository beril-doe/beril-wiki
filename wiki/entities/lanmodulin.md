---
type: "Gene_Or_Pathway"
description: "Lanthanide-binding protein whose genome annotation differs sharply between Bakta products and eggNOG preferred names."
sources: ["summaries/discoveries.md", "summaries/lanthanide_methylotrophy_atlas__REPORT.md"]
aliases: ["lanM"]
---
# Lanmodulin

Lanmodulin (also written lanM) is a lanthanide-binding protein. In KBase Data Lakehouse pangenome annotations, its two annotation sources disagree completely: Bakta products and eggNOG preferred names flag different genomes. The evidence is direct counts from a calibration on 134K pangenome genomes, and the reports recommend Bakta only. [src: discoveries, lanthanide_methylotrophy_atlas]

## Key facts

- Cotruvo et al. (2018, JACS) discovered lanmodulin in *Methylobacterium extorquens* AM1 and characterised picomolar rare-earth-element binding. [src: lanthanide_methylotrophy_atlas] See [[entities/methylobacterium-extorquens]].
- NB01 calibration on 134K pangenome genomes shows that the two annotation sources disagree completely. [src: discoveries]
- In the hit-bearing genome matrix, 0 genomes are called by both sources, 505 by eggNOG only and 62 by Bakta only. [src: lanthanide_methylotrophy_atlas]

## Bakta product='Lanmodulin'

Bakta flags 62 genomes, all in α-Proteobacterial methylotroph clades: Beijerinckiaceae *Methylobacterium*, Acetobacteraceae BOG-930 and Hyphomicrobiaceae. [src: discoveries, lanthanide_methylotrophy_atlas] These 62 genomes represent 10 species in the atlas. [src: lanthanide_methylotrophy_atlas] All 62 (62/62 = 100 %) fall within Beijerinckiaceae, Acetobacteraceae or Hyphomicrobiaceae, the three families pre-specified in H3. [src: lanthanide_methylotrophy_atlas] A one-sided binomial test against the 80 % threshold gave p = 9.8 × 10⁻⁷, so H3a is strongly supported. [src: lanthanide_methylotrophy_atlas] The report says this 100 % restriction at Lakehouse scale tightens the restriction compared with Cotruvo's small-scale survey. [src: lanthanide_methylotrophy_atlas] See [[concepts/lanmodulin-clade-restriction-and-xoxf-co-occurrence]] and [[entities/bakta]].

Co-occurrence with xoxF from any source is 49/62 = 79.0 %. That is just under the pre-registered 80 % threshold (one-sided binomial p = 0.65), so H3b is not formally supported. [src: lanthanide_methylotrophy_atlas] The report suggests the 13/62 genomes without xoxF may reflect annotation incompleteness or alternative lanthanide-handling pathways, since lanmodulin can bind REEs without being co-located with a lanthanide-MDH operon. [src: lanthanide_methylotrophy_atlas]

## eggNOG Preferred_name='lanM'

eggNOG flags 505 additional genomes, none also Bakta-validated. They concentrate in unrelated gut Bacillota: *Streptococcus pneumoniae* 10, *Blautia_A wexlerae* 9, *Enterococcus faecalis* 8 and *Ruminococcus_B gnavus* 8. [src: discoveries] The report adds *Streptococcus pyogenes* (7) and notes that none of these are lanthanide users. [src: lanthanide_methylotrophy_atlas] The report describes the 505 as false positives concentrated in a handful of *Streptococcus*, *Blautia* and *Enterococcus* species. [src: lanthanide_methylotrophy_atlas]

The reports suggest that the eggNOG label appears to be stale or seed-ortholog mislabeling rather than a true homology call. [src: discoveries] They also suggest it may be a propagated misannotation that is worth reporting upstream. [src: lanthanide_methylotrophy_atlas] See [[entities/eggnog-orthologous-groups]].

## Practical guidance

For Lakehouse pangenome lanmodulin analyses, use Bakta product='Lanmodulin' exclusively and treat eggNOG Preferred_name='lanM' as zero-information. [src: discoveries] The atlas likewise names the Bakta product as the trustworthy lanmodulin source for methylotrophy markers. [src: lanthanide_methylotrophy_atlas] It reports a tight 100 % clade boundary for Bakta-validated lanmodulin. [src: lanthanide_methylotrophy_atlas] Related background: [[concepts/annotation-source-disagreement-and-coverage]].
