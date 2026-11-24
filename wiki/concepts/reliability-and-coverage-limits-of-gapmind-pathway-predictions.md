---
type: "Concept"
description: "How far GapMind genome-derived pathway completeness calls can be trusted: database coverage gaps, score-category and scope aggregation, resolution for niche-specific metabolism, and agreement with ModelSEED gapfilling; stops at links to fitness and community chemistry."
sources: ["summaries/annotation_gap_discovery__REPORT.md", "summaries/clay_confined_subsurface__REPORT.md", "summaries/essential_metabolome__REPORT.md", "summaries/functional_dark_matter__REPORT.md", "summaries/fw300_metabolic_consistency__REPORT.md", "summaries/genotype_to_phenotype_enigma__REPORT.md", "summaries/nmdc_community_metabolic_ecology__REPORT.md", "summaries/pathway_capability_dependency__REPORT.md", "summaries/pitfalls.md", "summaries/plant_microbiome_ecotypes__REPORT.md", "summaries/pseudomonas_carbon_ecology__REPORT.md"]
---
# Reliability and coverage limits of GapMind pathway predictions

GapMind pathway-completeness calls partly agree with ModelSEED gapfilling and with matched experiments in one organism. [src: annotation_gap_discovery, fw300_metabolic_consistency] In Pseudomonas, the report says the 62 GapMind carbon pathways may be too coarse for strain-level niche-specific differences, and it proposes aromatic-degradation modules as a possible stronger signal. [src: pseudomonas_carbon_ecology] See [[entities/gapmind]] for the tool.

## Literature Context

The two candidate papers bear only indirectly on the hub's subject, which is how far GapMind pathway-completeness calls can be trusted. Neither evaluates GapMind. Both concern the general problem of inferring metabolism from genomes.

