#!/usr/bin/python
def checkio(expression):
    'transform the expression'
    order = {'(': 3, '^': 2, '%': 2, '*': 1, '/': 1, '+': 0, '-': 0}
    stack = []
    ret = ''
    for e in expression:
        if e.isalpha():
            ret += e
        else:
            if e == ')':
                while stack:
                    t = stack[-1]
                    if t == '(':
                        stack.pop()
                        break
                    ret += t
                    stack.pop()
            else:
                if len(stack) == 0:
                    stack.append(e)
                else:
                    while stack:
                        t = stack[-1]
                        if t == '(':
                            break
                        if order.get(t, 0) >= order.get(e, 0):
                            ret += t
                            stack.pop()
                        else:
                            break
                    stack.append(e)
    return ret + ''.join(reversed(stack))

if __name__ == '__main__':
    assert checkio('a+b') == 'ab+', 'First'
    assert checkio('((a+b)*(z+x))') == 'ab+zx+*', 'Second'
    assert checkio('((a+t)*((b+(a+c))^(c+d)))') == 'at+bac++cd+^*', 'Third'
    assert checkio('a+b*c+d') == 'abc*+d+' , 'Fourth'
    print 'All ok'
