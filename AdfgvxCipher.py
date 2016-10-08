#!/opt/local/bin/python3.3
from collections import defaultdict
CT = 'ADFGVX'


def permute(keyword, size):
    k = ''
    for c in keyword:
        if c not in k:
            k += c
    d = defaultdict(list)
    s = len(k)
    for i in range(size):
        d[k[i % s]].append(i)
    return sum((d[x] for x in sorted(d.keys())), [])


def encode(message, secret, keyword):
    msg = [x.lower() for x in message if x.isalnum()]
    frac = ''.join(CT[x] for m in msg for x in divmod(secret.index(m), 6))
    perm = permute(keyword, len(frac))
    return ''.join(frac[p] for p in perm)


def decode(message, secret, keyword):
    size = len(message)
    perm = permute(keyword, size)
    frac = ''.join(message[perm.index(i)] for i in range(size))
    return ''.join(secret[6 * CT.index(x) + CT.index(y)]
                   for x, y in zip(frac[::2], frac[1::2]))


if __name__ == '__main__':
    assert encode("I am going",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "cipher") == 'FXGAFVXXAXDDDXGA', "encode I am going"
    assert decode("FXGAFVXXAXDDDXGA",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "cipher") == 'iamgoing', "decode I am going"
    assert encode("attack at 12:00 am",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "privacy") == 'DGDDDAGDDGAFADDFDADVDVFAADVX', "encode attack"
    assert decode("DGDDDAGDDGAFADDFDADVDVFAADVX",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "privacy") == 'attackat1200am', "decode attack"
    assert encode("ditiszeergeheim",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "piloten") == 'DFGGXXAAXGAFXGAFXXXGFFXFADDXGA', "encode ditiszeergeheim"
    assert decode("DFGGXXAAXGAFXGAFXXXGFFXFADDXGA",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "piloten") == 'ditiszeergeheim', "decode ditiszeergeheim"
    assert encode("I am going",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "weasel") == 'DXGAXAAXXVDDFGFX', "encode weasel == weasl"
    assert decode("DXGAXAAXXVDDFGFX",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "weasel") == 'iamgoing', "decode weasel == weasl"
