#!/usr/bin/python
def checkio(data):
    A, B, C, N = data
    ret = 0
    for i in range(A + 1):
        for j in range(B + 1):
            for k in range(C + 1):
                if i + j + k <= N:
                    ret += 1
    return ret

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([3, 2, 1, 4]) == 20, "First example"
    assert checkio([1, 1, 1, 1]) == 4, "Second example"
