#!/usr/bin/python
def orient(p, q, r):
    px, py = p
    qx, qy = q
    rx, ry = r
    return qx*ry - qy*rx - (px*ry - py*rx) + px*qy - py*qx

def checkio(data):
    """list[list[int, int],] -> list[int,]
    Find the convex hull.
    """
    start, min_x, min_y, edge = -1, None, None, {}
    for i, p in enumerate(data):
        for j, q in enumerate(data):
            if i != j:
                found = True
                for k, r in enumerate(data):
                    if r != i and r != j:
                        if orient(p, q, r) > 0:
                            found = False
                            break
                if found:
                    px, py = p
                    if start == -1 or px < min_x or (px == min_x and py < min_y):
                        start = i
                        min_x, min_y = p
                    exist = edge.get(i, None)
                    if exist != None:
                        ex, ey = data[exist]
                        x, y = data[i]
                        jx, jy = data[j]
                        if (jx-x)**2 + (jy-y)**2 < (ex-x)**2 + (ey-y)**2:
                            edge[i] = j
                    else:
                        edge[i] = j
    ret = []
    p = start
    while edge.get(p, 0) != start:
        ret.append(p)
        p = edge[p]
    ret.append(p)
    return ret

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(
        [[7, 6], [8, 4], [7, 2], [3, 2], [1, 6], [1, 8], [4, 9]]
    ) == [4, 5, 6, 0, 1, 2, 3], "First example"
    assert checkio(
        [[3, 8], [1, 6], [6, 2], [7, 6], [5, 5], [8, 4], [6, 8]]
    ) == [1, 0, 6, 3, 5, 2], "Second example"
    print checkio([[1,1],[1,3],[1,4],[5,1],[5,5]])
