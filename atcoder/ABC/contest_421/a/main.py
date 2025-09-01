n = int(input())
d = {}
for i in range(n):
    d[str(i + 1)] = input()
x, y = input().split()
if d[x] == y:
    print("Yes")
else:
    print("No")
