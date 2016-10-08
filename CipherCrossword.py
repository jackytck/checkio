#!/usr/bin/python
from itertools import permutations

def trans(m):
    return map(list, zip(*m))

def valid(nums, words, p):
    d1, d2 = {0: ' '}, {}
    for i, num in enumerate(nums):
        w = words[p[i]]
        for j, x in enumerate(num):
            y = w[j]
            dw = d1.get(x, False)
            if dw and dw != y:
                return False, None
            wd = d2.get(y, False)
            if wd and wd != x:
                return False, None
            d1[x], d2[y] = y, x
    return True, d1

def checkio(crossword, words):
    nums = crossword[::2]
    nums.extend(trans(crossword)[::2])
    bind = {}
    for p in permutations(range(6)):
        v, d = valid(nums, words, p)
        if v:
            bind = d
            break
    return [[bind[x] for x in y] for y in crossword]

if __name__ == '__main__':
    assert checkio(
        [
            [21, 6, 25, 25, 17],
            [14, 0, 6, 0, 2],
            [1, 11, 16, 1, 17],
            [11, 0, 16, 0, 5],
            [26, 3, 14, 20, 6]
        ],
        ['hello', 'habit', 'lemma', 'ozone', 'bimbo', 'trace']
    ) == [['h', 'e', 'l', 'l', 'o'],
          ['a', ' ', 'e', ' ', 'z'],
          ['b', 'i', 'm', 'b', 'o'],
          ['i', ' ', 'm', ' ', 'n'],
          ['t', 'r', 'a', 'c', 'e']]
