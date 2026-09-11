# About This Wiki

This is an AI-generated wiki. A pipeline built every page on this site from the
BERIL Research Observatory's corpus of AI-conducted microbial-biology research
reports.

It is partially reviewed. Scientists have checked some of the research
underneath these pages, but no one reviewed the pages themselves before they
went up, and nothing marks which claims fall on which side of that line. Do not
assume anyone checked a particular claim. Read the rest of this page before you
cite anything here.

## What you are reading

The BERIL Research Observatory's AI agents produced the 75 reports in this
corpus. Most of them worked over the
[KBase Data Lakehouse](https://hub.berdl.kbase.us): pangenomes, RB-TnSeq
fitness assays, biochemistry, and environmental metadata. A few analysed data
brought from elsewhere, user-provided sequencing among it, and each report
states what it used. None of them generated new laboratory measurements.
For each report the pipeline writes a summary, works out which
synthesis pages it belongs on, and rewrites those pages to absorb it. A claim
therefore gathers evidence from every project that supports it, rather than
appearing once per project.

Every page states which kind it is, on the line above its title. Where a page
cites evidence, "Projects cited" lists the project reports it rests on, and
the numbered marks in the prose point into that list.

**Project reports.** One page per research project, summarising it and linking
to its raw report. These are the evidence: everything else on the site cites
them, and nothing cites anything else.

**Cross-project digests.** Two pages — discoveries and pitfalls — reading
across the whole corpus rather than summarising one project.

**Raw reports.** The reports themselves, unedited, behind each summary.

**Concepts.** Recurring ideas, each gathering evidence from every project that
speaks to it.

**Entities.** Specific named things: organisms, genes and pathways, compounds,
methods, and datasets.

**Topics.** Hubs that group related concepts. Each opens with a
literature-context section whose citations were checked against PubMed.

**Conflicts.** Places where projects in the corpus disagree, with the evidence
on each side and the work that would settle it.

## What the evidence label means

Synthesis pages carry a computed line under the title:

> **Evidence** · 5 source projects · well corroborated · conflict on record · literature context

Every part of it is counted, not judged:

| Term | Means |
| --- | --- |
| *N source projects* | distinct projects the page's prose actually cites |
| *single-source* | one project, so nothing here corroborates the claim |
| *corroborated* | 2 or 3 projects |
| *well corroborated* | 4 or more projects |
| *conflict on record* | the corpus records a disagreement spanning these same sources |
| *literature context* | the page opens with a literature-context section |

**This is not a confidence rating and not a review status.** "Well corroborated"
means several projects here point the same way. It does not mean the finding is
correct, and it does not mean anyone checked. Projects in this corpus share data
sources, tooling and methods, so agreement between them proves less than it
appears to. Several conflict pages exist because results that pointed the same
way turned out to rest on one shared confound.

## What is checked, and what is not

Every build checks these, and a failure stops publication:

- Every `[src:]` citation resolves to a real source document.
- Every number in a cited paragraph appears in a source that paragraph cites.
  The pipeline re-runs a page that fails against its own sources, and rejects
  the page if it fails twice.
- Every `[[wikilink]]` resolves. Dead ones become plain text.

Nothing checks these:

- Whether a finding is scientifically correct.
- Whether a statistical method suited its data.
- Whether the underlying research report reached a sound conclusion.
- Whether a synthesis fairly represents the projects it draws on.

One check runs when a page is written and not again at publication: the pipeline
verifies literature-context citations against PubMed by PMID at that point. The
*literature context* term only records that such a section exists.

The numeric check is real, and narrow. It proves a figure appears in a source
the paragraph cites. It compares figures as text, so it misses a flipped sign or
a changed unit, and it skips small integers. It never shows the source was right.

## Known limitations

The pipeline merges two entity pages only when something identifies them as the
same entity: a shared canonical name, a declared alias, or a shared external
identifier. It never merges on similarity, which over these pages cannot tell
two genes of one organism apart. Two pages naming the same thing without any of
those signals stay separate. Entities that only one project cites do not appear
here at all.

Reported budget figures undercount what a run actually spends, so the cost notes
in the repository are lower bounds.

## The data this rests on

Most projects in this corpus ran over the
[KBase Data Lakehouse](https://hub.berdl.kbase.us), the data platform of the
[Department of Energy Systems Biology Knowledgebase (KBase)](https://www.kbase.us/).
The pangenomes, fitness assays, genome annotations, amplicon surveys, metabolic
models and metadata that those reports analyse are KBase's, not this project's.
A few projects analysed data from elsewhere instead, and each one says so.
Little on this site would exist without the lakehouse.

<p class="ack"><a href="https://www.kbase.us/"><img src="assets/kbase-logo.svg" alt="KBase" width="190"></a></p>

KBase asks to be cited as:

> Arkin AP, Cottingham RW, Henry CS, et al. KBase: The United States Department
> of Energy Systems Biology Knowledgebase. *Nature Biotechnology*. 2018;36:566.
> [doi:10.1038/nbt.4163](https://doi.org/10.1038/nbt.4163)

Cite that alongside anything you take from this wiki that rests on lakehouse
data, which is all of it.

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

For a finding, cite the underlying research report rather than the synthesis
page that aggregates it. Every summary page links to its report.

## License

This wiki is compiled from the BERIL Research Observatory's research corpus,
which is licensed AGPL-3.0, so the pipeline and the compiled pages carry
[the same licence](https://www.gnu.org/licenses/agpl-3.0.html). The licence
grants you rights to the text. It makes no claim that the text is correct.

## Source

The compiler, the editorial contract it enforces, and this corpus are at
[github.com/beril-doe/beril-wiki](https://github.com/beril-doe/beril-wiki).
