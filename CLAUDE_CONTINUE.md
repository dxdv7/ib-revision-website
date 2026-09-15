# Continue the Economics Quiz website

## Update 2026-09-15: Biology added as a full second subject

The user asked for the same full treatment (notes + quizzes + real SL/HL
split) applied to a second textbook: Andrew Davis, *Biology for the IB
Diploma* (3rd ed., 2023, Hodder — new 2025 syllabus), at
`/Users/davidbukraba/Desktop/Davis A. Biology for the IB Diploma 3ed 2023.pdf`
(868 pages). This is now live: Biology SL and Biology HL are active,
clickable cards on Home, each with a full 40-sub-topic chapter list, full
notes, and 1027 quiz questions with real HL-only filtering.

### Why this book was easier than the Economics one

Unlike the Economics PDF, this one has a genuine text layer (confirmed via
PyMuPDF), so no OCR/visual-page-reading was needed — raw text was extracted
directly per sub-topic via `page.get_text()`. It also follows the *new*
(2025) IB Biology syllabus structure: 40 numbered sub-topics across 4
themes (A/B/C/D, e.g. "A1.1 Water", "D4.3 Climate change" — see
`source/bio_raw/mapping.json` for the full number/code/name/HL-only
mapping), several of which are marked **entirely HL-only right in the PDF's
own table of contents** (A2.1, A2.3, A3.2, B3.3, C2.1, D2.2 — 6 total).
Even better: within each sub-topic, the textbook's own "SYLLABUS CONTENT"
list at the top explicitly tags individual numbered points as "(HL only)"
in the raw text itself (e.g. "A1.2.11 Directionality of RNA and DNA (HL
only)") — this gave a much more precise, authoritative signal for HL
tagging than the Economics book ever had, and the whole HL-detection
infrastructure built for Economics (`hl_wrap.py`'s chip-detection logic)
carried over and worked on the first real attempt on most files.

### How it was built (mirrors the Economics pipeline, streamlined)

1. Extracted raw text per sub-topic via PyMuPDF page ranges (from the PDF's
   `get_toc()`) into `source/bio_raw/01_A1.1.txt` … `40_D4.3.txt`, plus
   `mapping.json`.
2. Grouped the 40 sub-topics into 21 batches (by page-count budget, ~2-3
   sub-topics per group) and launched one background subagent per group.
   Unlike the Economics build, **notes AND quiz questions were written in
   the same agent pass** (not two separate phases) — each agent had the
   raw text plus the exact "(HL only)" syllabus points already given, so
   it could write correctly-tagged `hl:true` quiz questions immediately
   without a separate tagging pass. This saved an entire phase of work
   compared to how Economics was built.
3. Every prompt explicitly warned about the exact `</p>` vs `</div>` bug
   class discovered during the Economics build, and told agents to
   self-scan their own output before finishing. This worked well — many
   agents self-caught and fixed the bug themselves; only ~9 residual
   instances slipped through across all 21 groups, all found and fixed the
   same way as before (exact-string, uniqueness-verified edits).
4. Hit the same session rate limit multiple times over the course of the
   build (~3 separate times); each time, most in-flight agents had already
   saved their files before being cut off, and only the few that hadn't
   were individually re-launched (sometimes just for the missing half —
   e.g. re-running only the quiz-writing step when notes had already
   saved). No content was lost.
5. Final content: 40 sub-topics, 40 `notes-section`-per-topic-plus files
   with zero HTML errors, 1027 quiz questions with zero duplicates/zero
   malformed entries (3 incidental duplicate question *texts* — same
   concept legitimately tested in two different sub-topics with different
   phrasing — were found and reworded to be distinct), 387 of the 1027
   tagged `hl:true`. One tagging judgment call was corrected during review:
   an agent left 2 questions in the entirely-HL-only "Gene expression"
   sub-topic untagged because they felt too "basic" — fixed to `hl:true`,
   since the whole sub-topic isn't in the SL syllabus at all, so *nothing*
   from it should ever appear in an SL quiz regardless of how basic a
   specific question feels.

### How the site's code was generalized to support two subjects

This was the biggest actual code-design decision of this session. The
site's JS previously hard-baked "Economics" everywhere (`BANK`,
`NOTES_HTML`, `goEconomics()`, etc.). Rather than duplicate all of that for
Biology, the existing functions were generalized to read from
`state.subject` ("economics" | "biology"):

