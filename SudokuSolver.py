#!/usr/bin/python
import copy

def sub_block(data, x, y):
    ret = []
    for i in range(x/3*3, x/3*3+3):
        for j in range(y/3*3, y/3*3+3):
            ret.append(data[i][j])
    return ret

def complement(l):
    return [x for x in range(1, 10) if x not in l]

def candiate(data, x, y):
    row = complement(data[x])
    col = complement(map(list, zip(*data))[y])
    block = complement(sub_block(data, x, y))
    return list(set(row) & set(col) & set(block))

def next_hole(data):
    l = len(data)
    for i in range(l):
        for j in range(l):
            if data[i][j] == 0:
                return i, j
    return None, None

def checkio(grid):
    x, y = next_hole(grid)
    if x != None:
        for c in candiate(grid, x, y):
            other = copy.deepcopy(grid)
            other[x][y] = c
            d = checkio(other)
            if d:
                return d
    else:
        return grid

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[0, 7, 1, 6, 8, 4, 0, 0, 0], 
                    [0, 4, 9, 7, 0, 0, 0, 0, 0], 
                    [5, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 8, 0, 0, 0, 0, 5, 0, 4], 
                    [0, 0, 0, 3, 0, 7, 0, 0, 0], 
                    [2, 0, 3, 0, 0, 0, 0, 9, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0, 9], 
                    [0, 0, 0, 0, 0, 3, 7, 2, 0], 
                    [0, 0, 0, 4, 9, 8, 6, 1, 0]]) == [[3, 7, 1, 6, 8, 4, 9, 5, 2], 
                                                      [8, 4, 9, 7, 2, 5, 3, 6, 1], 
                                                      [5, 6, 2, 9, 3, 1, 4, 7, 8], 
                                                      [6, 8, 7, 2, 1, 9, 5, 3, 4], 
                                                      [9, 1, 4, 3, 5, 7, 2, 8, 6], 
                                                      [2, 5, 3, 8, 4, 6, 1, 9, 7], 
                                                      [1, 3, 6, 5, 7, 2, 8, 4, 9], 
                                                      [4, 9, 8, 1, 6, 3, 7, 2, 5], 
                                                      [7, 2, 5, 4, 9, 8, 6, 1, 3]], "first"
    assert checkio([[5, 0, 0, 7, 1, 9, 0, 0, 4], 
                    [0, 0, 1, 0, 3, 0, 5, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 8, 5, 9, 7, 2, 6, 4, 0], 
                    [0, 0, 0, 6, 0, 1, 0, 0, 0], 
                    [0, 2, 6, 3, 8, 5, 9, 1, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 3, 0, 5, 0, 2, 0, 0], 
                    [8, 0, 0, 4, 9, 7, 0, 0, 6]]) == [[5, 6, 8, 7, 1, 9, 3, 2, 4], 
                                                      [9, 7, 1, 2, 3, 4, 5, 6, 8], 
                                                      [2, 3, 4, 5, 6, 8, 7, 9, 1], 
                                                      [1, 8, 5, 9, 7, 2, 6, 4, 3], 
                                                      [3, 9, 7, 6, 4, 1, 8, 5, 2], 
                                                      [4, 2, 6, 3, 8, 5, 9, 1, 7], 
                                                      [6, 1, 9, 8, 2, 3, 4, 7, 5], 
                                                      [7, 4, 3, 1, 5, 6, 2, 8, 9], 
                                                      [8, 5, 2, 4, 9, 7, 1, 3, 6]], "second"
    print('Done')
