---
type: "Concept"
description: "How cofitness, module enrichment and fitness-module context transferred from orthologs are used to assign function to hypothetical or unannotated (including essential) genes, how far they reach and how they benchmark; stops at group construction."
sources: ["summaries/discoveries.md", "summaries/essential_genome__REPORT.md", "summaries/fitness_modules__REPORT.md", "summaries/functional_dark_matter__REPORT.md", "summaries/metal_fitness_atlas__REPORT.md", "summaries/truly_dark_genes__REPORT.md"]
---
# Function prediction for uncharacterized genes by guilt-by-association and ortholog transfer

This page covers how guilt-by-association and ortholog transfer are used to assign function to hypothetical or unannotated genes, including essential ones. In a held-out benchmark across 32 organisms, ortholog transfer predicts specific KEGG ortholog (KO) groups far better than module-based methods. Module context is better read as biological-process information. Predictions for essential genes are indirect, because they come from orthologs in other organisms. [src: discoveries, fitness_modules, essential_genome]

## Literature Context

The one candidate paper addresses the same problem the hub covers: assigning function to uncharacterized genes when sequence similarity is not enough. In Plasmodium falciparum, about 57% of the 5 484 predicted genes lack sufficient sequence similarity to characterized genes in other species to warrant functional assignments [PMID 20078859](https://pubmed.ncbi.nlm.nih.gov/20078859/). The authors say non-homology methods are therefore needed. They note that gene expression data have been widely used for intra-species guilt-by-association (GBA) annotation [PMID 20078859](https://pubmed.ncbi.nlm.nih.gov/20078859/).

Their method starts from likely orthologs between reference species (S. cerevisiae and D. melanogaster) and the query species P. falciparum. It identifies clusters of coexpressed genes in the query whose coexpression is conserved in the reference. It then uses those conserved clusters to assess annotation transfers between genes with low sequence similarity [PMID 20078859](https://pubmed.ncbi.nlm.nih.gov/20078859/). The authors report that this improves accuracy over sequence similarity alone and outperforms the GBA approach. They propose high-confidence new or refined annotations for several dozens of hypothetical or putative genes, including revised ribosomal-protein and ribosome-biogenesis annotations that highlight potential drug targets [PMID 20078859](https://pubmed.ncbi.nlm.nih.gov/20078859/). The source is an abstract, so these results are stated as the authors report them, and the abstract gives no benchmark figures.

The corpus is consistent with this literature in its general direction. It also uses guilt-by-association, and it extends the expression-based principle to fitness data through ICA fitness modules. The two works differ in evidence type and in how they combine the layers. The Plasmodium study uses conserved coexpression to vet ortholog-based transfer. The corpus keeps the two layers apart. Ortholog transfer is benchmarked on its own, at 95.8% precision and 91.2% coverage, while module and cofitness predictions score below 1% strict KO precision and are read as process-level context. The corpus's 6,691 hypothetical-protein predictions are split into 2,455 family-backed ones, supported by cross-organism conservation, and 4,236 that are module-only. Only the family-backed subset has the cross-species support that the Plasmodium study makes central. The module-only predictions have no such support.

The essential-gene analysis is closest to the cross-species idea. It transfers module context from non-essential orthologs to essential genes, giving 1,382 predictions, all backed by module family conservation. These are indirect, and the essential gene's function may have diverged. The Plasmodium paper does not address essential genes or fitness data, and the corpus does not test whether conserved co-behavior improves transfer in the way the Plasmodium paper reports. The corpus findings therefore extend the approach to bacterial fitness data and are not in tension with the paper. The Plasmodium result is also not a direct validation of the corpus predictions. A comparison of module-only and family-backed predictions on withheld labels would test it.

## Benchmark: ortholog transfer versus modules

The NB07 held-out benchmark withheld 20% of KEGG-annotated genes and evaluated 4 methods that predict KO groups. [src: fitness_modules] Ortholog transfer dominated gene-level prediction, with 95.8% precision and 91.2% coverage. Module-ICA (independent component analysis) had <1% precision at the KO level. [src: discoveries] See ortholog transfer function prediction and [[entities/independent-component-analysis-fitness-modules]].

| Method | Strict precision | Coverage | F1 |
|---|---|---|---|
| Ortholog transfer | 95.8% | 91.2% | 0.934 [src: fitness_modules] |
| Domain-based | 29.1% | 66.6% | 0.401 [src: fitness_modules] |
| Module-ICA | <1% | 23.3% | not reported [src: fitness_modules] |
| Cofitness voting | <1% | 73.0% | not reported [src: fitness_modules] |

The report attributes the near-zero strict KO precision of Module-ICA and cofitness to KEGG KO groups being gene-level assignments (~1.2 genes per unique KO). [src: fitness_modules] A module with 20 annotated members typically has 20 different KOs. [src: fitness_modules] An ABC (ATP-binding cassette) transporter module groups binding, permease and ATPase subunits correctly, but each subunit has a different KO. [src: discoveries]

The report therefore treats modules as capturing process-level co-regulation, with 94.2% cofitness enrichment and 22.7× adjacency enrichment, rather than specific molecular function. [src: discoveries] Module predictions should be framed as "involved in [biological process]", not as exact KO assignments. [src: discoveries, fitness_modules] Module-ICA complements sequence-based methods by finding co-regulated gene groups. It should not be used to predict specific molecular functions, where ortholog transfer is far superior. [src: fitness_modules]

## Reach of module-based predictions

Adding Pfam domains and lowering the enrichment overlap threshold from 3 to 2 raised module annotation from 8% to 80% (92 to 890 modules). This unlocked 7.6x more function predictions. [src: fitness_modules] Pfam gave the broadest coverage, while KEGG KOs were too gene-specific for module-level enrichment. [src: fitness_modules] Pfam annotations are domain-level and may overcount functional associations. [src: fitness_modules] Predictions were backed by enrichment in KEGG, SEED, TIGRFam and PFam. [src: fitness_modules]

The fitness-module analysis made 6,691 function predictions for hypothetical proteins across all 32 organisms. Of these, 2,455 (37%) were family-backed, supported by cross-organism conservation, and 4,236 were module-only. [src: fitness_modules]

The dark-gene report found 6,142 dark genes in ICA fitness modules, giving guilt-by-association predictions. [src: functional_dark_matter] In its census, these are 10.8% of dark genes. [src: functional_dark_matter] Among the top 100 dark-gene candidates, 85 have module-based predictions. [src: functional_dark_matter] Cross-checking against prior module-based predictions found existing predictions for 85/100, all agreeing with the report's independent inference. [src: functional_dark_matter] The report supported its functional-coherence hypothesis (H1a) and called guilt-by-association its single strongest inference layer. [src: functional_dark_matter] These remain inferences, not direct experimental validation. [src: functional_dark_matter]

The ICA module approach extends Oliver's (2000) expression-based guilt-by-association principle to fitness data. [src: truly_dark_genes] The metal fitness atlas likewise reports 149 novel metal-biology candidates. These are gene families with conserved metal fitness phenotypes across ≥2 organisms but without full annotation. Their predictions rest solely on cross-species fitness data. [src: metal_fitness_atlas]

## Essential genes via ortholog module transfer

Essential genes lack fitness data and are invisible to ICA. Their non-essential orthologs in other organisms do have fitness data and can join modules, so the module's functional context can be transferred. [src: essential_genome] This adds a cross-organism essentiality dimension that reaches genes outside fitness profiling. [src: essential_genome] See [[concepts/essential-genes-as-a-blind-spot-of-transposon-fitness-screens]].

- The analysis found 8,297 hypothetical essential genes across 48 organisms, 20.2% of all essentials. [src: essential_genome]
- Of these, 3,912 have orthologs and are predictable. The other 4,385 are orphans and cannot be predicted by this method. [src: essential_genome]
- Module transfer produced 1,382 predictions, 35.3% of predictable targets. [src: discoveries, essential_genome]
- All predictions are backed by cross-organism module family conservation. [src: discoveries, essential_genome]
- Predictions span 48 organisms, from 90 in pseudo1_N1B4 to 1 in Caulo. [src: essential_genome]
- Top predicted functions include TIGR00254 (signal transduction), PF00460 (flagellar basal body rod) and PF00356 (lactoylglutathione lyase). [src: essential_genome]

The report concludes that module context from non-essential orthologs can illuminate essential genes that fitness-based methods cannot see. [src: discoveries]

Universally essential genes are only 8.2% hypothetical. [src: essential_genome] Orphan essentials are 58.7% hypothetical, the highest uncharacterized fraction of any category. [src: essential_genome] The report compares this with Hutchison et al. (2016), who found unknown function for 149 of 473 genes (31%) in a minimal Mycoplasma genome. [src: essential_genome] It reads its 7,084 orphan essentials as showing that the problem is universal across bacteria. [src: essential_genome]

Module-transfer predictions for essential genes are indirect, because they come from non-essential orthologs in other organisms and the essential gene's function may have diverged. [src: essential_genome]

The report proposes two follow-ups. One is to characterize the 7,084 orphan essentials for mobile-element association, recent acquisition, rapid evolution and functional categories. [src: essential_genome] The other is to test the 1,382 predictions by CRISPRi (CRISPR interference) knockdown under conditions predicted by module context. [src: essential_genome]

## Open Directions

- Characterize the orphan essentials (mobile elements, recent acquisition, evolutionary rate), since orphans are the group this method cannot reach.
- Test the module-transfer predictions by CRISPRi knockdown under module-predicted conditions. This would show whether diverged function limits them.
- Benchmark module-based predictions at the biological-process level, for example with pathway-level labels. The KO-level benchmark cannot credit modules.
- Extend the held-out benchmark to essential-gene transfer, which these reports do not benchmark on withheld labels.
