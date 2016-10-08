#!/usr/bin/python
def checkio(data):
    'Return True if password strong and False if not'
    s = True if len(data) >= 10 else False
    d, u, l = False, False, False
    for c in data:
        if c.isdigit():
            d = True
        else:
            if c.isupper():
                u = True
            else:
                l = True
    return s and d and u and l

if __name__ == '__main__':
    assert checkio('A1213pokl')==False, 'First'
    assert checkio('bAse730onE4')==True, 'Second'
    assert checkio('asasasasasasasaas')==False, 'Third'
    assert checkio('QWERTYqwerty')==False, 'Fourth'
    assert checkio('123456123456')==False, 'Fifth'
    assert checkio('QwErTy911poqqqq')==True, 'Sixth'
    print 'All ok'
