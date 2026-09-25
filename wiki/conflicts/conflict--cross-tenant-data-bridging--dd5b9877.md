<!-- tension-hash: dd5b9877c724554c -->
# Does a Corpus-Wide Summary Statistic Carry Meaning Across Tenants, or Does It Move With the Sample?

Two projects bridging separate data tenants report headline numbers that behave in opposite ways, and the wiki's account of bridged evidence in [[concepts/cross-tenant-data-bridging]] has to hold both. One project reads a highly skewed distribution as evidence that a single aggregate count is not a uniform proxy for evidence; the other finds that its aggregate magnitude — a median partial correlation, the association between two variables after the effect of a third is held constant — moved by a reported factor of 27x between samplings while its statistical conclusion, a null, did not move. The disagreement matters because bridged pipelines routinely export one number per entity (a paper count, a median partial correlation) into a downstream join, and these two results disagree about whether such a number is a portable quantity or an artifact of which rows were pulled.

## Evidence Sides

**Skew makes the aggregate non-portable (PaperBLAST side).** PaperBLAST's organism-level Gini coefficient — an inequality index running from 0 (perfectly even) to 1 (all attention on one entity) — is 0.967, and the gene-level Gini is 0.669; 9.2% of 50%-identity families (protein families grouped at 50% sequence identity) have zero papers, 46.1% exactly one, and 4.3% at least 20, contradicting paper count as a uniform evidence proxy. [src: paperblast_explorer]

**The conclusion survives even when the magnitude does not (ecotype side).** The ecotype analysis found p=0.83 and rho=-0.085, p=0.25 — Spearman's rho being a rank correlation, and p the probability of a result this extreme under the null — while its median partial correlation was 0.081 across 183 species versus 0.003 originally, a reported 27x difference caused by different sampling. [src: ecotype_env_reanalysis] Both tests remain null; nothing here is reported as significant. On this side the transferable object is the direction and the non-significance, not the magnitude.

## Possible Reconciliations

- **Hypothesis: level-of-analysis mismatch.** Perhaps counts over a Gini-0.967 distribution [src: paperblast_explorer] and medians over 183 species [src: ecotype_env_reanalysis] fail differently — the first at the entity level, the second at the sample level — so both claims can hold without contradiction.
- **Hypothesis: thresholds, not statistics, are the fragile part.** Perhaps 50%-identity family boundaries [src: paperblast_explorer] and the sampling frame behind the 27x shift [src: ecotype_env_reanalysis] are both threshold choices, and only threshold-free summaries bridge safely.
- **Hypothesis: nulls travel, magnitudes do not.** Perhaps p=0.83 and rho=-0.085, p=0.25 replicate because null results are insensitive to sampling depth [src: ecotype_env_reanalysis], while any point estimate — including a paper count — does not.

## Resolving Work

- Recompute the ecotype median partial correlation under the PaperBLAST sampling frame and ask whether the 0.081-versus-0.003 gap [src: ecotype_env_reanalysis] shrinks.
- Bootstrap the organism and gene Gini coefficients [src: paperblast_explorer] to test whether 0.967 and 0.669 are themselves sampling-stable.
- Re-cluster PaperBLAST families at identity thresholds other than 50% and ask whether the 9.2%/46.1%/4.3% split [src: paperblast_explorer] is threshold-driven.
- Re-run the Spearman test at several subsample sizes to ask whether p=0.25 [src: ecotype_env_reanalysis] is depth-invariant.
- Join both tenants' entities and test whether skewed paper counts predict partial-correlation instability.
