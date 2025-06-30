n = int(input())
a = list(map(int, input().split()))
a.insert(0, 0)

columtive_a = [0]
for i in range(1, n):
    columtive_a.append(columtive_a[i-1] + a[i])
ans = []
for i in range(n-1):
    res = []
    for j in range(i+1, n):
        res.append(columtive_a[j] - columtive_a[i])
    ans.append(res)
for i in range(n-1):
    print(" ".join(map(str, ans[i])))
