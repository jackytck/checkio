#!/opt/local/bin/python3.3
from itertools import *
golf=lambda h:min(sum(abs(a-b) for a,b in zip(chain([0j],p),p)) for p in permutations(x+y*1j for x,y in h))

if __name__ == '__main__':
    assert round(golf({(2, 2), (2, 8), (8, 8), (8, 2), (5, 5)}), 2) == 23.31
    assert round(golf({(2, 2), (4, 4), (6, 6), (8, 8), (9, 9)}), 2) == 12.73
