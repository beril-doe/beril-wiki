---
type: "Gene_Or_Pathway"
description: "Respiratory Complex I links NADH flux to condition-specific fitness in ADP1"
sources: ["summaries/aromatic_catabolism_network__REPORT.md", "summaries/respiratory_chain_wiring__REPORT.md"]
---
# Complex I

## Identity

**Canonical name:** Complex I. [src: aromatic_catabolism_network]

**Known aliases:** NADH:ubiquinone oxidoreductase; NDH-1; nuoA–N respiratory complex. [src: aromatic_catabolism_network]

**Stable external identifier:** No stable external identifier was specified in the source. [src: aromatic_catabolism_network]

Complex I is a multi-subunit respiratory subsystem that oxidizes NADH and supports high-flux catabolism by transferring reducing power into the respiratory chain. [src: aromatic_catabolism_network] In ADP1 it is a 13-subunit, proton-pumping complex that translocates 4 H⁺/NADH. [src: respiratory_chain_wiring]

## Evidence from the aromatic-catabolism network

Complex I is the largest support subsystem in the 51-gene quinate-catabolism network, containing 21/51 quinate-specific genes, or 41% of the network. [src: aromatic_catabolism_network]

The network analysis links Complex I to oxidation of NADH generated when aromatic-catabolism products enter the TCA cycle. [src: aromatic_catabolism_network]

[[entities/flux-balance-analysis|Flux-balance analysis]] predicts 1.76× higher Complex I flux on aromatic substrates than on the comparison condition, with fluxes of 0.55 versus 0.31. [src: aromatic_catabolism_network]

Despite this increased predicted flux, the model predicts 0% Complex I essentiality, indicating a gap between modeled respiratory demand and gene-level dependency. [src: aromatic_catabolism_network]

A total of 30/51 quinate-specific genes have no FBA reaction mappings, including newly identified Complex I-associated functions. [src: aromatic_catabolism_network]

The source interprets this discrepancy as an [[concepts/metabolic-model-gapfilling|FBA model gap]]: growth-optimizing linear programming can redistribute flux through alternative routes, whereas disruption of a multi-subunit Complex I can eliminate complex function. [src: aromatic_catabolism_network] The respiratory-chain wiring analysis **supports and refines** this interpretation: FBA routes NADH through Complex I because it produces more ATP per NADH, predicting zero flux through alternative dehydrogenases and missing capacity constraints that can force suboptimal respiratory routes. [src: respiratory_chain_wiring]

Observed phenotypes support Complex I dependence more strongly than the model prediction: 10/13 Complex I operon subunits independently produce quinate-specific growth defects. [src: aromatic_catabolism_network]

## Organization and candidate components

The Complex I operon lies at 714–729 kb and contains 13 nuoA–N subunits on the same strand, with <100 bp intergenic distances. [src: aromatic_catabolism_network]

Two DUF-domain proteins, [[entities/aciad3137|ACIAD3137]] (UPF0234) and [[entities/aciad2176|ACIAD2176]] (DUF2280), correlate with Complex I genes at r > 0.98 and are candidate uncharacterized Complex I accessory factors. [src: aromatic_catabolism_network]

The 11 Complex I-associated assignments beyond the core nuo operon are based on phenotypic correlation and may represent indirect connections rather than physical association. [src: aromatic_catabolism_network]

## Condition-specific and cross-species fitness

The [[entities/kescience-fitnessbrowser|KBase Fitness Browser]] ortholog-transferred dataset contains 12,241 entries covering 2,005 genes and 13 conditions. [src: aromatic_catabolism_network]

Complex I orthologs have significantly worse fitness on aromatic conditions than on comparison conditions, with mean fitness values of -1.35 versus -0.77 and Mann–Whitney p < 0.0001. [src: aromatic_catabolism_network]