The archaeal fusion/fission screen reports that natural fusions and splits of genes complicate the correct identification and functional annotation of sequences. It says fusion identifications are required for metabolic pathway completeness assessments. It also says that mapping fused to unfused proteins can fill some gaps in metabolic models [PMID 38700364](https://pubmed.ncbi.nlm.nih.gov/38700364/). The screen found more than 1,900 fusion/fission protein clusters. About 25% of the families lack functional annotation in both composite and split states [PMID 38700364](https://pubmed.ncbi.nlm.nih.gov/38700364/). This is a computational screen, validated against experimentally characterized fusion cases. It does not measure GapMind accuracy.

The Mycoplasma suis genome paper is a case study in reading pathways from gene content. The predicted pathway set is concise, and the pentose-phosphate pathway, cofactor and vitamin metabolism, and pyruvate dehydrogenase are missing. From this the authors infer that ribose, NADH, NADPH and coenzyme A are possibly essential for growth [PMID 21573007](https://pubmed.ncbi.nlm.nih.gov/21573007/). The organism has never been cultured, so these are predictions that have not been tested experimentally [PMID 21573007](https://pubmed.ncbi.nlm.nih.gov/21573007/).

The corpus's findings are consistent with these papers on one point. The hub says pathway completeness reflects gene presence, not activity. It says the pathway set misses non-canonical or poorly characterized routes. It also says "Incomplete but Important" pathways (14.9%, 24/161 organism-pathway pairs) may reflect annotation gaps or salvage routes. This agrees with the archaeal paper's point that annotation gaps and unrecognized gene architecture can make pathways look incomplete. It also agrees with the Mycoplasma paper's point that missing pathways are predictions until they are tested in culture. The corpus's other findings are not addressed by either paper and are novel relative to this evidence. These include the absence of E. coli from GapMind, the 13-metabolite agreement in FW300-N2E3, the 0.646 AUC for the ENIGMA baseline, the score-category pitfalls, and the coarseness of 62 carbon pathways in Pseudomonas. The candidate papers give no support or contradiction for any of these.

## Agreement with gapfilling and experiments

GapMind partly corroborates ModelSEED gapfilling, but exact agreement is limited. Of 104 GapMind-gapfill pathway pairings, GapMind partially corroborated the gapfilling results. [src: annotation_gap_discovery] It called pathways incomplete (not_present or steps_missing) for many of the same carbon sources where ModelSEED required gapfilling. [src: annotation_gap_discovery] Exact concordance was limited because the KBase Data Lakehouse data report step counts, not individual step identities. [src: annotation_gap_discovery]

In one organism, FW300-N2E3, all 13 GapMind-matched metabolites had a "complete" prediction and also showed growth in Fitness Browser experiments. [src: fw300_metabolic_consistency] The report reads this as validating GapMind for that organism. [src: fw300_metabolic_consistency] It cites Price et al. (2022) for high accuracy against fitness data. [src: fw300_metabolic_consistency] It also says the 2024 update improved amino acid biosynthesis annotations and that the pangenome-level predictions inherit this accuracy. [src: fw300_metabolic_consistency] This is a single-organism result with 13 metabolites.

In preliminary ENIGMA binary-growth prediction, the GapMind baseline for amino acids and carbon had AUC (area under curve) 0.646, accuracy 78.8% and coverage 24.3%. [src: genotype_to_phenotype_enigma] On 118 testable pairs it reached 96.5% recall and 79% precision. It almost never misses a grower but sometimes predicts growth when the pathway is present but unused. [src: genotype_to_phenotype_enigma] The report treats GapMind and a gradient boosted decision tree (GBDT) model as complementary. [src: genotype_to_phenotype_enigma] See [[concepts/predictability-of-binary-growth-phenotypes-from-gene-content]].

Fitness data can also disagree with GapMind. 14.9% (24/161) of classified organism-pathway pairs are "Incomplete but Important". GapMind scores these as incomplete, yet their mapped genes are fitness-important. [src: pathway_capability_dependency] The report suggests annotation gaps or salvage routes. [src: pathway_capability_dependency] See [[concepts/metabolic-capability-versus-fitness-dependency]].

## Database coverage gaps

GapMind covers about 80 carbon and amino acid pathways, not full metabolism, so many gapfilled reactions fall outside it. [src: annotation_gap_discovery] It does not cover all metabolic functions. [src: functional_dark_matter] About 76% of ENIGMA conditions (metals, antibiotics, nitrogen, stress) have neither GapMind pathway coverage nor carbon source phenotype (CSP) training data. [src: genotype_to_phenotype_enigma]

Organism coverage has gaps too. Escherichia coli genomes are completely absent from GapMind in the KBase pangenome collection. [src: essential_metabolome] E. coli K-12 (Keio), GCF_000005845.2, has 0 predictions. [src: essential_metabolome] The report attributes this to E. coli's exclusion from GTDB pangenome construction, because it has too many genomes for species-level analysis. [src: essential_metabolome] This limited the essential-metabolome analysis to a pilot of 7 organisms, not the intended 45 Fitness Browser (FB) organisms. [src: essential_metabolome] Coverage for the other 38 is unknown. [src: essential_metabolome] The dataset may also miss organisms with divergent metabolic genes. [src: essential_metabolome]

Other stated limits are that predictions are computational, not experimental. [src: essential_metabolome] That analysis used only complete and likely_complete categories and may miss partial pathways. [src: essential_metabolome] Non-canonical or poorly characterized pathways are not detected. [src: essential_metabolome] The essential-gene data come from random barcode transposon sequencing (RB-TnSeq) in rich media. [src: essential_metabolome] Supplementation may make biosynthetic genes look non-essential. [src: essential_metabolome] The report cannot separate essential for biosynthesis from essential for viability. [src: essential_metabolome] See [[concepts/limits-of-transposon-based-essentiality-calls]].

## Scope, score categories and aggregation

Misreading the table has produced wrong results, so the queries need care. GapMind has exactly 80 pathways, with several rows per genome-pathway pair, one per step or component. [src: pitfalls] Its score categories are complete, likely_complete, steps_missing_low, steps_missing_medium and not_present, not a binary present flag. [src: pitfalls] In pangenome_pathway_geography, searching for a nonexistent 'present' category counted exactly 80 pathways per species with 0% present. [src: pitfalls] The fix is to take the best score per genome-pathway pair before aggregating to species. [src: pitfalls] The table is genome-level, and the report specifies MAX(score_simplified) grouped by clade_name and pathway. [src: pitfalls]

With sequence_scope = 'core', score_simplified holds only 0.0 or 1.0, not a continuous confidence. [src: pitfalls] The metabolic_category values are 'aa' and 'carbon'. Filtering on 'amino_acid' returns 0 rows. [src: pitfalls]

Core-level scoring is also stringent. In plant_microbiome_ecotypes it gave 0% completeness across all compartments in broad taxonomic comparisons. [src: pitfalls, plant_microbiome_ecotypes] The report calls the threshold too stringent for genus-level or cross-species comparisons. [src: pitfalls] It recommends genus-level max-aggregation. [src: pitfalls] The core-level threshold remains an open question. [src: plant_microbiome_ecotypes]

Species-level aggregation can be defined differently. In the Pseudomonas carbon analysis, species completeness was the fraction of genomes scoring "complete" or "likely_complete" for each of 62 GapMind carbon pathways. [src: pseudomonas_carbon_ecology] Mean completeness across all species was 0.882. [src: pseudomonas_carbon_ecology] Richness, meaning pathways complete in >50% of genomes, ranged from 27 to 61 with mean = 54.6. [src: pseudomonas_carbon_ecology] The report reads this as substantial interspecific variation in metabolic breadth. [src: pseudomonas_carbon_ecology]

## Resolution for niche-specific metabolism

The pathway set is too coarse for some questions. Complementarity may exist at finer metabolic resolution than 80 pathways can detect. [src: plant_microbiome_ecotypes] The 62 GapMind carbon pathways miss genus-specific capabilities such as toluene, naphthalene and benzoate degradation, which are central to P. putida ecology. [src: pseudomonas_carbon_ecology] The report proposes extending to KEGG modules for these. [src: pseudomonas_carbon_ecology] It hypothesizes that aromatic degradation pathways likely carry stronger environmental signal. [src: pseudomonas_carbon_ecology] See [[concepts/carbon-pathway-profiles-as-predictors-of-environment-and-lifestyle]].

In Pseudomonas, ecology classification accuracy was only moderate. The report attributes this to small class sizes, overlap between environment types such as soil and rhizosphere, and the coarse resolution of 62 GapMind pathways. [src: pseudomonas_carbon_ecology] It also says the 62 pathways may be too coarse for strain-level niche-specific differences within environmental species. [src: pseudomonas_carbon_ecology] This fits Guo et al. (2026), as the report cites them: hydrocarbon degradation genes concentrate in the accessory genome and vary at strain rather than species level. [src: pseudomonas_carbon_ecology] The report's use of standardized GapMind predictions, not KEGG-based annotations, is presented as an extension of earlier ecological-differentiation findings. [src: pseudomonas_carbon_ecology] It proposes analyzing within-species pathway variation to seek metabolic ecotypes, meaning subpopulations adapted to different niches. [src: pseudomonas_carbon_ecology] See [[concepts/within-species-metabolic-ecotypes-from-pathway-variation]].

Resolution is limited at the top end as well. The 18-pathway amino-acid universe saturates near 18 for most cultivable bacteria. [src: clay_confined_subsurface] Most cultured organisms, deep or shallow, reach 17–18/18, which leaves little room for a positive signal. [src: clay_confined_subsurface]

In the functional dark matter analysis, GapMind pairs are organism-level co-occurrences of nearly-complete pathways and dark genes. No direct gene-to-gap enzymatic matching was done. [src: functional_dark_matter] Dark genes with signaling, regulatory or structural roles are not captured. [src: functional_dark_matter]

## Links to fitness and community chemistry

Pathway completeness measures gene presence, not active expression. Transcriptomics would be needed to test whether expressed biosynthesis tracks metabolite pools more closely. [src: nmdc_community_metabolic_ecology] See [[concepts/genome-predicted-pathway-completeness-and-community-metabolite-chemistry]].

## Remedies proposed by the essential-metabolome report

To get past the coverage gap, the report proposes adding more FB organisms to raise the sample size. [src: essential_metabolome] It also proposes eggNOG pathway analysis, using EC (Enzyme Commission) annotations mapped to KEGG pathways for all 45 FB organisms, including E. coli. [src: essential_metabolome] It suggests combining pathway-level GapMind with gene-level eggNOG. [src: essential_metabolome] It also suggests mapping essential genes directly to pathways instead of relying on GapMind. [src: essential_metabolome] It lists open questions: whether complete pathways are actually essential for viability [src: essential_metabolome], which pathways are essential only under specific growth conditions [src: essential_metabolome], and whether pathway gaps cluster by phylogeny or ecology. [src: essential_metabolome]

## Open Directions

- Rerun the essential-metabolome analysis with E. coli included, using the eggNOG route for all 45 Fitness Browser organisms. Compare it with GapMind on the 7 covered organisms. This would close the coverage gap.
- Test a hybrid of pathway-level GapMind and gene-level eggNOG, and direct essential-gene-to-pathway mapping.
- Add aromatic-degradation KEGG modules to the Pseudomonas carbon analysis. This would test whether niche-specific signal is hidden by GapMind's 62 carbon pathways.
- Analyze within-Pseudomonas-species pathway variation, at strain level where possible. This would test whether metabolic ecotypes exist that species-level completeness hides.
- Compare genus-level max-aggregation with core-level scoring across plant compartments. This would settle the core-level threshold question.
- Resolve the "Incomplete but Important" pathways with step-level calls. This would separate annotation gaps from salvage routes.
- Test whether pathway gaps cluster by phylogeny or ecology, using species-level best-score aggregation.
