#!/usr/bin/python
def price(c):
    if c == '.':
        return 1
    elif c == ',':
        return 2
    elif c == '!':
        return 3
    elif c == ' ':
        return 1
    return (ord(c) - ord('a')) % 3 + 1

def checkio(line):
    '''
    Output a single number representing the cost of the given slogan, according to Petr's pricing.
    '''
    return sum(map(price, line))

if __name__ == '__main__':
    assert checkio('diamonds are forever') == 38, 'First'
    assert checkio('just do it') == 18, 'Second'
    assert checkio('tastes great, less filling') == 48, 'Third'
    print 'All is ok'
