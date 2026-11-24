---
type: "Concept"
description: "How predicted or enriched aromatic and phthalate degraders cluster in clades such as Burkholderiales, and whether versatility is a clade trait; inferred from genomes and taxonomy only."
sources: ["summaries/enigma_carbon_census_1__REPORT.md", "summaries/lignin_community_enrichment__REPORT.md"]
---
# Taxonomic distribution of aromatic-compound catabolism

Predicted catabolic capacity for aromatic compounds, including phthalate-class aromatics, clusters in particular clades, mainly [[entities/burkholderiales]]. The evidence is genome-based prediction from the ENIGMA Carbon Census, plus 16S community enrichment in a lignin project. The clade pattern is an inference from genomes and taxonomy. [src: enigma_carbon_census_1]

## Burkholderiales concentration and versatility as a clade trait

Callable catabolic capacity in the ENIGMA census is phylogenetically concentrated in Burkholderiales. It is a specialist trait: 675 genomes have a single capacity, and only 18 are generalists with at least 3 capacities. [src: enigma_carbon_census_1] High-versatility genera cluster in the order Polaromonas, Alcaligenes, Burkholderia, Paraburkholderia, Comamonas, Hydrogenophaga. [src: enigma_carbon_census_1]

Generalist genome chassis fall in Paraburkholderia (5), Burkholderia (4) and Hydrogenophaga (2), plus scattered Burkholderiaceae. [src: enigma_carbon_census_1] The report says this is the same clade that dominates the versatility ranking. It reads this as versatility being a clade trait, not a widely portable module. [src: enigma_carbon_census_1]

Predicted ENIGMA isolate utilizers also concentrate in Pseudomonadota/Burkholderiales. Pseudomonadales and Sphingomonadales add to specific compounds, for example 47 Sphingomonadales strains for 4-hydroxybenzaldehyde. [src: enigma_carbon_census_1] The isolate deliverable has 494 strain placements on [[entities/gtdb]] taxonomy, covering 359 distinct strains. Of these, 64 are high-certainty gene-complete-pathway Tier 2, 387 are medium Tier 2 pathway, and 43 are medium Tier 3 signature-enzyme placements. [src: enigma_carbon_census_1]

## Compound-specific clade specialization

Per-clade conservation shows compound-specific specialization, not a shared generalist toolkit. [src: enigma_carbon_census_1] This **refines** the Burkholderiales picture: the clade is versatile overall, but individual genera hold different compounds.

The fractions below are denominated over depot genomes that already carry some catabolic call. They describe specialization within the called set, not absolute genus prevalence. [src: enigma_carbon_census_1]

- Castellaniella and Hylemonella carry 3-hydroxybenzoic-acid capacity in ~100% of such genomes. [src: enigma_carbon_census_1]
- Novosphingobium and Sphingobium carry 4-hydroxybenzaldehyde capacity at ~92–100%. [src: enigma_carbon_census_1]
- Paenarthrobacter carries phthalic-acid capacity at 100%. [src: enigma_carbon_census_1]
- Comamonas carries 3-hydroxybenzoate capacity at 92% and 4-hydroxybenzaldehyde capacity at 85%. [src: enigma_carbon_census_1]

Capacity breadth across the chassis is led by 3-hydroxybenzoic acid (296 genomes, 53 genera) and salicylic acid (197 genomes, 28 genera). Abscisic acid is a 2-genome edge case. [src: enigma_carbon_census_1]

## Phthalate and terephthalate degraders

The literature support for Burkholderiales/Comamonadaceae dominance is strongest for phthalate/terephthalate catabolism, which matches the versatility ranking. [src: enigma_carbon_census_1] The report calls this the best-characterized necromass aromatic catabolism in the census. [src: enigma_carbon_census_1] Terephthalate goes via terephthalate dioxygenase to protocatechuate. Its degraders concentrate in Pseudomonadota (Ideonella/Comamonas) and in actinobacterial degraders. [src: enigma_carbon_census_1]

Only 2 of the 8 ENIGMA-isolate-callable compounds are necromass-sourced, terephthalic and phthalic acid. Both are phthalate-class aromatics with Actinomycetota-heavy utilizers. [src: enigma_carbon_census_1] This limits the Burkholderiales story for these compounds. See [[concepts/confounding-of-compound-source-with-chemical-class]].

## Lignin enrichment: which aromatic degraders rise

