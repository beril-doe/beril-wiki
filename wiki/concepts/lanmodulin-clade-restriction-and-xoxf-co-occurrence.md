---
type: "Concept"
description: "Phylogenetic distribution of lanmodulin-carrying genomes and their co-occurrence with xoxF; stops at marker calibration."
sources: ["summaries/lanthanide_methylotrophy_atlas__REPORT.md"]
---
# Lanmodulin clade restriction and xoxF co-occurrence

This page covers the phylogenetic distribution of lanmodulin-carrying genomes and their co-occurrence with xoxF. Carriage is restricted to three α-Proteobacterial families, and xoxF co-occurrence falls just under the pre-registered threshold. [src: lanthanide_methylotrophy_atlas] The lanmodulin counts come from one report's 62 lanmodulin-positive genomes, and its conclusion about breadth is limited to that resolution. [src: lanthanide_methylotrophy_atlas] See [[entities/lanmodulin]] and [[summaries/lanthanide_methylotrophy_atlas__REPORT]].

## Literature Context

The one candidate paper, available to this session as an abstract only, is [PMID 33035309](https://pubmed.ncbi.nlm.nih.gov/33035309/). It addresses lanthanide availability and microbial C1 metabolism. It says that research over the last decade has shown lanthanides to play an important role in microbial carbon metabolism, particularly methylotrophy. It also says that environmental omics studies have revealed lanthoenzymes to be dominant in some environments. Separately, it says that laboratory studies have shown lanthoenzymes to be favored over their calcium-containing counterparts even when calcium is far more abundant. The preference claim comes from laboratory studies, not from environmental omics. [PMID 33035309](https://pubmed.ncbi.nlm.nih.gov/33035309/)

The abstract also says lanthanides are common in rocks but occur at exceedingly low levels in most natural waters, in the picomolar to nanomolar range. Volcanic hot springs are the exception and can reach micromolar concentrations. Bacteria that use lanthanides for growth on simple carbon compounds such as methanol and ethanol grow optimally at micromolar concentrations. The authors say it is highly likely that environmental bacteria have evolved specialized lanthanide sequestration and high-affinity uptake systems. That statement is an inference, not a measured result. They report identifying genes encoding the lanthanide-binding protein lanmodulin in soil metagenomes. They suggest, without testing it in the abstract, that lanmodulin may help cells distinguish calcium from lanthanides. They conclude that more research is needed on microbial adaptations to lanthanide scarcity. [PMID 33035309](https://pubmed.ncbi.nlm.nih.gov/33035309/)

The corpus findings in lanmodulin clade restriction and xoxF co occurrence are partly consistent with this paper and partly extend it. The paper expects lanmodulin to matter in lanthanide-scarce settings, and the abstract reports lanmodulin genes in soil metagenomes. The corpus finds Bakta-validated lanmodulin in 62 genomes representing 10 species, all within Beijerinckiaceae, Acetobacteraceae or Hyphomicrobiaceae. That is a genome-level, taxonomically resolved picture, which the abstract does not give. The corpus therefore adds a clade restriction that the abstract does not address. It also leads the report to conclude that lanmodulin is not a phylogenetically widespread REE handler, but only at the 62-genome resolution. The abstract's soil metagenome finding does not say which taxa carry the genes, so the two are not in direct conflict. They could be compared only by assigning the metagenomic lanmodulin genes to lineages.

The corpus's xoxF co-occurrence result is novel relative to this candidate. Lanmodulin and xoxF co-occur in 49 / 62 = 79.0 % of lanmodulin-positive genomes, just under the pre-registered 80 % threshold, so H3b is not formally supported. The abstract says nothing quantitative about co-occurrence. Its emphasis on lanthanide-dependent methylotrophy fits the report's reading that lanmodulin-without-xoxF genomes may reflect annotation incompleteness or alternative lanthanide handling. That reading is an interpretation, not a tested result.

## Clade restriction

Bakta-validated `product = 'Lanmodulin'` is detected in 62 genomes representing 10 species. [src: lanthanide_methylotrophy_atlas] All 62 (62 / 62 = 100 %) fall within Beijerinckiaceae, Acetobacteraceae or Hyphomicrobiaceae, the three α-Proteobacterial methylotroph families pre-specified in hypothesis H3. [src: lanthanide_methylotrophy_atlas] A one-sided binomial test against the 80 % threshold gives p = 9.8 × 10⁻⁷, so H3a is strongly supported. [src: lanthanide_methylotrophy_atlas] The report says this tightens the restriction substantially compared with Cotruvo's small-scale survey. [src: lanthanide_methylotrophy_atlas]

The report calls this restriction unusual for a protein supposedly "central to bacterial REE biology". It concludes that lanmodulin is not a phylogenetically widespread REE handler, but only at the 62-genome resolution. [src: lanthanide_methylotrophy_atlas]

### Who carries it

[[entities/methylobacterium-extorquens]] is the dominant carrier, with 22 genomes and 1 lanmodulin copy each, so there is no paralog story. [src: lanthanide_methylotrophy_atlas] The report proposes aligning representative lanmodulin cluster proteins in this species to test whether the protein has diversified within a single operon-defined locus or is invariant across the species. [src: lanthanide_methylotrophy_atlas] Other contributors are listed below.

| Taxon | Lanmodulin genomes |
|---|---|
| g__BOG-930 (uncharacterised Acetobacteraceae genus) | 12 [src: lanthanide_methylotrophy_atlas] |
| Methylobacterium thiocyanatum | 6 [src: lanthanide_methylotrophy_atlas] |
| Methylobacterium rhodesianum | 6 [src: lanthanide_methylotrophy_atlas] |
| Methylobacterium aminovorans | 4 [src: lanthanide_methylotrophy_atlas] |
| Hyphomicrobium_B | 2 [src: lanthanide_methylotrophy_atlas] |
| Methylocella | 2 [src: lanthanide_methylotrophy_atlas] |

Among 209 Methylobacterium genomes, 102 carry xoxF and 46 carry lanmodulin. The report calls this consistent with the lanthanide-switch model. [src: lanthanide_methylotrophy_atlas]

## xoxF co-occurrence

Lanmodulin and xoxF (from any source) co-occur in 49 / 62 = 79.0 % of lanmodulin-positive genomes. This is just under the 80 % threshold (one-sided binomial p = 0.65), so H3b is not formally supported. [src: lanthanide_methylotrophy_atlas]

The report reads the mismatches in both directions as suggestive. Lanmodulin may have binding or transport roles decoupled from methanol-oxidation operons. Some XoxF-bearing genomes may handle REEs without lanmodulin's small-protein chelation pathway. [src: lanthanide_methylotrophy_atlas] The 13/62 lanmodulin-without-xoxF genomes may reflect annotation incompleteness or genuine alternative lanthanide-handling pathways, because lanmodulin can bind REEs without being co-located with a lanthanide-MDH operon. [src: lanthanide_methylotrophy_atlas] These are interpretations, not tested results.

## Open Directions

- Run the multiple-sequence alignment of M. extorquens lanmodulin proteins described above, to settle diversification versus invariance.
- Re-survey lanmodulin in a much larger genome set. This would test whether the 100 % clade restriction survives beyond 62 genomes.
- Inspect the 13 lanmodulin-without-xoxF genomes for missed xoxF calls or other lanthanide-handling genes. This would separate annotation incompleteness from alternative pathways.
