def main():
    N, M = map(int, input().split())
    rows, columns = [-1] * N, [-1] * N
    for _ in range(M):
        r, c = map(int, input().split())
        r -= 1
        c -= 1
        if rows[r] == -1 and columns[c] == -1:
            rows[r] = c
            columns[c] = r
        elif rows[r] == -1:
            rows[r] = c
            rows[columns[c]] = -1
            columns[c] = r
        elif columns[c] == -1:
            columns[c] = r
            columns[rows[r]] = -1
            rows[r] = c
        else:
            pre_r = rows[r]
            pre_c = columns[c]
            columns[pre_r] = -1
            rows[pre_c] = -1
            rows[r] = c
            columns[c] = r
    result = len([i for i in rows if i >= 0])
    print(result)
    return


if __name__ == "__main__":
    main()