Lignin enrichment of communities (16S) gives a partly overlapping picture. Comamonas is described as an aromatic-compound degrader and is enriched in L (CLR effect -6.8) in the L-versus-LC comparison. CLR is centered log-ratio. [src: lignin_community_enrichment] Comamonas is 0.1% in base and 17–51x enriched in Round 2 groups (3.6–5.1%). [src: lignin_community_enrichment] It is known for degrading aromatic compounds including phenylpropanoids. [src: lignin_community_enrichment] The report ties later-passage Comamonas enrichment to Kanokratana et al. (2018, PMID: 29169786), who found Comamonas a major genus in Napier-grass lignocellulose-degrading consortia. PMID is PubMed identifier. [src: lignin_community_enrichment]

Other genera also rise under lignin enrichment:
- In Base versus Lignin, Acinetobacter rose from <0.1% to 17.0% (CLR +12.3). Pseudomonas rose from <0.1% to 7.5% (CLR +11.5). Flavobacterium rose from <0.1% to 9.0% (CLR +11.2). [src: lignin_community_enrichment]
- Round 2 groups with lignin history (L-L, L-LC) are Pseudomonas-dominated (52–53%) with low Acinetobacter (<1–20%). [src: lignin_community_enrichment] The report links Pseudomonas and Acinetobacter dominance to Hossain et al. (2024), who found these genera had the highest diversity of aromatic-degrading enzymes across 26 soil bacterial genomes. [src: lignin_community_enrichment] [[entities/pseudomonas]] is known for the [[entities/ketoadipate-pathway]] and protocatechuate catabolism. [src: lignin_community_enrichment]
- Flavobacterium is 0.1% in base and 14.1% in lignin-only L (CLR +11.2, Base vs L). [src: lignin_community_enrichment] Its species have documented aromatic degradation roles, and several strains carry ring-hydroxylating dioxygenases and come from PAH-contaminated environments (Lyu et al. 2014, PMID: 24957593). [src: lignin_community_enrichment]
- Aminobacter is absent in base and Round 1 but appears in Round 2 L-L (7.6%) and LC-L (6.4%). It is described as known for aromatic amine metabolism. [src: lignin_community_enrichment]
- Rhodococcus, a well-characterized lignin degrader, is at 0.03–0.67% across conditions and highest in L (0.67%). [src: lignin_community_enrichment]
- Sphingomonas is higher in base (1.74%) than in enriched conditions. This suggests lignin enrichment does not select it despite its known aromatic catabolism. [src: lignin_community_enrichment] See [[entities/sphingomonas]].
- Peredibacter, described as a bacterial predator, was enriched in L (CLR -7.3). [src: lignin_community_enrichment]

## Proposed follow-up in the lignin report

The lignin report proposes mapping the enriched Pseudomonas, Acinetobacter and Comamonas to [[entities/kbase-ke-pangenome]] for lignin-degradation gene annotations and aromatic catabolism pathway presence. [src: lignin_community_enrichment] It also proposes PICRUSt2 or Tax4Fun functional prediction from 16S data to test enrichment of the beta-ketoadipate and protocatechuate pathways. [src: lignin_community_enrichment]

## Tensions

- The census calls versatility a Burkholderiales clade trait. [src: enigma_carbon_census_1] Lignin enrichment raised Pseudomonas, Acinetobacter and Flavobacterium strongly. [src: lignin_community_enrichment] The two datasets measure different things (genome-called capacity versus 16S abundance), so they are not directly comparable.
- Sphingomonads carry 4-hydroxybenzaldehyde capacity at ~92–100% of called genomes [src: enigma_carbon_census_1], yet Sphingomonas was not selected by lignin enrichment. [src: lignin_community_enrichment] The denominators differ, so this is a contrast and not a contradiction. [src: enigma_carbon_census_1]

## Open Directions

- Run the pangenome mapping and the PICRUSt2 or Tax4Fun prediction proposed above. They would test whether lignin enrichment matches genome-encoded aromatic capacity.
- Recompute per-clade conservation over all genomes of each genus, not only genomes with a catabolic call, to get absolute prevalence. This addresses the denominator limit.
- Test whether Actinomycetota-heavy phthalate-class utilizers separate from Burkholderiales once compound source is controlled. This addresses the source-versus-class confound.

See also [[concepts/co-occurrence-and-modularity-of-catabolic-capacities-across-genomes]], [[summaries/enigma_carbon_census_1__REPORT]] and [[summaries/lignin_community_enrichment__REPORT]].
