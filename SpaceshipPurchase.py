#!/usr/bin/python
import math
def checkio(offers):
    '''
       the amount of money that Petr will pay for the ride
    '''
    a, b, c, d = offers
    if a >= c:
        return a
    else:
        i = int(math.ceil(float(c-a) / (b+d)))
        bid = a + b * i
        ask = c - d * (i-1)
    return bid if bid < ask else ask

if __name__ == '__main__':
    assert checkio([150, 50, 1000, 100]) == 450, 'First'
    assert checkio([150, 50, 900, 100]) == 400, 'Second'
    print 'All is ok'
