#!/usr/bin/python
def checkio(params):
    '''
    params[0] is a matrix  NxN (5<=N<=10) and params[1] == [x1, y1], params[2] ==  [x2, y2] pairs,
    where x1, x2 are row numbers of two points in matrix, y1, y2 - col numbers. 
    Matrix  consists of zero and non-zero numbers. 
    Say, you can pass from one point to another if you can move hosrisontally and vertically through zeros and not intersect nonzeros. 
    Return True if there is a way from [x1, y1] to [x2, y2]. Return False, otherwise.
    '''
    matr, point1, point2 = params
    point1, point2 = [x-1 for x in point1], [x-1 for x in point2]
    stack = [point1]
    visited = [[False for x in y] for y in matr]
    dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
    while stack:
        top = stack.pop()
        if top == point2:
            return True
        visited[top[0]][top[1]] = True
        for d in dirs:
            try:
                p = [top[0]+d[0], top[1]+d[1]]
                if p[0] >= 0 and p[1] >= 0 and matr[p[0]][p[1]] == 0 and not visited[p[0]][p[1]]:
                    stack.append(p)
            except IndexError:
                continue
    return False
    
if __name__ == '__main__':
    assert checkio(([
        [0, 0, 5, 4, 0], 
        [0, 1, 5, 0, 0], 
        [0, 0, 0, 7, 2], 
        [8, 0, 0, 0, 0], 
        [0, 9, 0, 1, 0]], 
        [1,1], [5,3])) == True, 'First'
        
    assert checkio(([
        [0, 0, 5, 4, 0], 
        [0, 1, 5, 0, 0], 
        [0, 0, 0, 7, 2], 
        [8, 0, 0, 0, 0], 
        [0, 9, 0, 1, 0]], 
        [1,1], [1,5])) == False, 'Second'
    
    print 'All ok'
