#!/opt/local/bin/python3.3
# -*- coding: utf-8 -*-
import math
from fractions import Fraction


def gauss(A):
    # martin-thoma.com/solving-linear-equations-with-gaussian-elimination
    n = len(A)

    for i in range(0, n):
        # Search for maximum in this column
        maxEl = abs(A[i][i])
        maxRow = i
        for k in range(i+1, n):
            if abs(A[k][i]) > maxEl:
                maxEl = abs(A[k][i])
                maxRow = k

        # Swap maximum row with current row (column by column)
        for k in range(i, n+1):
            tmp = A[maxRow][k]
            A[maxRow][k] = A[i][k]
            A[i][k] = tmp

        # Make all rows below this one 0 in current column
        for k in range(i+1, n):
            c = -A[k][i]/A[i][i]
            for j in range(i, n+1):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] += c * A[i][j]

    # Solve equation Ax=b for an upper triangular matrix A
    x = [0 for i in range(n)]
    for i in range(n-1, -1, -1):
        x[i] = A[i][n]/A[i][i]
        for k in range(i-1, -1, -1):
            A[k][n] -= A[k][i] * x[i]
    return x


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def trans(m):
    return list(map(list, zip(*m)))


def mult(a, b):
    return trans([[dot(r, c) for r in a] for c in trans(b)])


def predict_ghost(values, n=10):
    if (max(values) - min(values)) < 3:
        return sum(values) / n

    A = [[Fraction(i ** j) for j in range(n)] for i in range(1, n + 1)]
    for i in range(n):
        for j in range(1, n - 4):
            A[i][-j] = Fraction(math.sin(j * (i + 1)))
    AT = trans(A)
    ATA = mult(AT, A)

    y = [v for v in values]
    for i, v in enumerate(values):
        y[i] = Fraction(dot(AT[i], values))

    aug = trans(ATA)
    aug.append(y)
    aug = trans(aug)

    b = gauss(aug)
    x = [(n + 1) ** i for i in range(n)]
    for i in range(1, n - 4):
        x[-i] = Fraction(math.sin(i * (n + 1)))
    p = dot(b, x)
    return p.numerator / p.denominator


if __name__ == '__main__':
    from random import choice, random
    import math
    TESTS_QUANTITY = 30
    SCORE_DIST = 0.1

    def generate_formula(prob_x=0.5, prob_bracket=0.2, prob_trig=0.25):
        formula = "x"
        for _ in range(15):
            operation = choice(["+", "-", "*", "/"])
            formula += operation
            if random() < prob_x:
                formula += "x"
            else:
                formula += str(round(random() * 10, 3))
            if random() < prob_bracket:
                formula = "(" + formula + ")"
            if random() < prob_trig:
                formula = "math." + choice(["sin", "cos"]) + "(" + formula + ")"
        return formula

    def calculate_score(f):
        score = 0
        add = 0
        for count in range(TESTS_QUANTITY):
            formula_x = generate_formula()
            values = []
            for x in range(1, 12):
                try:
                    i = round(eval(formula_x), 3)
                    values.append(i)
                except OverflowError:
                    count -= 1
                    break
            else:
                if abs(max(values) - min(values)) < 1:
                    count -= 1
                else:
                    score_distance = (max(values) - min(values)) * SCORE_DIST
                    user_result = f(values[:-1])
                    distance = abs(user_result - values[-1])
                    if distance < score_distance:
                        add = round(100 * ((score_distance - distance) / score_distance))
                        score += add
                    else:
                        add = 0
                    print('sd: %.2f d: %.2f score: %d' % (score_distance, distance, add))
        print("Total score: {}".format(score))
        return score

    calculate_score(predict_ghost)
