<!-- tension-hash: e8b22b587fba56eb -->
# Composite COG Annotations: Biological Signal or Insufficiently Tested Interpretation?

Clusters of Orthologous Groups (COG) annotations sometimes assign one gene several functional letters at once. The corpus disagrees about how firmly these composite assignments can be read as multifunctional biology rather than annotation noise. The sources' confidence in the "not noise" reading is stronger than their evidence. [src: discoveries, cog_analysis, gene_function_ecological_agora] This matters because a recommendation to keep composite-COG genes changes how downstream pangenome analyses (studies of the collective gene repertoire across a set of genomes) filter their inputs. The strength of that recommendation should therefore match the strength of its support. The tension is recorded on [[concepts/composite-functional-annotation]].

## Evidence Sides

**Side A: composite categories should be treated as meaningful, not filtered as noise**

The discoveries digest advises against filtering composite-COG genes out as noise. [src: discoveries, cog_analysis, gene_function_ecological_agora] On this reading, composite assignments mark real multifunctional genes. One example is the LV composite, a single annotation combining L (mobile elements) and V (defense mechanisms). A parallel signal comes from KEGG Orthology (KO) groups that mix regulatory and metabolic pathway membership, though that signal is explicitly exploratory and hypothesis-generating rather than corroboration. [src: discoveries, cog_analysis, gene_function_ecological_agora]

**Side B: the evidence supports a hypothesis, not a filtering rule**

The underlying COG evidence is a single LV enrichment. That enrichment is interpreted without a separate validation test. [src: discoveries, cog_analysis, gene_function_ecological_agora] The parallel mixed-category KO signal is explicitly exploratory and hypothesis-generating. [src: discoveries, cog_analysis, gene_function_ecological_agora] On this side, the "not noise" reading stays a hypothesis rather than an established finding, even if retaining composite genes remains defensible as a precaution.

## Possible Reconciliations

- *Hypothesis:* Some composite categories, such as LV, reflect genuine functional modules, while others are annotation artifacts. If so, a blanket rule for or against filtering would be miscalibrated in both directions.
- *Hypothesis:* The COG and KO signals share a common biological cause. Each needs its own confirmatory test before the two can be treated as mutual corroboration rather than two exploratory observations.
- *Hypothesis:* The recommendation is sound as a precaution, meaning composite genes should not be discarded before testing, but not as a finding. Under this reading, the two sides differ in wording rather than in substance.

## Resolving Work

- **Held-out validation:** Repeat the LV enrichment test on a separate set of species pangenomes not used in the original analysis. Does the composite enrichment replicate under a pre-specified test?
- **Per-composite screen:** Run enrichment tests across every composite COG combination, with false discovery rate (FDR) correction, meaning a control on the expected share of false positives among the significant results. Which composites show the signal beyond LV, and which do not?
- **Annotation-artifact control:** Compare composite-COG genes against domain-architecture data, such as multi-domain protein structure. Do composite assignments coincide with multi-domain genes, as the multifunctional reading predicts?
- **Confirmatory KO test:** Convert the exploratory mixed-category KO observation into a pre-registered test using tree-aware gain attribution (assigning inferred gene gains to branches of an evolutionary tree) on an independent clade subset. Does the mixed-pathway signal survive confirmatory testing?
- **Filtering-sensitivity analysis:** Run downstream pangenome analyses with composite-COG genes both retained and removed. Does the choice change any substantive conclusion?
