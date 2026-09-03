<!-- tension-hash: db8d8c2189132c0c -->
# Callability, Darkness, and the Limits of Ecological Inference

The disagreement is whether apparent structure among callable or environmentally associated compounds reflects genuine chemical and ecological patterns, or instead the uneven coverage of databases, literature, genomes, and reaction-extraction methods. As described on [[concepts/callability-limited-comparative-inference]], the evidence supports several competing interpretations without decisively selecting among them: callable compounds may be concentrated in simpler classes, dark compounds may be biologically or computationally inaccessible, environmental occurrence may not demonstrate function, and null ecological contrasts may partly reflect callability limitations.

## Evidence Sides

**Chemical-class concentration versus formal statistical support**

The census showed a directional concentration of callable compounds in simpler, commonly represented chemical classes, suggesting an annotation-coverage hypothesis. [src: enigma_carbon_census_1] However, H1 was not formally supported by the chi-square test, so the result does not establish a true chemical-class gradient. [src: enigma_carbon_census_1]

**Biological darkness versus database darkness**

The 29 fully orphan compounds were not linkable through the queried resources, supporting a resource-limited discovery frontier. [src: enigma_carbon_census_1] At the same time, “organism-dark” does not mean unknown to science because the literature screen was shallow. [src: enigma_carbon_census_1] The 74-compound dark set therefore leaves unresolved whether darkness reflects absent biology, absent annotations, absent literature retrieval, or an overly restrictive reaction filter. [src: enigma_carbon_census_1]

**Environmental presence versus functional evidence**

The atlas provides occurrence and abundance data for implicated genera across an 86-genera, 3825-NMDC-metagenome, and 302-Planet-Microbe-run scope. [src: enigma_carbon_census_1] This environmental presence can prioritize enrichment sources, but it does not provide compound-resolved catabolic activity or establish that observed organisms consume a particular dark compound. [src: enigma_carbon_census_1]

**Within-method ecological null versus method-limited signal**

The ecotype reanalysis found no stronger environment–gene-content association among environmental species despite confirming clinical sampling bias, with U=1536 and p=0.83 for Environmental > Human-associated. [src: ecotype_env_reanalysis] This supports the within-method null comparison. [src: ecotype_env_reanalysis] Yet environmental species had a higher NaN rate, 21%, than human-associated species, 7%, and the extraction methodology produced a 27x difference in overall median correlation relative to the original analysis. [src: ecotype_env_reanalysis] These results leave unresolved how much ecological signal is lost through species-level filtering, genome-count imbalance, and extraction choices. [src: ecotype_env_reanalysis]

## Possible Reconciliations

- **Hypothesis — coverage gradient:** Callable compounds may genuinely be concentrated in simpler chemical classes while the chi-square test lacks sufficient power or is affected by annotation coverage.
- **Hypothesis — layered darkness:** Some of the 74-compound dark set may lack known biology, while other compounds are missed because databases, literature retrieval, or reaction filters are incomplete.
- **Hypothesis — occurrence without demonstrated function:** The 86-genera, 3825-NMDC-metagenome, and 302-Planet-Microbe-run atlas may identify plausible sources without proving compound-specific metabolism.
- **Hypothesis — null attenuated by extraction:** The U=1536 and p=0.83 result may be valid within the reanalysis method while species-level filtering, NaN rates, genome-count imbalance, or extraction choices obscure an ecological association.

## Resolving Work

- Re-run the chemical-class analysis with expanded annotation databases and coverage-matched null models; test whether the directional concentration and H1 support persist after representation bias is controlled.
- Perform a deeper literature and database search for all 29 fully orphan compounds and the broader 74-compound dark set; distinguish absent biology from absent retrieval or overly restrictive reaction filtering.
- Pair the atlas with compound-resolved metagenomics, metatranscriptomics, metabolomics, and enrichment cultures; test whether implicated organisms consume particular dark compounds.
- Reanalyze ecological associations using genome-count-balanced samples, explicit missingness models for the 21% versus 7% NaN rates, and multiple extraction pipelines; test whether the U=1536 and p=0.83 null is method-robust.
- Compare the reanalysis with the original workflow while auditing the source of the 27x difference in overall median correlation; identify which processing choices alter the ecological conclusion.
