#!/opt/local/bin/python3.3
from collections import deque, defaultdict

DIR = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}
PLAYER = 'P'
UNKNOWN = '?'
EXIT = 'E'
EMPTY = '.'

WORLD = defaultdict(bool)
LAST_POS = None


def get_position(visible, thing=PLAYER, dx=0, dy=0):
    for i, x in enumerate(visible):
        for j, y in enumerate(x):
            if y == thing:
                return i - dx, j - dy
    return None, None


def change_of_coords(visible):
    dx, dy = 0, 0
    if LAST_POS:
        lx, ly = LAST_POS
        px, py = get_position(visible)
        dx, dy = px - lx, py - ly
    return dx, dy


def update_world(visible):
    global WORLD
    dx, dy = change_of_coords(visible)
    for i, x in enumerate(visible):
        for j, y in enumerate(x):
            if y != UNKNOWN:
                WORLD[(i - dx, j - dy)] = y
    return dx, dy


def move_from_to(px, py, ex, ey):
    sequence = ''
    visit = defaultdict(bool)
    q = deque([(px, py, '')])
    while q:
        x, y, seq = q.popleft()
        if x == ex and y == ey:
            return seq, (ex, ey)
        if visit[(x, y)]:
            continue
        visit[(x, y)] = True
        for s, (dx, dy) in DIR.items():
            qx, qy = x + dx, y + dy
            if WORLD[(qx, qy)] in (EMPTY, EXIT, PLAYER):
                q.append((qx, qy, seq + s))


def find_cracks():
    for (x, y), cell in list(WORLD.items()):
        if (WORLD[(x, y)] == EMPTY and
                not all(WORLD[(x + dx, y + dy)] for dx, dy in DIR.values())):
            yield x, y


def find_path(visible):
    # merge all seen into one world
    dx, dy = update_world(visible)
    px, py = get_position(visible, PLAYER, dx, dy)
    ex, ey = get_position(visible, EXIT, dx, dy)
    if ex:
        # move to exit
        return move_from_to(px, py, ex, ey)[0]
    else:
        # move to closest crack
        global LAST_POS
        seq, LAST_POS = min((move_from_to(px, py, cx, cy) for cx, cy in
                             find_cracks()), key=lambda x: len(x[0]))
        return seq


if __name__ == '__main__':
    DIR = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}
    PLAYER = "P"
    WALL = "X"
    UNKNOWN = "?"
    EXIT = "E"
    EMPTY = "."
    MAX_STEP = 250

    def clear_zone(zone):
        return [row for row in zone if not all(el == UNKNOWN for el in row)]

    def get_visible(maze, player):
        grid = [["?" for _ in range(len(row))] for row in maze]
        grid[player[0]][player[1]] = PLAYER
        for direction, diff in DIR.items():
            r, c = player
            while maze[r][c] != WALL:
                r, c = r + diff[0], c + diff[1]
                grid[r][c] = maze[r][c]
                if direction in "NS":
                    grid[r + DIR["W"][0]][c + DIR["W"][1]] = maze[r + DIR["W"][0]][c + DIR["W"][1]]
                    grid[r + DIR["E"][0]][c + DIR["E"][1]] = maze[r + DIR["E"][0]][c + DIR["E"][1]]
                else:
                    grid[r + DIR["S"][0]][c + DIR["S"][1]] = maze[r + DIR["S"][0]][c + DIR["S"][1]]
                    grid[r + DIR["N"][0]][c + DIR["N"][1]] = maze[r + DIR["N"][0]][c + DIR["N"][1]]
        grid = clear_zone(list(zip(*clear_zone(grid))))
        return tuple("".join(trow) for trow in zip(*grid))

    def initial(maze, player):
        return maze, get_visible(maze, player)

    def checker(func, player, maze):
        global WORLD, LAST_POS
        WORLD = defaultdict(bool)
        LAST_POS = None
        step = 0
        while True:
            result = func(get_visible(maze, player))
            if not isinstance(result, str) or any(ch not in DIR.keys() for ch in result):
                print("The function should return a string with directions.")
                return False

            for act in result:
                if step >= MAX_STEP:
                    print("You are tired and your flashlight is off. Bye bye.")
                    return False
                r, c = player[0] + DIR[act][0], player[1] + DIR[act][1]
                if maze[r][c] == WALL:
                    print("BAM! You in the wall at {}, {}.".format(r, c))
                    return False
                elif maze[r][c] == EXIT:
                    print("GRATZ!")
                    return True
                else:
                    player = r, c
                    step += 1

    assert checker(find_path, (1, 1), [
        "XXXXXXX",
        "X.....X",
        "X.X.X.X",
        "X.....X",
        "X.X.X.X",
        "X.X.E.X",
        "XXXXXXX",
    ]), "Simple"
    assert checker(find_path, (1, 4), [
        "XXXXXXXXXX",
        "X....X...X",
        "X.XXXX.X.X",
        "X....X.X.X",
        "X.XXXX.X.X",
        "X.X....X.X",
        "X.XXEX.X.X",
        "X.XXXXXX.X",
        "X........X",
        "XXXXXXXXXX",
    ]), "First"
    assert checker(find_path, (10, 10), [
        "XXXXXXXXXXXX",
        "XX...X.....X",
        "X..X.X.X.X.X",
        "X.XX.X.X.X.X",
        "X..X.X.X.X.X",
        "XX.X.X.X.X.X",
        "X..X.X.X.X.X",
        "X.XX.X.X.X.X",
        "X..X.X.X.X.X",
        "XX.X.X.X.X.X",
        "XE.X.....X.X",
        "XXXXXXXXXXXX",
    ]), "Up down"
    assert checker(find_path, (2, 2), [
            "XXXXXXXXXXXXXXX",
            "XXX...........X",
            "X...XXXXXXXXX.X",
            "X.X.X.......X.X",
            "X.X.X.X.X.X.X.X",
            "X.X.X.X.X.X.X.X",
            "X.....XXXXX...X",
            "X.X.X.......X.X",
            "X.X.XXXX.X.XX.X",
            "X.X.X..X.X.X..X",
            "X...XX.X.XXXX.X",
            "X.X..X.X....X.X",
            "X.XXXX.XXXXXX.X",
            "X........XE...X",
            "XXXXXXXXXXXXXXX",
    ]), "Big"
