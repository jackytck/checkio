#!/opt/local/bin/python3.3
from datetime import date


def days_diff(date1, date2):
    return abs((date(*date1) - date(*date2)).days)

if __name__ == '__main__':
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
