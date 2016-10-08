#!/usr/bin/python
def conv(mask, chars):
    ret = ''
    for i, l in enumerate(mask):
        for j, c in enumerate(l):
            if c == 'X':
                ret += chars[i][j]
    return ret

def rotate(mask):
    ret = []
    h = len(mask) - 1
    for l in mask:
        a = ''
        for c in l:
            a += '.'
        ret.append(a)
    for i, l in enumerate(mask):
        for j, c in enumerate(l):
            if c == 'X':
                ret[j] = ret[j][:h-i] + 'X' + ret[j][h-i+1:]
    return ret

def checkio(input_data):
    'Return password of given cipher map'
    mask, chars = input_data[0], input_data[1]
    ret = ''
    for i in range(4):
        ret += conv(mask, chars)
        mask = rotate(mask)
    return ret

if __name__ == '__main__':
    assert checkio([[
    'X...',
    '..X.',
    'X..X',
    '....'],[
    'itdf',
    'gdce',
    'aton',
    'qrdi']]) == 'icantforgetiddqd', 'First'

    assert checkio( [[
    '....',
    'X..X',
    '.X..',
    '...X'],[
    'xhwc',
    'rsqx',
    'xqzz',
    'fyzr']]) == 'rxqrwsfzxqxzhczy', 'Second'
    print('All ok')
