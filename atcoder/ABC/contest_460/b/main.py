def main():
    T = int(input())
    for _ in range(T):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())
        d = (x2 - x1) ** 2 + (y2 - y1) ** 2
        def_sub = abs(r1 - r2) ** 2
        def_sum = (r1 + r2) ** 2
        if def_sum < d or d < def_sub:
            print("No")
        else:
            print("Yes")
    return


if __name__ == "__main__":
    main()
