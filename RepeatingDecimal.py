#!/usr/bin/python
def checkio(fraction):
    nu, de = fraction
    q, r = nu / de, nu % de
    if r == 0:
        return str(q)

    digit, visit = '', {}
    while not visit.get(r, (False, 0))[0]:
        visit[r] = True, len(digit)
        r *= 10
        d, r = r / de, r % de
        digit += str(d)
        if r == 0:
            return '%d.%s' % (q, digit)

    b = visit[r][1]
    return '%d.%s' % (q, digit[:b] + '(' + digit[b:] + ')')

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([1, 3]) == "0.(3)", "1/3 Classic"
    assert checkio([5, 3]) == "1.(6)", "5/3 The same, but bigger"
    assert checkio([3, 8]) == "0.375", "3/8 without repeating part"
    assert checkio([7, 11]) == "0.(63)", "7/11 prime/prime"
    assert checkio([29, 12]) == "2.41(6)", "29/12 not and repeating part"
    assert checkio([11, 7]) == "1.(571428)", "11/7 six digits"