- `BANK`/`NOTES_HTML` (Economics) sit alongside new `BIO_BANK`/
  `BIO_NOTES_HTML` (Biology) — same shape, completely separate arrays/
  objects, so `ch:5` in one never collides with `ch:5` in the other.
- New helper functions `currentBank()`, `currentNotesHtml()`,
  `currentHlOnlyChapters()`, `currentSubjectLabel()`, `currentSubjectView()`,
  `currentSubjectNav()` all branch on `state.subject` — `filteredBank()`,
  `goNotes()`, `updateHlLocks()`, `renderCrumbs()` etc. now call these
  instead of touching `BANK`/`NOTES_HTML` directly, so both subjects share
  one code path.
- `chapterLabel(scope)` now returns `"Chapter "+scope` for Economics (same
  as before) or the sub-topic code (e.g. `"A1.1"`) from a new `BIO_CODE`
  lookup table for Biology.
- `ECON_HL_ONLY_CHAPTERS`/`BIO_HL_ONLY_CHAPTERS` are both computed via one
  shared `computeHlOnlyChapters(bank)` function (previously this was an
  Economics-only inline IIFE).
- New `<section id="view-biology">` with all 40 chapter cards, styled
  identically to `#view-economics`'s cards (same `.chapter-card` markup,
  same `data-notes`/`data-chapter` attributes) — a single shared
  `handleChapterListClick` function is bound to both `#view-economics` and
  `#view-biology`, so there's no duplicated click-handling code.
- New `goBiology()` mirrors `goEconomics()`; new `goSubjectChapters()`
  dispatches to whichever one matches `state.subject` (used by "back to
  chapters" and breadcrumb navigation so they return to the right
  subject's list).
- The Home page's "Biology SL"/"Biology HL" cards (previously disabled
  placeholders) now have `data-level="SL"/"HL"` **and** a new
  `data-subject="biology"` attribute (Economics's cards got
  `data-subject="economics"` added too) — the carousel's click handler
  reads both attributes and sets `state.level`/`state.subject` before
  calling `goSubjectChapters()`.
- **Bug fixed in passing**: `bestKey()` (the localStorage key for
  "personal best" tracking) previously didn't include `state.level` or
  `state.subject` at all — meaning Economics SL and Economics HL attempts
  on the same chapter were incorrectly sharing one "personal best" (and
  after this change, Economics chapter 5 and Biology chapter 5 would have
  collided too, since both use `ch:5`). Fixed to
  `state.subject+"-"+state.level+"-quiz-best-"+state.scope+"-"+state.count`.
- **Bug fixed in passing**: the in-quiz question chip (`els.qChip`, shown
  during an actual quiz question) had Ch19/Ch20-specific hardcoded text
  ("Chapter 19 — Unemployment"/"Chapter 20 — Inflation") that would have
  shown nonsense (or just been silently wrong) for every other chapter in
  both subjects. Now calls the same generic `chapterLabel()` used
  everywhere else, so it correctly shows e.g. "A2.3" during a Biology
  quiz question.

### Final verification performed

Same rigor as the Economics build: `node --check` on the full merged
script, zero non-ASCII characters across the entire ~4MB file, a full
`html.parser`-based tag-nesting validation (zero errors across the whole
file, not just the new Biology sections), zero duplicate element IDs, and
a Node-sandbox functional test confirming: Economics behaviour is
byte-for-byte unchanged (706/574 HL/SL counts, Ch12 still the only
Economics HL-only chapter), and Biology's numbers are all correct (1027/640
HL/SL counts, HL-only sub-topics `[3,5,7,17,23,33]` exactly matching the
textbook's own table of contents).

