---
type: "Concept"
description: "Covers whether compound origin (groundwater versus necromass) can be separated from chemical class when assessing utilization, and where it cannot."
sources: ["summaries/enigma_carbon_census_1__REPORT.md"]
---
# Confounding of compound source with chemical class

Compound source (groundwater versus necromass) cannot be separated from chemical class among the callable compounds in the ENIGMA Carbon Census. [src: enigma_carbon_census_1] Darkness tracks chemical class, not source. [src: enigma_carbon_census_1] The evidence comes from a single report, [[summaries/enigma_carbon_census_1__REPORT]], and rests on direct counts of a small compound set. [src: enigma_carbon_census_1]

## Literature Context

The candidate papers contain almost nothing on microbial catabolism of compounds, so the literature support here is indirect and methodological. One paper is relevant. It is a cheminformatics study of urease inhibitors, and it asks whether differences between compound collections reflect the collection's provenance or the chemistry of interest [PMID 42941928](https://pubmed.ncbi.nlm.nih.gov/42941928/). The study used UI-Ref, a curated set of 1218 compounds reported in urease assays. A random forest trained on 25 physicochemical descriptors predicted the depositing database with a ROC AUC of 0.954 and the source publication with a median one-versus-rest AUC of 0.997. After property matching and publication-grouped cross-validation, separation from external libraries fell to AUCs of 0.762-0.841. The authors state that their design cannot distinguish target-related chemistry from residual provenance structure. They conclude that provenance-associated confounding can dominate cross-collection comparisons and should be quantified before chemical or biological interpretations are drawn [PMID 42941928](https://pubmed.ncbi.nlm.nih.gov/42941928/). This is a computational study of one target class. It is not evidence about groundwater or necromass compounds.

The corpus finding is consistent with that general caution but differs in kind. The ENIGMA Carbon Census report found no physicochemical separation between groundwater and necromass compounds, with all contrasts p>0.14. The dark fractions were also nearly identical: 53/59 = 90% for groundwater and 21/24 = 88% for necromass. The report therefore treats darkness as a property of chemical class, not of sampling source. Among the 8 ENIGMA-isolate-callable compounds, however, only 2 are necromass-sourced (terephthalic and phthalic acid), and both are phthalate-class aromatics. Source and class are fully confounded at n=2, so the report declines to run the H3 test. This matches the provenance-confounding literature in spirit. Both decline to read a source contrast as chemistry when the design cannot separate the two. [PMID 42941928](https://pubmed.ncbi.nlm.nih.gov/42941928/) quantified its confounding with predictive models and null models, whereas the corpus relies on direct counts of a small compound set. The corpus result is therefore a descriptive limitation, not a quantified one.

The corpus's own claims have no counterpart in the candidate set. These include the necromass skew among fully orphan compounds (13/24 versus 16/59 groundwater) and the phthalate-class identity of the callable necromass compounds. They are novel to this project and rest on a single report. The other candidates concern slaughterhouse effluent tracing, organofluorine analysis, epidemiology and pharmacology. They do not bear on this question, so I did not use them. The urease paper's approach of conditioning on provenance and testing with matched nulls could inform the open directions. These include adding non-aromatic necromass compounds and groundwater phthalate analogs so that source and class can vary independently. The urease paper is a different domain and does not validate those steps.

## Where source and chemistry do not differ

Source does not predict chemistry or darkness. Groundwater and necromass compounds show no physicochemical separation, with all contrasts p>0.14. [src: enigma_carbon_census_1] The dark fraction is nearly identical across sources: groundwater 53/59 = 90% and necromass 21/24 = 88%. The report concludes that darkness is a chemical-class property, not a sampling-source artifact. [src: enigma_carbon_census_1] It describes the dark map as biased by chemical class, with alkaloids and terpenoids dark and aromatics callable. [src: enigma_carbon_census_1] See [[concepts/resource-darkness-of-compound-catabolism]].

Source does show one skew. The 29 fully orphan compounds, which have no KEGG link, lean toward necromass: 13/24 necromass versus 16/59 groundwater compounds are orphan. [src: enigma_carbon_census_1]

## Where source and class are fully confounded

Among compounds that can be called, source collapses into chemistry. Of the 8 ENIGMA-isolate-callable compounds, only 2 are necromass-sourced (terephthalic and phthalic acid). Both are phthalate-class aromatics with Actinomycetota-heavy utilizers. [src: enigma_carbon_census_1] See [[concepts/taxonomic-distribution-of-aromatic-compound-catabolism]]. The 9th callable compound, lauric acid, is also necromass. It has no ENIGMA-isolate utilizers and no field data, so it adds nothing to the source contrast. [src: enigma_carbon_census_1]

Source is therefore inseparable from chemical class at n=2, and the report finds no honest statistical contrast to run. [src: enigma_carbon_census_1] H3 is untestable with these compounds, because the n=2 necromass callables are fully confounded with phthalate chemistry. The report states this rather than forcing a test. [src: enigma_carbon_census_1]

## Open Directions

- Add necromass-sourced compounds from non-aromatic classes, such as fatty acids and sugars, that have ENIGMA-isolate utilizers. This would break the phthalate confound and allow a source contrast among callable compounds.
- Add groundwater-sourced phthalate-class aromatics or close analogs. Source and class would then vary independently within one chemical class.
- Check whether the necromass skew among orphan compounds (13/24 versus 16/59) reflects annotation coverage or real chemistry. Test it by comparing KEGG linkage across chemical classes.
- Use measured fitness data ([[concepts/measured-fitness-as-independent-evidence-of-carbon-utilization]]) to extend callability beyond the 8 isolate-callable compounds, then rerun the H3 test.
