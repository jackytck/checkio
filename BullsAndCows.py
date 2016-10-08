#!/usr/bin/python
import itertools

def valid(t, d):
    b, c = 0, 0
    guess, bullcow = d.split(' ')
    for i, g in enumerate(guess):
        if t[i] == int(g):
            b += 1
        elif int(g) in t:
            c += 1
    return '%dB%dC' % (b, c) == bullcow

def checkio(data):
    if len(data) == 1:
        return '4567'
    for t in itertools.permutations(range(10), 4):
        found = True
        for d in data:
            if not valid(t, d):
                found = False
                break
        if found:
            return '%d%d%d%d' % t

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print(checkio([]))
    #print(checkio(["0123 1B1C"]))
    #5901
    #print(checkio(['0123 0B2C']))
    #print(checkio(['0123 0B2C', '4567 0B1C']))
    #print(checkio(['0123 0B2C', '4567 0B1C', '1048 0B2C']))
    #print(checkio(['0123 0B2C', '4567 0B1C', '1048 0B2C', '2384 0B0C']))
