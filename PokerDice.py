#!/opt/local/bin/python3.3
from itertools import combinations
from collections import Counter


HANDS = (
    'one pair',
    'two pair',
    'three of a kind',
    'flush',
    'straight',
    'full house',
    'four of a kind',
    'five of a kind',
)


def keep_score(keep, used):
    score = [0 for _ in range(8)]
    cnt = Counter(keep)
    cv = Counter(cnt.values())
    cs = Counter([x[1] for x in keep])
    digi = {x[0] for x in keep}
    mv = max(cnt.values())

    if mv >= 2:
        score[0] = 10
    if cv[2] == 2 or (cv[2] and cv[3]) or max(cnt.values()) >= 4:
        score[1] = 20
    if mv >= 3:
        score[2] = 30
    if max(cs.values()) == 5:
        score[3] = 40
    if digi == {'9', 'T', 'J', 'Q', 'K'} or digi == {'A', 'K', 'Q', 'J', 'T'}:
        score[4] = 50
    if cv[2] and cv[3]:
        score[5] = 60
    if mv >= 4:
        score[6] = 70
    if mv == 5:
        score[7] = 80

    for u in used:
        score[HANDS.index(u)] = 0

    ms = max(score)
    if ms:
        return ms + 5 - len(keep), HANDS[ms // 10 - 1], keep
    else:
        for h in HANDS:
            if h not in used:
                return 0, h, keep


def all_keep(rolls):
    for i in range(1, len(rolls) + 1):
        for keep in combinations(rolls, i):
            yield keep


def poker_dice(rolls, scores):
    used = [k for k, v in scores.items() if v]
    maxi = max(keep_score(keep, used) for keep in all_keep(rolls[-1]))
    return maxi[1] if len(rolls) == 3 or len(maxi[2]) == 5 else maxi[2]


poker_dice([['9S', 'TH', '9S', 'JS', 'AS']], {'two pair': 4})
poker_dice([['9S', 'JS', '9S', 'JS', 'AS']], {'two pair': 4})
poker_dice([['9S', '9S', '9S', '9S', 'AS']], {'two pair': 4})
poker_dice([['9S', '9S', '9S', '9S', '9S']], {'two pair': 4})
poker_dice([['9S', '9S', '9S', 'JS', 'AS']], {'two pair': 4})
poker_dice([['9S', '9S', '9S', 'JS', 'JS']], {'two pair': 4})
poker_dice([['9S', 'TH', 'JS', 'QH', 'KH']], {'two pair': 4})
poker_dice([['TH', 'JS', 'KH', 'TH', 'KH']], {'one pair': 2, 'two pair': 0, 'three of a kind': 6, 'flush': 0})
