#!/usr/bin/python
def addDot(d):
    ret = []
    i = 2
    s = d[-3:]
    while s:
        ret.append(s)
        s = d[-3 * i: -3 * (i-1)]
        if not s:
            break
        i += 1
    return '.'.join(reversed(ret))

def checkio(txt):
    '''
    string with dot separated numbers, which inserted after every third digit from right to left
    '''
    ret = []
    tokens = txt.split(' ')
    for t in tokens:
        if t.isdigit():
            t = addDot(t)
        ret.append(t)
    return ' '.join(ret)

if __name__ == '__main__':
    assert checkio('123456') == '123.456'
    assert checkio('333') == '333'
    assert checkio('9999999') == '9.999.999'
    assert checkio('123456 567890') == '123.456 567.890'
    assert checkio('price is 5799') == 'price is 5.799'
    assert checkio('he was born in 1966th') == 'he was born in 1966th'
    print 'All ok'
