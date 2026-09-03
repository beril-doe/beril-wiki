<!-- tension-hash: 7e3317ca95842077 -->
# Does Functional Association Survive Taxonomic and Coverage-Resolution Choices?

The disagreement concerns whether contamination-associated functional signals are robust ecological associations or instead depend on coverage adjustment, taxonomic resolution, model specification, and compositional structure. One set of analyses finds coverage-sensitive or finer-resolution evidence, while stricter genus-level and confirmatory analyses are null or attenuated. The distinction matters because functional differentiation may be real without implying that a particular contamination-associated estimate is stable across analytical choices.

## Evidence Sides

### **Coverage-sensitive and finer-resolution analyses detect functional structure**

The relaxed coverage-adjusted model yielded FDR q = 0.0462, whereas the strict coverage-adjusted model yielded FDR q = 0.130, and both confirmatory genus-level modes were null after predeclared testing. [src: enigma_contamination_functional_potential] The functional-dark-matter report found that 29 of 47 testable lab–field clusters were concordant (61.7%), with Fisher’s combined probability across 47 individual tests giving p = 0.031. [src: functional_dark_matter] NMDC confirmed all 4 testable pre-registered abiotic predictions. [src: functional_dark_matter] Within-species ecotype analysis detected functional differentiation, although it lacked within-species phylogenetic controls. [src: ecotype_functional_differentiation] The COG comparison also found consistent core-versus-novel functional partitioning across 32 species. [src: cog_analysis]

### **Strict, confirmatory, and composition-aware analyses weaken the association**

The strict coverage-adjusted model yielded FDR q = 0.130, and both confirmatory genus-level modes were null after predeclared testing. [src: enigma_contamination_functional_potential] For the 29 of 47 testable lab–field clusters that were concordant (61.7%), the one-sided binomial test gave p = 0.072. [src: functional_dark_matter] Although 441 of 449 exploratory trait tests reached FDR < 0.05, the report cautions that this was largely because of compositional coupling. [src: functional_dark_matter] In plant-associated communities, compartment effects explained only 0.060 of location-only variance, and the earlier large effect was reduced to R² = 0.072 after removal of genome-rich species. [src: plant_microbiome_ecotypes] The same report found that categorical assignments misclassified all four neutral controls in a curated 18-organism panel. [src: plant_microbiome_ecotypes]

## Possible Reconciliations

- **Hypothesis — coverage and retained-abundance effects:** The relaxed and strict ENIGMA models may estimate different signals because coverage adjustment changes which abundance information is retained. [src: enigma_contamination_functional_potential]
- **Hypothesis — taxonomic and bridge ambiguity:** Taxonomic aggregation or ambiguity in bridging reads and functions may erase a real finer-scale association at genus resolution. [src: enigma_contamination_functional_potential]
- **Hypothesis — compositional and genome-size artifacts:** Broad exploratory associations may be inflated by compositional coupling or genome-rich taxa, while finer-resolution signals may still contain genuine structure. [src: functional_dark_matter] [src: plant_microbiome_ecotypes]
- **Hypothesis — different estimands:** COG core-versus-novel partitioning and site-level contamination association test different signals, so their differing results need not conflict. [src: cog_analysis] [src: enigma_contamination_functional_potential]

## Resolving Work

- Reanalyze the ENIGMA data under matched relaxed and strict coverage models, quantifying retained abundance, bridge ambiguity, covariate sensitivity, and genus-level aggregation; ask which component changes FDR q = 0.0462 to FDR q = 0.130.
- Replicate the 29 of 47 lab–field clusters in independent samples using preregistered directional tests and Fisher’s combination; ask whether p = 0.072 or p = 0.031 better predicts held-out data.
- Add within-species phylogenetic controls to the ecotype analysis; ask whether functional differentiation remains after separating ecological effects from shared ancestry.
- Refit plant-association models with genome-size and compositional controls, including neutral controls; ask whether the compartment variance of 0.060 and R² = 0.072 persist.
