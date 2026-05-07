def main():
    alp_numbers_by_digits = [[set() for _ in range(11)] for _ in range(11)]
    N = int(input())
    targets = []
    for i in range(N):
        targets.append(tuple(map(int, input().split())))
    M = int(input())
    strings = []
    for i in range(M):
        s = input()
        size = len(s)
        for j in range(size):
            alp_numbers_by_digits[size][j + 1].add(s[j])
        strings.append((s, size))
    for s, size in strings:
        is_ok = True
        if size != N:
            print("No")
            continue
        for index, target in enumerate(targets):
            char = s[index]
            if char not in alp_numbers_by_digits[target[0]][target[1]]:
                is_ok = False
                break
        if is_ok is True:
            print("Yes")
        else:
            print("No")
    return


if __name__ == "__main__":
    main()
