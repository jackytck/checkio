#!/usr/bin/python
def trans(m):
    return [''.join(x) for x in zip(*m)]

def diag(m):
    return [m[0][0] + m[1][1] + m[2][2], m[2][0] + m[1][1] + m[0][2]]

def check(m, p):
    return [True for x in m if x == p*3]

def checkio(m):
    flat = m + trans(m) + diag(m)
    for x in 'XO':
        if check(flat, x):
            return x
    return 'D'

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        u"X.O",
        u"XX.",
        u"XOO"]) == "X", "Xs wins"
    assert checkio([
        u"OO.",
        u"XOX",
        u"XOX"]) == "O", "Os wins"
    assert checkio([
        u"OOX",
        u"XXO",
        u"OXX"]) == "D", "Draw"
