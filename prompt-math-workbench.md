# Reusable prompt — step-graded math workbench, study notes, and teaching pen

Persona: **Creator** for the drafting, with an **Assistant** pass for verification and auditing.
Tier: **Comprehensive** — all six blocks. A child uses this unsupervised, so a wrong answer or a
leaked hint does real damage.

Attach before sending: the problem set (PDF). If you have them, attach the class slides and the
transcript too — the transcript is usually worth more than the slides, because the teacher's own
phrasing, worked reasoning and throwaway teaching points live there.

---

## The prompt

**Role.** You are a math curriculum engineer who builds self-marking practice software for
competition-track elementary students. You care equally about mathematical correctness and about not
doing the child's thinking for him.

**Task.** From the attached problem set, build four self-contained HTML pages that work together as a
small site hosted from a GitHub Pages repo root:

1. `index.html` — landing page linking the other three, with a short explanation of how grading works.
2. `[topic-slug]-notes.html` — a reading page: the whole topic written out, the traps, worked examples,
   a cheat sheet and a glossary. No grading.
3. `[topic-slug]-lesson.html` — the workbench with concept text plus one guided problem per concept.
4. `[topic-slug]-practice.html` — the workbench with every problem from the attached set, no concept teaching.

Every page also carries the annotation pen described below.

**Context.**
- Student: `[grade]` grade, `[age]` years old, in `[program, e.g. AwesomeMath Academy Level 1]`.
  Arithmetic is reliable; he is learning to write out method rather than just answers.
- A parent sits with him and explains things on screen, which is what the pen is for.
- Source: the attached `[problem set file]`. `[If attached: the class slides and transcript — mine them
  for the teacher's explanations, vocabulary, worked examples, and teaching points the slides alone
  don't show.]`
- Topic scope: `[list the concepts]`.
- Every problem in the set appears. Do not drop, merge or simplify any of them, challenges included.
  If one sits far above the stated grade, keep it, split it into smaller steps, and flag it at the end.

**Requirements.**

### The two workbench pages — three-pane layout, one screen, no page scrolling on desktop

- **Top bar:** problem dropdown grouped by the set's own sections, prev/next arrows, a finished
  counter, a per-problem timer, links to the sibling pages.
- **Left rail:** every problem grouped by section, each with a live status dot (untouched / in
  progress / closed).
- **Middle pane, tabbed:** **Problem** · **Concept** (lesson page only, default tab there) ·
  **Rules** (practice page only — a one-screen reminder card, never a lesson) · **My steps** (live
  per-step status).
- **Right pane:** step pills, the current step's question, a line-numbered work editor, an answer
  field, and a dark feedback console underneath that logs every attempt.

### Step decomposition

1–6 steps per problem, following the mathematical argument, one quantity per step. Each step carries:
the question, an answer type (`factor` / `num` / `nums` / `choice` / `text`), three escalating nudges,
one hint, the revealed answer with its check, and a one-line note shown on success.

### The grading loop — implement exactly this

- He writes method in the editor and the result in the answer box, then presses **Check step**.
- Wrong → a nudge, escalating with each try. Three tries per step.
- After the third miss, one final attempt. Miss that and the step's answer is handed over with a push
  into the next step, which he still does himself.
- **Hint for this step** is a button opening a dialog with that step's hint. Hints appear *only* on
  press, never automatically, and asking does not consume a try. Record hint use in the tries readout.
- **Submit question** prints per-step feedback (right first try / right after n tries / answer given)
  and unlocks the verified answer only once every step is closed.
- **Show worked answer** needs an in-page two-click confirmation when steps are untried — no browser dialog.
- Answer checking is tolerant of form: accept `2^3*5*11`, `2*2*2*5*11`, `2³·5·11`, commas in large
  numbers, lists as `2, 5` or `2 and 2017`, letters for multiple choice, and short free text matched
  against a regex list with a reject list for the opposite answer. Name the specific error where
  possible: too big, too small, very close, "the product is right but some pieces are still
  composite", "right number of values but one is off".

### The notes page

Long-form reading with a sticky table of contents, containing in this order:

