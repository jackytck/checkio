#!/usr/bin/python
import re

def coe_deg(s):
    coe = 1
    try:
        coe = int(re.match(r'[+-]?\d+', s).group())
    except:
        pass
    deg = s.count('x')
    return coe, deg

def tokens(s):
    s = s.replace('+', ' +')
    s = s.replace('-', ' -')
    s = s.replace('-x', '-1*x')
    return map(coe_deg, filter(None, s.split(' ')))

def deg(t):
    return t[0][1]

def arith(t1, t2, op):
    d = {}
    for t in t1:
        old = d.get(t[1], 0)
        d[t[1]] = old + t[0]
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
            d = d2
    return [(x[1], x[0]) for x in sorted(d.iteritems(), reverse = True) if x[1] != 0]

def lead_div_lead(t1, t2):
    return [(t1[0][0] / t2[0][0], t1[0][1] - t2[0][1])]

def tokens_to_str(toks):
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

def checkio(data):
    dividend, divider = data

    #n = d * q + r
    n, d = tokens(dividend), tokens(divider)
    q, r = [], n

    while r and deg(r) >= deg(d):
        t = lead_div_lead(r, d)
        q, r = arith(q, t, '+'), arith(r, arith(d, t, '*'), '-')

    return map(tokens_to_str, [q, r])

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(['x*x*x-12*x*x-42', 'x-3']) == ['x*x-9*x-27', '-123'], "1st"
    assert checkio(['x*x-1', 'x+1']) == ['x-1', ''], "2nd"
    assert checkio(['x*x*x+6*x*x+12*x+8', 'x+2']) == ['x*x+4*x+4', ''], "3rd"
    assert checkio(['x*x*x*x*x+5*x+1', 'x*x']) == ['x*x*x', '5*x+1'], "4th"
    assert checkio(['7*x*x*x*x*x-3*x*x*x+5*x', 'x*x-3*x-9']) == ['7*x*x*x+21*x*x+123*x+558','2786*x+5022'], "5th"
