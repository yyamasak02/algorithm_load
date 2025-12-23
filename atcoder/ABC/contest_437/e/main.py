def main():
    n = int(input())
    pairs = []
    p = [0]
    # number, parent, additional, layer
    d = {i: [0, 0, 0, 0] for i in range(n + 1)}
    for i in range(1, n + 1):
        x, y = map(int, input().split())
        d[i][0] = i
        d[i][1] = x
        d[i][2] = y
        d[i][3] = d[x][3] + 1
    print(d)
    return


if __name__ == "__main__":
    main()
