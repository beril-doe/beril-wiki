<!-- tension-hash: 8542320b237088a6 -->
# Does Differential Missingness Explain the Weak Environmental Signal?

Species from different ecological classes lose data at different rates, with Environmental species affected more often than Human-associated ones [src: ecotype_env_reanalysis]. Yet removing more Environmental species did not produce the expected stronger environmental signal [src: ecotype_env_reanalysis]. The tension matters because missingness, sampling depth and ecological classification are each candidate explanations for why environment–gene-content relationships look weak. If they are treated as interchangeable, a sampling artifact could be mistaken for a biological null, or the reverse. It is recorded from [[concepts/sampling-depth-and-downsampling-effects]].

## Evidence Sides

**Side 1: Missingness is unequal and could distort the comparison.**
Environmental species had a 21% NaN rate, compared with 7% for Human-associated species [src: ecotype_env_reanalysis]. NaN ("not a number") marks a missing or undefined value. Upstream, the explorer project reports 3,838 records with at least one embedding NaN, along with uneven metadata coverage [src: env_embedding_explorer]. An embedding is a numeric vector that summarises a genome's environmental context. On this side, missingness is a measured asymmetry that falls more heavily on the Environmental group [src: ecotype_env_reanalysis].

**Side 2: The unequal missingness did not behave as the expected explanation.**
Removing more Environmental species did not produce the expected stronger environmental signal [src: ecotype_env_reanalysis]. This null outcome does not by itself show that missingness contributes nothing; the source concludes that missingness, sampling depth and ecological classification must be analysed jointly rather than treated as interchangeable explanations [src: ecotype_env_reanalysis]. The explorer's NaN count **refines** this tension but does not resolve it [src: env_embedding_explorer].

## Possible Reconciliations

- *Hypothesis:* missingness is not random with respect to signal strength. The Environmental species dropped as NaN may differ systematically from those retained. If so, their removal would neither raise nor lower the group's apparent signal in a predictable direction.
- *Hypothesis:* the uneven metadata coverage noted upstream overlaps with ecological classification. Missingness and classification would then be confounded rather than independent sources of bias.
- *Hypothesis:* sampling depth, not missingness, is the limiting factor. Better-sampled classes could show stronger relationships regardless of how many species are excluded.

None of these is established by the current evidence.

## Resolving Work

- Use the per-species NaN status from the ecotype reanalysis and the explorer's NaN-bearing records. Compare retained and dropped Environmental species on genome count and metadata completeness with a logistic model (a regression predicting the probability of missing versus non-missing status). This tests whether missingness is predictable from sampling depth.
- Use the same species set and either recover the original values of NaN-affected records or impute them (estimate the missing values statistically). Rerun the group comparison as a sensitivity analysis. This tests whether including the dropped Environmental species changes the environmental signal.
- Use species-level metadata coverage, sampling depth and ecological class in a joint regression (one model estimating each factor's effect while holding the others fixed) of the environment–gene-content relationship. This tests which factor carries explanatory weight when all three are modelled together.
- Use the explorer's records with at least one embedding NaN. Tabulate which embedding dimensions fail by ecological class. This tests whether NaN arises from specific environment types or occurs uniformly.
