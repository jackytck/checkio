#!/opt/local/bin/python3.3
from unicodedata import normalize#, category


def checkio(s):
    return normalize('NFD', s).encode('ascii', 'ignore').decode() or s
    #return ''.join([c for c in normalize('NFD', s) if category(c) != 'Mn'])

if __name__ == '__main__':
    assert checkio(u"préfèrent") == u"preferent"
    assert checkio(u"loài trăn lớn") == u"loai tran lon"
    print(checkio(u"完好無缺loài trăn lớ"))
    print('Done')
