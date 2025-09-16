n = int(input())
ll = list(map(int, input().split()))
first, second = None, None
for i in range(n):
    if ll[i] == 1:
        if first is None:
            first = i
        second = i
print(second - first if second is not None else 0)
