#!/usr/bin/python
def checkio(arr):
    'unsual way of finding zero in this array'
    ret = 0
    try:
        for i in arr:
            ret += i / i
    except ZeroDivisionError:
        return ret
    
if __name__ == '__main__':
    assert checkio([1,1,0,3]) == 2, 'First'
    assert checkio([1,0,1]) == 1, 'Second'
    print 'All ok :)'
