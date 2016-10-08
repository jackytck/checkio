#!/usr/bin/python
from random import randint

def checkio(field):
    w, h = 10, 10

    def neighbors(x, y):
        ret = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                a, b = x + i, y + j
                if 0 <= a < w and 0 <= b < h and (a, b) != (x, y):
                    ret.append((a, b))
        return ret

    def mine_cnt(x, y):
        ret = 0
        for n in neighbors(x, y):
            if field[n[0]][n[1]] == 9:
                ret += 1
        return ret

    def uncover(x, y):
        ret = []
        for n in neighbors(x, y):
            c = field[n[0]][n[1]]
            if c == -1:
                ret.append(n)
        return ret

    rand = []
    for i in range(w):
        for j in range(h):
            state = field[i][j]
            if state in range(9):
                diff = state - mine_cnt(i, j)
                un = uncover(i, j)
                if diff == 0 and un:
                    return False, un[0][0], un[0][1]
                if diff == len(un) and diff:
                    return True, un[0][0], un[0][1]
            elif state == -1:
                rand.append((i, j))

    guess = randint(0, len(rand) - 1)
    return [False, rand[guess][0], rand[guess][1]]

if __name__ == '__main__':
    #These are just examples
    print checkio([
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        ])  # [False, 0, 0]
    print checkio([
        [0, 2, -1, -1, -1, -1, -1, -1, -1, -1],
        [0, 2, -1, -1, -1, -1, -1, -1, -1, -1],
        [0, 1, 1, 1, -1, -1, -1, -1, -1, -1],
        [0, 0, 0, 1, -1, -1, -1, -1, -1, -1],
        [0, 1, 1, 2, -1, -1, -1, -1, -1, -1],
        [0, 1, -1, -1, -1, -1, -1, -1, -1, -1],
        [0, 1, -1, -1, -1, -1, -1, -1, -1, -1],
        [2, 1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        ])  # [True, 0, 2]