**Not visually tested** — same sandboxed-environment limitation as every
other UI change this project has had (no display access). If you get real
browser access, a good first check: Home → Biology SL card → click into a
few sub-topics' notes (especially one of the 6 entirely-HL-only ones, e.g.
"A2.1", which should show the "HL only, switch to Biology HL" message and
have its card visually locked in the chapter list) → Biology HL → same
sub-topic should show full content. Also worth clicking the "Full mix" card
in both subjects to confirm they don't cross-contaminate.

### Where things live

- `source/bio_raw/` — raw extracted textbook text per sub-topic (40 `.txt`
  files) + `mapping.json` (the number/code/name/HL-only reference table
  for all 40 sub-topics — useful if any content ever needs regenerating).
- `source/bio_notes/` — the 21 group-level notes files as originally
  written by agents (`gNN_....html`), plus a `split/` subfolder with the
  per-sub-topic files (`01.html`…`40.html`) actually merged into
  `index.html`. If any single sub-topic's notes need editing later, edit
  the file in `split/` and re-splice it into `index.html`'s
  `BIO_NOTES_HTML` object (find the `"N": ...` entry and replace).
- `source/bio_quiz/` — same structure: `gNN_....js` group files plus a
  `split/` subfolder with per-sub-topic question arrays (`01.js`…`40.js`)
  actually merged into `BIO_BANK`.
- The original textbook PDF is at
  `/Users/davidbukraba/Desktop/Davis A. Biology for the IB Diploma 3ed 2023.pdf`
  — not copied into the project folder (95MB, and PyMuPDF can always
  re-extract from it directly if ever needed).

## Update 2026-09-14 (night): real Economics SL/HL content split implemented

The user asked for Economics SL to genuinely exclude HL-only material (notes
and quiz questions), while Economics HL keeps everything. This is now built
and working — not just the two UI cards from before, but real filtering.

### How it works

- **Notes**: every chapter's notes HTML now wraps any HL-only content in
  `<div class="hl-only">...</div>`. A CSS rule `.sl-mode .hl-only{display:none
  !important;}` hides that content when `#notes-body` has the `sl-mode`
  class. `goNotes()` toggles that class based on `state.level`.
- **Quiz**: every question object in `BANK` that tests HL-only material now
  has `hl:true`. `filteredBank()` excludes `hl:true` questions whenever
  `state.level==="SL"`.
- **state.level**: new field in the global `state` object, `"SL"` or
  `"HL"`, default `"HL"`. Set when the user clicks the Economics SL or HL
  card on Home (`els.tileEconomicsSL`/`tileEconomicsHL` click handlers set
  it before calling `goEconomics()`), and persists through chapter
  navigation until they go back Home and pick a level again. The breadcrumb
  shows it, e.g. "Economics (SL)".
