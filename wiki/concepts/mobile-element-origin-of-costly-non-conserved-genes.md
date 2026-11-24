---
type: "Concept"
description: "Whether genes that are burdensome in the lab and absent from the species core are mostly horizontally acquired mobile-element debris, covering their annotation, ortholog breadth, length and organism distribution; stops short of genomic-context tests."
sources: ["summaries/conservation_fitness_synthesis__REPORT.md", "summaries/costly_dispensable_genes__REPORT.md"]
---
# Mobile-element origin of costly, non-conserved genes

The question here is whether genes that are burdensome in the lab and absent from the species core are mostly horizontally acquired mobile-element debris. One report (costly_dispensable_genes) says yes, on annotation, ortholog breadth, length and organism-distribution evidence. That evidence is correlational and rests on keywords and annotation categories. Genomic-context tests are only proposed, so the conclusion is supported but not fully tested. The earlier synthesis report left the identity of these genes as an open question. [src: conservation_fitness_synthesis] The later report finds them overwhelmingly associated with mobile genetic elements, which narrows that question but does not settle each gene's identity. [src: conservation_fitness_synthesis, costly_dispensable_genes] See also [[concepts/horizontal-gene-transfer-and-mobile-elements-as-a-source-of-novel-and-dark-genes]] and [[concepts/costly-but-conserved-genes-laboratory-burden-versus-conservation]].

## Literature Context

