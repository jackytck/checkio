#!/opt/local/bin/python3.3
def to_seconds(time):
    t = [int(x) for x in time.split(':')]
    return t[0] * 3600 + t[1] * 60 + t[2]


def to_string(time):
    return '%02d:%02d:%02d' % (time / 3600, time % 3600 / 60, time % 60)


def error_factor(description):
    unit = {'hours': 3600, 'hour': 3600, 'minutes': 60,
            'minute': 60, 'seconds': 1, 'second': 1}
    d = description.split(' ')
    return 1 + int(d[0]) * unit[d[1]] / int(d[3]) / unit[d[4]]


def broken_clock(starting_time, wrong_time, error_description):
    s = to_seconds(starting_time)
    w = to_seconds(wrong_time)
    f = error_factor(error_description)
    return to_string(s + (w - s) / f)


if __name__ == "__main__":
    assert broken_clock('00:00:00', '00:00:15', '+5 seconds at 10 seconds') == '00:00:10', "First example"
    assert broken_clock('06:10:00', '06:10:15', '-5 seconds at 10 seconds') == '06:10:30', 'Second example'
    assert broken_clock('13:00:00', '14:01:00', '+1 second at 1 minute') == '14:00:00', 'Third example'
    assert broken_clock('01:05:05', '04:05:05', '-1 hour at 2 hours') == '07:05:05', 'Fourth example'
    assert broken_clock('00:00:00', '00:00:30', '+2 seconds at 6 seconds') == '00:00:22', 'Fifth example'
