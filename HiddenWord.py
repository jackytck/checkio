#!/usr/bin/python
def checkio(text, word):
    text = [x.replace(' ', '') for x in text.split('\n')]

    #search horizontally
    def search(text):
        for i, t in enumerate(text):
            col = t.find(word)
            if col != -1:
                return [i + 1, col + 1, i + 1, col + len(word)]

    h = search(text)
    if h:
        return h

    #find max length of line, make text square, transpose
    m = 0
    for t in text:
        m = max(m, len(t))
    text = [x + ' ' * (m - len(x)) for x in text]
    text = map(''.join, zip(*text))

    v = search(text)
    return [v[1], v[0], v[3], v[2]]

#These "asserts" using only for self-checking and not necessary for auto-testing
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
