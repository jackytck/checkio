#!/opt/local/bin/python3.3
def healthy(grid):
    colony, max_lv = (0, 0), 1
    w, h = len(grid), len(grid[0])

    def ring(level, x, y):
        for i in range(level + 1):
            yield from ((x + i, y + level - i), (x + i, y + i - level),
                        (x - i, y + level - i), (x - i, y + i - level))

    def check(z):
        return 0 <= z[0] < w and 0 <= z[1] < h and grid[z[0]][z[1]]

    for x in range(w):
        for y in range(h):
            if grid[x][y]:
                level = 1

                # check pattern
                while all(map(check, ring(level, x, y))):
                    level += 1

                # check if isolated
                if level > max_lv and not any(map(check, ring(level, x, y))):
                    colony = (x, y)
                    max_lv = level
    return colony


if __name__ == '__main__':
    def check(result, answers):
        return list(result) in answers

    assert check(healthy(((0, 1, 0),
                   (1, 1, 1),
                   (0, 1, 0),)), [[1, 1]])
    assert check(healthy(((0, 0, 1, 0, 0),
                   (0, 1, 1, 1, 0),
                   (0, 0, 1, 0, 0),
                   (0, 0, 0, 0, 0),
                   (0, 0, 1, 0, 0),)), [[1, 2]])
    assert check(healthy((
                   (0, 0, 1, 0, 0),
                   (0, 1, 1, 1, 0),
                   (0, 0, 1, 0, 0),
                   (0, 0, 1, 0, 0),
                   (0, 0, 1, 0, 0),)), [[0, 0]])
    assert check(healthy((
                   (0, 0, 0, 0, 0, 0, 1, 0),
                   (0, 0, 1, 0, 0, 1, 1, 1),
                   (0, 1, 1, 1, 0, 0, 1, 0),
                   (1, 1, 1, 1, 1, 0, 0, 0),
                   (0, 1, 1, 1, 0, 0, 1, 0),
                   (0, 0, 1, 0, 0, 1, 1, 1),
                   (0, 0, 0, 0, 0, 0, 1, 0),)), [[3, 2]])
    assert check(healthy(((0, 0, 0, 0, 0, 0, 2, 0),
                   (0, 0, 0, 2, 2, 2, 2, 2),
                   (0, 0, 1, 0, 0, 0, 2, 0),
                   (0, 1, 1, 1, 0, 0, 2, 0),
                   (1, 1, 1, 1, 1, 0, 2, 0),
                   (0, 1, 1, 1, 0, 0, 2, 0),
                   (0, 0, 1, 0, 0, 0, 2, 0),
                   (0, 0, 0, 1, 0, 0, 2, 0),
                   (0, 0, 1, 1, 1, 0, 2, 0),
                   (0, 1, 1, 1, 1, 1, 0, 0),
                   (0, 0, 1, 1, 1, 0, 0, 0),
                   (0, 0, 0, 1, 0, 0, 0, 0),)), [[4, 2], [9, 3]])
