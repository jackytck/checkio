#!/usr/bin/python
def checkio(number):
    k = int((6 * number) ** (1.0 / 3))
    if k * (k + 1) * (k + 2) > 6 * number:
        k -= 1
    t = k * (k + 1) / 2
    s = t * (k + 2) / 3
    return t + max(number - s - t, 0)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"
