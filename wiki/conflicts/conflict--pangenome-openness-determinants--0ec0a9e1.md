<!-- tension-hash: 0ec0a9e134ab38f7 -->
# Is Pangenome Openness Driven by Metabolic Variability, Environment and Phylogeny, or Gene Conservation?

Projects in this corpus disagree about what explains pangenome openness, meaning how far a species' gene repertoire keeps expanding as more genomes are sampled. Metabolic pathway variability looks like a reproducible candidate determinant or proxy of openness [src: discoveries]. Direct environmental and phylogenetic effects remain specification-dependent. Only 6.8% of species had sufficient coverage for the AlphaEarth environmental associations [src: discoveries]. A further question is whether conservation explains openness. Conservation is what divides genes into core genes, shared across a species' genomes, and accessory genes, which vary between genomes. The answer decides which mechanisms deserve functional testing. The framing comes from [[concepts/pangenome-openness-determinants]].

## Evidence Sides

**Side A: metabolic variability is a candidate determinant or proxy of openness**

The strongest current interpretation is that metabolic pathway variability is a reproducible candidate determinant or proxy of openness [src: discoveries]. Ecotypes are within-species clusters with distinct metabolic profiles. The association between ecotype count and openness **supports** metabolic diversification as an additional correlate. However, it depends on clustering thresholds and genome-count eligibility, so it cannot establish causality [src: pathway_capability_dependency]. Latent capabilities are complete pathways with no detected fitness importance under tested conditions. A positive association with latent capabilities **further supports** this correlate. It leaves open three possibilities: openness may promote fitness-neutral capabilities, shared ecological context may produce both, or sampling and community interactions may affect both [src: metabolic_capability_dependency].

**Side B: environmental and phylogenetic effects do not clearly predict openness**

Direct environmental and phylogenetic effects remain specification-dependent [src: discoveries]. The AlphaEarth associations rely on embeddings, which are numerical summaries of the environment at each genome's sampling location. They should be treated as coverage-limited, not as population-wide causal estimates, because only 6.8% of species had sufficient coverage [src: discoveries]. Two explanations of the null correlations remain hypotheses that need functional and transfer-specific tests. Neither is an established consequence of the nulls:

* HGT (horizontal gene transfer, the movement of genes between organisms other than by descent) may not track environmental similarity [src: pangenome_openness].
* The core/accessory classification may not capture functional adaptation [src: pangenome_openness].

**Side C: core and accessory genes differ functionally, but conservation alone may not explain openness**

The fitness study **supports** a functional distinction between core and accessory genes. It also **refines** any interpretation that conservation alone explains pangenome openness. Its conservation gradient was statistically robust yet weak, and core genes also showed condition-specific and opposing fitness effects [src: fitness_effects_conservation].

## Possible Reconciliations

* **Hypothesis 1:** The AlphaEarth associations may change once coverage extends beyond the 6.8% of species with sufficient data [src: discoveries].
* **Hypothesis 2:** Shared ecological context, or sampling and community interactions, may affect both metabolic capabilities and openness [src: metabolic_capability_dependency]. That would make metabolic variability a proxy rather than a determinant.
* **Hypothesis 3:** Gene acquisition through HGT may not track environmental similarity [src: pangenome_openness]. This could leave openness unrelated to environmental effects while metabolic correlates persist.

## Resolving Work

* Using the ecotype clustering outputs, rerun the ecotype–openness test across a range of clustering thresholds and genome-count eligibility cutoffs. This would show whether the association survives these specification changes.
* Using environmental metadata for species outside the AlphaEarth-covered subset, re-estimate the environment–openness association with coverage-matched comparisons. This would show whether the AlphaEarth results depend on coverage.
* Apply phylogenetic reconciliation to accessory genes. This method compares gene trees with species trees to infer transfer events. Test whether acquired genes track environmental similarity.
* Using condition-stratified fitness data, test whether the latent-capability–openness association persists after adjusting for ecological context and sampling depth.
* Using core genes with condition-specific or opposing fitness effects, test whether a functional classification predicts openness better than conservation alone.
