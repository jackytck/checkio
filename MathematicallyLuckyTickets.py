#!/usr/bin/python
def arth(a, b):
    yield a + b
    yield a - b
    yield a * b
    if b != 0:
        yield a / float(b)

def exhaust(num):
    yield int(num)
    for i in range(1, len(num)):
        a, b = exhaust(num[:i]), exhaust(num[i:])
        for x in a:
            for y in b:
                for r in arth(x, y):
                    yield r
            b = exhaust(num[i:])

def checkio(data):
    for x in exhaust(data):
        if x == 100:
            return False
    return True

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio('000000') == True, "All zeros"
    assert checkio('707409') == True, "You can not transform it to 100"
    assert checkio('595347') == False, "(5 + ((9 / (3 / 34)) - 7)) = 100"
    assert checkio('271353') == False, "(2 - (7 * (((1 / 3) - 5) * 3))) = 100"
