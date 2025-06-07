n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort(reverse=True)
b.sort(reverse=True)
new = 0
b_num = 0

for i in range(n):
    omotya_size = a[i]
    if b_num >= n-1 and new == 0:
        new = omotya_size
        break
    elif b_num >= n-1:
        new = -1
        break
    hako_size = b[b_num]
    if (omotya_size > hako_size) and new == 0:
        new = omotya_size
    elif (omotya_size > hako_size):
        new = -1
        break
    else:
        b_num += 1
print(new)