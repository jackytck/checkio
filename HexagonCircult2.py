#!/usr/bin/python
import math

def rect(p, r):
    return p * math.cos(r), p * math.sin(r)

def coords(k):
    if k == 1:
        return 0, 0
    t = (3 + (12 * k - 3) ** 0.5) / 6
    n = int(t)
    if n == t:
        n -= 1
    rank = k - 1 - 3 * (n - 1) * n
    s1, r = (rank / n) % 6, rank % n
    if r == 0:
        ang = math.pi / (3 * n) * rank
        return rect(n, ang)
    s2 = (s1 + 1) % 6
    ang1, ang2 = math.pi / 3 * s1, math.pi / 3 * s2
    r1, r2 = r, n - r
    kx1, ky1 = rect(n, ang1)
    kx2, ky2 = rect(n, ang2)
    return (kx1 * r2 + kx2 * r1) / n, (ky1 * r2 + ky2 * r1) / n

def checkio(data):
    "Find the destination"
    a, b = data
    x1, y1 = coords(a)
    x2, y2 = coords(b)
    print x1, y1
    print x2, y2
    return int(round(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5))

if __name__ == '__main__':
    #assert checkio([2, 9]) == 1, "First"
    #assert checkio([9, 2]) == 1, "Reverse First"
    #assert checkio([6, 19]) == 2, "Second, short way"
    #assert checkio([5, 11]) == 3, "Third"
    #assert checkio([13, 15]) == 2, "Fourth, One row"
    #assert checkio([11, 17]) == 4, "Fifrth, One more test"
    #assert checkio([78, 84]) == 3, "New test"
    #print checkio([78, 84])
    print checkio([12, 18])