- **Every concept**, written out with worked numerical examples.
- **A tricky-bits section.** Ten to fifteen named traps, each drawn from a specific problem in this
  set, each saying what the wrong answer looks like and why it's tempting. The most valuable section
  on the page — do not pad it with generic advice.
- **Three to five problems worked end to end**, written the way a solution should be handed in, with
  the narrowing reasoning shown before any arithmetic.
- **A one-page cheat sheet** as a situation → move table.
- **A glossary** stating the vocabulary precisely, including the awkward ones (empty product,
  "ordered" triple, what "common" means).
- **A short section on write-up habits**, sourced from the class norms if the transcript is attached.
- At the end of each concept section, chips deep-linking to the problems that use it, e.g.
  `practice.html#q8`.

### The teaching pen (all four pages)

A floating **Pen** button opens an annotation layer so the parent can draw on the page while
explaining.

- **Tools:** four ink colours, three nib widths, a translucent marker, a straight line, a box, and an
  eraser. Holding Shift while drawing with the pen or marker snaps the stroke to a straight line.
- **Stroke quality:** smooth the path through the midpoints of consecutive samples rather than drawing
  raw polylines, and taper the width with stroke speed, smoothing the width between segments. Raw
  polylines look faceted and are immediately obvious.
- **Undo, redo, clear, and PNG export.** Clear is undoable. Ctrl/Cmd+Z and Ctrl/Cmd+Shift+Z work while
  the pen is on. State plainly in your summary that the export captures the ink only, not the page
  underneath, since rasterising the DOM would need a library.
- **Stylus-only toggle** that ignores `pointerType === 'touch'`, for a tablet with a resting palm.
- **Keyboard:** `P` toggles, `Escape` turns off, and both are suppressed while focus is in a textarea,
  input or select so they cannot corrupt his answers.
- **Anchoring, two modes:** on long reading pages the ink is stored in page coordinates and stays glued
  to the content, so the page can scroll with the pen still active (finger scrolls, stylus draws). On
  the workbench pages, where a problem fits on one screen and each pane scrolls separately, the ink is
  viewport-anchored and the layer swallows scrolling while the pen is on. Say which mode each page uses.
- **Ink is held per problem** on the workbench pages: switching problems parks the current ink and
  restores that problem's ink on return. Expose the layer as `window.INK` with `get` / `set` so the
  host page can do this.

**Performance is a requirement, not a nicety.** A naive implementation lags badly and it is the single
most likely thing to go wrong:

- Use **two viewport-sized canvases**: a committed layer for finished strokes, never touched while
  drawing, and a live layer for the stroke in progress. Append only the new points each frame; on
  pointer-up, draw the stroke once onto the committed layer and wipe the live layer.
- **Never size a canvas to the document.** A full-page canvas on a retina screen is tens of millions
  of pixels and a quarter of a gigabyte, and clearing it every frame is what kills the frame rate.
  Handle scrolling by re-rendering with a translate instead.
- **Never redraw all strokes per frame.** Per-frame cost must be proportional to the new points, not
  to the ink already on the page.
- Cap `devicePixelRatio` at 2, batch to one repaint per animation frame with a reentrancy-safe flag,
  and use `getCoalescedEvents` where available.
- Report a measurement: with roughly 40 strokes and 2,000 points already drawn, state how many old
  strokes are redrawn per frame while drawing (it should be zero) and the canvas megapixel count.

*Tone across everything:* plain, warm, matter-of-fact. Never gush, never scold. Nudges point at the
next question to ask, not at the child.

**Boundaries.**

### Nothing hint-like may be visible before the hint button is pressed

This is the rule that matters most, and it is easy to violate without noticing.

- Step questions are bare questions asking for a quantity. No "440 = 44 × 10, start with 44", no
  "substitute b = 2 and solve", no "factor all four, then take the biggest power of each prime". If a
  step cannot be asked without handing over the method, the method goes in the hint.
- If a problem's step breakdown only exists to walk him through a factor split, collapse it into one
  step and put the split in the hint. The walkthrough *is* the giveaway.
- The work-area placeholder is one generic line on every step. No per-step scaffold, no blanked-out
  template like `44 = ___ × ___`.
- Answer-box placeholders show format only and must never match the answer of the step they sit on.
  Check every one individually.
