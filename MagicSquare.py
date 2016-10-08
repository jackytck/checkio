#!/usr/bin/python
import copy

SUM = (15, 34, 65)

def candidate(data):
    used = []
    for r in data:
        used.extend(r)
    return [x for x in range(1, len(data)**2 + 1) if x not in used]

def fill_trivial(data):
    dirty = False
    l = len(data)
    c = SUM[l - 3]
    #rows
    for i in range(l):
        zero, zp = 0, None
        for j in range(l):
            if data[i][j] == 0:
                zero += 1
                zp = j
                if zero > 1:
                    break
        if zero == 1:
            x = c - sum(data[i])
            data[i][zp] = x
            if x != 0:
                dirty = True
    #cols
    for i in range(l):
        zero, zp, s = 0, None, 0
        for j in range(l):
            if data[j][i] == 0:
                zero += 1
                zp = j
                if zero > 1:
                    break
            s += data[j][i]
        if zero == 1:
            x = c - s
            data[zp][i] = x
            if x != 0:
                dirty = True
    #diag1
    zero, zp, s = 0, None, 0
    for i in range(l):
        if data[i][i] == 0:
            zero += 1
            zp = i
            if zero > 1:
                break
        s += data[i][i]
    if zero == 1:
        x = c - s
        data[zp][zp] = x
        if x != 0:
            dirty = True
    #diag2
    zero, zp, s = 0, None, 0
    for i in range(l):
        if data[i][l-i-1] == 0:
            zero += 1
            zp = i
            if zero > 1:
                break
        s += data[i][l-i-1]
    if zero == 1:
        x = c - s
        data[zp][l-zp-1] = x
        if x != 0:
            dirty = True
    return dirty

def is_valid(data):
    l = len(data)
    c = SUM[l - 3]
    t = l**2 + 1
    while fill_trivial(data):
        pass
    #out of bound
    for row in data:
        for x in row:
            if x < 0 or x >= t:
                return False
    #duplicate
    d = [0] * t
    for row in data:
        for x in row:
            if x != 0:
                d[x] += 1
    if [x for x in d if x > 1]:
        return False
    #rows
    for r in data:
        if sum(r) > c:
            return False
    #cols
    for r in map(list, zip(*data)):
        if sum(r) > c:
            return False
    #diag1
    s, zero = 0, False
    for i in range(l):
        d = data[i][i]
        s += d
        if d == 0:
            zero = True
    if zero:
        if s > c:
            return False
    else:
        if s != c:
            return False
    #diag2
    s, zero = 0, False
    for i in range(l):
        d = data[i][l-i-1]
        s += d
        if d == 0:
            zero = True
    if zero:
        if s > c:
            return False
    else:
        if s != c:
            return False
    return True

def next_hole(data):
    l = len(data)
    for i in range(l):
        for j in range(l):
            if data[i][j] == 0:
                return i, j

def solve(data):
    hole = next_hole(data)
    if hole:
        for c in candidate(data):
            other = copy.deepcopy(data)
            other[hole[0]][hole[1]] = c
            if is_valid(other):
                done, d = solve(other)
                if done:
                    return True, d
        return False, None
    else:
        return True, data

def checkio(data):
    return solve(data)[1]
    
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':

    print(checkio([
        [2, 7, 6],
        [9, 5, 1],
        [4, 3, 0]
    ]))
    #must return [[2, 7, 6], [9, 5, 1], [4, 3, 8]]

    print(checkio([
        [0, 0, 0],
        [0, 5, 0],
        [0, 0, 0]
    ]))
    #can return [[2, 7, 6], [9, 5, 1], [4, 3, 8]] or
    # [[4, 9, 2], [3, 5, 7], [8, 1, 6]

    print(checkio([[1, 15, 14, 4],
                   [12, 0, 0, 9],
                   [8, 0, 0, 5],
                   [13, 3, 2, 16]]))
    # answer [[1, 15, 14, 4], [12, 6, 7, 9], [8, 10, 11, 5], [13, 3, 2, 16]]

    print(checkio([[0,7,0,16,0],[11,0,23,0,9],[0,4,0,15,0],[10,0,17,0,1],[0,21,0,8,0]]))
