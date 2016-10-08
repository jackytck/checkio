#!/opt/local/bin/python3.3
import itertools
from pprint import pprint

#def golf(b,t):
#    n=len(b);r=range(n)
#    for k,i,j in __import__('itertools').product(r,r,r):b[i][j]=(min(b[i][j],b[i][k]+b[k][j]) if b[i][j] else b[i][k]+b[k][j]) if i!=j and i!=k and k!=j and  b[i][k] and b[k][j] else b[i][j]
#    return sum(b[i][i] for i in r if b[0][i]<=t)

#def golf(b,t):
#    n=len(b);r=range(n);f=[[b[i][j] or 9**9 if i!=j else 0 for i in r] for j in r]
#    for k,i,j in __import__('itertools').product(r,r,r):f[i][j]=min(f[i][j],f[i][k]+f[k][j])
#    return sum(b[i][i] for i in r if f[0][i]<=t)

def golf(b,t):
    r=range(len(b))
    f=[[b[i][j] or abs(i-j)*9**9 for i in r] for j in r]
    for k in r:
        for i in r:
            for j in r:
                f[i][j]=min(f[i][j],f[i][k]+f[k][j])
    return sum(b[i][i] for i in r if f[0][i]<=t)

        #if i != j and i != k and k != j and  b[i][k] and b[k][j]:
if __name__ == '__main__':
    assert golf([[0, 40, 0, 40, 0, 0],
                 [40, 6, 0, 0, 40, 0],
                 [0, 0, 3, 0, 15, 0],
                 [40, 0, 0, 4, 40, 15],
                 [0, 40, 15, 40, 1, 0],
                 [0, 0, 0, 15, 0, 2]], 80) == 13
