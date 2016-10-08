#!/opt/local/bin/python3.3

DIR = {(0, 1): ((-1, 0), (0, 1), (1, 0)),
       (0, -1): ((1, 0), (0, -1), (-1, 0)),
       (1, 0): ((0, 1), (1, 0), (0, -1)),
       (-1, 0): ((0, -1), (-1, 0), (0, 1))}


def lanterns_flow(river_map, minutes):
    river = [list(x) for x in river_map]
    river.append('@' * len(river[0]))
    stack = [(0, j, (1, 0), 0) for j, x in enumerate(river[0]) if x == '.']
    while stack:
        i, j, d, t = stack.pop()
        river[i][j] = t
        for dx, dy in DIR[d]:
            px, py = i + dx, j + dy
            mark = river[px][py]
            if mark == '.':
                stack.append((px, py, (dx, dy), t + 1))
                break
            elif mark == '@':
                break

    lantern = [(i, j) for i, x in enumerate(river)
               for j, y in enumerate(x) if y == minutes]
    light = set()
    for x, y in lantern:
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                px, py = x + dx, y + dy
                if px >= 0 and river_map[px][py] == '.':
                    light.add((px, py))
    return len(light)


if __name__ == '__main__':
    assert lanterns_flow(("X....XXX",
                          "X....XXX",
                          "X....XXX",
                          "X....XXX",
                          "X....XXX",
                          "X......X",
                          "X......X",
                          "X......X",
                          "X......X",
                          "XXX....X"), 0) == 8, "Start"
    assert lanterns_flow(("X....XXX",
                          "X....XXX",
                          "X....XXX",
                          "X....XXX",
                          "X....XXX",
                          "X......X",
                          "X......X",
                          "X......X",
                          "X......X",
                          "XXX....X"), 7) == 18, "7th minute"
    assert lanterns_flow(("X....XXX",
                          "X....XXX",
                          "X....XXX",
                          "X....XXX",
                          "X....XXX",
                          "X......X",
                          "X......X",
                          "X......X",
                          "X......X",
                          "XXX....X"), 9) == 17, "9th minute"
