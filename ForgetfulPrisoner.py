#!/opt/local/bin/python3.3
from random import shuffle
from collections import defaultdict

DIR = {'W': (0, -1), 'N': (-1, 0), 'E': (0, 1), 'S': (1, 0)}
DIR2 = 'WNES'
DIR3 = {'W': 'E', 'N': 'S', 'E': 'W', 'S': 'N'}


def save(back, vecs, move, junction):
    memory = format(back, '05b')

    if not back:
        # merge with previous vector if not a junction
        if not junction and vecs and vecs[-1][0] == move and vecs[-1][1] < 7:
            vecs[-1][1] += 1
        else:
            vecs.append((move, 1))

    # only keep most recent 19 vectors
    for d, s in vecs[-19:]:
        memory += format(DIR2.index(d), '02b') + format(s, '03b')

    # fill '0' for unused storage
    memory = memory.ljust(100, '0')

    return int(memory, 2)


def load(memory):
    bits = format(memory, '0100b')

    # first 5 bits: number of vectors to backtrack
    back = int(bits[:5], 2)

    # next 95 bits: 19 5-bits vectors
    vecs = [bits[i:i+5] for i in range(5, 100, 5)]

    # each vector: 2-bits direction, 3-bits length
    vecs = [[DIR2[int(v[:2], 2)], int(v[2:], 2)] for v in vecs
            if int(v[2:], 2)]

    # visited table
    visited = defaultdict(bool)
    x, y, bx, by = 0, 0, 0, 0
    visited[(x, y)] = True
    for i, (d, s) in enumerate(reversed(vecs)):
        dx, dy = DIR[d]
        for _ in range(s):
            x -= dx
            y -= dy
            visited[(x, y)] = True

        if i + 1 == back:
            # backtracked coords
            bx, by = x, y

    return back, vecs, visited, bx, by


def backtrack(back, vecs):
    v = vecs[-1 - back]
    return back + 1, DIR3[v[0]] * v[1]


def find_path(scanner, memory):
    back, vecs, visited, bx, by = load(memory)
    move, junction = '', False

    if back:
        tried = vecs[-back][0]
        for d in DIR2:
            x, y = bx + DIR[d][0], by + DIR[d][1]
            if (scanner[d] and not visited[(x, y)] and
                    DIR2.index(d) > DIR2.index(tried)):
                # found new way, stop backtracking, reset states
                vecs = vecs[:-back]
                back = 0
                junction = True
                move = d
                break
        if not move:
            if back == len(vecs):
                # memory exhaustion, old junction is lost, restart
                vecs = []
                back = 0
                for d in DIR2:
                    if scanner[d]:
                        move = d
                        break
            else:
                # continue backtracking, search for old junction
                back, move = backtrack(back, vecs)
    else:
        dirs = [d for d in DIR2]
        shuffle(dirs)
        for d in dirs:
            if scanner[d] and not visited[DIR[d]]:
                # explore unvisited, save new junction
                if not move:
                    move = d
                else:
                    junction = True
                    break
        if not move:
            # dead end, go back
            back, move = backtrack(back, vecs)

    memory = save(back, vecs, move, junction)
    return move, memory


