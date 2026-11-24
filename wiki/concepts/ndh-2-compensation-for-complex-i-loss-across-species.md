---
type: "Concept"
description: "Covers whether type II NADH dehydrogenase presence predicts Complex I dispensability, including cross-species Fitness Browser tests and annotation caveats; stops at NADH dehydrogenases."
sources: ["summaries/aromatic_catabolism_network__REPORT.md", "summaries/discoveries.md", "summaries/respiratory_chain_wiring__REPORT.md"]
---
# NDH-2 compensation for Complex I loss across species

After false-positive NDH-2 calls were corrected, Fitness Browser (FB) data did not show that type II NADH dehydrogenase (NDH-2) presence predicts Complex I dispensability on aromatics. [src: respiratory_chain_wiring] The evidence is a small ortholog-transferred dataset of 14 organisms, so the result is weak. [src: respiratory_chain_wiring] Compensation is better described as a hypothesis for ADP1 than as a general rule. [src: respiratory_chain_wiring] See also [[concepts/substrate-dependent-complex-i-requirement-and-ndh-2-compensation]] and [[entities/alternative-nadh-dehydrogenase-ndh-2]].

## The ADP1 hypothesis

The aromatic_catabolism_network report proposes that ADP1's quinate-specific Complex I dependency likely reflects compensation by NDH-2 on simpler substrates. [src: aromatic_catabolism_network] The report states that NDH-2 can substitute for Complex I at low NADH (reduced nicotinamide adenine dinucleotide) flux but cannot match its capacity at high flux. [src: aromatic_catabolism_network] The discoveries digest repeats this as a hypothesis about lower-NADH-flux substrates. [src: discoveries] In ADP1, NDH-2 (one subunit, non-pumping) is predicted to back up glucose growth, but no growth data exist. [src: discoveries]

## Cross-species fitness: substrate, not aromatics

Cross-species Complex I dependency tracks high-NADH substrates rather than aromatics specifically. [src: aromatic_catabolism_network] In ortholog-transferred FB data (12,241 entries, 2,005 genes, 13 conditions), Complex I orthologs have significantly worse fitness on aromatic than non-aromatic conditions (mean = -1.35 vs -0.77, Mann-Whitney p < 0.0001). [src: aromatic_catabolism_network] Per condition, however, the largest defects relative to background are on acetate (-1.55) and succinate (-1.39), which are non-aromatic. [src: aromatic_catabolism_network, discoveries] The report states that its cross-species data show Complex I dispensable on glucose and lactate, where NDH-2 suffices, and essential on high-TCA-flux (tricarboxylic acid) substrates: aromatics, acetate and succinate. [src: aromatic_catabolism_network] The direct NDH-2 presence test below addresses aromatics only. It does not support NDH-2 presence as a predictor of Complex I dispensability there. [src: respiratory_chain_wiring]

## Direct test of NDH-2 presence

The direct test fails. The initial analysis found 10/14 organisms with NDH-2 and apparent support for compensation. That result came from misannotated Complex I subunits passing the text filter in 5 organisms. [src: discoveries] Organisms with more than 2 NDH-2 hits were excluded as likely misannotated Complex I subunits, and those with 1-2 hits were kept. [src: respiratory_chain_wiring] After this filter, 5 of 14 organisms have validated NDH-2. [src: respiratory_chain_wiring]

Organisms with NDH-2 then had larger Complex I aromatic deficits (mean -0.297) than those without (-0.156). This is the opposite of the compensation prediction, and it is not significant (p = 0.52). [src: discoveries, respiratory_chain_wiring] The report concludes that NDH-2 presence does not predict Complex I dispensability on aromatics. [src: respiratory_chain_wiring] It considers compensation likely ADP1-specific [src: respiratory_chain_wiring], and cautions that ADP1 respiratory wiring may be species-specific. [src: respiratory_chain_wiring]

## Annotation and sample caveats

- The comparison has only 4 organisms without NDH-2, too few for statistical significance. [src: respiratory_chain_wiring]
- NDH-2 calls used gene-description text matching, which likely gives false positives where Complex I subunits are incompletely annotated. [src: respiratory_chain_wiring] An example is pseudo3_N2E3, whose 8 "NDH-2" hits are probably a Complex I operon. [src: respiratory_chain_wiring]
- The NDH-2 search may also miss orthologs because annotation varies. [src: respiratory_chain_wiring]
- Ortholog-transferred fitness mixes organisms with different respiratory-chain architectures. Single-organism Complex I measurements on aromatics would be more definitive. [src: aromatic_catabolism_network]
- The report considers KEGG ortholog (KO)-based identification with K03885 more reliable than text matching. [src: respiratory_chain_wiring]
- The planned pangenome KO co-occurrence analysis was not performed, so NDH-2 and Complex I co-occurrence across Acinetobacter species is untested. [src: respiratory_chain_wiring]
- The report proposes querying the full KBase Data Lakehouse pangenome for NDH-2 (K03885) and Complex I (K00330-K00343) co-occurrence across 27K species, which would give a much larger sample. [src: respiratory_chain_wiring]

## Open Directions

- Re-identify NDH-2 in FB organisms by KO (K03885) instead of text matching, then repeat the aromatic-deficit comparison. This would remove the annotation false positives that reversed the first result.
- Run the pangenome co-occurrence query for K03885 and K00330-K00343 across the 27K species. This would replace the 14-organism sample.
- Run the unperformed Acinetobacter co-occurrence analysis to test whether NDH-2 and Complex I co-occur.
- Measure Complex I fitness on aromatic, acetate, succinate, glucose and lactate substrates in single organisms with and without validated NDH-2. This avoids mixed architectures.
- Collect ADP1 growth data for NDH-2 on glucose to test the predicted backup role.
