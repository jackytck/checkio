#!/opt/local/bin/python3.3
from fractions import gcd
from functools import reduce


def greatest_common_divisor(*args):
    return reduce(gcd, args)

if __name__ == '__main__':
    assert greatest_common_divisor(6, 4) == 2, "Simple"
    assert greatest_common_divisor(2, 4, 8) == 2, "Three arguments"
    assert greatest_common_divisor(2, 3, 5, 7, 11) == 1, "Prime numbers"
    assert greatest_common_divisor(3, 9, 3, 9) == 3, "Repeating arguments"
