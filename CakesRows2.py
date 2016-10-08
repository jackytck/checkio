#!/opt/local/bin/python3.3
from itertools import combinations
from fractions import Fraction
from collections import Counter


class Point(object):
    """ Represents a point or line in the projective plane.

    """

    def __init__(self, x, y, w=1):
        self.u = x
        self.v = y
        self.w = w

    def __mul__(self, other):
        """Standard cross product."""
        return Point(self.v * other.w - self.w * other.v,
                     self.w * other.u - self.u * other.w,
                     self.u * other.v - self.v * other.u)

    def __eq__(self, other):
        """Equal if two points cross to zero."""
        cross = self * other
        return cross.u == cross.v == cross.w == 0

    def __hash__(self):
        """Give the same hash iff two points are
        multiple of each other.

        """
        if self.u != 0:
            return hash((1, Fraction(self.v, self.u),
                        Fraction(self.w, self.u)))
        if self.v != 0:
            return hash((Fraction(self.u, self.v), 1,
                        Fraction(self.w, self.v)))
        return hash((0, 0, 1))


def checkio(cakes):
    """Count the number of unique line that passes
    through three or more points.

    Args:
        cakes: list of two integers
    Returns:
        number of unique line

    """
    lines = Counter()
    for p, q in combinations(cakes, 2):
        lines[Point(*p) * Point(*q)] += 1
    return sum(1 for i in lines.values() if i > 1)
