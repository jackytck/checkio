#!/usr/bin/python
import math

def checkio(radius):
    """count tiles"""
    s, p, f, c = 0, 0, int(radius / 2 ** 0.5), int(math.ceil(radius))
    for i in range(1, c + 1):
        for j in range(1, c + 1):
            if i <= f and j <= f:
                s += 1
                continue
            if abs(complex(i, j)) <= radius:
                s += 1
            elif abs(complex(i-1, j-1)) <= radius:
                p += 1
    return [s * 4, p * 4]

if __name__ == '__main__':
    assert checkio(2) == [4, 12], "First, N=2"
    assert checkio(3) == [16, 20], "Second, N=3"
    assert checkio(2.1) == [4, 20], "Third, N=2.1"
    assert checkio(2.5) == [12, 20], "Fourth, N=2.5"
