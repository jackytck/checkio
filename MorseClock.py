#!/usr/bin/python
def checkio(data):
    ret = []
    for i, d in enumerate(data.split(':')):
        r, d = '', int(d)
        f, s = d / 10, d % 10
        if i == 0:
            r += '{0:02b} '.format(f)
        else:
            r += '{0:03b} '.format(f)
        r += '{0:04b}'.format(s)
        ret.append(r)
    ret = ' : '.join(ret)
    return ret.replace('0', '.').replace('1', '-')

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':    
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("11:10:12") == ".- ...- : ..- .... : ..- ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"
