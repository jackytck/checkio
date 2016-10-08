#!/usr/bin/python
def checkio(n, m):
    z = len(bin(max(n, m))) - 2
    n, m = [bin(x)[2:].zfill(z) for x in (n, m)]
    return sum(1 for x, y in zip(n, m) if x != y)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"
