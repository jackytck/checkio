#!/opt/local/bin/python3.3
def safe_pawns(pawns):
    COL = '#abcdefgh#'
    safe = set()
    for c, r in pawns:
        r = int(r) + 1
        c = COL.index(c)
        safe.add('%s%d' % (COL[c - 1], r))
        safe.add('%s%d' % (COL[c + 1], r))
    return sum(1 for p in pawns if p in safe)

if __name__ == '__main__':
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
