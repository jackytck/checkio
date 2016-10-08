#!/opt/local/bin/python3.3
import re
from math import radians, sin, cos, acos

R = 6371


def latlong(s):
    s = re.findall('(\d+)°(\d+)′(\d+)″([NESW])', s)
    d = {'N': 1, 'E': 1, 'S': -1, 'W': -1}
    return map(lambda x: radians(d[x[3]] * (int(x[0]) + int(x[1]) / 60
                                 + int(x[2]) / 3600)), s)


def distance(first, second):
    p1, l1 = latlong(first)
    p2, l2 = latlong(second)
    return acos(sin(p1) * sin(p2) + cos(p1) * cos(p2) * cos(l1 - l2)) * R


if __name__ == '__main__':
    def almost_equal(checked, correct, significant_digits=1):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(
        distance(u"51°28′48″N 0°0′0″E", u"46°12′0″N, 6°9′0″E"), 739.2), "From Greenwich to Geneva"
    assert almost_equal(
        distance(u"90°0′0″N 0°0′0″E", u"90°0′0″S, 0°0′0″W"), 20015.1), "From South to North"
    assert almost_equal(
        distance(u"33°51′31″S, 151°12′51″E", u"40°46′22″N 73°59′3″W"), 15990.2), "Opera Night"