- **Edge case handled**: Chapter 12 (Monopoly and Oligopoly) is *entirely*
  HL-only in the real IB syllabus — all 28 of its quiz questions and all of
  its notes content are HL-only. In SL mode this chapter would otherwise
  show an empty notes page or a broken "0 questions" quiz screen.
  `buildCountOptions()` and `goNotes()` both detect this (empty filtered
  pool / empty rendered text) and show a friendly message instead
  ("This chapter has no Standard Level questions/content — it's Higher
  Level only. Switch to Economics HL from Home to access it.") with the
  Start Quiz button disabled. No other chapter is 100% HL-only, but any
  future one would be handled the same way automatically.

### How the HL-only content was identified and tagged

1. Wrote a script (`hl_wrap.py`, in the session scratchpad —
   `/private/tmp/claude-501/-Users-davidbukraba/a18c03b5-117a-48d3-b871-9a0ba6caacd8/scratchpad/hl_wrap.py`,
   copy it somewhere durable if you need to rerun this later) that finds
   every `<span class="chip">Higher Level</span>` marker already present in
   the notes (added when the notes were originally written) and wraps the
   right scope in `<div class="hl-only">`:
   - If the chip is in/before an `<h2>`: the whole `.notes-section` is
     HL-only.
   - If the chip is in/before an `<h3>` or `<h4>`: that sub-section (up to
     the next heading of the same-or-higher level) is HL-only.
   - Otherwise (chip inside a `<p>`, `<li>`, or `<div class="callout">`):
     just that element is HL-only.
   - A companion `hl_unwrap.py` reverses this — useful if the wrapping
     logic ever needs to be rerun with fixes (which happened twice this
     session, see below).
2. Ran it across all 30 external chapter files
   (`source/notes/ch01.html`...`ch32.html`, excluding 19/20) and, separately,
   directly on the Ch19/Ch20 content inline in `index.html`. Result: 46
   whole-section wraps, 10 h3-chunk wraps, 1 h4-chunk wrap, 6 inline-element
   wraps, 74 chip occurrences total across the 30 files (plus 3 more in
   ch19/20) — zero left unresolved.
3. For the quiz questions: extracted the HL-only topic list per chapter,
   then ran 15 parallel background subagents (one per chapter-group, same
   grouping as the original notes-writing task), each given its chapter's
   already-wrapped notes (the `hl-only` divs are the ground truth) plus its
   existing quiz question file, with strict instructions to ONLY add
   `,hl:true` to questions that test HL-only material — never touch `q`,
   `choices`, `explain`, ordering, or the `QUIZ_START`/`QUIZ_END` markers.
   6 chapter-groups needed no agent at all (ch10/11, ch14, ch15/16, ch18,
   ch21, ch30 have zero HL-only content — confirmed programmatically first,
   which saved 3 unnecessary agent calls). Ch19/Ch20 (only 72 questions,
   hand-written directly in `index.html`) were tagged directly by hand
   rather than via an agent, since the scope was small.
4. Result: **132 of 706 questions tagged `hl:true`** across all 32
   chapters. Verified: `node --check` valid, 706 total questions unchanged,
   zero duplicates, zero malformed entries, zero non-ASCII characters
   anywhere in the file, zero HTML tag-nesting errors.

### Real pre-existing bugs found and fixed along the way (unrelated to SL/HL, but blocking it)

While building the HL-wrapping script, discovered the notes markup had to
be 100% structurally valid for the div-boundary-matching logic to work
reliably — running a strict `html.parser`-based validator surfaced **17
genuine pre-existing bugs across 12 chapters** (ch03, ch07, ch09, ch10,
ch13, ch14, ch17, ch22, ch24, ch27, ch30, ch31) that had been present since
the original notes-writing session and were NOT caught by that session's
"div open-count == div close-count" check (because most of these bugs swap
a `</p>` for a `</div>` or vice versa on ADJACENT elements, which keeps the
total counts balanced while still being structurally wrong — e.g. a
callout box merging with the paragraph after it). All 17 were individually
diagnosed and fixed with exact-string, uniqueness-verified edits (not a
blanket regex) to avoid any risk of corrupting correct content nearby.
Also found and fixed: two genuinely orphaned, contentless
`<span class="chip">Higher Level</span>` fragments sitting outside any
section at the very top of `ch10.html` and `ch11.html` (deleted, they had
no accompanying content), and one more spurious extra `</div>` in `ch10.html`
unrelated to any of the above. **Net result: all 30 chapter notes files
now pass strict HTML validation with zero errors** (they didn't before,
even though the site "looked fine" — browsers silently auto-correct stray
tags, which is exactly why this had gone unnoticed).

If you ever add more chapters or re-run notes generation, it would be
worth running the same `html.parser`-based strict check (see any of the
Python snippets used throughout this session for the pattern) rather than
just checking that div-tag counts balance — that check alone provably
misses real bugs, as this session found the hard way.

### Where things live now (updated)

- `source/notes/ch01.html`...`ch32.html` (excl. 19/20): now contain the
  `hl-only`-wrapped, markup-bug-fixed version — this superseded and
  replaced the pre-SL/HL-split versions mentioned in the update below.
- `source/quiz/quiz_ch01-02.js`...`quiz_ch32.js`: now contain the `hl:true`
  tags — superseded the pre-tagging versions mentioned below.
- Both were kept in sync with what's merged into `index.html` — verified
  identical counts, not just "should match."

## STANDING INSTRUCTION from the user (2026-09-14, applies to all future work)

The user has explicitly asked that ALL work from now on be saved directly
and immediately into this folder (`/Users/davidbukraba/Desktop/Economics
Quiz/index.html`) as it happens — not just at session end. If a session
runs out of time/limit mid-task, whatever has been completed so far MUST
already be saved here (not stranded in the ephemeral scratchpad). In
practice this means: edit `index.html` in THIS folder directly (not a
scratchpad copy first), verify, and only copy to the scratchpad as a
secondary sync step — the reverse of a "copy in at the end" workflow. Keep
doing this for every future change, however small.

## Update 2026-09-14 (evening): "IB Revision" page title added

Added a big, bold title reading "IB Revision" (`<p class="site-title">`,
Fraunces serif, `clamp(30px,6.5vw,42px)`, bold) as the very first element
inside `.wrap` — so it appears above everything else, on every view (Home,
Economics, Notes, Setup, Quiz, Results alike), not just the Home hero.
This is separate from and sits above both the small compact header
(`#site-header`, "Revision Deck" eyebrow + "Study by subject") and the big
Home-only hero ("What do you want to revise?") added in the redesign
below — all three now coexist, ordered: IB Revision (always) → compact
header (all views except Home) → Home hero (Home only) → page content.

## Update 2026-09-14 (later same day): Quizlet-style home page redesign

The user shared a screenshot of quizlet.com's homepage and asked for the
Home view's layout to match it ("keep the same colour" — i.e. reuse this
site's own existing teal/gold/green/plum/red palette, not Quizlet's
blue/purple/orange). Done:

