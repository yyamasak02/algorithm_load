n = int(input())
a = list(map(int, input().split()))

result = 0
count = {}
for i in range(n - 1, -1, -1):
    target = i + 1 + a[i]
    if target in count:
        result += count[target]
    current_val = (i + 1) - a[i]
    if current_val in count:
        count[current_val] += 1
    else:
        count[current_val] = 1
print(result)
