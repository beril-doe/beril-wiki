---
type: "Concept"
description: "What literature, experimental host-range and in-vivo viromic evidence exists for phages against Crohn's-disease-associated pathobionts, how a cocktail is designed from it for E. coli, and where coverage gaps remain; stops at per-patient assignment."
sources: ["summaries/ibd_phage_targeting__REPORT.md"]
---
# Phage availability for gut pathobionts and the gut-anaerobe phage gap

Phage availability for Crohn's-disease-associated pathobionts is uneven. Evidence from one project (ibd_phage_targeting) supports a concrete 5-phage cocktail for E. coli, while the anaerobic pathobionts have little or no usable phage evidence. The evidence has three layers: curated literature, experimental host-range data and in-vivo viromics. The report treats all three as necessary and none as sufficient. [src: ibd_phage_targeting] See also [[summaries/ibd_phage_targeting__REPORT]].

## Three evidence layers

The project stacks three notebooks for the 6 actionable Tier-A core pathobionts: NB12 (curated literature), NB13 (experimental susceptibility) and NB14 (in-vivo phageome). [src: ibd_phage_targeting] NB12 scores 12 organisms for phage availability on a 0-3 scale from ref_phage_biology, a literature-curated synthesis. [src: ibd_phage_targeting] The report says the convergence across layers rests on directional concordance, not matched effect sizes. [src: ibd_phage_targeting]

## Literature classes among the actionable pathobionts

The 6 actionable species fall into four classes. [src: ibd_phage_targeting]

| Class | Species | Evidence |
|---|---|---|
| 3, clinical | E. coli | EcoActive precedent [src: ibd_phage_targeting] |
| 2, lytic literature | E. lenta, E. bolteae | PMBT5 and PMBT24 [src: ibd_phage_targeting] |
| 1, temperate-limited | M. gnavus | 6 temperate phages [src: ibd_phage_targeting] |
| 0, gap | H. hathewayi, F. plautii | none [src: ibd_phage_targeting] |

Three of the six therefore have no lytic phage in the KBase Data Lakehouse ref_phage_biology curation. [src: ibd_phage_targeting] The 2 gap species also have the highest NB05 scores, 4.0 and 3.3. [src: ibd_phage_targeting]

## Experimental host range and the E. coli cocktail

The PhageFoundry dataset (see [[entities/phagefoundry]]) holds 96 phages × 188 E. coli strains × 17,672 experimentally tested susceptibility pairs, from Gaborieau 2025-10-02. [src: ibd_phage_targeting] It shows a 22 % susceptibility rate. [src: ibd_phage_targeting] Of 94 phages, 65 (69 %) were isolated against B2/D phylogroup hosts, described as predominantly AIEC (adherent-invasive E. coli). Top phages include those isolated on the reference AIEC strains LF82, LF73 and 536. [src: ibd_phage_targeting]

Greedy minimum-set-cover gives a 5-phage cocktail covering 94.7 % of the 188 strains. The phages are DIJ07_P2, LF73_P1, AL505_Ev3, 55989_P2 and LF110_P2. The report calls it comparable in size to the 7-phage EcoActive clinical-trial cocktail. [src: ibd_phage_targeting] The remaining 26 strains (14 %) are resistant at ≤5 % susceptibility and are escape candidates. [src: ibd_phage_targeting]

Caveats on this cocktail:
- The 95 % figure concerns PhageFoundry strains, not UC Davis patient isolates. Patient applicability needs AIEC strain-resolution diagnostics on stool isolates. [src: ibd_phage_targeting]
- PhageFoundry has no explicit AIEC-versus-commensal annotation. Accurate AIEC coverage needs cross-reference to literature isolate annotations, even though the 188 strains include LF82, LF73, 536, NIC06 and BCH953 as phage isolation hosts. [src: ibd_phage_targeting]
- The clinical significance of the 26 escape strains needs cross-reference to AIEC pks-island annotation. [src: ibd_phage_targeting]
- The report requires per-patient detection of pks-island, Yersiniabactin and Enterobactin genes before cocktail selection. The cocktail covers broad E. coli diversity but does not separate AIEC from commensals. [src: ibd_phage_targeting]
- The susceptibility matrix is binary, with no titer or burst size. Dosing factors such as burst size, receptor binding and gastric survival are out of project scope. [src: ibd_phage_targeting]
- The other 5 actionable species are absent from phagefoundry_strain_modelling, so their availability rests on literature curation alone. [src: ibd_phage_targeting]

