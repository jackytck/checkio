#!/opt/local/bin/python3.3
def infer_key(encrypted, decrypted):
    diff = [(ord(e) - ord(d)) % 26 for e, d in zip(encrypted, decrypted)]
    size = len(diff)
    for i in range(1, size + 1):
        key = diff[:i]
        if key * (size // i) + key[:size % i] == diff:
            return key


def decrypt(msg, key):
    msg = [ord(x) - ord('A') for x in msg]
    q, r = divmod(len(msg), len(key))
    key = key * q + key[:r]
    return ''.join(chr((x - y) % 26 + ord('A')) for x, y in zip(msg, key))


def decode_vigenere(old_decrypted, old_encrypted, new_encrypted):
    return decrypt(new_encrypted, infer_key(old_encrypted, old_decrypted))


if __name__ == '__main__':
    assert decode_vigenere('DONTWORRYBEHAPPY',
                           'FVRVGWFTFFGRIDRF',
                           'DLLCZXMFVRVGWFTF') == "BEHAPPYDONTWORRY", "CHECKIO"
    assert decode_vigenere('HELLO', 'OIWWC', 'ICP') == "BYE", "HELLO"
    assert decode_vigenere('LOREMIPSUM',
                           'OCCSDQJEXA',
                           'OCCSDQJEXA') == "LOREMIPSUM", "DOLORIUM"
