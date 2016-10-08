#!/opt/local/bin/python3.3
from collections import Counter


def convert(numerator, denominator):
    q, r = divmod(numerator, denominator)
    if r == 0:
        return '%d.' % q

    digit, visit = '', Counter()
    while not visit[r]:
        visit[r] = len(digit) + 1
        r *= 10
        d, r = divmod(r, denominator)
        digit += str(d)
        if r == 0:
            return '%d.%s' % (q, digit)

    b = visit[r] - 1
    return '%d.%s' % (q, digit[:b] + '(' + digit[b:] + ')')

if __name__ == '__main__':
    assert convert(1, 3) == "0.(3)", "1/3 Classic"
    assert convert(5, 3) == "1.(6)", "5/3 The same, but bigger"
    assert convert(3, 8) == "0.375", "3/8 without repeating part"
    assert convert(7, 11) == "0.(63)", "7/11 prime/prime"
    assert convert(29, 12) == "2.41(6)", "29/12 not and repeating part"
    assert convert(11, 7) == "1.(571428)", "11/7 six digits"
    assert convert(0, 117) == "0.", "Zero"
