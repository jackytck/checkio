#!/opt/local/bin/python3.3
def extract(m):
    return [(i // 4, i % 4) for i, x in enumerate(''.join(m)) if x == 'X']


def rotate(m):
    return sorted([(j, 3 - i) for i, j in m])


def conv(m, c):
    return ''.join(c[i][j] for i, j in m)


def recall_password(cipher_grille, ciphered_password):
    ret = ''
    mask = extract(cipher_grille)
    for i in range(4):
        ret += conv(mask, ciphered_password)
        mask = rotate(mask)
    return ret


if __name__ == '__main__':
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
