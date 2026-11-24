---
type: "Concept"
description: "Whether classical microbiology phenotypes (Gram stain, urease, catalase, oxygen tolerance) predict metal tolerance independently of taxonomy, including Simpson's-paradox reversals within taxonomic classes; stops at the BacDive/Metal Fitness Atlas comparison."
sources: ["summaries/bacdive_phenotype_metal_tolerance__REPORT.md", "summaries/discoveries.md"]
---
# Phylogenetic confounding of phenotype–metal tolerance associations

Classical microbiology phenotypes (Gram stain, urease, catalase, oxygen-related traits) show real univariate associations with metal tolerance in BacDive. The evidence from one report, `bacdive_phenotype_metal_tolerance`, and the central discoveries digest is that taxonomy absorbs these associations, and some reverse sign within classes (Simpson's paradox). The evidence is observational and comes from one dataset ([[entities/bacdive]]). It rests on class stratification and model comparison, not on a formal phylogenetic comparative test. [src: bacdive_phenotype_metal_tolerance, discoveries]

## Literature Context

None of the retrieved papers tests whether classical phenotypes such as Gram stain, urease or catalase predict metal tolerance after taxonomy is controlled. The candidates are genome-centred studies of individual taxa or isolates. They are indirect context only, and they neither confirm nor contradict the BacDive result.

Several papers show that metal-tolerance determinants are often carried by mobile or accessory elements. In Teesta River *Pseudomonas* and *Serratia* isolates, phylogenetic incongruency and GC-composition analysis of PIB-type metal-tolerance genes suggested that some isolates had acquired resistance by horizontal gene transfer [PMID 37227565](https://pubmed.ncbi.nlm.nih.gov/37227565/). The study was of selected isolates and gave no estimate of how much taxonomy explains. A comparative analysis of 512 plasmids from 282 strains of 51 Lactobacillaceae species found that metal ion transport and stress-tolerance genes were significantly enriched on plasmids of nomadic and free-living species, compared with vertebrate-adapted species [PMID 33166245](https://pubmed.ncbi.nlm.nih.gov/33166245/). Metal tolerance genes were also predicted in all 90 genomes of F4- and F18-positive enterotoxigenic *E. coli* from pigs, where copper showed the highest diversity [PMID 32948526](https://pubmed.ncbi.nlm.nih.gov/32948526/). Genomic work on *Blastococcus*, a stone-dwelling Actinomycete genus, reported heavy metal resistance. It also found no correlation between ecological or plant-growth-promoting traits and isolation source, and the authors say the findings still need wet-lab validation [PMID 39833680](https://pubmed.ncbi.nlm.nih.gov/39833680/). A *Klebsiella pneumoniae* study reported that resistance-conferring TetA variants reduced tolerance to cadmium and H2O2, a fitness cost [PMID 41467803](https://pubmed.ncbi.nlm.nih.gov/41467803/).

These papers fit a hypothesis that metal tolerance depends on a lineage's gene repertoire and its accessory gene flow, not on a single phenotype. That reading is compatible with the corpus finding that taxonomy alone explains 35.4% of metal-tolerance variance while phenotype alone explains 16.3%. It is also compatible with the genome-versus-phenotype framing in [[concepts/genome-encoded-metal-resistance-repertoire-versus-phenotype-as-predictor-of-metal-tolerance]]. The accessory and plasmid-borne evidence points to a possible caveat. If metal genes move between lineages, class-level taxonomy may not capture all of the genetic signal. The corpus does not test this, because it uses class stratification and not phylogenetic comparative methods.

The corpus claims are otherwise not addressed by these candidates. The Simpson's-paradox reversals for urease, which is driven by Actinomycetes (d = -0.59), and for catalase within classes, the Gram-stain confounding with the Actinomycete versus Proteobacteria contrast, and the lack of added predictive value from phenotype (delta R² = -0.009) have no direct counterpart in this set, so they stay novel relative to it. Settling them still needs the phylogenetic generalized least squares or phylogeny-blocked analyses listed under Open Directions.

## Univariate associations

Seven phenotype features pass false discovery rate (FDR) correction at q < 0.05. [src: bacdive_phenotype_metal_tolerance] Gram-negative species score higher than Gram-positive species, the largest effect tested (Cohen's d = -0.61, p < 1e-60, n = 3,272 species). [src: bacdive_phenotype_metal_tolerance]

| Feature | Effect | n | p | FDR q | Claim |
|---|---|---|---|---|---|
| Gram stain (+) | d = -0.610 | 3,272 | 4.0e-61 | 4.0e-60 | [src: bacdive_phenotype_metal_tolerance] |
| Oxidase (+) | d = +0.530 | 1,799 | 2.7e-25 | 1.3e-24 | [src: bacdive_phenotype_metal_tolerance] |
| Motility | d = +0.345 | 3,138 | 2.2e-23 | 7.2e-23 | [src: bacdive_phenotype_metal_tolerance] |
| Urease (+) | d = -0.175 | 3,035 | 3.7e-06 | 9.1e-06 | [src: bacdive_phenotype_metal_tolerance] |
| Enzyme breadth | rho = -0.058 | 3,746 | 4.1e-04 | 8.2e-04 | [src: bacdive_phenotype_metal_tolerance] |
| Nitrate reduction | d = +0.100 | 3,088 | 4.4e-03 | 7.4e-03 | [src: bacdive_phenotype_metal_tolerance] |
| Catalase (+) | d = +0.104 | 2,930 | 2.8e-02 | 4.1e-02 | [src: bacdive_phenotype_metal_tolerance] |

The Gram-negative outer membrane is described as a permeability barrier restricting metal cation uptake. The report calls the association mechanistically plausible but statistically confounded with phylogeny. [src: bacdive_phenotype_metal_tolerance]

## Taxonomy explains the signal

Taxonomy alone (phylum/class/order) explains 35.4% of metal-tolerance variance. Phenotype alone explains 16.3%. Combining them gives R² = 34.5%, slightly worse than taxonomy alone. [src: bacdive_phenotype_metal_tolerance] The three models:

- Phenotype only: R² = 0.163, RMSE (root mean square error) = 0.043, n = 3,994, 13 features. [src: bacdive_phenotype_metal_tolerance]
- Taxonomy only: R² = 0.354, RMSE = 0.038, n = 3,994, 3 features. [src: bacdive_phenotype_metal_tolerance]
- Taxonomy plus phenotype: R² = 0.345, RMSE = 0.038, n = 3,994, 16 features. [src: bacdive_phenotype_metal_tolerance]

Phenotype features contribute minimally to individual predictions once taxonomy is included. The report reads classical phenotypes as phylogenetic proxies, not independent predictors. [src: bacdive_phenotype_metal_tolerance] Adding them lowers predictive power slightly (delta R² = -0.009). [src: bacdive_phenotype_metal_tolerance] The discoveries digest repeats this conclusion. It states that the signal is real but entirely phylogenetically confounded. [src: discoveries] The report concludes that phenotypes capture real differences that phylogenetic structure fully explains. [src: bacdive_phenotype_metal_tolerance] The Gram-negative advantage is called real but indistinguishable from "being a Proteobacterium" in a predictive model. [src: bacdive_phenotype_metal_tolerance] For related work see [[concepts/genome-encoded-metal-resistance-repertoire-versus-phenotype-as-predictor-of-metal-tolerance]].

## Gram stain: a between-lineage signal

The Gram association cannot be tested within taxonomic classes. It is almost entirely a contrast between Gram-positive Actinomycetes and Gram-negative Proteobacteria. [src: bacdive_phenotype_metal_tolerance] The matched data contain no Gram-positive Proteobacteria and no Gram-negative Actinomycetes. [src: bacdive_phenotype_metal_tolerance] The report treats hypothesis H1a (Gram-negative species are more metal tolerant) as supported univariately but phylogenetically confounded. [src: bacdive_phenotype_metal_tolerance]

## Urease: a Simpson's-paradox reversal

Urease-positive species have lower metal tolerance (d = -0.18, p < 1e-5). This is opposite to the prediction that nickel-import machinery would confer nickel tolerance. [src: bacdive_phenotype_metal_tolerance] The effect is driven by Actinomycetes (d = -0.59, p < 1e-16), where urease-positive species form a distinct low-metal-score subgroup. [src: bacdive_phenotype_metal_tolerance] Within Gammaproteobacteria (d = +0.08, ns) and Bacilli (d = +0.06, ns) the effect disappears. [src: bacdive_phenotype_metal_tolerance] Within other classes the report finds the urease effect is zero. [src: bacdive_phenotype_metal_tolerance] The report therefore calls H1e (urease predicts nickel tolerance) reversed and driven by Actinomycetes. [src: bacdive_phenotype_metal_tolerance] It explains that urease positivity correlates with Actinomycetes and other lineages that have fewer metal resistance genes. [src: bacdive_phenotype_metal_tolerance, discoveries] The pangenome-scale urease effect is near zero in Gammaproteobacteria. [src: bacdive_phenotype_metal_tolerance] See [[entities/urease]] and [[entities/actinomycetota]].

## Catalase: sign reversal within classes

Overall, catalase-positive species score slightly higher (d = +0.10). This marginally supports H1d (q = 0.04). [src: bacdive_phenotype_metal_tolerance] Within each major class the sign is opposite. Catalase-negative species score higher in Actinomycetes (d = -0.62, p < 1e-5), Gammaproteobacteria (d = -0.49, p = 0.004) and Betaproteobacteria (d = -0.51, p = 0.006). [src: bacdive_phenotype_metal_tolerance] The report interprets the overall effect as a between-class composition artifact, the same Simpson's paradox pattern as urease. Catalase-positive classes (Proteobacteria) happen to have higher metal scores. [src: bacdive_phenotype_metal_tolerance] See also [[entities/pseudomonadota]].

## Literature context

The report cites Goberna & Verdú (2016), a meta-analysis showing that bacterial trait–environment associations routinely reflect shared ancestry. [src: bacdive_phenotype_metal_tolerance] It also cites Van Assche & Álvarez (2017), who found phylogenetic signal up to λ = 0.98 for chemical sensitivity traits in *Acinetobacter*. [src: bacdive_phenotype_metal_tolerance] The report proposes phylogenetic generalized least squares (PGLS) or phylogenetic principal component analysis (PCA) to remove phylogenetic signal before testing phenotype–metal associations. [src: bacdive_phenotype_metal_tolerance]

## Open Directions

- Run PGLS or phylogenetic PCA on the BacDive phenotype–metal data to replace class stratification with a continuous phylogenetic control. See [[entities/phylogenetic-generalized-least-squares]].
- Profile per-metal fitness of urease-positive versus urease-negative bacteria within one class, ideally Gammaproteobacteria, where the pooled urease effect is near zero. This would test nickel-specific tolerance.
- Compare the BacDive taxonomy result with phylogeny-blocked cross-validation ([[entities/xgboost-with-phylogenetic-blocked-cross-validation]]). This would show whether phenotypes add anything for unseen lineages.
- Test Gram stain on data that include Gram-positive Proteobacteria or other cross-lineage contrasts, if such data exist. The current data lack them.
