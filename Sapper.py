#!/usr/bin/python
def checkio(open_map):
    w, h = len(open_map), len(open_map[0])

    def neighbors(x, y):
        ret = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                a, b = x + i, y + j
                if 0 <= a < w and 0 <= b < h and (a, b) != (x, y):
                    ret.append((a, b))
        return ret

    def mineCnt(x, y):
        ret = 0
        for n in neighbors(x, y):
            if open_map[n[0]][n[1]] == 'M':
                ret += 1
        return ret

    def unopen(x, y):
        ret = []
        for n in neighbors(x, y):
            c = open_map[n[0]][n[1]]
            if not c and c != 0:
                ret.append(n)
        return ret

    for i in range(w):
        for j in range(h):
            state = open_map[i][j]
            if state in range(9):
                diff = state - mineCnt(i, j)
                un = unopen(i, j)
                if diff == 0 and un:
                    return False, un[0][0], un[0][1]
                if diff == len(un) and diff:
                    return True, un[0][0], un[0][1]
