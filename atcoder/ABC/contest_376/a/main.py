n,c = map(int, input().split())
t = list(map(int, input().split()))
prev_eat = t[0]
ans = 1
for i in range(1,n):
    if t[i] - prev_eat >= c:
        ans += 1
        prev_eat = t[i]
print(ans)