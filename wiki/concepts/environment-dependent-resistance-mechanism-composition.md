---
type: "Concept"
description: "How the mix of AMR mechanisms (metal resistance, target modification, efflux, enzymatic inactivation) differs across environments and what selective pressures it is thought to reflect; stops at gene-level conservation."
sources: ["summaries/amr_environmental_resistome__REPORT.md", "summaries/discoveries.md"]
---
# Environment-dependent resistance mechanism composition

The mix of antimicrobial resistance (AMR) mechanisms differs strongly between environments. The amr_environmental_resistome report finds that metal resistance dominates soil and aquatic AMR, while target modification (and, in one account, efflux) is more prominent in gut and clinical species. The report reads this as niche-specific selection. The environment effects are statistically strong, but the selective-pressure reading is the report's interpretation. The report's own numbers for efflux and target modification also disagree between its sections (see Tensions). [src: amr_environmental_resistome, discoveries]

## Mechanism fractions by environment

All four mechanisms show significant environment-dependent composition (all q ~ 0 after Benjamini-Hochberg false discovery rate, BH-FDR, correction). [src: amr_environmental_resistome] The tests are Kruskal-Wallis (KW) tests on bacterial species; see [[entities/kruskal-wallis-test-with-eta-squared-effect-size]]. Effect sizes (η²) rank metal resistance highest and enzymatic inactivation lowest. [src: amr_environmental_resistome]

Fractions of AMR by environment, in the order clinical, human gut, host-associated, soil, aquatic, other environmental:

- Metal resistance: 19.7%, 6.1%, 12.7%, 44.0%, 45.0%, 24.9%; η² = 0.107. [src: amr_environmental_resistome]
- Target modification: 27.5%, 43.6%, 22.8%, 10.1%, 6.2%, 25.1%; η² = 0.100. [src: amr_environmental_resistome]
- Efflux: 6.1%, 7.0%, 3.7%, 2.0%, 1.1%, 2.7%; η² = 0.055. [src: amr_environmental_resistome]
- Enzymatic inactivation: 28.2%, 24.1%, 44.1%, 34.3%, 41.2%, 33.6%; η² = 0.019. [src: amr_environmental_resistome]

The KW statistics are H=1498.4 for metal resistance, H=1394.9 for target modification, H=768.0 for efflux and H=266.0 for enzymatic inactivation. [src: amr_environmental_resistome]

Metal resistance is the largest environment effect. It makes up 45% of AMR in aquatic species and 44% in soil, but only 6% in human gut (η² = 0.107). [src: amr_environmental_resistome, discoveries] See [[entities/metal-resistance-genes]] and [[concepts/metal-resistance-genes-within-amr-catalogs]].

Target modification accounts for 44% of human gut AMR and 28% of clinical AMR, but only 6% in aquatic species (η² = 0.100). [src: amr_environmental_resistome] The report classes tet(M,O,Q,W) ribosomal protection proteins as target modification and tet(A-E,K,L) as efflux. [src: amr_environmental_resistome] See [[entities/target-modification-resistance]].

Efflux is a small share of AMR everywhere in the main table, highest in the human gut (7.0%) and lowest in aquatic species (1.1%). [src: amr_environmental_resistome] See [[entities/efflux-pumps]]. Enzymatic inactivation, including beta-lactamases, is the most uniformly distributed mechanism: present in all environments, dominant in none. [src: amr_environmental_resistome] Its fractions range from 24.1% in human gut to 44.1% in host-associated species. [src: amr_environmental_resistome] See [[entities/enzymatic-inactivation-of-antibiotics]].

## Proposed selective pressures

The report interprets these patterns as showing that different ecological niches select fundamentally different resistance strategies. [src: amr_environmental_resistome] It describes soil and aquatic metal resistance as consistent with heavy-metal exposure in natural environments. It describes clinical and gut target modification and efflux as consistent with antibiotic selection pressure. [src: amr_environmental_resistome] These are the report's interpretations of the observed patterns. [src: amr_environmental_resistome]

## Scale of the underlying catalog

The resistome has 26,220 enzymatic-inactivation clusters, 22,223 metal-resistance clusters, 11,067 target-modification clusters and 5,224 efflux clusters. [src: amr_environmental_resistome] The central discoveries digest describes the analysis as covering 14,723 species. [src: discoveries]

## Tensions

- The table gives efflux as 7.0% of human gut AMR with η²=0.055. [src: amr_environmental_resistome] The discoveries digest gives 21% in human gut versus 1% in aquatic, with η²=0.127. [src: discoveries] The report's narrative also gives clinical and gut efflux as 15-21%. [src: amr_environmental_resistome] The sources do not say what causes the difference, and I have not reconciled it.
- For target modification, the table gives 27.5% clinical and 43.6% human gut. [src: amr_environmental_resistome] The narrative gives 19-29% for clinical and gut bacteria. [src: amr_environmental_resistome] The summary line gives 28-44%. [src: amr_environmental_resistome]

## Caveats

Mechanism fractions exclude 18.7% of AMR clusters (15,550) that could not be classified from gene name or product annotation. [src: amr_environmental_resistome] This could bias the results if the unclassified genes are not spread evenly across environments. [src: amr_environmental_resistome] See [[concepts/functional-annotation-of-amr-genes-and-mechanism-classification]] and [[concepts/sampling-bias-and-metadata-sparsity-in-amr-resistome-surveys]].

## Open Directions

- Recompute the efflux fractions and η² from the species-level data to settle the gap between 7.0% and 21% for human gut. This would show which definition of efflux each figure uses.
- Rerun the mechanism fractions with the 15,550 unclassified clusters as a separate category, or reclassify them with sequence-based annotation. This would test whether the exclusion biases the environment contrasts.
- Test whether the soil and aquatic metal-resistance signal holds after controlling for sampling depth and phylogeny. This would separate selection from taxonomic composition.
- Compare site-level metal and antibiotic concentrations with mechanism fractions, where the metadata exist. This would test the selective-pressure interpretation directly.
