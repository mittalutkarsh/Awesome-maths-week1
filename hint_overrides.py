# -*- coding: utf-8 -*-
"""Rewrites for nudges/hints that stated the step's answer outright.
Key: (problem id, step index 0-based, field). Field is 'hint' or 'n0'/'n1'/'n2'
for the first, second and third nudge, or 'workHint'."""

OVER = {
# ---------------- practice set ----------------
("q1", 2, "hint"): "Collect the leaves of both branches, then count how many copies of each prime you ended up with.",
("q2", 2, "hint"): "Collect the leaves of both branches, then fold repeated primes into a power.",
("q3", 0, "hint"): "Cross out any prime that appears in only one of the two lists. Whatever survives is your answer.",
("q3", 1, "hint"): "Multiply the smaller power of each shared prime together.",
("q4", 0, "hint"): "Write both prime lists side by side and merge them, dropping anything you have already written.",
("q5", 2, "hint"): "Keep only the primes in both lists, each at its smaller exponent, then multiply those together.",
("q6", 0, "hint"): "Go prime by prime — 2, then 5, then 7, then 11 — and keep the larger exponent of each.",
("q6", 1, "n2"): "40 × 49 = 1960. Now multiply that by 11.",
("q6", 2, "hint"): "Work out 28 × 21,560, and separately 616 × 980. The identity says the two must match.",
("q7", 0, "hint"): "One of the four numbers is a pure power of 2. That one sets the highest power of 2 needed.",
("q7", 1, "hint"): "Take the biggest power of 2, then the 3, then the 5, and multiply them.",
("q7", 2, "hint"): "Ask how many 30s fit into 120.",
("q8", 1, "hint"): "Write out the three conditions on n, then build the smallest number that meets all of them.",
("q9", 0, "hint"): "Start from 1800 = 18 × 100 and break each of those two parts down.",
("q9", 1, "hint"): "Only what 225 is missing has to come from n. Nothing else is required.",
("q9", 2, "hint"): "Push every allowed exponent up to its maximum, then multiply.",
("q10", 0, "hint"): "Look at the last digit and decide even or odd. Then think about what that forces.",
("q10", 1, "hint"): "There is exactly one even prime number. Name it.",
("q10", 2, "hint"): "Subtract 2 from 2019, then test the result for primality.",
("q11", 2, "hint"): "Shared primes only, each at its smaller exponent, then multiply.",
("q11", 3, "hint"): "Every prime that appears anywhere, each at its larger exponent, then multiply.",
("q11", 4, "hint"): "Instead of long division, cancel the shared prime powers: subtract the exponents.",
("q12", 1, "hint"): "After substituting a you get 5b + 15c = 55. Divide that whole line by 5.",
("q12", 1, "n2"): "Divide the line 5b + 15c = 55 through by 5.",
("q12", 2, "hint"): "Work out b = 11 − 3c for c = 2, then c = 3, then c = 5, and see which give a prime b.",
("q13", 1, "hint"): "After substituting c you get 3a + 6b = 21. Divide that whole line by 3.",
("q13", 1, "n2"): "Divide the line 3a + 6b = 21 through by 3.",
("q13", 2, "hint"): "Work out a = 7 − 2b for b = 2, then b = 3, and ask which of those a values is prime.",
("q13", 2, "n1"): "Work out a = 7 − 2b for b = 2 and for b = 3. Only one of those a values is prime.",
("q14", 1, "hint"): "There is exactly one even prime number, so that has to be the even one here.",
("q14", 2, "hint"): "Subtract 2 from 55, then test whether the result is prime.",
("q14", 2, "n1"): "Once you subtract, test the result with primes up to 7, since 8² = 64 is already past it.",
("q14", 2, "n2"): "Your number is odd, its digits add to 8, it does not end in 0 or 5, and dividing by 7 is not whole.",
("q15", 1, "hint"): "Biggest power of 2 among the four numbers, times the 3 that 12 brings in.",
("q15", 3, "hint"): "Add up the month lengths to the end of November, then see how far past that day 338 lands.",
("q16", 0, "hint"): "Biggest power of 2 among the three, then the 3 and the 5 as well.",
("q16", 1, "hint"): "Divide 240 by 16.",
("q17", 0, "hint"): "Find the first number that appears in both lists of multiples.",
("q17", 1, "hint"): "Divide 60 by the gap you found in step 1.",
("q18", 1, "hint"): "Step each exponent of n up to the next multiple of 3 — do it for the exponent 4.",
("q18", 2, "hint"): "Split each exponent of p³q³r⁶ by 3 to write it as a single cube, then find the matching choice.",
("q19", 1, "hint"): "k² needs 2⁴ · 3² at the very least, so halve those exponents to see what k itself needs.",
("q19", 2, "hint"): "Divide 1000 by 12 and keep the whole-number part. The multiples start at 12 · 1.",
("q19", 2, "n1"): "Divide 1000 by 12 — the whole-number part tells you how many multiples fit.",
("q19", 2, "n2"): "The count is just how many multiplier values there are, starting from 1.",
("q20", 0, "hint"): "The identity says a · b equals GCF × LCM, and the problem already handed you that product.",
("q20", 1, "hint"): "Go down the factor pairs of 384 and subtract each pair. Stop when the difference is 8.",
("q21", 0, "hint"): "Factor both prices and pull out the part they share — that is their GCF.",
("q21", 0, "n2"): "Pull the shared factor out in front: 300p + 210g = (shared factor)(10p + 7g).",
("q21", 1, "hint"): "Try five pigs paid with seven goats back as change: work out 5(300) − 7(210).",
("q21", 1, "n1"): "Try p = 5 and g = −7, then work out 1500 − 1470.",
("q21", 1, "n2"): "Every payable amount is a multiple of your step-1 number, so the smallest positive debt is that number itself.",
("q22", 2, "n2"): "After subtracting, check one case: divide your answer by 8 and confirm the remainder is 7.",
("q23", 0, "hint"): "The least possible money is the LCM of 12, 14 and 15 — biggest power of each prime.",
("q23", 1, "hint"): "Divide his money by the price of one purple candy.",
("q23", 1, "n1"): "Cancel a zero from each number, then work out 42 ÷ 2.",
("q24", 0, "hint"): "Start from 600 = 6 × 100 and factor each of those two parts.",
("q24", 1, "hint"): "y₂ is capped at 2 by the 900 condition, yet lcm(x, y) needs the full power of 2 in 72 — so x must supply it.",
("q24", 2, "hint"): "Count all pairs from {0,1,2} × {0,1,2}, then subtract the ones where both entries are below 2.",
("q24", 2, "n2"): "Take 9 and subtract 4.",
("q24", 3, "hint"): "x₃ is capped at 1, so x cannot supply the two 3s that lcm(x, y) needs. That leaves y.",
("q24", 4, "hint"): "Count all pairs from {0,1} × {0,1}, then remove the one where both entries are 0.",
("q24", 4, "n2"): "Take 4 and subtract 1.",

# ---------------- lesson page ----------------
("g1", 1, "hint"): "You already found a divisor. Divide 91 by it and check that both pieces are prime.",
("g4", 2, "hint"): "Multiply the smaller power of each shared prime.",
("g5", 0, "hint"): "Go prime by prime and keep the larger exponent each time.",
("g5", 1, "n1"): "4 × 9 = 36. Now multiply that by 7.",
("g5", 1, "n2"): "Check your result: it has to divide exactly by both 84 and 126.",
("g6", 0, "hint"): "48 × 18 = 864. Now put the factor of 10 back.",
("g7", 0, "n2"): "The smallest choice is 3² and nothing else at all — work that number out.",
("g8", 0, "hint"): "5b is even and 5 is odd, so b is even — and only one prime number is even.",
("g8", 0, "n2"): "Only one prime number is even. That is the one.",
("g8", 1, "n2"): "After dividing, check whether your a is prime.",
("g9", 1, "hint"): "Take each exponent of 720 and step it up to the next multiple of 3.",
("g9", 1, "n2"): "Write your three rounded prime powers as one product.",
("g9", 2, "n2"): "Work out 60 × 60 × 60.",
("g10", 0, "hint"): "Take the biggest power of 2 and the biggest power of 3 across 9 and 12.",
("g11", 0, "hint"): "Shared primes at their smaller powers, multiplied.",
("g11", 1, "hint"): "Divide the pencils by the number of kits.",
("g11", 1, "n2"): "Then do the same with the erasers: 36 ÷ 12.",
("g12", 0, "hint"): "Biggest power of 2, biggest power of 3, then the 5 — multiply them.",
("g12", 1, "n2"): "Check your answer: divide it by 4 and confirm the remainder is 1.",

# ---------------- work-box templates that were too generous ----------------
("q12", 0, "workHint"): "rearrange so one side is a multiple of 5:  4a = …",
("q13", 0, "workHint"): "rearrange so one side is a multiple of 3:  2c = …",
("g8", 0, "workHint"): "5b = 54 − 4a = 2(…)",
("q3", 0, "workHint"): "440: 2,2,2,5,11     2020: 2,2,5,101     in both: …",
}


