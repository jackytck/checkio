#!/usr/bin/python
def checkio(stones):
    '''
    minimal possible weight difference between stone piles
    '''
    ks = {}
    N = len(stones)
    S = sum(stones)
    W = S / 2
    for w in range(W+1):
        ks[(0, w)] = 0
    for i in range(1, N+1):
        for w in range(W+1):
            if stones[i-1] <= w:
                ks[(i, w)] = max(ks[(i-1, w)], ks[(i-1, w-stones[i-1])] + stones[i-1])
            else:
                ks[(i, w)] = ks[(i-1, w)]
    return abs(S - ks[(N, W)] * 2)
    

if __name__ == '__main__':
    assert checkio([10,10]) == 0, 'First, with equal weights'
    assert checkio([10]) == 10, 'Second, with a single stone'
    assert checkio([5, 8, 13, 27, 14]) == 3, 'Third'
    assert checkio([5,5,6,5]) == 1, 'Fourth'
    assert checkio([12, 30, 30, 32, 42, 49]) == 9, 'Fifth'
    assert checkio([1, 1, 1, 3]) == 0, "Six, don't forget - you can hold different quantity of parts"
    print 'All is ok'
