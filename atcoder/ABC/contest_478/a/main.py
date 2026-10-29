def main():
    N, M = map(int, input().split())
    quotient, mod = M // N, M % N
    for _ in range(N):
        if mod > 0:
            print(quotient + 1)
            mod -= 1
        else:
            print(quotient)
    return


if __name__ == "__main__":
    main()
