#!/usr/bin/python
import itertools

def checkio(data):
    ret = 0
    for c in itertools.combinations(data, 3):
        if c[0] + c[1] < c[2] or c[0] + c[2] < c[1] or c[1] + c[2] < c[0]:
            ret += 1
    return ret

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio((4, 2, 10)) == 1, "First"
    assert checkio((1, 2, 3)) == 0, "Second"
    assert checkio((5, 2, 9, 6)) == 2, "Third"
