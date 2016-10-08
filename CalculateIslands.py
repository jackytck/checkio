#!/usr/bin/python
from collections import deque

def checkio(data):
    ret = []
    w, h = len(data), len(data[0])
    visit = {}
    for i, x in enumerate(data):
        for j, y in enumerate(data[i]):
            if not visit.get((i, j), False):
                if y == 1:
                    cnt = 0
                    q = deque([(i, j)])
                    while q:
                        f = q.popleft()
                        if visit.get(f, False):
                            continue
                        cnt += 1
                        visit[f] = True

                        for u in range(-1, 2):
                            for v in range(-1, 2):
                                s, t = f[0] + u, f[1] + v
                                if 0 <= s < w and 0 <= t < h and not visit.get((s, t), False) and data[s][t] == 1:
                                    q.append((s, t))
                    ret.append(cnt)
                else:
                    visit[(i, j)] = True
    return sorted(ret)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0]]) == [1, 3], "1st example"
    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 1, 0, 0]]) == [5], "2nd example"
    assert checkio([[0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 1, 1, 1],
                    [1, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0]]) == [2, 3, 3, 4], "3rd example"
