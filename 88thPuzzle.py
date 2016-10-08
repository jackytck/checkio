#!/opt/local/bin/python3.3
from collections import deque

GOAL = (1, 2, 1, 0, 2, 0, 0, 3, 0, 4, 3, 4)
RINGS = ((0, 3, 5, 2), (1, 4, 6, 3), (5, 8, 10, 7), (6, 9, 11, 8))


def rotate(state, ring):
    ret = list(state)
    cir = RINGS[ring]
    for i, x in enumerate(cir):
        ret[x] = state[cir[i - 1]]
    return ret


def puzzle88(state):
    q = deque([(state, '')])
    while q:
        s, m = q.popleft()
        if tuple(s) == GOAL:
            return m
        for i in range(4):
            q.append((rotate(s, i), m + str(i + 1)))


if __name__ == '__main__':
    assert puzzle88((0, 2, 1, 3, 2, 1, 4, 0, 0, 4, 0, 3)) in ('1433', '4133'), "Example"
    assert puzzle88((0, 2, 1, 2, 0, 0, 4, 1, 0, 4, 3, 3)) in ('4231', '4321'), "Rotate all"
    assert puzzle88((0, 2, 1, 2, 4, 0, 0, 1, 3, 4, 3, 0)) in ('2314', '2341', '3214', '3241'), "Four paths"
