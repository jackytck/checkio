#!/usr/bin/python
#import Queue

class PriorityQueue:
    def __init__(self):
        self._q = []

    def put(self, item):
        self._q.append(item)

    def empty(self):
        return len(self._q) == 0

    def get(self):
        if not self.empty():
            self._q.sort(key=lambda x: x[0])
            ret = self._q[0]
            self._q = self._q[1:]
            return ret

def checkio(data):
    ret = -1
    w, h = len(data), len(data[0])

    for i, x in enumerate(data[0]):
        visit = {}
        #pq = Queue.PriorityQueue()
        pq = PriorityQueue()
        pq.put((x, (0, i)))

        while not pq.empty():
            d, top = pq.get()
            if visit.get(top, False):
                continue
            visit[top] = True
            if top[0] == w - 1:
                ret = min(ret, d) if ret != -1 else d

            for u, v in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                s, t = top[0] + u, top[1] + v
                if 0<= s < w and 0 <= t < h and not visit.get((s, t), False):
                    pq.put((d + data[s][t], (s, t)))
    return ret

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[1, 1, 1, 1, 0, 1, 1],
                    [1, 1, 1, 1, 0, 0, 1],
                    [1, 1, 1, 1, 1, 0, 1],
                    [1, 1, 0, 1, 1, 0, 1],
                    [1, 1, 0, 1, 1, 1, 1],
                    [1, 0, 0, 1, 1, 1, 1],
                    [1, 0, 1, 1, 1, 1, 1]]) == 2, "1st example"
    assert checkio([[0, 0, 0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 0, 1, 0, 1, 1],
                    [1, 0, 0, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0, 0, 0]]) == 3, "2nd example"
    assert checkio([[1, 1, 1, 1, 1, 0, 1, 1],
                    [1, 0, 1, 1, 1, 0, 1, 1],
                    [1, 0, 1, 0, 1, 0, 1, 0],
                    [1, 0, 1, 1, 1, 0, 1, 1],
                    [0, 0, 1, 1, 0, 0, 0, 0],
                    [1, 0, 1, 1, 1, 1, 1, 1],
                    [1, 0, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 0, 1, 1, 1, 1]]) == 2, "3rd example"
