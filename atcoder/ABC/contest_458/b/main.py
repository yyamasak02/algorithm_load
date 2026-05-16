def main():
    H, W = map(int, input().split())
    DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for i in range(H):
        tmp = []
        for j in range(W):
            counter = 0
            for dx, dy in DIRS:
                ddx = dx + i
                ddy = dy + j
                if ddx < 0 or H <= ddx:
                    continue
                if ddy < 0 or W <= ddy:
                    continue
                counter += 1
            tmp.append(counter)
        print(*tmp)
    return


if __name__ == "__main__":
    main()
