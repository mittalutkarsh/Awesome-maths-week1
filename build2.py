import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from assets2 import CSS, JS_CHECK, JS_APP, HEAD, SHELL, TAIL, INK_CSS, INK_HTML, INK_JS
from lesson_data import G
from practice_data import P
import hint_overrides
import notes_data
import build as old   # LESSON_BODY holds the concept sections

OUT = "/mnt/user-data/outputs"
INDEX = "index.html"
NOTES = "prime-factorization-notes.html"
LESSON = "prime-factorization-lesson.html"
PRACTICE = "prime-factorization-practice.html"

IDEA_KEYS = ["primes", "factorize", "factors", "gcf", "lcm",
             "identity", "backwards", "parity", "powers", "words"]


def concepts():
    """id -> (title, html) for the ten lesson sections."""
    secs = re.findall(r'<section class="lesson" id="s(\d+)">(.*?)</section>',
                      old.LESSON_BODY, re.S)
    out = {}
    for n, html in secs:
        html = re.sub(r'<div id="host-[a-z]+"></div>', '', html)
        title = re.search(r'<h2>(.*?)</h2>', html).group(1)
        out[IDEA_KEYS[int(n) - 1]] = (title, html.strip())
    return out


REFERENCE = """
<h1>Rules you already know</h1>
<p class="dimtext">A reminder card, not a lesson. The full explanations live on the lesson page.</p>
<div class="rulebox"><p><b>Prime factorization.</b> Split the number into any two factors and keep
splitting until every piece is prime. The result is the same whichever split you start from.</p></div>
<div class="rulebox"><p><b>GCF.</b> Primes in <b>both</b> numbers, each at its <b>smaller</b> power.</p></div>
<div class="rulebox"><p><b>LCM.</b> <b>Every</b> prime in either number, each at its <b>bigger</b> power.</p></div>
<div class="rulebox"><p><b>Identity.</b> a \u00b7 b = GCF(a, b) \u00b7 LCM(a, b).</p></div>
<div class="rulebox"><p><b>Squares and cubes.</b> Perfect square \u2192 every exponent even.
Perfect cube \u2192 every exponent a multiple of 3.</p></div>
<div class="rulebox"><p><b>Primes in equations.</b> If the equation forces a prime to be even it is 2.
If every term but one is divisible by d, that last one is too. Then bound the rest and check the survivors.</p></div>
<div class="rulebox"><p><b>Word problems.</b> Cycles lining up \u2192 LCM. A pile split into equal groups \u2192 GCF.
Same remainder every time \u2192 LCM, then add or subtract.</p></div>
<h2>Typing answers</h2>
<p>Products use <span class="m">*</span> and powers use <span class="m">^</span>, so 2\u00b3 \u00b7 5 \u00b7 11 is
<span class="m">2^3*5*11</span>. <span class="m">2*2*2*5*11</span> works too. Lists: <span class="m">2, 5</span>.</p>
"""


def initial(app):
    """Static first-paint markup so the page is readable before/without JS."""
    p = app["problems"][0]
    chips = "".join('<span class="chip %s">%s</span>' % (t.get("k", ""), t["t"])
                    for t in p.get("tags", []))
    if app.get("startTab") == "concept" and p.get("concept"):
        desc = p["concept"]
    else:
        desc = ('<h1>%s</h1><div class="chips">%s<span class="chip">%d steps</span></div>'
                '<div class="qbody">%s</div>' % (p["label"], chips, len(p["steps"]), p["prompt"]))
    tabs = "".join('<button%s>step %d</button>' % (' class="on"' if i == 0 else '', i + 1)
                   for i in range(len(p["steps"])))
    prompt = ('<span class="lab">step 1 of %d</span>%s'
              % (len(p["steps"]), p["steps"][0]["ask"]))
    picker = ""
    for g in app["groups"]:
        picker += '<optgroup label="%s">' % g["title"]
        for pid in g["items"]:
            q = next(x for x in app["problems"] if x["id"] == pid)
            picker += '<option value="%s">%s</option>' % (pid, q["label"])
        picker += "</optgroup>"
    side = ""
    for g in app["groups"]:
        side += "<h3>%s</h3><ol>" % g["title"]
        for pid in g["items"]:
            q = next(x for x in app["problems"] if x["id"] == pid)
            side += ('<li><button><span class="dot">\u25cb</span><span>%s</span></button></li>'
                     % q.get("short", q["label"]))
        side += "</ol>"
    conc = app.get("startTab") == "concept" and p.get("concept")
    return dict(desc0=desc, steptabs0=tabs, prompt0=prompt, side0=side, picker0=picker,
                on_problem="" if conc else ' class="on"',
                on_concept=' class="on"' if conc else "")


