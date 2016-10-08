#!/opt/local/bin/python3.3
def neighbours(i, j):
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx != 0 or dy != 0:
                yield i + dx, j + dy


def neighbour_count(universe, cell):
    return sum(x in universe for x in neighbours(*cell))


def tick(universe):
    life, dead = set(), set()
    # will live
    for cell in universe:
        num = neighbour_count(universe, cell)
        if num == 2 or num == 3:
            life.add(cell)
        dead |= {x for x in neighbours(*cell) if x not in universe}
    # will born
    for cell in dead:
        if neighbour_count(universe, cell) == 3:
            life.add(cell)
    return life


def life_counter(state, tick_n):
    life = {(i, j) for i, x in enumerate(state) for j, y in enumerate(x) if y}
    for _ in range(tick_n):
        life = tick(life)
    return len(life)


if __name__ == '__main__':
    assert life_counter(((0, 1, 0, 0, 0, 0, 0),
                         (0, 0, 1, 0, 0, 0, 0),
                         (1, 1, 1, 0, 0, 0, 0),
                         (0, 0, 0, 0, 0, 1, 1),
                         (0, 0, 0, 0, 0, 1, 1),
                         (0, 0, 0, 0, 0, 0, 0),
                         (1, 1, 1, 0, 0, 0, 0)), 4) == 15, "Example"
    assert life_counter(((0, 1, 0, 0, 0, 0, 0),
                         (0, 0, 1, 0, 0, 0, 0),
                         (1, 1, 1, 0, 0, 0, 0),
                         (0, 0, 0, 0, 0, 1, 1),
                         (0, 0, 0, 0, 0, 1, 1),
                         (0, 0, 0, 0, 0, 0, 0),
                         (1, 1, 1, 0, 0, 0, 0)), 15) == 14, "Little later"
    assert life_counter(((0, 1, 0),
                         (0, 0, 1),
                         (1, 1, 1)), 50) == 5, "Glider"
    assert life_counter(((1, 1, 0, 1, 1),
                         (1, 1, 0, 1, 1),
                         (0, 0, 0, 0, 0),
                         (1, 1, 0, 1, 1),
                         (1, 1, 0, 1, 1)), 100), "Stones"
