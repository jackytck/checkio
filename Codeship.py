#!/opt/local/bin/python3.3
from collections import deque, defaultdict
import random

SHIP = 'S'
TORNADO = 'O'
ICEBERG = 'X'


def move_ship(sea_map, fuel):
    w, h = len(sea_map), len(sea_map[0])
    sx, sy = 0, 0

    # find minimum steps from each tornado to each cell
    step_map = [[0 for y in range(h)] for x in range(w)]
    for i, _ in enumerate(sea_map):
        for j, cell in enumerate(_):
            if cell == TORNADO:
                visit = defaultdict(bool)
                q = deque([(i, j, 0)])
                while q:
                    x, y, s = q.popleft()
                    if visit[(x, y)]:
                        continue
                    old = step_map[x][y]
                    if old:
                        step_map[x][y] = min(old, s)
                    elif sea_map[x][y] != TORNADO:
                        step_map[x][y] = s
                    visit[(x, y)] = True
                    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        px, py = x + dx, y + dy
                        if (0 <= px < w and 0 <= py < h and
                                sea_map[px][py] != ICEBERG):
                            q.append((px, py, s + 1))
            elif cell == SHIP:
                sx, sy = i, j

    # find guaranteed shortest ship path to goal
    visit = defaultdict(bool)
    q = deque([(sx, sy, 0, sx, sy)])
    prev = {}
    success = False
    while q:
        x, y, s, px, py = q.popleft()
        if x == w - 1 and y == h - 1:
            prev[(x, y)] = (px, py)
            success = True
            break
        if visit[(x, y)]:
            continue
        prev[(x, y)] = (px, py)
        visit[(x, y)] = True
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            i, j = x + dx, y + dy
            if (0 <= i < w and 0 <= j < h and
                    sea_map[i][j] != ICEBERG and
                    s < step_map[i][j] - 1):
                q.append((i, j, s + 1, x, y))

    # if no solution, find closest node
    gx, gy, dist = w - 1, h - 1, 0
    if not success:
        visit = defaultdict(bool)
        q = deque([(gx, gy, 0)])
        while q:
            x, y, s = q.popleft()
            if (x, y) in prev.keys():
                gx, gy, dist = x, y, s
                break
            visit[(x, y)] = True
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                i, j = x + dx, y + dy
                if 0 <= i < w and 0 <= j < h and sea_map[i][j] != ICEBERG:
                    q.append((i, j, s + 1))

    # if too far from goal, just random walk
    dirs = {(-1, 0): 'N', (1, 0): 'S', (0, -1): 'W', (0, 1): 'E'}
    if dist > 3:
        ds = list(dirs.keys())
        random.shuffle(ds)
        for dx, dy in ds:
            i, j = sx + dx, sy + dy
            if 0 <= i < w and 0 <= j < h and step_map[i][j] > 1:
                return dirs[(dx, dy)]
        return '.'

    move = '.'
    while (gx, gy) != (sx, sy):
        px, py = prev[(gx, gy)]
        dx, dy = gx - px, gy - py
        move = dirs[(dx, dy)]
        gx, gy = px, py

    return move

if __name__ == '__main__':
    import random

    SHIP = 'S'
    TORNADO = 'O'
    ICEBERG = 'X'
    EMPTY = '.'

    HUNT_DISTANCE = 2

    DIRS = {
        'N': (-1, 0),
        'S': (1, 0),
        'W': (0, -1),
        'E': (0, 1),
        '.': (0, 0)
    }

    def prepare_map(grid, ship, tornadoes):
        grid = list(list(row) for row in grid)
        grid[ship[0]][ship[1]] = SHIP
        for t in tornadoes:
            grid[t[0]][t[1]] = TORNADO
        return tuple("".join(row) for row in grid)

    def check_solution(func, sea, fuel, tornadoes):
        ship = (0, 0)
        for step in range(fuel):
            user_result = func(prepare_map(sea, ship, tornadoes), fuel - step)
            if not isinstance(user_result, str) or user_result not in DIRS.keys():
                print("You should return a string with an action.")
                return False
            sx, sy = ship
            sea_width = len(sea[0])
            sea_height = len(sea)
            new_sx, new_sy = sx + DIRS[user_result][0], sy + DIRS[user_result][1]
            ship = new_sx, new_sy
            if new_sx < 0 or new_sx >= len(sea) or new_sy < 0 or new_sy >= len(sea[0]):
                print("Captain, we lost.")
                return False
            if (new_sx, new_sy) in tornadoes:
                print("Dont move in a tornado! SOS")
                return False
            if sea[new_sx][new_sy] == ICEBERG:
                print("ICEBERG! Turn to ... SOS")
                return False

            if (new_sx, new_sy) == (sea_height - 1, sea_width - 1):
                print("WIN!")
                print(fuel - step)
                return True

            # Aaaaand tornado move
            for i in range(len(tornadoes)):
                tx, ty = tornadoes[i]
                possible = []
                for direction, (dx, dy) in DIRS.items():
                    x, y = tx + dx, ty + dy
                    if 0 <= x < sea_height and 0 <= y < sea_width and sea[x][y] != ICEBERG and (x, y) not in tornadoes:
                        possible.append((direction, (x, y)))
                distance = abs(sx - tx) + abs(sy - ty)
                if distance <= HUNT_DISTANCE:
                    best = float("inf"), (tx, ty), "."
                    for d, (x, y) in possible:
                        possible_distance = abs(sx - x) + abs(sy - y)
                        if possible_distance < best[0]:
                            best = possible_distance, (x, y), d
                        elif possible_distance == best[0]:
                            best = random.choice([(possible_distance, (x, y), d), best])
                    tornadoes[i] = best[1]
                else:
                    rand = random.choice(possible)
                    tornadoes[i] = rand[1]
            if ship in tornadoes:
                print("Tornado caught us, Cap.")
                return False
        print("We don't have fuel.")
        return False

    assert check_solution(move_ship, (
        ".....",
        ".XXX.",
        "...X.",
        ".XXX.",
        ".....",), 100, [(2, 2)]), "First"

    assert check_solution(move_ship, ("S........",".X.X.X.X.","......O..",".X.X.X.X.","....O....",".X.X.X.X.","..O......",".X.X.X.X.","........."), 100, [(6, 2), (4, 4), (6, 2)]), 'second'
