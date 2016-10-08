#!/opt/local/bin/python3.3
from collections import defaultdict


class Friends:
    def __init__(self, connections):
        self.connections = defaultdict(set)
        for con in connections:
            a, b = tuple(con)
            self.connections[a].add(b)
            self.connections[b].add(a)

    def add(self, connection):
        a, b = tuple(connection)
        if a in self.connections[b]:
            return False
        self.connections[a].add(b)
        self.connections[b].add(a)
        return True

    def remove(self, connection):
        a, b = list(connection)
        if a in self.connections[b]:
            self.connections[a].remove(b)
            self.connections[b].remove(a)
            return True
        return False

    def names(self):
        return {k for k, v in self.connections.items() if v}

    def connected(self, name):
        return self.connections[name]


if __name__ == '__main__':
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
