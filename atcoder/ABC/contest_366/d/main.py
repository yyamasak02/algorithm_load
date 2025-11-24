def main():
    n = int(input())
    # col_list[x][y][z]
    col_list = [[[] for _ in range(n)] for _ in range(n)]
    ll = []
    for i in range(n):
        tmp = []
        for j in range(n):
            tmp.append(list(map(int, input().split())))
        ll.append(tmp)
    return


if __name__ == "__main__":
    main()
