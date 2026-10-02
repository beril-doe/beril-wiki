<!-- tension-hash: 782017fabdc04203 -->
# Ecology or Lineage? Whether the Environmental AMR Signal Survives Within-Taxon Testing

At issue is whether environment-associated differences in AMR (antimicrobial resistance — genes conferring resistance to antibiotics) gene content reflect ecology, or whether they track the taxonomic composition and uneven sampling of the genomes available. One analysis reports significant effects within five of six phyla and 20 of 141 families, which supports an ecological association [src: amr_environmental_resistome]; the same analysis holds that the majority of families were not testable or significant because of limited environmental breadth [src: amr_environmental_resistome], while a within-species follow-up reports that no general statistical demonstration was obtained [src: amr_strain_variation]. The disagreement matters because it decides whether the environment→resistome link in [[concepts/phylogenetic-confounding-of-pangenome-associations]] is a within-lineage effect or an artifact of which lineages were sequenced.

## Evidence Sides

**Stratified testing supports an ecological association.** The environmental-resistome analysis qualifies rather than contradicts the earlier environmental comparison: significant effects within five of six phyla and 20 of 141 families support an ecological association [src: amr_environmental_resistome].

**The same analysis reports insufficient breadth and unresolved confounders.** The majority of families were not testable or significant because of limited environmental breadth [src: amr_environmental_resistome]. Its species-level classifications, sampling imbalance, and AMRFinderPlus-focused annotation (AMRFinderPlus is NCBI's curated detector for known resistance genes) also leave unresolved how much of the clinical contrast reflects lineage, representation, or unrecognized environmental resistance [src: amr_environmental_resistome].

**Within species, visible structure is not matched by a general result.** The within-species analysis adds a similar tension: visible environmental structuring in case-study AMR ecotypes (ecotype — a within-species lineage associated with a particular habitat) was not matched by a general statistical demonstration because metadata and within-species environmental diversity were insufficient [src: amr_strain_variation]. This stands as a null at the general level, not as a demonstration that structuring is absent.

## Possible Reconciliations

- **Hypothesis: the split is statistical power, not biology.** The families that tested significant may be the ones with enough environmental breadth to test at all, and the non-significant remainder may be uninformative rather than negative [src: amr_environmental_resistome].
- **Hypothesis: the effect is real but scale-dependent.** Ecology may structure resistomes detectably within phyla and only weakly within families and within species, so stratified and case-study evidence can both be correct [src: amr_environmental_resistome, amr_strain_variation].
- **Hypothesis: annotation scope generates the contrast.** If AMRFinderPlus-focused annotation under-detects unrecognized environmental resistance, the clinical contrast would be partly a detection gradient rather than an ecological one [src: amr_environmental_resistome].

## Resolving Work

- Re-run the family-level environmental tests only on families meeting an explicit environmental-breadth threshold, reporting testable and untestable families separately: does the 20 of 141 result change when the denominator is restricted to testable families?
- Subsample genomes to equalize sampling imbalance across environments and lineages, then repeat the stratified comparison: does the ecological effect persist under balanced representation?
- Complement AMRFinderPlus with broader homology-based searches for uncharacterized resistance determinants: how much of the clinical contrast remains once unrecognized environmental resistance is detectable?
- Assemble strain-level environmental metadata for species with genuine within-species habitat diversity and test ecotype structuring formally: can the case-study pattern be generalized statistically?
- Compare classifications at species versus finer resolution for the same genomes: how much of the clinical contrast is reassigned when species-level labels are refined?
