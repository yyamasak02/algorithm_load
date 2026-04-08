# a = list(map(int, input().split()))
# b = int(input())
# c = input()
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_d = {}

for i in a:
    if i in a_d:
        a_d[i] += 1
    else:
        a_d[i] = 1
for i in b:
    if i in a_d and a_d[i] != 0:
        a_d[i] -= 1

result = []
for key, count in a_d.items():
    if count > 0:
        result.extend([key] * count)

print(" ".join(map(str, result)))
