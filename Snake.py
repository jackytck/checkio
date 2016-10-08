#!/usr/bin/python
from collections import deque

move = {(0,1): ((0,1),(-1,0),(1,0)), (0,-1): ((0,-1),(1,0),(-1,0)), (-1,0): ((-1,0),(0,-1),(0,1)), (1,0): ((1,0),(0,1),(0,-1))}
symbol = 'FLR'
forrest = None

def setup_forrest(data):
    global forrest
    w, h = len(data), len(data[0])
    forrest = ['.' * h for i in range(w)]
    for i, x in enumerate(data):
        for j, y in enumerate(x):
            if y == 'T':
                forrest[i] = forrest[i][:j] + 'T' + forrest[i][j+1:]

def snake(data):
    d = {}
    for i, x in enumerate(data):
        for j, y in enumerate(x):
            if y.isdigit():
                d[int(y)] = i, j
    return [d[x] for x in sorted(d)]

def cherry(data):
    for i, x in enumerate(data):
        for j, y in enumerate(x):
            if y == 'C':
                return i, j

def move_body(body, x, y):
    return [(x, y)] + body[:-1]

def hash_body(body):
    ret = ''
    for x in body:
        ret += '%d%d' % x
    return ret

def next_move(body):
    ret = []
    global move, symbol, forrest
    w, h = len(forrest), len(forrest[0])
    heading = tuple([i - j for i, j in zip(body[0], body[1])])
    for i, p in enumerate(move[heading]):
        x, y = body[0][0] + p[0], body[0][1] + p[1]
        if 0 <= x < w and 0 <= y < h:
            if (forrest[x][y] == '.' and (x, y) not in body) or (x, y) == body[-1]:
                nex = move_body(body, x, y)
                ret.append((symbol[i], nex))
    return ret

def checkio(data):
    setup_forrest(data)
    body, goal = snake(data), cherry(data)
    q = deque([(body, '')])
    visit = {}
    while q:
        b, seq = q.popleft()
        if b[0] == goal:
            return seq
        h = hash_body(b)
        if visit.get(h, False):
            continue
        visit[h] = True

        for x in next_move(b):
            sym, child = x
            q.append((child, seq + sym))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    TEST_CASES = (
        ('trivial', [".........."] * 9 + ["..43210.C."]),
        ('easy', ["..T...T...", "C.T.......", "..T...TT..", "......T...", "..........", "...TT...T.", "....0T....", "....12T...", "..T..34T..", "....T....."]),
        ('wall', [".........."] * 4 + ["TTTT.TTTTT"] + [".........."] * 4 + [".43210..C."]),
        ('hard', ["......T...", ".C.T..T...", "...T.TT.T.", "..TT..T...", "TT......TT", "...TT.T...", ".T....T..4", "...TTTTTT3", "..T....012", "..T.....TT"]),
        ('evil', ["....T...TT", ".TT.C.T...", "....T...T.", "TTTTTTTTT.", "T.........", "T.TTTTTTT.", "T..4.TT...", "TTT32T..T.", "TT.01T....", "TT...TTTTT"]),
    )
    print checkio(TEST_CASES[0][1])
    print checkio(TEST_CASES[1][1])
    print checkio(TEST_CASES[2][1])
    print checkio(TEST_CASES[3][1])
    print checkio(TEST_CASES[4][1])
