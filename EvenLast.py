#!/opt/local/bin/python3.3
def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    return sum(array[::2]) * array[-1] if array else 0

if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "Empty"
