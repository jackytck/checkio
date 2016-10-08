#!/usr/bin/python
from fractions import Fraction

def checkio(alloys):
    """
        Find proportion of gold, assume exist unique solution.
    """
    #gold = Fraction(1, 1)
    #for k, v in alloys.iteritems():
    #    if 'gold' in k:
    #        gold -= (1 - v) / 2
    #    else:
    #        gold -= v / 2
    #return gold
    return 1 - sum([1 - v if 'gold' in k else v for (k, v) in alloys.iteritems()]) / 2

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio({
        'gold-tin': Fraction(1, 2),
        'gold-iron': Fraction(1, 3),
        'gold-copper': Fraction(1, 4),
        }) == Fraction(1, 24), "1/24 of gold"
    assert checkio({
        'tin-iron': Fraction(1, 2),
        'iron-copper': Fraction(1, 2),
        'copper-tin': Fraction(1, 2),
        }) == Fraction(1, 4), "quarter"