# second pass: remaining outright giveaways
OVER.update({
("q20", 1, "n2"): "Work down your list subtracting each pair. The pairs nearest the middle of the list are the closest together.",
("q7", 0, "n1"): "The biggest pile of 2s belongs to two of the four numbers: the one that is a pure power of 2, and 24.",
("q8", 1, "n2"): "n may contain no 5, since 240 has a 5 and sharing it would push the GCF past 12. So build n from only the primes it is required to have.",
("q12", 0, "hint"): "4a is a multiple of 5 while 4 is not, so a itself must carry that factor of 5 \u2014 and only one prime can.",
("q13", 0, "hint"): "2c is a multiple of 3 while 2 is not, so c itself must carry that factor of 3 \u2014 and only one prime can.",
("g8b", 0, "hint"): "14b is a multiple of 3 while 14 is not, so b itself must carry that factor of 3 \u2014 and only one prime can.",
})


# third pass: nudges that asserted the answer in prime-power form
OVER.update({
("q9", 1, "n2"): "n may contain no other primes \u2014 they would show up in the LCM. So n is exactly the power of 2 that 1800 needs. Multiply it out.",
("q9", 2, "n2"): "Push each allowed exponent to its maximum, then multiply the three prime powers out.",
("q11", 4, "n1"): "Shortcut: subtract exponents instead of dividing. (2\u00b2 \u00b7 3\u00b3 \u00b7 5 \u00b7 11) \u00f7 (2 \u00b7 3\u00b2) leaves one 2, one 3, the 5 and the 11 \u2014 multiply those.",
("q19", 1, "n2"): "k must contain 2\u00b2 and one 3. Multiply those together.",
("q22", 1, "hint"): "Take 2\u00b3 from 8, 3\u00b2 from 9, then the 5 and the 7, and multiply them out.",
("g10", 0, "n1"): "9 = 3\u00b2 and 12 = 2\u00b2 \u00b7 3, so take 2\u00b2 \u00b7 3\u00b2 and multiply it out.",
("g12", 0, "n2"): "Multiply 4 \u00d7 3 \u00d7 5.",
})