if __name__ == '__main__':
    DIR = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}
    WALL = "X"
    EXIT = "E"
    EMPTY = "."
    MAX_STEP = 300

    def get_visible(maze, player):
        result = {}
        for direction, (dr, dc) in DIR.items():
            cr, cc = player
            distance = -1
            while maze[cr][cc] != WALL:
                cr += dr
                cc += dc
                distance += 1
            result[direction] = distance
        return result

    def checker(func, player, maze):
        step = 0
        memory = 0
        while True:
            result, memory = func(get_visible(maze, player), memory)
            if not isinstance(result, str) or any(ch not in DIR.keys() for ch in result):
                print("The function should return a string with directions.")
                return False
            if not isinstance(memory, int) or memory < 0 or memory >= 2 ** 100:
                print("The memory number should be an integer from 0 to 2**100.")
                return False
            for act in result:
                if step >= MAX_STEP:
                    print("You are tired and your scanner is off. Bye bye.")
                    return False
                r, c = player[0] + DIR[act][0], player[1] + DIR[act][1]
                if maze[r][c] == WALL:
                    print("BAM! You in the wall at {}, {}.".format(r, c))
                    return False
                elif maze[r][c] == EXIT:
                    print("GRATZ!", step)
                    return True
                else:
                    player = r, c
                    step += 1

    assert checker(find_path, (3, 9), [
        "XXXXXXXXXXXX",
        "X..........X",
        "X.....X....X",
        "X.....X....X",
        "X.....X....X",
        "XX.XXXXXXXXX",
        "X....X.....X",
        "X..........X",
        "X....X.....X",
        "X....X...E.X",
        "X....X.....X",
        "XXXXXXXXXXXX",
    ]), "4 rooms"
    assert checker(find_path, (8, 4), [
        "XXXXXXXXXXXX",
        "X..........X",
        "X.XXXX...X.X",
        "X...X....X.X",
        "XXX..X.....X",
        "X.X..X...X.X",
        "X.X..X.E.X.X",
        "X.X..X...X.X",
        "X....X.....X",
        "X.XXXXXXXX.X",
        "X..........X",
        "XXXXXXXXXXXX",
    ]), "Vinc"
    assert checker(find_path, (1, 1), [
        "XXXXXXXXXXXX",
        "X..........X",
        "X.XXXXXXXX.X",
        "X.X......X.X",
        "X.X......X.X",
        "X.X......X.X",
        "X.X......X.X",
        "X.X......X.X",
        "X.X......X.X",
        "X.XXXXXXXX.X",
        "X.........EX",
        "XXXXXXXXXXXX",
    ]), "Simple"
    assert checker(find_path, (1, 4), [
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
    ]), "Up Down"
    assert checker(find_path, (10, 10), [
        "XXXXXXXXXXXX",
        "X..........X",
        "X.XXXXXXXX.X",
        "X.X......X.X",
        "X.X.XX.X.X.X",
        "X.X......X.X",
        "X.X......X.X",
        "X.X..E...X.X",
        "X.X......X.X",
        "X.XXXX.XXX.X",
        "X..........X",
        "XXXXXXXXXXXX",
    ]), "Left"
    assert checker(find_path, (4, 7), [
        "XXXXXXXXXXXX",
        "X.X.X...X..X",
        "X.X...X...XX",
        "X.XXXXXXX..X",
        "X...X...XX.X",
        "XXX...X....X",
        "X.XXXXXXXX.X",
        "X.X..E..XX.X",
        "X...X.XXX..X",
        "X.XXX.X...XX",
        "X...X...X..X",
        "XXXXXXXXXXXX",
    ]), "Edge 1"
    assert checker(find_path, (1, 4), [
        'XXXXXXXXXXXX',
        'X.X...X.X..X',
        'X.XXX.....XX',
        'X...X.X.XXXX',
        'XXX.XXX...XX',
        'X.X..X..X..X',
        'X.XX.XXXXX.X',
        'X..X.XX....X',
        'XX...X..XX.X',
        'X..X.X.XX..X',
        'X.XX...XE.XX', 
        'XXXXXXXXXXXX',
    ]), "Edge 2"
    assert checker(find_path, (1, 5), [
        'XXXXXXXXXXXX',
        'X.X.X......X',
        'X...X.X.XX.X',
        'XXX.X.X.XXXX',
        'X...X.X....X',
        'XX.XX.XXX.XX',
        'X..X...EX.XX',
        'X.XXXXX.X..X',
        'X.X...XXXX.X',
        'X...X..XX..X',
        'X.X.XX....XX',
        'XXXXXXXXXXXX'
    ]), "Edge 3"
