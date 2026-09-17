import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from assets import CSS, JS, HEAD, TAIL
from lesson_data import G
from practice_data import P
import hint_overrides

OUT = "/mnt/user-data/outputs"
os.makedirs(OUT, exist_ok=True)
LESSON_FILE = "prime-factorization-lesson.html"
PRACTICE_FILE = "prime-factorization-practice.html"

# ------------------------------------------------------------------ hero
def tree_svg():
    nodes = [  # x, y, text, prime?
        (360, 34, "440", 0),
        (215, 112, "44", 0), (515, 112, "10", 0),
        (140, 190, "4", 0), (290, 190, "11", 1),
        (455, 190, "2", 1), (580, 190, "5", 1),
        (95, 268, "2", 1), (195, 268, "2", 1),
    ]
    edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6), (3, 7), (3, 8)]
    s = ['<svg viewBox="0 0 700 320" role="img" aria-label="Factor tree of 440 ending in the primes 2, 2, 2, 5 and 11">']
    s.append('<style>.nd{font-family:"IBM Plex Mono",monospace;font-size:19px;text-anchor:middle}'
             '.lk{stroke:#9fb6bb;stroke-width:1.6}</style>')
    for i, (a, b) in enumerate(edges):
        x1, y1 = nodes[a][0], nodes[a][1] + 20
        x2, y2 = nodes[b][0], nodes[b][1] - 20
        s.append(f'<line class="lk grow" style="animation-delay:{0.06*i:.2f}s" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"/>')
    for i, (x, y, t, pr) in enumerate(nodes):
        fill = "#fff5dd" if pr else "#ffffff"
        stroke = "#b1820f" if pr else "#0d6b6e"
        s.append(f'<g class="grow" style="animation-delay:{0.05*i:.2f}s">'
                 f'<circle cx="{x}" cy="{y}" r="24" fill="{fill}" stroke="{stroke}" stroke-width="2"/>'
                 f'<text class="nd" x="{x}" y="{y+7}" fill="#10242b">{t}</text></g>')
    s.append('<text x="640" y="300" text-anchor="end" font-family="IBM Plex Mono,monospace" '
             'font-size="20" fill="#10242b">440 = 2\u00b3 \u00b7 5 \u00b7 11</text>')
    s.append('</svg>')
    return "".join(s)

def bar(link_text, link_href):
    return (f'<div class="bar"><span id="ptxt">0 finished</span>'
            f'<span class="track"><span class="fill" id="fill"></span></span>'
            f'<a href="{link_href}">{link_text}</a></div>')

def hosts(ids):
    return "".join(f'<div id="host-{i}"></div>' for i in ids)

def mount_js(mapping):
    """mapping: list of (hostId, python list of problems)"""
    out = []
    for host, plist in mapping:
        out.append(f"mountProblems({json.dumps(plist, ensure_ascii=False)}, 'host-{host}');")
    return "\n".join(out)

