#!/opt/local/bin/python3.3
import math

#ref: http://en.wikipedia.org/wiki/Spheroid
def checkio(height, width):
    a, c = width / 2, height / 2
    v = 4 * math.pi / 3 * a ** 2 * c

    s = v * 3 / c
    if c < a:
        e = (1 - c ** 2 / a ** 2) ** 0.5
        s = s / 2 * (1 + (1 - e ** 2) / e * math.atanh(e))
    elif c > a:
        e = (1 - a ** 2 / c ** 2) ** 0.5
        s = s / 2 * (1 + c / a / e * math.asin(e))

    return [round(v, 2), round(s, 2)]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 2) == [8.38, 21.48], "Prolate spheroid"
    assert checkio(2, 2) == [4.19, 12.57], "Sphere"
    assert checkio(2, 4) == [16.76, 34.69], "Oblate spheroid"
