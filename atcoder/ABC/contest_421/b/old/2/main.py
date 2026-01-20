def main():
    x, y = map(int, input().split())
    ai = None
    for i in range(3, 11):
        target = str(x + y)
        ai = int("".join(list(target)[::-1]))
        x = y
        y = ai
    print(ai)
    return


if __name__ == "__main__":
    main()
