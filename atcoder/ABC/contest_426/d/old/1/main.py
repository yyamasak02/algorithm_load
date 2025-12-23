def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        s = input()
        col = [0, 0]
        tmp = s[0]
        counter = 1
        c0 = 1 if tmp == "0" else 0
        for c in s[1:]:
            if c == "0":
                c0 += 1
            if tmp != c:
                tmp_i = int(tmp)
                col[tmp_i] = max(col[tmp_i], counter)
                tmp = c
                counter = 0
            counter += 1
        tmp_i = int(tmp)
        col[tmp_i] = max(col[tmp_i], counter)
        print(min(2 * (c0 - col[0]) + n - c0, 2 * (n - c0 - col[1]) + c0))
    return


if __name__ == "__main__":
    main()