# ------------------------------------------------------------------ lesson body
LESSON_BODY = """
<header class="top">
  <p class="kicker">AwesomeMath Academy &nbsp;\u00b7&nbsp; Week 1, Level 1 &nbsp;\u00b7&nbsp; <b>Lesson</b></p>
  <h1>Prime factorization,<br>GCF and LCM</h1>
  <p class="lede">Every whole number is built out of primes, the way a word is built out of letters.
  Once you can see those building blocks, questions about common factors, common multiples,
  squares and cubes all become the same kind of question.</p>
  <figure class="hero">%(hero)s
    <figcaption>The gold circles are primes \u2014 numbers that cannot be split any further.
    Three 2s, one 5 and one 11 are the building blocks of 440.</figcaption>
  </figure>
  <div class="jump">
    <a href="#s1">Start the lesson</a>
    <a class="alt" href="%(practice)s">Go to the 24-problem practice set</a>
  </div>
</header>

<nav class="toc" aria-label="Contents">
  <ol>
    <li><a href="#s1">Primes and composites</a></li>
    <li><a href="#s2">Prime factorization</a></li>
    <li><a href="#s3">Reading factors off the factorization</a></li>
    <li><a href="#s4">Greatest common factor</a></li>
    <li><a href="#s5">Least common multiple</a></li>
    <li><a href="#s6">The GCF \u00d7 LCM shortcut</a></li>
    <li><a href="#s7">Working backwards</a></li>
    <li><a href="#s8">Primes hiding in equations</a></li>
    <li><a href="#s9">Squares, cubes and exponents</a></li>
    <li><a href="#s10">Word problems: which tool?</a></li>
  </ol>
</nav>

<section class="lesson">
  <p class="tag">How this page works</p>
  <p>Each idea comes with a <b>Try it</b> problem broken into steps. For every step: write your
  thinking in the work box, put your result in the answer box, and check it.</p>
  <ul>
    <li>Wrong answers get a nudge, not the answer. You get <b>three tries</b>.</li>
    <li>After the third try you get a real <b>hint</b>, plus one more attempt.</li>
    <li>If that attempt misses, the step's answer is handed to you \u2014 copy it down and carry on
    to the next step yourself.</li>
    <li><b>Submit all steps</b> at the bottom gives you feedback on every step and the full verified answer.</li>
  </ul>
  <div class="rulebox"><p><b>Why the work boxes matter.</b> In class the rule is that an answer with no
  work shown scores zero \u2014 not to be strict, but because written steps are the only way anyone can see
  where a method went wrong and tell you what to fix. Hard problems are also meant to be slept on:
  one you cannot finish today is normal, and worth returning to tomorrow.</p></div>
  <p>Answer format: write products with <span class="m">*</span> and powers with <span class="m">^</span>,
  so 2\u00b3 \u00b7 5 \u00b7 11 is typed <span class="m">2^3*5*11</span>. Typing <span class="m">2*2*2*5*11</span> is fine too.</p>
</section>

<section class="lesson" id="s1">
  <p class="tag">Idea 1</p>
  <h2>Primes and composites</h2>
  <p>A <b>prime</b> is a whole number with exactly two positive divisors: 1 and itself.
  A <b>composite</b> has more than two. The number 1 is neither \u2014 it has only one divisor.</p>
  <p>Think of primes as bricks. Factoring a number shows which bricks it was built from:
  66 = 2 \u00b7 33 = 2 \u00b7 3 \u00b7 11, and none of 2, 3, 11 can be broken down further. That is also why
  1 is kept out. If 1 counted as prime you could write 66 = 1 \u00b7 1 \u00b7 1 \u00b7 2 \u00b7 3 \u00b7 11 and add as
  many 1s as you liked \u2014 the list of bricks would stop being one fixed list, and every rule in
  this lesson depends on it being fixed.</p>
  <div class="stack">primes:     2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, \u2026
composites: 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, \u2026</div>
  <p>2 is the only even prime. Every other even number has 2 as a factor, so it already has three
  factors at least. That single fact solves a surprising number of competition problems \u2014 you will
  use it in Idea 8.</p>
  <h3>Fast divisibility checks</h3>
  <table class="cmp">
    <tr><th>Divisor</th><th>Test</th><th>Example</th></tr>
    <tr><td>2</td><td>last digit is even</td><td>440 \u2713</td></tr>
    <tr><td>3</td><td>digits add to a multiple of 3</td><td>594 \u2192 5+9+4 = 18 \u2713</td></tr>
    <tr><td>4</td><td>last two digits form a multiple of 4</td><td>616 \u2192 16 \u2713</td></tr>
    <tr><td>5</td><td>ends in 0 or 5</td><td>2020 \u2713</td></tr>
    <tr><td>6</td><td>passes both the 2 test and the 3 test</td><td>594 \u2713</td></tr>
    <tr><td>9</td><td>digits add to a multiple of 9</td><td>225 \u2192 9 \u2713</td></tr>
    <tr><td>11</td><td>alternating digit sum is a multiple of 11</td><td>616 \u2192 6 \u2212 1 + 6 = 11 \u2713</td></tr>
  </table>
  <div class="rulebox"><p><b>How far do you have to test?</b> Only up to the square root. To check
  whether 101 is prime you test 2, 3, 5 and 7 \u2014 and stop, because 11 \u00d7 11 = 121 is already past 101.
  If a number had a factor bigger than its square root, the matching partner factor would be smaller,
  and you would have found it already.</p></div>
  <div id="host-primes"></div>
</section>

<section class="lesson" id="s2">
  <p class="tag">Idea 2</p>
  <h2>Prime factorization</h2>
  <p>The prime factorization of a number is that number written as a product of primes.
  You find it with a <b>factor tree</b>: split the number into any two factors, then keep
  splitting anything that is not yet prime.</p>
  <div class="two">
    <div class="stack">440
 = 44 \u00b7 10
 = (4 \u00b7 11) \u00b7 (2 \u00b7 5)
 = 2 \u00b7 2 \u00b7 11 \u00b7 2 \u00b7 5
 = 2\u00b3 \u00b7 5 \u00b7 11</div>
    <div class="stack">440
 = 8 \u00b7 55
 = (2 \u00b7 2 \u00b7 2) \u00b7 (5 \u00b7 11)
 = 2 \u00b7 2 \u00b7 2 \u00b7 5 \u00b7 11
 = 2\u00b3 \u00b7 5 \u00b7 11</div>
  </div>
  <p>Two different starts, one answer. That is not luck.</p>
  <div class="rulebox"><p><b>Unique factorization.</b> Every whole number above 1 has exactly one
  prime factorization, apart from the order of the factors. So you may always begin with the easiest
  split you can see \u2014 the answer cannot depend on your route.</p></div>
  <p><b>Exponent notation</b> is just shorthand for repeats:
  <span class="m">2 \u00b7 2 \u00b7 2 = 2^3</span>. The small number counts how many copies of the prime
  there are. Keeping the exponents visible is what makes the next four ideas easy.</p>
  <div id="host-factorize"></div>
</section>

<section class="lesson" id="s3">
  <p class="tag">Idea 3</p>
  <h2>Reading factors off the factorization</h2>
  <p>Here is the key move behind everything that follows. Since 440 = 2 \u00b7 2 \u00b7 2 \u00b7 5 \u00b7 11,
  <b>every factor of 440 is a group chosen from that pile</b> \u2014 up to three 2s, maybe the 5,
  maybe the 11. Choosing nothing gives the factor 1.</p>
  <div class="stack">pick nothing        \u2192 1
pick 2              \u2192 2
pick 2 \u00b7 2          \u2192 4
pick 2 \u00b7 5          \u2192 10
pick 2 \u00b7 2 \u00b7 2 \u00b7 11  \u2192 88
pick everything     \u2192 440</div>
  <p>Choosing nothing at all is worth a mention: the empty group has value 1, which is exactly why
  1 is a factor of every number.</p>
  <p>So the exponents tell you how many factors a number has. For 72 = 2\u00b3 \u00b7 3\u00b2 you may take
  0, 1, 2 or 3 twos (four choices) and 0, 1 or 2 threes (three choices), giving
  4 \u00d7 3 = 12 factors.</p>
  <div class="rulebox"><p><b>Factor count.</b> Add 1 to every exponent, then multiply.
  For 2\u00b3 \u00b7 3\u00b2 that is (3+1)(2+1) = 12.</p></div>
  <div id="host-factors"></div>
</section>

<section class="lesson" id="s4">
  <p class="tag">Idea 4</p>
  <h2>Greatest common factor</h2>
  <p>Read the name backwards: <b>factor</b> means divisor, <b>common</b> means shared,
  <b>greatest</b> means largest \u2014 the largest divisor the two numbers share.
  A <b>common factor</b> is a group you could pick from either pile.
  Line up the two factorizations and the answer stares back at you.</p>
  <div class="stack">440  = 2 \u00b7 2 \u00b7 2 \u00b7 5 \u00b7 11
2020 = 2 \u00b7 2 \u00b7 5 \u00b7 101
       \u2514\u2500\u2500\u2500\u2500\u2500\u252c\u2500\u2500\u2500\u2500\u2518
   shared: 2 \u00b7 2 \u00b7 5  =  20</div>
  <p>440 can spare three 2s but 2020 only has two, so a shared group may use two 2s at most.
  Both have one 5. The 11 and the 101 are unshared, so they cannot appear in a common factor at all.</p>
  <div class="rulebox"><p><b>GCF rule.</b> Keep only the primes that appear in <em>both</em> numbers,
  each at its <b>smaller</b> power, and multiply. GCF(440, 2020) = 2\u00b2 \u00b7 5 = 20.
  If a prime has the same exponent in both numbers, either copy gives the same thing.</p></div>
  <div id="host-gcf"></div>
</section>

<section class="lesson" id="s5">
  <p class="tag">Idea 5</p>
  <h2>Least common multiple</h2>
  <p>Flip the question. A <b>multiple</b> of 440 must contain everything 440 contains: three 2s,
  a 5, an 11. A multiple of 2020 must contain two 2s, a 5, a 101. A number that is a multiple of
  both must satisfy both demands at once \u2014 and the smallest such number does no more than that.</p>
  <div class="stack">440  needs  2 \u00b7 2 \u00b7 2 \u00b7 5 \u00b7 11
2020 needs  2 \u00b7 2     \u00b7 5      \u00b7 101
LCM  =      2 \u00b7 2 \u00b7 2 \u00b7 5 \u00b7 11 \u00b7 101  =  44,440</div>
  <p>Another way to see it: start with everything 440 needs. Two of its 2s and its 5 already cover
  what 2020 demands, so the only thing still missing is the 101. Shared factors do not get duplicated
  just because both numbers happen to contain them.</p>
  <div class="rulebox"><p><b>LCM rule.</b> Take <em>every</em> prime that appears in either number,
  each at its <b>bigger</b> power, and multiply. Dropping a prime because it appears in only one
  number is the most common mistake here \u2014 the LCM still needs it.</p></div>
  <table class="cmp">
    <tr><th></th><th>GCF</th><th>LCM</th></tr>
    <tr><td>which primes</td><td>only the shared ones</td><td>all of them</td></tr>
    <tr><td>which power</td><td>the smaller</td><td>the bigger</td></tr>
    <tr><td>size</td><td>no bigger than either number</td><td>no smaller than either number</td></tr>
  </table>
  <p>One convention makes both rules read the same way: if a prime is missing from a number, treat its
  exponent there as 0. Then 11 has exponent 0 in 2020, and \u201csmaller of 1 and 0\u201d correctly keeps 11 out
  of the GCF while \u201cbigger of 1 and 0\u201d correctly puts it into the LCM. Every prime, every time \u2014
  minimum for the GCF, maximum for the LCM.</p>
  <div id="host-lcm"></div>
</section>

<section class="lesson" id="s6">
  <p class="tag">Idea 6</p>
  <h2>The GCF \u00d7 LCM shortcut</h2>
  <p>Look at what the two rules do to one prime. If one number has 2\u00b3 and the other has 2\u00b2, then
  the GCF takes 2\u00b2 and the LCM takes 2\u00b3 \u2014 between them they use exactly the same 2s as the two
  original numbers. That happens for every prime, so:</p>
  <div class="stack">120 = 2\u00b3 \u00b7 3 \u00b7 5        GCF(120, 300) = 2\u00b2 \u00b7 3 \u00b7 5  =  60
300 = 2\u00b2 \u00b7 3 \u00b7 5\u00b2       LCM(120, 300) = 2\u00b3 \u00b7 3 \u00b7 5\u00b2 =  600

120 \u00b7 300 = 36,000        60 \u00b7 600 = 36,000</div>
  <div class="rulebox"><p><b>Identity.</b> For any positive integers a and b:
  <span class="m">a \u00b7 b = GCF(a, b) \u00b7 LCM(a, b)</span>. Know any three of the four and the fourth
  is one division away. It is also the fastest way to check work you have already done.</p></div>
  <div id="host-identity"></div>
</section>

<section class="lesson" id="s7">
  <p class="tag">Idea 7</p>
  <h2>Working backwards</h2>
  <p>Harder questions give you the GCF or LCM and ask what the mystery number could be.
  Translate the condition into rules about exponents, one prime at a time.</p>
  <h3>Given a GCF</h3>
  <div class="stack">GCF(240, n) = 12        240 = 2\u2074 \u00b7 3 \u00b7 5,  12 = 2\u00b2 \u00b7 3
n must have 2\u00b2 exactly  (2\u00b9 \u2192 GCF loses a 2;  2\u00b3 \u2192 GCF gains one)
n must have 3\u00b9 or more  (needed for the 3 in 12)
n must have no 5        (240 has a 5; sharing it would enlarge the GCF)
other primes: free      (240 has no 7, 11, 13 \u2026 so they change nothing)</div>
  <p>Smallest n = 2\u00b2 \u00b7 3 = 12. Largest? There is none: n = 12 \u00b7 7\u1d4f keeps the GCF at 12 forever.</p>
  <h3>Given an LCM</h3>
  <div class="stack">LCM(225, n) = 1800      225 = 3\u00b2 \u00b7 5\u00b2,  1800 = 2\u00b3 \u00b7 3\u00b2 \u00b7 5\u00b2
n must have 2\u00b3 exactly  (225 has no 2s, so n supplies them all)
n may have 3\u2070\u207b\u00b2, 5\u2070\u207b\u00b2   (225 already covers these)
n may have nothing else (a new prime would show up in the LCM)</div>
  <p>Smallest n = 8, largest n = 1800.</p>
  <div class="rulebox"><p><b>The asymmetry worth remembering.</b> A GCF condition sets a floor
  but no ceiling, so unwanted primes can be piled on forever and there is no largest n.
  An LCM condition caps every exponent, so n is boxed in from above.</p></div>
  <div id="host-backwards"></div>
</section>

<section class="lesson" id="s8">
  <p class="tag">Idea 8</p>
  <h2>Primes hiding in equations</h2>
  <p>Problems like &ldquo;find all primes a, b with 4a + 5b = 54&rdquo; look like algebra with too few
  equations. The trick is that primes are extremely restricted, so <b>divisibility pins one of
  them down</b> and the rest is arithmetic.</p>
  <div class="stack">4a + 5b = 54
5b = 54 \u2212 4a = 2(27 \u2212 2a)   \u2190 factor the right side
so 5b is even; 5 is odd, so b is even
the only even prime is 2    \u2192  b = 2
4a + 10 = 54  \u2192  4a = 44  \u2192  a = 11  (prime \u2713)</div>
  <p>The same move works with any shared divisor, not just 2. In
  <span class="m">4a + 5b + 15c = 75</span>, the terms 5b, 15c and 75 are all multiples of 5,
  so 4a must be too \u2014 and since 4 is not divisible by 5, a is. The only prime multiple of 5 is 5,
  so a = 5 before you do any work at all.</p>
  <p>A third move is <b>bounding</b>. In 4a + 5b = 54 both terms are positive, so 5b &lt; 54 and
  b \u2264 10 \u2014 that leaves only 2, 3, 5 and 7 to test. Narrow the field with divisibility or bounds
  first, then check the few survivors by hand. Guess-and-check is a finishing move, not an opening one.</p>
  <p>And sometimes the honest answer is that nothing works. If the argument forces b = 3, and that
  forces a = 93 = 3 \u00b7 31, then no prime pair exists. A contradiction you were driven into is a
  finished proof, not a mistake.</p>
  <div class="rulebox"><p><b>Two moves to try first.</b> (1) <b>Parity:</b> if the equation forces a
  prime to be even, that prime is 2. (2) <b>Shared divisor:</b> if every term but one is divisible
  by d, the last one must be too. And always check your answer really is prime \u2014 sometimes the
  conclusion is &ldquo;no such primes exist&rdquo;.</p></div>
  <div id="host-parity"></div>
</section>

<section class="lesson" id="s9">
  <p class="tag">Idea 9</p>
  <h2>Squares, cubes and exponents</h2>
  <p>Raising a number to a power multiplies every exponent in its factorization:</p>
  <div class="stack">1800 = 2\u00b3 \u00b7 3\u00b2 \u00b7 5\u00b2
1800\u2077 = (2\u00b3 \u00b7 3\u00b2 \u00b7 5\u00b2)\u2077 = 2\u00b2\u00b9 \u00b7 3\u00b9\u2074 \u00b7 5\u00b9\u2074      \u2190 seven copies of each</div>
  <p>Read that backwards and you get a test:</p>
  <div class="rulebox"><p><b>Perfect powers.</b> A number is a perfect square exactly when every
  exponent in its prime factorization is even, and a perfect cube exactly when every exponent is a
  multiple of 3. In general, a = b\u207f means every exponent of a is a multiple of n.</p></div>
  <p>The test runs both ways. If every exponent is already a multiple of 3, divide each one by 3 to
  read off the cube root: 2\u2076 \u00b7 3\u00b3 \u00b7 5\u00b3 is the cube of 2\u00b2 \u00b7 3 \u00b7 5 = 60.</p>
  <p>That turns &ldquo;smallest cube divisible by 720&rdquo; into bookkeeping. 720 = 2\u2074 \u00b7 3\u00b2 \u00b7 5, so
  the exponents must be at least 4, 2, 1 \u2014 and each must be a multiple of 3. Round each one up:</p>
  <div class="stack">2: 4 \u2192 6      3: 2 \u2192 3      5: 1 \u2192 3
2\u2076 \u00b7 3\u00b3 \u00b7 5\u00b3 = (2\u00b2 \u00b7 3 \u00b7 5)\u00b3 = 60\u00b3 = 216,000</div>
  <p>The same rounding, with multiples of 2 instead of 3, answers &ldquo;which squares are multiples of
  24?&rdquo; \u2014 problem 19 in the practice set.</p>
  <div id="host-powers"></div>
</section>

<section class="lesson" id="s10">
  <p class="tag">Idea 10</p>
  <h2>Word problems: which tool?</h2>
  <p>Almost every word problem in this set is one of three shapes. Decide the shape first,
  then the arithmetic is short.</p>
  <table class="cmp">
    <tr><th>Shape</th><th>Signals</th><th>Tool</th></tr>
    <tr><td>Things repeat on cycles and must line up again</td>
        <td>every 4 weeks, blinks every 6 seconds, round trip of 12 days</td><td>LCM</td></tr>
    <tr><td>A fixed pile is divided into equal groups with nothing left over</td>
        <td>identical kits, largest possible groups, share equally</td><td>GCF</td></tr>
    <tr><td>The same remainder appears every time</td>
        <td>remainder 1 when divided by 2, 3, 4, 5</td><td>LCM, then add or subtract</td></tr>
  </table>
  <p>Two traps to watch. Multiplying the numbers together gives <em>a</em> common multiple but
  usually not the <em>least</em> one: 9 \u00d7 12 = 108 while LCM(9, 12) = 36. And when a problem asks
  &ldquo;how many times per minute&rdquo;, count the events inside the minute rather than the starting
  moment when everything was switched on.</p>
  <div id="host-words"></div>
</section>

<section class="lesson">
  <p class="tag">Next</p>
  <h2>Now do the problem set</h2>
  <p>You have seen all ten ideas. The practice page has all 24 problems from
  Problem Set A1 \u2014 prime factorization, GCF and LCM, problem solving and three challenges \u2014
  in the same step-by-step format, with every answer verified.</p>
  <div class="jump"><a href="%(practice)s">Open the 24-problem practice set</a>
  <a class="alt" href="#s1">Back to the top of the lesson</a></div>
</section>
"""

