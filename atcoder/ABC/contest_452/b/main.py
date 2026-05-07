def main():
    H, W = map(int, input().split())
    for y in range(1, H + 1):
        for x in range(1, W + 1):
            signal = "."
            if y == 1 or y == H:
                signal = "#"
            elif x == 1 or x == W:
                signal = "#"
            print(signal, end="")
        print()
    return


if __name__ == "__main__":
    main()
