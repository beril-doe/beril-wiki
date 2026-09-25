<!-- tension-hash: e503d1e436885118 -->
# Conflict: a modest genome-wide conservation–fitness gradient versus an AMR-specific null

Three projects disagree about whether pangenome conservation — how widely a gene is shared across sampled genomes of a species, splitting genes into a near-universal "core" and a variable "accessory" fraction — carries information about fitness cost. One project reports no predictive relationship for antimicrobial resistance (AMR) genes specifically; others report a real but small genome-wide association between core membership and essentiality. The disagreement matters because a modest average gradient and a gene-class-specific null can both be true, and averaging them would erase the very distinction — between conservation, essentiality, and measured laboratory cost — that the concept [[concepts/pangenome-conservation-fitness-decoupling]] turns on.

## Evidence Sides

**The AMR-specific null.** One side is a null result specific to AMR genes, and it stays a null: the module-level result is directionally consistent with the opposing side but does not resolve the AMR-specific null, and a null must not be averaged away into a weak positive. [src: module_conservation]

**The modest genome-wide gradient.** A 33-organism integration presents the same directional association with a smaller effect — 86.1% core essential genes versus 81.2% core non-essential genes, and a median odds ratio (the multiplicative change in odds of core membership) of 1.56 — rather than resolving the tension. [src: conservation_vs_fitness] A synthesis likewise supports a modest genome-wide gradient, but shows that core genes can be more burdensome in the laboratory, so conservation, essentiality, and laboratory cost should not be treated as interchangeable. [src: conservation_fitness_synthesis]

**The module-level signal, with a scope caveat.** The module result — from independent component analysis (ICA), which decomposes fitness profiles into co-regulated gene modules — is directionally consistent with enrichment of conserved, coordinated fitness units (86.0% versus 81.5%), but it does not resolve the AMR-specific null, because ICA modules exclude essential genes and summarize module membership rather than AMR baseline means. [src: module_conservation]

## Possible Reconciliations

- *Hypothesis:* the difference reflects AMR biology — AMR genes are a gene class in which the genome-wide gradient genuinely does not hold. [src: conservation_vs_fitness]
- *Hypothesis:* the difference is an averaging artefact, a genome-wide mean absorbing a null subset. [src: conservation_vs_fitness]
- *Hypothesis:* organism composition or pangenome sampling differs between the analyses, shifting core/accessory labels. [src: conservation_vs_fitness]
- *Hypothesis:* incompatible essentiality definitions, or module-callability, make the two measurements non-comparable. [src: module_conservation]

## Resolving Work

- Restrict the 33-organism essential-versus-core comparison to AMR genes only, using the same Fisher-style enrichment test, and ask whether the 86.1%/81.2% contrast survives with AMR genes as the denominator. [src: conservation_vs_fitness]
- Run matched, condition-specific comparisons — same organisms, same conditions, same conservation labels — to test whether the disagreement is biological or compositional. [src: conservation_vs_fitness]
- Hold one essentiality definition fixed across both analyses and re-derive the odds ratio, asking how much of the gap is definitional. [src: conservation_vs_fitness]
- Recompute the module enrichment with AMR baseline means rather than module membership, and ask whether module-level conservation says anything about AMR fitness once essential genes are known to be excluded. [src: module_conservation]
- Separate conservation, essentiality, and laboratory cost as three measured variables in one model, and ask where core genes are more burdensome in the laboratory. [src: conservation_fitness_synthesis]
