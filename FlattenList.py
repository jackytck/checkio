#!/opt/local/bin/python3.3
def flat_list(a):
    r = []
    [r.extend(flat_list(i)) if isinstance(i, list) else r.append(i) for i in a]
    return r

if __name__ == '__main__':
    assert flat_list([1, 2, 3]) == [1, 2, 3], 'First'
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], 'Second'
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]])\
        == [2, 4, 5, 6, 6, 6, 6, 6, 7], 'Third'