- Home view replaced: a big centered hero ("What do you want to revise?" +
  subtitle + pill CTA button) sits above a horizontally-scrollable row of
  large rounded subject cards (one per subject tile), each with a solid
  brand-color background, a bold title, and a small white "preview" inset
  box — directly modelled on Quizlet's card row, including left/right
  scroll-arrow buttons (`#carousel-prev`/`#carousel-next`).
- The 6 subject cards reuse the site's own existing accent hues 1:1 (no new
  colors introduced): Economics=teal, Polish=plum, English=red,
  Biology=green, Business=gold, Maths AI=teal-deep. These are declared as
  new FIXED tokens (`--chip-teal`, `--chip-plum`, etc.) in the CSS `:root`
  block, deliberately NOT redefined per light/dark theme (like a brand
  mark) — see the CSS comment above them for why, and don't "fix" this by
  making them theme-reactive; it's intentional so white card text stays
  legible in both themes.
- The old compact header (`#site-header`, "Revision Deck" / "Study by
  subject") still exists and still shows on every non-home view exactly as
  before (Economics, Notes, Setup, Quiz, Results) — it's now just hidden
  specifically on the Home view (`hideAllViews()` shows it by default,
  `goHome()` hides it) since the new big hero replaces it there.
- The `active`/`disabled` states, the `id="tile-economics"` click target,
  and the whole rest of the navigation/quiz engine are unchanged — only the
  Home view's markup and CSS changed.

**Also fixed in this pass (unrelated to the redesign, found while reading
the code):** `showResults()` had a hardcoded `byCh = {19:.., 20:..}` — it
would throw and crash the results screen for any quiz on chapters 1-18,
21-32, or the "Full mix — all 32 chapters" option, since those all
include chapter numbers the hardcoded object didn't have keys for. Fixed
to build `byCh` dynamically from whatever chapters actually appear in
`state.results`, using the existing generic `chapterLabel()` function for
the breakdown labels. This was a real, session-breaking bug that predates
this session but had gone untested until now — worth a real browser test
if you get display access (take any non-19/20 chapter's quiz through to
the results screen).

**Not visually tested** — same sandboxed-environment limitation as every
other UI change in this project so far (no display access;
`screencapture` fails). Verified only structurally: JS syntax
(`node --check`), zero non-ASCII characters, zero HTML tag-nesting errors
(`html.parser`), zero duplicate element IDs, and that every new/moved
element referenced by JS (`hero-cta`, `carousel-prev`, `carousel-next`,
`subject-carousel`, `tile-economics`, `site-header`) actually exists in the
markup. If you get real browser access, load the site and check: the hero
renders and its button navigates to Economics; the card row scrolls (both
via the arrow buttons and by dragging/swiping); disabled cards look muted
and don't navigate; and both light and dark OS theme look right (the fixed
chip colors should look identical in both — that's intentional, see above).

---


The live website is `index.html` in this folder — a single self-contained
HTML file (no build step). Also published as a Claude Artifact at:
`https://claude.ai/code/artifact/fa03b988-91e3-4cd9-903d-082f93799440`

## Status as of 2026-09-14 (afternoon session): quizzes added for all 32 chapters

Following the earlier full-notes expansion (see history below), the user
asked for a quiz to be created for every chapter. This is now done.

### What was done

1. **634 new multiple-choice questions written**, covering all 30 chapters
   that previously had notes-only cards (Chapters 1-18 and 21-32). Combined
   with the original 72 questions for Ch19/20, the site's `BANK` array now
   has **706 questions across all 32 chapters**.
2. **Generation approach**: 18 parallel background subagents (same grouping
   as the earlier notes-writing task), each given the already-extracted
   chapter notes HTML (`chapters_split/chNN.html`) as source material and a
   strict format contract matching the site's existing `BANK` entry shape
   (`{ch:N,q:"...",choices:[...4 items...],explain:"..."}`, HTML entities
   for punctuation, `−` JS escape for minus signs, no backticks, no
   raw Unicode). Each agent saved its own output directly to a
   `quiz_chNN.js` file in the scratchpad rather than just returning text in
   chat — this was a deliberate fix for the exact problem that bit the
   earlier notes-writing task (agents whose final response never got
   captured before a session limit hit).
3. **Handled partial failures cleanly**: several agents hit a
   `rate_limit`/session-limit error and reported `status: failed`, but 17 of
   18 had already written their file successfully before hitting the limit
   — only Chapter 28-29's file was genuinely missing, and it was
   regenerated in a single retry once the rate limit reset. No data was
   lost.
4. **Found and fixed one real bug across 4 of the 18 files**: some agents
   used a literal Unicode minus sign (U+2212) instead of the required
   `−` JS escape (this is the same character-encoding bug class from
   the original Ch19/20 mojibake fix, just a different character). Fixed
   by replacing all literal `−` with the `−` escape in
   `quiz_ch10-11.js`, `quiz_ch13-14.js`, `quiz_ch15-17.js`, and
   `quiz_ch21-22.js` before merging.
5. **Validated everything before merging**: every file was syntax-checked
   with `node --check` (wrapped in a throwaway array literal), every
   question object was `eval`'d and checked for exactly 4 choices plus
   non-empty `q`/`explain` fields, and all 706 questions (across all 18
   files plus the original 72) were checked for duplicate question text —
   zero errors, zero duplicates.
6. **Merged into `index.html`**: appended all 634 new question objects to
   the end of the `BANK` array (before its closing `];`).
7. **Updated the chapter-card UI**: all 30 previously notes-only chapter
   cards now also have a "Start quiz" button (`data-chapter="N"`) and their
   meta text was updated from "full notes" to "{count} questions &middot;
   full notes" with the real per-chapter question count. No JS changes were
   needed for this to work — the site's click handler already delegates
   generically on `button[data-chapter]`, and `buildCountOptions()` already
   computes quiz-length choices dynamically from whatever pool size it's
   given.
8. **Fixed a UI honesty issue this surfaced**: the "Full mix" card used to
   say "both chapters / 72 questions", but `filteredBank("both")` returns
   the *entire* `BANK` array — so now that `BANK` has 706 questions across
   32 chapters, that card was silently pulling from everything. Relabelled
   it "Full mix &mdash; all 32 chapters" / "706 questions" to match reality
   rather than leaving a misleading label.
9. **Full re-audit after every merge step**: `node --check` on the
   extracted script, a whole-file non-ASCII character scan (zero found),
   and a full HTML tag-nesting validation via Python's `html.parser` (zero
   errors, nothing unclosed) — all clean.
