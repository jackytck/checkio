#!/opt/local/bin/python3.3
def shot(wall1, wall2, shot_point, later_point):
    cx, cy = wall1
    dx, dy = wall2
    ax, ay = shot_point
    bx, by = later_point
    det = (bx - ax) * (cy - dy) - (by - ay) * (cx - dx)
    # parallel
    if det == 0:
        det2 = bx*dy - by*dx - ax*dy + ay*dx + ax*by - ay*bx
        # collinear
        if det2 == 0:
            k1 = bx - ax
            k2 = by - ay
            # non-vertical, solve s by dx
            if k1 != 0:
                s = (dx - ax) / float(k1)
                return 0 if s >= 0 else -1
            # vertical, solve s by dy
            else:
                s = (dy - ay) / float(k2)
                return 0 if s >= 0 else -1
        # parallel but not collinear
        else:
            return -1
    # non-parallel
    else:
        s = ((cx - ax) * (cy - dy) + (cy - ay) * (dx - cx)) / float(det)
        t = ((cx - ax) * (ay - by) + (cy - ay) * (bx - ax)) / float(det)
        # hit
        if 0 <= t <= 1 and 0 <= s:
            return round(200 * min(t, 1 - t))
        # miss
        else:
            return -1

if __name__ == '__main__':
    assert shot((2, 2), (5, 7), (11, 2), (8, 3)) == 100, "1st case"
    assert shot((2, 2), (5, 7), (11, 2), (7, 2)) == 0, "2nd case"
    assert shot((2, 2), (5, 7), (11, 2), (8, 4)) == 29, "3th case"
    assert shot((2, 2), (5, 7), (11, 2), (9, 5)) == -1, "4th case"
    assert shot((2, 2), (5, 7), (11, 2), (10.5, 3)) == -1, "4th case again"

    assert shot((0, 0), (1, 1), (3, 3), (2, 2)) == 0, "shot in butt of wall"
    assert shot((0, 0), (1, 1), (2, 2), (3, 3)) == -1, "shot away from butt"
    assert shot((0, 0), (0, 1), (0, 3), (0, 2)) == 0, "shot in butt of butt"
    assert shot((0, 0), (0, 1), (0, 2), (0, 3)) == -1, "shot away from butt"
