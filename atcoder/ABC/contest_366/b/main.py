def main():
    n = int(input())
    strs = []
    max_length = 0
    for i in range(n):
        s = input()
        strs.append(s)
        max_length = max(max_length, len(s))
    ver_strs = [["*"] * n for _ in range(max_length)]
    for i in range(max_length):
        for j in range(n - 1, -1, -1):
            if len(strs[j]) <= i:
                continue
            ver_strs[i][n - 1 - j] = strs[j][i]
    for i in range(max_length):
        modori = None
        for j in range(n - 1, -1, -1):
            if ver_strs[i][j] != "*":
                modori = j
                break
        if modori is not None:
            for j in range(n - 1, modori, -1):
                ver_strs[i][j] = ""
    for c in ver_strs:
        print("".join(c))
    return


if __name__ == "__main__":
    main()
