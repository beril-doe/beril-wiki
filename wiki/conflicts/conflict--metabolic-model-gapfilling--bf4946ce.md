<!-- tension-hash: bf4946cec130b22e -->
# Does Model-Predicted Flux Locate Respiratory Bottlenecks in Aromatic Catabolism?

This page records a disagreement over what the respiratory-chain evidence shows. One reading treats Complex I, which oxidises NADH (reduced nicotinamide adenine dinucleotide, a cellular electron carrier), as an aromatic-specific requirement that the flux balance analysis (FBA) model detects as higher flux but misses as essentiality: 1.76× higher Complex I flux alongside 10/13 operon-subunit growth defects [src: aromatic_catabolism_network]. An operon is a set of genes transcribed together, and FBA is a constraint-based method that predicts feasible flux distributions. The other reading holds that the strongest defects sit on non-aromatic substrates and in a gene the model routes no flux through: ACIAD3522 has ratios of 0.013 on acetate and 1.39 on quinate and glucose [src: discoveries]. The outcome decides whether elevated model flux can prioritise condition-specific essential genes, a central question for [[concepts/metabolic-model-gapfilling]].

## Evidence Sides

**Side A: Complex I is an aromatic-associated bottleneck that the model under-calls.** The aromatic analysis found 1.76× higher Complex I flux but 10/13 operon-subunit growth defects [src: aromatic_catabolism_network]. On this reading, the model registers the increased demand on aromatic substrates but does not predict the essentiality that the mutant data show [src: aromatic_catabolism_network].

**Side B: The strongest defects are not aromatic-specific, and the model misses them entirely.** Fitness defects transferred from orthologs (equivalent genes in other species) were strongest on acetate and succinate rather than exclusively on aromatic substrates [src: discoveries]. ACIAD3522 ratios were 0.013 on acetate and 1.39 on quinate and glucose [src: discoveries]. The synthesis calls this acetate effect, 0.013 on acetate against no defect on quinate (1.39) or glucose (1.39), the largest condition-specific effect of any single gene in the 2,034-gene growth matrix [src: discoveries]. FBA predicts zero flux through ACIAD3522 on all conditions, and the gene's biological role is unknown [src: discoveries].

The data also did not support a cross-species compensation hypothesis invoking NDH-2, a single-subunit alternative NADH dehydrogenase, once annotations were corrected. Complex I aromatic deficits were −0.297 in organisms with validated NDH-2 and −0.156 in those without, with p = 0.52, where p is the probability, assuming no true difference, of observing a difference at least this large [src: discoveries]. This is a null result. It does not show that compensation is absent.

## Possible Reconciliations

- *Hypothesis:* Complex I demand tracks NADH flux in general rather than aromatic substrates specifically. Both sides would then describe one high-NADH-flux requirement seen in different substrate panels.
- *Hypothesis:* Model flux and essentiality are different quantities. A reaction can carry elevated predicted flux without being predicted essential, and a gene predicted to carry zero flux can still be required for growth.
- *Hypothesis:* Respiratory functions are divided by metabolic regime, with Complex I and ACIAD3522 required under different conditions.

## Resolving Work

- **Data:** direct growth assays of Complex I subunit mutants on acetate, succinate, quinate and glucose in the native organism. **Method:** per-condition comparison against wild type. **Question:** are native defects aromatic-specific, or as strong on acetate and succinate as the transferred data suggest?
- **Data:** ACIAD3522 sequence and genomic context. **Method:** homology and domain annotation, then adding a candidate reaction to the model. **Question:** does a mapped reaction reproduce the acetate-specific requirement?
- **Data:** NDH-2 calls validated beyond text matching across fitness-profiled organisms. **Method:** a better-powered comparison of Complex I deficits with and without NDH-2. **Question:** is the p = 0.52 null a matter of statistical power, or a true absence of compensation?
- **Data:** model flux predictions paired with mutant growth across the 2,034-gene growth matrix. **Method:** rank correlation (an association measured on ranked rather than raw values) between predicted flux change and observed defect, per condition. **Question:** does elevated predicted flux forecast condition-specific essentiality at all?
