#!/opt/local/bin/python3.3
from collections import defaultdict
from heapq import heappush, heappop


def capture(matrix):
    ret = 0
    visit = defaultdict(bool)
    q = []
    heappush(q, (0, 0))
    while q:
        t, u = heappop(q)
        if visit[u]:
            continue
        visit[u] = True
        ret = max(ret, t)
        for i, c in enumerate(matrix[u]):
            if i != u and c:
                heappush(q, (t + matrix[i][i], i))
    return ret


if __name__ == '__main__':
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 8, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 8, "Base example"
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 1, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 4, "Low security"
    assert capture([[0, 1, 1],
                    [1, 9, 1],
                    [1, 1, 9]]) == 9, "Small"
    assert capture([[0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 2, 1, 0, 0, 0, 0, 0, 0],
                      [0, 0, 1, 3, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 4, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 5, 1, 0, 0, 0],
                      [0, 0, 0, 0, 0, 1, 6, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 7, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1, 8, 1],
                      [0, 0, 0, 0, 0, 0, 0, 0, 1, 9]]) == 45
