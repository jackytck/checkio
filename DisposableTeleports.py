#!/usr/bin/python
def child(a, e):
    return [x.replace(a, '') for x in e.split(',') if x.find(a) >= 0]

def remove(e, a, b):
    return ','.join([x for x in e.split(',') if x != a + b and x != b + a])

def is_done(route):
    return len(set(route)) == 8 and route[-1] == '1'

def checkio(teleports_string):
    stack = [('1', teleports_string)]
    visit = {}
    while stack:
        r, e = stack.pop()
        if is_done(r):
            return r
        if visit.get(r, False):
            continue
        visit[r] = True
        for c in child(r[-1], e):
            x = r + c
            y = remove(e, r[-1], c)
            stack.append((x, y))
    
if __name__ == "__main__":
    print(checkio("12,23,34,45,56,67,78,81")) #"123456781"
    print(checkio("12,28,87,71,13,14,34,35,45,46,63,65")) #"1365417821"
    print(checkio("12,15,16,23,24,28,83,85,86,87,71,74,56")) #"12382478561"
    print(checkio("13,14,23,25,34,35,47,56,58,76,68")) #"132586741"
    print checkio("12,23,34,45,56,67,78,81,17,28,88")
