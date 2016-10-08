#!/opt/local/bin/python3.3
def polynomial(s):
    return [(1, 1)] if s == 'x' else [(int(s), 0)]


def arith(t1, t2, op):

    def dict_to_poly(dic):
        return [(c, d) for d, c in sorted(dic.items(), reverse=True) if c]

    d = {}
    for t in t1:
        old = d.get(t[1], 0)
        d[t[1]] = old + t[0]
    adding = []
    for t in t2:
        old = d.get(t[1], 0)
        if op == '+':
            d[t[1]] = old + t[0]
        elif op == '-':
            d[t[1]] = old - t[0]
        elif op == '*':
            d2 = {}
            for k, v in d.items():
                d2[k + t[1]] = v * t[0]
            adding.append(dict_to_poly(d2))
    if adding:
        while len(adding) >= 2:
            res = arith(adding[0], adding[1], '+')
            adding = [res] + adding[2:]
        return adding[0]
    else:
        return dict_to_poly(d)


def poly_to_str(poly):
    ret = ''
    for t in poly:
        c, d = t
        ret += '%+d*' % c if d > 0 else '%+d' % c
        ret += 'x**%d' % d
        ret = ret.replace('+1*', '+')
        ret = ret.replace('-1*', '-')
        ret = ret.replace('x**0', '')
        ret = ret.replace('x**1', 'x')
    if ret and ret[0] == '+':
        ret = ret[1:]
    return ret or '0'


def simplify(expr):
    s1, s2, digit = [], [], ''
    op, prec = '+-*()', {'+': 1, '-': 1, '*': 2}

    def consume():
        a, b, o = s1.pop(), s1.pop(), s2.pop()
        s1.append(arith(b, a, o))

    for e in expr:
        if e in op and digit:
            s1.append(polynomial(digit))
            digit = ''
        if e not in op:
            digit += e
        elif e == '(':
            s2.append(e)
        elif e == ')':
            while s2 and s2[-1] != '(':
                consume()
            s2.pop()
        else:
            while s2 and s2[-1] != '(' and prec[e] <= prec[s2[-1]]:
                consume()
            s2.append(e)
    if digit:
        s1.append(polynomial(digit))
    while s2:
        consume()
    return poly_to_str(s1[0])


if __name__ == "__main__":
    assert simplify("(x-1)*(x+1)") == "x**2-1", "First and simple"
    assert simplify("(x+1)*(x+1)") == "x**2+2*x+1", "Almost the same"
    assert simplify("(x+3)*x*2-x*x") == "x**2+6*x", "Different operations"
    assert simplify("x+x*x+x*x*x") == "x**3+x**2+x", "Don't forget about order"
    assert simplify("(2*x+3)*2-x+x*x*x*x") == "x**4+3*x+6", "All together"
    assert simplify("x*x-(x-1)*(x+1)-1") == "0", "Zero"
    assert simplify("5-5-x") == "-x", "Negative C1"
    assert simplify("x*x*x-x*x*x-1") == "-1", "Negative C0"
