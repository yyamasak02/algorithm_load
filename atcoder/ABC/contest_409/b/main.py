n = int(input())
a = list(map(int, input().split()))
ans = 0
a.sort(reverse=True)

for i in range(100, 0, -1):
    for j in range(n):
        if a[j] < i:
            j -= 1
            break
    if (j+1) >= i:
        print(i)
        exit()
print(ans)