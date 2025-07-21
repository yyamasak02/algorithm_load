from dataclasses import dataclass
from collections import deque


@dataclass
class Pair:
    num: int
    count: int


q = int(input())
queue = deque()
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        c, x = query[1], query[2]
        queue.append(Pair(num=x, count=c))
    else:
        k = query[1]
        ans = 0
        while queue and queue[0].count <= k:
            # print("before: ", queue)
            nokori = queue.popleft()
            ans += nokori.num * nokori.count
            k -= nokori.count
            # print("after: ", queue)
        # print(k)
        if k > 0 and queue:
            ans += queue[0].num * k
            queue[0].count -= k
        print(ans)