# ------------------------------------------------------------------ practice body
PRACTICE_BODY = """
<header class="top">
  <p class="kicker">AwesomeMath Academy &nbsp;\u00b7&nbsp; Problem Set A1 &nbsp;\u00b7&nbsp; <b>Practice</b></p>
  <h1>Problem Set A1</h1>
  <p class="lede">All 24 problems, one step at a time. No concept pages here \u2014 if a problem stalls,
  the nudges will point you back to the idea you need.</p>
  <div class="lesson" style="margin-top:22px">
    <p class="tag">The deal</p>
    <ul>
      <li>Write your thinking in the work box, put the result in the answer box, check the step.</li>
      <li>Three tries, each with a nudge. Then a hint, and one more try.</li>
      <li>Miss that one and the step's answer is handed over \u2014 write it down and take the next step yourself.</li>
      <li><b>Submit all steps</b> gives you step-by-step feedback plus the full verified answer.</li>
    </ul>
    <p>Type products with <span class="m">*</span> and powers with <span class="m">^</span>:
    2\u00b3 \u00b7 5 \u00b7 11 is <span class="m">2^3*5*11</span>. Lists can be typed like
    <span class="m">2, 5</span>.</p>
  </div>
  <div class="jump"><a href="#q1">Start with problem 1</a>
  <a class="alt" href="%(lesson)s">Back to the lesson</a></div>
</header>

<section class="lesson" style="padding-bottom:18px">
  <p class="tag">Sections</p>
  <h2 style="font-size:24px">Where the problems sit</h2>
  <ul>
    <li><b>Prime factorization</b> \u2014 problems 1 to 4</li>
    <li><b>GCF and LCM</b> \u2014 problems 5 to 9</li>
    <li><b>Problem solving</b> \u2014 problems 10 to 21</li>
    <li><b>Challenges</b> \u2014 problems 22 to 24</li>
  </ul>
</section>
<div id="host-all"></div>

<section class="lesson">
  <p class="tag">Finished</p>
  <h2>What to do after the last problem</h2>
  <p>Go back to any problem where a step was handed to you and redo it on paper from scratch,
  without reading the page. That second pass is where the method sticks.</p>
  <div class="jump"><a href="%(lesson)s">Reread the lesson</a>
  <a class="alt" href="#q1">Back to problem 1</a></div>
</section>
"""

