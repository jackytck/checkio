#!/usr/bin/python
def factor(data, x):
    ret = []
    for r in data[1:]:
        l = []
        for i, e in enumerate(r):
            if i != x:
                l.append(e)
        ret.append(l)
    return ret

def checkio(data):
    if len(data) == 1:
        return data[0][0]
    if len(data) == 2:
        return data[0][0]*data[1][1] - data[0][1]*data[1][0]
    ret = 0
    for i, x in enumerate(data[0]):
        ret += (-1)**i * x * checkio(factor(data, i))
    return ret

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[4,3], [6,3]]) == -6, 'First example'

    assert checkio([[1, 3, 2],
                    [1, 1, 4],
                    [2, 2, 1]]) == 14, 'Second example'
