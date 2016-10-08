#!/usr/bin/python
def checkio(values):
    'Calculate the greatest common divisor of two numbers'
    a, b = values
    if a == 0:
        return b
    if b == 0:
        return a
    if a >= b:
        return checkio((a % b, b))
    else:
        return checkio((b % a, a))

if __name__ == '__main__':
    assert checkio((12, 8)) == 4, "First"
    assert checkio((14, 21)) == 7, "Second"
    print 'All ok'
