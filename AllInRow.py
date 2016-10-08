#!/usr/bin/python
def checkio(arr):
    'convert all elements in arr in one row'
    ret = []
    for i in arr:
        if isinstance(i, list):
            ret.extend(checkio(i))
        else:
            ret.append(i)
    return ret

if __name__ == '__main__':
    assert checkio([1,2,3]) == [1,2,3], 'First'
    assert checkio([1,[2,2,2],4]) == [1,2,2,2,4], 'Second'
    assert checkio([[[2]],[4,[5,6,[6],6,6,6],7]])\
                              == [2,4,5,6,6,6,6,6,7], 'Third'
    print 'All ok'
