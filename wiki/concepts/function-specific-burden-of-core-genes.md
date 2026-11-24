---
type: "Concept"
description: "Covers which functional categories show excess fitness burden among core genes versus accessory genes, and why costly genes may still be retained; stops at overall conservation gradients."
sources: ["summaries/amr_pangenome_atlas__REPORT.md", "summaries/conservation_fitness_synthesis__REPORT.md", "summaries/core_gene_tradeoffs__REPORT.md", "summaries/costly_dispensable_genes__REPORT.md", "summaries/discoveries.md"]
---
# Function-specific burden of core genes

The category numbers come from the Fitness Browser analysis in core_gene_tradeoffs, and the discoveries digest repeats them. [src: core_gene_tradeoffs, discoveries] See [[summaries/core_gene_tradeoffs__REPORT]] and [[summaries/conservation_fitness_synthesis__REPORT]].

## Overall pattern

Core genes are more likely than accessory genes to be burdens: 24.4% show positive fitness when deleted, against 19.9% for accessory genes. [src: conservation_fitness_synthesis] Accessory genes are therefore less costly than core genes, contrary to the streamlining hypothesis. [src: conservation_fitness_synthesis] The core-burden paradox is not a uniform property of the core genome. It reflects the trade-off architecture of specific functional systems. [src: discoveries]

## Categories with core-burden excess

Three categories drive the effect. The excess is reported in percentage points (pp).

| Category | Core-burden excess | Sources |
|---|---|---|
| RNA (ribonucleic acid) metabolism | +12.9pp | [src: conservation_fitness_synthesis, core_gene_tradeoffs, discoveries] |
| Motility and chemotaxis | +7.8pp | [src: conservation_fitness_synthesis, core_gene_tradeoffs, discoveries] |
| Protein metabolism | +6.2pp | [src: conservation_fitness_synthesis, core_gene_tradeoffs, discoveries] |

The costly_dispensable_genes report adds a related result. Costly+conserved genes are enriched in Protein Metabolism, Respiration and Motility. [src: costly_dispensable_genes] This **supports** the same picture from a different angle. See [[concepts/costly-but-conserved-genes-laboratory-burden-versus-conservation]].

## Cell wall reverses the pattern

Non-core cell wall genes are more burdensome than core cell wall genes. [src: conservation_fitness_synthesis] The reported difference is -14.1pp. [src: core_gene_tradeoffs, discoveries] This **limits** any reading of the burden excess as general to all core functions. [src: discoveries]

## Why costly genes may still be retained

The reports explain that core genes are more burdensome in the lab because they encode functions that are energetically expensive but essential in natural environments. Their examples are motility, ribosomal components and RNA metabolism. [src: core_gene_tradeoffs]

- Flagella are energetically expensive but essential for chemotaxis in natural environments. [src: conservation_fitness_synthesis] Motility genes exemplify the paradox: the machinery is conserved for chemotaxis in nature despite its cost under lab conditions. [src: core_gene_tradeoffs]
- Ribosomal components are costly but required for rapid growth responses. [src: conservation_fitness_synthesis, core_gene_tradeoffs]
- Costly+conserved functions are interpreted as maintained by purifying selection for natural environments that lab experiments do not capture. [src: costly_dispensable_genes] Their lab-measured burden is interpreted as offset by natural selection in the environment. [src: costly_dispensable_genes]

## Antimicrobial resistance as an exception

Intrinsic AMR (antimicrobial resistance) genes are fitness-neutral. The amr_pangenome_atlas report reads this as an exception to the overall core burden: core AMR genes appear to impose even less cost than non-AMR core genes. [src: amr_pangenome_atlas] See [[concepts/fitness-cost-of-antimicrobial-resistance-genes]] and [[summaries/amr_pangenome_atlas__REPORT]].

## Open Directions

- Test the natural-environment hypothesis directly. Compare burden in the motility, RNA and protein categories across lab conditions that approximate natural settings. This would show whether the offsetting benefit exists.
- Explain the cell wall reversal. Find which non-core cell wall genes carry the burden and whether they are mobile or strain-specific.
- Extend the category analysis to more functional categories and organisms. Check whether the three enriched categories hold beyond the Fitness Browser set.
- Compare burden in core AMR genes with the three enriched categories in one model. This would show whether AMR neutrality is a category effect.
