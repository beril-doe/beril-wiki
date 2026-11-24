---
type: "Concept"
description: "How phage-host infection data and pathogen genome annotations bear on whether receptors or defense systems limit infection and what that means for phage therapy; stops at the report's datasets (E. coli panel, four PhageFoundry pathogens)."
sources: ["summaries/discoveries.md", "summaries/snipe_defense_system__REPORT.md"]
---
# Adsorption receptors versus defense systems as determinants of phage host range

How phage-host infection data and pathogen genome annotations bear on whether receptors or defense systems limit infection and what that means for phage therapy; stops at the report's datasets (E. coli panel, four PhageFoundry pathogens).

## Literature Context

The candidate papers largely agree that surface receptors are a first and major determinant of phage host range, with defense systems acting as an additional layer. In 20 Salmonella isolates challenged with 52 wild phages (more than 1,000 interactions), receptor identity and surface phase variation explained about 67% of susceptibility patterns, so cell-surface architecture was the major determinant [PMID 42849435](https://pubmed.ncbi.nlm.nih.gov/42849435/). The same study found a prophage-encoded defense factor, AppA, that blocks phage DNA packaging among resistance phenotypes that surface features did not explain [PMID 42849435](https://pubmed.ncbi.nlm.nih.gov/42849435/). Receptor masking is also documented. In Pseudomonas aeruginosa, glycosylation of type IV pili protects against certain pilus-specific phages by blocking adsorption, and specific phage tail proteins can overcome it [PMID 29133883](https://pubmed.ncbi.nlm.nih.gov/29133883/). In the E. coli–phage λ model system, quorum-sensing signals (AHLs) reduce λ receptor numbers, which gives a 2-fold reduction in the adsorption rate. The abstract describes this as a proof-of-principle study [PMID 23422409](https://pubmed.ncbi.nlm.nih.gov/23422409/).

Defense systems also matter. In a panel of P. aeruginosa clinical isolates with host range data for 70 phages, strains with more antiphage systems, predicted with PADLOC, tended to be more phage resistant. The study calls this a correlation and not a demonstration of causation [PMID 38338703](https://pubmed.ncbi.nlm.nih.gov/38338703/). Synthetic Klebsiella phages with swapped genomic scaffolds replicated better on some strains than wild-type phages. The authors suggest, presumably, that this reflects evasion of host anti-phage defenses, while capsular specificity followed the tailspike protein [PMID 40725069](https://pubmed.ncbi.nlm.nih.gov/40725069/). A review of phage engineering lists receptor modification and activation of antiviral defense systems as complicating phage therapy [PMID 40216545](https://pubmed.ncbi.nlm.nih.gov/40216545/).

The corpus's reading of the E. coli panel (188 strains, 96 phages) is consistent with this literature. It reports that adsorption factors outweigh defense systems, and it links lambda's 0.5% infection rate to ManYZ variation or loss. The Salmonella result [PMID 42849435](https://pubmed.ncbi.nlm.nih.gov/42849435/) and the λ receptor work [PMID 23422409](https://pubmed.ncbi.nlm.nih.gov/23422409/) support the receptor emphasis. The ManYZ link remains an interpretation in the corpus and was not tested here.

The corpus's Klebsiella SNIPE proposal extends this literature without confirming it. The finding is one DUF4041 description covering 3 proteins of 558 aa in Klebsiella, and it rests on annotation counts alone. The Pseudomonas correlation [PMID 38338703](https://pubmed.ncbi.nlm.nih.gov/38338703/) and the Klebsiella scaffold result [PMID 40725069](https://pubmed.ncbi.nlm.nih.gov/40725069/) make a therapy-relevant role for defense genes plausible. None of the candidate papers examines SNIPE or ManYZ-linked defense, so that specific hypothesis is novel. The apparent tension in the hub, between receptor primacy and a defense system affecting therapy, is softened by the Salmonella finding. There, receptors explained about 67% of susceptibility and a defense factor accounted for part of the remainder [PMID 42849435](https://pubmed.ncbi.nlm.nih.gov/42849435/).

## The E. coli infection panel

The phagefoundry_strain_modelling database holds the Gaborieau et al. 2024 dataset. It covers 188 E. coli strains (ECOR collection, NILS collection, clinical/environmental isolates) and 96 phages (41 Podoviridae, 32 Myoviridae, 23 Siphoviridae). That gives 17,672 binary infection outcomes. [src: discoveries, snipe_defense_system] The overall infection rate is 22% (3,929 positive / 13,743 negative). [src: snipe_defense_system] A machine-learning model on this data reached AUC (area under curve) = 0.883 and accuracy of 84.3%. It used 1,582 gene cluster presence/absence features with SHAP (Shapley additive explanations) importance scores. [src: discoveries, snipe_defense_system]

The report states that the paper's key conclusion is that adsorption factors (surface receptors) are the primary predictors of phage-host interaction, not antiphage defense systems. [src: snipe_defense_system]

## Infection rates by phage family

| Family | Infection rate | Report's interpretation |
|---|---|---|
| Myoviridae | 43.4% (2,531/5,828) | Broad host range (tail fibers, not ManYZ-dependent) [src: snipe_defense_system] |
| Podoviridae | 13.0% (978/7,520) | Moderate host range [src: snipe_defense_system] |
| Siphoviridae | 9.7% (420/4,324) | Narrow host range [src: snipe_defense_system] |

Lambdavirus 411_P1 (phage lambda) infects only 1 of 188 strains (NILS06). Its 0.5% infection rate is the lowest of any phage in the dataset. [src: snipe_defense_system, discoveries] The report calls this consistent with widespread ManYZ variation/loss conferring near-universal lambda resistance. [src: snipe_defense_system, discoveries] ManYZ is the mannose transporter that lambda uses for DNA (deoxyribonucleic acid) injection. [src: discoveries] See [[entities/bacteriophage-lambda]] and [[entities/manxyz-mannose-phosphotransferase-system]].

## Defense system and transporter annotations in PhageFoundry pathogens

Searches of four PhageFoundry pathogens found SNIPE's DUF4041 domain only in Klebsiella. Generic nuclease and restriction hits were common in all four. [src: snipe_defense_system]

| Pathogen | DUF4041 | GIY-YIG | Nuclease | Restriction | Abortive infection |
|---|---|---|---|---|---|
| Klebsiella | 1 | 1 | 98 | 42 | 2 [src: snipe_defense_system] |
| Acinetobacter | 0 | 3 | 91 | 33 | 2 [src: snipe_defense_system] |
| P. aeruginosa | 0 | 2 | 125 | 54 | 2 [src: snipe_defense_system] |
| P. viridiflava | 0 | 0 | 90 | 41 | 1 [src: snipe_defense_system] |

Klebsiella's DUF4041 hit is 1 description covering 3 proteins of 558 aa each. The other three species have none. [src: snipe_defense_system] The three proteins (JJW41_17025, KFB13_RS08150, KFB31_RS01490) match the length of the characterized E. coli SNIPE protein A0A0A1A5Z2. The report says this strongly suggests full-length two-domain (PF13250 + PF13455) SNIPE proteins. [src: snipe_defense_system] SNIPE is described on [[entities/snipe]].

Klebsiella also carries mannose transporter components. It has 28 proteins with mannose PTS IID (ManZ) eggNOG annotations and 1 with a mannose PTS IIA (ManX) eggNOG annotation. [src: snipe_defense_system] PF02378 / PTS_EIIC (ManY family) Pfam annotations number 4,619 in Klebsiella, 891 in Acinetobacter, 1,067 in P. aeruginosa and 260 in P. viridiflava. [src: snipe_defense_system] PF00358 / PTS_EIIA_1 (ManX family) annotations number 571 in Klebsiella and 0 in the other three. [src: snipe_defense_system] Klebsiella is the only PhageFoundry species with both SNIPE and the PF00358 domain by exact Pfam accession. [src: snipe_defense_system]

The report reads this co-occurrence as consistent with SNIPE defending ManYZ pores that provide a phage entry route. [src: snipe_defense_system] It also says the paper's receptor conclusion supports SNIPE's niche. In the report's account, SNIPE targets the adsorption/injection step by cleaving DNA during ManYZ transit. [src: snipe_defense_system] This is an interpretation of annotation counts, not a measurement of function. [src: snipe_defense_system]

## Implications for phage therapy

The report proposes that SNIPE could affect phage therapy efficacy in Klebsiella, a key phage therapy target. This is a hypothesis resting on DUF4041 detection. [src: discoveries, snipe_defense_system] See [[entities/klebsiella]] and [[entities/klebsiella-pneumoniae]].

## Tensions

- The report says the E. coli paper identifies surface receptors, not antiphage defense systems, as the primary predictors of infection. [src: snipe_defense_system] The same report proposes that a defense system, SNIPE, could affect phage therapy efficacy in Klebsiella. [src: snipe_defense_system] The report's own argument is that SNIPE operates at the adsorption/injection step, during ManYZ transit. [src: snipe_defense_system] The claims give no direct test of that argument.

## Limits

PhageFoundry gives genome annotations only, in GenomeDepot format, with no fitness/TnSeq (transposon sequencing) tables. This analysis therefore has no Klebsiella-specific SNIPE or ManYZ fitness data. [src: snipe_defense_system] Generating such data would require new mutant libraries in natural SNIPE carriers such as K. pneumoniae NCTC9140 or HS11286. [src: snipe_defense_system] Related: [[concepts/fitness-data-coverage-gaps-for-defense-genes]], [[concepts/phage-resistance-versus-metabolic-cost-trade-off-at-receptor-transporters]], [[entities/phagefoundry]].

## Open Directions

- Test whether ManYZ gene presence or loss predicts lambda infection of the 188 E. coli strains. This would turn the 0.5% infection rate from an interpretation into a tested link.
- Check whether SNIPE-like genes occur in the E. coli panel and whether they predict infection beyond receptor features. The SHAP importances for the 1,582 gene cluster features would show this. It would address whether defense systems add predictive power.
- Build transposon libraries in K. pneumoniae NCTC9140 or HS11286 and screen for phage susceptibility. This would close the Klebsiella fitness gap.
- Pair Klebsiella phage infection data with the genomes' DUF4041 status, to test whether SNIPE carriage changes therapy outcomes.
