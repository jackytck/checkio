#!/opt/local/bin/python3.3
from collections import deque, defaultdict


def check(enemy, player):
    total = 0
    for p in player:
        for e in enemy:
            if p > e:
                total += 1
            elif p < e:
                total -= 1
    return total > 0


def child(dice, maxi):
    s = set()
    mutate = [d for d in dice]
    for i, x in enumerate(dice):
        for j, y in enumerate(dice):
            if i != j:
                if x > 1 and y <= maxi:
                    mutate[i] -= 1
                    mutate[j] += 1
                    s.add(tuple(sorted(mutate)))
                    mutate[i] += 1
                    mutate[j] -= 1
    return s


def winning_die(enemy):
    m = min(18, max(enemy))
    visit = defaultdict(bool)
    q = deque([tuple(enemy)])
    cnt = 0
    while q and cnt < 10000:
        f = q.popleft()
        h = hash(f)
        if visit[h]:
            continue
        if check(enemy, f):
            return f
        visit[h] = True
        for c in child(f, m):
            q.append(c)
        cnt += 1
    return []

if __name__ == '__main__':
    def check_solution(func, enemy):
        player = func(enemy)
        total = 0
        for p in player:
            for e in enemy:
                if p > e:
                    total += 1
                elif p < e:
                    total -= 1
        return total > 0

    assert check_solution(winning_die, [3, 3, 3, 3, 6, 6]), "Threes and Sixes"
    assert check_solution(winning_die, [4, 4, 4, 4, 4, 4]), "All Fours"
    assert check_solution(winning_die, [1, 1, 1, 4]), "Unities and Four"
    assert winning_die([1, 2, 3, 4, 5, 6]) == [], "All in row -- No die"
