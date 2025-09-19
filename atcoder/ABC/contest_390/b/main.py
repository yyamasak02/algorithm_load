n = int(input())
a = list(map(int, input().split()))

if len(a) == 2:
    print("Yes")
else:
    for i in range(n - 2):
        if a[i] * a[i + 2] != a[i + 1] * a[i + 1]:
            print("No")
            break
    else:
        print("Yes")
