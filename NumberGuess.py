#!/usr/bin/python
def cong(r, m):
    return [x for x in range(1, 101) if x % m == r]

def divisor(g):
    g = [x[1] for x in g]
    return [x for x in range(2, 11) if x not in g][0]

def checkio(attempts):
    c = [cong(r, m) for (r, m) in attempts]
    s = set(c[0])
    for x in c[1:]:
        s = s.intersection(x)
    return divisor(attempts), list(s)[0]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    checkio([(1,5)])                # the number has a remainder 1
    checkio([(1,5),(2,3)])          # the number has a remainder 2
    checkio([(1,5),(2,3),(3,4)])    # the number has a remainder 3
    checkio([(1,5),(2,3),(3,4),(3,8)])    # the number has a remainder 3
