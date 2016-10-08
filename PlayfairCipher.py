#!/opt/local/bin/python3.3
import string


def digraph(message):
    ret = []
    m = [x.lower() for x in message if x.isalnum()][::-1]
    while m:
        a, b = m.pop(), m.pop() if m else 'z' if a != 'z' else 'x'
        if a != b:
            ret.append(a + b)
        else:
            ret.append(a + ('x' if a != 'x' else 'z'))
            m.append(b)
    return ret


def key_table(key):
    s = key + string.ascii_lowercase + string.digits
    t = ''
    for c in s:
        if c not in t:
            t += c
    return t


def idx2pair(idx):
    return divmod(idx, 6)


def pair2idx(x, y):
    return 6 * x + y


def master(message, key, mode):
    ret = ''
    d = digraph(message)
    k = key_table(key)
    for a, b in d:
        x1, y1 = idx2pair(k.index(a))
        x2, y2 = idx2pair(k.index(b))
        if x1 == x2:
            y1 = (y1 + mode) % 6
            y2 = (y2 + mode) % 6
        elif y1 == y2:
            x1 = (x1 + mode) % 6
            x2 = (x2 + mode) % 6
        else:
            y1, y2 = y2, y1
        ret += k[pair2idx(x1, y1)]
        ret += k[pair2idx(x2, y2)]
    return ret


def encode(message, key):
    return master(message, key, 1)


def decode(secret_message, key):
    return master(secret_message, key, -1)


if __name__ == '__main__':
    assert encode("Fizz Buzz is x89 XX.", "checkio101") == 'do2y7mt22kry94y2y2', "Encode fizz buzz"
    assert decode("do2y7mt22kry94y2y2", "checkio101") == 'fizxzbuzzisx89xzxz', "Decode fizz buzz"
    assert encode("How are you?", "hello") == 'ea2imb1ht0', "Encode How are you"
    assert decode("ea2imb1ht0", "hello") == 'howareyouz', "Decode How are you"
    assert encode("My name is Alex!!!", "alexander") == 'i1dlkxjqlexn', "Encode Alex"
    assert decode("i1dlkxjqlexn", "alexander") == 'mynameisalex', "Decode Alex"
    assert encode("Who are you?", "human") == 'rnvftc1jd5', "Encode WHo"
    assert decode("rnvftc1jd5", "human") == 'whoareyouz', "Decode Who"
    assert encode("ATTACK AT DAWN", "general") == 'ewwektewhnua', "Encode attack"
    assert decode("ewwektewhnua", "general") == 'attackatdawn', "Decode attack"
