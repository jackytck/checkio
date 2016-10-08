#!/usr/bin/python
import string, re

def checkio(url):
    unres = {}
    for c in '%s%s-._~' % (string.ascii_letters, string.digits):
        unres[hex(ord(c)).split('x')[1]] = c.lower()

    def norm(m):
        m = m.group(1)
        return '%s' % unres.get(m, '%%%s' % m.upper())

    url = url.lower()#rule 1
    url = re.sub(r'%([\da-f]{2})', norm, url)#rule 2, 3
    url = re.sub(r':80/', '/', url)#rule 4
    url = re.sub(r':80$', '', url)#rule 4
    url = re.sub(r'\/\.(?!\.)', '', url)# /./././
    p, con = re.compile(r'\/[\w\-\.~]+\/\.\.'), True
    while con:# /../../../
        url, con = re.subn(p, '', url)

    return url

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"Http://Www.Checkio.org") == \
        "http://www.checkio.org", "1st rule"
    assert checkio(u"http://www.checkio.org/%cc%b1bac") ==\
        "http://www.checkio.org/%CC%B1bac", "2nd rule"
    assert checkio(u"http://www.checkio.org/task%5F%31") == \
        "http://www.checkio.org/task_1", "3rd rule"
    assert checkio(u"http://www.checkio.org:80/home/") == \
        "http://www.checkio.org/home/", "4th rule"
    assert checkio(u"http://www.checkio.org/task/./1/../2/././name") == \
        "http://www.checkio.org/task/2/name", "5th rule"
    print('First set of tests done')
    #checkio(u'http://www.abc.com/abc/def/../..')
    #checkio(u'http://www.abc.com/abc/././././def/../..')
    #checkio(u'http://www.abc.com/abc/././././a_def/../..')
