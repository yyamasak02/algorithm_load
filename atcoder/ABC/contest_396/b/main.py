N,K = map(int,input().split())
a = list(map(int,input().split()))
res = 1
for i in range(N):
    res *= a[i]
    if res >= 10**K:
        res = 1
print(res)