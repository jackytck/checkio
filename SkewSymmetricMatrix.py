#!/usr/bin/python
def checkio(matr):
    'return whether the specified square matrix is skew-symmetric or not'
    AT = map(list, zip(*matr))
    return matr == [[-x for x in y] for y in AT]

if __name__ == '__main__':
    assert checkio([[0, 1,2],
             [-1,0,1],
             [-2,-1,0]]) == True, 'First'
    assert checkio([[0, 1,2],
             [-1,1,1],
             [-2,-1,0]]) == False, 'Second'
    assert checkio([[0, 1,2],
             [-1,0,1],
             [-3,-1,0]]) == False, 'Third'
    print 'All ok'
