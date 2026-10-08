---
type: "Concept"
description: "Carbon compounds in the ENIGMA carbon census whose utilization the queried resources cannot link to any organism, how they are stratified by why they are dark, and the proposed routes to making them callable."
sources: ["summaries/enigma_carbon_census_1__REPORT.md"]
---
# Organism-Dark Compounds: Compounds Not Linked to a Degrading Organism in Queried Resources

In the ENIGMA carbon census ([[summaries/enigma_carbon_census_1__REPORT]]), the report calls 74/83 (89%) of the census compounds "organism-dark". For these compounds, the genetic determinants of utilization could not be linked through the queried the KBase Data Lakehouse and curated resources. The report explicitly calls this *resource-darkness*, not proof of absence from science. It notes that class-level catabolic literature exists for several of these compounds (e.g. monoterpenes, nicotine). The project's literature-rescue channel returned zero only because it used a shallow PubMed-title screen, which the report treats as a method floor rather than evidence of absence. This page treats organism-dark compounds as a compound-side counterpart to the gene-level darkness in [[concepts/experimental-prioritization-of-functional-dark-matter]]: that page asks which proteins lack a known function, and this one asks which substrates lack a linkable consumer. All the evidence comes from a single project, so the framing is provisional. [src: enigma_carbon_census_1]

## Scale and Stratification

The report ranks the 74 organism-dark compounds by *why* they are dark (NB09 Part 4). Its hardest stratum is 29 fully orphan compounds with no [[entities/kegg]] linkage (KEGG, the Kyoto Encyclopedia of Genes and Genomes pathway database). The report proposes starting this stratum, especially its necromass-heavy alkaloids and terpenoids, with anonymous community enrichment plus metagenomics, meaning sequencing of the whole enriched community rather than isolates. This is a proposed discovery-mode direction. The report does not show a utilization result for any of these compounds, and it does not show that existing literature cannot resolve them. [src: enigma_carbon_census_1]

## Biosynthesis-Known Subset

The report sets aside six organism-dark compounds whose biosynthesis is already known: Tyramine, guanidineacetic acid, cinnamic acid, caffeic acid, palmitic acid and farnesol. It proposes a separate MIBiG/biosynthetic-literature consult for them before any wet-lab effort is committed (MIBiG is the Minimum Information about a Biosynthetic Gene cluster repository). The purpose of the consult is to use existing knowledge before spending wet-lab effort. A consult like this could find a linkage that was missed, but if it finds none, that would not show that no organism degrades these compounds. [src: enigma_carbon_census_1]

## Literature-Mining Route to Callability

The report proposes a second route. It would mine [[entities/kescience-paperblast]] and [[entities/kescience-pubmed]] for alkaloid and terpenoid catabolic enzymes, then search those enzymes back into the genomes. The report says this could convert some dark compounds to callable without new experiments. No conversion has been demonstrated, so how much of the darkness is a resource or annotation artefact remains a hypothesis, not a measured yield. [src: enigma_carbon_census_1]

## Relation to Gene-Level Darkness

The triage resembles how gene-level dark matter is handled elsewhere in this wiki. Some cases are routed to new experiments, and others are routed to existing literature or homology searches, which links this topic to [[concepts/evidence-triangulation-for-functional-annotation]] and [[concepts/homology-search-negative-evidence]]. In both settings, a failure to link through queried resources is negative evidence that depends on the method used. It does not establish absence. This page records the parallel as an interpretation of a single project's triage, not as an established cross-project finding. [src: enigma_carbon_census_1]

## Open Directions

- Run the proposed PaperBLAST/PubMed mining for alkaloid and terpenoid catabolic enzymes, using full-text or enzyme-level searches rather than a title screen. Search the hits back into the genomes and report how many organism-dark compounds become callable. This would turn the literature-mining hypothesis into a measured conversion rate. [src: enigma_carbon_census_1]
- Complete the MIBiG/biosynthetic-literature consult for the six biosynthesis-known compounds before wet-lab work. This would test whether existing literature supplies a degrader linkage that the queried resources missed. [src: enigma_carbon_census_1]
- Apply anonymous community enrichment with metagenomics to the fully orphan, necromass-heavy alkaloids and terpenoids. Growth on a compound would only be a starting point. Linking utilization to specific organisms or genes would need further evidence, such as the compound's depletion and analysis of the enriched metagenome. [src: enigma_carbon_census_1]
