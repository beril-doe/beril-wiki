<!-- tension-hash: 6c57ba851fd6e5e4 -->
# Sulfite Reduction or Sulfate Reduction? Two Labels for the Same Retained Signal

Two projects report what appears to be the same retained functional signal in subsurface Bacillota_B/clay genomes, with the same positive count and the same null scale, but name it differently: one calls it "sulfite reduction," the other calls it dissimilatory "sulfate reduction." Because the label determines which metabolism is being inferred — reduction of sulfite versus the full dissimilatory reduction of sulfate — the mismatch matters even though no number is in dispute. This is the marker-validation problem from [[concepts/functional-marker-validation]] in its narrowest form: a naming discrepancy that cannot be settled by looking at the counts, only by going back to the marker definitions behind them. Terms used below: a *marker* is the gene or orthologous-group set used to score a genome as function-positive, and *dissimilatory* reduction is energy-conserving respiratory reduction rather than assimilation into biomass.

## Evidence Sides

**The "sulfite reduction" label.** The existing source describes the retained signal as "sulfite reduction," reporting 5/9 positives at the stated null scale. [src: bacillota_b_subsurface_accessory]

**The "dissimilatory sulfate reduction" label.** The new clay report describes the same retained signal as dissimilatory "sulfate reduction," likewise reporting 5/9 positives at the same null scale. [src: clay_confined_subsurface]

Neither side contradicts the other numerically: both report 5/9 positives and the same null scale. [src: bacillota_b_subsurface_accessory] [src: clay_confined_subsurface] The disagreement is entirely in what the positives are said to represent, and the tension text is explicit that this **requires** verification against the underlying marker definitions and source tables rather than silently treating the labels as interchangeable. [src: bacillota_b_subsurface_accessory] [src: clay_confined_subsurface]

## Possible Reconciliations

- *Shared-marker hypothesis*: both reports may be scoring an identical marker set, with one naming it by the reaction step the genes catalyse and the other by the broader respiratory pathway those genes sit in. If true, the counts agree because they are the same computation under two names.
- *Divergent-definition hypothesis*: the two reports may use non-identical marker sets that happen to return the same 5/9 positives on this cohort. Coincident counts would then be an artifact of a small denominator, not evidence of agreement.
- *Label-inheritance hypothesis*: one report may have re-derived the count while carrying over the other's wording, so the discrepancy reflects prose drift rather than any analytical difference.

## Resolving Work

- Retrieve the marker definitions (orthologous-group and KO — KEGG Orthology — identifiers) behind each report's sulfur call and diff the two sets: are they the same identifiers, or merely the same tally?
- Compare the per-genome positive/negative tables from both projects side by side: are the same genomes positive on each side, or different genomes summing to the same count?
- Check whether each marker set covers the full dissimilatory sulfate-to-sulfide route or only the sulfite-reducing step, and record which claim each set can license.
- Re-score both cohorts under a single harmonised marker definition and report whether 5/9 and the null scale survive, without averaging the two existing labels.
- Propagate whichever label the definitions support back to the downstream ecological statements that cite this signal, flagging any inference that depended on the broader reading.
