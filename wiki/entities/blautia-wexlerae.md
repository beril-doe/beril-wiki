---
type: "Organism"
description: "Human gut bacterial species listed among the discovery digest's trustworthy Crohn's-enriched E3 candidates but dropped from that set by a stricter E3-restricted recheck."
sources: ["summaries/discoveries.md", "summaries/ibd_phage_targeting__REPORT.md"]
---
*Blautia wexlerae* appears in this corpus as a candidate taxon in the inflammatory-bowel-disease differential-abundance screens, where its status changed between analysis passes: it was listed among the trustworthy candidates in the cross-project discovery digest, then removed from that set when a stricter, E3-restricted recheck was applied [src: discoveries, ibd_phage_targeting].

## Candidate status in the E3 differential-abundance screen

In the discovery digest, **3 of 15 E3 candidates passed all three filters**: [[entities/mediterraneibacter-gnavus]] (within-substudy CD↑ +5.13, LinDA E3 +1.64), [[entities/flavonifractor-plautii]] (within-substudy +1.89, LinDA +2.91), and *Blautia wexlerae* (within-substudy +0.91, LinDA +2.00) — described there as the trustworthy Tier-A set [src: discoveries].

Two pieces of jargon recur on this page. LinDA ([[entities/linda]]) is a linear-model method for differential abundance of compositional microbiome counts, and FDR is the false discovery rate. "Within-substudy" refers to effects estimated inside individual substudies; such estimates are then combined across substudies in a within-substudy meta-analysis, which is what yields a cohort-level effect, so estimation within a substudy and subsequent pooling across substudies are distinct steps [src: ibd_phage_targeting].

## Non-replication under the stricter E3 test

*Blautia wexlerae* does **not** replicate (+0.25, FDR 0.80). The NB04d "rock-solid E3 triad" that included *B. wexlerae* relied on NB04c's cohort-level within-substudy evidence rather than the E3-restricted within-substudy evidence; under the stricter E3 × HallAB_2017 test, *B. wexlerae* is removed from the rock-solid set [src: ibd_phage_targeting].

## How the two passes relate

The later result **contradicts** the digest's Tier-A listing for this species specifically, and does so by identifying the evidence base the earlier call rested on — cohort-level rather than E3-restricted within-substudy estimates. The two numbers (+0.91 from the cohort-level within-substudy evidence, +0.25 at FDR 0.80 under the E3 × HallAB_2017 test) are therefore not averaged or reconciled here: they are measurements under different restrictions, and the stricter one is the E3-restricted recheck that invalidated the earlier Tier-A inclusion [src: discoveries, ibd_phage_targeting].

That recheck is not itself a demonstration of cross-cohort replication: the E3 Tier-A analysis is single-study (HallAB_2017) and the E3 list should be treated as provisional until a second cMD-IBD sub-study populating E3 becomes available. The reliability of *B. wexlerae* as an IBD-associated taxon is accordingly best treated as unresolved rather than refuted outright, and the two companion taxa of the former triad are unaffected by this specific failure — a pattern that bears on how far candidate lists travel between cohorts ([[concepts/cross-cohort-microbiome-portability]], [[concepts/compositional-robustness-of-differential-abundance-calls]]) [src: ibd_phage_targeting].
