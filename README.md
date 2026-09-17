# Math Lab — build source

Generates four HTML pages for AwesomeMath Week 1 (prime factorization, GCF, LCM):
`index.html`, `prime-factorization-notes.html`, `prime-factorization-lesson.html`,
`prime-factorization-practice.html`.

## Build

```bash
python3 build2.py          # writes the four pages to /mnt/user-data/outputs
```

Change `OUT` at the top of `build2.py` to write somewhere else.

## Files

| File | What it holds |
|---|---|
| `build2.py` | The builder. Page templates for the landing and notes pages, the app shell assembly, the section→problem mapping, and `OUT`. |
| `assets2.py` | The workbench: CSS, the answer-checking engine (`JS_CHECK`), the app engine (`JS_APP`), the three-pane shell markup, and the ink/pen layer (`INK_CSS`, `INK_HTML`, `INK_JS`). |
| `practice_data.py` | The 24 problems of Set A1: prompt, steps, nudges, hints, revealed answers, verified answer + explanation. |
| `lesson_data.py` | The 14 guided problems, grouped by the ten lesson ideas. |
| `helpers.py` | `step()`, `pf_step()`, `gcf_step()` constructors and the yes/no regex lists. |
| `hint_overrides.py` | The anti-leakage layer. `ASK` rewrites step questions, `HINT_ADD` supplies the hints that replaced the old scaffolding, `STEPS` drops steps that only walked through a factor split, and `apply()` strips work-area scaffolds and normalises answer placeholders. **Edit rules here rather than un-picking the data modules.** |
| `notes_data.py` | Notes-page-only content: `TRAPS`, `WORKED`, `CHEAT`, `GLOSSARY`, `WRITEUP`. |
| `build.py`, `assets.py` | First-generation single-scroll pages. Kept only because `build2.py` reads the concept prose out of `build.py`'s `LESSON_BODY`. Do not ship its output. |
| `app.js`, `ink3.js`, `harness.js`, `text.js` | Node test harnesses with a hand-rolled DOM shim. `node app.js` answers every step of every problem and exercises the miss/hint/reveal paths; `node ink3.js` checks the pen and reports its per-frame drawing cost. |

## Adding problems

1. Append a `prob(...)` call in `practice_data.py` following the existing shape. Every step needs
   `ask`, `type`, `answer`, three `nudges`, a `hint`, a `solution`, and the problem needs a verified
   `answer` and `explain`.
2. Verify the answers in Python first, brute-forcing anything that counts or enumerates.
3. Add the problem's id to the right section in `build2.py` → `sections`.
4. If a question or nudge carries the method or the answer, fix it in `hint_overrides.py`.
5. Rebuild, then run `node app.js` and check for zero errors.

## House rules that are easy to break

- Nothing hint-like may be visible before the **Hint for this step** button is pressed: no scaffolded
  questions, one generic work-area placeholder, answer placeholders that show format only and never
  match their own step's answer, and nudges that never state the value in digits or prime-power form.
- No `localStorage`, `alert`, `confirm`, or `prompt`, and `history.replaceState` / `location.hash`
  must stay wrapped in try/catch — the pages run inside sandboxed iframes where those throw and one
  unguarded call blanks the page.
- The pen keeps finished strokes on a committed canvas and only the live stroke on a second canvas.
  Never size a canvas to the document, and never redraw all strokes per frame.
