#!/opt/local/bin/python3.3
def moveRowLeft(row):
    ret, skip = [], []
    row = [x for x in row if x]
    for i, x in enumerate(row):
        if i in skip or not x:
            continue
        if i < len(row) - 1 and x == row[i + 1]:
            ret.append(x * 2)
            skip.append(i + 1)
        else:
            ret.append(x)
    ret.extend([0] * (4 - len(ret)))
    return ret


def moveRowRight(row):
    return moveRowLeft(row[::-1])[::-1]


def moveLeft(state):
    return [moveRowLeft(x) for x in state]


def moveRight(state):
    return [moveRowRight(x) for x in state]


def transpose(state):
    return list(map(list, zip(*state)))


def moveUp(state):
    return transpose(moveLeft(transpose(state)))


def moveDown(state):
    return transpose(moveRight(transpose(state)))


def checkWin(state):
    for x in state:
        for y in x:
            if y == 2048:
                return [list('UWIN')] * 4
    return state


def checkLose(state):
    lose = True
    for x in state:
        for y in x:
            if y == 0:
                lose = False
                break
    if lose:
        return [list('GAME'), list('OVER')] * 2
    return state


def addNew(state):
    for i, x in enumerate(reversed(state)):
        for j, y in enumerate(reversed(x)):
            if y == 0:
                state[3 - i][3 - j] = 2
                return state
    return state


def move2048(state, move):
    if move == 'up':
        state = moveUp(state)
    elif move == 'down':
        state = moveDown(state)
    elif move == 'left':
        state = moveLeft(state)
    elif move == 'right':
        state = moveRight(state)
    return addNew(checkWin(checkLose(state)))


if __name__ == '__main__':
    assert move2048([[0, 2, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 2, 0, 0]], 'up') == [[0, 4, 0, 0],
                                              [0, 0, 0, 0],
                                              [0, 0, 0, 0],
                                              [0, 0, 0, 2]], "Start. Move Up!"
    assert move2048([[4, 0, 0, 0],
                     [0, 4, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 8, 8]], 'right') == [[0, 0, 0, 4],
                                                 [0, 0, 0, 4],
                                                 [0, 0, 0, 0],
                                                 [0, 0, 2, 16]], "Simple right"
    assert move2048([[2, 0, 2, 2],
                     [0, 4, 4, 4],
                     [8, 8, 8, 16],
                     [0, 0, 0, 0]], 'right') == [[0, 0, 2, 4],
                                                 [0, 0, 4, 8],
                                                 [0, 8, 16, 16],
                                                 [0, 0, 0, 2]], "Three merging"
    assert move2048([[256, 0, 256, 4],
                     [16, 8, 8, 0],
                     [32, 32, 32, 32],
                     [4, 4, 2, 2]], 'right') == [[0, 0, 512, 4],
                                                 [0, 0, 16, 16],
                                                 [0, 0, 64, 64],
                                                 [0, 2, 8, 4]], "All right"
    assert move2048([[4, 4, 0, 0],
                     [0, 4, 1024, 0],
                     [0, 256, 0, 256],
                     [0, 1024, 1024, 8]], 'down') == [['U', 'W', 'I', 'N'],
                                                      ['U', 'W', 'I', 'N'],
                                                      ['U', 'W', 'I', 'N'],
                                                      ['U', 'W', 'I', 'N']], "We are the champions!"
    assert move2048([[2, 4, 8, 16],
                     [32, 64, 128, 256],
                     [512, 1024, 2, 4],
                     [8, 16, 32, 64]], 'left') == [['G', 'A', 'M', 'E'],
                                                   ['O', 'V', 'E', 'R'],
                                                   ['G', 'A', 'M', 'E'],
                                                   ['O', 'V', 'E', 'R']], "Nobody moves!"
