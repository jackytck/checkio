#!/opt/local/bin/python3.3
import functools
from collections import defaultdict, deque


def all_verts(rings):
    return sorted(functools.reduce(set.union, rings))


def get_child(rings, x):
    for r in rings:
        if x in r:
            a, b = r
            yield a if a != x else b


def frozen(rings):
    return frozenset(frozenset(r) for r in rings)


def connected_chain(verts, rings):
    visit = defaultdict(bool)
    for v in verts:
        if not visit[v]:
            comp = {v}
            q = deque([v])
            while q:
                f = q.popleft()
                if visit[f]:
                    continue

                visit[f] = True
                for c in get_child(rings, f):
                    comp.add(c)
                    q.append(c)

            yield frozenset(comp), frozen(filter(lambda x: x <= comp, rings))


def discard_ring(verts, rings, v):
    vs = [r for r in verts if r != v]
    rs = [x for x in rings if v not in x]
    return vs, rs


def keep_ring(verts, rings, v):
    broke = set(get_child(rings, v))
    vs = [r for r in verts if r not in broke]
    rs = [x for x in rings if not x & broke]
    return vs, rs


@functools.lru_cache(maxsize=None)
def max_rings(verts, rings):
    if not rings:
        return len(verts)

    verts = list(verts)
    rings = [set(r) for r in set(rings)]
    v = verts[-1]

    discard = sum(map(lambda x: max_rings(*x),
                      list(connected_chain(*discard_ring(verts, rings, v)))))
    keep = sum(map(lambda x: max_rings(*x),
                   list(connected_chain(*keep_ring(verts, rings, v)))))
    return max(discard, keep)


def break_rings(rings):
    verts = all_verts(rings)
    return len(verts) - sum(map(lambda x: max_rings(*x),
                                connected_chain(verts, rings)))


if __name__ == '__main__':
    assert break_rings(({1, 2}, {2, 3}, {4, 5}, {5, 6}, {4, 6})) == 3, "example"
    assert break_rings(({1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {4, 6})) == 3, "example"
    assert break_rings(({1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4})) == 3, "All to all"
    assert break_rings(({5, 6}, {4, 5}, {3, 4}, {3, 5}, {3, 6})) == 2, "Chain"
    assert break_rings(({8, 9}, {1, 9}, {1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {8, 7})) == 5, "Long chain"

    big = [[4, 6], [4, 12], [2, 4], [12, 5], [12, 14], [12, 7], [9, 13], [1, 10], [9, 18], [17, 19], [4, 13], [2, 20], [10, 14], [11, 12], [11, 15], [16, 2], [8, 5], [3, 12], [17, 11], [10, 19]]
    big = tuple(set(x) for x in big)
    assert break_rings(big) == 8, 'big'
