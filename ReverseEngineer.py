#!/opt/local/bin/python3.3
from collections import deque
from random import randint

BOUND = 1000000
ERROR = 0.000001
QUERY = (-1000, 1000)

def verify(f, step):
    x, y, r = step
    if isinstance(r, list):
        r = r[0] / r[1]
    f = f.replace('x', str(x)).replace('y', str(y))
    ret = False
    try:
        res = eval(f)
        if abs(res - r) < ERROR:
            ret = True
    except ZeroDivisionError:
        ret = 'ZeroDivisionError' == r
    except SyntaxError:
        pass
    return ret

def checkio(steps):
    if not steps:
        return ['x+y', 1, -1]

    type1 = ('+', '-', '*', '/', ')')
    type2 = ('x', 'y', '(')
    childs = {'x': type1, 'y': type1, '+': type2, '-': type2, '*': type2, '/': type2, '(': type2, ')': type1}

    q = deque([('x', 'x'), ('(', '('), ('y', 'y')])
    cnt = 0
    while q and cnt < BOUND:
        f, t = q.popleft()
        cnt += 1
        valid = True
        for step in steps:
            if not verify(f, step):
                valid = False
                break
        if valid:
            return [f, randint(*QUERY), randint(*QUERY)]
        for c in childs[t]:
            if c == ')' and f.count('(') <= f.count(')'):
                continue
            q.append((f + c, c))
    
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print(checkio([]))
    print(checkio([[5, 7, [12, 1]]]))
    print(checkio([[5, 7, [12, 1]], [1, 2, [3, 1]]]))
