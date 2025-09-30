n = int(input())
a = list(map(int, input().split()))
d = [0] * (n + 1)
free_indexes = []
error_flag = False

for i in range(n):
    if a[i] == -1:
        free_indexes.append(i)
        continue
    d[a[i]] += 1
    if d[a[i]] >= 2:
        error_flag = True
        break
if error_flag is True:
    print("No")
else:
    for i in range(1, n + 1):
        if d[i] == 0:
            k = free_indexes.pop(0)
            a[k] = i
    print("Yes")
    print(*a)
