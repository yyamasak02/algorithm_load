def main():
    n = int(input())
    min_x, max_x, min_y, max_y = 10**9, 0, 10**9, 0
    for _ in range(n):
        r, c = map(int, input().split())
        min_x = min(min_x, r)
        max_x = max(max_x, r)
        min_y = min(min_y, c)
        max_y = max(max_y, c)
    result = (max(max_y - min_y, max_x - min_x) + 1) // 2
    print(result)
    return


if __name__ == "__main__":
    main()