The largest Complex I defects relative to background occur on acetate (-1.55) and succinate (-1.39), which are non-aromatic substrates that also generate high NADH flux through the TCA cycle. [src: aromatic_catabolism_network]

Complex I is reported as dispensable on glucose and lactate, consistent with the hypothesis that an alternative NADH dehydrogenase, [[entities/ndh-2|NDH-2]], compensates under lower NADH flux. [src: aromatic_catabolism_network] The new ADP1 analysis **supports** substrate-dependent wiring but **refines** the mechanism: Complex I growth ratios are 0.37 on quinate, 1.44 on glucose, and 0.49 on acetate, while quinate requires Complex I, lactate specifically requires cytochrome bo3, and glucose has no specifically required respiratory component. [src: respiratory_chain_wiring] The report proposes that quinate’s concentrated TCA-cycle NADH burst exceeds alternative dehydrogenase capacity, whereas glucose distributes NADH production; this is a biochemical interpretation based on theoretical stoichiometry rather than measured flux distributions. [src: respiratory_chain_wiring]

Because the transferred data mixes organisms with different respiratory-chain architectures, the cross-species evidence does not definitively establish the cause of Complex I dependence in [[entities/acinetobacter-baylyi-adp1|Acinetobacter baylyi]] ADP1. [src: aromatic_catabolism_network] The new comparison **contradicts** the predicted general compensation pattern: among filtered organisms, those with validated NDH-2 had a mean Complex I aromatic deficit of −0.297 versus −0.156 without validated NDH-2 (p = 0.52), although only 4 organisms lacked NDH-2. [src: respiratory_chain_wiring]

## Interpretation and open directions

The report's novel finding is a proposed relationship between Complex I dependence and high NADH flux rather than aromatic chemistry alone. [src: aromatic_catabolism_network] Proteomics **supports** a passive, flux-based rather than transcriptionally switched model: Complex I, NDH-2, and ACIAD3522 had protein levels of 27.6, 27.0, and 26.2, respectively, compared with a genome median of 26.4. [src: respiratory_chain_wiring]

This interpretation remains a hypothesis because direct Complex I fitness measurements on aromatic substrates in a single organism are not yet available in the source analysis. [src: aromatic_catabolism_network] NDH-2 is a core, standalone gene identified as ACIAD_RS16420 (KO K03885), but it has no growth data; ACIAD3522 is dispensable on quinate and glucose and has a 0.013 growth ratio on acetate, where its function may not be respiratory. [src: respiratory_chain_wiring]

Specific tests include searching the ADP1 genome for NDH-2, testing NDH-2 deletion on quinate versus glucose, validating ACIAD3137 and ACIAD2176 by protein-interaction or co-purification experiments, and adding respiratory-chain capacity constraints to the ADP1 FBA model. [src: aromatic_catabolism_network] The first search is now resolved, while deletion experiments, NADH/NAD⁺ measurements, ACIAD3522 characterization, expanded KO-based cross-species analysis, and quinate-versus-succinate respiratory proteomics remain tests of the wiring hypothesis. [src: respiratory_chain_wiring]

## Related pages

- [[summaries/aromatic_catabolism_network__REPORT]] — source summary for the Complex I support-network analysis. [src: aromatic_catabolism_network]
- [[summaries/respiratory_chain_wiring__REPORT]] — source summary for condition-specific respiratory-chain configuration in ADP1.
- [[concepts/gene-essentiality]] — contrasts observed Complex I defects with 0% model-predicted essentiality.
- [[concepts/metabolic-model-gapfilling]] — covers unmapped support functions and respiratory blind spots in FBA.
- [[concepts/cofitness-network-architecture]] — covers co-fitness assignment of Complex I-associated genes and candidate accessory factors.
- [[concepts/condition-specific-fitness]] — covers substrate-dependent Complex I fitness patterns.
- [[concepts/multi-omics-integration]] — covers integration of fitness, FBA, genomic organization, and transcriptomic evidence.
