#!/usr/bin/python
from random import randint

def checkio(steps):
    if len(steps) < 2:
        return 4, 4

    visit = [(x[0], x[1]) for x in steps]
    state = [(x[0], x[1]) for x in steps if x[2] >= 0]
    temp = int(max(5 - len(state)*1.8, 1))
    state = state[-1]

    def search():
        x, y = state[0] + randint(-temp, temp), state[1] + randint(-temp, temp)
        return min(max(x, 0), 9), min(max(y, 0), 9)

    def candidate():
        x, y = search()
        while (x, y) in visit:
            x, y = search()
        d = 0
        for v in visit:
            d += (x - v[0])**2 + (y - v[1])**2
        return x, y, d

    ret = []
    for i in range(temp):
        ret.append(candidate())
    ret.sort(key=lambda x: x[2])
    ret = ret[-temp/2:]
    return ret[randint(0, len(ret)-1)][:2]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print(checkio([[2, 2, 0]]))  # [0, 2]
    print(checkio([[2, 2, 0], [0, 2, -1]]))  # [3, 2]
    print(checkio([[2, 2, 0], [0, 2, -1], [3, 2, 1]]))  # [4, 1]
    print(checkio([[2, 2, 0], [0, 2, -1], [3, 2, 1], [4, 1, 0]]))  # [3, 1]
