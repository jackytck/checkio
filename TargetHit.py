#!/usr/bin/python
from math import pi, atan2

error = 1.0e-7

def orient(p, q, r):
    px, py = p
    qx, qy = q
    rx, ry = r
    return qx*ry - qy*rx - (px*ry - py*rx) + px*qy - py*qx

def norm(p, q):
    px, py = p
    qx, qy = q
    return ((px - qx)**2 + (py - qy)**2) ** 0.5

def dot(p, q, r):
    a = [p[0] - q[0], p[1] - q[1]]
    b = [r[0] - q[0], r[1] - q[1]]
    return sum([x*y for x, y in zip(a, b)])

def sin(p, q, r):
    return orient(q, p, r) / norm(p, q) / norm(r, q)

def cos(p, q, r):
    return dot(p, q, r) / norm(p, q) / norm(r, q)

def ang(p, q, r):
    return atan2(sin(p, q, r), cos(p, q, r))

def checkio(data):
    verts, q = data
    wn = 0
    for i in range(-1, len(verts)-1):
        p, r = verts[i], verts[i+1]
        try:
            a = ang(p, q, r)
            if abs(a - pi) < error:#on edge
                return True
            wn += a
        except ZeroDivisionError:#on vertex
            return True

    if abs(wn) < error:
        return False
    return True

if __name__ == '__main__':
    assert checkio([[[1,1],[1,3],[3,3],[3,1]], [2,2]]) == True, "First"
    assert checkio([[[1,1],[1,3],[3,3],[3,1]], [4,2]]) == False, "Second"
    assert checkio([[[1,1],[4,1],[2,3]], [3,2]]) == True, "Third"
    assert checkio([[[1,1],[4,1],[1,3]], [3,3]]) == False, "Fourth"
    assert checkio([[[2,1],[4,1],[5,3],[3,4],[1,3]], [4,3]]) == True, "Fifth"
    assert checkio([[[2,1],[4,1],[3,2],[3,4],[1,3]], [4,3]]) == False, "Sixth"
    assert checkio([[[1,1],[3,2],[5,1],[4,3],[5,5],[3,4],[1,5],[2,3]], [3,3]]) == True, "Seventh"
    assert checkio([[[1,1],[1,5],[5,5],[5,4],[2,4],[2,2],[5,2],[5,1]], [4,3]]) == False, "Eighth"