## In-vivo viromics

HMP2 fact_viromics contains observations of 16 unique E. coli phages and 13 unique Klebsiella phages. [src: ibd_phage_targeting] NB14 reports E. coli Spearman correlations of +0.18 with Podoviridae and +0.13 with Myoviridae. The report interprets these as endogenous carriage by T7-like and T4-like Caudovirales families. [src: ibd_phage_targeting] Gokushovirus WZ-2015a is lower in Crohn's disease (CD) across ecotypes (E1 cliff=-0.358, false discovery rate (FDR) 5e-7, n_CD=231 vs n_HC=125). This is consistent with Norman 2015 and Clooney 2019 on Microviridae depletion. [src: ibd_phage_targeting]

HMP2 shows no observations of phages targeting H. hathewayi, M. gnavus, F. plautii, E. lenta or E. bolteae. The report says this confirms the literature-side gut-anaerobe gap. [src: ibd_phage_targeting] No strong (|ρ|>0.30) endogenous phage candidate targets a Tier-A pathobiont, and all correlations have |ρ|≤0.18. [src: ibd_phage_targeting] The report calls the endogenous phageome a noisier channel than species-level taxonomy, where |CLR-Δ| is routinely >1.0. [src: ibd_phage_targeting]

Limits on this layer:
- 80 % of observations have an "Unknown" family (a VirMAP classification gap), so most phage observations cannot be linked to a host. [src: ibd_phage_targeting]
- The 7 unique E. coli phages in HMP2 (D108, EC6, ECML-117, Murica, slur16, vB_EcoM-VpaE1, vB_EcoM_AYO145A) do not name-overlap with PhageFoundry phages. [src: ibd_phage_targeting] The project's data therefore do not validate in-vivo gut delivery of the cocktail phages, which would need in-vivo testing. [src: ibd_phage_targeting]

## Gut-anaerobe gap by species

- **M. gnavus** ([[entities/mediterraneibacter-gnavus]]) has 6 temperate siphoviruses. It is not in PhageFoundry and has weak in-vivo signal. The report rates it limited and says alternatives are needed. [src: ibd_phage_targeting]
- **H. hathewayi** has no known phages, is not in PhageFoundry and has no detectable in-vivo correlation. The report makes it an external-database query priority. [src: ibd_phage_targeting]
- **F. plautii** ([[entities/flavonifractor-plautii]]) is absent from literature curation and PhageFoundry and has no detectable in-vivo correlation. The report prefers alternatives because it also has the highest bile-acid-coupling cost. [src: ibd_phage_targeting]

The report calls this gap the structural ceiling on cocktail completeness. Pure phage cocktails suit Enterobacteriaceae-dominated dysbiosis, such as the E. coli AIEC subset with high phage diversity. The dominant gut-anaerobe pathobionts need alternative or hybrid strategies. [src: ibd_phage_targeting]

The report ranks INPHARED and IMG/VR external database queries as the highest-priority follow-up before clinical translation. [src: ibd_phage_targeting] Its Lakehouse-internal scope excluded them. [src: ibd_phage_targeting]

## Open Directions

- Query INPHARED and IMG/VR for H. hathewayi, F. plautii and M. gnavus phages, to close the external-data gap the report left out of scope.
- Cross-reference the 188 PhageFoundry strains with literature AIEC annotation and pks-island status. This would give true AIEC coverage and show whether the 26 escape strains matter clinically.
- Run AIEC strain-resolution diagnostics on patient stool isolates and test the 5-phage cocktail against them. This closes the gap between PhageFoundry and patient strains.
- Reclassify the 80 % "Unknown"-family HMP2 phage observations to link them to hosts.
- Test lytic activity and burst size for the cocktail phages, and test in-vivo delivery, since the HMP2-PhageFoundry overlap is 0.
