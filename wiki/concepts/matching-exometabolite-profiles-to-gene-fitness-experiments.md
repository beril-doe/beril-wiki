---
type: "Concept"
description: "Whether strains and conditions in an exometabolomics database can be matched to Fitness Browser organisms and carbon/nitrogen-source experiments, and how strong the match is; covers strain-level versus genus-level matches and coverage caveats."
sources: ["summaries/discoveries.md", "summaries/fw300_metabolic_consistency__REPORT.md", "summaries/webofmicrobes_explorer__REPORT.md"]
---
# Matching exometabolite profiles to gene-fitness experiments

Two Web of Microbes (WoM) Pseudomonas strains match Fitness Browser (FB) organisms exactly, E. coli matches at strain level with very little WoM data, and Synechococcus PCC7002 matches only at genus level. [src: discoveries, webofmicrobes_explorer] The strongest evidence is a curated crosswalk for Pseudomonas FW300-N2E3, which links 19 produced metabolites to FB carbon or nitrogen source experiments. [src: webofmicrobes_explorer] The WoM-to-FB link is rated strong for 3 organisms, and the 2018 WoM snapshot records only production, so coverage is thin. [src: webofmicrobes_explorer]

## Strain-level and genus-level matches

Two WoM organisms are exact FB strain matches. Pseudomonas sp. FW300-N2E3 matches pseudo3_N2E3, with 5,854 genes and 211 experiments. [src: discoveries, webofmicrobes_explorer] Pseudomonas sp. GW456-L13 matches pseudo13_GW456_L13, with 5,243 genes and 106 experiments. [src: discoveries, webofmicrobes_explorer] Both are ENIGMA groundwater isolates with rich FB data. [src: webofmicrobes_explorer] See [[entities/pseudomonas-fluorescens-fw300-n2e3]] and [[entities/pseudomonas-sp-gw456-l13]].

E. coli BW25113 in WoM is the same strain as Keio in FB, which has 4,610 genes and 168 experiments. [src: discoveries, webofmicrobes_explorer] This **limits** the usefulness of the match. WoM holds only 12 observations for this strain, in ZMMG medium, focused on sulfur or cysteine metabolism. [src: webofmicrobes_explorer] Keio is one of the richest FB organisms. [src: webofmicrobes_explorer] See [[entities/escherichia-coli]].

WoM Synechococcus PCC7002 matches FB SynE (PCC 7942) only at genus level, with 2,722 genes and 129 experiments. [src: webofmicrobes_explorer] The report rates the WoM-to-FB link as strong for 3 organisms. [src: webofmicrobes_explorer]

## Matching metabolites to carbon and nitrogen conditions

For the matched organisms, FB carbon-source experiments test metabolites that WoM detects as produced. One report counted 109 metabolite-condition name overlaps. [src: discoveries]

For FW300-N2E3, curated matching found 19 produced metabolites that FB tests as carbon or nitrogen sources. [src: webofmicrobes_explorer] Of these, 5 are de novo products (E) and 14 are amplified metabolites (I). [src: webofmicrobes_explorer] Examples:

| WoM metabolite | Action | FB condition | Source type |
|---|---|---|---|
| alanine | I | L-Alanine, D-Alanine | carbon/nitrogen [src: webofmicrobes_explorer] |
| arginine | I | L-Arginine | nitrogen [src: webofmicrobes_explorer] |
| glycine | I | Glycine | nitrogen [src: webofmicrobes_explorer] |
| lactate | E | Sodium D-Lactate | carbon [src: webofmicrobes_explorer] |
| proline | I | L-Proline | carbon [src: webofmicrobes_explorer] |
| valine | E | L-Valine | carbon [src: webofmicrobes_explorer] |
| trehalose | I | D-Trehalose dihydrate | carbon [src: webofmicrobes_explorer] |
| malate | I | L-Malic acid | carbon [src: webofmicrobes_explorer] |
| thymine | E | Thymine | nitrogen [src: webofmicrobes_explorer] |
| nicotinamide | I | Nicotinamide | unspecified [src: webofmicrobes_explorer] |
| carnitine | E | Carnitine hydrochloride | unspecified [src: webofmicrobes_explorer] |

