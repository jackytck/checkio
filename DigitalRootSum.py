#!/usr/bin/python
from itertools import combinations

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

def digital_root(x):
    ret = x
    while ret > 9:
        ret = sum(ord(y)-48 for y in '%d' % ret)
    return ret

def digital_root_list(x):
    return sum(map(digital_root, x))

def minus(a, b):
    ret = []
    for x in a:
        ret.append(x)
    prod = 1
    for x in b:
        ret.remove(x)
        prod *= x
    ret.append(prod)
    return sorted(ret)

def combine(x):
    if len(x) < 2:
        return x
    sets = set()
    for c in combinations(x, 2):
        sets.add(c)
    ret = []
    for s in sets:
        ret.append(minus(x, s))
    return ret

def unique(x):
    sets = set()
    x = map(tuple, x)
    for i in x:
        sets.add(i)
    return sets

def checkio(value):
    'calculate sum of the digital roots of a numbers which are the results of factorization of the specified number'
    primes = prime_factors(value)
    all_factors = [primes]
    def recur(x):
        for n in combine(x):
            all_factors.append(n)
            if len(n) > 1:
                recur(n)
    recur(primes)
    all_factors = unique(all_factors)
    return sum(map(digital_root_list, all_factors))
    
if __name__ == '__main__':
    assert checkio(50) == 32, 'First'
    assert checkio(100) == 75, 'Second'
    assert checkio(999) == 75, 'Third'
    assert checkio(9999) == 117, 'Fourth'
    print 'All ok'
