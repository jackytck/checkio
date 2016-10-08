#!/opt/local/bin/python3.3
def convert(code):
    bin_code = bin(code)[2:].zfill(6)[::-1]
    return [[int(bin_code[j + i * 3]) for i in range(2)] for j in range(3)]


LETTERS_NUMBERS = list(map(convert,
                           [1, 3, 9, 25, 17, 11, 27, 19, 10, 26,
                            5, 7, 13, 29, 21, 15, 31, 23, 14, 30,
                            37, 39, 62, 45, 61, 53]))
CAPITAL_FORMAT = convert(32)
NUMBER_FORMAT = convert(60)
PUNCTUATION = {',': convert(2), '-': convert(18), '?': convert(38),
               '!': convert(22), '.': convert(50), '_': convert(36),
               ' ': convert(0)}


def braille_page(text: str):
    # build symbol list
    symbols = []
    for c in text:
        if c.isalpha():
            if c.isupper():
                symbols.append(CAPITAL_FORMAT)
            symbols.append(LETTERS_NUMBERS[ord(c.lower()) - ord('a')])
        elif c.isdigit():
            symbols.append(NUMBER_FORMAT)
            symbols.append(LETTERS_NUMBERS[(int(c) - 1) % 10])
        else:
            symbols.append(PUNCTUATION[c])

    # initialize page
    rows = [symbols[i:i+10] for i in range(0, len(symbols), 10)]
    w = len(rows[0]) * 3 - 1
    h = len(rows) * 4 - 1
    page = [[0 for i in range(w)] for j in range(h)]

    # fill page by each symbol
    for i, s in enumerate(symbols):
        x = (i // len(rows[0])) * 4
        y = (i * 3) % (w + 1)
        for u in range(3):
            for v in range(2):
                page[x + u][y + v] = s[u][v]

    return page


if __name__ == '__main__':
    def checker(func, text, answer):
        result = func(text)
        return tuple(tuple(x) for x in answer) == tuple(tuple(row) for row in result)

    assert checker(braille_page, "hello 1st World!", (
        (1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1),
        (1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1),
        (0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0))
    ), "Example"
    assert checker(braille_page, "42", [
        [0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0],
        [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0],
        [1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0]]), "42"
    assert checker(braille_page, "CODE", [
        (0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1),
        (0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0)]
    ), "CODE"
