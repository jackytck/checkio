#!/opt/local/bin/python3.3
def orient(px, py, qx, qy, rx, ry):
    return qx * ry - qy * rx - (px * ry - py * rx) + px * qy - py * qx


def is_inside(polygon, point):
    # winding number
    wn = 0
    x, y = point
    for (x0, y0), (x1, y1) in zip(polygon, polygon[1:] + (polygon[0],)):
        turning = orient(x0, y0, x1, y1, x, y)
        if (min(x0, x1) <= x <= max(x0, x1)
                and min(y0, y1) <= y <= max(y0, y1) and not turning):
            # on vertex or edge
            return True

        if y0 <= y <= y1 and turning >= 0:
            # upward crossing
            wn += 1

        if y1 <= y <= y0 and turning <= 0:
            # downward crossing
            wn -= 1

    return wn != 0


if __name__ == '__main__':
    assert is_inside(((1,1),(1,3),(2,4),(4,4),(4,3),(2,1)),(3,1)) == False, "Extra 8"
    assert is_inside(((0,0),(1,1),(2,0),(3,1),(4,0),(4,2),(0,2)),(2,1)) == True, "Extra 20"
    assert is_inside(((1, 1), (1, 3), (3, 3), (3, 1)),
                     (2, 2)) == True, "First"
    assert is_inside(((1, 1), (1, 3), (3, 3), (3, 1)),
                     (4, 2)) == False, "Second"
    assert is_inside(((1, 1), (4, 1), (2, 3)),
                     (3, 2)) == True, "Third"
    assert is_inside(((1, 1), (4, 1), (1, 3)),
                     (3, 3)) == False, "Fourth"
    assert is_inside(((2, 1), (4, 1), (5, 3), (3, 4), (1, 3)),
                     (4, 3)) == True, "Fifth"
    assert is_inside(((2, 1), (4, 1), (3, 2), (3, 4), (1, 3)),
                     (4, 3)) == False, "Sixth"
    assert is_inside(((1, 1), (3, 2), (5, 1), (4, 3), (5, 5), (3, 4), (1, 5), (2, 3)),
                     (3, 3)) == True, "Seventh"
    assert is_inside(((1, 1), (1, 5), (5, 5), (5, 4), (2, 4), (2, 2), (5, 2), (5, 1)),
                     (4, 3)) == False, "Eighth"

    assert is_inside(((1, 1), (4, 1), (4, 4), (1, 4)),
                     (2, 4)) == True, "On horizontal edge"
    assert is_inside(((1, 1), (4, 1), (4, 4), (1, 4)),
                     (4, 4)) == True, "On vertex"
    assert is_inside(((1, 1), (4, 1), (4, 4), (1, 4)),
                     (1, 1)) == True, "On vertex"
    assert is_inside(((1, 1), (4, 1), (4, 4), (1, 4)),
                     (4, 2)) == True, "On vertical edge"
    assert is_inside(((1, 1), (4, 4), (1, 4)),
                     (2, 2)) == True, "On tilted edge"
    assert is_inside(((1, 1), (4, 4), (1, 4)),
                     (2, 2.1)) == True, "Slightly inside tilted edge"
    assert is_inside(((1, 1), (4, 4), (1, 4)),
                     (2.1, 2)) == False, "Slightly outside tilted edge"
    assert is_inside(((0,0),(0,2),(2,2),(2,0)),(0,1)) == True, "on left vertical edge"
