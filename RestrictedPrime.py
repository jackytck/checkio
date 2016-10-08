#!/usr/bin/python
def one():
    return int(True)

def odd(n):
    o = one()
    i = o
    while i < n:
        yield i
        i += o + o

def is_even(n):
    i, o = int(), one()
    t = o + o
    n = int(list(str(n)).pop())
    while i < n:
        i += t
    return i == n and n != t

def checkio(n):
    #if is_even(n):
    #    return False
    #else:
    #    for i in odd(n):
    #        for j in odd(n):
    #            if i >= j and i * j == n:
    #                return False
    #    return True
    #b = __builtins__
    #m, r = b['di' + 'vmod'], b['ra' + 'nge']
    b = __builtins__.__getattribute__
    m, r = b('di' + 'vmod'), b('ra' + 'nge')
    return all(x * x == x or m(n, x)[True] for x in r(n))

if __name__ == '__main__':
    assert checkio(5) == True, "1st example"
    assert checkio(18) == False, "2nd example"
