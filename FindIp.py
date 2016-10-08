#!/usr/bin/python
def checkio(text):
    """
        find all IPs
    """
    ret = []
    for t in text.split(' '):
        try:
            if len([x for x in t.split('.') if 0 <= int(x) <= 255 and len(x) < 4]) == 4:
                ret.append(t)
        except ValueError:
            pass
    return ret

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"192.168.1.1 and 10.0.0.1 or 127.0.0.1") == \
        ["192.168.1.1", "10.0.0.1", "127.0.0.1"], "All correct"
    assert checkio(u"10.0.0.1.1 but 127.0.0.256 1.1.1.1") == \
        ["1.1.1.1"], "Only 1.1.1.1"
    assert checkio(u"167.11.0.0 1.2.3.255 192,168,1,1") == \
        ["167.11.0.0", "1.2.3.255"], "0 and 255"
    assert checkio(u"267.11.0.0 1.2.3.4/16 192:168:1:1") == \
        [], "I don't see IP"
    print checkio("00250.00001.0000002.1 251.1.2.1")#new test
