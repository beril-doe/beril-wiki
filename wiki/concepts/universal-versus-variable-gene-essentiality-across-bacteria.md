---
type: "Concept"
description: "How many gene families are essential in every bacterium versus only in some, what that implies for minimal gene sets and drug targets, and where it stops (conservation in genomes is a separate concept)."
sources: ["summaries/conservation_fitness_synthesis__REPORT.md", "summaries/discoveries.md", "summaries/essential_genome__REPORT.md", "summaries/essential_metabolome__REPORT.md", "summaries/field_vs_lab_fitness__REPORT.md"]
---
# Universal versus variable gene essentiality across bacteria

Across 48 bacteria with random barcode transposon sequencing (RB-TnSeq) data from the Fitness Browser (FB), a small share of ortholog families is essential everywhere, and most essential families are essential only in some organisms. The evidence is direct measurement in one dataset, analysed in the essential_genome project. A separate synthesis report still lists universal essentiality across 43 organisms as an open question. [src: conservation_fitness_synthesis] Conservation of genes in genomes is a different concept; see [[concepts/essential-genes-and-core-genome-conservation]].

## How many families are universal, variable or never essential

The analysis covers 221,005 genes across 48 organisms, of which 41,059 (18.6%) are essential. [src: essential_genome] Essentiality rates range from 12.2% in Pedo557 to 29.7% in Magneto. [src: essential_genome] Bidirectional best hit (BBH) pairs, 2,838,750 in all, yield 17,222 ortholog groups spanning all 48 organisms. [src: essential_genome] A family counts as universally essential if it is essential in every organism where it has members. [src: essential_genome]

Most families fall into the never-essential class. The split is as follows:

- Universally essential: 859 of 17,222 families (5.0%). [src: discoveries, essential_genome]
- Variably essential, meaning essential in some organisms and not in others: 4,799 families (27.9%). [src: discoveries, essential_genome]
- Never essential: 11,564 families (67.1%). [src: discoveries, essential_genome]

Another section of the report calls variably essential families the largest category (4,799, 28%). [src: essential_genome] Among variable families, median essentiality penetrance is 33%. [src: essential_genome] 813 variable families are more than 50% essential, and 704 are less than 10% essential. [src: essential_genome] Separately, 7,084 essential genes have no orthologs in any other FB organism. [src: essential_genome] Clade size does not predict essentiality rate (rho=-0.13, p=0.36). [src: essential_genome]

Among the 859 universal families, 839 are strict single-copy families (copy ratio <=1.5, no non-essential paralogs), and 20 contain paralogs. [src: essential_genome] A tabulated file of these families lists 859 families across 45 organisms. [src: essential_metabolome]

## The pan-bacterial core

Fifteen families are essential in all 48 organisms with no exceptions. [src: essential_genome, discoveries] They are ten ribosomal proteins (rpsC, rplW, rplK, rplB, rplA, rplF, rps11, rpsJ, rpsI, rpsM), the chaperonin groEL, CTP synthase pyrG, elongation factor G fusA, valyl-tRNA synthetase valS and geranyltranstransferase SelGGPS. [src: discoveries] The report calls these the irreducible essential core of bacterial life. [src: discoveries] See also [[entities/ribosomal-protein-families]].

The report treats this set as consistent with Koonin (2003), who estimated ~60 proteins common to all cellular life. [src: essential_genome] It suggests the cell wall and nucleotide metabolism genes among the 15 may be bacteria-specific essentials. [src: essential_genome]

The 859-family set is larger than the ~206-gene minimal set that Gil et al. (2004) proposed. [src: essential_genome] The report attributes this to including free-living bacteria with larger genomes, not only obligate symbionts. [src: essential_genome] It also says its experimental set is smaller than computational conservation sets because it requires lethal transposon disruption in all 48 organisms. [src: essential_genome] Duffield et al. (2010) predicted 52 conserved essential proteins across 14 genomes computationally. The report calls its experimental approach complementary. [src: essential_genome]

## Variable essentiality and context

The report reads variable essentiality as showing that genomic context shapes viability requirements. [src: discoveries] It names paralogs, alternative pathways and compensatory accessory-genome functions as the likely context. [src: essential_genome] This is the report's interpretation, stated as such.

Within-species precedent comes from several studies the reports cite:

- Rosconi et al. (2022) showed strain-dependent essentiality in *S. pneumoniae*, shaped by the accessory genome. [src: essential_genome, field_vs_lab_fitness] It spanned 36 strains. [src: essential_genome]
- Lee et al. (2015) found 352 general and 199 condition-specific essential genes in *P. aeruginosa* across six media. [src: field_vs_lab_fitness]
- Akusobi et al. (2025) found 259 core essential and 425 differentially required genes across 21 *M. abscessus* isolates. [src: field_vs_lab_fitness]

The report extends this to species: the same gene can be essential in Methanococcus but dispensable in Pseudomonas, depending on metabolic context. [src: essential_genome] It asserts this holds across Proteobacteria, Bacteroidetes, Firmicutes and Archaea. [src: essential_genome]

## Implications for drug targets

The report argues that only the 859 universally essential families are reliable broad-spectrum antibiotic targets. [src: essential_genome] This is the report's assertion. A family essential in a given pathogen but variable elsewhere would be a narrower target.

## Open Directions

- Test whether the 859 universal families remain essential in organisms outside the 48 (the synthesis report poses this for 43 organisms [src: conservation_fitness_synthesis]). Use RB-TnSeq or essentiality calls from other collections. This would show whether the set is truly universal or specific to this panel.
- For the 4,799 variable families, link essential versus non-essential calls to paralog counts, pathway redundancy and accessory-gene presence. This would test the context explanation, which the report proposes.
- Compare the 859 families with computational minimal sets such as Gil et al. (2004) and Duffield et al. (2010) family by family. This would show which differences come from the experimental criterion and which from genome size.
- Check the 839 single-copy universal families against known antibiotic targets and human homologs. This would test the broad-spectrum target claim.
- Look at the 7,084 essential genes with no orthologs in other FB organisms. They may be orphan essentials, or they may reflect orthology-calling limits.
