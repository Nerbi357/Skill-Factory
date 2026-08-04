# SIGNALS

Raw observations about how the work goes, recorded when they happen. Material,
not decisions — an entry becomes a change only at a review, and only if the owner
says so. The format and the rules are in `skills/signal-capture/`.

The owner speaks Russian; his words are translated as closely as the sentence
allows, keeping his structure. Nothing here is paraphrased.

---

## 2026-08-04 · correction · the mining method

What happened: the boundary between `verify-before-done` and `git-repo-structure`
was argued as an overlap because both fire at a phase close, and a rule was nearly
moved out of the skill that owns it.
Verbatim: "git-repo-structure is responsible only for the presentation and
contents of the repository, while verify-before-done and other skills are for the
work process itself; they use phases differently, you cannot merge this, you are
wrong."
Candidate: overlap is about the question a skill answers, not the moment it fires.
Two skills triggered by the same event are not neighbours unless they answer the
same question.
Confidence: strong — the owner's own correction, and the argument it overturned
was mine, made without reading the bodies.

## 2026-08-04 · correction · the mining method

What happened: a skill was proposed for adoption after checking only the `Covers`
and `Leaves out` declarations of what was already in force, not the file bodies.
Verbatim: "did you check that the verify-before-done you are putting into force
does not overlap other files, for example confidence-check? or will that be
checked later by an audit?"
Candidate: overlap is checked against the bodies of everything in force before a
skill enters, never deferred to an audit — an audit catches drift that
accumulated, not a collision present on day one.
Confidence: strong — asking the question found four real collisions that the
declaration check had missed.

## 2026-08-04 · correction · the library using its own artifacts

What happened: mining was being done by hand while `skill-creator`, the agent
whose job this is, sat unwired and unused.
Verbatim: "since you cannot mine skills off the cuff, let us wire up the
skill-creator agent, so that for each new skill it produces a summary — what to
change, what to add, what to fix."
Candidate: an artifact the library owns gets used on the library's own work. One
that is only described is decoration, and the fastest evidence about whether it
works is running it.
Confidence: strong — and it exposed that nothing in `.claude/` wired the agent up
at all.

## 2026-08-04 · correction · the plan

What happened: the mining plan proposed a target library size and a batch of
folders to decline unmined because they had no current need.
Verbatim: "target size — we have none, you must check each skill separately for
whether there is anything useful in it" · "the deferred pile — no, I disagree, you
must run each skill separately and try to extract something useful from each."
Candidate: no target count, and no batch dismissal. Every candidate is read on its
own, and "no current need" is a reason not to build on an idea yet, never a reason
to skip reading for it.
Confidence: strong — stated twice, in two forms, in one message.

## 2026-08-04 · friction · the working session

What happened: a plan was proposed grouping forty-six review folders into thirteen
thematic pull requests; the owner replaced it with one folder per exchange,
discussed before any file is written.
Candidate: the owner buys judgement per artifact, not throughput. A plan that
optimises for fewer pull requests optimises the wrong number.
Confidence: medium — one observation, and it may belong to the base phase rather
than being a standing preference.

## 2026-08-04 · correction · confidence-check

What happened: a worked example inside a skill — "1.06 s → 0.40 s on the real
dataset" — was reported as violating the rule that a drifting figure carries its
date.
Verbatim: "those are examples of phrasing, not examples; they can be reference
data."
Candidate: the dating rule governs facts being asserted, not illustrations of a
sentence shape. Dating an invented example would itself be inventing a specific,
which the same skill forbids more strongly.
Confidence: strong — and it inverts the finding rather than softening it.

## 2026-08-04 · correction · the mining method

What happened: two claims in a draft were listed as things to drop because they
overclaimed.
Verbatim: "this is exactly the point of mining — not simply copying phrasings, but
taking them apart into ideas and building them into existing skills, creating new
skills with the right ideas, even if the original phrasings in the draft material
were bad."
Candidate: mining takes ideas, not wording. A badly stated rule can carry a good
idea; restate it and judge the restatement. Only the idea being wrong, already
held, or not worth its space is grounds for leaving it.
Confidence: strong — it names the failure directly and it applies to every folder
still queued.

## 2026-08-04 · correction · the two layers

What happened: a rule was proposed for the owner-preferences layer because it was
phrased as his instruction, on the reasoning that restating it in the method's
voice would soften it.
Verbatim: "remove the exact phrase about tripling the time, keep the idea that it
matters. we are not moving it to preferences, it stays in the method, it is its
idea. my preferences are something else, more to do with the immediate style of
interaction than with the idea or the mechanism."
Candidate: the two layers split mechanism from manner, not "general" from "his".
An idea the owner supplied is still method and is argued on its merits; the
preferences layer is how he wants to be worked with.
Confidence: strong — it settles a line that had been drawn by attribution rather
than by subject.

