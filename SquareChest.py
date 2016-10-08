#!/usr/bin/python
def decode(s):
    s = [int(x) for x in s.split()]
    b = s[1:] + [s[0]]
    ret = [list(sorted(x)) for x in zip(b, s)]
    return ret

def side1():
    b = decode('1 2 6 5')
    ret = []
    for i in range(11):
        if i != 3 and i != 7:
            ret.append([[x + i for x in y] for y in b])
    return ret

def side2():
    b = decode('1 2 3 7 11 10 9 5')
    l = (0, 1, 4, 5)
    ret = []
    for i in l:
        ret.append([[x + i for x in y] for y in b])
    return ret

def side3():
    return [decode('1 2 3 4 8 12 16 15 14 13 9 5')]

def squares():
    return side1() + side2() + side3()

def checkio(lines_list):
    """Return the qantity of squares"""
    lines_list = [sorted(x) for x in lines_list]
    ret = 0
    for s in squares():
        add = 1
        for e in s:
            if e not in lines_list:
                add = 0
                break
        ret += add
    return ret

if __name__ == '__main__':
    assert (checkio([[1,2],[3,4],[1,5],[2,6],[4,8],[5,6],[6,7],
                     [7,8],[6,10],[7,11],[8,12],[10,11],
                     [10,14],[12,16],[14,15],[15,16]]) == 3) , "First, from description"
    assert (checkio([[1,2],[2,3],[3,4],[1,5],[4,8],
                     [6,7],[5,9],[6,10],[7,11],[8,12],
                     [9,13],[10,11],[12,16],[13,14],[14,15],[15,16]]) == 2), "Second, from description"
    assert (checkio([[1,2], [1,5], [2,6], [5,6]]) == 1), "Third, one small square"
    assert (checkio([[1,2], [1,5], [2,6], [5,9], [6,10], [9,10]]) == 0), "Fourth, it's not square"
    assert (checkio([[16,15], [16,12], [15,11], [11,10],
                     [10,14], [14,13], [13,9]]) == 0), "Fifth, snake"
