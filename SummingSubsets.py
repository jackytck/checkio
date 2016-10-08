#!/usr/bin/python
def checkio(n):
    '''
    Let G(S) denote the sum of the elements of set S and F(n) be the sum of G(s) 
    for all subsets of the set consisting of the first n natural numbers. 
    For example, F(3) = (1) + (2) + (3) + (1 + 2) + (1 + 3) + (2 + 3) + (1 + 2 + 3) = 24. 
    Given n, calculate F(1) + F(2) + ... + F(n)
    '''
    ret = dp = 0
    for i in range(n):
        if i == 0:
            ret = dp = 1
        else:
            dp = 2 * dp + 2**i * (i + 1)
            ret += dp
    return ret

if __name__ == '__main__':
    assert checkio(2) == 7, "First"
    assert checkio(3) == 31, "Second"
    assert checkio(1) == 1, "Third"
    assert checkio(4) == 111, "4"
    print 'All ok'
