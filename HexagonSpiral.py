#!/opt/local/bin/python3.3
def cube(k):
    if k == 1:
        return 0, 0, 0

    y, n = 1, 2
    while n <= k:
        n = 2 + 3 * (y - 1) * (y - 2)
        y += 1
    y = max(0, y - 3)
    x, z = -y, 0

    rotate, step = divmod(n - k - 1, y)
    for _ in range(rotate):
        x, y, z = -y, -z, -x

    delta = ((0, -1, 1), (1, -1, 0), (1, 0, -1),
             (0, 1, -1), (-1, 1, 0), (-1, 0, 1))[rotate]
    x += delta[0] * step
    y += delta[1] * step
    z += delta[2] * step

    return x, y, z


def hex_spiral(first, second):
    return max(abs(a - b) for a, b in zip(cube(first), cube(second)))


if __name__ == '__main__':
    assert hex_spiral(2, 9) == 1, "First"
    assert hex_spiral(9, 2) == 1, "Reverse First"
    assert hex_spiral(6, 19) == 2, "Second, short way"
    assert hex_spiral(5, 11) == 3, "Third"
    assert hex_spiral(13, 15) == 2, "Fourth, One row"
    assert hex_spiral(11, 17) == 4, "Fifth, One more test"
    assert hex_spiral(42, 13) == 5, "Fifth, One more test"
    assert hex_spiral(76, 65) == 10, "Fifth, One more test"
