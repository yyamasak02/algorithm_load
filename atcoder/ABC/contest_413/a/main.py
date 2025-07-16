n, m = map(int, input().split())
a = list(map(int, input().split()))

if sum(a) <= m:
    print("Yes")
else:
    print("No")