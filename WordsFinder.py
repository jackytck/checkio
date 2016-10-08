#!/opt/local/bin/python3.3
import re
import bisect


TAG = 'span'


def addTag(text, pos, offset):
    a, b = pos[0]+offset, pos[1]+1+offset
    return '{}<{}>{}</{}>{}'.format(text[:a], TAG, text[a:b], TAG, text[b:])


def checkio(text, words):
    largest, match, last = [], [], -1
    [[bisect.insort(match, (x.start(), x.start()+len(w)-1)) for x in
        re.finditer('(?={})'.format(re.escape(w)), text.lower())] for w in
        words.lower().split()]
    for a, b in match:
        if a > last:
            largest.append([a, b])
            last = b
        elif b > last:
            largest[-1][1] = last = b
    for i, pos in enumerate(largest):
        text = addTag(text, pos, i*(2*(len(TAG)+2)+1))
    return text

if __name__ == '__main__':
    assert (checkio("This is only a text example for task example.", "example") ==
            "This is only a text <span>example</span> for task <span>example</span>."), "Simple test"

    assert (checkio("Python is a widely used high-level programming language.", "pyThoN") ==
            "<span>Python</span> is a widely used high-level programming language."), "Ignore letters cases, but keep original"

    assert (checkio("It is experiment for control groups with similar distributions.", "is im") ==
            "It <span>is</span> exper<span>im</span>ent for control groups with s<span>im</span>ilar d<span>is</span>tributions."), "Several subwords"

    assert (checkio("The National Aeronautics and Space Administration (NASA).", "nasa  THE") ==
            "<span>The</span> National Aeronautics and Space Administration (<span>NASA</span>)."), "two spaces"

    assert (checkio("Did you find anything?", "word space tree") ==
            "Did you find anything?"), "No comments"

    assert (checkio("Hello World! Or LOL", "hell world or lo") ==
            "<span>Hello</span> <span>World</span>! <span>Or</span> <span>LO</span>L"), "Contain or intersect"
    assert (checkio('aaaa', 'a aa') == '<span>aaaa</span>')