INDEX_CSS = """
:root{--ink:#11242b;--ink-soft:#4a626c;--paper:#eef2f3;--card:#fff;--rule:#d3dcdf;
  --teal:#0d6b6e;--teal-dark:#094f52;--gold:#b1820f;--gold-soft:#fff5dd;
  --mono:"IBM Plex Mono",ui-monospace,Menlo,monospace;}
*{box-sizing:border-box}
body{margin:0;color:var(--ink);background:var(--paper);
  background-image:linear-gradient(to right,rgba(13,107,110,.07) 1px,transparent 1px),
    linear-gradient(to bottom,rgba(13,107,110,.07) 1px,transparent 1px);
  background-size:26px 26px;
  font-family:"Atkinson Hyperlegible","Segoe UI",system-ui,sans-serif;font-size:17px;line-height:1.6}
main{max-width:760px;margin:0 auto;padding:44px 20px 70px}
h1{font-family:Fraunces,Georgia,serif;font-size:clamp(32px,6vw,46px);line-height:1.12;margin:0 0 12px}
h2{font-family:Fraunces,Georgia,serif;font-size:21px;margin:0 0 6px}
p{margin:0 0 14px;max-width:64ch}
.kicker{font-family:var(--mono);font-size:13px;color:var(--teal-dark);margin:0 0 16px;letter-spacing:.04em}
.lede{font-size:19px;color:var(--ink-soft)}
.cards{display:grid;gap:16px;margin:26px 0 30px}
a.card{display:block;background:var(--card);border:1px solid var(--rule);border-left:5px solid var(--teal);
  border-radius:4px;padding:20px 22px;text-decoration:none;color:inherit;box-shadow:0 1px 0 #dbe3e6}
a.card:hover{border-left-color:var(--gold);background:#fcfdfd}
a.card:focus-visible{outline:3px solid var(--teal);outline-offset:2px}
a.card .go{font-family:var(--mono);font-size:13px;color:var(--teal-dark)}
a.card p{margin:6px 0 10px;color:var(--ink-soft);font-size:16px}
.tags{display:flex;gap:7px;flex-wrap:wrap;margin-top:4px}
.tag{font-family:var(--mono);font-size:11.5px;padding:3px 8px;border-radius:99px;
  border:1px solid var(--rule);color:var(--ink-soft)}
.note{background:var(--card);border:1px solid var(--rule);border-radius:4px;padding:18px 22px}
.note ul{padding-left:20px;margin:8px 0 0}
.note li{margin:5px 0}
code{font-family:var(--mono);font-size:.9em;background:#f1f6f6;border:1px solid #e0e9e9;
  border-radius:4px;padding:1px 5px}
footer{color:var(--ink-soft);font-size:14.5px;margin-top:30px}
"""

INDEX_TPL = """<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Math Lab \u2014 Prime Factorization, GCF and LCM</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700&family=Atkinson+Hyperlegible:wght@400;700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>%(css)s</style>
</head><body data-ink-mode="document"><main>
<p class="kicker">AwesomeMath Academy \u00b7 Week 1 \u00b7 Level 1</p>
<h1>Prime factorization,<br>GCF and LCM</h1>
<p class="lede">Two workbenches. Read an idea, then solve it one step at a time, with a nudge
when a step goes wrong and a hint only when you ask for one.</p>

<div class="cards">
  <a class="card" href="%(lesson)s">
    <h2>Lesson and guided practice</h2>
    <p>Ten ideas, from primes and factor trees through GCF, LCM, working backwards,
    primes in equations, and perfect squares and cubes. Each idea has a guided problem
    beside it. Start here.</p>
    <span class="go">open the lesson \u2192</span>
    <div class="tags"><span class="tag">10 ideas</span><span class="tag">14 guided problems</span></div>
  </a>
  <a class="card" href="%(notes)s">
    <h2>Study notes</h2>
    <p>The whole topic written out: why the GCF and LCM rules work, the twelve traps that cost marks,
    four problems worked end to end, a cheat sheet and a glossary. Read it before class, or revise
    from it after.</p>
    <span class="go">read the notes \u2192</span>
    <div class="tags"><span class="tag">reading</span><span class="tag">12 traps</span><span class="tag">4 worked examples</span></div>
  </a>
  <a class="card" href="%(practice)s">
    <h2>Problem Set A1</h2>
    <p>All 24 problems from the class set \u2014 prime factorization, GCF and LCM,
    problem solving, and three challenges. No concept pages; the nudges point you back
    to the idea you need.</p>
    <span class="go">open the problem set \u2192</span>
    <div class="tags"><span class="tag">24 problems</span><span class="tag">answers verified</span></div>
  </a>
</div>

<div class="note">
  <h2>How the grading works</h2>
  <ul>
    <li>Write your working in the editor, put the result in the answer box, press <b>Check step</b>.</li>
    <li>Three tries per step. A wrong answer gets a nudge about what went wrong, never the answer.</li>
    <li><b>Hint for this step</b> opens a hint for the step you are on. Nothing appears unless you ask,
    and asking does not use up a try.</li>
    <li>After three misses you get one last attempt. Miss it and the step answer is handed over,
    with a push into the next step.</li>
    <li><b>Submit question</b> prints feedback on every step and the verified answer.</li>
  </ul>
</div>

<footer>Everything runs in the browser \u2014 no accounts, no server, nothing saved.
Closing a page clears its progress.</footer>
</main>
%(ink_html)s
<script>%(ink_js)s</script>
</body></html>
"""


