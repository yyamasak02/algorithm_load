def main():
    a, b, c = map(int, input().split())
    if b <= c:
        if b > a or a > c:
            print("Yes")
        else:
            print("No")
    else:
        if b <= a and a <= 24:
            print("No")
        elif 0 <= a and a <= c:
            print("No")
        else:
            print("Yes")
    return


if __name__ == "__main__":
    main()
