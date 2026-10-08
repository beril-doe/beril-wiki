<!-- tension-hash: 68690ec7a11f5d94 -->
# Does Flux Balance Analysis Agree With Experimental Essentiality in *Acinetobacter baylyi* ADP1?

Two projects in the corpus compare *Acinetobacter baylyi* ADP1 metabolic-model predictions against experimental gene-essentiality data, and their readings pull in different directions. One reports majority agreement between model predictions and transposon-based essentiality calls. [src: acinetobacter_adp1_explorer] The other reports only moderate agreement with knockouts, and no link between model class and growth defects among genes that transposon data call dispensable. [src: adp1_triple_essentiality] The disagreement matters for [[concepts/metabolic-model-gapfilling]] because it affects how far model essentiality predictions can validate a gapfilled model, and which experimental endpoint should be the benchmark.

## Evidence Sides

**Side A: FBA and TnSeq calls largely concordant.** Flux balance analysis (FBA) is a constraint-based method that predicts feasible metabolic flux distributions and, from them, which genes a simulated cell needs. TnSeq (transposon-insertion sequencing) infers essentiality from where transposon insertions can be recovered across the genome. Comparing the two for 866 genes gave 73.8% concordance. [src: acinetobacter_adp1_explorer] The denominator is the set of genes that have both an FBA flux prediction and a TnSeq essentiality call, and the endpoint is an essentiality call. [src: acinetobacter_adp1_explorer]

**Side B: FBA agreement with knockouts is moderate, and FBA class does not track growth defects.** FBA shows moderate concordance with experimental knockouts, meaning complete-gene deletion mutants. [src: adp1_triple_essentiality] Separately, the same project finds a null association between FBA class and growth defects within TnSeq-dispensable genes. [src: adp1_triple_essentiality] The knockout comparison uses a different reference from Side A (knockouts rather than TnSeq), while the null result applies to a narrower gene subset (TnSeq-dispensable genes only) and a growth-defect endpoint.

## Possible Reconciliations

- **Hypothesis 1: The gene sets differ.** The concordance figure covers genes with both FBA and TnSeq calls. [src: acinetobacter_adp1_explorer] The null result is confined to TnSeq-dispensable genes. [src: adp1_triple_essentiality] Most agreement may come from clearly essential or clearly non-essential genes, leaving FBA uninformative within the dispensable subset.
- **Hypothesis 2: The endpoints differ.** Agreement on an essential/non-essential call may coexist with no predictive power for growth defects, in which case both results could hold at once.
- **Hypothesis 3: The reference assay differs.** Concordance with TnSeq and with knockouts may diverge because TnSeq and knockout definitions of essentiality do not coincide. Under this reading, FBA's apparent reliability depends on which experimental standard it is scored against.

Neither side is preferred here. Because the endpoints and gene sets differ, matched-gene comparisons are needed to settle the question.

## Resolving Work

- Restrict both analyses to an identical ADP1 gene list, scored under the same medium condition. Recompute FBA concordance against TnSeq and against knockouts to test whether the gap persists on matched genes.
- Use one fixed knockout definition and one FBA class assignment across both projects. Ask whether the concordance against TnSeq calls changes when the essentiality reference is harmonized.
- Replace binary essentiality calls with a continuous growth endpoint, such as mutant growth measurements, across the full gene set. Test whether FBA class predicts growth outside the TnSeq-dispensable subset as well as inside it.
- Stratify the FBA/TnSeq comparison by TnSeq-dispensable versus TnSeq-essential genes. Ask whether the overall agreement is carried by one stratum.
- Repeat the matched comparison under a second medium. Determine whether concordance is condition-specific, which bears on how gapfilled reactions should be validated.
