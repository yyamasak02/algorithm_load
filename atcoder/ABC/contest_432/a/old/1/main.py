def main():
    x = int(input())
    a = list(map(int, list(map(str, x))))
    a.sort()
    print(a)
    return


if __name__ == "__main__":
    main()
