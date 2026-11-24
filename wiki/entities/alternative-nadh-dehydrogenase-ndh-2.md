---
type: "Gene_Or_Pathway"
description: "Non-proton-pumping NADH dehydrogenase that can substitute for Complex I at low NADH flux."
sources: ["summaries/aromatic_catabolism_network__REPORT.md", "summaries/discoveries.md", "summaries/respiratory_chain_wiring__REPORT.md"]
aliases: ["ACIAD_RS16420", "K03885", "NDH-2", "type II NADH dehydrogenase"]
---
# Alternative NADH dehydrogenase NDH-2

Alternative NADH dehydrogenase NDH-2 (type II NADH dehydrogenase) is a non-proton-pumping enzyme that can substitute for Complex I at low NADH flux. In ADP1 it is encoded by ACIAD_RS16420 (KEGG ortholog K03885). The evidence for its compensating role is indirect: ADP1 has no growth data for it, and a cross-species test did not support compensation after correction. [src: aromatic_catabolism_network, respiratory_chain_wiring, discoveries]

## Key facts

- Bacteria typically have branched respiratory chains with both proton-pumping Complex I (NDH-1) and non-pumping NDH-2. [src: aromatic_catabolism_network]
- NDH-2 can substitute for Complex I under low NADH flux but cannot match Complex I's capacity under high flux. [src: aromatic_catabolism_network]
- ADP1 NDH-2 has 1 subunit and does not pump protons. [src: respiratory_chain_wiring, discoveries]
- ADP1 NDH-2 is ACIAD_RS16420 with KO K03885. It is TnSeq-dispensable but missing from the deletion collection, so it has no growth data. [src: respiratory_chain_wiring]
- It is a standalone core-genome gene, not in a respiratory operon. [src: respiratory_chain_wiring]
- See [[entities/respiratory-complex-i-nadh-ubiquinone-oxidoreductase]] for the enzyme it backs up.

## Expression and flux modelling in ADP1

Under standard growth conditions, NDH-2 protein expression is 27.0 (59th percentile). The report states that it is not repressed but constitutively co-expressed with Complex I. [src: respiratory_chain_wiring] Flux balance analysis (FBA) predicts zero flux through NDH-2 on all standard carbon sources, routing all NADH through Complex I. [src: respiratory_chain_wiring] The report describes Complex I as the high-capacity primary system and NDH-2 as a low-capacity backup. It calls this consistent with Lencina et al. (2018), who showed NDH-2 can be the sole NADH dehydrogenase in some organisms (*S. agalactiae*). [src: respiratory_chain_wiring] See [[entities/flux-balance-analysis]].

## Proposed compensation for Complex I

The aromatic catabolism report proposes that ADP1's apparent quinate-specificity of Complex I likely reflects NDH-2 compensating on simpler substrates. [src: aromatic_catabolism_network] Its cross-species data show Complex I is dispensable on glucose and lactate, where NDH-2 suffices. Complex I is essential on substrates that generate high TCA (tricarboxylic acid) cycle flux: aromatics, acetate and succinate. [src: aromatic_catabolism_network] The respiratory wiring report suggests NDH-2 partially compensates on lactate, because Complex I has only a mild growth effect (0.77) there. [src: respiratory_chain_wiring] ADP1 NDH-2 is predicted to be a backup for glucose, but it has no growth data. [src: discoveries]

The aromatic catabolism report proposes a direct test: search the ADP1 genome for NDH-2 genes and, if present, compare their deletion phenotypes on quinate and glucose. This would show whether NDH-2 compensates for Complex I on non-aromatic substrates. [src: aromatic_catabolism_network]

## Tensions

- The cross-species compensation reading is supported in the aromatic catabolism report. [src: aromatic_catabolism_network] After NDH-2 false positives were corrected (text-matched candidates were filtered to organisms with ≤2 hits per genome), the test reversed. Organisms with validated NDH-2 showed larger Complex I aromatic deficits (mean -0.297) than those without (-0.156, p=0.52), so the test did not support cross-species compensation. [src: discoveries]

## Open Directions

- Construct an NDH-2 deletion, since the gene is missing from the deletion collection. Then measure growth on quinate, glucose and lactate.
- Repeat the cross-species test with validated NDH-2 calls and more organisms, to see whether the reversed result holds.

See also [[concepts/ndh-2-compensation-for-complex-i-loss-across-species]] and [[concepts/substrate-dependent-complex-i-requirement-and-ndh-2-compensation]].
