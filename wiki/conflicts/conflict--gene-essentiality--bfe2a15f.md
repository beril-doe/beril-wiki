<!-- tension-hash: bfe2a15fe26a86e3 -->
# Do production, completeness and conservation signals indicate gene essentiality?

Several lines of evidence in the [[concepts/gene-essentiality]] synthesis treat what an organism *can* make, or what its genome encodes, as a guide to what it *requires*. Other evidence shows those signals do not settle the question. Metabolite production records cannot show uptake or dependency [src: webofmicrobes_explorer]. Many ortholog families (groups of genes descended from one ancestral gene) are not essential in every organism that carries them [src: discoveries]. A pathway predicted complete in most mapped genomes can still be missing in one [src: essential_metabolome]. This matters because the synthesis ranks direct perturbation above predictors, and reading capability signals as essentiality calls would promote predictors beyond what they can carry.

## Evidence Sides

**Side A: capability and conservation signals are widely shared and look like a common core**

- Of 17,222 ortholog families, 859 were universally essential, meaning essential in every organism where the family has members [src: discoveries]. This is a shared essential core among member organisms, not proof of presence or essentiality across the whole sample.
- By pathway-completeness prediction, 17 of 18 amino-acid pathways were complete in all 7 mapped organisms [src: essential_metabolome].
- Web of Microbes (WoM), an exometabolomics database recording metabolites organisms release into growth media, supplies production matches linked to organisms' metabolic output [src: webofmicrobes_explorer].

**Side B: these signals cannot establish uptake, pathway completeness, or essentiality**

- WoM production matches cannot establish uptake, pathway completeness, or gene essentiality [src: webofmicrobes_explorer].
  - The snapshot has no organism consumption actions [src: webofmicrobes_explorer].
  - 107 formula-only matches (matches on molecular formula alone, without structural identity) expanded to 900 candidate molecules [src: webofmicrobes_explorer].
- Most ortholog families are not universally essential: of the 17,222 families, 4,799 were variably essential and 11,564 were never essential [src: discoveries].
- Uniform completeness has an exception: *Desulfovibrio vulgaris* (DvH) lacked predicted serine biosynthesis [src: essential_metabolome].
- A genomically complete pathway can show no detectable fitness importance under the conditions tested, so completeness does not by itself indicate dependency [src: metabolic_capability_dependency].

## Possible Reconciliations

- **Hypothesis 1:** Capability, conservation and dependency are distinct layers. Production records, completeness predictions and family conservation describe what organisms make or encode; essentiality would require perturbation evidence under defined conditions. Under this reading, Side A's signals are real but not interchangeable with essentiality.
- **Hypothesis 2:** The DvH serine gap may be a prediction artifact or a genuine auxotrophy (a requirement for an externally supplied nutrient). The result is a pathway prediction, not a growth measurement [src: essential_metabolome].
- **Hypothesis 3:** Only the universally essential families may track essentiality within the conserved signal, with variably essential families reflecting genomic context rather than capability alone.

## Resolving Work

- **WoM and transposon fitness:** Join WoM production records to transposon-sequencing (TnSeq, which infers gene importance from mutant abundance) fitness data for shared organisms, testing whether genes behind emerged metabolites are fitness-relevant.
- **Formula-only matches:** Re-score the 107 formula-only WoM matches against structure-resolved standards or spectral libraries to ask how many of the 900 candidates are real [src: webofmicrobes_explorer].
- **DvH serine:** Grow DvH in serine-free versus serine-supplemented media to test whether the predicted serine gap is a true auxotrophy [src: essential_metabolome].
- **Variable essentiality:** For the 4,799 variably essential families [src: discoveries], model essential status against pathway completeness and gene-neighbourhood context, asking whether context explains variability better than conservation.
- **Completeness versus dependency:** Cross-tabulate the 17 complete amino-acid pathways in the 7 mapped organisms [src: essential_metabolome] against per-gene TnSeq fitness, asking whether completeness predicts dependency within this sample.