## 2026-08-04 · correction · signal-capture

What happened: signals were recorded with the owner's Russian quoted verbatim and
an English rendering beneath.
Verbatim: "write them straight in English."
Candidate: the log is kept in the language of the library. Translating is not
paraphrasing, and a log the owner cannot skim is a log nobody reviews.
Confidence: strong — direct instruction about the mechanism's own format.

## 2026-08-04 · correction · skill-creator

What happened: the MINE report came back as an analysis of the source's defects
and a routing verdict, without the text being proposed for adoption.
Verbatim: "it should not be a silent breakdown of what we do with the skill and
what its errors are; it should be a detailed breakdown of every idea and phrasing,
what in them is useful and how we can use it — so that I can look over all the
useful blocks and ideas and give approval to include them in one file or another."
Candidate: a MINE report is a list of inclusions to approve, not a review of
someone else's work. Every surviving idea carries the actual wording proposed, its
destination file and section, and what already exists that touches it.
Confidence: strong — the report was accurate and still not usable for the decision
it was written for.

## 2026-08-04 · caught · skill-creator

What happened: the agent reported that `git-repo-structure` line 24 hands off "it
works" to a skill that does not exist, and recommended naming `verify-before-done`
there. The line is a contrast — the bar in the final phase rises above "it works"
— not a hand-off. The owner caught it: "what skill was it handing off to? it looks
clean to me."
Candidate: a cross-reference recommendation needs the sentence quoted and its
grammar stated, not just its subject. The agent's other findings were checked
against line numbers; this one was inferred from a paraphrase.
Confidence: strong — the first false positive from the agent, and it survived my
own reading of the report before the owner stopped it.

## 2026-08-04 · correction · the working session

What happened: a question was put to the owner as "should §7 reference
FINAL_PASS.md" without naming which file §7 belonged to or where that checklist
lives.
Verbatim: "when you write §7 referencing FINAL_PASS.md, say section 7 of which
file and which final_pass."
Candidate: a cross-reference names its file, every time, in reports as much as in
the artifacts. A bare section number is readable only by someone already holding
both texts — and the reader who needs the pointer is the one who is not.
Confidence: strong — it cost an exchange, which is the cheapest possible
demonstration of the cost.

## 2026-08-04 · correction · the overlap rule

What happened: one checklist item appearing in `git-repo-structure`'s final pass
and again in the new skill's boundary section was reported as the one genuine
textual duplicate, with a pointer offered as the alternative.
Verbatim: "no link, we keep the repeated item. each checklist is unique if it is
attached to a separate skill, so these are not repeats but different
manifestations of one logic."
Candidate: repetition across checklists belonging to different skills is not
duplication — each checklist is complete for its own skill's question, and a
pointer would invite exactly the merge the overlap rule refuses.
Confidence: strong — it extends the earlier overlap ruling to a case that ruling
did not obviously cover.

## 2026-08-04 · gap · skill-creator

What happened: nothing in the library re-checks which skills an agent should read
when a skill enters, changes, merges or splits. The agent proposed destinations
for every idea and never asked whether any agent in force should now consume the
result.
Verbatim: "I also want that when the agent adds a new skill, substantially changes
a current one, merges two, splits one into two, or does mining, it does not only
say which idea goes into which skill and section — but also checks whether a new
skill can be added to or removed from some existing agent (asking my opinion), or
if a new agent is being added, which skills to give it."
Candidate: agents consume skills, so every change to the library's shape leaves
some reading list possibly wrong, and nobody looks by default.
Confidence: strong — the gap is structural, and the first mining run walked
straight past it.

## 2026-08-04 · correction · skill-creator

What happened: the MINE report was accurate and complete but written as prose
blocks, so the owner had to reassemble the decision from it.
Verbatim: "I also do not like the form the mine report is presented in now: I want
it presented more structurally, and the questions about changes too."
Candidate: the report's shape is fixed rather than left to the agent — numbered
sections, ideas in one table, proposed text keyed to it, and questions carrying
options and a recommendation instead of being asked bare.
Confidence: strong — the second correction of this report in two runs, both about
usability rather than accuracy.

## 2026-08-04 · correction · the mining method

What happened: moving two rules out of a draft's owner-preferences section into
its method body was raised as a flag at the end of the report, on the reading that
the standing rule forbids mining from touching preferences.
Verbatim: "about the transfer between layers: this is the section on correcting a
working skill and skill-creator has that option, but it must explain them on equal
terms with the other ideas in the mine run."
Candidate: relocating a rule between layers is a correction, and the rule
protecting preferences protects their content, not their address. Every move is a
numbered row like any other idea — a change explained in a footnote is one the
owner did not review.
Confidence: strong.