FACTOR_PLACEHOLDER = "like 2^4*7^2"
NUMS_PLACEHOLDER = "numbers separated by commas"


def apply(problems):
    """Apply overrides in place; returns number of edits. Raises on a stale key."""
    index = {}
    for p in problems:
        for i, s in enumerate(p["steps"]):
            index[(p["id"], i)] = s
    used = set()
    for (pid, i, field), text in OVER.items():
        s = index[(pid, i)]          # KeyError => stale override
        if field.startswith("n") and field[1:].isdigit():
            s["nudges"][int(field[1:])] = text
        else:
            s[field] = text
        used.add((pid, i, field))
    # nothing hint-like may be visible before the hint button is pressed:
    # the work area gets one generic placeholder, never a scaffold for this step
    for p in problems:
        for s in p["steps"]:
            s.pop("workHint", None)
    # a date placeholder that does not name the date
    for p in problems:
        if p["id"] == "q15":
            p["steps"][3]["placeholder"] = "a date \u2014 month and day"
    # neutral answer-box placeholders
    for p in problems:
        for s in p["steps"]:
            if s["type"] == "factor":
                s["placeholder"] = FACTOR_PLACEHOLDER
            elif s["type"] == "nums":
                s["placeholder"] = NUMS_PLACEHOLDER
    return len(used)


# ============================================================================
# Step questions must read as questions. No step may carry the method, the
# factor pair to start from, or an intermediate result the child has not
# worked out yet. Anything like that belongs behind the hint button.
# ============================================================================

