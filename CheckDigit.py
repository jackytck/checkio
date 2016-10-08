#!/usr/bin/python
import re

def digital_root(x):
    return sum(ord(y) - ord('0') for y in '%d' % x)

def map_point(i, c):
    d = ord(c) - ord('0')
    if i % 2 == 0:
        return digital_root(2 * d)
    else:
        return d

def checkio(data):
    data = re.sub(r'[\W_a-z]+', '', data)
    sd = sum([map_point(i, x) for i, x in enumerate(reversed(data))])
    return ['%d' % (-sd % 10), sd]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert (checkio(u"799 273 9871") == ["3", 67]), "First Test"
    assert (checkio(u"139-MT") == ["8", 52]), "Second Test"
    assert (checkio(u"123") == ["0", 10]), "Test for zero"
    assert (checkio(u"999_999") == ["6", 54]), "Third Test"
    assert (checkio(u"+61 820 9231 55") == ["3", 37]), "Fourth Test"
    assert (checkio(u"VQ/WEWF/NY/8U") == ["9", 201]), "Fifth Test"

    print("OK, done!")
