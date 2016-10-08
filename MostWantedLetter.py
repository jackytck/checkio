#!/usr/bin/python
def checkio(text):
    text = [x.lower() for x in text if x.isalpha()]
    c = [(len(text) - text.count(x), x) for x in text]
    c.sort()
    return c[0][1]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"Hello World!") == "l", "Hello test"
    assert checkio(u"How do you do?") == "o", "O is most wanted"
    assert checkio(u"One") == "e", "All letter only once."
