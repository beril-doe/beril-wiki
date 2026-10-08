<!-- tension-hash: 732543c8a078ae87 -->
# Does an 11/13 Directional Signal Support Community-Scale Black Queen Behavior, or Is It Too Coverage-Limited to Generalize?

This page records a disagreement over how much weight the amino-acid evidence in [[concepts/community-metabolic-interdependence]] can bear. Community metabolic interdependence, the framing behind Black Queen predictions, is the hypothesis that organisms can rely on metabolites produced by neighboring organisms, allowing loss or reduction of otherwise costly biosynthetic functions. [src: discoveries] One reading treats the 11/13 directional result as supportive. [src: discoveries] It also notes that a leucine signal strengthened after a mapping correction. [src: nmdc_community_metabolic_ecology] The other reading holds that sparse compound annotation, untestable pathways and proxy metabolites leave the result coverage-limited, unable to distinguish universal from pathway-specific Black Queen behavior. [src: discoveries]

## Evidence Sides

**Side A: the signal is supportive, and correcting an error strengthened it**

The 11/13 directional result counts as supportive of Black Queen behavior. [src: discoveries] The NMDC (National Microbiome Data Collaborative) analysis confirms that the reported run corrected an isoleucine/leucine mapping collision. [src: nmdc_community_metabolic_ecology] Before the fix, three isoleucine compounds had been misassigned to leucine. Those compounds had near-zero completeness-versus-metabolite correlation, so they diluted the true leucine signal. Correcting them moved leucine from correlation coefficient r −0.326 to −0.390, and from q (false-discovery-rate-adjusted p-value) 0.045 to 0.022. [src: nmdc_community_metabolic_ecology] Under this reading, removing the diluting misassignments strengthened the leucine signal rather than weakening it. [src: nmdc_community_metabolic_ecology]

**Side B: coverage limits prevent generalization**

Only approximately 2% of compounds had KEGG (Kyoto Encyclopedia of Genes and Genomes) identifiers. Matching therefore relied on compound-name substrings, which risked collisions such as leucine versus isoleucine. [src: discoveries] Three amino-acid pathways (cysteine, histidine and lysine) were untestable because the relevant compounds were absent. [src: discoveries] These pathways remained untestable in the NMDC run. [src: nmdc_community_metabolic_ecology] As a result, the 11/13 result is supportive but coverage-limited: the untested pathways cannot distinguish universal Black Queen behavior from pathway-specific behavior. [src: discoveries]

Aromatic readouts carry a related gap. Chorismate itself is rarely detected, so shikimic acid and 3-dehydroshikimic acid serve as upstream proxies. These proxies reflect precursor availability, not chorismate pool size. [src: discoveries] The NMDC analysis **supports** this caution. It states that these compounds are upstream intermediates and that the chorismate Black Queen correlation (r = −0.038) should be interpreted cautiously. [src: nmdc_community_metabolic_ecology]

## Possible Reconciliations

- *Hypothesis:* Both sides are correct at different scopes. The directional signal is real for the pathways that could be tested, but it says nothing about the untested ones. In that case "supportive" and "coverage-limited" are compatible descriptions rather than competing ones.
- *Hypothesis:* Remaining name-matching errors could bias other pathway correlations toward zero, as the leucine collision did. If so, better annotation would strengthen the signal rather than overturn it.
- *Hypothesis:* Black Queen provisioning may be pathway-specific. If so, the untested pathways and the aromatic proxy readout could legitimately diverge from the tested majority.

## Resolving Work

- **Annotation audit:** Re-map NMDC metabolomics compounds to KEGG or ChEBI (Chemical Entities of Biological Interest) identifiers using structure- or formula-based matching. Then re-run the completeness-versus-metabolite correlations to ask whether any other pathway shifts the way leucine did.
- **Untested pathways:** Add metabolomics datasets that detect cysteine, histidine and lysine compounds, and test whether these pathways follow the tested majority. This would distinguish universal from pathway-specific Black Queen behavior.
- **Direct chorismate measurement:** Use targeted metabolomics that quantifies chorismate pools, and ask whether the aromatic correlation differs from the upstream-proxy result.
- **Collision sensitivity analysis:** Deliberately perturb the substring-matching order and measure how much each pathway's correlation and q value depend on the mapping choices.