ASK = {
("q1", 2): "Write 440 as a product of primes, using exponents.",
("q2", 0): "Write 2020 as a product of primes, using exponents.",
("q2", 1): "Is 101 prime? Answer yes or no, and say which divisors you tested.",
("q3", 0): "Which primes appear in both 440 and 2020?",
("q3", 1): "What is the largest number that can be built out of the primes they share?",
("q4", 0): "Which primes appear in 440 or in 2020, or in both?",
("q5", 2): "What is GCF(616, 980)?",
("q6", 0): "Write LCM(616, 980) as a product of prime powers.",
("q6", 1): "What is LCM(616, 980) as a single number?",
("q6", 2): "What is 616 \u00d7 980?",
("q7", 0): "What is the highest power of 2 that the LCM must contain? Give it as a number.",
("q7", 1): "What is LCM(6, 8, 24, 30)?",
("q7", 2): "Check your answer: 120 \u00f7 30 = ?",
("q8", 1): "What is the smallest possible value of n?",
("q8", 2): "Is there a largest possible value of n? Answer yes or no, and say why.",
("q9", 0): "Write 1800 as a product of primes.",
("q10", 0): "Is 2019 odd or even?",
("q10", 1): "Which prime must be one of the two?",
("q10", 2): "What are the two primes?",
("q11", 2): "What is GCF(180, 594)?",
("q11", 4): "What is LCM \u00f7 GCF?",
("q12", 0): "What must a equal?",
("q12", 1): "What does b + 3c equal?",
("q12", 2): "Which prime values of c work?",
("q12", 3): "With that larger value of c, what is b?",
("q13", 0): "What must c equal?",
("q13", 1): "What does a + 2b equal?",
("q13", 2): "What is b?",
("q13", 3): "What is a?",
("q14", 0): "What is b?",
("q14", 1): "a + c = 55. What is the smaller of those two primes?",
("q14", 2): "And the other one?",
("q15", 1): "How many weeks pass before all four ships are in port together?",
("q16", 0): "What is LCM(12, 16, 20)?",
("q16", 1): "Check your answer: how many round trips does the 16-day ship make in that time?",
("q18", 1): "What is the smallest multiple of 3 that is at least 4?",
("q18", 2): "Which answer choice is the smallest cube?",
("q19", 1): "If k\u00b2 is a multiple of 24, then k itself must be a multiple of which number?",
("q19", 2): "k\u00b2 has to stay below 10\u2076. How many values of k work?",
("q20", 0): "What is the product of the two numbers?",
("q20", 1): "What are the two numbers?",
("q21", 0): "Every debt that can be settled with pigs and goats is a multiple of what number?",
("q21", 1): "What is the smallest debt that can actually be paid? Give it in dollars, and show in your working one way to pay it.",
("q22", 0): "What is true about (the number + 1)?",
("q22", 2): "What is the least such whole number?",
("q23", 0): "What is the smallest amount of money, in cents, that Casper could have?",
("q23", 1): "How many purple candies can he buy with that?",
("q24", 0): "Write 600 as a product of primes.",
("q24", 1): "Take the prime 2 on its own. What is the exponent of 2 in x?",
("q24", 2): "Still on the prime 2: how many (y\u2082, z\u2082) pairs are possible?",
("q24", 3): "Now the prime 3. What is the exponent of 3 in y?",
("q24", 4): "Still on the prime 3: how many (x\u2083, z\u2083) pairs are possible?",
("q24", 5): "How many ordered triples are there altogether?",

("g1", 0): "Is 91 prime? Answer yes or no, and say which divisors you tested.",
("g2", 0): "Write 120 as a product of primes, using exponents.",
("g2", 1): "Now build it again starting from a different factor pair. Do you get the same primes? Answer yes or no.",
("g3", 1): "How many factors does 72 have?",
("g4", 2): "What is GCF(84, 126)?",
("g5", 0): "Write LCM(84, 126) as a product of prime powers.",
("g5", 1): "What is LCM(84, 126) as a single number?",
("g6", 1): "What is LCM(48, 180)?",
("g7", 0): "What is the smallest n that works?",
("g8", 0): "What is b?",
("g8", 1): "What is a?",
("g8b", 0): "What must b be?",
("g8b", 1): "What is a?",
("g8b", 2): "Is that value of a prime? So what is the answer to the problem?",
("g8c", 0): "How many of the two primes a and b can be even?",
("g8c", 1): "Take the case a = 2, which gives 9b = 9993. Is that case possible? Answer yes or no.",
("g8c", 2): "Take the case b = 2. What is a?",
}

# Steps kept, in order, by original index. Used where the old decomposition
# only existed to hand over the first factor split.
STEPS = {
"q1": [2],
"q2": [0, 1],
}

