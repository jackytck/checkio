#!/usr/bin/python
def checkio(opacity):
    a, d = (1 + 5**.5) / 2, 10000 - opacity
    if d == 0:
        return 0
    for i in range(2, 21):
        t = a**(i) / 5**.5
        s = round(a * t) + i - 3
        if s >= d:
            return min(round(t) + s - d, 5000)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"

    assert checkio(10000-22) == 16, "5 years"
    assert checkio(10000-16) == 8, "5 years"
    assert checkio(10000-13) == 11, "5 years"
    assert checkio(0) == 5000, "5 years"
