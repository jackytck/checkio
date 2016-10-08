#!/opt/local/bin/python3.3
def nCr(n, r):
    top, val = n, 1
    while (top > (n - r)):
        val *= top
        top -= 1
    n = 1
    while (n < r + 1):
        val /= n
        n += 1
    return val


def probability(n, s, p):
    if p == 0:
        return 0
    r = min((p - n) // s, n) + 1
    c = sum((-1)**k * nCr(n, k) * nCr(p - s*k - 1, n - 1) for k in range(r))
    return c / (s**n)

if __name__ == '__main__':
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert(almost_equal(probability(1, 2, 0), 0))
    assert(almost_equal(probability(2, 6, 3), 0.0556)), "Basic example"
    assert(almost_equal(probability(2, 6, 4), 0.0833)), "More points"
    assert(almost_equal(probability(2, 6, 7), 0.1667)), "Maximum for two 6-sided dice"
    assert(almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
    assert(almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
    assert(almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
    assert(almost_equal(probability(10, 10, 50), 0.0375)), "Many dice, many sides"
