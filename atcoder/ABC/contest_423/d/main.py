from collections import deque
import heapq

n, k = map(int, input().split())
d: deque[tuple] = deque()
for i in range(n):
    a, b, c = map(int, input().split())
    d.append((a, b, c, i))
ans = [0 for i in range(n)]

tmp = 0
dt = 0
ll: list[tuple] = []
sorted_flag = False
while d:
    while len(d) != 0 and tmp + d[0][2] <= k:
        sorted_flag = False
        e = d.popleft()
        ans[e[3]] = e[0] if dt < e[0] else dt
        heapq.heappush(ll, (ans[e[3]] + e[1], e[2]))
        tmp += e[2]
    if ll:
        tmp_e = heapq.heappop(ll)
        dt = tmp_e[0]
        tmp -= tmp_e[1]
print(*ans, sep="\n")
