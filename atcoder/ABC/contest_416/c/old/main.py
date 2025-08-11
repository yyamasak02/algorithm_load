import itertools

n, k, x = map(int, input().split())
s = [input() for _ in range(n)]
s.sort()
lst = []
for p in itertools.product(s, repeat=k):
    lst.append("".join(p))
print(lst[x - 1])
