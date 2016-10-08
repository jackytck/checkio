#!/opt/local/bin/python3.3
def boolean(x, y, operation):
    if operation == 'conjunction':
        return x & y
    if operation == 'disjunction':
        return x | y
    if operation == 'implication':
        return (not x) | y
    if operation == 'exclusive':
        return x ^ y
    if operation == 'equivalence':
        return x == y

if __name__ == '__main__':
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"
