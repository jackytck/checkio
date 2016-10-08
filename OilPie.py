#!/opt/local/bin/python3.3
from fractions import Fraction


def divide_pie(groups):
    pie = 1
    size = sum(abs(x) for x in groups)
    for g in groups:
        if g > 0:
            pie -= Fraction(g, size)
        else:
            pie *= Fraction(size + g, size)
    return pie.numerator, pie.denominator

if __name__ == '__main__':
    assert isinstance((2, -2), (tuple, list)), "Return tuple or list"
    assert tuple(divide_pie((2, -1, 3))) == (1, 18), "Example"
    assert tuple(divide_pie((1, 2, 3))) == (0, 1), "All know about the pie"
    assert tuple(divide_pie((-1, -1, -1))) == (8, 27), "One by one"
    assert tuple(divide_pie((10,))) == (0, 1), "All together"
