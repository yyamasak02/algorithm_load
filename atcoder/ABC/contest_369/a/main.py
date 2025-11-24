def main():
    a, b = map(int, input().split())
    if a == b:
        print(1)
    else:
        bigger = max(a, b)
        smaller = min(a, b)
        if (bigger - smaller) % 2 == 0:
            print(3)
        else:
            print(2)
    return


if __name__ == "__main__":
    main()
