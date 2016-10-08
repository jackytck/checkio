#!/usr/bin/python
def rot(m):
    return map(list, zip(*m[::-1]))

def trans(m):
    return map(list, zip(*m))

def diag(m):
    ret = []
    for i, x in enumerate(m):
        tmp, k  = [], 0
        while i+k < len(m):
            tmp.append(m[i+k][k])
            k += 1
        if len(tmp) > 3:
            ret.append(tmp)
    return ret

def diags(m):
    return diag(m) + diag(trans(m)) + diag(rot(m)) + diag(trans(rot(m)))

def checkrow(r):
    ml, l, last = 0, 1, ''
    for x in r:
        if x == last:
            l += 1
        else:
            ml = max(l, ml)
            l = 1
        last = x
    ml = max(l, ml)
    return True if ml > 3 else False

def checkio(matr):
    '''
    Given the matrix NxN (4<=N<=10). Check if 4 numbers in sequence in a column or in a row or diagonally exist.
    '''
    return bool(filter(checkrow, matr + trans(matr) + diags(matr)))

if __name__ == '__main__':
    assert checkio([
        [1, 1, 1, 1],
        [1, 2, 3, 4],
        [5, 4, 3, 1],
        [6, 1, 3, 2]
    ]) == True, "First, horizontal"
    assert checkio([
        [7, 6,  5, 7, 9],
        [8, 7,  3, 6, 5],
        [4, 0,  6, 5, 4],
        [9, 8,  4, 0, 5],
        [2, 10, 7, 2, 10]
    ]) == False, "Second"
    assert checkio([
        [10, 1, 9,  6, 4, 1],
        [2,  5, 4,  2, 2, 7],
        [2,  2, 1,  2, 6, 4],
        [3,  2, 2,  1, 0, 2],
        [7,  9, 6,  2, 5, 7],
        [7,  3, 10, 5, 6, 2]
    ]) == True, "Third"
    assert checkio([
        [6, 6, 7, 7, 7],
        [1, 7, 3, 6, 5],
        [4, 1, 2, 3, 2],
        [9, 0, 4, 0, 5],
        [2, 0, 7, 5, 10]
    ]) == False, "fourth"
    assert checkio([
        [1,  1, 1,  6, 1, 1, 1],
        [2,  5, 4,  2, 2, 7, 2],
        [2,  6, 1,  2, 6, 4, 3],
        [3,  2, 2,  1, 0, 2, 4],
        [7,  9, 6,  2, 5, 7, 5],
        [7,  3, 10, 5, 6, 2, 5],
        [7,  3, 10, 5, 6, 2, 5]
    ]) == False, "Fifth"
    assert checkio([
        [1, 1, 3, 1],
        [1, 2, 3, 4],
        [5, 4, 3, 1],
        [6, 1, 3, 2]
    ]) == True, "Six, vertircal"
