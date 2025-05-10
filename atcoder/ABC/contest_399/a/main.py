s = int(input())
a = input()
b = input()

res = 0
for i in range(s):
    if a[i] != b[i]:
        res += 1
print(res)