10. **Published** to the Artifact (now version 5) and copied to this
    folder's `index.html`.

### Per-chapter question counts (for reference)

Ch1:20, Ch2:20, Ch3:20, Ch4:20, Ch5:18, Ch6:16, Ch7:17, Ch8:24, Ch9:24,
Ch10:20, Ch11:20, Ch12:28, Ch13:20, Ch14:20, Ch15:17, Ch16:17, Ch17:18,
Ch18:21, Ch19:32 (original), Ch20:40 (original), Ch21:19, Ch22:23, Ch23:20,
Ch24:20, Ch25:20, Ch26:20, Ch27:20, Ch28:21, Ch29:20, Ch30:25, Ch31:48,
Ch32:18. Total: 706.

**Not tested:** actual visual/browser rendering, same limitation as before
— this sandboxed environment has no display access. All verification was
structural/programmatic (JS syntax, question-object shape, duplicate
detection, character encoding, HTML tag nesting). If you have real browser
access, a good first check would be: open the site, go to a few new
chapters (e.g. Chapter 9, Chapter 31), click "Start quiz", answer a
question or two, and confirm the shuffle/scoring/results flow works exactly
like it already does for Chapter 19/20 (it should — it's the same generic
engine, just with a bigger `BANK`), and spot-check that the "Full mix / all
32 chapters" quiz draws questions from multiple chapters, not just 19/20.

