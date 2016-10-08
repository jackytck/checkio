#!/opt/local/bin/python3.3
import itertools


def checkio(words_set):
    for w1, w2 in itertools.combinations(words_set, 2):
        if w1.endswith(w2) or w2.endswith(w1):
            return True
    return False

if __name__ == '__main__':
    assert checkio({"hello", "lo", "he"}) == True, "helLO"
    assert checkio({"hello", "la", "hellow", "cow"}) == False, "hellow la cow"
    assert checkio({"walk", "duckwalk"}) == True, "duck to walk"
    assert checkio({"one"}) == False, "Only One"
    assert checkio({"helicopter", "li", "he"}) == False, "Only end"