NOTES_CSS = """
:root{--ink:#11242b;--ink-soft:#4a626c;--paper:#eef2f3;--card:#fff;--rule:#d3dcdf;
  --teal:#0d6b6e;--teal-dark:#094f52;--gold:#b1820f;--gold-soft:#fff5dd;
  --mono:"IBM Plex Mono",ui-monospace,Menlo,monospace;}
*{box-sizing:border-box}
html{scroll-behavior:smooth;scroll-padding-top:70px}
body{margin:0;color:var(--ink);background:var(--paper);
  font-family:"Atkinson Hyperlegible","Segoe UI",system-ui,sans-serif;font-size:17px;line-height:1.62}
.topbar{position:sticky;top:0;z-index:10;background:rgba(238,242,243,.95);backdrop-filter:blur(5px);
  border-bottom:1px solid var(--rule);padding:9px 20px;display:flex;gap:14px;align-items:center;flex-wrap:wrap}
.topbar b{font-weight:700}
.topbar a{color:var(--teal-dark);font-family:var(--mono);font-size:13.5px;margin-left:14px}
.topbar .sp{flex:1}
.wrap{max-width:1080px;margin:0 auto;padding:30px 20px 80px;display:grid;
  grid-template-columns:225px minmax(0,1fr);gap:34px;align-items:start}
@media(max-width:900px){.wrap{grid-template-columns:1fr;gap:18px}nav.toc{position:static!important}}
nav.toc{position:sticky;top:60px;background:var(--card);border:1px solid var(--rule);border-radius:4px;
  padding:14px 16px;font-size:14.5px}
nav.toc h4{margin:0 0 8px;font-size:12px;font-family:var(--mono);color:var(--ink-soft);letter-spacing:.05em}
nav.toc ol{list-style:none;margin:0;padding:0;counter-reset:s}
nav.toc li{margin:4px 0;counter-increment:s}
nav.toc a{display:block;text-decoration:none;color:var(--ink);padding:2px 0}
nav.toc a:before{content:counter(s) ".";font-family:var(--mono);font-size:12px;color:var(--ink-soft);margin-right:6px}
nav.toc a:hover{color:var(--teal-dark)}
nav.toc .plain a:before{content:none}
header.hero h1{font-family:Fraunces,Georgia,serif;font-size:clamp(31px,5vw,44px);line-height:1.12;margin:0 0 12px}
header.hero p{font-size:19px;color:var(--ink-soft);max-width:60ch}
.kicker{font-family:var(--mono);font-size:13px;color:var(--teal-dark);margin:0 0 14px;letter-spacing:.04em}
section.note{background:var(--card);border:1px solid var(--rule);border-radius:4px;
  padding:24px 26px 28px;margin:22px 0;box-shadow:0 1px 0 #dbe3e6}
section.note h2{font-family:Fraunces,Georgia,serif;font-size:26px;margin:0 0 4px;line-height:1.16}
section.note h3{font-size:18px;margin:24px 0 5px}
.tag{display:inline-block;font-family:var(--mono);font-size:11.5px;color:var(--teal-dark);
  border-bottom:2px solid var(--gold);padding-bottom:2px;margin:0 0 12px;letter-spacing:.05em}
p{margin:0 0 13px;max-width:68ch}
ul,ol{padding-left:21px;max-width:66ch}
li{margin:5px 0}
.stack{background:#f7fafa;border:1px solid #e3ebeb;border-radius:4px;padding:12px 14px;
  font-family:var(--mono);font-size:14px;line-height:1.8;white-space:pre-wrap;overflow-x:auto;margin:13px 0}
.rulebox{border-left:4px solid var(--gold);background:var(--gold-soft);padding:12px 15px;margin:14px 0;border-radius:0 4px 4px 0}
.rulebox p:last-child{margin:0}
table.cmp{border-collapse:collapse;width:100%;font-size:15px;margin:14px 0}
table.cmp th,table.cmp td{border:1px solid var(--rule);padding:8px 10px;text-align:left;vertical-align:top}
table.cmp th{background:#f1f6f6}
.m{font-family:var(--mono);font-size:.93em;background:#f1f6f6;border:1px solid #e0e9e9;border-radius:4px;padding:1px 5px}
.two{display:grid;grid-template-columns:1fr 1fr;gap:13px}
@media(max-width:760px){.two{grid-template-columns:1fr}}
.practice{margin-top:18px;padding-top:13px;border-top:1px dashed var(--rule);font-size:15px;color:var(--ink-soft)}
.practice a{display:inline-block;font-family:var(--mono);font-size:13px;text-decoration:none;
  background:#eef5f5;border:1px solid #cfe0e0;color:var(--teal-dark);border-radius:99px;
  padding:3px 10px;margin:3px 5px 0 0}
.practice a:hover{background:var(--teal);color:#fff;border-color:var(--teal)}
a:focus-visible{outline:3px solid var(--teal);outline-offset:2px}
footer.end{color:var(--ink-soft);font-size:15px;margin-top:26px}
footer.end a{color:var(--teal-dark)}
"""

