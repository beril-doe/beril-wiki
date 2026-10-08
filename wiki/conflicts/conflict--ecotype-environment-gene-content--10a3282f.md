<!-- tension-hash: 10a3282f8dc9cee9 -->
# Does Environment Structure Microbial Functional Gene Content Strongly, or Only Weakly?

This tension, recorded on [[concepts/ecotype-environment-gene-content]], sets two kinds of evidence against each other. Targeted comparisons find strong environmental signals in functional gene content: soil enriches specific plant growth-promoting (PGP) genes [src: pgp_pangenome_ecology; ecotype_env_reanalysis], and soil and freshwater communities separate in metabolic pathway space. [src: nmdc_community_metabolic_ecology; ecotype_env_reanalysis] A broad species-level reanalysis is null and points the opposite way from expectation: environmental species do not show stronger environment–gene-content coupling than human-associated species (median 0.051 versus 0.084). [src: nmdc_community_metabolic_ecology; ecotype_env_reanalysis] The answer decides whether "environment shapes gene content" should be stated generally or limited to particular traits, scales and habitat contrasts.

## Evidence Sides

**Environment strongly structures functional gene content**

- Soil strongly enriched three PGP genes: acdS (ACC deaminase, where ACC is 1-aminocyclopropane-1-carboxylate, linked to ethylene reduction), pqqC (pyrroloquinoline quinone biosynthesis, linked to phosphate solubilization) and hcnC. Soil depleted nifH, which is linked to nitrogen fixation. [src: pgp_pangenome_ecology; ecotype_env_reanalysis]
- The NMDC (National Microbiome Data Collaborative) community analysis found that soil and freshwater samples separate on pathway profiles. On PC1, the first axis of a principal component analysis (PCA), the soil median is +3.86 and the freshwater median is −6.28. [src: nmdc_community_metabolic_ecology; ecotype_env_reanalysis]

**Environmental grouping does not predict stronger environment–gene-content coupling**

- The broad environmental comparison was null. [src: pgp_pangenome_ecology; ecotype_env_reanalysis]
- In the ecotype reanalysis, Environmental species had a median of 0.051 and Human-associated species a median of 0.084. Each median summarizes the per-species partial correlations (associations measured while controlling for other variables) across the species in that group. Species classed as environmental therefore did not show the stronger coupling the original hypothesis predicted. [src: nmdc_community_metabolic_ecology; ecotype_env_reanalysis]

## Possible Reconciliations

- *Hypothesis (unit of analysis):* The two sides measure different things. The strong signals come from habitat contrasts at the level of genes or communities. The null comes from comparing summaries of per-species partial correlations between species groups. Both could hold at once: environment could sort which genes and taxa are present in a habitat without making environment–gene-content coupling stronger in environmental species.
- *Hypothesis (trait specificity):* Environmental structuring may be concentrated in a few ecologically targeted genes, such as acdS, pqqC, hcnC and nifH. A genome-wide gene-content signal would dilute those genes.
- *Hypothesis (grouping coarseness):* The labels "Environmental" and "Human-associated" may be too broad to pick up the habitat axis, such as soil versus freshwater, along which the strong separations appear.

None of these is established. Each needs the analyses below.

## Resolving Work

- **Per-gene environmental partial correlations:** Re-run the ecotype reanalysis, scoring partial correlations (associations controlling for other variables) for acdS, pqqC, hcnC and nifH only. Question: does the null persist when only these soil-enriched or soil-depleted genes are scored?
- **Finer habitat labels in the species-level test:** Replace the Environmental/Human-associated split with soil, freshwater and other habitat categories, then repeat the group comparison. Question: does a soil-versus-freshwater contrast produce a signal that the coarse grouping hides?
- **Taxonomic decomposition of the NMDC pathway separation:** Partition the soil-versus-freshwater difference on PC1 into a between-taxa component (which taxa are present) and a within-taxon component (how gene content differs inside a taxon). Question: is the separation driven by taxonomic turnover or by gene-content shifts within the same taxa?
- **Matched-scale comparison:** Compute both PGP enrichment and pathway PCA on the same species set used in the ecotype reanalysis. Question: does the disagreement disappear once all three analyses share one denominator?
