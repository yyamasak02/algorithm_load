from collections import deque

n = int(input())
d = {}
ans = [False for i in range(n + 1)]
visited = [False for i in range(n + 1)]
start_list = deque()
for i in range(n):
    a, b = map(int, input().split())
    if a == b and a == 0:
        ans[i + 1] = True
        start_list.append(i + 1)
    else:
        if a not in d:
            d[a] = set()
        d[a].add(i + 1)
        if b not in d:
            d[b] = set()
        d[b].add(i + 1)

while start_list:
    i = start_list.popleft()
    if visited[i] is True:
        continue
    else:
        visited[i] = True
        ans[i] = True
        if i not in d:
            continue
        for j in d[i]:
            if visited[j] is True:
                continue
            start_list.append(j)
print(ans.count(True))
