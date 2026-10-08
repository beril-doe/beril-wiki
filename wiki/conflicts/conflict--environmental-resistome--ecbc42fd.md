<!-- tension-hash: ecbc42fd1f199bb8 -->
# AMRFinderPlus catalog scope: broad stress-resistance landscape versus narrow antibiotic-resistance reading, with unclassified fractions that do not match

Projects describing the environmental resistome, the set of antimicrobial-resistance (AMR) genes carried by bacteria across ecological settings, read the same reference catalog in two ways. The AMRFinderPlus reference catalog detects metal and stress systems, while narrower language treats its hits as antibiotic resistance [src: amr_pangenome_atlas, amr_environmental_resistome]. The projects also report an Other/Unclassified category and a count of unassigned clusters that differ in size and rest on differing denominators and vocabularies [src: amr_pangenome_atlas, amr_environmental_resistome]. This matters because conclusions in [[concepts/environmental-resistome]] about how environment structures the resistome depend on what the catalog counts and on how much of it carries no mechanism label.

## Evidence Sides

**Side 1: the catalog is broad and includes metal and stress systems**
The AMRFinderPlus catalog detects metal and stress systems, so a count based on the catalog is not a narrow count of antibiotic resistance [src: amr_pangenome_atlas, amr_environmental_resistome]. Under this reading, mercury- and arsenic-resistance families and an Other/Unclassified category of 22.2% weaken the narrow antibiotic-resistance interpretation [src: amr_pangenome_atlas, amr_environmental_resistome].

**Side 2: narrow antibiotic-resistance language**
Other wording describes the catalog's contents as antibiotic resistance [src: amr_pangenome_atlas, amr_environmental_resistome]. This narrow reading is weakened, not refuted: it remains in tension with the broad catalog and is not overturned by it [src: amr_pangenome_atlas, amr_environmental_resistome].

**Side 3: the size of the unclassified fraction disagrees**
The environmental-resistome analysis reports 15,550 unassigned clusters (18.7%), not 18,448 (22.2%) [src: amr_pangenome_atlas, amr_environmental_resistome]. The two figures rest on differing denominators and vocabularies. The record states that they must not be silently reconciled [src: amr_pangenome_atlas, amr_environmental_resistome].

## Possible Reconciliations

- **Hypothesis A:** The two unclassified counts differ because each project used its own mechanism vocabulary. A label set that assigns more clusters to named mechanisms would leave fewer clusters unassigned. This is untested.
- **Hypothesis B:** The two counts differ because the denominators differ: the projects may have counted different cluster sets or different hit sets. Under this hypothesis, neither figure is wrong, and the two cannot be compared directly.
- **Hypothesis C:** Both readings are partly correct. A core of genuine antibiotic-resistance genes would sit inside a wider metal and stress-resistance landscape. The relative share of each would vary by environment. This is a hypothesis, not an established finding.

## Resolving Work

- Re-run mechanism assignment on one shared cluster table with a single fixed vocabulary in both projects. Then test whether the difference between the 18,448 Other/Unclassified clusters and the 15,550 unassigned clusters persists when the denominator and the labels are identical [src: amr_pangenome_atlas, amr_environmental_resistome].
- Map catalog hits to an external ontology of antibiotic-resistance terms, and test whether that mapping can separate antibiotic-resistance genes from metal and stress families such as mercury- and arsenic-resistance families. The question is how much of the Other/Unclassified category falls into non-antibiotic families.
- Recompute the environment comparisons twice, once with all catalog hits and once with only the subset confirmed as antibiotic resistance. The question is whether conclusions about the environmental structuring of the resistome hold under the narrow reading.
- Test whether unassigned clusters are non-randomly distributed across environment classes, using a contingency test with false-discovery-rate (FDR, the expected share of false positives among significant results) correction. A non-random distribution would flag a possible bias from excluding these clusters, though it would not by itself establish one.
