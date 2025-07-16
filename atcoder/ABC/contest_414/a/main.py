n,l,r = map(int, input().split())

ans = 0
for i in range(n):
    x,y = map(int, input().split())
    if l >= x and r <= y:
        ans += 1
print(ans)