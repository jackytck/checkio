#!/usr/bin/python
def checkio(data):
    x, y = [r[0] for r in data], [r[1] for r in data]
    return abs(sum(i * j for i, j in zip(x, y[1:] + [y[0]])) - sum(i * j for i, j in zip(y, x[1:] + [x[0]]))) * 0.5

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[1, 1], [9, 9], [9, 1]]) == 32, "The half of the square"
    assert checkio([[4, 10], [7, 1], [1, 4]]) == 22.5, "Triangle"
    assert checkio([[1, 2], [3, 8], [9, 8], [7, 1]]) == 40, "Quadrilateral"
    assert checkio([[3, 3], [2, 7], [5, 9], [8, 7], [7, 3]]) == 26, "Pentagon"
    assert checkio([[7, 2], [3, 2], [1, 5],
                    [3, 9], [7, 9], [9, 6]]) == 42, "Hexagon"
    assert checkio([[4, 1], [3, 4], [3, 7], [4, 8],
                    [7, 9], [9, 6], [7, 1]]) == 35.5, "Heptagon"
