#!/usr/bin/python
from collections import deque

def move(a, b):
    b += a[-1]
    a = a[:-1]
    return a, b

def is_counter(seq, i, j):
    if seq and seq.split(',')[-1] == '%d%d' % (j, i):
        return True
    return False

def progress(s, goal):
    ret = -1
    for i, c in enumerate(s):
        if c == goal[i]:
            ret = i
        else:
            break
    return ret

def checkio(data):
    start, goal = data.split('-')
    q = deque()
    q.append((['', start[:-1], start[-1]], '12'))
    q.append(([start[-1], start[:-1], ''], '10'))
    p = -1
    while q:
        stack, seq = q.popleft()
        if stack[2] == goal:
            return seq

        p2 = progress(stack[2], goal)
        if p2 < p:
            continue
        else:
            p = p2

        want = goal[p2 + 1]
        if stack[0] and stack[0][-1] == want and len(stack[2]) == p + 1:
            q.append((['', stack[1], stack[2] + stack[0]], seq + ',02'))
            continue
        if stack[1] and stack[1][-1] == want and len(stack[2]) == p + 1:
            q.append(([stack[0], stack[1][:-1], stack[2] + stack[1][-1]], seq + ',12'))
            continue

        for i in range(3):
            for j in range(3):
                if i != j:
                    if stack[i] and (j != 0 or (j == 0 and stack[0] == '')) and not is_counter(seq, i, j):
                        nex = [x for x in stack]
                        nex[i], nex[j] = move(stack[i], stack[j])
                        q.append((nex, '%s,%d%d' % (seq, i, j)))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("rice-cire") == "10,12,12,12,02", "rice-cire"
    assert checkio("mirror-mirorr") == "12,12,10,12,12,02,10,21,21,21,21,21,02,12,12,12,10,21,21,21,02,12,12,12,12", "mirror-mirorr"