- Nudges never state the answer, in digits *or* in prime-power form. A nudge may set up the final
  calculation only if it ends in something he still has to compute.
- Hints give method and setup but stop short of the value. Only the post-final-attempt reveal states it.

### Audit for leakage programmatically, then report

Search every step question, nudge, hint and placeholder for that step's own answer in numeral form,
comma form, and factored/prime-power form. Report the hit count, fix the real ones, and list the false
positives rather than silently rewriting reasoning that legitimately mentions a number.

### Verification

- Compute every answer in Python before writing it into a page. Solve counting and enumeration
  problems by brute force *as well as* by argument, and confirm the two agree.
- Do not trust the source's answer key, and do not rely on remembering a competition answer.
- Every revealed answer includes its check, not just the number.

### Technical — the pages must survive a sandboxed iframe

- One self-contained HTML file per page: CSS, JavaScript and problem data inlined. No build step at
  runtime, no frameworks, no CDN except fonts.
- **Do not call any browser API that reaches outside the document, and guard the ones you do use.**
  No `localStorage` / `sessionStorage`, no `alert` / `confirm` / `prompt`, and wrap
  `history.replaceState` and `location.hash` access in try/catch, skipping them when
  `location.protocol === 'about:'`. In a sandboxed `about:srcdoc` frame each of these throws, and one
  unguarded call kills the whole script silently, leaving a blank pane. Confirmations happen in-page.
- URL-hash deep links (`#q8` opens problem 8, hash updates on navigation) behind those guards,
  degrading to "open the first problem" when blocked.
- Relative links only, so it works at a Pages subpath and from `file://`.
- Keyboard: Enter checks from the answer box, Ctrl/Cmd+Enter from the editor, Escape closes the hint
  dialog. Visible focus rings, ARIA labels on icon buttons and the dialog, responsive to a phone
  (panes stack, left rail becomes a toggle). Pen tools hidden when printing.
- Generate everything from a `build.py`, with problem data in separate Python modules and the
  answer-checking, layout and pen code shared between pages, so the set can be regenerated and extended.

*Design:* don't use the default AI look. Choose a palette and two typefaces that suit a math notebook
and commit to them. Avoid cream-and-terracotta, all-caps eyebrow labels, and identical rounded cards
with the same soft grey shadow.

**Reasoning.**

- Before writing any HTML, state your step decomposition for two or three representative problems so
  I can check the granularity.
- Show the Python verification output for every answer.
- After building, run scripted passes over the generated data and report the counts: one answering
  every step correctly on every problem; one missing a step four times, to prove the nudge → final
  attempt → handover path; one opening a hint mid-attempt; one exercising reveal and navigation; and
  one exercising the pen (each tool, palm rejection, undo/redo/clear, export, ink parked and restored
  per problem).
- Simulate the sandbox: run the same passes with `confirm` and `history.replaceState` throwing, and
  confirm nothing breaks.
- Report the pen performance measurement described above.
- List every element id the JavaScript touches and confirm each exists in the markup, on every page.
- Check that every internal link and anchor resolves, including the notes page's deep links.
- Close with: which problems sit above the stated grade, anything in the source you think is wrong or
  ambiguous, and any answer you could not verify independently.

---

## Notes on using this

- Fill the bracketed placeholders. The ones that matter most are the grade, the concept list, and the
  file-name slug.
- The four failure modes this prompt exists to prevent, in the order they cost the most time:
  hints leaking through question wording and placeholders; unverified answers; unguarded browser APIs
  blanking the page inside a sandboxed frame; and a pen that redraws everything every frame.
- Default is stateless — closing a tab clears progress and ink. If you want either to survive a
  reload, add it as a requirement and say where it lives, given the no-`localStorage` rule.
- To extend an existing set instead of starting fresh, replace the Task block with: *"Add the attached
  problems to the existing practice page, matching its step format, nudge and hint conventions, leakage
  rules and verification standard exactly, and update the notes page's traps section if these problems
  introduce new ones."*
- Deliberately left out of the pen, in case you want them later: a laser-pointer mode where strokes
  fade after a second, and shape recognition that straightens a rough circle.
