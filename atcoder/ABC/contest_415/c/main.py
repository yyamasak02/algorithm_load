t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    s = "0" + s
    s_len = 1 << n
    res: list[bool] = [False for i in range(1 << n)]
    res[0] = True
    for i in range(1 << n):
        if res[i] is False:
            continue
        for j in range(n):
            if i & (1 << j):
                continue
            next_index = i | (1 << j)
            if s[next_index] == "0":
                res[next_index] = True
    print("Yes" if res[(1 << n) - 1] is True else "No")
