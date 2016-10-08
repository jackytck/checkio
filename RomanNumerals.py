#!/usr/bin/python
def checkio(number):
    'return roman numeral using the specified integer value from range 1...3999'
    roman = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    num = '%04d' % number
    ret = ''
    for i, n in enumerate(num):
        n = int(n)
        base = 10 ** (3 - i)
        if n < 4:
            ret += roman[base] * n
        elif n == 4:
            ret += roman[base] + roman[base * 5]
        elif n < 9:
            ret += roman[base * 5] + roman[base] * (n - 5)
        else:
            ret += roman[base] + roman[base * 10]
    return ret
    
if __name__ == '__main__':
    assert checkio(6) == 'VI', 'First'
    assert checkio(76) == 'LXXVI', 'Second'
    assert checkio(499) == 'CDXCIX', 'Third'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', 'Fourth'
    print 'All ok'
