#!/usr/bin/python
from collections import deque

def pour(j1, c1, j2, c2):
    if j1 + j2 > c2:
        j1, j2 = j1 - c2 + j2, c2
    else:
        j1, j2 = 0, j1 + j2
    return j1, j2 

def checkio(c1, c2, goal):
    q = deque([(c1, 0, '01'), (0, c2, '02')])
    while q:
        j1, j2, seq = q.popleft()
        if j1 == goal or j2 == goal:
            return seq.split(',')

        if j1 == c1 and j2 == 0:
            j1, j2 = pour(j1, c1, j2, c2)
            q.append((j1, j2, seq + ',12'))
        elif j1 == 0 and j2 == c2:
            j2, j1 = pour(j2, c2, j1, c1)
            q.append((j1, j2, seq + ',21'))
        elif j1 == c1 and j2 < c2:
            q.append((0, j2, seq + ',10'))
            j1, j2 = pour(j1, c1, j2, c2)
            q.append((j1, j2, seq + ',12'))
        elif j1 < c1 and j2 == c2:
            q.append((j1, 0, seq + ',20'))
            j2, j1 = pour(j2, c2, j1, c1)
            q.append((j1, j2, seq + ',21'))
        elif j1 == 0 and j2 < c2:
            q.append((c1, j2, seq + ',01'))
            j2, j1 = pour(j2, c2, j1, c1)
            q.append((j1, j2, seq + ',21'))
        elif j1 < c1 and j2 == 0:
            q.append((j1, c2, seq + ',02'))
            j1, j2 = pour(j1, c1, j2, c2)
            q.append((j1, j2, seq + ',12'))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print(checkio(5, 7, 6))  # ['02', '21', '10', '21', '02', '21', '10', '21', '02', '21']
    print(checkio(3, 4, 1))  # ["02", "21"]
