#!/opt/local/bin/python3.3
from collections import deque, defaultdict


def can_pass(matrix, first, second):
    w, h = len(matrix), len(matrix[0])
    q = deque([first])
    visit = defaultdict(bool)
    while q:
        p = q.popleft()
        if p == second:
            return True
        if visit[p]:
            continue
        visit[p] = True
        px, py = p
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            i, j = px + dx, py + dy
            if 0 <= i < w and 0 <= j < h and matrix[i][j] == matrix[px][py]:
                q.append((i, j))
    return False


if __name__ == '__main__':
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 2), (0, 5)) == True, 'First example'
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 3), (6, 0)) == False, 'First example'
