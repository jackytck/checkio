#!/usr/bin/python
from collections import deque

class PriorityQueue:
    def __init__(self):
        self._q = []

    def put(self, item):
        self._q.append(item)

    def empty(self):
        return len(self._q) == 0

    def get(self):
        if not self.empty():
            self._q.sort(key=lambda x: x[1])
            ret = self._q[0]
            self._q = self._q[1:]
            return ret

def nodes(m):
    cc, cnt = {}, -1
    visit = {}
    w, h = len(m), len(m[0])
    for i, x in enumerate(m):
        for j, y in enumerate(x):
            if y == 1 and not visit.get((i, j), False):
                cnt += 1
                q = deque([(i, j)])
                while q:
                    fx, fy = q.popleft()
                    if visit.get((fx, fy), False):
                        continue
                    visit[(fx, fy)] = True
                    if not cc.get(cnt, False):
                        cc[cnt] = []
                    cc[cnt].append((fx, fy))
                    for u in range(-1, 2):
                        for v in range(-1, 2):
                            if (u, v) != (0, 0):
                                s, t = fx + u, fy + v
                                if 0 <= s < w and 0 <= t < h and m[s][t] == 1 and not visit.get((s, t), False):
                                    q.append((s, t))
    return cc, cnt + 1

def hit(m, w, h, dx, dy, x, y):
    if not (0 <= x < w and 0 <= y < h):
        return
    if m[x][y] == 1:
        return x, y, 0
    cost = 0
    if dy != 0:
        while 0 <= y < h:
            if m[x][y] == 1:
                return x, y, cost
            y += dy
            cost += 1
    if dx != 0:
        while 0 <= x < w:
            if m[x][y] == 1:
                return x, y, cost
            x += dx
            cost += 1

def pipe(m, x, y):
    ps = []
    w, h = len(m), len(m[0])
    for i in range(-1, 2):
        ps.append(hit(m, w, h, 0, 1, x+i, y+1))
    for i in range(-1, 2):
        ps.append(hit(m, w, h, 0, -1, x+i, y-1))
    for i in range(-1, 2):
        ps.append(hit(m, w, h, 1, 0, x+1, y+i))
    for i in range(-1, 2):
        ps.append(hit(m, w, h, -1, 0, x-1, y+i))
    return [x for x in ps if x]

def edges(m, cc):
    es = []
    group = {}
    for k, v in cc.items():
        for p in v:
            group[p] = k
    w, h = len(m), len(m[0])
    for i, x in enumerate(m):
        for j, y in enumerate(x):
            if y == 1:
                f = group[(i, j)]
                for p in pipe(m, i, j):
                    t = group[p[:-1]]
                    if f != t:
                        es.append((f, t, p[2]))

    return es

def checkio(stations_map):
    pipes, length = 0, 0
    cc, cnt = nodes(stations_map)
    es = edges(stations_map, cc)
    visit = [False] * cnt
    for i in range(cnt):
        if not visit[i]:
            pq = PriorityQueue()
            pq.put((i, 0))
            while not pq.empty():
                top, cost = pq.get()
                if visit[top]:
                    continue
                visit[top] = True
                if top != i:
                    pipes += 1
                    length += cost
                for e in [x for x in es if x[0] == top]:
                    if not visit[e[1]]:
                        pq.put((e[1], e[2]))
    return [pipes, length]

if __name__ == '__main__':
    assert checkio([
        [1, 0, 0, 0, 1],
        [0, 0, 1, 0, 0],
        [1, 0, 0, 0, 1]
    ]) == [4, 4], 'First'
    assert checkio([
        [1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 0, 1]
    ]) == [0, 0], 'Second'
    assert checkio([
        [1, 0, 0, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1]
    ]) == [3, 5], 'Third'
    assert checkio([
        [1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1]
    ]) == [1, 1], 'Fourth'
    assert checkio([
        [1, 0, 0, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0]
    ]) == [1, 3], 'Fifth'
    assert checkio([
        [1, 0, 0, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 0, 0, 0, 1]
    ]) == [3, 9], 'Sixth'
    assert checkio([
        [1, 0, 0, 0, 1],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [1, 0, 0, 0, 1]
    ]) == [4, 4], 'Seventh'