NOTES_TPL = """<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Study notes \u2014 Prime Factorization, GCF and LCM</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700&family=Atkinson+Hyperlegible:wght@400;700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>%(css)s</style>
</head><body data-ink-mode="document">
<div class="topbar"><b>Study notes</b><span class="sp"></span>
  <a href="%(index)s">home</a><a href="%(lesson)s">lesson</a><a href="%(practice)s">problem set</a></div>
<div class="wrap">
<nav class="toc"><h4>ON THIS PAGE</h4><ol>%(toc)s</ol></nav>
<main>
<header class="hero">
  <p class="kicker">AwesomeMath Academy \u00b7 Week 1 \u00b7 Level 1</p>
  <h1>Everything in one place</h1>
  <p>The full write-up: how numbers are built out of primes, why the GCF and LCM rules are what they
  are, the traps that cost marks, four problems worked end to end, and a page you can revise from the
  night before class.</p>
</header>
%(body)s
<footer class="end">Every number on this page was checked by computer.
Practise it on the <a href="%(practice)s">problem set</a>, or work through the ideas one at a time in
the <a href="%(lesson)s">lesson</a>.</footer>
</main></div>
%(ink_html)s
<script>%(ink_js)s</script>
</body></html>
"""

PRACTICE_LINKS = {
    "primes":    [2, 10],
    "factorize": [1, 2, 19],
    "factors":   [18],
    "gcf":       [5, 11, 21],
    "lcm":       [6, 7, 16, 17],
    "identity":  [6, 20],
    "backwards": [8, 9],
    "parity":    [10, 12, 13, 14],
    "powers":    [18, 19],
    "words":     [15, 22, 23],
}

EXTRA_SECTIONS = [
    ("traps", "Tricky bits that cost marks", "Traps", None),
    ("worked", "Four problems worked end to end", "Worked examples", None),
    ("cheat", "One-page cheat sheet", "Cheat sheet", None),
    ("glossary", "The words, precisely", "Glossary", None),
    ("writeup", "How to write it up", "Habits", None),
]


