#!/opt/local/bin/python3.3
import itertools
from collections import defaultdict
from heapq import heappush, heappop

DIRS = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}


def get_coords(m):
    ret = []
    for i, x in enumerate(m):
        for j, y in enumerate(x):
            if y == 'F':
                ret = [(i, j)] + ret
            elif y in '1234':
                ret.append((i, j))
    return ret


def per_path(x, y, p):
    ret = []
    for k in p:
        dx, dy = DIRS[k]
        x += dx
        y += dy
        ret.append((x, y))
    return ret


def visited(x, y, paths):
    ret = {(x, y)}
    last = []
    for p in paths:
        ts = per_path(x, y, p)
        last.append(ts[-1])
        for t in ts:
            ret.add(t)
    return last, ret


def next_state(pot):
    for s in itertools.product(*list(pot.values())):
        if (len(set((x, y) for d, x, y in s)) == 4
                and any(k[0] for k in s)):
            yield s


def dist(l1, l2):
    return sum(abs(i - j) for i, j in zip(sum(l1, ()), sum(l2, ())))


def heuristic(sups, state):
    state = [(x, y) for k, x, y in state]
    return min(dist(sups, p) for p in itertools.permutations(state))


def revert(path):
    m = {'N': 'S', 'E': 'W', 'S': 'N', 'W': 'E'}
    return ''.join(m[p] for p in path[::-1])


def supply_routes(the_map):
    w, h = len(the_map), len(the_map[0])
    (fx, fy), *sups = get_coords(the_map)
    q = []
    tried = defaultdict(bool)
    heappush(q, (1, ('N', 'E', 'S', 'W')))
    while q:
        d, ps = heappop(q)
        ha = ','.join(ps)
        if tried[ha]:
            continue
        tried[ha] = True

        curs, v = visited(fx, fy, ps)
        if d == 0:
            ans = [None] * 4
            for i, p in enumerate(ps):
                x, y = curs[i]
                ans[int(the_map[x][y]) - 1] = revert(p)
            return ans

        pot = defaultdict(list)
        for i, (x, y) in enumerate(curs):
            if (x, y) in sups:
                pot[i].append(('', x, y))
            else:
                for k, (dx, dy) in DIRS.items():
                    mx, my = x + dx, y + dy
                    if (0 <= mx < w and 0 <= my < h
                            and (mx, my) not in v
                            and the_map[mx][my] != 'X'):
                        pot[i].append((k, mx, my))

        for s in next_state(pot):
            next_p = []
            for i, (k, x, y) in enumerate(s):
                next_p.append(ps[i] + k)
            cost = heuristic(sups, s)
            heappush(q, (cost, next_p))


if __name__ == '__main__':
    DIRS = {
        "N": (-1, 0),
        "S": (1, 0),
        "W": (0, -1),
        "E": (0, 1),
    }

    def checker(f, the_map):
        result = f(the_map)
        print(result)
        if (not isinstance(result, (tuple, list)) and len(the_map) != 4 and
                any(not isinstance(r, str) for r in the_map)):
            return False, "The result must be a list/tuple of four strings"
        stations = [None] * 4
        factory_supply = [0] * 4
        for i, row in enumerate(the_map):
            for j, ch in enumerate(row):
                if ch in "1234":
                    stations[int(ch) - 1] = (i, j)
        wmap = [list(row) for row in the_map]
        width = len(wmap[0])
        height = len(wmap)
        for numb, route in enumerate(result, 1):
            coor = stations[numb - 1]
            for i, ch in enumerate(route):
                if ch not in DIRS.keys():
                    return False, "Routes must contain only NSWE"
                row, col = coor[0] + DIRS[ch][0], coor[1] + DIRS[ch][1]
                if not (0 <= row < height and 0 <= col < width):
                    return False, "Ooops, we lost the route from station {}".format(numb)
                checked = wmap[row][col]
                if checked == "X":
                    return False, "The route {} was struck {} {}".format(numb, coor, (row, col))
                if checked == "F":
                    factory_supply[numb - 1] = 1
                    if i >= len(route):
                        return False, "A route should be ended in the factory"
                    break
                if checked != ".":
                    return False, "Don't intersect routes"
                wmap[row][col] = str(numb)
                coor = row, col
        if factory_supply != [1, 1, 1, 1]:
            return False, "You should deliver all four resources"
        return True, "Great!"

    test1 = checker(supply_routes, ("..........",
                                    ".1X.......",
                                    ".2X.X.....",
                                    ".XXX......",
                                    ".X..F.....",
                                    ".X........",
                                    ".X..X.....",
                                    ".X..X.....",
                                    "..3.X...4.",
                                    "....X....."))
    print(test1[1])
    assert test1[0], "First test"
    test2 = checker(supply_routes, ("1...2",
                                    ".....",
                                    "..F..",
                                    ".....",
                                    "3...4"))
    print(test2[1])
    assert test2[0], "Second test"
    test3 = checker(supply_routes, ("..2..",
                                    ".....",
                                    "1.F.3",
                                    ".....",
                                    "..4.."))
    print(test3[1])
    assert test3[0], "Third test"

    EXTRA_TESTS = [
    (
        "..........",
        ".F..XXXXX.",
        "..........",
        ".X........",
        ".X........",
        ".X........",
        ".X........",
        ".X......4.",
        ".X.....3X2",
        "........1.",
    ),
    (
        ".X...X4..",
        "X..X.X...",
        "3.XX.XX..",
        "XXXX.XXX.",
        "....F....",
        ".XXX.XXXX",
        "..XX.XX.1",
        "...X.X..X",
        "..2X...X.",
    ),
    (
        ".....",
        "..F..",
        ".....",
        "2.X.4",
        ".1X3.",
    ),
    (
        "2.......",
        "X.XXX.X.",
        ".F..X.X.",
        "..X.X.X.",
        "1.3...X4",
    ),
    (
        ".....4...",
        "....3F...",
        ".........",
        "XXXXXXX..",
        "X.....X..",
        "1........",
        "2..X.....",
    ),
    (
        ".....",
        "...X.",
        "3F..1",
        ".4.2.",
        ".....",
    ),
    (
        "..........",
        "1.......X.",
        "........X.",
        "........X.",
        "........X.",
        "........X.",
        "34.2....X.",
        "X.........",
        "...X...F.X",
        "....X.....",
    )
    ]
    for i, t in enumerate(EXTRA_TESTS):
        t = checker(supply_routes, t)
        print(t[1])
        assert t[0], '%d-th extra test' % i
