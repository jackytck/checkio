#!/opt/local/bin/python3.3
from collections import deque, defaultdict


def find_chains(family, couples):
    chains = []
    size = len(family)
    edges = defaultdict(set)
    for a in family:
        for b in family - {a}:
            if {a, b} not in couples:
                edges[a].add(b)
                edges[b].add(a)
    q = deque([[family.pop()]])
    # all posible chains with constraints #1 and #2
    while q:
        chain = q.popleft()
        # valid chain
        if len(chain) == size and chain[0] in edges[chain[-1]]:
            history = set(zip(chain, chain[1:] + [chain[0]]))
            chains.append((tuple(chain), history))
        else:
            # next possible recipients
            for e in edges[chain[-1]]:
                # not in current year
                if e not in chain:
                    q.append(chain + [e])

    print(len(chains))

    max_chain_seq = []
    # store posible chains for next year
    edges = defaultdict(list)
    for c1, h1 in chains:
        print(c1)
        for c2, h2 in chains:
            if c1 != c2 and not h1 & h2:
                edges[c1].append((c2, h2))
                edges[c2].append((c1, h1))
        break

    for e in edges:
        print('##', e)
    exit(-1)
    # (current chain list, accumulated history set)
    q = deque([([c], h) for c, h in chains])
    while q:
        seq, hist = q.popleft()
        end = True
        for ec, eh in edges[tuple(seq[-1])]:
            # constraint #3
            if not hist & eh:
                end = False
                q.append((seq + [ec], hist | eh))
        if end:
            if len(seq) > len(max_chain_seq):
                max_chain_seq = seq

    return max_chain_seq

if __name__ == '__main__':
    def checker(function, family, couples, total):
        user_result = function(family.copy(), tuple(c.copy() for c in couples))
        if (not isinstance(user_result, (list, tuple)) or
                any(not isinstance(chain, (list, tuple)) for chain in user_result)):
            return False
        if len(user_result) < total:
            return False
        gifted = set()
        for chain in user_result:
            if set(chain) != family or len(chain) != len(family):
                return False
            for f, s in zip(chain, list(chain[1:]) + [chain[0]]):
                if {f, s} in couples:
                    return False
                if (f, s) in gifted:
                    return False
                gifted.add((f, s))
        return True

    assert checker(find_chains, 
             {'Loraine', 'Leah', 'Jenifer', 'Russell', 'Benjamin', 'Todd', 'Maryanne', 'Penny',
                 'Matthew'}, ({'Loraine', 'Benjamin'}, {'Leah', 'Matthew'}, {'Todd', 'Jenifer'}), 6)
    assert checker(find_chains, {'Gary', 'Jeanette', 'Hollie'},
                   ({'Gary', 'Jeanette'},), 0), "Three of us"
    assert checker(find_chains, {'Curtis', 'Lee', 'Rachel', 'Javier'},
                   ({'Rachel', 'Javier'}, {'Curtis', 'Lee'}), 2), "Pairs"
    assert checker(find_chains, {'Philip', 'Sondra', 'Mary', 'Selena', 'Eric', 'Phyllis'},
                   ({'Philip', 'Sondra'}, {'Eric', 'Mary'}), 4), "Pairs and Singles"
