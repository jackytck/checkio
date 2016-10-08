#!/usr/bin/python
def checkio(data):
    data.sort()
    s = len(data)
    if s % 2 == 0:
        return (data[s/2-1] + data[s/2]) / 2.0
    else:
        return data[s/2]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
