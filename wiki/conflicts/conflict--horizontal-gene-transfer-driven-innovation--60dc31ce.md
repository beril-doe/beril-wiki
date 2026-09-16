<!-- tension-hash: 60dc31ce5b31dec9 -->
# Do Mobile Elements Carry Most Bacterial Gene Novelty, or Do Focal Innovations Arrive Without an MGE-Cargo Signal?

Within [[concepts/horizontal-gene-transfer-driven-innovation]], projects disagree about how much bacterial gene novelty arrives through mobile genetic elements (MGEs, DNA such as transposons, phages and plasmids that can move within or between genomes). The COG analysis reads its result as suggesting that most genomic novelty comes from mobile elements. The costly+dispensable report proposes HGT-mediated genome expansion (HGT, horizontal gene transfer, the movement of genes between lineages) as the primary source of costly non-conserved genes. [src: cog_analysis, costly_dispensable_genes] A third project detected no MGE-cargo enrichment for its best-supported cross-clade innovation, photosystem II (PSII). [src: gene_function_ecological_agora] The answer determines whether mobile-element content can stand in as a general marker of how genes are gained. The sources do not establish what share of novelty each route carries. [src: cog_analysis, costly_dispensable_genes, gene_function_ecological_agora]

## Evidence Sides

**Side A: mobile elements as the primary source of novelty**

The COG analysis uses Clusters of Orthologous Groups, a scheme that sorts genes into functional categories. It found a +10.88% enrichment of COG L, the mobile-element category, among novel or singleton genes. The analysis interprets this as *suggesting* that most genomic novelty comes from mobile elements. The costly+dispensable report *proposes* HGT-mediated genome expansion as the primary source of costly non-conserved genes. [src: cog_analysis, costly_dispensable_genes] On this side, the mobile-element primacy claim is an interpretation and a proposal. It is not a direct measurement of where each gene came from.

**Side B: focal innovations with no detected MGE-cargo signal**

The agora analysis measured MGE-machinery rates of 0%, 0%, and 0.57% for three focal gene sets: photosystem II (PSII), polysaccharide utilization loci (PUL), and mycolic acid. The PSII gene neighborhood was at baseline (10.91% versus 10.6%). No MGE-cargo enrichment was therefore detected for the project's best-supported cross-clade innovation. [src: gene_function_ecological_agora] This is a null enrichment result. It does not exclude transfer by mobile elements. The report's proposed route for these genes includes integrative and conjugative elements (ICEs), which are themselves mobile elements. The disagreement therefore concerns phage or MGE-cargo signatures, not mobility as such. [src: cog_analysis, costly_dispensable_genes, gene_function_ecological_agora]

## Possible Reconciliations

- **Hypothesis 1 (different units):** The two sides measure different things. Side A counts novel or singleton genes, while Side B counts focal gains of KEGG Orthology (KO) groups, which are functional ortholog families. Both results could hold at once if mobile elements dominate the singleton pool but not durable cross-clade gains. [src: cog_analysis, costly_dispensable_genes, gene_function_ecological_agora]
- **Hypothesis 2 (signature versus mobility):** Focal genes may have moved on ICEs or other mobile vehicles that left no lasting phage or cargo signature. That would make Side B's null compatible with mobile-element transfer. [src: cog_analysis, costly_dispensable_genes, gene_function_ecological_agora]
- **Hypothesis 3 (signature decay):** Recently acquired genes may still sit beside mobile machinery, while older gains that have spread across clades may have lost that context. Under this hypothesis, each side samples a different stage of gene residence.

## Resolving Work

- **Same unit for both sides:** Apply the agora MGE-machinery and neighborhood test to the novel or singleton gene set behind the COG L result. This asks whether the enrichment persists when both sides use the same metric.
- **ICE detection around focal genes:** Run a dedicated ICE and integrative-element search around the PSII, PUL and mycolic-acid loci. This asks whether a mobile route without phage cargo can be detected directly.
- **Age-stratified comparison:** Stratify novel genes by acquisition depth or gain age and compare MGE-neighborhood rates. This tests the signature-decay hypothesis.
- **Novelty apportioned by route:** Partition each project's novelty set into MGE-associated and non-MGE-associated gains under one shared definition. This asks what share of novelty each route carries, which the sources currently leave open.
