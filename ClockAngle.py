#!/opt/local/bin/python3.3
def clock_angle(time):
    h, m = (int(x) for x in time.split(':'))
    ang = abs((h % 12) * 30 - 5.5 * m)
    return min(ang, 360 - ang)

if __name__ == '__main__':
    assert clock_angle("02:30") == 105, "02:30"
    assert clock_angle("13:42") == 159, "13:42"
    assert clock_angle("01:42") == 159, "01:42"
    assert clock_angle("01:43") == 153.5, "01:43"
    assert clock_angle("00:00") == 0, "Zero"
    assert clock_angle("12:01") == 5.5, "Little later"
    assert clock_angle("18:00") == 180, "Opposite"
