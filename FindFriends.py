#!/opt/local/bin/python3.3
from collections import defaultdict, deque


def check_connection(network, first, second):
    edges = defaultdict(list)
    for n in network:
        a, b = n.split('-')
        edges[a].append(b)
        edges[b].append(a)

    q = deque([first])
    visit = defaultdict(bool)
    while q:
        f = q.popleft()
        if visit[f]:
            continue
        if f == second:
            return True
        visit[f] = True
        for c in edges[f]:
            q.append(c)
    return False


if __name__ == '__main__':
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
