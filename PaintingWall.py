#!/opt/local/bin/python3.3
import bisect


def painted(data):
    cnt, last = 0, -1
    for a, b in data:
        cnt += max(0, min(b - a + 1, b - last))
        last = max(last, b)
    return cnt


def checkio(num, data):
    ranges = []
    for i, r in enumerate(data, 1):
        bisect.insort(ranges, r)
        if painted(ranges) >= num:
            return i
    return -1

if __name__ == '__main__':
    assert checkio(5, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 1, "1st"
    assert checkio(6, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 2, "2nd"
    assert checkio(11, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 3, "3rd"
    assert checkio(16, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 4, "4th"
    assert checkio(21, [[1, 5], [11, 15], [2, 14], [21, 25]]) == -1, "not enough"
    assert checkio(1000000011, [[1, 1000000000], [11, 1000000010]]) == -1, "large"
