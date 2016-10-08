#!/usr/bin/python
import re

def checkio(instring):
    s1, s2 = [], []
    op, prec = '+-*/', {'+': 2, '-': 2, '*': 1, '/': 1}

    clean = ''
    for c in instring:
        if c.isdigit():
            clean += c
        if c in op:
            clean += ' %s ' % c
    clean = reversed(re.findall(r'[\d\+\-\*\/]+', clean))

    def consume():
        a, b, o = s1.pop(), s1.pop(), s2.pop()
        try:
            s1.append(str(eval(b + o + a)))
        except ZeroDivisionError:
            s1.append(0)

    for s in clean:
        if s not in op:
            s1.append(s)
        else:
            while s2 and prec[s] <= prec[s2[-1]]:
                consume()
            s2.append(s)
    while s2:
        consume()
    return int(s1[0])

if __name__ == '__main__':
    assert checkio("2 + 2") == 4, "2+2=4"
    assert checkio("2 * 2") == 4, "2*2=4"
    assert checkio("2 + 2 * 2") == 8, "Yes, it is 8"
    assert checkio("1 - 2 - 3") == 0, "Right to left"
    assert checkio("3 - 2 - 1") == -4, "Again, right to left"
    assert checkio("4 / 8") == 2, "For divide, too"
    assert checkio("2 / 5") == 2, "Don't forget about floor result"
    assert checkio("0 / 10") == 0, "Divide by zero"
    assert checkio("1+1*1+1") == 4, "It is four"
    assert checkio("(3*2)+(4*2)") == 36, "Ignore brackets"
    assert checkio("asd4 + 86() )+( a56d :)") == 146, "Ignore All"
    assert checkio("4 + 8 / 6 * 3 - 33") == 15, "Right to left and operator priority"
    assert checkio("3 - 3 / 10") == 0, "Reduce and zero"
    assert checkio("((2 - 4) - (6 / 8)) + (4 * 6)") == 0, "Complex"
    assert checkio("4 / 2 * 2 + ((3 - 3) / 15)") == 3, "Complex 2"
