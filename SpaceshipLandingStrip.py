#!/usr/bin/python
def checkio(m):
    w, h = len(m[0]), len(m)

    def mask(sx, sy, pw, ph):
        if sx + pw <= w and sy + ph <= h:
            for i in range(pw):
                for j in range(ph):
                    p = m[sy + j][sx + i]
                    if p != 'G' and p != 'S':
                        return False
            return True
        else:
            return False

    def expand(sx, sy):
        w, h = 1, 1
        while mask(sx, sy, w, h):
            w += 1
        w -= 1
        while mask(sx, sy, w, h):
            h += 1
        h = max(1, h - 1)
        hori = w * h
        w, h = 1, 1
        while mask(sx, sy, w, h):
            h += 1
        h -= 1
        while mask(sx, sy, w, h):
            w += 1
        w = max(1, w - 1)
        return max(hori, w * h)

    ret = 0
    for y in range(h):
        for x in range(w):
            p = m[y][x]
            if p == 'G' or p == 'S':
                ret = max(ret, expand(x, y))
    return ret

if __name__ == '__main__':
    assert checkio(['G']) == 1, 'First'
    assert checkio(['GS','GS']) == 4, 'Second'
    assert checkio(['GT','GG']) == 2, 'Third'
    assert checkio(['GGTGG','TGGGG','GSSGT','GGGGT','GWGGG','RGTRT','RTGWT','WTWGR']) == 9, 'Fourth'
    print 'All is ok'
