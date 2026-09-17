# -*- coding: utf-8 -*-
"""Content that exists only on the notes page: the tricky-concept section,
fully worked examples, a cheat sheet and a glossary."""

TRAPS = r"""
<p>Every one of these has cost someone the mark on a problem in this set. They are worth more
attention than the rules themselves, because the rules are easy and these are where the rules get
misapplied.</p>

<h3>1. Multiplying two numbers gives <em>a</em> common multiple, not the least one</h3>
<p>9 &times; 12 = 108 is a common multiple of 9 and 12. It is not the LCM, which is 36. Multiplying
counts the shared factor of 3 twice. Multiplying only gives the LCM when the two numbers share
nothing, like 9 and 10.</p>

<h3>2. Dropping a prime from the LCM because only one number has it</h3>
<p>For 616 = 2&sup3; &middot; 7 &middot; 11 and 980 = 2&sup2; &middot; 5 &middot; 7&sup2;, the LCM needs
the 5 <em>and</em> the 11 even though neither is shared. A multiple of 616 must contain 11; a multiple
of 980 must contain 5; a multiple of both contains both. The GCF is the one that throws out unshared
primes, not the LCM.</p>
<div class="rulebox"><p>The exponent-zero trick kills this mistake. Write the missing prime with
exponent 0: 11&sup0; in 980. Then "smaller exponent" gives 11&sup0; = 1 for the GCF and "bigger
exponent" gives 11&sup1; for the LCM, and both rules read the same way for every prime.</p></div>

<h3>3. Counting the starting moment as an event</h3>
<p>Two signs blink together every 12 seconds. In one minute they blink together at 12, 24, 36, 48 and
60 seconds &mdash; five times. The moment they were switched on is the start of the minute, not a blink
inside it. Answering 6 is the standard slip.</p>

<h3>4. Assuming a big leftover factor is prime &mdash; or that it isn't</h3>
<p>2020 = 2&sup2; &middot; 5 &middot; 101 only finishes if you check 101. Test primes up to the square
root: 2, 3, 5, 7, and stop, because 11 &times; 11 = 121 &gt; 101. The same test settles 2017 (primes to
43, since 44&sup2; = 1936 and 45&sup2; = 2025) and catches 91 = 7 &middot; 13, which looks prime and
isn't.</p>

<h3>5. Treating a contradiction as your own mistake</h3>
<p>In 9a + 14b = 879, divisibility by 3 forces b = 3 with no alternatives, and then a = 93 = 3
&middot; 31, which is not prime. The correct answer is that no such primes exist. You were driven
into the contradiction by a valid argument, so the contradiction <em>is</em> the result. Going back and
"fixing" it produces a wrong answer.</p>

<h3>6. Stopping after one parity case fails</h3>
<p>For 5a + 9b = 10,003, case a = 2 gives 9b = 9993, whose digit sum is 30, so that case dies. The
problem is not over &mdash; case b = 2 gives a = 1997, which is prime. A dead case rules out that case
and nothing else.</p>

<h3>7. Assuming the mystery number is bounded both ways</h3>
<p>GCF(240, n) = 12 has a smallest n (12) but <em>no</em> largest: n = 12 &middot; 7<sup>k</sup> keeps
the GCF at 12 forever, because 240 has no 7 to share. LCM(225, n) = 1800 has both a smallest (8) and a
largest (1800), because nothing dividing 1800 can exceed it. A GCF condition sets a floor; an LCM
condition sets a ceiling.</p>

<h3>8. Halving exponents the wrong way on squares and cubes</h3>
<p>For k&sup2; to be a multiple of 24 = 2&sup3; &middot; 3, you cannot just say k is a multiple of 24.
Every exponent in k&sup2; is even, so to cover 2&sup3; it must reach 2&#8308;, meaning k needs 2&sup2;;
and to cover 3&sup1; it must reach 3&sup2;, meaning k needs 3&sup1;. So k is a multiple of
2&sup2; &middot; 3 = 12, not 24. Then k &lt; 1000 gives 83 values.</p>

<h3>9. Reading "shared" as one thing when it can mean two</h3>
<p>"What prime factors do 440 and 2020 share?" has two defensible answers: the distinct primes 2 and
5, or the shared copies 2 &middot; 2 &middot; 5 = 20. Both were accepted in class. When a question can
be read two ways, answer the reading you chose <em>and say which one you chose</em>.</p>

<h3>10. Forgetting that change runs backwards</h3>
<p>In the pigs-and-goats problem, a payment is 300p + 210g where p and g may be <em>negative</em>,
because change comes back the other way. That is what makes $30 reachable: five pigs handed over,
seven goats received, 1500 &minus; 1470 = 30. Restricting to positive counts gives the wrong,
larger answer.</p>

<h3>11. Ordered versus unordered</h3>
<p>Problem 24 asks for ordered triples (x, y, z), so (8, 9, 300) and (9, 8, 300) would count
separately if both worked. Counting sets instead of ordered triples is the fastest way to get 15
wrong. Read the words "ordered" and "distinct" as constraints, not decoration.</p>

<h3>12. Letting 1 into the primes</h3>
<p>If 1 were prime, 66 = 1 &middot; 1 &middot; 1 &middot; 2 &middot; 3 &middot; 11 would be a valid
factorization and so would infinitely many others. Unique factorization &mdash; the thing every rule
on this page rests on &mdash; would be false. 1 has exactly one divisor, primes have exactly two.</p>
"""

