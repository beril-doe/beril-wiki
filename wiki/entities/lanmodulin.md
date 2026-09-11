---
type: "Gene_Or_Pathway"
description: "Lanmodulin is a clade-restricted lanthanide-handling protein marker."
sources: ["summaries/lanthanide_methylotrophy_atlas__REPORT.md"]
---
# Lanmodulin

## Identity

**Canonical name:** Lanmodulin. In this study, lanmodulin refers to the Bakta-validated product annotation `Lanmodulin`. [src: lanthanide_methylotrophy_atlas]

**Known aliases:** No aliases are specified in the report. [src: lanthanide_methylotrophy_atlas]

**Stable external identifier:** No stable external identifier is reported. [src: lanthanide_methylotrophy_atlas]

Lanmodulin is used as a marker of lanthanide handling in the atlas of methylotrophy-associated genes. [src: lanthanide_methylotrophy_atlas]

## Evidence from the lanthanide methylotrophy atlas

Bakta-validated lanmodulin occurs in 62 genomes spanning 10 species. [src: lanthanide_methylotrophy_atlas]

All 62 of 62 lanmodulin-positive genomes occur within Beijerinckiaceae, Acetobacteraceae, or Hyphomicrobiaceae, supporting clade restriction with a one-sided binomial p-value of 9.8 × 10⁻⁷ against the 80% threshold. [src: lanthanide_methylotrophy_atlas]

Lanmodulin co-occurs with xoxF in 49 of 62 genomes, or 79.0%, just below the preregistered 80% threshold; the one-sided binomial p-value is 0.65, so the report does not formally support the co-occurrence hypothesis. [src: lanthanide_methylotrophy_atlas]

The 13 of 62 lanmodulin-positive genomes without xoxF may reflect annotation incompleteness or alternative lanthanide-handling pathways, while xoxF-positive genomes without lanmodulin may use other mechanisms; these interpretations are hypotheses rather than established functional demonstrations. [src: lanthanide_methylotrophy_atlas]

The dominant carrier is [[entities/methylobacterium-extorquens]] (*Methylobacterium extorquens*), with 22 genomes and 1 lanmodulin copy per genome. [src: lanthanide_methylotrophy_atlas]

Other reported carriers include an uncharacterised Acetobacteraceae genus, g__BOG-930, with 12 genomes; *M. thiocyanatum* with 6; *M. rhodesianum* with 6; *M. aminovorans* with 4; *Hyphomicrobium_B* with 2; and *Methylocella* with 2. [src: lanthanide_methylotrophy_atlas]

The report found 505 eggNOG-only lanmodulin calls and 62 Bakta-only calls in a 134,578-row hit-bearing matrix, with 0 calls shared by both sources. [src: lanthanide_methylotrophy_atlas]

The 505 eggNOG `Preferred_name = lanM` calls were concentrated in unrelated gut Bacillota, including *Streptococcus pneumoniae* (10), *Blautia_A wexlerae* (9), *Enterococcus faecalis* (8), *Ruminococcus_B gnavus* (8), and *Streptococcus pyogenes* (7). [src: lanthanide_methylotrophy_atlas]

Because Bakta product = Lanmodulin identified 62 genomes, all in canonical α-Proteobacterial methylotroph clades, the report recommends using Bakta product annotations exclusively for future KBase Data Lakehouse lanmodulin analyses. [src: lanthanide_methylotrophy_atlas]

## Interpretation and limitations

The strict clade distribution supports lanmodulin as a more specific marker than the eggNOG `lanM` calls, but annotation evidence alone does not establish lanmodulin activity or lanthanide-dependent methylotrophy. [src: lanthanide_methylotrophy_atlas]

The 13 lanmodulin-positive genomes lacking xoxF and the 3,272 eggNOG-only xoxF calls indicate that marker presence and marker co-occurrence should not be treated as complete evidence for a shared pathway. [src: lanthanide_methylotrophy_atlas]

The report proposes examining lanmodulin sequence diversity in 22 *Methylobacterium extorquens* genomes, each carrying 1 copy. [src: lanthanide_methylotrophy_atlas]

## Related pages

- [[entities/xoxf]]
- [[entities/xoxj]]
- [[entities/bakta]]
- [[entities/eggnog]]
- [[entities/methylobacterium-extorquens]]
- [[concepts/gene-function-acquisition-depth]]
- [[concepts/pangenome-integration]]
- [[summaries/lanthanide_methylotrophy_atlas__REPORT]]
