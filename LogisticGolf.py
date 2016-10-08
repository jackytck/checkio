#!/opt/local/bin/python3.3
from itertools import *;c=9**9
def golf(m):
 d=[[y if y else c for y in x] for x in m]
 for k,i,j in product(*[range(len(m))]*3):d[i][j]=min(d[i][j],d[i][k]+d[k][j]);v=d[0][-1]
 return v if v!=c else 0

if __name__ == '__main__':
    assert golf(((0, 80, 58, 0), (80, 0, 71, 80), (58, 71, 0, 58), (0, 80, 58, 0))) == 116, 'first'
    assert golf(((0,57,42,0,14,0),(57,0,71,0,0,0),(42,71,0,51,0,0),(0,0,51,0,42,0),(14,0,0,42,0,0),(0,0,0,0,0,0))) == 0
