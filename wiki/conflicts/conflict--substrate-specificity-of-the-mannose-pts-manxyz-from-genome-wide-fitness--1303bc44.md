<!-- tension-hash: 1303bc44d3121bcb -->
# Fructose Annotation Versus Fitness Data for the Mannose PTS ManXYZ

The tension concerns which sugar the ManXYZ transporter handles. ManXYZ is the mannose phosphotransferase system (PTS), a bacterial sugar-uptake system. UniProt, a curated protein database, annotates the ManX component as "fructose-specific" and with "fructose import across plasma membrane" (GO:0005354, a Gene Ontology term). [src: snipe_defense_system, discoveries] Genome-wide fitness data, by contrast, show ManXYZ is dispensable for fructose, and the discoveries digest states that this contradicts the annotation. [src: discoveries, snipe_defense_system] It matters because the two sources assign the transporter different substrates. The concept page this comes from is [[concepts/substrate-specificity-of-the-mannose-pts-manxyz-from-genome-wide-fitness]].

## Evidence Sides

**Side A: the annotation says fructose**

- UniProt annotates ManX as a "fructose-specific" PTS component. [src: snipe_defense_system, discoveries]
- UniProt also annotates ManX with "fructose import across plasma membrane" (GO:0005354, Gene Ontology). [src: snipe_defense_system, discoveries]

**Side B: the fitness data say ManXYZ is dispensable for fructose**

- Fitness data, meaning gene-knockout growth effects measured by random barcode transposon sequencing (RB-TnSeq), show ManXYZ is dispensable for fructose. [src: discoveries, snipe_defense_system]
- The discoveries digest states that this contradicts the annotation. [src: discoveries, snipe_defense_system]

The TENSION text gives no further numbers, thresholds or denominators for either side. The fitness result is a direct measurement, not an extrapolation.

## Possible Reconciliations

- **Hypothesis: the annotation reflects inference from homology.** The "fructose-specific" label may come from related PTS components and not from measurement in this organism. Nothing in the evidence tests this.
- **Hypothesis: the substrate depends on condition.** Fructose could matter for ManXYZ under conditions the fitness experiments did not cover. The fitness data describe only the conditions tested.
- **Hypothesis: another transporter masks the fructose role.** A redundant fructose uptake system could make ManXYZ dispensable in knockouts even if it can transport fructose. This is untested here.

None of these favours either side. Each needs its own test.

## Resolving Work

- **Data:** the fitness experiments with fructose as sole carbon source. **Method:** compare ManXYZ knockouts with wild type, including double knockouts of other fructose PTS genes. **Question:** does a redundant transporter hide a ManXYZ fructose role?
- **Data:** in vitro transport or phosphorylation assays on purified ManXYZ. **Method:** measure uptake of fructose, mannose and glucosamine directly. **Question:** can ManXYZ transport fructose at all, regardless of whether growth depends on it?
- **Data:** the evidence behind the UniProt entry and GO:0005354. **Method:** trace the annotation to its source records and evidence codes. **Question:** is the fructose label experimental or inferred?
- **Data:** fitness data for ManXYZ homologs in other bacteria. **Method:** compare fructose-condition fitness across organisms. **Question:** is the fructose-dispensable result specific to one organism or general?
