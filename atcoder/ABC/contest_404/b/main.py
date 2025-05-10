
def lotate(s):
    n = len(s)
    m = len(s[0])
    res = []
    for j in range(m):
        tmp = ""
        for i in range(n):
            tmp += s[n - 1 - i][j]
        res.append(tmp)
    return res

def same_numbers(s, t):
    n = len(s)
    m = len(s[0])
    same = 0
    for i in range(n):
        for j in range(m):
            if s[i][j] == t[i][j]:
                same += 1
    return same


if __name__ == "__main__":
    n = int(input())
    s = []
    for i in range(n):
        tmp = input()
        s.append(tmp)
    t = []
    for i in range(n):
        tmp = input()
        t.append(tmp)
    ans = 10**9
    for i in range(4):
        diff = int(n*n) - same_numbers(s, t)
        ans = min(ans, diff + i)
        s = lotate(s)
    print(ans)



