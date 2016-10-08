#!/opt/local/bin/python3.3
from collections import defaultdict


def build_graph(segments):
    g = defaultdict(list)
    for s in segments:
        a, b = s[:2], s[-2:]
        g[a].append(b)
        g[b].append(a)
    return g


def is_bridge(g, s):
    a, b = s[:2], s[-2:]
    stack = [(a, a)]
    visit = defaultdict(bool)
    visit[a + b] = True
    visit[b + a] = True
    while stack:
        p, t = stack.pop()
        if p + t in visit:
            continue
        if t == b:
            return False
        visit[p + t] = True
        visit[t + p] = True
        for c in g[t]:
            if t + c not in visit:
                stack.append((t, c))
    return True


def remove_edge(g, s):
    a, b = s[:2], s[-2:]
    g[a].remove(b)
    g[b].remove(a)


def draw(segments):
    g = build_graph(segments)

    # Euler Path Theorem
    odd = sum(len(e) & 1 for e in g.values())
    if odd and odd != 2:
        return ()
    start = next(iter(g.keys()))
    if odd:
        start = [k for k, v in g.items() if len(v) & 1][0]

    # Fleury's algorithm
    route = [start]
    while sum(g.values(), []):
        cur = route[-1]
        for c in g[cur]:
            s = cur + c
            if len(g[cur]) == 1 or not is_bridge(g, s):
                route.append(c)
                remove_edge(g, s)
                break
    return route


if __name__ == '__main__':
    def checker(func, in_data, is_possible=True):
        user_result = func(in_data)
        if not is_possible:
            if user_result:
                print("How did you draw this?")
                return False
            else:
                return True
        if len(user_result) < 2:
            print("More points please.")
            return False
        data = list(in_data)
        for i in range(len(user_result) - 1):
            f, s = user_result[i], user_result[i + 1]
            if (f + s) in data:
                data.remove(f + s)
            elif (s + f) in data:
                data.remove(s + f)
            else:
                print("The wrong segment {}.".format(f + s))
                return False
        if data:
            print("You forgot about {}.".format(data[0]))
            return False
        return True

    assert checker(draw,
                   {(1, 2, 1, 5), (1, 2, 7, 2), (1, 5, 4, 7), (4, 7, 7, 5)}), "Example 1"
    assert checker(draw,
                   {(1, 2, 1, 5), (1, 2, 7, 2), (1, 5, 4, 7),
                    (4, 7, 7, 5), (7, 5, 7, 2), (1, 5, 7, 2), (7, 5, 1, 2)},
                   False), "Example 2"
    assert checker(draw,
                   {(1, 2, 1, 5), (1, 2, 7, 2), (1, 5, 4, 7), (4, 7, 7, 5),
                    (7, 5, 7, 2), (1, 5, 7, 2), (7, 5, 1, 2), (1, 5, 7, 5)}), "Example 3"
