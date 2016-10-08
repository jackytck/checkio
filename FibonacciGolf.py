#!/opt/local/bin/python3.3
def fibgolf(t, n):

    def q(c, d, f, b=1, e=1, a=0):
        for i in range(n):
            a, b, c = b, c, d * a + e * b + f * c
        return a

    t = t[0] + t[2]
    if t == 'fb':
        return q(1, 0, 1)
    if t == 'ti':
        return q(1, 1, 1)
    if t == 'lc':
        return q(3, 0, 1, 1, 1)
    if t == 'jc':
        return q(1, 0, 1, 1, 2)
    if t == 'pl':
        return q(2, 0, 2)
    if t == 'pr':
        return q(2, 1, 0, 0, 1, 3)
    if t == 'pd':
        return q(1, 1, 0)


if __name__ == '__main__':
    assert fibgolf('fibonacci', 10) == 55
    assert fibgolf('tribonacci', 10) == 149
    assert fibgolf('lucas', 10) == 123
    assert fibgolf('jacobsthal', 10) == 341
    assert fibgolf('pell', 10) == 2378
    assert fibgolf('perrin', 10) == 17
    assert fibgolf('padovan', 10) == 9
