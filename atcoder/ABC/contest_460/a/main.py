def main():
    N, M = map(int, input().split())
    counter = 0
    while M != 0:
        M = N % M
        counter += 1
    print(counter)
    return


if __name__ == "__main__":
    main()
