#!/usr/bin/python
def polynomial(s):
    if s == 'x':
        return [(1, 1)]
    else:
        return [(int(s), 0)]

def arith(t1, t2, op):
    def dict_to_poly(dic):
        return [(x[1], x[0]) for x in sorted(dic.iteritems(), reverse = True) if x[1] != 0]

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
            for k, v in d.iteritems():
                d2[k + t[1]] = v * t[0]
            adding.append(dict_to_poly(d2))
    if adding:
        while len(adding) >= 2:
            res = arith(adding[0], adding[1], '+')
            adding = [res] + adding[2:]
        return adding[0]
    else:
        return dict_to_poly(d)

def poly_to_str(toks):
    ret = ''
    for t in toks:
        c, d = t
        ret += '%+d*' % c if d > 0 else '%+d' % c
        ret += ('x*' * d)[:-1]
        ret = ret.replace('+1*', '+')
        ret = ret.replace('-1*', '-')
    if ret and ret[0] == '+':
        ret = ret[1:]
    return ret

def checkio(expr):
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

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert checkio(u"(x-1)*(x+1)") == "x*x-1", "First and simple"
    assert checkio(u"(x+1)*(x+1)") == "x*x+2*x+1", "Almost the same"
    assert checkio(u"(x+3)*x*2-x*x") == "x*x+6*x", "Different operations"
    assert checkio(u"x+x*x+x*x*x") == "x*x*x+x*x+x", "Don't forget about order"
    assert checkio("(2*x+3)*2-x+x*x*x*x") == "x*x*x*x+3*x+6", "All together"