# Extra hints for steps whose scaffolding moved out of the question.
HINT_ADD = {
("q1", 2): "Start the tree with 440 = 44 \u00d7 10 (or 8 \u00d7 55 \u2014 either works), then break each part down until every piece is prime.",
("q2", 0): "Start with 2020 = 10 \u00d7 202, then break each part down.",
("q6", 0): "Go prime by prime \u2014 2, then 5, then 7, then 11 \u2014 keeping the larger exponent of each. You factored both numbers in problem 5.",
("q6", 2): "Multiply 616 by 980 directly. Then compare it with GCF \u00d7 LCM = 28 \u00d7 21,560 \u2014 the identity says they match.",
("q7", 0): "Factor all four numbers. One of them is a pure power of 2, and that one sets the highest power needed.",
("q9", 0): "Start with 1800 = 18 \u00d7 100 and break each part down. You will also want 225 = 3\u00b2 \u00b7 5\u00b2 for the next step.",
("q10", 0): "Look at the last digit of 2019.",
("q10", 1): "An odd total needs one even addend and one odd one, and only one prime is even.",
("q12", 0): "5b, 15c and 75 are all multiples of 5, so 4a must be too. Since 4 is not, a itself carries that 5 \u2014 and only one prime can.",
("q13", 0): "3a, 6b and 27 are all multiples of 3, so 2c must be too. Since 2 is not, c itself carries that 3 \u2014 and only one prime can.",
("q14", 0): "Subtract the second equation from the first: the a and the c cancel.",
("q14", 1): "55 is odd, and odd + odd = even, so the two primes cannot both be odd. Only one prime is even.",
("q19", 2): "k\u00b2 < 10\u2076 means k < 1000. Count the multiples of 12 in that range: divide 1000 by 12 and keep the whole-number part.",
("q20", 0): "For any two numbers, a \u00b7 b = GCF(a, b) \u00b7 LCM(a, b), and the problem already gives you that product.",
("q21", 0): "Any payment is 300p + 210g with p and g whole numbers, possibly negative. Factor both prices and pull out what they share.",
("q22", 0): "Each remainder is exactly one less than its divisor, so the number is always one short of a multiple.",
("q23", 0): "If 12 pieces cost exactly his money, his money is a multiple of 12 \u2014 and the same for 14 and 15.",
("q24", 1): "lcm(y, z) = 900 caps y and z at 2\u00b2, yet lcm(x, y) = 72 needs 2\u00b3. So x has to supply it.",
("q24", 3): "lcm(x, z) = 600 carries only one 3, so x cannot supply the two 3s that lcm(x, y) = 72 needs.",
("g2", 0): "Any starting split works: 12 \u00d7 10, or 4 \u00d7 30, or 8 \u00d7 15. Break each part down until every piece is prime.",
("g3", 1): "A factor is built by choosing how many of each prime to take. Count the choices for the 2s, count the choices for the 3s, and multiply.",
("g5", 0): "Go prime by prime across 84 = 2\u00b2 \u00b7 3 \u00b7 7 and 126 = 2 \u00b7 3\u00b2 \u00b7 7, keeping the larger exponent each time.",
("g6", 1): "The identity gives LCM = (a \u00b7 b) \u00f7 GCF, and you already have the product.",
("g7", 0): "36 = 2\u00b2 \u00b7 3\u00b2 and 9 = 3\u00b2. Work out what n must contain and what it must avoid.",
("g8", 0): "5b = 54 \u2212 4a = 2(27 \u2212 2a), so 5b is even. Since 5 is odd, b is even \u2014 and only one prime is.",
("g8b", 0): "879 is divisible by 3, so 14b = 879 \u2212 9a = 3(293 \u2212 3a). Since 14 carries no 3, b must.",
("g8c", 0): "Both coefficients are odd and the total is odd, and odd + odd = even.",
("g8c", 1): "Test 9993 for divisibility by 9 by adding its digits.",
}


def apply_asks(problems):
    """Rewrite step questions, add the hints that replace the old scaffolding,
    and drop steps that existed only to hand over a factor split."""
    index = {}
    for p in problems:
        for i, s in enumerate(p["steps"]):
            index[(p["id"], i)] = s
    for key, text in ASK.items():
        index[key]["ask"] = text
    for key, text in HINT_ADD.items():
        index[key]["hint"] = text
    for pid, keep in STEPS.items():
        for p in problems:
            if p["id"] == pid:
                p["steps"] = [p["steps"][i] for i in keep]
    return len(ASK) + len(HINT_ADD)

ASK.update({
("q7", 2): "Check your answer: divide it by 30. What do you get?",
("q15", 2): "How many days is that?",
("q15", 3): "Counting that many days on from noon on 2 January 2010, what date do you land on? (Month and day.)",
("g9", 1): "Write the smallest cube that is divisible by 720 as a product of prime powers.",
("g9", 2): "What is that number?",
("g10", 0): "How many seconds until the two lamps flash together again?",
("g11", 0): "What is the largest number of kits?",
("g12", 1): "What is the smallest such number?",
})
HINT_ADD.update({
("g9", 1): "A cube needs every exponent divisible by 3, and it must keep every exponent of 720. Step each one up to the next multiple of 3.",
("g10", 0): "Repeating events lining up again is a least-common-multiple question. Factor 9 and 12.",
("g11", 0): "Splitting a fixed pile into equal groups with nothing left over is a greatest-common-factor question. Factor 24 and 36.",
("g12", 1): "If a number leaves remainder 1 on division by all of them, then the number minus 1 is a common multiple. You just found the smallest one.",
})