def build():
    all_problems = list(P)
    for v in G.values():
        all_problems += v
    print("overrides applied:", hint_overrides.apply(all_problems))

    # lesson page
    body = LESSON_BODY % dict(hero=tree_svg(), practice=PRACTICE_FILE)
    data = mount_js([(k, v) for k, v in G.items()])
    html = (HEAD.format(title="Prime Factorization, GCF and LCM \u2014 Lesson", css=CSS)
            + bar("Practice set \u2192", PRACTICE_FILE) + "<main>" + body
            + '<footer class="end">AwesomeMath Academy \u00b7 Week 1 \u00b7 Level 1 \u2014 '
              'lesson page. Every answer on this page was checked by computer.</footer></main>'
            + TAIL.format(js=JS, data=data))
    with open(os.path.join(OUT, LESSON_FILE), "w", encoding="utf-8") as f:
        f.write(html)

    # practice page
    body = PRACTICE_BODY % dict(lesson=LESSON_FILE)
    data = mount_js([("all", P)])
    html = (HEAD.format(title="Problem Set A1 \u2014 Practice", css=CSS)
            + bar("\u2190 Lesson", LESSON_FILE) + "<main>" + body
            + '<footer class="end">Problem Set A1 \u00b7 24 problems \u00b7 all answers verified by computer.'
              '</footer></main>'
            + TAIL.format(js=JS, data=data))
    with open(os.path.join(OUT, PRACTICE_FILE), "w", encoding="utf-8") as f:
        f.write(html)

    for fn in (LESSON_FILE, PRACTICE_FILE):
        p = os.path.join(OUT, fn)
        print(fn, os.path.getsize(p), "bytes")

if __name__ == "__main__":
    build()
