#!/opt/local/bin/python3.3
from itertools import zip_longest


def checkio(text, word):
    text = [x.replace(' ', '').lower() for x in text.split('\n')]
    word = word.lower()

    def search_horizontal(text):
        for i, t in enumerate(text, 1):
            col = t.find(word)
            if col != -1:
                return [i, col + 1, i, col + len(word)]

    h = search_horizontal(text)
    if h:
        return h
    text = map(''.join, zip_longest(*text, fillvalue=' '))
    v = search_horizontal(text)
    return [v[1], v[0], v[3], v[2]]


if __name__ == '__main__':
    assert checkio(u"""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", u"ten") == [2, 14, 2, 16]
    assert checkio(u"""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", u"noir") == [4, 16, 7, 16]
