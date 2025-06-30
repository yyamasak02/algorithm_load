n = int(input())
res = 0
for i in range(n):
    a, b = map(int, input().split())
    if a < b:
        res += 1
print(res)