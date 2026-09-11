<!-- tension-hash: 538e5b1b3fdfe665 -->
# Genome-Wide Environmental Effects versus Locus-Specific Ecological Adaptation

The disagreement concerns whether ecological adaptation is expressed broadly across gene content or primarily through particular loci and functional categories. One analysis finds that environment can dominate gene-content signals in many species, while significant environmental effects are detected in relatively few species. Other evidence supports functional differentiation but does not establish whether it is environmentally assigned. This matters because the competing interpretations imply different mechanisms of adaptation and require different analyses to resolve. See [[concepts/genome-wide-versus-locus-specific-ecological-adaptation]].

## Evidence Sides

**Side 1: Environment can dominate genome-wide gene-content variation.**  
The dataset indicates that environment dominated the gene-content signal in 39.5% of species. [src: ecotype_analysis] This supports the possibility that environmental variables are important drivers of broad gene-content differences, although the source does not establish whether “dominance” corresponds to statistically significant effects. [src: ecotype_analysis]

**Side 2: Ecological adaptation is primarily locus-specific.**  
Significant positive environmental effects were detected in only 12 species (7.0%), and significant negative environmental effects were detected in 4 species (2.3%). [src: ecotype_analysis] The relatively small number of significant effects is consistent with a weak or localized genome-wide environmental signal. However, the absence of a strong genome-wide signal may also result from incomplete AlphaEarth coverage, imprecise metadata, or environmental embeddings that do not capture biologically relevant variation. [src: ecotype_analysis]

The ecotype study reports functional differentiation without environmental assignment or phylogenetic control. [src: ecotype_functional_differentiation] It therefore supports the locus-specific hypothesis while leaving the ecological interpretation unresolved. [src: ecotype_functional_differentiation] The null relationship between pangenome openness and environment or phylogeny effects also qualifies a genome-wide interpretation: openness did not predict either effect, although the test did not directly compare individual loci or functional categories. [src: pangenome_openness] This does not contradict functional differentiation, but it leaves unresolved whether openness metrics conceal category-specific ecological associations. [src: pangenome_openness, ecotype_functional_differentiation]

The original and reanalysis correlation magnitudes are not a directly replicated effect. The reanalysis reports a median of 0.081 across 183 species versus 0.003 in the original analysis, while the original page reports 0.0025 across its 172-species analysis. [src: ecotype_env_reanalysis, ecotype_analysis] The reanalysis attributes the discrepancy to different genome sets and downsampling procedures and preserves only the within-method group comparison. [src: ecotype_env_reanalysis]

## Possible Reconciliations

- **Hypothesis—effect size versus significance:** Environment may dominate comparative effect sizes without producing significant effects in most species because the metrics answer different questions.
- **Hypothesis—different biological scales:** Broad gene-content differences and localized functional adaptation may coexist if ecological selection affects a limited subset of loci.
- **Hypothesis—measurement limitations:** Coverage, metadata precision, or environmental embeddings may weaken genome-wide associations while leaving locus-specific differentiation detectable.
- **Hypothesis—analysis composition:** The correlation discrepancy may reflect different genome sets and downsampling rather than incompatible biological conclusions. [src: ecotype_env_reanalysis]

## Resolving Work

- Reanalyze the same species, genomes, environmental variables, and statistical thresholds to test whether environmental dominance and significance identify the same species.
- Compare genome-wide, locus-level, and functional-category associations with a hierarchical model to test whether environmental signal is concentrated in particular categories.
- Add environmental assignment and phylogenetic control to the functional-differentiation analysis to test whether differentiation remains ecologically structured.
- Quantify AlphaEarth coverage and metadata uncertainty, then repeat the analysis with alternative environmental embeddings to test for measurement-driven attenuation.
- Recalculate both correlation estimates on matched genome sets without differential downsampling to test whether the discrepancy persists.
