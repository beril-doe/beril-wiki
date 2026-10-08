<!-- tension-hash: f884063a33eb8b44 -->
# Whole-genome gene content versus prophage modules: where does environmental structure appear?

Comparisons across projects disagree about where environment leaves a mark on bacterial gene content. Whole-genome comparisons found weak or usually nonsignificant relationships between environment and gene content. In contrast, prophage-module composition showed an environmental effect after genome-size and family-level comparisons. A prophage is a phage genome integrated into a bacterial chromosome, and a prophage module is a functional group of its genes, such as packaging or lysis genes. [src: ecotype_analysis, ecotype_env_reanalysis, prophage_ecology] This is a difference of scope rather than a direct contradiction. It matters because [[concepts/ecotype-clustering-validity]] depends on whether environment-linked gene-content groups are real biological units. These groups are called "ecotypes": strains assumed to be adapted to distinct habitats. A signal confined to one module system could be read either as concentrated adaptation or as an analytical artifact.

## Evidence Sides

**Whole-genome comparisons: weak or nonsignificant environmental signal**

Comparisons of environment and gene content at whole-genome scale found weak or usually nonsignificant relationships. [src: ecotype_analysis, ecotype_env_reanalysis, prophage_ecology] This describes the observed associations. It is a null-leaning result, not evidence of absence in every lineage.

**Prophage-module composition: an environmental effect beyond controls**

Prophage-module composition showed an environmental effect after genome-size and family-level comparisons. [src: ecotype_analysis, ecotype_env_reanalysis, prophage_ecology] The same evidence cannot say whether this difference reflects:

- genuine concentration of ecological adaptation in prophage modules,
- annotation or sampling differences, or
- residual confounding.

It therefore does not justify treating prophage-module structure as validated ecotype structure. [src: prophage_ecology]

## Possible Reconciliations

- **Hypothesis: concentrated adaptation.** Environmental adaptation may be concentrated in a small, variable module system such as prophage modules. That signal would then be diluted when the whole genome is compared, so both results could hold at their own scale. The prophage project leaves this undetermined. [src: prophage_ecology]
- **Hypothesis: annotation or sampling artifact.** The prophage effect may arise from how prophage genes are annotated, or from which genomes are sampled. If so, it would not reflect ecology. [src: prophage_ecology]
- **Hypothesis: residual confounding.** Genome-size and family-level comparisons may not fully remove phylogenetic effects or genome-architecture effects. Phylogenetic effects are those associated with evolutionary relatedness. Genome-architecture effects are those associated with genome size and organization. The remaining environmental signal in prophage modules could therefore be confounded. [src: prophage_ecology]

## Resolving Work

- **Same genomes, both feature sets.** Use the prophage-module calls and the whole-genome gene-content matrices for the same set of species. Run identical partial-correlation tests (correlation between environment and gene content, holding phylogenetic distance fixed) on each feature set. Question: does the scope difference persist when genomes, environment labels and statistics are held fixed?
- **Matched random modules.** Draw random gene-module sets matched to prophage modules in size and prevalence. Test them for environmental effects with the same genome-size and family-level controls. Question: is the prophage signal larger than that of comparably variable non-prophage modules?
- **Alternative annotation.** Re-identify prophage regions with a second annotation approach, independent of the original gene-cluster annotations. Re-run the environmental comparison. Question: does the effect survive a change in annotation method?
- **Finer phylogenetic control.** Replace family-level comparisons with within-genus or within-species comparisons, or with phylogenetically explicit models. Question: does the prophage environmental effect remain once residual phylogenetic confounding is reduced?
- **Ecotype test on prophage profiles.** Cluster genomes on prophage-module profiles and assess cluster stability and separation. Question: does the environmental effect form discrete, stable groups that qualify as ecotypes, or only a continuous gradient?
