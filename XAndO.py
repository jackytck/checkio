#!/opt/local/bin/python3.3
def is_empty(grid):
    return ''.join(grid).count('.') == 9


def holes(grid):
    for i in range(3):
        for j in range(3):
            if grid[i][j] == '.':
                yield i, j


def fill(grid, x, y, your_mark):
    g = [list(x) for x in grid]
    g[x][y] = your_mark
    return [''.join(x) for x in g]


def score(grid, your_mark):
    enemy = {'X': 'O', 'O': 'X'}[your_mark]
    lines = ([''.join(row) for row in grid] +
             [''.join(row) for row in zip(*grid)] +
             [''.join(row) for row in
                 zip(*[(r[i], r[2 - i]) for i, r in enumerate(grid)])])
    if your_mark * 3 in lines:
        return 1
    elif enemy * 3 in lines:
        return -1
    elif '.' not in ''.join(lines):
        return 0
    else:
        best = -1
        for hx, hy in holes(grid):
            g = fill(grid, hx, hy, enemy)
            s = score(g, enemy)
            if s == 1:
                return -1
            best = max(best, s)
        return -best


def x_and_o(grid, your_mark):
    if is_empty(grid):
        return 0, 0
    dx, dy = 0, 0
    for x, y in holes(grid):
        g = fill(grid, x, y, your_mark)
        s = score(g, your_mark)
        if s == 1:
            return x, y
        elif s == 0:
            dx, dy = x, y
    return dx, dy


if __name__ == '__main__':
    from random import choice

    def random_bot(grid, mark):
        empties = [(x, y) for x in range(3) for y in range(3) if grid[x][y] == "."]
        return choice(empties) if empties else (None, None)

    def referee(field):
        lines = (["".join(row) for row in field] + ["".join(row) for row in zip(*field)] +
                 [''.join(row) for row in zip(*[(r[i], r[2 - i]) for i, r in enumerate(field)])])
        if "X" * 3 in lines:
            return "X"
        elif "O" * 3 in lines:
            return "O"
        elif not "." in "".join(lines):
            return "D"
        else:
            return "."

    def check_game(user_func, user_mark, bot_mark, bot_algorithm=random_bot):
        grid = [["."] * 3 for _ in range(3)]
        if bot_mark == "X":
            x, y = bot_algorithm(grid, bot_mark)
            grid[x][y] = "X"
        while True:
            user_result = user_func(tuple("".join(row) for row in grid), user_mark)
            if (not isinstance(user_result, (tuple, list)) or len(user_result) != 2 or
                    not all(isinstance(u, int) and 0 <= u < 3 for u in user_result)):
                print("The result must be a list/tuple of two integers from 0 to 2.")
                return False

            if grid[user_result[0]][user_result[1]] != ".":
                print("You tried to mark the filled cell.")
                return False
            grid[user_result[0]][user_result[1]] = user_mark
            game_result = referee(grid)

            if game_result == "D" or game_result == user_mark:
                return True
            bot_move = bot_algorithm(grid, bot_mark)
            grid[bot_move[0]][bot_move[1]] = bot_mark
            game_result = referee(grid)
            if game_result == bot_mark:
                print("Lost :-(")
                return False
            elif game_result == "D":
                return True

    assert check_game(x_and_o, "X", "O"), "Random X"
    assert check_game(x_and_o, "O", "X"), "Random O"
