#!/opt/local/bin/python3.3
def count_inversion(sequence):
    return sum(x > y for i, x in enumerate(sequence) for y in sequence[i+1:])

if __name__ == '__main__':
    assert count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3, "Example"
    assert count_inversion((0, 1, 2, 3)) == 0, "Sorted"
    assert count_inversion((99, -99)) == 1, "Two numbers"
    assert count_inversion((5, 3, 2, 1, 0)) == 10, "Reversed"
