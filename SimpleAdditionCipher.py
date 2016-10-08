#!/usr/bin/python
orda, ords = ord('a'), ord(' ')

def decrypt(data, key):
    ds, ks = len(data), len(key)
    data = [(ord(x) - orda + 1)%(orda - ords - 1) for x in data]
    mask = key * (ds / ks)
    mask.extend(key[:ds % ks])
    diff = [(a - b)%27 for a, b in zip(data, mask)]
    ret = [chr(x + orda - 1) if x != 0 else ' ' for x in diff]
    return ''.join(ret)

def checkio(data):
    old_encrypted, old_decrypted, new_encrypted = data
    oe = [(ord(x) - orda + 1)%(orda - ords - 1) for x in old_encrypted]
    od = [(ord(x) - orda + 1)%(orda - ords - 1) for x in old_decrypted]
    diff = [(a - b)%27 for a, b in zip(oe, od)]
    size = len(old_encrypted)

    for i in range(1, len(diff)+1):
        key = diff[:i]
        pack = key * (size / i)
        pack.extend(key[:size % i])
        if pack == diff:
            return decrypt(new_encrypted, key)
    return ''

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(
        [
            'lmljemxbwrhhfyd stlmhrxyvwhk',
            'this text contain the secret',
            'tsgryaaxckjqledcxhshreyuasckmysxhuwyl'
        ]) == 'and this text also contain the secret', 'Secret'
    assert checkio(
        [
            'pjxxchnedonncdhhrqdgilq',
            'hello its first message',
            'pjxxchnedo jo bleyqg fsq'
        ]) == 'hello its second message', "Hello"
    assert checkio(
        [
            'dxb dxb dxb dxb',
            'bla bla bla bla',
            'tqblbefxv'
        ]) == 'real text', "Bla Bla Bla"
    assert checkio(
        [
            'dtqyefpxqtlh',
            'long message',
            'kmriy'
        ]) == 'short', "Short"
    assert checkio(
        [
            'vjwclkjfijm',
            'keyofsecret',
            'lpcmuyxhuwyd'
        ]) == 'akeyofsecret', "Almost"
