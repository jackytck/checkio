#!/usr/bin/python
probes = []

def checkio(data):
    global probes
    if not data:
        for i in range(10):
            for j in range(10):
                probes.append((i, j))
        return [4, 4]
    cx, cy, r = data[-1]
    update = []
    for c in probes:
        if int(round(((c[0] - cx)**2 + (c[1] - cy)**2) ** .5)) == r:
            update.append(c)

    probes = update
    return probes[-1]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print(checkio([]))
    print(checkio([[5, 3, 4]]))
    print(checkio([[5, 3, 4], [2, 9, 3]]))
