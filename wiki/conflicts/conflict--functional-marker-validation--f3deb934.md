<!-- tension-hash: f3deb9342cdce607 -->
# Does the Retained "SR" Signal Denote Sulfite Reduction or Sulfate Reduction?

Two projects appear to report the same retained marker signal under different names. The Bacillota_B subsurface project labels it only with the abbreviation "SR", which has been read as "sulfite reduction". The clay-confined subsurface project calls it dissimilatory "sulfate reduction". [src: bacillota_b_subsurface_accessory] [src: clay_confined_subsurface] The difference matters for the principle set out in [[concepts/functional-marker-validation]]: an ecological claim is only as sound as the match between a marker and the function it is meant to represent. An unresolved label could carry the wrong functional interpretation into later synthesis, even when the underlying counts agree.

## Evidence Sides

**Side A: "SR" read as sulfite reduction.** The Bacillota_B report names the retained signal only with the abbreviation "SR", and that abbreviation has been read as "sulfite reduction". It reports 5/9 positives and the same null scale as the clay report. [src: bacillota_b_subsurface_accessory] [src: clay_confined_subsurface] The case for this side rests on how an undefined abbreviation was read, not on any marker definition stated in the report text.

**Side B: the signal is dissimilatory sulfate reduction.** The clay report describes the signal as dissimilatory "sulfate reduction", also with 5/9 positives and the same null scale. [src: bacillota_b_subsurface_accessory] [src: clay_confined_subsurface] The Bacillota_B report lists its SR markers as K11180, K11181, K00394, K00395 and K00958. These are KEGG Orthology (KO) identifiers, which are database accessions for gene families. The central discoveries digest defines the SR-marker set as dsrAB-aprAB-sat. This **weakens** the terminology tension in favour of the sulfate-reduction reading. Even so, the label-to-marker mapping should be verified against the underlying marker definitions and source tables rather than assumed. [src: bacillota_b_subsurface_accessory, discoveries]

## Possible Reconciliations

- *Hypothesis 1:* "SR" in the Bacillota_B report is shorthand for the same dissimilatory sulfate-reduction marker set used in the clay report, and the "sulfite reduction" reading is a misreading of an undefined abbreviation. The matching 5/9 positives and the shared null scale fit this, but they do not establish it. [src: bacillota_b_subsurface_accessory] [src: clay_confined_subsurface]
- *Hypothesis 2:* The two reports use different marker definitions that happen to produce the same positives. In that case the agreement would be coincidental, and the labels might each be accurate for their own marker set.

## Resolving Work

- **Marker definitions:** Compare the Bacillota_B notebook's SR marker list with the clay report's sulfate-reduction marker definition. Do both projects use the identical set of five KOs?
- **Source tables:** Cross-tabulate per-genome SR calls from both projects' source tables for the shared cohort. Are the same genomes positive, or do the counts merely coincide?
- **KO annotation:** Check each listed KO against current KEGG annotations and the discoveries digest's dsrAB-aprAB-sat definition. Does the set include genes specific to sulfate activation, which would justify the "sulfate reduction" label over "sulfite reduction"?
- **Step-wise split:** Re-score positives separately for the sulfite-reductase subset and the sulfate-activation subset within the listed KOs. Does the retained signal depend on the full pathway or on the sulfite-reduction step alone?
