#!/usr/bin/python
def checkio(number):
    k = int(number ** 0.5)
    table = [x * (x + 1) / 2 for x in range(1, k + 1)]
    candidates = [([], -1)]

    #just try all
    for i in range(k - 1):
        for j in range(i + 1, k):
            if sum(table[i:j + 1]) == number:
                candidates.append((table[i:j + 1], j - i))

    candidates.sort(key = lambda x: x[1])
    return candidates[-1][0]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(64) == [15, 21, 28], "1st example"
    assert checkio(371) == [36, 45, 55, 66, 78, 91], "2nd example"
    assert checkio(225) == [105, 120], "3rd example"
    assert checkio(882) == [], "4th example"
