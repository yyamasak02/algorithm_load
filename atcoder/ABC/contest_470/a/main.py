def main():
    N = int(input())
    for i in range(N):
        if (i + 1) % 3 == 0:
            print("Fizz")
        else:
            print(i + 1)
    return


if __name__ == "__main__":
    main()
