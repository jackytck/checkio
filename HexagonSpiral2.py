#!/opt/local/bin/python3.3
def cube(k):
    if k == 1:
        return 0, 0, 0
    y = int((3 + (12 * k - 15) ** 0.5) / 6)
    x, z = -y, 0
    r, step = divmod(3 * y * (y + 1) + 1 - k, y)
    c = [x, y, z]
    s = -1 if r & 1 else 1
    x, y, z = [s * c[r % 3], s * c[(r + 1) % 3], s * c[(r + 2) % 3]]
    d = ((0, -1, 1), (1, -1, 0), (1, 0, -1),
         (0, 1, -1), (-1, 1, 0), (-1, 0, 1))[r]
    return x + d[0] * step, y + d[1] * step, z + d[2] * step


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
