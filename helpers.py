SUPS = "\u2070\u00b9\u00b2\u00b3\u2074\u2075\u2076\u2077\u2078\u2079"

def pretty(expr):
    """2^3*5*11 -> 2\u00b3 \u00b7 5 \u00b7 11"""
    out = []
    for tok in expr.split("*"):
        if "^" in tok:
            b, e = tok.split("^")
            out.append(b + "".join(SUPS[int(c)] for c in e))
        else:
            out.append(tok)
    return " \u00b7 ".join(out)

def val(expr):
    v = 1
    for tok in expr.split("*"):
        if "^" in tok:
            b, e = tok.split("^"); v *= int(b) ** int(e)
        else:
            v *= int(tok)
    return v

def step(ask, type, answer, *args, **kw):
    """step(ask, type, answer, nudges, hint, solution) or, for text steps,
       step(ask, 'text', answer, regex_list, nudges, hint, solution)."""
    if len(args) == 4:
        rex, nudges, hint, solution = args
        kw.setdefault("re", rex)
    else:
        nudges, hint, solution = args
    d = dict(ask=ask, type=type, answer=answer, nudges=nudges, hint=hint, solution=solution,
             recheck="Redo this step on paper before you close the page.")
    d.update(kw)
    return d

def pf_step(n, ans, split, ask=None, placeholder="like 2^2*3*7"):
    """A standard 'write n as a product of primes' step."""
    b1, b2 = split
    return step(
        ask or f"Write <span class='m'>{n}</span> as a product of prime numbers.",
        "factor", ans,
        [f"Find any divisor you can see. Does 2 go into {n}? Does 3? Does 5?",
         "Keep splitting every piece that is not prime. Stop only when every piece on the tree is prime.",
         f"Multiply your pieces back together \u2014 you must land exactly on {n}."],
        f"Start the tree with {n} = {b1} \u00d7 {b2}, then break each of those two numbers down.",
        f"{n} = {pretty(ans)}",
        placeholder=placeholder,
        workHint=f"{n} = ___ \u00d7 ___, then split each part until every piece is prime",
        why="Every number has exactly one prime factorization, so this is the one right answer.",
        forward="you now have the primes you need",
    )

def gcf_step(a, b, fa, fb, g, extra=""):
    return step(
        f"Now take the <b>smaller</b> power of each shared prime. What is GCF({a}, {b})?",
        "num", g,
        ["Line up the two factorizations. Which primes appear in both lists?",
         "For each shared prime, keep the smaller exponent. A prime in only one list is not shared, so it is out.",
         f"Multiply the kept primes together. Then check your answer divides both {a} and {b}."],
        "Keep only the primes in both lists, each at its smaller exponent, then multiply those together.",
        f"GCF({a}, {b}) = {g}. {extra}",
        placeholder="a number",
        workHint=f"{a} = {fa}\n{b} = {fb}\nshared: \u2026",
    )

def lcm_step(a, b, l, extra=""):
    return step(
        f"Now take the <b>bigger</b> power of every prime that shows up in either number. What is LCM({a}, {b})?",
        "num", l,
        ["A multiple of both must contain everything both numbers need.",
         "For each prime, keep the larger exponent \u2014 and do not forget primes that appear in only one of the numbers.",
         f"Check: your answer must divide evenly by both {a} and {b}."],
        f"Bigger exponent of every prime, then multiply.",
        f"LCM({a}, {b}) = {l}. {extra}",
        placeholder="a number",
    )

YESNO_NO = [r"^\s*no\b", r"\bno largest\b", r"\bnot\b", r"\bunbounded\b", r"infinit", r"forever",
            r"as (big|large) as", r"keep going", r"never ends", r"none", r"\bcomposite\b"]
YESNO_YES = [r"^\s*yes\b", r"\bthere is\b", r"\bexists\b", r"\byep\b", r"\byeah\b"]
NO_REJECT = [r"^\s*yes\b", r"^\s*yep\b"]
YES_REJECT = [r"^\s*no\b", r"\bnot\b", r"\bnope\b"]
