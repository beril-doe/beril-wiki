<!-- tension-hash: e8ac0fe110ef7248 -->
# Genome-wide mobile-element association versus local physical linkage: which counts as evidence that mobile elements disseminate accessory genes?

Both projects that touch mobile genetic elements in [[concepts/environmental-resistome]] report strong signal, but the signal sits at different scales, and the two scales disagree about what has been shown. One project finds that genome-wide *density* of prophages (bacteriophage genomes integrated into a host chromosome) tracks antimicrobial-resistance (AMR) gene breadth strongly, while *local* co-location of the same elements is modest and inconsistent. The other project accumulates large co-occurrence and event counts for type IV secretion systems (T4SS, conjugative DNA-transfer machinery) and carbohydrate-active enzyme (CAZy) genes, yet returns a null when it looks for the CAZy cargo on plasmids. The disagreement matters because it decides whether "associated with mobile elements" licenses the claim "moved by mobile elements."

## Evidence Sides

**Density carries the association; proximity is modest and heterogeneous (prophage side).** Prophage density and local proximity provide non-equivalent evidence: density was strongly associated with AMR breadth (rho=0.572, a Spearman rank correlation; partial rho=0.464 after controlling for genome count), whereas local proximity was modest and heterogeneous, with median species-level OR=0.85 (odds ratio). [src: prophage_amr_comobilization] On this reading the mobile-element signal is read as a whole-genome propensity rather than as a demonstration that any particular gene rode a particular element.

**Accumulated co-occurrence and event counts, with a plasmid null (T4SS–CAZy side).** T4SS–CAZy evidence supports dissemination as a hypothesis rather than demonstrated transfer: it reports 92 elevated co-occurrences, 77 GT2 HGT (horizontal gene transfer) events, 32 normalized high-confidence cross-phylum events, and 10× higher MGE (mobile genetic element) density in T4SS-positive genomes, but no CAZy genes on plasmids by ICEfinder (a tool that annotates integrative and conjugative elements) and only 12 IMEs (integrative mobilizable elements) among the top 100 accumulators. [src: t4ss_cazy_environmental_hgt]

## Possible Reconciliations

- *Hypothesis: scale mismatch.* Genome-wide density and local adjacency measure different things — element-permissive genomes versus completed cargo capture — so a strong rho=0.572 and a median OR=0.85 can both hold without contradiction. [src: prophage_amr_comobilization]
- *Hypothesis: chromosomal/integrative route.* Absence of CAZy genes on plasmids with elevated MGE density in T4SS-positive genomes would be expected if transfer proceeds chromosomally rather than by plasmid carriage. [src: t4ss_cazy_environmental_hgt]
- *Hypothesis: erosion after transfer.* Cargo may be inserted near an element and subsequently relocated or the element degraded, leaving genome-level association intact while local linkage decays.

## Resolving Work

- Re-run the proximity test across the same species set at several distance thresholds and report whether the median species-level OR crosses 1 anywhere, rather than at one threshold. [src: prophage_amr_comobilization]
- Assemble long-read or closed genomes for the top 100 accumulators and ask whether CAZy cargo sits inside identifiable integrative elements that short-read ICEfinder calls miss. [src: t4ss_cazy_environmental_hgt]
- Apply the prophage density/proximity pair of statistics to CAZy–T4SS data, and the co-occurrence/event-counting pipeline to AMR–prophage data, to test whether the discrepancy is biological or methodological.
- Test whether the 32 normalized high-confidence cross-phylum events fall in genomes whose T4SS loci are within the co-occurrence window, linking those events to physical linkage in the same genome. [src: t4ss_cazy_environmental_hgt]
- Control both analyses for genome count and assembly completeness, reporting raw and partial coefficients side by side so the two scales are compared on the same covariates. [src: prophage_amr_comobilization]
