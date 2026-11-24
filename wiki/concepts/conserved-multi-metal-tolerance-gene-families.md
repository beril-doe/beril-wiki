---
type: "Concept"
description: "Ortholog groups important for multiple metals across several organisms, their functions, and their potential use in engineering tolerance or bioremediation."
sources: ["summaries/metal_cross_resistance__REPORT.md"]
---
# Conserved multi-metal tolerance gene families

This page covers conserved multi-metal tolerance gene families: ortholog groups important for multiple metals across several organisms, their functions, and their potential use in engineering tolerance or bioremediation. The metal_cross_resistance report identified 318 such groups and proposes them as shared multi-metal tolerance machinery. [src: metal_cross_resistance] The engineering use is a proposal, not a tested result. See [[summaries/metal_cross_resistance__REPORT]] for the full report.

## Literature Context

The candidate papers mostly concern metal resistance genes found in environmental and clinical isolates and metagenomes. They do not test conserved multi-metal tolerance families defined by fitness data. Several describe named resistance genes. A landfill-leachate metagenomic study of 13 landfills across six regions in China named arsB and copA as dominant metal resistance genes. It reported that Cu, Zn, Cr and As were important for the formation and stability of pathogen-metal resistance gene-virulence gene assemblies [PMID 41217278](https://pubmed.ncbi.nlm.nih.gov/41217278/). In wastewater pipe sediment, tetracycline and Cu stress increased the abundance of genes encoding efflux pumps, including copA and copB, and promoted intl1-mediated horizontal gene transfer [PMID 40721230](https://pubmed.ncbi.nlm.nih.gov/40721230/). Genome analyses of single isolates also report metal resistance genes. Exiguobacterium sp. E21L carries czcD, copB and nikA, and the authors suggest potential horizontal gene transfer from genomic islands [PMID 40148599](https://pubmed.ncbi.nlm.nih.gov/40148599/). Pseudomonas sp. P11 carries operons and gene clusters for multiple heavy metal tolerance, and its paralogous arsenic resistance genes show different evolutionary paths [PMID 31471685](https://pubmed.ncbi.nlm.nih.gov/31471685/). Arctic haemolytic isolates also carried heavy metal and disinfectant resistance genes [PMID 39440916](https://pubmed.ncbi.nlm.nih.gov/39440916/). Each of these is a single-strain or survey observation, not a cross-organism ortholog analysis.

Two reviews give general context on mobility. Conjugation can spread traits including resistance to heavy metals [PMID 33105635](https://pubmed.ncbi.nlm.nih.gov/33105635/). Prokaryotic transposable elements can carry heavy metal resistance genes [PMID 38819561](https://pubmed.ncbi.nlm.nih.gov/38819561/). These reviews show that some metal resistance determinants can move between cells. They do not say whether the broadly shared families in the hub page are mobile or not. A nematode study found that a gut bacterium, Brucella pseudogrignonensis, improved host survival under Cd(II) exposure. The mechanism was host glutathione S-transferase detoxification and immune activation, so it is a host-microbe result and not bacterial gene conservation [PMID 42142804](https://pubmed.ncbi.nlm.nih.gov/42142804/).

The metal_cross_resistance report identified 318 ortholog groups important for at least two metals in at least two organisms. The broadest span up to 14 organisms, and their functions include cell envelope, energy metabolism, DNA repair and ion homeostasis. This is broadly consistent with the literature in one narrow respect: metal-related efflux and homeostasis functions, such as the copper efflux genes copA and copB, appear in the candidate studies. The match is partial, because the candidates concern named genes in particular environments or strains. The report's claim of conserved multi-metal families across diverse bacteria extends this literature. It rests on cross-organism fitness data, which none of the candidates provide. The proposal to use these families for engineered tolerance or bioremediation is untested in the corpus. The candidates do not test it either. The nematode study is the only one that frames bioremediation, and it does so through a bacterial symbiont and not through gene engineering [PMID 42142804](https://pubmed.ncbi.nlm.nih.gov/42142804/). The corpus's claim is therefore novel relative to these papers and still needs direct validation.

The antibiotic nitrogen-cycling review [PMID 38615962](https://pubmed.ncbi.nlm.nih.gov/38615962/) and the Mycobacterium marinum acetyltransferase study [PMID 40680026](https://pubmed.ncbi.nlm.nih.gov/40680026/) are not relevant to this topic.

## Conserved cross-resistance families

Notebook NB05 identified 318 ortholog groups (OGs) that are metal-shared (important for ≥2 metals) in ≥2 organisms. [src: metal_cross_resistance] The most broadly conserved families span up to 14 organisms. They encode cell envelope, energy metabolism, DNA repair (DNA is deoxyribonucleic acid) and ion homeostasis functions. [src: metal_cross_resistance]

The report interprets these families as the core machinery of multi-metal tolerance. In its words, they are consistently required for defense against multiple metals across phylogenetically diverse bacteria. [src: metal_cross_resistance]

## Proposed uses

The report proposes the 318 families as candidates for engineering enhanced metal tolerance or for bioremediation applications. [src: metal_cross_resistance]

## Proposed follow-up

The report suggests applying independent component analysis (ICA) from the fitness_modules project to metal conditions. This would identify co-regulated metal-response modules. It would also test whether cross-resistance genes cluster into coherent regulatory units. [src: metal_cross_resistance] See [[concepts/metal-responsive-ica-fitness-modules]]. It also suggests using AlphaFold structures to ask whether metal-shared proteins have metal binding sites or membrane interfaces that explain multi-metal sensitivity. [src: metal_cross_resistance]

## Open Directions

- Run ICA on metal conditions only and check whether members of the 318 families fall into the same modules. This would show whether they form regulatory units.
- Compare AlphaFold structures of proteins in the broadest families, those spanning up to 14 organisms, for metal binding sites or membrane interfaces.
- Test one or two of the broadest families, such as a DNA-repair or ion-homeostasis family, by overexpression in a single host. This would check the engineering proposal.
