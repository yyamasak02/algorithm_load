def rev(x: int) -> int:
    x_list = list(str(x))
    x = 0
    for index, v in enumerate(x_list):
        x += int(v) * (10**index)
    return x


x, y = map(int, input().split())
a = [x, y]
for i in range(2, 10):
    a.append(rev(a[i - 2] + a[i - 1]))
print(a[-1])
