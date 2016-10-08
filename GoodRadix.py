#!/usr/bin/python
def checkio(number):
    m = max(number)
    if not m.isdigit():
        m = ord(m) - ord('A') + 10
    for i in range(int(m)+1, 37):
        if int(number, i) % (i - 1) == 0:
            return i
    return 0

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"18") == 10, "Simple decimal"
    assert checkio(u"1010101011") == 2, "Any number is divisible by 1"
    assert checkio(u"222") == 3, "3rd test"
    assert checkio(u"A23B") == 14, "It's not a hex"
    print('Local tests done')