def build_notes():
    C = concepts()
    body, toc = [], []
    for n, key in enumerate(IDEA_KEYS, start=1):
        title, html = C[key]
        links = "".join('<a href="%s#q%d">problem %d</a>' % (PRACTICE, q, q)
                        for q in PRACTICE_LINKS[key])
        html = html.replace('<p class="tag">Idea %d</p>' % n,
                            '<p class="tag">IDEA %d</p>' % n)
        body.append('<section class="note" id="i%d">%s<div class="practice">'
                    'Practise this: %s</div></section>' % (n, html, links))
        toc.append('<li><a href="#i%d">%s</a></li>' % (n, title))
    for sid, heading, short, _ in EXTRA_SECTIONS:
        content = {"traps": notes_data.TRAPS, "worked": notes_data.WORKED,
                   "cheat": notes_data.CHEAT, "glossary": notes_data.GLOSSARY,
                   "writeup": notes_data.WRITEUP}[sid]
        body.append('<section class="note" id="%s"><p class="tag">%s</p><h2>%s</h2>%s</section>'
                    % (sid, short.upper(), heading, content))
        toc.append('<li><a href="#%s">%s</a></li>' % (sid, heading))
    return NOTES_TPL % dict(css=NOTES_CSS + INK_CSS, toc="".join(toc), body="".join(body),
                            index=INDEX, lesson=LESSON, practice=PRACTICE,
                            ink_html=INK_HTML, ink_js=INK_JS)


def page(title, brand, subtitle, other, otherlabel, app, css=CSS):
    return (HEAD.format(title=title, css=css + INK_CSS)
            + SHELL.format(brand=brand, subtitle=subtitle, other=other,
                           otherlabel=otherlabel, ink_html=INK_HTML, **initial(app))
            + TAIL.format(check=JS_CHECK, app=JS_APP, ink_js=INK_JS,
                          data=json.dumps(app, ensure_ascii=False)))


def build():
    lesson_problems = []
    for v in G.values():
        lesson_problems += v
    all_problems = list(P) + lesson_problems
    hint_overrides.apply(all_problems)
    print("question rewrites:", hint_overrides.apply_asks(all_problems))

    # ---------------- lesson app ----------------
    C = concepts()
    groups = []
    for n, key in enumerate(IDEA_KEYS, start=1):
        title, html = C[key]
        items = []
        for p in G[key]:
            p["concept"] = html
            p["short"] = p["label"].replace("Try it \u00b7 ", "")
            p["tags"] = [{"t": f"Idea {n}", "k": "set"},
                         {"t": title, "k": ""},
                         {"t": "guided", "k": "core"}]
            items.append(p["id"])
        groups.append({"title": f"{n}. {title}", "items": items})
    lesson_app = {"groups": groups, "problems": lesson_problems, "startTab": "concept"}

    # ---------------- practice app ----------------
    sections = [("Prime factorization", 1, 4), ("GCF and LCM", 5, 9),
                ("Problem solving", 10, 21), ("Challenges", 22, 24)]
    pby = {p["id"]: p for p in P}
    pgroups = []
    for title, lo, hi in sections:
        items = []
        for k in range(lo, hi + 1):
            p = pby["q%d" % k]
            p["short"] = p["label"].replace("Problem ", "").replace("Challenge ", "")
            p["tags"] = [{"t": "Set A1", "k": "set"}, {"t": title, "k": ""}]
            if title == "Challenges":
                p["tags"].append({"t": "Hard", "k": "hard"})
            items.append(p["id"])
        pgroups.append({"title": title, "items": items})
    practice_app = {"groups": pgroups, "problems": list(P), "reference": REFERENCE}

    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, LESSON), "w", encoding="utf-8") as f:
        f.write(page("Prime Factorization, GCF and LCM \u2014 Lesson",
                     "Math Lab", "Week 1 \u00b7 lesson + guided practice",
                     PRACTICE, "problem set \u2192", lesson_app))
    with open(os.path.join(OUT, PRACTICE), "w", encoding="utf-8") as f:
        f.write(page("Problem Set A1 \u2014 Practice", "Math Lab",
                     "Problem Set A1 \u00b7 24 problems",
                     LESSON, "\u2190 lesson", practice_app))

    with open(os.path.join(OUT, NOTES), "w", encoding="utf-8") as f:
        f.write(build_notes())

    with open(os.path.join(OUT, INDEX), "w", encoding="utf-8") as f:
        f.write(INDEX_TPL % dict(css=INDEX_CSS + INK_CSS, lesson=LESSON, practice=PRACTICE,
                                 notes=NOTES, ink_html=INK_HTML, ink_js=INK_JS))

    for fn in (INDEX, NOTES, LESSON, PRACTICE):
        print(fn, os.path.getsize(os.path.join(OUT, fn)), "bytes")


if __name__ == "__main__":
    build()
