def main():
    N = int(input())
    rows = []
    for _ in range(N):
        x, y = map(int, input().split())
        rows.append((x, y))
    rows.sort(key=lambda x: x[0])
    minimum_y = 10**9
    minimum_x = 10**9
    result = 0
    for row in rows:
        if row[0] <= minimum_x or row[1] <= minimum_y:
            result += 1
        minimum_x = min(minimum_x, row[0])
        minimum_y = min(minimum_y, row[1])
    print(result)
    return


if __name__ == "__main__":
    main()
