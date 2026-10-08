<!-- tension-hash: 3d6cb5641cbe154b -->
# Do the Regex and MetaCyc Schemas Cover the Same Pathway Set in the IBD Reversal?

The central discoveries digest and the inflammatory bowel disease (IBD) phage-targeting project report give different coverage figures for the two categorization schemas in the same verdict reversal. One schema is a regular-expression (regex) match on pathway names and the other is the MetaCyc pathway class hierarchy [src: discoveries, ibd_phage_targeting]. The digest reports 3 of 52 CD-up pathways (pathways elevated in Crohn's disease, CD) identified by regex and 262/409 pathways assigned by MetaCyc [src: discoveries]. The report gives 44/409 background pathways for regex and 514/575 pathways categorized by MetaCyc [src: ibd_phage_targeting]. The MetaCyc-side denominators differ, so the counts may describe different pathway sets, and the corpus does not reconcile them [src: discoveries, ibd_phage_targeting]. The disagreement matters for how schema coverage is reported in [[concepts/ontology-and-category-schema-sensitivity]].

## Evidence Sides

**Side A: discoveries digest**
- The regex identified 3 of 52 CD-up pathways in 7 themes [src: discoveries].
- The MetaCyc hierarchy assigned 262/409 pathways to at least one of 12 IBD themes [src: discoveries].

**Side B: ibd_phage_targeting project report**
- The regex covered 44/409 background pathways [src: ibd_phage_targeting].
- MetaCyc categorized 514/575 pathways, described as 90 % coverage of 575 HUMAnN3 pathways [src: ibd_phage_targeting].

**What the corpus states about the gap**
- The MetaCyc-side denominators differ, so the counts may describe different pathway sets [src: discoveries, ibd_phage_targeting].
- The corpus does not reconcile the figures, and both are kept as written [src: discoveries, ibd_phage_targeting].

## Possible Reconciliations

- **Hypothesis 1: different denominators.** The two documents may count against different denominators. The digest's 409 for MetaCyc may be a background set tested for enrichment. The report's 575 may be the full HUMAnN3 output. Nothing in the corpus confirms this.
- **Hypothesis 2: different units of measure.** The regex figures may measure different things. "3 of 52 CD-up pathways in 7 themes" counts regex hits among the CD-up pathways. "44/409 background pathways" counts hits in a background set. Under this reading the two are not competing values for one quantity.
- **Hypothesis 3: different analysis versions.** The two documents may report different iterations of the analysis, with filters, theme definitions or pathway lists that changed between them. For example, the digest's 12 IBD themes may not correspond to the report's categorization scope. This is not established in the corpus.

## Resolving Work

- **Re-derive the MetaCyc denominator.** Data: the HUMAnN3 pathway table and the MetaCyc class hierarchy used in `ibd_phage_targeting`. Method: re-run the class assignment while logging every filtering step. Question: does the 409-pathway set arise as a filtered subset of the 575, and do 262 and 514 both follow from the same hierarchy?
- **Recount the regex hits in both units.** Data: the regex rules and pathway names. Method: count matches separately among CD-up pathways and among the background set. Question: are "3 of 52" and "44/409" two units of one run, or outputs of different runs?
- **Map theme definitions across documents.** Data: the 7 regex themes and the 12 IBD themes. Method: a side-by-side mapping of theme definitions. Question: do the schemas target the same biological categories, so that coverage is comparable?
- **Check provenance against the digest.** Data: the notebook versions cited in the project report. Method: provenance tracing from each digest figure back to a specific notebook output. Question: which analysis version does each figure come from?
