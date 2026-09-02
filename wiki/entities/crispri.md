---
type: "Method"
description: "CRISPRi method for testing essential and functionally dark genes"
sources: ["summaries/functional_dark_matter__REPORT.md", "summaries/truly_dark_genes__REPORT.md"]
---
# CRISPRi-based transcriptional knockdown for testing essential dark genes

## What this entity is

**Canonical name:** CRISPRi-based transcriptional knockdown for testing essential dark genes. [src: functional_dark_matter]

**Known aliases:** CRISPRi; CRISPR interference; Mobile-CRISPRi. [src: functional_dark_matter]

**Stable external identifier:** None was specified in the source document. [src: functional_dark_matter]

CRISPRi, or CRISPR interference, is a method recommended for transcriptionally reducing expression of essential genes whose complete disruption prevents recovery of viable mutants. [src: functional_dark_matter]

## Key facts

The Functional Dark Matter report identified 9,557 essential dark genes among 57,011 dark genes. [src: functional_dark_matter]

These genes require a separate experimental strategy because standard [[entities/tnseq|RB-TnSeq]], randomly barcoded transposon sequencing, yields no viable knockout fitness profiles for essential genes. [src: functional_dark_matter]

Essential-gene candidates were prioritized using gene-neighbor context, cross-organism conservation, phylogenetic breadth, domain annotations, and CRISPRi tractability. [src: functional_dark_matter]

Among all 57,011 dark genes, 30,190 (52.9%) shared a predicted operon with an annotated gene, and 97.2% had at least one annotated neighbor within a five-gene window. [src: functional_dark_matter]

The report cautions that the 97.2% neighborhood rate is expected in part because the genome-wide annotation rate was 75%. [src: functional_dark_matter]

The highest-ranked essential candidates were *Escherichia coli* Keio 14796, with score 0.875 and a YbeY domain; MR-1 200382, with score 0.874 and RimP_N/DUF150_C domains; and *Klebsiella oxytoca* BWI76_RS08540, with score 0.865 and OmpA/TIGR02802 domains. [src: functional_dark_matter]

The recommended workflow is CRISPRi knockdown followed by growth measurements under standard and stress conditions. [src: functional_dark_matter]

The report specifically recommends Mobile-CRISPRi for organisms with less-established genetic tools. [src: functional_dark_matter]

The newer truly-dark-gene analysis **supports** this strategy by proposing Mobile-CRISPRi for rapid functional testing of its prioritized candidates, including genes selected from fitness, annotation, orthology, genomic-context, and tractability evidence. [src: truly_dark_genes]

It also **refines** the experimental design: proposed follow-up includes motility assays for PV4/5210953 and nitrogen-limitation growth assays for ANA3/7026383, rather than relying only on generic stress measurements. [src: truly_dark_genes]

CRISPRi therefore addresses a limitation of [[concepts/gene-essentiality|gene-essentiality]] analysis: essential dark genes lack direct transposon-derived fitness magnitudes, so controlled knockdown can provide condition-specific phenotypes for testing their inferred functions. [src: functional_dark_matter]

The truly-dark-gene report cautions that some strong fitness phenotypes may reflect polar effects on downstream genes, so CRISPRi results should be interpreted with operon structure and neighboring-gene measurements in mind. [src: truly_dark_genes]

Condition-specific growth measurements can connect essential-gene knockdown effects to [[concepts/condition-specific-fitness|condition-specific fitness]], while neighborhood and co-fitness evidence can refine candidate interpretation through [[concepts/cofitness-network-architecture|co-fitness network architecture]]. [src: functional_dark_matter]

The source reports are summarized at [[summaries/functional_dark_matter__REPORT]] and [[summaries/truly_dark_genes__REPORT]]. [src: functional_dark_matter], [src: truly_dark_genes]
