#!/usr/bin/python
def to_seconds(t):
    t = [int(x) for x in t.split(':')]
    return t[0] * 3600 + t[1] * 60 + t[2]

def parse_desc(d):
    unit = {'hours': 3600, 'hour': 3600, 'minutes': 60, 'minute': 60, 'seconds': 1, 'second': 1}
    d = d.split(' ')
    return int(d[0]) * unit[d[1]], int(d[3]) * unit[d[4]]

def to_str(t):
    t = int(t)
    return '%02d:%02d:%02d' % (t / 3600, t % 3600 / 60, t % 60)

def checkio(data):
    start, end, description = data
    start, end, (n, m) = to_seconds(start), to_seconds(end), parse_desc(description)
    correct = start + (end - start) / (1 + float(n) / m)
    return to_str(correct)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert checkio(['00:00:00', '00:00:15', '+5 seconds at 10 seconds']) == '00:00:10', "First example"
    assert checkio(['06:10:00', '06:10:15', '-5 seconds at 10 seconds']) == '06:10:30', 'Second example'
    assert checkio(['13:00:00', '14:01:00', '+1 second at 1 minute']) == '14:00:00', 'Third example'
    assert checkio(['01:05:05', '04:05:05', '-1 hour at 2 hours']) == '07:05:05', 'Fourth example'
    assert checkio(['00:00:00', '00:00:30', '+2 seconds at 6 seconds']) == '00:00:22', 'Fifth example'
