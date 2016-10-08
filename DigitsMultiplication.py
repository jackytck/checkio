#!/opt/local/bin/python3.3
def checkio(number):
    return checkio(number // 10) * max(number % 10, 1) if number else 1

if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
