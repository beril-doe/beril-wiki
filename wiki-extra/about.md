# About This Wiki

The BERIL Knowledge Wiki is compiled, not written. Every page here was generated
by a pipeline from the BERIL Research Observatory's corpus of AI-conducted
microbial-biology research reports. Not all of it has been reviewed by a
scientist, and no page was reviewed as a whole before publication, so do not
assume that any particular claim was checked. Read the rest of this page before
citing anything here.

## What you are reading

The corpus is 75 research reports produced by AI agents working over BERDL
(KBase) data: pangenomes, RB-TnSeq fitness assays, biochemistry, and
environmental metadata. The pipeline summarises each report, plans which
synthesis pages it touches, and merge-rewrites those pages, so that a claim
accumulates evidence across projects instead of being restated once per project.

**Summaries.** One page per research project, linking to its raw report.

**Sources.** The raw reports themselves, unedited.

**Concepts.** Recurring ideas, each accumulating evidence from every project
that speaks to it.

**Entities.** Specific named things: organisms, genes and pathways, compounds,
methods, and datasets.

**Topics.** Hubs that cluster related concepts. Each opens with a
literature-context section whose citations were verified against PubMed.

**Conflicts.** Places where projects in the corpus disagree, with the evidence
on each side and the work that would resolve it.

## What the evidence label means

Synthesis pages carry a computed line under the title:

> **Evidence** · 5 source projects · well corroborated · conflict on record · literature context

Every part of it is counted, not judged:

| Term | Means |
| --- | --- |
| *N source projects* | distinct projects the page's prose actually cites |
| *single-source* | one project, so the claim has not been corroborated within this corpus |
| *corroborated* | 2 or 3 projects |
| *well corroborated* | 4 or more projects |
| *conflict on record* | the corpus records a disagreement spanning these same sources |
| *literature context* | the page opens with a literature-context section |

**It is not a confidence rating and not a review status.** "Well corroborated"
means several projects in this corpus point the same way. It does not mean the
finding is correct, and it does not mean anyone checked. Corroboration inside a
single corpus that shares data sources, tooling and methods is weaker evidence
than it looks. Several of the conflict pages exist precisely because
same-direction results turned out to rest on a shared confound.

## What is checked, and what is not

Automatically, on every build, and blocking publication:

- Every `[src:]` citation resolves to a real source document.
- Every number in a cited paragraph appears in a source that paragraph cites.
  Pages that fail are re-run against their own sources, and rejected if they
  fail again.
- Every `[[wikilink]]` resolves. Dead ones are downgraded to plain text.

Not checked by anything:

- Whether a finding is scientifically correct.
- Whether a statistical method suited its data.
- Whether the underlying research report reached a sound conclusion.
- Whether a synthesis fairly represents the projects it draws on.

Checked once, when the page is written, but not re-checked at publication:
literature-context citations are verified against PubMed by PMID at that point.
The *literature context* term only records that such a section exists.

Numeric fidelity is a real guarantee and a narrow one. It proves a figure
appears in a source the paragraph cites. It compares figures as tokens, so it
misses a flipped sign or a changed unit, and it ignores small integers. It never
shows the source was right.

## Known limitations

Entity pages are deduplicated by identity: a shared canonical name, a declared
alias, or a shared external identifier. Never by similarity, which over these
pages cannot tell two genes of one organism apart. Two entities that are the
same thing under names sharing none of those signals go undetected. Entities
cited by only one project are not published.

Reported budget figures undercount actual spend, so the cost notes in the
repository are lower bounds.

## How to cite

Cite the specific page and the date you read it, since pages change when the
corpus does.

> BERIL Project. *BERIL Knowledge Wiki: PAGE TITLE*. Lawrence Berkeley National
> Laboratory. PAGE URL (accessed DATE).

For example:

> BERIL Project. *BERIL Knowledge Wiki: Fitness costs and conditional benefits
> of antimicrobial-resistance genes*. Lawrence Berkeley National Laboratory.
> https://beril-doe.org/beril-wiki/concepts/antimicrobial-resistance-fitness-cost
> (accessed 2026-09-09).

For a finding, prefer citing the underlying research report, linked from every
summary page, over the synthesis page that aggregates it.

## License

This wiki is compiled from the BERIL Research Observatory's research corpus,
which is licensed AGPL-3.0, so the pipeline and the compiled pages carry
[the same licence](https://www.gnu.org/licenses/agpl-3.0.html). The licence
grants you rights to the text. It makes no claim that the text is correct.

## Source

The compiler, the editorial contract it enforces, and this corpus are at
[github.com/beril-doe/beril-wiki](https://github.com/beril-doe/beril-wiki).
