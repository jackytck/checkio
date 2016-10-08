#!/usr/bin/python
FONT = ('-XX---X--XXX-XXX-X-X-XXX--XX-XXX-XXX--XX-',
        '-X-X-XX----X---X-X-X-X---X-----X-X-X-X-X-',
        '-X-X--X---XX--X--XXX-XX--XXX--X--XXX-XXX-',
        '-X-X--X--X-----X---X---X-X-X-X---X-X---X-',
        '--XX--X--XXX-XXX---X-XX---XX-X---XXX-XX--')
WIDTH = 3
SPACE = 1
ERROR = 1

#transpose
def trans(m):
    return map(list, zip(*m))

#transpose and cut into pieces
def cut(m):
    mt = trans(m)
    w, s, l = WIDTH, SPACE, len(mt)
    return [mt[s + (w + s) * i : (w + s) * (i + 1)] for i in range((l - s) / (w + s))]

#distance of individual input and FONT
def dist(a, b):
    return sum(x != '-X'.index(y) for x, y in zip(sum(a, []), sum(b, [])))

def checkio(image):
    ret = ''
    for p in cut(image):
        for i, f in enumerate(cut(FONT)):
            if dist(p, f) <= ERROR:
                ret += str(i)
                continue
    return int(ret)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
                    [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                    [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]) == 394, "394 clear"
    assert checkio([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0],
                    [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                    [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                    [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]) == 394, "again 394 but with noise"
