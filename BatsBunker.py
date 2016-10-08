#!/usr/bin/python
class PriorityQueue:
    def __init__(self):
        self._q = []

    def put(self, item):
        self._q.append(item)

    def empty(self):
        return len(self._q) == 0

    def get(self):
        if not self.empty():
            self._q.sort(key=lambda x: x[0])
            ret = self._q[0]
            self._q = self._q[1:]
            return ret

def hit_horizontal(a, b):
    hit = []
    (ax, ay), (bx, by) = a, b
    if ax > bx:
        ax, ay, bx, by = bx, by, ax, ay
    r = bx - ax
    for k in range(r):
        s = (0.5 + k) / r
        ex, ey = ax + 0.5 + k, (1 - s) * ay + s * by
        rx, ry = int(round(ex)), int(round(ey))
        hit.append((rx - 1, ry))
        hit.append((rx, ry))
        if ey == ry - 0.5:#corner cases
            hit.append((rx - 1, ry - 1))
            hit.append((rx, ry - 1))
    return hit

def hit_vertical(a, b):
    (ax, ay), (bx, by) = a, b
    return [(y, x) for (x, y) in hit_horizontal((ay, ax), (by, bx))]

def hit_test(a, b):
    return list(set(hit_horizontal(a, b) + hit_vertical(a, b)))

def build_graph(bunker):
    verts, edges, goal = [], [], None
    for i, x in enumerate(bunker):
        for j, y in enumerate(x):
            if y == 'B':
                verts.append((i, j))
            elif y == 'A':
                goal = (i, j)
                verts.append(goal)
    edges = [[] for i in range(len(verts))]
    for i, a in enumerate(verts):
        for j, b in enumerate(verts):
            if j > i:
                valid = True
                for h in hit_test(a, b):
                    if bunker[h[0]][h[1]] == 'W':
                        valid = False
                        break
                if valid:
                    edges[i].append(j)
                    edges[j].append(i)
    return verts, edges, goal

def dist(a, b):
    (ax, ay), (bx, by) = a, b
    return ((ax - bx) ** 2 + (ay - by) ** 2) ** 0.5

def checkio(bunker):
    V, E, goal = build_graph(bunker)
    visit = [False] * len(V)
    pq = PriorityQueue()
    pq.put((0, 0))

    while not pq.empty():
        d, v = pq.get()
        if visit[v]:
            continue
        visit[v] = True
        if V[v] == goal:
            return float('%0.2f' % d)
        for c in E[v]:
            if not visit[c]:
                pq.put((d + dist(V[v], V[c]), c))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        "B--",
        "---",
        "--A"]) == 2.83, "1st example"
    assert checkio([
        "B-B",
        "BW-",
        "-BA"]) == 4, "2nd example"
    assert checkio([
        "BWB--B",
        "-W-WW-",
        "B-BWAB"]) == 12, "3rd example"
    assert checkio([
        "B---B-",
        "-WWW-B",
        "-WA--B",
        "-W-B--",
        "-WWW-B",
        "B-BWB-"]) == 9.24, "4th example"
