#!/opt/local/bin/python3.3
def decode_amsco(message, key):
    n = len(message)
    w = len(str(key))
    h = int(n / w)
    p = 0

    m = [[[] for i in range(w)] for j in range(h)]
    for i, x in enumerate(m):
        for j, y in enumerate(x):
            if p >= n:
                break
            m[i][j].append(p)
            p += 1
            if (i + j) & 1 and p < n:
                m[i][j].append(p)
                p += 1
    m = list(map(list, zip(*m)))

    permute = []
    for i in range(w):
        j = str(key).index(str(i + 1))
        permute.append(m[j])
    permute = sum(sum(permute, []), [])

    return ''.join(message[permute.index(x)] for x in range(n))

if __name__ == '__main__':
    assert decode_amsco("oruoreemdstmioitlpslam", 4123) == "loremipsumdolorsitamet", "Lorem Ipsum"
    assert decode_amsco('kicheco', 23415) == "checkio", "Checkio"
    assert decode_amsco('hrewhoorrowyilmmmoaouletow', 123) == "howareyouwillhometommorrow", "How are you"
