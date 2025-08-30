n, m = map(int, input().split())
a = []
scores = [0 for i in range(n)]
for i in range(n):
    s = input()
    a.append(s)
for i in range(m):
    zero = 0
    one = 0
    zeros = []
    ones = []
    for j in range(n):
        if a[j][i] == "0":
            zero += 1
            zeros.append(j)
        else:
            one += 1
            ones.append(j)
    if zero == 0:
        for k in ones:
            scores[k] += 1
    elif one == 0:
        for k in zeros:
            scores[k] += 1
    elif zero < one:
        for k in zeros:
            scores[k] += 1
    else:
        for k in ones:
            scores[k] += 1

res = max(scores)
saikyo = []
for i in range(n):
    if scores[i] == res:
        saikyo.append(str(i + 1))
print(" ".join(saikyo))
