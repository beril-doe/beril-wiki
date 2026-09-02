<!-- tension-hash: ded38efd1d6fb53c -->
# System-Level Signals versus Marker-Level and Mechanistic Proof

The corpus contains several related disagreements about how far broad ecological, genomic, and co-occurrence signals can support mechanistic claims. [[concepts/phage-defense-syndromes-and-arms-race]] One side treats system-presence associations and species-level patterns as evidence of defense, prophage, or arms-race structure; the other emphasizes marker specificity, genomic adjacency, intactness, and direct functional validation. The disagreement matters because the same observations can support different conclusions about whether a system is present, how it acts, and whether it caused the observed ecological or antimicrobial-resistance pattern.

## Evidence Sides

**Broad system-level and ecological signal.** EggNOG description matching gives 96% CRISPR-Cas prevalence, while co-occurrence and arms-race patterns provide system-presence associations [src: phage_defense_arsenal]. The species-level prophage-density/AMR-breadth association has rho=0.572 across 4,770 species [src: prophage_amr_comobilization]. Environmental effects on prophage-module composition remained after genome-size stratification and exceeded the reported family-level phylogenetic effect [src: prophage_ecology]. SNIPE-associated observations include 4,572 DUF4041 clusters and DUF4041 detection in *Klebsiella* but not in *Acinetobacter*, *P. aeruginosa*, or *P. viridiflava* in the four-species comparison [src: snipe_defense_system].

**Marker-level and mechanistic caution.** The Cas1 PF01867 marker gives approximately 55%, and the DISARM anchor can identify non-DISARM SNF2 helicases [src: phage_defense_arsenal]. Only 54 of 4,572 DUF4041 clusters carried the Mug113 co-annotation, and DUF4041 may occur outside complete SNIPE architectures [src: snipe_defense_system]. Only 10.4% of AMR instances were within 10 genes of a strict prophage marker [src: prophage_amr_comobilization]. Genome size was still dominant (F=212.99), and prophage calls may include bacterial homologs and domesticated remnants [src: prophage_ecology]. SNIPE’s low Lambdavirus infection rate in PhageFoundry—1 of 188 *E. coli* strains, or 0.5%—does not establish that SNIPE caused the pattern; no *Klebsiella* SNIPE or ManYZ fitness data were available [src: snipe_defense_system]. Co-occurrence with mannose-transporter annotations was only consistent with, rather than proof of, defense at the phage-entry route [src: snipe_defense_system].

## Possible Reconciliations

- **Hypothesis — measurement scope:** Description matching and system-level co-occurrence may detect broader gene neighborhoods or defense-associated signals than a single conserved marker.
- **Hypothesis — architectural completeness:** DUF4041 clusters may represent partial, divergent, or non-SNIPE architectures, explaining the gap between 4,572 clusters and 54 Mug113 co-annotations.
- **Hypothesis — scale of association:** Species-level co-acquisition or shared ecological exposure could produce rho=0.572 without immediate AMR–prophage adjacency.
- **Hypothesis — call composition:** Environmental prophage-module effects may be ecological while still being inflated or altered by bacterial homologs and domesticated remnants.
- **Hypothesis — host-range context:** ManYZ variation or loss could explain low Lambdavirus infection without proving SNIPE-mediated defense.

## Resolving Work

- Re-analyze the same genomes with complete multi-marker architectures, neighborhood rules, and Cas1 PF01867, EggNOG, DISARM, DUF4041, and Mug113 calls; test whether system-level prevalence persists after specificity filters.
- Use closed, sequence-resolved genomes to measure strict prophage boundaries, intactness, AMR adjacency, and orientation; test whether the species-level association reflects direct mobilization or nonadjacent co-acquisition.
- Reclassify prophage calls against homolog and remnant databases, then repeat environmental models with genome size and phylogeny; test whether intact prophages retain the reported effects.
- Measure SNIPE, ManYZ genotype, Lambdavirus infection, and fitness across *E. coli* and *Klebsiella*; test whether ManYZ variation predicts infection and defense phenotypes.
