#!/opt/local/bin/python3.3
from math import log


def super_root(number, trial=10):
    x, d = 1, log(number)
    for i in range(trial):
        x = (x + d) / (1 + log(x))
    return x

if __name__ == '__main__':
    def check_result(function, number):
        result = function(number)
        if not isinstance(result, (int, float)):
            print("The result should be a float or an integer.")
            return False
        p = result ** result
        if number - 0.001 < p < number + 0.001:
            return True
        return False
    assert check_result(super_root, 4), "Square"
    assert check_result(super_root, 9), "Cube"
    assert check_result(super_root, 81), "Eighty one"
    assert check_result(super_root, 9999999999)
    assert check_result(super_root, 6753053087)
    assert check_result(super_root, 3599715496)
