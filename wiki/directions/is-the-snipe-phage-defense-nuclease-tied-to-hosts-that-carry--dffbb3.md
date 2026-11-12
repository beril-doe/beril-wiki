---
type: "Research direction"
description: "Do species carrying SNIPE-family DUF4041 proteins also carry ManYZ-type transporters more often than expected from relatedness, and does a SNIPE host's susceptibility to phages depend on its ManYZ?"
hypothesis: "SNIPE-family hosts carry ManYZ-type transporters more often than relatedness predicts, and deleting manYZ in a SNIPE-carrying strain changes its phage susceptibility."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "Co-occurrence and E. coli susceptibility analyses use catalog tables, but Klebsiella-specific fitness was unmeasured and deletion mutants in SNIPE-carrying strains must be built."
databases: ["kbase.ke_pangenome", "phagefoundry.klebsiella_genome_browser", "phagefoundry.phage_host_interactions"]
tables: ["kbase.ke_pangenome.bakta_pfam_domains", "kbase.ke_pangenome.eggnog_mapper_annotations", "phagefoundry.phage_host_interactions.strainmodelling_interaction", "phagefoundry.phage_host_interactions.strainmodelling_genome", "phagefoundry.klebsiella_genome_browser.browser_gene"]
findings: ["snipe_defense_system--5727ec31", "snipe_defense_system--69396dc3", "snipe_defense_system--792b9ec1"]
conflicts: []
papers: ["41741653", "34032565", "25968644"]
builds_on: ["findings/snipe_defense_system--5727ec31", "findings/snipe_defense_system--69396dc3", "findings/snipe_defense_system--792b9ec1"]
projects: ["snipe_defense_system"]
topics: ["data-infrastructure-provenance-and-research-practice"]
---
# Is the SNIPE phage-defense nuclease tied to hosts that carry the ManYZ phage-entry transporter?

Do species carrying SNIPE-family DUF4041 proteins also carry ManYZ-type transporters more often than expected from relatedness, and does a SNIPE host's susceptibility to phages depend on its ManYZ?

## Hypothesis

SNIPE-family hosts carry ManYZ-type transporters more often than relatedness predicts, and deleting manYZ in a SNIPE-carrying strain changes its phage susceptibility.

## Why it matters

The DUF4041 domain was found in 4,572 gene clusters across 1,696 species, but an estimated 80.4% of clusters are SNIPE-family proteins, so the rest may be other proteins or annotation noise. A link between a defense and the host entry route it guards would show how defenses coevolve with the proteins phages exploit and would help predict which strains phage therapy can reach.

## How to test it

Across the pangenome, test co-occurrence of DUF4041 clusters, restricted to those with additional SNIPE-family features where available, with ManYZ-type transporter clusters within genera. In E. coli, where phage susceptibility calls exist, ask whether strains with SNIPE and ManYZ differ in susceptibility from strains lacking either. In Klebsiella, where the catalog shows annotations but no fitness data, build deletion mutants of manYZ in a SNIPE-carrying strain such as NCTC9140 or HS11286 and challenge them with phages.

## What would support or refute it

Support: co-occurrence exceeds lineage expectation and manYZ loss shifts phage susceptibility in the SNIPE strain. Refute: co-occurrence matches relatedness and the deletion leaves infection unchanged.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. Co-occurrence and E. coli susceptibility analyses use catalog tables, but Klebsiella-specific fitness was unmeasured and deletion mutants in SNIPE-carrying strains must be built.

## Builds on

- Finding: [[findings/snipe_defense_system--5727ec31|DUF4041 SNIPE domain is far more widespread than originally reported]] (Insufficient literature evidence)
- Finding: [[findings/snipe_defense_system--69396dc3|E. coli K-12 ManXYZ genes show severe fitness defects in few conditions]] (Insufficient literature evidence)
- Finding: [[findings/snipe_defense_system--792b9ec1|PhageFoundry has no Klebsiella fitness tables to test SNIPE–ManYZ interplay]] (Insufficient literature evidence)

## Closest published work

- [PMID 41741653](https://pubmed.ncbi.nlm.nih.gov/41741653/) A membrane-bound nuclease directly cleaves phage DNA during genome injection.
- [PMID 34032565](https://pubmed.ncbi.nlm.nih.gov/34032565/) Sustained coevolution of phage Lambda and Escherichia coli involves inner- as well as outer-membrane defences and counter-defences.
- [PMID 25968644](https://pubmed.ncbi.nlm.nih.gov/25968644/) Rapid quantification of mutant fitness in diverse bacteria by sequencing randomly bar-coded transposons.

PMID 41741653 shows a membrane-bound nuclease cleaving phage DNA during injection and PMID 34032565 shows membrane defenses and counter-defenses in E. coli; neither tests co-occurrence across species or the role of ManYZ in Klebsiella.
