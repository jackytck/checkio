#!/usr/bin/python
from collections import deque

def swap(s, i, j):
    s = list(s)
    s[i], s[j] = s[j], s[i]
    return ''.join(s)

def move(f, c):
    p = f.find('0')
    if c == 'U' and p >= 3:
        return swap(f, p, p-3)
    elif c == 'D' and p <= 5:
        return swap(f, p, p+3)
    elif c == 'L' and p%3 != 0:
        return swap(f, p, p-1)
    elif c == 'R' and (p+1)%3 != 0:
        return swap(f, p, p+1)
    return f

def is_done(f):
    return f == '123456780'

def checkio(puzzle):
    flat = ''.join(str(x) for x in sum(puzzle, []))
    Q = deque([(flat, '')])
    visit = {}
    while Q:
        state, seq = Q.popleft()
        if is_done(state):
            return seq
        if visit.get(state, False):
            continue
        visit[state] = True
        for m in 'UDLR':
            Q.append((move(state, m), seq + m))

if __name__ == '__main__':
    print(checkio([[1, 2, 3],
                   [4, 6, 8],
                   [7, 5, 0]]))
