def main():
    already = set()
    dirs = [(0, 0), (1, 0), (0, 1), (1, 1)]
    n, m = map(int, input().split())
    result = 0
    for i in range(m):
        r, c = map(int, input().split())
        nothing = False
        for dx, dy in dirs:
            if (r + dx, c + dy) in already:
                nothing = True
                break
        if nothing is False:
            result += 1
            for dx, dy in dirs:
                already.add((r + dx, c + dy))
    print(result)
    return


if __name__ == "__main__":
    main()
