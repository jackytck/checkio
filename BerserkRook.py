#!/opt/local/bin/python3.3
def berserk_rook(berserker, enemies):
    bx, by = ord(berserker[0]), int(berserker[1])

    def see(dx, dy):
        x, y = bx, by
        for i in range(8):
            x += dx
            y += dy
            t = chr(x) + str(y)
            if t in enemies:
                return [t]
        return []

    attack = see(0, -1) + see(0, 1) + see(-1, 0) + see(1, 0)
    ret = 0
    for a in attack:
        enemies.remove(a)
        ret = max(1 + berserk_rook(a, enemies), ret)
        enemies.add(a)
    return ret

if __name__ == '__main__':
    assert berserk_rook('d3', {'d6', 'b6', 'c8', 'g4', 'b8', 'g6'}) == 5, "one path"
    assert berserk_rook('a2', {'f6', 'f2', 'a6', 'f8', 'h8', 'h6'}) == 6, "several paths"
    assert berserk_rook('a2', {'f6', 'f8', 'f2', 'a6', 'h6'}) == 4, "Don't jump through"
