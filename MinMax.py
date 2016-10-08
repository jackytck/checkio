#!/opt/local/bin/python3.3
def minmax(args, key, reverse):
    if len(args) == 1:
        args = args[0]
    return sorted(args, key=key, reverse=reverse)[0]


def min(*args, key=None):
    return minmax(args, key, False)


def max(*args, key=None):
    return minmax(args, key, True)


if __name__ == '__main__':
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
    assert min(abs(i) for i in range(-10, 10)) == 0
    assert max(x + 5 for x in range(6)) == 10
