#!/usr/bin/python
def checkio(matr):
    'return a transposed matrix'
    r, c = len(matr), len(matr[0])
    ret = []
    for i in range(c):
        ret.append([0] * r)
    for i in range(c):
        for j in range(r):
            ret[i][j] = matr[j][i]
    return ret
    
if __name__ == '__main__':
    assert checkio([[1,2],
             [1,2]]) ==  [[1, 1],
                          [2, 2]], 'First'
    assert checkio([[1,0,3,4,0],
                    [2,0,4,5,6],
                    [3,4,9,0,6]]) == [[1, 2, 3],
                                      [0, 0, 4],
                                      [3, 4, 9],
                                      [4, 5, 0],
                                      [0, 6, 6]],'Second'
    print 'All ok'
