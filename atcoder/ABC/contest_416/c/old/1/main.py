# 単語を辞書順に並べ、X番目を単語の組み合わせで決定する。
n, k, x = map(int, input().split())
d = [input() for _ in range(n)]
d.sort()

ans = []
for i in range(k):
    block = n ** (k - 1 - i)
    idx = (x - 1) // block
    ans.append(d[idx])
    x = x - idx * block

print("".join(ans))
