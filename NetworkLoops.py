#!/opt/local/bin/python3.3
from collections import deque, defaultdict


def find_cycle(connections):
    ans = []
    edges = defaultdict(list)
    for a, b in connections:
        edges[a].append(b)
        edges[b].append(a)

    r = connections[0][0]
    q = deque([[r]])
    while q:
        seq = q.popleft()
        i = seq.index(seq[-1])
        j = len(seq) - i
        if j > 1:
            if j > len(ans):
                ans = seq[i:]
        else:
            for e in edges[seq[-1]]:
                if len(seq) == 1 or e != seq[-2]:
                    q.append(seq + [e])
    return ans

if __name__ == '__main__':
    def checker(function, connections, best_size):
        user_result = function(connections)
        if not isinstance(user_result, (tuple, list)) or not all(isinstance(n, int) for n in user_result):
            print("You should return a list/tuple of integers.")
            return False
        if not best_size and user_result:
            print("Where did you find a cycle here?")
            return False
        if not best_size and not user_result:
            return True
        if len(user_result) < best_size + 1:
            print("You can find a better loop.")
            return False
        if user_result[0] != user_result[-1]:
            print("A cycle starts and ends in the same node.")
            return False
        if len(set(user_result)) != len(user_result) - 1:
            print("Repeat! Yellow card!")
            return False
        for n1, n2 in zip(user_result[:-1], user_result[1:]):
            if (n1, n2) not in connections and (n2, n1) not in connections:
                print("{}-{} is not exist".format(n1, n2))
                return False
        return True, "Ok"
    
    assert checker(find_cycle, 
                   ((1, 2), (2, 3), (3, 4), (4, 5), (5, 7), (7, 6),
                    (8, 5), (8, 4), (1, 5), (2, 4), (1, 8)), 6), "Example"
    assert checker(find_cycle, 
                   ((1, 2), (2, 3), (3, 4), (4, 5), (5, 7), (7, 6), (8, 4), (1, 5), (2, 4)), 5), "Second"
    assert checker(find_cycle,
            [tuple(x) for x in [[6, 8], [3, 8], [3, 4], [3, 5], [2, 8], [3, 9], [2, 7], [4, 7], [5, 8], [5, 10], [7, 9], [2, 6],
                      [5, 6], [7, 8], [6, 7], [1, 3], [9, 10], [1, 10], [3, 6], [4, 10], [6, 9], [2, 3], [3, 10],
                      [1, 5], [1, 7], [4, 5], [2, 4], [8, 9], [2, 9], [4, 8], [2, 10], [2, 5], [8, 10], [1, 6]]], 10), 'third'
    assert checker(find_cycle,
            ((4,8),(1,6),(1,5),(1,3),(1,11),(5,6),(4,10),(6,11),(4,7),(5,12),(9,11),(8,9),(3,9),(2,3)), 6), 'forth'
