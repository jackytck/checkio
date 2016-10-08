#!/usr/bin/python
def checkio(matr):
    '''
    Given matrix  NxN (3<=N<=10). 
    Numbers between 1 and 5 are elements of A. 
    Find the biggest union of the same numbers in group and the number. 
    Say, group is a bunch of numbers that stay near each other.
    '''
    ret = [0, 0]
    dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
    visited = [[False for x in y] for y in matr]
    for i, x in enumerate(matr):
        for j, y in enumerate(x):
            if not visited[i][j]:
                stack = [(i, j)]
                cnt = 0
                while stack:
                    tx, ty = stack.pop()
                    if visited[tx][ty]:
                        continue
                    cnt += 1
                    visited[tx][ty] = True
                    for dx, dy in dirs:
                        try:
                            px, py = tx + dx, ty + dy
                            if px >= 0 and py >= 0 and matr[px][py] == y and not visited[px][py]:
                                stack.append((px, py))
                        except IndexError:
                            continue
                if cnt > ret[0]:
                    ret = [cnt, y]
    return ret

if __name__ == '__main__':
    assert checkio([
        [1,2,3,4,5],
        [1,1,1,2,3],
        [1,1,1,2,2],
        [1,2,2,2,1],
        [1,1,1,1,1]
    ])==[14,1], 'First'

    assert checkio([
        [2, 1, 2, 2, 2, 4],
        [2, 5, 2, 2, 2, 2],
        [2, 5, 4, 2, 2, 2],
        [2, 5, 2, 2, 4, 2],
        [2, 4, 2, 2, 2, 2],
        [2, 2, 4, 4, 2, 2]
    ])==[19,2], 'Second'

    print 'All ok'
