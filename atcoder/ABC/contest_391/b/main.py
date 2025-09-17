def solve(s: list[str], t: list[str], i: int, j: int, m: int, n: int) -> bool:
    for k in range(m):
        for ll in range(m):
            if i + k >= n:
                return False
            if j + ll >= n:
                return False
            if s[i + k][j + ll] != t[k][ll]:
                return False
    return True


n, m = map(int, input().split())
s = ["" for _ in range(n)]
t = ["" for _ in range(m)]
for i in range(n):
    s[i] = input()
for i in range(m):
    t[i] = input()
for i in range(n):
    for j in range(n):
        if s[i][j] == t[0][0]:
            if solve(s, t, i, j, m, n) is True:
                print(f"{i+1} {j+1}")
                exit(0)
