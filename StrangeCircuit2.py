#!/opt/local/bin/python3.3
def coords(k):
    t = (k ** 0.5 + 1) / 2
    n = int(t)
    if n == t:
        n -= 1
    if n == 0:
        return 0, 0
    rank = k - (2 * n - 1) ** 2
    s = 2 * n
    s, r = rank // s, s - rank % s
    if s == 0:
        return n - r, n
    elif s == 1:
        return n, -n + r
    elif s == 2:
        return -n + r, -n
    elif s == 3:
        return -n, n - r
    else:
        return -n, n


def find_distance(first, second):
    a, b = coords(first), coords(second)
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

if __name__ == '__main__':
    assert find_distance(1, 9) == 2, "First"
    assert find_distance(9, 1) == 2, "Reverse First"
    assert find_distance(10, 25) == 1, "Neighbours"
    assert find_distance(5, 9) == 4, "Diagonal"
    assert find_distance(26, 31) == 5, "One row"
    assert find_distance(50, 16) == 10, "One more test"
