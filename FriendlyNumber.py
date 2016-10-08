#!/opt/local/bin/python3.3


def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    """
    Format a number as friendly text, using common suffixes.
    """
    p, unit = 0, ''
    while abs(number) >= base ** (p + 1) and p < len(powers) - 1:
        p += 1
    number /= base ** p
    if number:
        unit = powers[p]
    if not decimals:
        number = int(number)
    return '%.*f%s%s' % (decimals, number, unit, suffix)

if __name__ == '__main__':
    assert friendly_number(102) == '102', '102'
    assert friendly_number(10240) == '10k', '10k'
    assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
    assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
    assert friendly_number(1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'
