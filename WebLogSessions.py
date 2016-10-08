#!/usr/bin/python
from datetime import datetime

SESSION_IDLE = 30 * 60

#assume simple x.y domain
def url_parse(url):
    return '.'.join(url.split('//')[1].split('/')[0].split('.')[-2:])

def date_parse(date):
    return int(datetime.strptime(date, '%Y-%m-%d-%H-%M-%S').strftime('%s'))

def checkio(log_text):
    log = []
    for l in log_text.split('\n'):
        a, b, c = l.split(';;')
        log.append(['%s;;%s' % (b.lower(), url_parse(c)), date_parse(a)])
    log.sort(key=lambda x: x[1])

    ret, d = [], {}
    for l in log:
        k, t = l
        last = d.get(k, None)
        if last:
            a, b, c = d[k]
            if t - c > SESSION_IDLE:
                ret.append((k, a, b))
                d[k] = (1, 1, t)
            else:
                d[k] = (a + t - c, b + 1, t)
        else:
            d[k] = (1, 1, t)

    for k, v in d.iteritems():
        ret.append((k, v[0], v[1]))
    return '\n'.join(['%s;;%d;;%d' % x for x in sorted(ret)])

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert (checkio(
"""2013-01-01-01-00-00;;Name;;http://checkio.org/task
2013-01-01-01-02-00;;name;;http://checkio.org/task2
2013-01-01-01-31-00;;Name;;https://admin.checkio.org
2013-01-01-03-00-00;;Name;;http://www.checkio.org/profile
2013-01-01-03-00-01;;Name;;http://example.com
2013-02-03-04-00-00;;user2;;http://checkio.org/task
2013-01-01-03-11-00;;Name;;http://checkio.org/task""")
==
"""name;;checkio.org;;661;;2
name;;checkio.org;;1861;;3
name;;example.com;;1;;1
user2;;checkio.org;;1;;1"""), "Example"
