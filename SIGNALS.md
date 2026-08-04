# SIGNALS

Raw observations about how the work goes, recorded when they happen. Material,
not decisions — an entry becomes a change only at a review, and only if the owner
says so. The format and the rules are in `skills/signal-capture/`.

The owner speaks Russian; his words are quoted exactly, with an English rendering
beneath. The quote is the record — the rendering is a convenience and may drift.

---

## 2026-08-04 · correction · the mining method

What happened: the boundary between `verify-before-done` and `git-repo-structure`
was argued as an overlap because both fire at a phase close, and a rule was nearly
moved out of the skill that owns it.
Verbatim: "git_repo_structure отвечает только за оформление и содержание
репозитория, а verify_before_done и другие скиллы - за сам процесс работы,
использование фаз у них разное, нельзя это мерджить, ты не прав"
*(git-repo-structure is only responsible for the repository's presentation and
contents, while verify-before-done and other skills are for the work process
itself; they use phases differently, you cannot merge this, you are wrong)*
Candidate: overlap is about the question a skill answers, not the moment it
fires. Two skills triggered by the same event are not neighbours unless they
answer the same question.
Confidence: strong — the owner's own correction, and the argument it overturned
was mine, made without reading the bodies.

## 2026-08-04 · correction · the mining method

What happened: a new skill was proposed for adoption after checking only the
`Covers` / `Leaves out` declarations of what was already in force, not the file
bodies.
Verbatim: "проверил ли ты, что вводимый в работу verify_before_done не
пересекается с другими файлами, например, с confidence_check? или это будет
проверяться потом аудитом?"
*(did you check that the verify-before-done you are putting into force does not
overlap other files, for example confidence-check? or will that be checked later
by an audit?)*
Candidate: overlap is checked against the bodies of everything in force before a
skill enters, never deferred to an audit — an audit catches drift that
accumulated, not a collision present on day one.
Confidence: strong — asking the question found three real collisions that the
declaration check had missed.

## 2026-08-04 · correction · the library using its own artifacts

What happened: mining was being done by hand while `skill-creator`, the agent
whose job this is, sat unwired and unused.
Verbatim: "раз ты не можешь сходу майнить скиллы, давай подключим агента
skill-creator, чтобы он по каждому новому скиллу выдавал резюме, что менять, что
добавлять, что править"
*(since you cannot mine skills off the cuff, let us wire up the skill-creator
agent, so that for each new skill it produces a summary — what to change, what to
add, what to fix)*
Candidate: an artifact the library owns gets used on the library's own work. One
that is only described is decoration, and the fastest evidence about whether it
works is running it.
Confidence: strong — and it exposed that nothing in `.claude/` wired the agent up
at all.

## 2026-08-04 · correction · the plan

What happened: the mining plan proposed a target library size and a batch of
folders to decline unmined because they had no current need.
Verbatim: "целевой размер - у нас нет его, ты должен каждый скилл проверять
отдельно, есть ли в нем что-то полезное или нет" · "отложенная куча - нет, не
согласен. ты должен будешь каждый скилл прогнать отдельно и из каждого
постараться извлечь что-то полезное"
*(target size — we have none, you must check each skill separately for whether
there is anything useful in it · the deferred pile — no, I disagree, you must run
each skill separately and try to extract something useful from each)*
Candidate: no target count, and no batch dismissal. Every candidate is read on
its own, and "no current need" is not a reason to skip extraction — only a reason
not to build on what is extracted yet.
Confidence: strong — stated twice, in two forms, in one message.

## 2026-08-04 · friction · the working session

What happened: a plan was proposed grouping forty-six review folders into
thirteen thematic pull requests; the owner replaced it with one folder per
exchange, discussed in chat before any file is written.
Candidate: the owner buys judgement per artifact, not throughput. A plan that
optimises for fewer pull requests optimises the wrong number.
Confidence: medium — one observation, and it may be specific to the base phase
rather than a standing preference.
