#!/usr/bin/python
def checkio(data):
    'calculate sum of the factorials for all digits of the specified positive integer number.'
    fac = (1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880)
    ret = 0
    for i in str(data):
        ret += fac[int(i)]
    return ret
    
if __name__ == '__main__':
    assert checkio(100) == 3, 'First'
    assert checkio(222) == 6, 'Second'
    assert checkio(1234) == 33, 'Third'
    print 'All ok'
