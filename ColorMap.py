#!/opt/local/bin/python3.3
import copy
from collections import defaultdict


def color_graph(graph, coloring=defaultdict(int)):
    if not graph:
        return (1,)
    answer = [coloring[i] for i in range(len(coloring)) if coloring[i]]
    if len(graph) == len(answer):
        return answer

    for node, childs in graph.items():
        if not coloring[node]:
            used = [coloring[c] for c in childs if coloring[c]]
            for color in range(1, 5):
                if color not in used:
                    trial = copy.deepcopy(coloring)
                    trial[node] = color
                    answer = color_graph(graph, trial)
                    if answer:
                        return answer


def color_map(region):
    graph = defaultdict(set)
    for i, _ in enumerate(region):
        for j, country in enumerate(_):
            for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                px, py = i + dx, j + dy
                if 0 <= px < len(region) and 0 <= py < len(_):
                    neighs = region[px][py]
                    if neighs != country:
                        graph[country].add(neighs)
                        graph[neighs].add(country)

    return color_graph(graph)


if __name__ == '__main__':
    NEIGHS = ((-1, 0), (1, 0), (0, 1), (0, -1))
    COLORS = (1, 2, 3, 4)
    ERROR_NOT_FOUND = "Didn't find a color for the country {}"
    ERROR_WRONG_COLOR = "I don't know about the color {}"

    def checker(func, region):
        user_result = func(region)
        if not isinstance(user_result, (tuple, list)):
            print("The result must be a tuple or a list")
            return False
        country_set = set()
        for i, row in enumerate(region):
            for j, cell in enumerate(row):
                country_set.add(cell)
                neighbours = []
                if j < len(row) - 1:
                    neighbours.append(region[i][j + 1])
                if i < len(region) - 1:
                    neighbours.append(region[i + 1][j])
                try:
                    cell_color = user_result[cell]
                except IndexError:
                    print(ERROR_NOT_FOUND.format(cell))
                    return False
                if cell_color not in COLORS:
                    print(ERROR_WRONG_COLOR.format(cell_color))
                    return False
                for n in neighbours:
                    try:
                        n_color = user_result[n]
                    except IndexError:
                        print(ERROR_NOT_FOUND.format(n))
                        return False
                    if cell != n and cell_color == n_color:
                        print("Same color neighbours.")
                        return False
        if len(country_set) != len(user_result):
            print("Excess colors in the result")
            return False
        return True

    checker(color_map, ((0,),))
    checker(color_map, ((0, 0, 0), (0, 1, 1), (0, 0, 2)))
    checker(color_map, [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 6, 0, 8, 10, 0, 1, 0],
        [0, 1, 0, 5, 0, 7, 9, 0, 1, 0],
        [0, 1, 0, 0, 4, 0, 0, 0, 1, 0],
        [0, 1, 0, 3, 0, 2, 2, 0, 1, 0],
        [0, 1, 0, 3, 0, 2, 11, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ])
    checker(color_map, ((11,0,0,0,0,0,7,0),(0,0,0,0,0,0,7,0),(0,0,4,4,4,0,7,0),(0,0,0,0,0,0,0,0),(0,0,1,0,1,0,0,0),(5,5,1,2,1,6,6,0),(0,0,1,0,1,0,0,0),(0,0,0,0,0,0,0,0),(0,0,3,3,3,0,8,0),(0,0,10,10,9,0,8,0),(0,0,0,10,9,9,8,0)))
