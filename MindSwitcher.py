#!/opt/local/bin/python3.3
def mind_switcher(journal):
    # array form
    robots = {}
    for r1, r2 in journal:
        robots[r1], robots[r2] = robots.get(r2, r2), robots.get(r1, r1)

    # disjoint cycles
    cycles, visit = [], set()
    for r1, r2 in robots.items():
        if r1 not in visit:
            cycle, c = [], r1
            while c not in visit:
                visit.add(c)
                cycle.append(c)
                c = robots[c]
            if len(cycle) > 1:
                cycles.append(cycle)

    # invert each cycle
    x, y = 'nikola', 'sophia'
    inverse = []
    for cycle in cycles:
        for c in cycle[:-1]:
            inverse.append({x, c})
        k = cycle[-1]
        inverse.extend([{y, k}, {x, k}, {y, cycle[0]}])
    if len(cycles) % 2:
        inverse.append({x, y})

    return inverse


if __name__ == '__main__':
    def check_solution(func, data):
        robots = {"nikola": "nikola", "sophia": "sophia"}
        switched = []
        for pair in data:
            switched.append(set(pair))
            r1, r2 = pair
            robots[r1], robots[r2] = robots.get(r2, r2), robots.get(r1, r1)

        result = func(data)
        if not isinstance(result, (list, tuple)) or not all(isinstance(p, set) for p in result):
            print("The result should be a list/tuple of sets.")
            return False
        for pair in result:
            if len(pair) != 2:
                print(1, "Each pair should contain exactly two names.")
                return False
            r1, r2 = pair
            if not isinstance(r1, str) or not isinstance(r2, str):
                print("Names must be strings.")
                return False
            if r1 not in robots.keys():
                print("I don't know '{}'.".format(r1))
                return False
            if r2 not in robots.keys():
                print("I don't know '{}'.".format(r2))
                return False
            if set(pair) in switched:
                print("'{}' and '{}' already were switched.".format(r1, r2))
                return False
            switched.append(set(pair))
            robots[r1], robots[r2] = robots[r2], robots[r1]
        for body, mind in robots.items():
            if body != mind:
                print("'{}' has '{}' mind.".format(body, mind))
                return False
        return True

    assert check_solution(mind_switcher, ({"scout", "super"},))
    assert check_solution(mind_switcher, ({'hater', 'scout'}, {'planer', 'hater'}))
    assert check_solution(mind_switcher, ({'scout', 'driller'}, {'scout', 'lister'},
                                          {'hater', 'digger'}, {'planer', 'lister'}, {'super', 'melter'}))
    assert check_solution(mind_switcher, ({'melter', 'digger'}, {'melter', 'planer'}, {'digger', 'planer'}))
