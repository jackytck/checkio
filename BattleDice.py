#!/opt/local/bin/python3.3
from collections import Counter


def battle(ad1, ad2):
    a, b = ad1
    c, d = ad2
    return max(0, c - b), max(0, a - d)


def add(ad1, ad2):
    a, b = ad1
    c, d = ad2
    return a + c, b + d


def joint(c1, c2):
    ret = Counter()
    for ad1 in c1:
        for ad2 in c2:
            ret[battle(ad1, ad2)] += c1[ad1] * c2[ad2]
    return ret


def get_board(n1, n2):
    return [[0 for x in range(n2 + 1)] for y in range(n1 + 1)]


def battle_probability(dice, n1, n2, trial=100):
    ret = 0

    # 1. base case: 1 dice, 1 unit
    m = max(n1, n2)
    table = Counter()
    side = len(dice)
    dice = [(x.count('A'), x.count('D')) for x in dice]
    base = Counter()
    for d in dice:
        base[d] += 1 / side
    table[1] = base

    # 2. probabilities for 2 to m dice
    for i in range(1, m):
        new = Counter()
        old = table[i]
        for o in old:
            for b in base:
                new[add(o, b)] += old[o] * base[b]
        table[i+1] = new

    # 3. joint-probabilities for every pair of unit
    joint_table = Counter()
    for i in range(n1):
        for j in range(n2):
            joint_table[(i+1, j+1)] = joint(table[i+1], table[j+1])

    # 4. simulate every move on board iteratively
    board = get_board(n1, n2)
    board[0][0] = 1

    for t in range(trial):
        temp = get_board(n1, n2)
        for x in range(n1):
            for y in range(n2):
                prior = board[x][y]
                if prior != 0:
                    moves = joint_table[(n1-x, n2-y)]
                    for m in moves:
                        a, b = x + m[0], y + m[1]
                        a, b = min(n1, a), min(n2, b)
                        temp[a][b] += prior * moves[m]
        board = temp
        ret += sum(list(zip(*board))[-1][:-1])

    return ret


if __name__ == '__main__':
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert(almost_equal(battle_probability(['A', 'D'], 3, 3), 0.0000)), "Always ties, nobody wins"
    assert(almost_equal(battle_probability(['A', 'D'], 4, 3), 1.0000)), "Always win"
    assert(almost_equal(battle_probability(['AA', 'A', 'D', 'DD'], 3, 4), 0.0186)), "You can win"
    assert(almost_equal(battle_probability(['AA', 'A', 'D', 'DD'], 4, 4), 0.4079)), "Ready to fight"
    assert(almost_equal(battle_probability(['AA', 'A', 'D', 'DD'], 5, 4), 0.9073)), "I have good chance"
    #battle_probability(['AA', 'A', 'D', 'DD'], 3, 4)
    #battle_probability(['AA', 'A', 'D', 'DD'], 10, 4)
    #battle_probability(['A', 'A', 'A', 'A', 'A', 'A', 'D', 'D', 'D', ''], 10, 10)
