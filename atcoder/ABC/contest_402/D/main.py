n, m = map(int, input().split())
from collections import defaultdict

group_dict = defaultdict(int)
for _ in range(m):
    a, b = map(int, input().split())
    length = b - a
    center = (a + b) % n  # 中心点位置をmodでずらす
    group_dict[(length, center)] += 1
print(group_dict)
ans = (m * (m - 1)) // 2
for value in group_dict.values():
    ans -= (value * (value - 1)) // 2

print(ans)
