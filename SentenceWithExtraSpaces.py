#!/usr/bin/python
#def checkio(string):
#    'return sentence without extra spaces'
#    return ' '.join(string.split())
#
#    
#if __name__ == '__main__':
#    assert checkio('I  like   python') == "I like python", 'First'
#    print 'All ok'

def checkio(line):
    return '-'.join([x for x in line.split('-') if x])

#These "asserts" using only for self-checking and not necessary for auto-testing    
if __name__ == '__main__':
    assert checkio(u'I---like--python') == "I-like-python", 'Example'
