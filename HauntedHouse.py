#!/usr/bin/python
from collections import deque

Outer = ('W', 'N', 'N', 'EN', 'W', '', '', 'E', 'W', '', '', 'E', 'WS', 'S', 'S', 'ES')
Dir = {'N': -4, 'E': 1, 'S': 4, 'W': -1}

def dist(p1, p2):
    x1, y1 = (p1 - 1) / 4, (p1 - 1) % 4
    x2, y2 = (p2 - 1) / 4, (p2 - 1) % 4
    return (x1 - x2) ** 2 + (y1 - y2) ** 2

def checkio(house, stephan, ghost):

    def next_step(pos):
        walls = house[pos - 1] + Outer[pos - 1]
        return [(x, pos + Dir[x]) for x in 'NESW' if x not in walls]

    Q = deque([(stephan, ghost, '')])
    path, visit, avoid = 'N', {}, [x[1] for x in next_step(ghost)]
    while Q:
        p, g, seq = Q.popleft()
        if p == 1:
            if seq:
                path = seq
            break
        if visit.get((p, g), False):
            continue
        visit[(p, g)] = True
        avoid = [x[1] for x in next_step(g)]
        for s in next_step(p):
            if s[1] in avoid:
                continue
            avoid.sort(key=lambda x: dist(s[1], x))
            Q.append((s[1], avoid[0], seq + s[0]))

    return path[0]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    checkio(
        ["", "S", "S", "",
         "E", "NW", "NS", "",
         "E", "WS", "NS", "",
         "", "N", "N", ""],
        16, 1)
    checkio(
        ["", "", "", "",
         "E", "ESW", "ESW", "W",
         "E", "ENW", "ENW", "W",
         "", "", "", ""],
        11, 6)