WORKED = r"""
<p>Four problems worked end to end, with the reasoning written out the way a solution should be
handed in. Notice how little arithmetic there is in each one: the work is in narrowing the
possibilities first.</p>

<h3>A. Find all primes a, b with 5a + 9b = 10,003</h3>
<div class="stack">Is there a shared divisor? 10,003 is divisible by neither 5 nor 3, so no shortcut there.

Parity: 5 and 9 are both odd, and 10,003 is odd.
An odd total needs one even addend and one odd addend,
so exactly one of a and b is even &mdash; and the only even prime is 2.

Case a = 2:  10 + 9b = 10,003  &rarr;  9b = 9993
             digit sum of 9993 is 30, not a multiple of 9  &rarr;  no solution

Case b = 2:  5a + 18 = 10,003  &rarr;  5a = 9985  &rarr;  a = 1997
             1997 is prime (no prime up to 43 divides it)

Answer: a = 1997, b = 2.    Check: 9985 + 18 = 10,003.</div>
<p>The whole problem is decided before any real calculation: parity forces one prime to be 2, and
there are only two cases to try.</p>

<h3>B. The smallest perfect cube divisible by 720</h3>
<div class="stack">720 = 2&#8308; &middot; 3&sup2; &middot; 5

A cube needs every exponent divisible by 3.
Divisibility by 720 needs exponents of at least 4, 2, 1.
Round each one up to the next multiple of 3:

   2:  4 &rarr; 6        3:  2 &rarr; 3        5:  1 &rarr; 3

2&#8310; &middot; 3&sup3; &middot; 5&sup3; = (2&sup2; &middot; 3 &middot; 5)&sup3; = 60&sup3; = 216,000

Check: 216,000 &divide; 720 = 300.</div>
<p>The last line of the factorization is worth studying: dividing every exponent by 3 reads the cube
root straight off, which is why the answer is 60&sup3; and not just "216,000".</p>

<h3>C. The least number leaving remainder 9 on division by 10, 8 by 9, &hellip; , 1 by 2</h3>
<div class="stack">Each remainder is exactly one less than its divisor.
So the number is always one short of a multiple:  N + 1 is divisible by 2, 3, 4, &hellip; , 10.

LCM(2, &hellip; , 10) = 2&sup3; &middot; 3&sup2; &middot; 5 &middot; 7 = 2520
   (2&sup3; from 8, 3&sup2; from 9, then 5 and 7)

N = 2520 &minus; 1 = 2519

Spot checks: 2519 &divide; 8 = 314 r 7,  2519 &divide; 9 = 279 r 8,  2519 &divide; 10 = 251 r 9.</div>
<p>Spotting the "one short of a multiple" pattern turns a problem with nine conditions into a single
LCM. If instead the remainder had been the same each time &mdash; say 1 every time &mdash; the answer
would be LCM + 1.</p>

<h3>D. Ordered triples with lcm(x,y) = 72, lcm(x,z) = 600, lcm(y,z) = 900</h3>
<div class="stack">72 = 2&sup3; &middot; 3&sup2;      600 = 2&sup3; &middot; 3 &middot; 5&sup2;      900 = 2&sup2; &middot; 3&sup2; &middot; 5&sup2;

Handle one prime at a time. lcm takes the maximum exponent, so each prime is independent.

Prime 2:  lcm(y,z) has 2&sup2;  &rarr;  y, z both at most 2
          lcm(x,y) has 2&sup3;  &rarr;  x must supply it, so x = 3
          max(y, z) = 2 with both in {0,1,2}  &rarr;  9 &minus; 4 = 5 pairs

Prime 3:  lcm(x,z) has 3&sup1;  &rarr;  x, z both at most 1
          lcm(x,y) has 3&sup2;  &rarr;  y = 2
          max(x, z) = 1 with both in {0,1}  &rarr;  4 &minus; 1 = 3 pairs

Prime 5:  lcm(x,y) = 72 has no 5  &rarr;  x = y = 0
          lcm(x,z) has 5&sup2;    &rarr;  z = 2                     &rarr;  1 way

Total: 5 &times; 3 &times; 1 = 15 ordered triples.
Examples: (8, 9, 300), (24, 36, 25), (24, 36, 300).</div>
<p>The move that makes this tractable is treating each prime as its own small counting problem,
because an LCM condition on a product of primes is really one condition per prime. Multiply the
counts at the end.</p>
"""

