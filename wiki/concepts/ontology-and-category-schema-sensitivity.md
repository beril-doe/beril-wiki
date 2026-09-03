---
type: "Concept"
description: "Biological conclusions can change when ontology or category definitions change."
sources: ["summaries/discoveries.md"]
---
# Ontology and Category-Schema Dependence of Biological Conclusions

Biological conclusions are partly determined by the ontology, category schema, and matching rules used to represent observations, so analyses should treat schema choice as an explicit source of uncertainty rather than as a neutral preprocessing step. [src: discoveries] The findings summarized in [[summaries/discoveries]] connect this issue to [[concepts/environmental-resistome]], [[concepts/composite-functional-annotation]], [[concepts/evidence-triangulation-for-functional-annotation]], and [[concepts/cross-tenant-data-bridging]].

## Category definitions can reverse pathway conclusions

In an inflammatory-bowel-disease pathway analysis, a regex-based category scheme identified 3 of 52 CD-up pathways in 7 themes and produced a structurally degenerate result. [src: discoveries] A MetaCyc hierarchy assigned 262/409 pathways to at least one of 12 IBD themes and supported iron/heme acquisition with OR=8.1, FDR=7e-6, and 15/52 CD-up pathways. [src: discoveries] Here, FDR means false discovery rate, and OR means odds ratio. [src: discoveries]

This **contradicts** any interpretation that the biological theme is independent of category construction: the same underlying pathway results yielded materially different counts and conclusions under the two schemas. [src: discoveries] The evidence supports using curator-validated ontology hierarchies as the primary analysis and regex categories as a sensitivity analysis. [src: discoveries]

## Composite annotations can carry biological signal

Across 32 species and 9 phyla, novel or singleton genes were enriched in COG L mobile elements by +10.88%, COG V defense mechanisms by +2.83%, and COG S unknown function by +1.64%. [src: discoveries] Core genes were depleted in COG J translation by -4.65%, COG F nucleotide metabolism by -2.09%, COG H coenzyme metabolism by -2.06%, COG E amino acid metabolism by -1.81%, and COG C energy production by -1.75%. [src: discoveries]

Composite assignments such as LV showed +0.34% enrichment and 76% consistency, indicating that multi-function assignments can represent real mobile-defense modules rather than annotation noise. [src: discoveries] This **supports** [[concepts/composite-functional-annotation]] and cautions against forcing genes with multiple functional labels into a single mutually exclusive category. [src: discoveries]

## Annotation systems define different measurable spaces

Bakta and eggNOG produced complementary functional coverage across 132.5M gene clusters. [src: discoveries] eggNOG had higher COG coverage, at 51% versus 8.2%; KEGG coverage, at 38.5% versus 17.3%; and Pfam coverage, at 63% versus 7.7%. [src: discoveries] Bakta had higher GO coverage, at 15% versus 7.4%; product descriptions, at 71.2% versus 70.4%; and unique UniRef50 links covering 79.2%. [src: discoveries]

Their union increased any-functional-annotation coverage to 77.3%, and Bakta rescued 11.2M clusters among 39.2M missed by eggNOG. [src: discoveries] Only 33.3% of Bakta's 17.6M distinct UniRef50 IDs existed in the BERDL UniProt identifier table. [src: discoveries] These results **refine** [[concepts/evidence-triangulation-for-functional-annotation]]: apparent functional absence can reflect annotation-system coverage or identifier-table coverage rather than biological absence. [src: discoveries]

## Marker and ontology proxies require validation

Annotation proxies can produce substantially different biological counts depending on the selected preferred name, KO, or product definition. [src: discoveries] eggNOG `Preferred_name='lanM'` produced 505 additional hits with zero overlap with 62 Bakta-validated Lanmodulin genomes. [src: discoveries] eggNOG KO K02030 produced 46,369 nonspecific hits, and only 418 of 5,092 genomes with any xoxF marker hit both eggNOG K00114 and Bakta lanthanide-dependent methanol-dehydrogenase products. [src: discoveries]

The findings **support** [[concepts/environmental-resistome]] and [[concepts/homology-search-negative-evidence]] by showing that generic KOs and stale preferred names should not be treated as definitive markers. [src: discoveries] Analyses should report marker definitions explicitly and validate them against an independent annotation or curated reference set. [src: discoveries]

## Schema choice interacts with integration and transfer

The category-schema problem extends beyond pathway enrichment because joins, classifiers, and cross-dataset comparisons depend on compatible representations of the same biological object. [src: discoveries] Relative-abundance spaces were cross-cohort-portable because they were unitless and compositional, whereas absolute-intensity metabolomics required explicit batch correction such as ComBat, SVA, RUV, or quantile normalization. [src: discoveries] In a pooled HMP2 and Franzosa metabolomics analysis, PCA plus K-means with K=4 separated completely by cohort rather than diagnosis, PC1 explained 79% of variance, and cross-cohort LOSO ARI was 0.000 versus 0.113 for taxonomic ecotypes. [src: discoveries]

A CLR-plus-PCA GMM projection assigned all 26 Kuehl samples to E3 at confidence greater than 0.97 because Kuehl detected only 54% of training species, whereas LDA projection across MetaPhlAn3 and Kaiju namespaces produced plausible Kuehl proportions of 27/42/31% across ecotypes. [src: discoveries] These results **refine** [[concepts/cross-cohort-microbiome-portability]]: representation and namespace compatibility can determine whether a transfer appears biologically plausible or fails through projection artifacts. [src: discoveries]

## Analytical implications

Ontology selection, category construction, marker definition, and identifier mapping should be recorded as model choices that can alter effect sizes, pathway counts, and inferred biological themes. [src: discoveries] A robust analysis should compare at least one curator-validated hierarchy with a simpler sensitivity schema, preserve multi-label assignments where biologically justified, and validate positive and negative marker calls against independent evidence. [src: discoveries]

This approach **supports** [[concepts/ontology-and-category-schema-sensitivity]] as a methodological complement to [[concepts/multi-omics-integration]] and [[concepts/cross-tenant-data-bridging]]: a cross-modal conclusion is only as stable as the mappings and category definitions used to connect its modalities. [src: discoveries]

## Open Directions

- Re-run the 52 CD-up pathway analysis with the regex scheme, the curator-validated MetaCyc hierarchy, and a third ontology while holding the statistical model and multiple-testing procedure fixed; test which iron/heme-acquisition conclusion remains stable. [src: discoveries]
- Build a benchmark of independently validated lanthanide-dependent methanol-dehydrogenase genomes and compare preferred-name, KO, product-description, and profile-based markers; quantify precision, recall, and disagreement across marker definitions. [src: discoveries]
- Recompute the 32-species COG enrichment analysis with mutually exclusive versus multi-label category assignments; test whether the +0.34% LV enrichment and 76% consistency persist under each representation. [src: discoveries]
- Reconcile MetaPhlAn3 and Kaiju species namespaces before cross-cohort projection, then compare LDA and CLR-plus-PCA GMM using held-out samples; determine whether the Kuehl E3 assignment is a namespace artifact or a reproducible ecotype signal. [src: discoveries]
- Audit pathway and metabolite joins using explicit identifier dictionaries and collision tests, including leucine versus isoleucine; measure how many inferred pathway associations change after schema-to-value-space validation. [src: discoveries]
