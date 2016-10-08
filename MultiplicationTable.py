#!/usr/bin/python
'''
operations of AND, OR, XOR are reduced to either 'unchanged' or 'all ones'
unchanged: 0 with OR, XOR
all ones: 1 with (AND + XOR), OR
'''
def checkio(first, second):
    n = second.bit_length()
    f0, f1 = bin(first).count('0') - 1, bin(first).count('1')
    return 2 * (f0 * second + f1 * (2 ** n - 1))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 6) == 38
    assert checkio(2, 7) == 28
    assert checkio(7, 2) == 18
