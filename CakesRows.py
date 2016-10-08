#!/usr/bin/python
import itertools

#orientation of 3 points
def orient(p, q, r):
    px, py = p
    qx, qy = q
    rx, ry = r
    return qx * ry - qy * rx - (px * ry - py * rx) + px * qy - py * qx

#length square of 2 points
def len2(p, q):
    px, py = p
    qx, qy = q
    return (px - qx) ** 2 + (py - qy) ** 2

def checkio(cakes):
    cnt = 0
    n = len(cakes)
    segments = []
    ids = [set() for i in range(n)]
    
    #for each nC2 segment, find its length, and other points that are collinear to it
    for s in itertools.combinations(range(n), 2):
        p, q = cakes[s[0]], cakes[s[1]]
        collinear = []
        for i in range(n):
            if i not in s:
                r = cakes[i]
                if orient(p, q, r) == 0:
                    collinear.append(i)
        if collinear:
            segments.append((s, len2(p, q), collinear))

    #sort by length descendingly
    segments.sort(key = lambda x: x[1], reverse = True)

    #assign id(s) to each point, same id for the whole segment
    for s in segments:
        p_ids, q_ids = ids[s[0][0]], ids[s[0][1]]

        #ignore sub-segment
        if p_ids and q_ids and p_ids.intersection(q_ids):
            continue

        #found new segment
        p_ids.add(cnt)
        q_ids.add(cnt)
        for r in s[2]:
            ids[r].add(cnt)
        cnt += 1

    return cnt

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[3, 3], [5, 5], [8, 8], [2, 8], [8, 2]]) == 2
    assert checkio(
        [[2, 2], [2, 5], [2, 8], [5, 2], [7, 2], [8, 2],
         [9, 2], [4, 5], [4, 8], [7, 5], [5, 8], [9, 8]]) == 6
