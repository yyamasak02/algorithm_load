n,q = map(int, input().split())
x = list(map(int, input().split()))
ans = [0 for _ in range(n+1)]
answer = []
for i in range(q):
    if x[i] == 0:
        res = min(ans[1:])
        for j in range(1, n+1):
            if ans[j] == res:
                ans[j] += 1
                answer.append(j)
                break
    else:
        ans[x[i]] += 1
        answer.append(x[i])
print(" ".join(map(str, answer)))