#!/opt/local/bin/python3.3
VOWELS = 'aeiouy'


def translate(phrase):
    ret = ''
    skip = []
    for i, c in enumerate(phrase):
        if i in skip:
            skip.pop()
            continue
        if c in VOWELS:
            ret += c
            skip.append(i+2)
            skip.append(i+1)
        else:
            ret += c
            if c != ' ':
                skip.append(i+1)
    return ret

if __name__ == '__main__':
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