The same report also lists phenylalanine, tryptophan, lysine, threonine, adenine, adenosine and inosine. [src: webofmicrobes_explorer] Related pages: [[entities/arginine]], [[entities/malate]], [[entities/trehalose]], [[entities/tryptophan]].

A second report built a crosswalk for FW300-N2E3. It matched 28/58 (48%) WoM metabolites to FB carbon/nitrogen source conditions. [src: fw300_metabolic_consistency] Manual curation gave 28 WoM–FB and 8 WoM–BacDive matches. [src: fw300_metabolic_consistency] The 28 and the 19 are not the same quantity. The 19 counts produced metabolites tested in FB. [src: webofmicrobes_explorer] The 28 counts crosswalk matches. [src: fw300_metabolic_consistency] I do not relate the two further.

## Coverage and match-quality caveats

Of 31 FB conditions mapped in the crosswalk, 7 had no FW300-N2E3 experiments: 4-aminobutanoate, 5-oxo-proline, Betaine, Guanine, Nicotinamide, Sarcosine and trans-Aconitate. [src: fw300_metabolic_consistency] The downstream analysis uses only the 24 conditions with fitness data. [src: fw300_metabolic_consistency]

Two matches are approximate base-to-nucleoside mappings, Cytosine→Cytidine and Uracil→Uridine. They are flagged fb_match_quality=approximate. [src: fw300_metabolic_consistency] Excluding them cut testable metabolites from 21 to 19 and shifted mean concordance from 0.937 to 0.930. [src: fw300_metabolic_consistency] The report calls this negligible because both were already fully concordant. [src: fw300_metabolic_consistency] A sensitivity analysis found no effect on concordance results. [src: fw300_metabolic_consistency] See [[concepts/cross-database-concordance-of-metabolite-evidence]].

The 2018 WoM snapshot records only production, not consumption. This prevents testing whether consumed metabolites predict gene essentiality. [src: webofmicrobes_explorer] See [[concepts/production-versus-consumption-coverage-in-exometabolomic-databases]].

## How strong is the integration?

One report states that no published study has systematically compared WoM exometabolomic profiles with FB gene fitness data, although the same research program (ENIGMA/Arkin Lab) generated both. [src: fw300_metabolic_consistency] That is the report's own claim. Both reports conclude that the integration is feasible. [src: fw300_metabolic_consistency, webofmicrobes_explorer] The webofmicrobes_explorer report finds its hypothesis H1 only partially supported, saying the cross-collection links are real and actionable. [src: webofmicrobes_explorer] The evidence supports feasibility for 3 organisms. [src: webofmicrobes_explorer] It does not yet show broad coverage.

The webofmicrobes_explorer report proposes a first test. For pseudo3_N2E3 and pseudo13_GW456_L13, identify genes that are fitness-important on carbon sources the same organism produces, to test whether metabolic output predicts gene essentiality. [src: webofmicrobes_explorer]

## Open Directions

- Run the proposed gene-fitness test on self-produced carbon sources in pseudo3_N2E3 and pseudo13_GW456_L13, using the 19 FW300-N2E3 matches and equivalent GW456-L13 matches.
- Build a curated crosswalk for GW456-L13 like the FW300-N2E3 one, with match-quality flags. This would show whether the approximate-match pattern repeats.
- Add WoM data on consumption, or newer exometabolomics, to test consumed metabolites against fitness. This would close the production-only gap.
- Extend WoM sampling of E. coli BW25113 beyond sulfur metabolism, to use the Keio strain match.

See also [[summaries/fw300_metabolic_consistency__REPORT]], [[summaries/webofmicrobes_explorer__REPORT]], [[summaries/discoveries]], [[entities/web-of-microbes]] and [[entities/fitness-browser]].
