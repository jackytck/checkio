#!/usr/bin/python
def checkio(buildings):
    cnt = 0
    buildings = sorted(buildings, key=lambda x: x[1])
    for i, b in enumerate(buildings):
        mask = [1] * (b[2] - b[0])
        for j in range(0, i):
            f = buildings[j]
            if f[1] < b[1] and f[4] >= b[4]:
                left, right = f[0] - b[0], f[2] - b[0]
                for k in range(left, right):
                    if 0 <= k < len(mask):
                        mask[k] = 0
        if sum(mask) > 0:
            cnt += 1
    return cnt

if __name__ == '__main__':
    assert checkio([
        [1, 1, 4, 5, 3.5],
        [2, 6, 4, 8, 5],
        [5, 1, 9, 3, 6],
        [5, 5, 6, 6, 8],
        [7, 4, 10, 6, 4],
        [5, 7, 10, 8, 3]
    ]) == 5, "First"
    assert checkio([
        [1, 1, 11, 2, 2],
        [2, 3, 10, 4, 1],
        [3, 5, 9, 6, 3],
        [4, 7, 8, 8, 2]
    ]) == 2, "Second"
    assert checkio([
        [1, 1, 3, 3, 6],
        [5, 1, 7, 3, 6],
        [9, 1, 11, 3, 6],
        [1, 4, 3, 6, 6],
        [5, 4, 7, 6, 6],
        [9, 4, 11, 6, 6],
        [1, 7, 11, 8, 3.25]
    ]) == 4, "Third"
    assert checkio([
        [0, 0, 1, 1, 10]
    ]) == 1,"Alone"
    assert checkio([
        [2, 2, 3, 3, 4],
        [2, 5, 3, 6, 4]
    ]) == 1, "Shadow"
