def main():
    p, q = map(int, input().split())
    x, y = map(int, input().split())
    if p > x or x > p + 99:
        print("No")
    elif q > y or y > q + 99:
        print("No")
    else:
        print("Yes")
    return


if __name__ == "__main__":
    main()
