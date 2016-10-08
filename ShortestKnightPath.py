#!/usr/bin/python
from collections import deque

def coords(s):
    return 'abcdefgh'.find(s[0]), int(s[1]) - 1

def checkio(move):
    """str -> int
    Number of moves in the shortest path of knight
    """
    start, goal = [coords(x) for x in move.split('-')]
    move = ((1,2), (-1,2), (-1,-2), (1,-2), (-2,1), (-2,-1), (2,-1), (2,1))
    q = deque([(start, 0)])
    visit = {}
    while q:
        f, cnt = q.popleft()
        if f == goal:
            return cnt
        if visit.get(f, False):
            continue
        visit[f] = True
        for m in move:
            x, y = f[0] + m[0], f[1] + m[1]
            if 0 <= x < 8 and 0 <= y < 8 and not visit.get((x, y), False):
                q.append(((x, y), cnt + 1))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert checkio("b1-d5") == 2, "1st example"
    assert checkio("a6-b8") == 1, "2nd example"
    assert checkio("h1-g2") == 4, "3rd example"
    assert checkio("h8-d7") == 3, "4th example"
    assert checkio("a1-h8") == 6, "5th example"
