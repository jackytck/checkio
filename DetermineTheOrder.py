#!/usr/bin/python
def minimum(data):
    ms = list(set([x[0] for x in data]))
    check = []
    for m in ms:
        ok = True
        for d in data:
            if d.find(m) > 0:
                ok = False
                break
        if ok:
            check.append(m)
    return min(check)

def remove(data, c):
    data = [x.replace(c, '') for x in data]
    return [x for x in data if x != '']

def checkio(data):
    ans = ''
    while data:
        m = minimum(data)
        ans += m
        data = remove(data, m)
    return ans

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(["acb", "bd", "zwa"]) == "zwacbd", \
        "Just concatenate it"
    assert checkio(["klm", "kadl", "lsm"]) == "kadlsm", \
        "Paste in"
    assert checkio(["a", "b", "c"]) == "abc", \
        "Cant determine the order - use english alphabet"
    assert checkio(["aazzss"]) == "azs", \
        "Each symbol only once"
    assert checkio(["dfg", "frt", "tyg"]) == "dfrtyg", \
        "Concatenate and paste in"
