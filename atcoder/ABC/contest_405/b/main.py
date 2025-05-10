def check_all(d, m):
    for num in range(1, m+1):
        if (not d.get(num)) or (d[num] == 0):
            return False
    return True


n,m = map(int, input().split())
A = list(map(int, input().split()))
d = {}
for a in A:
    if not d.get(a):
        d[a] = 0
    d[a] += 1
res = 0
while (check_all(d, m)):
    a = A.pop(-1)
    d[a] -= 1
    res += 1


print(res)
