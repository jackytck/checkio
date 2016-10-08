#!/usr/bin/python
import re

VOWELS = 'AEIOUY'
PUNCTUATION = ',.:;?!'

def isStriped(w):
    ret = False
    s = len(w)
    if s > 1 and not re.search('\d+', w):
        w = ''.join(['1' if x.upper() in VOWELS else '0' for x in w])
        if w == ('01' * s)[:s] or w == ('10' * s)[:s]:
            ret = True
    return ret

def checkio(text):
    tokens = re.split('[ %s]' % PUNCTUATION, text)
    return sum([isStriped(x) for x in tokens])

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"My name is ...") == 3, "All words are striped"
    assert checkio(u"Hello world") == 0, "No one"
    assert checkio(u"A quantity of striped words.") == 1, "Only of"
    assert checkio(u"Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
