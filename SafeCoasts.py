#!/opt/local/bin/python3.3
from collections import deque, defaultdict


def finish_map(regional_map):
    w, h = len(regional_map), len(regional_map[0])
    m = [['.' for x in range(h)] for y in range(w)]
    q = deque([])

    # dilation of coasts
    for i, x in enumerate(regional_map):
        for j, y in enumerate(x):
            if y == 'D':
                q.append((i, j))
            elif y == 'X':
                m[i][j] = 'X'
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        px, py = i + dx, j + dy
                        if (0 <= px < w and 0 <= py < h
                                and regional_map[px][py] == '.'):
                            m[px][py] = 'S'

    # bfs of ships
    visit = defaultdict(bool)
    while q:
        v = q.popleft()
        if visit[v]:
            continue
        visit[v] = True
        x, y = v
        m[x][y] = 'D'
        for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            px, py = x + dx, y + dy
            if 0 <= px < w and 0 <= py < h and m[px][py] == '.':
                q.append((px, py))

    # the rest
    for i, x in enumerate(m):
        for j, y in enumerate(x):
            if y == '.':
                m[i][j] = 'S'

    return [''.join(x) for x in m]


if __name__ == '__main__':
    assert isinstance(finish_map(("D..", "...", "...")), (list, tuple)), "List or tuple"
    assert list(finish_map(("D..XX.....",
                            "...X......",
                            ".......X..",
                            ".......X..",
                            "...X...X..",
                            "...XXXXX..",
                            "X.........",
                            "..X.......",
                            "..........",
                            "D...X....D"))) == ["DDSXXSDDDD",
                                                "DDSXSSSSSD",
                                                "DDSSSSSXSD",
                                                "DDSSSSSXSD",
                                                "DDSXSSSXSD",
                                                "SSSXXXXXSD",
                                                "XSSSSSSSSD",
                                                "SSXSDDDDDD",
                                                "DSSSSSDDDD",
                                                "DDDSXSDDDD"], "Example"
    assert list(finish_map(("........",
                            "........",
                            "X.X..X.X",
                            "........",
                            "...D....",
                            "........",
                            "X.X..X.X",
                            "........",
                            "........",))) == ["SSSSSSSS",
                                               "SSSSSSSS",
                                               "XSXSSXSX",
                                               "SSSSSSSS",
                                               "DDDDDDDD",
                                               "SSSSSSSS",
                                               'XSXSSXSX',
                                               "SSSSSSSS",
                                               "SSSSSSSS"], "Walls"
