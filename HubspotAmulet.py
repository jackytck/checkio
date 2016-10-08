#!/usr/bin/python
GOAL = (0, 225, 315)

def checkio(matrix):
    g1, g2, g3 = GOAL
    d1, f2, f3, s1, d2, s3, t1, t2, d3 = sum(matrix, [])
    for i in range(-180, 180):
        for j in range(-180, 180):
            b1 = g1 - i - j * s1
            b2 = g2 - i * f2 - j
            b3 = (g3 - i * f3 - j * s3) % 360
            if -180 <= b3 <180 and (b1 - b3 * t1) % 360 == 0 and (b2 - b3 * t2) % 360 == 0:
                return i, j, b3

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print(checkio([
        [1, 2, 3],
        [3, 1, 2],
        [2, 3, 1]]))
    print(checkio([
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]]))
    print(checkio([
        [1, 3, 5],
        [3, 1, 5],
        [2, 5, 1]]))