CHEAT = r"""
<table class="cmp">
  <tr><th>Situation</th><th>Move</th></tr>
  <tr><td>Factor a number</td><td>Split into any two factors, keep splitting until every piece is prime. Any route gives the same answer.</td></tr>
  <tr><td>Is n prime?</td><td>Test primes up to &radic;n only. Stop when the prime squared passes n.</td></tr>
  <tr><td>GCF</td><td>Primes in both, smaller exponent of each.</td></tr>
  <tr><td>LCM</td><td>Every prime in either, bigger exponent of each.</td></tr>
  <tr><td>Know three of a, b, GCF, LCM</td><td>a &middot; b = GCF &middot; LCM &mdash; one division gives the fourth.</td></tr>
  <tr><td>How many factors?</td><td>Add 1 to every exponent and multiply. 2&sup3; &middot; 3&sup2; &rarr; (3+1)(2+1) = 12.</td></tr>
  <tr><td>Perfect square / cube</td><td>Every exponent even / every exponent a multiple of 3.</td></tr>
  <tr><td>Smallest n-th power divisible by N</td><td>Round each exponent of N up to the next multiple of n.</td></tr>
  <tr><td>Given GCF(A, n)</td><td>Fix the shared exponents exactly, forbid the primes that would raise it, everything else free. No largest n.</td></tr>
  <tr><td>Given LCM(A, n)</td><td>n supplies what A lacks, caps at the LCM's exponents, no new primes. Largest n is the LCM itself.</td></tr>
  <tr><td>Primes in an equation</td><td>Shared divisor &rarr; forces one prime. Odd total with odd coefficients &rarr; one prime is 2. Then bound and check the survivors.</td></tr>
  <tr><td>Cycles lining up again</td><td>LCM.</td></tr>
  <tr><td>Pile split into equal groups</td><td>GCF.</td></tr>
  <tr><td>Same remainder every time</td><td>LCM, then add or subtract the remainder.</td></tr>
</table>
"""

GLOSSARY = r"""
<table class="cmp">
  <tr><th>Word</th><th>Means</th></tr>
  <tr><td>Divisor / factor</td><td>A number that divides another with no remainder. 28 is a factor of 616 because 616 = 28 &middot; 22.</td></tr>
  <tr><td>Multiple</td><td>The other side of the same relationship: 616 is a multiple of 28.</td></tr>
  <tr><td>Prime</td><td>Exactly two positive divisors: 1 and itself.</td></tr>
  <tr><td>Composite</td><td>More than two divisors. 1 is neither prime nor composite.</td></tr>
  <tr><td>Prime factorization</td><td>A number written as a product of primes. Unique apart from order.</td></tr>
  <tr><td>Exponent / power</td><td>The count of repeats: 2&sup3; means three 2s multiplied.</td></tr>
  <tr><td>Common</td><td>Shared by all the numbers in question.</td></tr>
  <tr><td>Greatest common factor</td><td>The largest divisor shared by all of them.</td></tr>
  <tr><td>Least common multiple</td><td>The smallest positive number that all of them divide.</td></tr>
  <tr><td>Parity</td><td>Whether a number is even or odd.</td></tr>
  <tr><td>Perfect square / cube</td><td>A number of the form k&sup2; / k&sup3; for a whole number k.</td></tr>
  <tr><td>Ordered triple</td><td>(x, y, z) where the positions matter, so swapping entries gives a different triple.</td></tr>
  <tr><td>Empty product</td><td>Choosing no factors at all. Its value is 1, which is why 1 divides everything.</td></tr>
</table>
"""

WRITEUP = r"""
<p>Three habits from the class that are worth more than any single technique.</p>
<div class="rulebox"><p><b>Show the work, not just the answer.</b> An answer with no working scores
zero &mdash; not out of strictness, but because the working is the only thing anyone can give feedback
on. If the method is right and the arithmetic slipped, that is a small fix; nobody can tell that from a
bare number.</p></div>
<div class="rulebox"><p><b>A hard problem is meant to take days.</b> Some problems in the set are
deliberately beyond a first sitting. Leaving one and coming back tomorrow is the intended way to use
it, not a sign of failing at it.</p></div>
<div class="rulebox"><p><b>Narrow first, guess last.</b> Divisibility, parity and bounds cut the
candidates down to a handful; then checking by hand is fast and safe. Guess-and-check as an opening
move is how you end up testing forty cases and trusting the one that looked right.</p></div>
"""
