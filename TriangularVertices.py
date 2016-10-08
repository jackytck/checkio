#!/usr/bin/python
def coords(k):
    u = int((-1 + (1 +  8 * (k - 1)) ** 0.5) / 2)
    v = k - u * (u + 1) / 2 - 1
    return (u, v)

def dot(a, b, c, d):
    return 8 * (a * c + b * d) - 4 * (b * c + a * d)

def ang(u, v):
    a, b, c, d = u[0], u[1], v[0], v[1]
    return dot(a, b, c, d) / float(dot(a, b, a, b)) / dot(c, d, c, d)

def minus(u, v):
    return (u[0] - v[0], u[1] - v[1])

def hull(pts):
    ret = []
    d = {}
    for p in pts:
        d[p] = [coords(p), False]

    cur = min(pts)
    d[cur][1] = True
    head = (0, 1)
    ret.append(cur)

    for i in range(len(pts)):
        m = -1
        select = None
        for p in pts:
            if not d[p][1]:
                a = ang(head, minus(d[p][0], d[cur][0]))
                if a > m:
                    m = a
                    select = p
        if select:
            head = minus(d[select][0], d[cur][0])
            d[select][1] = True
            ret.append(select)
            cur = select
    ret.append(min(pts))
    return ret, d

def edge(u, v):
    d = minus(u, v)
    if d[0] == 0 or d[1] == 0 or d[0] == d[1]:
        return True
    return False

def dist(u, v):
    d = minus(u, v)
    if d[0] == d[1]:
        return abs(d[0])
    return abs(d[0] + d[1])

def checkio(inset):
    if len(inset) < 3 or len(inset) == 5:
        return 0
    pts, coos = hull(inset)
    for i in range(len(pts)-1):
        if not edge(coos[pts[i]][0], coos[pts[i+1]][0]):
                return 0
    side = dist(coos[pts[0]][0], coos[pts[1]][0])
    for i in range(len(pts)-1):
        if dist(coos[pts[i]][0], coos[pts[i+1]][0]) != side:
                return 0
    return len(pts) - 1

if __name__ == "__main__":
    assert checkio([1,2,3]) == 3, 'triangle'
    assert checkio([11,13,29,31]) == 0, 'not parallelogram'
    assert checkio([26,11,13,24]) == 4, 'parallelogram'
    assert checkio([4,5,9,13,12,7]) == 6, 'hexagon'
    assert checkio([1,2,3,4,5]) == 0, 'it very strange triangle'
    assert checkio([47]) == 0, 'point'
    assert checkio([11,13,23,25]) == 0, 'again not parallelogram'
