#!/usr/bin/python
def checkio(number):
    s = ('', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
    ss = ('ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen')
    sss = ('', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety')
    if number == 0:
        return 'zero'
    elif number == 1000:
        return 'one thousand'
    else:
        ret = s[number/100]
        if number >= 100:
            ret += ' hundred'
        d2 = (number % 100) / 10
        d3 = (number % 100) % 10
        if d2 == 1:
            if ret:
                ret += ' '
            ret += ss[d3]
            return ret
        elif d2 > 1:
            if ret:
                ret += ' '
            ret += sss[d2]
        if d3 != 0:
            if ret:
                ret += ' '
            ret += s[d3]
    return ret

if __name__ == '__main__':
    assert checkio(4) == 'four', "First"
    assert checkio(133) == 'one hundred thirty three', "Second"
    assert checkio(12)=='twelve', "Third"
    assert checkio(101)=='one hundred one', "Fifth"
    assert checkio(212)=='two hundred twelve', "Sixth"
    assert checkio(40)=='forty', "Seventh, forty - it is correct"

    print 'All ok'
