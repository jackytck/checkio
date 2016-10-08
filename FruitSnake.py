#!/opt/local/bin/python3.3
from collections import deque, defaultdict
from copy import deepcopy

SIZE = 10
TREE = 'T'
CHERRY = 'C'
EMPTY = '.'
ACT = 'FLR'

Eaten = 0


def build_forrest(field):
    return [[x if x in 'T.' else '.' for x in y] for y in field]


def cherry_pos(field):
    for i, x in enumerate(field):
        for j, y in enumerate(x):
            if y == CHERRY:
                return i, j


def snake(field):
    d = {}
    for i, x in enumerate(field):
        for j, y in enumerate(x):
            if y.isdigit():
                d[int(y)] = i, j
    return [d[x] for x in sorted(d)]


def move_to(body, x, y):
    return [(x, y)] + body[:-1]


def next_move(body, forrest):
    hx, hy = body[0]
    sx, sy = body[1]
    f = complex(hx - sx, hy - sy)
    moves = (f, f * 1j, f / 1j)
    for i, z in enumerate(moves):
        x, y = hx + int(z.real), hy + int(z.imag)
        if (0 <= x < SIZE and 0 <= y < SIZE and forrest[x][y] == EMPTY
                and (x, y) not in body[:-1]):
            yield ACT[i], move_to(body, x, y), body[-1]


def is_stuck(forrest, body, grow):
    if Eaten == 5:
        return False
    f = deepcopy(forrest)
    for i, (x, y) in enumerate(body + [grow]):
        f[x][y] = str(i)

    empty = []
    for i, x in enumerate(f):
        for j, y in enumerate(x):
            if y == '.':
                empty.append((i + j, i, j))
    empty.sort()
    t1 = empty[0][1:]
    t2 = empty[-1][1:]
    f[t1[0]][t1[1]] = 'C'
    field1 = [''.join(x) for x in f]
    f[t1[0]][t1[1]] = '.'
    f[t2[0]][t2[1]] = 'C'
    field2 = [''.join(x) for x in f]

    return not move_snake(field1, True) or not move_snake(field2, True)


def move_snake(field, simple=False):
    forrest = build_forrest(field)
    goal = cherry_pos(field)
    body = snake(field)

    q = deque([(body, '', '')])
    visit = defaultdict(bool)
    while q:
        b, seq, g = q.popleft()
        if b[0] == goal and (simple or not is_stuck(forrest, b, g)):
            global Eaten
            Eaten += 1
            return seq
        t = tuple(b)
        if visit[t]:
            continue
        visit[t] = True

        for m in next_move(b, forrest):
            symbol, child, grow = m
            q.append((child, seq + symbol, grow))

if __name__ == '__main__':
    ACTION = ("L", "R", "F")
    SNAKE_HEAD = '0'
    SNAKE = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

    DISTANCE = 5
    INITIAL_STEPS = 200

    def find_snake(field_map):
        snake = {}
        for i, row in enumerate(field_map):
            for j, ch in enumerate(row):
                if ch in SNAKE:
                    snake[ch] = (i, j)
        return snake

    def find_new_head(snake, action):
        head = snake[SNAKE_HEAD]
        snake_dir = (head[0] - snake["1"][0], head[1] - snake["1"][1])
        if action == 'F':
            return head[0] + snake_dir[0], head[1] + snake_dir[1]
        elif action == 'L':
            return head[0] - snake_dir[1], head[1] + snake_dir[0]
        elif action == 'R':
            return head[0] + snake_dir[1], head[1] - snake_dir[0]
        else:
            raise ValueError("The action must be only L,R or F")

    def pack_map(list_map):
        return [''.join(row) for row in list_map]

    def create_cherry(field, head):
        from random import choice

        distance = DISTANCE
        possible = []
        while not possible:
            possible = [(i, j) for i in range(SIZE) for j in range(SIZE)
                        if field[i][j] == "." and (abs(i - head[0]) + abs(j - head[1])) == distance]
            distance = (distance + 1) % SIZE
        return choice(possible)

    def check_solution(func, field_map):
        global Eaten
        Eaten = 0

        temp_map = [list(row) for row in field_map]
        head = find_snake(field_map)[SNAKE_HEAD]
        crow, ccol = create_cherry(field_map, head)
        temp_map[crow][ccol] = CHERRY
        field_map = pack_map(temp_map)
        step_count = INITIAL_STEPS
        while True:
            route = func(field_map[:])
            res_route = ""
            for ch in route:
                if step_count < 0:
                    print("Too many steps."),
                    return False
                if ch not in ACTION:
                    print("The route must contain only F,L,R symbols")
                    return False
                res_route += ch
                snake = find_snake(temp_map)
                tail = snake[max(snake.keys())]
                temp_map[tail[0]][tail[1]] = EMPTY
                new_head = find_new_head(snake, ch)
                for s_key in sorted(snake.keys())[:-1]:
                    s = snake[s_key]
                    temp_map[s[0]][s[1]] = str(int(temp_map[s[0]][s[1]]) + 1)
                if (new_head[0] < 0 or new_head[0] >= len(temp_map) or
                            new_head[1] < 0 or new_head[1] >= len(temp_map[0])):
                    print("The snake crawl outside")
                    return False
                elif temp_map[new_head[0]][new_head[1]] == 'T':
                    print("The snake struck at the tree")
                    return False
                elif temp_map[new_head[0]][new_head[1]] in SNAKE:
                    print("The snake bit itself")
                    return False

                if temp_map[new_head[0]][new_head[1]] == 'C':
                    temp_map[new_head[0]][new_head[1]] = SNAKE_HEAD
                    if max(snake.keys()) == '9':
                        print("Score: {}".format(step_count))
                        return True
                    else:
                        temp_map[tail[0]][tail[1]] = str(int(max(snake.keys())) + 1)
                        cherry = create_cherry(temp_map, new_head)
                        temp_map[cherry[0]][cherry[1]] = CHERRY
                        step_count -= 1
                else:
                    temp_map[new_head[0]][new_head[1]] = SNAKE_HEAD
                step_count -= 1
                field_map = pack_map(temp_map)

    #ans = move_snake(
    #    ["......T...",
    #    "...T..T...",
    #    "...T.TT.T.",
    #    "..TT..T...",
    #    "TT567...TT",
    #    "..4TT.T...",
    #    ".T3...T...",
    #    ".12TTTTTT.",
    #    ".0T.......",
    #    "..T...C.TT"])
    #print(ans)
    for i in range(10):
        assert check_solution(move_snake, [
            ".T.....T..",
            "..........",
            ".....T....",
            "..T....T..",
            "..........",
            ".0...T....",
            ".1........",
            ".2.T...T..",
            ".3...T....",
            ".4........"]), "Basic map"
        assert check_solution(move_snake, [
            "..T....T..",
            ".......T..",
            "...TTT....",
            "..T....T..",
            "..T...T...",
            ".0T..T....",
            ".1........",
            ".2.T..TT..",
            ".3..TT....",
            ".4........"]), "Extra map"

        assert check_solution(move_snake, [
            "....T...TT",
            ".TT...T...",
            "....T...T.",
            "TTTTTTTTT.",
            "T.........",
            "T.TTTTTTT.",
            "T..4.TT...",
            "TTT32T..T.",
            "TT.01T....",
            "TT...TTTTT"]), 'Evil'
