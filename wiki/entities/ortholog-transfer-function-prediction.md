---
type: "Method"
description: "Function prediction by transferring annotations or fitness-module context between orthologs (bidirectional best hits); stops at the ortholog inference itself."
sources: ["summaries/essential_genome__REPORT.md", "summaries/fitness_modules__REPORT.md", "summaries/functional_dark_matter__REPORT.md"]
aliases: ["BBH ortholog transfer", "Ortholog transfer", "module transfer", "ortholog-module transfer"]
---
# Ortholog transfer function prediction

This page covers ortholog transfer function prediction, also called BBH ortholog transfer or module transfer. In the held-out KEGG benchmark, direct ortholog transfer scored far better than module- or cofitness-based methods. [src: fitness_modules] Module transfer also produced many predictions for essential genes, but those are indirect and untested. [src: essential_genome] See also [[concepts/function-prediction-for-uncharacterized-genes-by-guilt-by-association-and-ortholog-transfer]].

## Benchmark performance

Ortholog transfer was the strongest of four methods in the held-out KEGG KO (KEGG ortholog) test. That test withheld 20% of KEGG-annotated genes and asked four methods to predict KO groups. [src: fitness_modules] Ortholog transfer reached 95.8% strict precision, 91.2% coverage and F1 of 0.934. [src: fitness_modules] The domain-based method reached 29.1% strict precision, 66.6% coverage and F1 of 0.401. [src: fitness_modules] Module-ICA (independent component analysis) had <1% strict precision and 23.3% coverage. [src: fitness_modules] Cofitness voting had <1% strict precision and 73.0% coverage. [src: fitness_modules] No F1 was reported for the last two.

The report attributes the near-zero strict precision of Module-ICA and cofitness to KEGG KO groups being gene-level assignments, averaging ~1.2 genes per unique KO. [src: fitness_modules] It concludes that Module-ICA should not be used to predict specific molecular functions, where ortholog transfer is far superior. [src: fitness_modules] The cross-organism module alignment used 1.15M BBH (bidirectional best hit) pairs across 32 organisms, giving 13,402 ortholog groups. [src: fitness_modules] See [[entities/independent-component-analysis-fitness-modules]] and [[entities/kegg]].

## Module transfer for essential genes

The essential-genome report uses ortholog-module transfer to give functional context to essential genes. Essential genes lack fitness data, so ICA cannot see them. Their non-essential orthologs in other organisms do have fitness data and can sit in modules. The method transfers that module context across organisms. [src: essential_genome] See [[concepts/essential-genes-as-a-blind-spot-of-transposon-fitness-screens]].

Of the hypothetical essential genes, 3,912 have orthologs and are predictable, and 4,385 are orphans that this method cannot predict. [src: essential_genome] The method generated 1,382 function predictions, covering 35.3% of predictable targets. [src: essential_genome] All of these predictions are family-backed. [src: essential_genome]

## Caveats

Module-transfer predictions are indirect. They come from non-essential orthologs in other organisms, and the essential gene's function may have diverged. [src: essential_genome] The report proposes testing the 1,382 predictions by CRISPRi (CRISPR interference) knockdown under conditions the module context predicts. [src: essential_genome]

## Independent agreement

In the functional dark matter report, the top 100 dark gene candidates from its NB05 analysis were cross-checked against Paramvir Dehal's earlier module-based predictions. Of the 100, 85 already had predictions, and all agreed with the report's independent inference. The report calls this strong orthogonal validation. [src: functional_dark_matter]

## Open Directions

- Run the proposed CRISPRi knockdowns on a sample of the 1,382 module-transfer predictions. This would show whether diverged function undermines them.
- Benchmark module transfer against held-out annotations using non-strict KO matching. This would separate method failure from the gene-level KO granularity problem.
- Look for other evidence, such as synteny or domains, that could cover the 4,385 orphan hypothetical essential genes.
