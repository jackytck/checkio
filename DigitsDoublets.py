#!/usr/bin/python
import itertools
from collections import deque

def link(a, b):
    return sum(x != y for x, y in zip(str(a), str(b))) == 1

def checkio(numbers):
    n = len(numbers)

    #build graph
    edges = [[] for i in range(n)]
    for i, j in itertools.combinations(range(len(numbers)), 2):
        if link(numbers[i], numbers[j]):
            edges[i].append(j)
            edges[j].append(i)

    #bfs
    q = deque([(0, '0')])
    visit = [False for i in range(n)]
    while q:
        w, path = q.popleft()
        if visit[w]:
            continue
        if w == n - 1:
            return [numbers[int(x)] for x in path.split('.')]
        visit[w] = True
        for c in edges[w]:
            q.append((c, '%s.%d' % (path, c)))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([123, 991, 323, 321, 329, 121, 921, 125, 999]) == [123, 121, 921, 991, 999], "First"
    assert checkio([111, 222, 333, 444, 555, 666, 121, 727, 127, 777]) == [111, 121, 127, 727, 777], "Second"
    assert checkio([456, 455, 454, 356, 656, 654]) == [456, 454, 654], "Third, [456, 656, 654] is correct too"
