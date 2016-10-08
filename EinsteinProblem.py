#!/opt/local/bin/python3.3
from collections import deque, defaultdict

KEY = ('number', 'color', 'nationality', 'beverage', 'cigarettes', 'pet')
LABELS = ('1', '2', '3', '4', '5',
          'blue', 'green', 'red', 'white', 'yellow',
          'Brit', 'Dane', 'German', 'Norwegian', 'Swede',
          'beer', 'coffee', 'milk', 'tea', 'water',
          'Rothmans', 'Dunhill', 'Pall Mall', 'Winfield', 'Marlboro',
          'cat', 'bird', 'dog', 'fish', 'horse')


# propagate edges within same group
def connect(matrix, i, j):
    visit = defaultdict(bool)
    q = deque([i])
    while q:
        f = q.popleft()
        if visit[f]:
            continue
        visit[f] = True
        matrix[f][i] = matrix[i][f] = matrix[f][j] = matrix[j][f] = 1
        for k, c in enumerate(matrix[f]):
            if c:
                q.append(k)


# fill remaining entry in permutation matrix
def fill_trivial(matrix):
    for x in range(6):
        for y in range(x):
            left, right = set(), set()
            for i in range(5):
                for j in range(5):
                    u, v = x * 5 + i, y * 5 + j
                    if matrix[u][v]:
                        left.add(i)
                        right.add(j)
            if len(left) == 4:
                s = set(range(5))
                i, j = (s - left).pop(), (s - right).pop()
                u, v = x * 5 + i, y * 5 + j
                connect(matrix, u, v)
                return True


def answer(relations, question):
    m = [[1 if i == j else 0 for j in range(30)] for i in range(30)]
    for d in relations:
        connect(m, *map(LABELS.index, d.split('-')))
    # assume trivial solution exists
    while fill_trivial(m):
        pass
    q, k = question.split('-')
    i, j = LABELS.index(q), KEY.index(k) * 5
    return LABELS[j + m[i][j:].index(1)]


if __name__ == '__main__':
    assert answer(('Norwegian-Dunhill', 'Marlboro-blue', 'Brit-3',
                   'German-coffee', 'beer-white', 'cat-water',
                   'horse-2', 'milk-3', '4-Rothmans',
                   'dog-Swede', 'Norwegian-1', 'horse-Marlboro',
                   'bird-Brit', '4-green', 'Winfield-beer',
                   'Dane-blue', '5-dog', 'blue-horse',
                   'yellow-cat', 'Winfield-Swede', 'tea-Marlboro'),
                  'fish-color') == 'green'  # What is the color of the house where the Fish lives?
    assert answer(('Norwegian-Dunhill', 'Marlboro-blue', 'Brit-3',
                   'German-coffee', 'beer-white', 'cat-water',
                   'horse-2', 'milk-3', '4-Rothmans',
                   'dog-Swede', 'Norwegian-1', 'horse-Marlboro',
                   'bird-Brit', '4-green', 'Winfield-beer',
                   'Dane-blue', '5-dog', 'blue-horse',
                   'yellow-cat', 'Winfield-Swede', 'tea-Marlboro'),
                  'tea-number') == '2'  # What is the number of the house where tea is favorite beverage?
    assert answer(('Norwegian-Dunhill', 'Marlboro-blue', 'Brit-3',
                   'German-coffee', 'beer-white', 'cat-water',
                   'horse-2', 'milk-3', '4-Rothmans',
                   'dog-Swede', 'Norwegian-1', 'horse-Marlboro',
                   'bird-Brit', '4-green', 'Winfield-beer',
                   'Dane-blue', '5-dog', 'blue-horse',
                   'yellow-cat', 'Winfield-Swede', 'tea-Marlboro'),
                  'Norwegian-beverage') == 'water'  # What is the favorite beverage of the Norwegian man?

def pprint(matrix):
    for i, x in enumerate(matrix):
        for j, y in enumerate(x):
            print(y, end=', ')
            if j % 5 == 4:
                print('   ', end='')
        print()
        if i % 5 == 4:
            print()

