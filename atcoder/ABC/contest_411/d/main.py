import heapq
from collections import defaultdict

n, m = map(int, input().split())
g = defaultdict(list)
for _ in range(m):
    a, b, w = map(int, input().split())
    g[a].append((b, w))
xor_values = [set() for _ in range(n + 1)]
xor_values[1].add(0)
pq = [(0, 1)]
while pq:
    current_xor, v = heapq.heappop(pq)
    for next_v, weight in g[v]:
        new_xor = current_xor ^ weight
        if new_xor in xor_values[next_v]:
            continue
        xor_values[next_v].add(new_xor)
        heapq.heappush(pq, (new_xor, next_v))
if not xor_values[n]:
    print(-1)
else:
    print(min(xor_values[n]))
