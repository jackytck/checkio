#!/usr/bin/python
def prime_factors(x):
    ret = []
    c = x
    while c % 2 == 0:
        ret.append(2)
        c /= 2
    i = 3
    while i <= c**0.5 + 1:
        if c % i == 0:
            ret.append(i)
            c /= i
        else:
            i += 2
    if c > 1:
        ret.append(c)
    return ret

def factors_234(xs):
    ret = []
    x = 1
    for c in xs:
        x *= c
    i = 9
    while i > 1:
        if x % i == 0:
            ret.append(i)
            x /= i
        else:
            i -= 1
    return ret

def checkio(data):
    ret = []
    facs = prime_factors(data)
    f234 = []
    for f in facs:
        if f >= 11:
            return 0
        elif f < 5:
            f234.append(f)
        else:
            ret.append(f)
    ret.extend(factors_234(f234))
    return int(''.join([str(x) for x in sorted(ret)]))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(5) == 5, "5th example"

