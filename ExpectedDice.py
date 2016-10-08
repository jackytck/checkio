#!/opt/local/bin/python3.3
from collections import Counter


def nCr(n, r):
    top, val = n, 1
    while (top > (n - r)):
        val *= top
        top -= 1
    n = 1
    while (n < r + 1):
        val /= n
        n += 1
    return val


def probability(n, s, p):
    if p == 0:
        return 0
    r = min((p - n) // s, n) + 1
    c = sum((-1)**k * nCr(n, k) * nCr(p - s*k - 1, n - 1) for k in range(r))
    return c / (s**n)


def expected(dice_number, sides, target, board, trial=500):
    ret, size = 0, len(board)
    moves = range(dice_number, dice_number * sides + 1)
    p = Counter()
    for move in moves:
        p[move] = probability(dice_number, sides, move)

    v = [1] + [0] * (size - 1)
    for roll in range(1, trial):
        tmp = [0] * size
        for move in moves:
            for src in range(size):
                if src != target:
                    dest = (src + move) % size
                    dest = (dest + board[dest]) % size
                    tmp[dest] += p[move] * v[src]
        v = tmp
        ret += roll * v[target]

    return ret

if __name__ == '__main__':
    def almost_equal(checked, correct, significant_digits=1):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert(almost_equal(expected(1, 4, 3, [0, 0, 0, 0]), 4.0))
    assert(almost_equal(expected(1, 4, 1, [0, 0, 0, 0]), 4.0))
    assert(almost_equal(expected(1, 4, 3, [0, 2, 1, 0]), 1.3))
    assert(almost_equal(expected(1, 4, 3, [0, -1, -2, 0]), 4.0))
    assert(almost_equal(expected(1, 6, 1, [0] * 10), 8.6))
    assert(almost_equal(expected(2, 6, 1, [0] * 10), 10.2))
    assert(almost_equal(expected(1, 6, 29, [0, -2, -3, -4, -5, -6, -7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 1.0))
    assert(almost_equal(expected(2, 6, 29, [0, -1, -2, -3, -4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 31.67))
    assert(almost_equal(expected(1, 4, 29, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 29.6))
