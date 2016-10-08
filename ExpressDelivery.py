#!/usr/bin/python
from collections import deque

def checkio(field_map):
    MOVES = (('U', -1, 0), ('D', 1, 0), ('L', 0, -1), ('R', 0, 1))
    width, height = len(field_map), len(field_map[0])

    def neighbors(x, y):
        for s, dx, dy in MOVES:
            a, b = x + dx, y + dy
            if 0 <= a < width and 0 <= b < height and field_map[a][b] != 'W':
                yield s, a, b

    #bfs, each loop represents 1 min
    q = deque([('', True, True, 0, 0)])#(path, loading, wait, x, y)
    visit = {}
    while q:
        p, l, w, x, y = q.popleft()
        if visit.get((x, y, l), False):
            continue
        f = field_map[x][y]
        if f == 'E' and l:
            return p
        if not w:
            visit[(x, y, l)] = True
        if l:
            if w:
                q.append((p, l, False, x, y))
                if f == 'B':
                    q.append((p + 'B', False, False, x, y))
            else:
                for s, a, b in neighbors(x, y):
                    q.append((p + s, l, True, a, b))
        else:
            for s, a, b in neighbors(x, y):
                q.append((p + s, l, False, a, b))
            if f == 'B':
                q.append((p + 'B', True, True, x, y))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    checkio([u"S...", u"....", u"B.WB", u"..WE"])  # RRRDDD
    checkio([u"S...", u"....", u"B..B", u"..WE"])  # DDBRRRBD