## Where things live

- `index.html` (this folder) — the live site: 32 chapters of notes + 706
  quiz questions across all 32 chapters. **This is the only file that
  matters for the actual deployed/published site.**
- `source/` (this folder) — **durable backup of everything that was merged
  into `index.html`**, copied here from the session's ephemeral scratchpad
  (`/private/tmp/...`, which is NOT persistent and could be wiped between
  sessions) specifically so this content survives even if that temp
  directory disappears:
  - `source/notes/ch01.html` … `ch32.html` (30 files) — the per-chapter
    revision notes HTML fragments, one per chapter, exactly as merged into
    `index.html`'s `NOTES_HTML` object. (Ch19/Ch20 aren't here since their
    notes were hand-written directly into `index.html` from the start and
    never existed as separate files.)
  - `source/quiz/quiz_ch01-02.js` … `quiz_ch32.js` (18 files) — the raw
    quiz-question JS object arrays, grouped by the same chapter groupings
    used during generation, exactly as merged into `index.html`'s `BANK`
    array. (Ch19/Ch20's original 72 questions are hand-written directly in
    `index.html` and never existed as separate files either.)
  - Verified byte-identical to what was actually merged in (see the
    diff check run right after copying).
  - If any single chapter's notes or quiz ever need editing in isolation,
    edit the file here, then manually re-splice it into `index.html`'s
    `NOTES_HTML`/`BANK` (find the matching `"N": ...` or `{ch:N,...}`
    entries and replace).
- The 18 original PDF slices used to generate the notes (only needed if
  notes ever need to be regenerated from scratch — NOT copied here since
  they're large (~136MB) and are trivially re-derivable from the user's own
  `economics textbook.pdf` on the Desktop, which is the real source of
  truth): they currently still exist in the session's scratchpad at
  `.../scratchpad/group_pdfs/g01_ch01-02.pdf` … `g18_ch32.pdf`, but that
  location is ephemeral — if you need them and they're gone, re-split the
  textbook PDF by chapter page ranges using PyMuPDF, as the original
  session did.

## What's still NOT done / possible follow-ups (don't start unprompted)

- No visual/browser QA pass (see above) — do this first if the user reports
  anything looking wrong, or if you gain display access.
- The chapter cards' question-count meta text is now accurate as of this
  merge, but is still hand-written, not computed live from `BANK.length` —
  it will go stale again if anyone hand-edits `BANK` later without also
  updating the card text.
- Other subject tiles (Polish/English/Biology/Business/Maths AI) remain
  disabled placeholders, untouched.
- This project is now feature-complete relative to everything the user has
  asked for so far (quiz + notes covering all 32 chapters). No pending work
  unless the user requests something new.

Do not push anything anywhere, don't touch passwords/credentials, and don't
start unrelated work unless the user asks for it.
