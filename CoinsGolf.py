#!/opt/local/bin/python3.3
from itertools import *
r=range(92)
golf=lambda c:min(set(r)-set(sum(s) for i in r for s in combinations(c,i)))

if __name__ == '__main__':
    assert golf([10, 2, 2, 1]) == 6
    assert golf([1, 1, 1, 1]) == 5
    assert golf([1, 2, 3, 4, 5]) == 16
