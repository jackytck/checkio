#!/usr/bin/python
from collections import deque

def checkio(chips):
    ret = 0
    a, b, c = chips[0]
    q = deque([(a, b, c, '100000'), (a, c, b, '100000'), (b, c, a, '100000')])
    while q:
        t, f, s, v = q.popleft()#to, from, score, visit
        if v.count('0') == 0 and t == f:
            ret = max(ret, s)
        for i, ch in enumerate(chips):
            if v[i] != '1' and t in ch:
                a, b, c = ch
                mask = v[:i] + '1' + v[i+1:]
                if b == t:
                    a, b = b, a
                elif c == t:
                    a, c = c, a
                q.append((b, f, s + c, mask))
                q.append((c, f, s + b, mask))
    return ret

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(
        [[1, 4, 20], [3, 1, 5], [50, 2, 3],
         [5, 2, 7], [7, 5, 20], [4, 7, 50]]) == 152, "First"
    assert checkio(
        [[1, 10, 2], [2, 20, 3], [3, 30, 4],
         [4, 40, 5], [5, 50, 6], [6, 60, 1]]) == 210, "Second"
    assert checkio(
        [[1, 2, 3], [2, 1, 3], [4, 5, 6],
         [6, 5, 4], [5, 1, 2], [6, 4, 3]]) == 21, "Third"
    assert checkio(
        [[5, 9, 5], [9, 6, 9], [6, 7, 6],
         [7, 8, 7], [8, 1, 8], [1, 2, 1]]) == 0, "Fourth"
