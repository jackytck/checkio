#!/usr/bin/python
import math

def ang(a, b, c):
    try:
        return int(round(math.acos(float(a*a + b*b - c*c)/(2*a*b)) / math.pi * 180)) % 180
    except:
        return 0

def checkio(a, b, c):
    return sorted([ang(a, b, c), ang(b, c, a), ang(a, c, b)])

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
