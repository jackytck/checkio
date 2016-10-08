#!/usr/bin/python
def det(m):
    a11, a12, a13 = m[0]
    a21, a22, a23 = m[1]
    a31, a32, a33 = m[2]
    return a11*a22*a33+a21*a32*a13+a31*a12*a23-a11*a32*a23-a31*a22*a13-a21*a12*a33

def inverse(m):
    a11, a12, a13 = m[0]
    a21, a22, a23 = m[1]
    a31, a32, a33 = m[2]
    d = float(det(m))
    return [[(a22*a33-a23*a32)/d, (a13*a32-a12*a33)/d, (a12*a23-a13*a22)/d], [(a23*a31-a21*a33)/d, (a11*a33-a13*a31)/d, (a13*a21-a11*a23)/d], [(a21*a32-a22*a31)/d, (a12*a31-a11*a32)/d, (a11*a22-a12*a21)/d]]

def dot(u, v):
    return sum(x * y for x, y in zip(u, v))

def mult(m, b):
    return [dot(x, b) for x in m]

def strip(s):
    for i in range(2):
        if s[-1] == '0':
            s = s[:-1]
    if s[-1] == '.':
        s = s[:-1]
    return s

def checkio(data):
    data = eval('[%s]' % data)
    m = []
    for d in data:
        m.append([d[0], d[1], 1])
    m = inverse(m)
    b = [-(x*x + y*y) for x, y in data]
    a = mult(m, b)
    cx, cy, r = 0.5 * a[0], 0.5 * a[1], ((a[0]*a[0]+a[1]*a[1])/4 - a[2]) ** 0.5
    sx, sy, sr = '%+.02f' % cx, '%+.02f' % cy, '%.02f' % r

    return '(x%s)^2+(y%s)^2=%s^2' % (strip(sx), strip(sy), strip(sr))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"
