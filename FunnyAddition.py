#!/usr/bin/python
import math

def fact(x):
    if x == 0:
        return 1
    return reduce(lambda i, j: i * j, range(1, x + 1))

def exp(x):
    ret = 0
    try:
        for i in range(2012):
            ret += float(x ** i) / fact(i)
    except OverflowError:
        pass
    return ret

def checkio(data):
    'The sum of two integer elements'
    a,b = data
    return int(round(math.log(exp(a) * exp(b))))
    
if __name__ == '__main__':
    assert checkio([5, 5]) == 10, 'First'
    assert checkio([7,1]) == 8, 'Second'
    print 'All ok'
