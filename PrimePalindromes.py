#!/usr/bin/python
def isPrime(a):
    for i in range(2, a):
        if a % i == 0:
            return False
    return True

def isPal(a):
    s = '%d' % a
    if s == s[::-1]:
        return True
    return False

def checkio(data):
    while True:
        if isPal(data) and isPrime(data):
            return data
        else:
            data += 1

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(31) == 101, 'First example'
    assert checkio(130) == 131, 'Second example'
    assert checkio(131) == 131, 'Third example'