The candidate evidence for this page is thin: one paper, and it is indirectly related. [PMID 26849314](https://pubmed.ncbi.nlm.nih.gov/26849314/) is a mathematical model of integron evolution. Integrons are genetic elements that are common in bacteria and are hotspots for genome evolution. They help bacteria acquire and reassemble gene cassettes, including cassettes for drug resistance. The paper is an abstract-level source, and it reports model results, not measurements from organisms or genomes. It does not examine annotation, ortholog breadth, gene length or organism distribution, and it does not use Fitness Browser data.

The model asks how a costly mobile-element function can persist. In bacterial populations facing fluctuating antibiotic exposure, a functional integrase that reshuffles cassette genes can be stably maintained across a wide range of parameters, despite substantial fitness costs. The proposed reason is that cassette shuffling generates genetic diversity, so the population can respond quickly when selection changes. The same model finds that horizontal gene transfer promotes stable maintenance of the integrase and can also lead to de novo assembly of integrons. It predicts that functional integrases are lost in stable environments. It also predicts selection for intermediate gene-shuffling rates in changing environments. The authors say experimental studies of integron population biology are needed [PMID 26849314](https://pubmed.ncbi.nlm.nih.gov/26849314/).

The corpus finding on this page is that costly, dispensable genes are overwhelmingly associated with mobile genetic elements, based on keyword, SEED category, ortholog breadth and length evidence. This is **consistent in general direction** with the model. The model treats mobile elements as costly yet able to persist, and as supplied by horizontal transfer. That fits the idea that HGT-mediated genome expansion feeds the pool of burdensome non-conserved genes. The fit is conceptual only. The model concerns one element class, integrons, and does not predict the corpus's specific numbers. These include the odds ratio of 7.45 for mobile-element keywords and the median lengths of 615 bp versus 765 bp.

The model also bears on the report's "not inert" observation, that 14.1% of costly+dispensable genes show condition-specific phenotypes, and on its suggestion that such effects may slow loss. The model supplies a mechanism by which a costly element is retained when conditions fluctuate. This **suggests the hypothesis** that some of these genes are kept by episodic benefit, not just by slow decay. That hypothesis is untested here. The corpus's own debris interpretation, in which the genes are on the way out, is not contradicted by the model, since the model predicts loss in stable environments. Neither source tests genomic context, so the question the hub leaves open stays open.

Overall, the literature available here neither confirms nor challenges the corpus's main claim. It offers only a theoretical backdrop for persistence of costly mobile elements.

## The candidate set

The synthesis report identified 5,526 costly and dispensable genes as candidates for ongoing gene loss. [src: conservation_fitness_synthesis] It left open whether they were mobile elements or recently acquired genes on the way out. [src: conservation_fitness_synthesis] The follow-up report concluded that they are overwhelmingly associated with mobile genetic elements. [src: costly_dispensable_genes] It interprets them as the debris of horizontal gene transfer (HGT): insertion sequences, prophage remnants, transposases and defense systems that cost the host metabolically and are not conserved across the species pangenome. [src: costly_dispensable_genes] It also says they have the hallmarks of recently acquired DNA. [src: costly_dispensable_genes]

## Annotation evidence

Costly+dispensable genes are 7.45x more likely than costly+conserved genes to carry mobile-element keywords in their descriptions (odds ratio, OR=7.45, p=4.6e-71). [src: costly_dispensable_genes] Keywords include transposase, integrase, phage, IS element, recombinase and prophage. [src: costly_dispensable_genes] In SEED functional categories, "Phages, Prophages, Transposable elements, Plasmids" is 11.7x enriched (false discovery rate, FDR=1.3e-17). [src: costly_dispensable_genes] "Virulence" is 26.7x enriched (FDR=5.6e-14). [src: costly_dispensable_genes] The Virulence result rests on small counts, 21 vs 4 genes, so it is weak support. [src: costly_dispensable_genes] Fourteen top-level SEED categories are significantly depleted (FDR < 0.05), including Protein Metabolism, Respiration, Carbohydrates, Amino Acids, Cofactors/Vitamins, Motility, Stress Response and RNA Metabolism. [src: costly_dispensable_genes]

These genes are also poorly annotated. SEED annotation covers 50.8% of them versus 74.9% of costly+conserved genes. [src: costly_dispensable_genes] KEGG covers 20.0% versus 42.7%. [src: costly_dispensable_genes] The report summarizes this as 24pp less likely to have SEED annotations. [src: costly_dispensable_genes]

## Ortholog breadth and distribution

Costly+dispensable genes are taxonomically restricted. The median number of organisms sharing the ortholog group is 15, versus 31 for costly+conserved genes (Mann-Whitney p=4.0e-99, rank-biserial r=0.233). [src: costly_dispensable_genes] Orphan genes with no ortholog group make up 44.5%, versus 13.1%. [src: costly_dispensable_genes] Singletons found in only 1 genome make up 24.2%, and no costly+conserved genes are singletons. [src: costly_dispensable_genes] That contrast is partly structural, because core genes cannot be singletons by definition. [src: costly_dispensable_genes] Within dispensable genes, costly genes are only slightly more likely than neutral ones to be singletons (OR=1.09, p=0.02). [src: costly_dispensable_genes] The report treats the narrow distribution as confirming its hypothesis. [src: costly_dispensable_genes]

## Gene length

The median length is 615 bp for costly+dispensable genes versus 765 bp for costly+conserved (p=4.2e-75, rank-biserial r=0.170). [src: costly_dispensable_genes] The report calls this consistent with IS elements and gene fragments. [src: costly_dispensable_genes] It summarizes the genes as 20% shorter and poorly annotated, confirming its hypothesis. [src: costly_dispensable_genes]

## Not inert

Condition-specific phenotypes occur in 14.1% of costly+dispensable genes versus 16.7% of costly+conserved genes. [src: costly_dispensable_genes] Neutral+dispensable genes show 2.7%. [src: costly_dispensable_genes] The report suggests these genes retain fitness effects that may slow their loss. [src: costly_dispensable_genes]

## Conclusion and caveats

The report concludes that the genes are almost exclusively mobile-element debris, not degrading metabolic pathways. It suggests HGT-mediated genome expansion is the primary source of costly non-conserved genes in bacteria. [src: costly_dispensable_genes] Several caveats limit this:

- Burden is defined as max_fit > 1 in any experiment, so one experiment can classify a gene as burdensome and noise matters. [src: costly_dispensable_genes]
- SEED/KEGG annotations cover only 56-79% of genes, and the unannotated fraction may differ functionally. [src: costly_dispensable_genes]
- The 90% identity DIAMOND threshold for linking Fitness Browser genes to the pangenome may miss recently acquired genes with low similarity. [src: costly_dispensable_genes]
- Ortholog groups use bidirectional best hits (BBH) across 48 organisms, so genes with orthologs outside that set would be misclassified as orphans. [src: costly_dispensable_genes]
- Genomic context is untested. The report proposes checking whether these genes cluster in genomic islands, near tRNA genes or at scaffold edges, which it describes as hallmarks of HGT. [src: costly_dispensable_genes]

## Open Directions

- Run the genomic context analysis the report proposes. This would test the mobile-element claim directly, beyond keywords. [src: costly_dispensable_genes]
- Repeat the burden classification with a replicated-experiment or noise-aware threshold. This would address the single-experiment sensitivity. [src: costly_dispensable_genes]
- Test the unannotated genes, for example by domain search for mobile-element signatures. This would address the annotation gap. [src: costly_dispensable_genes]
- Re-link with a more permissive similarity threshold and a wider organism set. This would check the orphan and recent-acquisition calls. [src: costly_dispensable_genes]
- Compare the retained condition-specific phenotypes with gene-loss rates to test whether fitness effects slow loss. [src: costly_dispensable_genes]
