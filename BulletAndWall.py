#!/usr/bin/python
def checkio(data):
    cx, cy = data[0]
    dx, dy = data[1]
    ax, ay = data[2]
    bx, by = data[3]
    det = (bx - ax) * (cy - dy) - (by - ay) * (cx - dx)
    if det == 0:
        det2 = bx*dy - by*dx - ax*dy + ay*dx + ax*by - ay*bx
        if det2 == 0:
            k1 = bx - ax
            k2 = by - ay
            if k1 != 0:
                s = (dx - ax) / float(k1)
                return True if s >= 0 else False
            else:
                s = (dy - ay) / float(k2)
                return True if s >= 0 else False
        else:
            return False
    s = ((cx - ax) * (cy - dy) + (cy - ay) * (dx - cx)) / float(det)
    t = ((cx - ax) * (ay - by) + (cy - ay) * (bx - ax)) / float(det)
    return True if (t >= 0 and t <= 1 and s >= 0) else False

if __name__ == '__main__':
    assert checkio([[0,0], [0,2], [5,1], [3,1]]) == True, "First"
    assert checkio([[0, 0], [0, 2], [3, 1], [5, 1]]) == False, "Reverse First"
    assert checkio([[0, 0], [2, 2], [6, 0], [3, 1]]) == True, "Second"
    assert checkio([[6, 0], [5, 5], [4, 0], [5, 6]]) == False, "Third"
    assert checkio([[0, 0], [1, 1], [3, 3], [2, 2]]) == True, "Fourth, shot in butt of wall :)"
    assert checkio([[0, 0], [1, 1], [3, 2], [2, 1]]) == False, "Fifth, parallel"
    assert checkio([[2, 4], [2, 0], [0, 2], [2, 3]]) == True, "Sixth, Vertical wall"
