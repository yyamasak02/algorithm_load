def main():
    # a = list(map(int, input().split()))
    # b, c = map(int, input().split())
    # n = int(input())
    # s = input()
    x, y, z = map(int, input().split())
    q = (x - (z * y)) % (z - 1)
    if x >= z * y and q == 0:
        print("Yes")
    else:
        print("No")
    return


if __name__ == "__main__":
    main()
